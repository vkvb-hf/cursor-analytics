# Observe - Config-Based Monitoring System

A config-driven monitoring system for tracking metrics and detecting anomalies using multiple alert rules.

## Overview

Observe monitors daily metrics across different dimensions and alerts when values deviate from expected patterns:

* Compares current day vs historical baselines (same weekday last week, 4-week averages)
* Supports multiple alert rules: missing data detection, large deviations, and statistical anomalies
* Suppresses redundant alerts via hierarchy (e.g., if country-level alerts, don't also alert on country+region)
* Tracks alert recovery with follow-up notifications

## How It Works

**One notebook does everything**: `observe_daily.py`

1. Syncs config from Workspace to DBFS
2. Creates tables if they don't exist
3. Checks if monitor config changed (hash of metrics, dimensions, source)  
   * **Changed** → backfill 720 days  
   * **Unchanged** → refresh last 30 days
4. Computes metrics with hierarchy roll-ups
5. Evaluates alert rules (zero_when_expected, large_deviation, auto_threshold)
6. Deduplicates via hierarchy suppression
7. Checks yesterday's alerts for recovery (follow_up)
8. Sends Slack notifications with diagnosis

## Alert Rules

Observe supports four alert rules, each independently configurable per monitor:

### 1. Zero When Expected (Active by Default)

Alerts when today has **zero data** but the same weekday had data for the past N weeks.

```yaml
zero_when_expected:
  enabled: true
  lookback_weeks: 4        # Check last 4 same-weekdays
  min_expected_weeks: 3    # Alert if ≥3 of those weeks had data
  min_denominator: 30      # Minimum volume to consider "had data"
```

**Use case**: Catches complete outages or data pipeline failures.

### 2. Large Deviation (Active by Default)

Alerts when metric drops more than a threshold percentage vs the 4-week same-weekday average.

```yaml
large_deviation:
  enabled: true
  direction: decrease      # Only alert on drops (not increases)
  threshold_pct: 50        # Alert if >50% drop
  lookback_weeks: 4        # Compare to 4-week average
  min_denominator: 30      # Minimum volume
```

**Use case**: Catches major degradations without statistical calibration.

### 3. Auto-Threshold (Disabled by Default)

Statistical anomaly detection using auto-calibrated thresholds from historical data.

```yaml
auto_threshold:
  enabled: false           # Currently disabled
  comparison: same_weekday
  calibration_days: 365
  target_flag_rate: 0.03   # Calibrate so ~3% of historical days would flag
  min_denominator: 30
  min_effective_volume: 10
  severity_map:
    critical: 3.0
    warning: 1.0
```

**How it works**:
1. Pairs each day with same weekday 7 days prior
2. Computes residuals and their standard deviation
3. Finds k such that |residual| > k × std for ~`target_flag_rate` of days
4. Alerts when today's deviation exceeds calibrated threshold

**Use case**: Fine-grained anomaly detection with automatic threshold tuning.

### 4. Follow-Up (Active by Default)

Checks yesterday's alerts and reports recovery status.

```yaml
follow_up:
  enabled: true
```

**Statuses**:
- `recovered`: Yesterday's alert no longer triggers today
- `still_degraded`: Alert still active today

Follow-ups are posted as **thread replies** to yesterday's Slack alert.

---

## Quick Start

### Prerequisites

* Databricks workspace with access to your data tables
* (Optional) Slack bot token for notifications

### Step 1: Clone/Fork the Repository

```bash
git clone https://github.com/your-org/cursor-analytics.git
cd cursor-analytics/observe
```

### Step 2: Create Your Config Files

Create three YAML files in `observe/config/`:

**sources.yml** - Define your data source:

```yaml
version: 1

sources:
  - name: my_events
    database: my_database
    table: events_table
    date_column: event_date
    columns:
      - name: region
      - name: category
      - name: status
      # Column with custom expression (optional)
      - name: category_group
        expression: "CASE WHEN category IN ('A','B') THEN 'group1' ELSE 'group2' END"
    filters: []
    diagnosis:
      error_column: error_reason
      failure_filter: "status = 'failed'"
```

**metrics.yml** - Define what to measure (uses PySpark expressions):

```yaml
version: 1

metrics:
  - name: success_rate
    source: my_events
    type: ratio
    filter: "F.col('category') == 'web'"
    numerator: "F.sum(F.when(F.col('status') == 'success', 1).otherwise(0))"
    denominator: "F.sum(F.when(F.col('status').isin('success', 'failed'), 1).otherwise(0))"
    description: "Success rate for web events"
    increase_is_good: true
    is_p0: true
    is_ratio: true
    team_ownership: "Platform Team"
```

**monitors.yml** - Configure alerting:

```yaml
version: 1

defaults:
  historical_lookback_days: 720
  refresh_lookback_days: 30
  alert_channels:
    - "#my-alerts-channel"

monitors:
  - name: my_monitor
    description: "Monitor success rate by region"
    severity: critical
    metrics:
      - success_rate
    dimensions:
      - [region, category]
    hierarchy:
      - []
      - [region]
      - [region, category]
    rules:
      zero_when_expected:
        enabled: true
        lookback_weeks: 4
        min_expected_weeks: 3
        min_denominator: 30
      large_deviation:
        enabled: true
        direction: decrease
        threshold_pct: 50
        lookback_weeks: 4
        min_denominator: 30
      auto_threshold:
        enabled: false
        comparison: same_weekday
        calibration_days: 365
        target_flag_rate: 0.03
        min_denominator: 30
        min_effective_volume: 10
        severity_map:
          critical: 3.0
          warning: 1.0
      follow_up:
        enabled: true
```

### Step 3: Connect to Databricks

1. Go to Databricks → Repos → Add Repo
2. Connect your repository URL
3. Navigate to `observe/notebooks/observe_daily`

### Step 4: Configure Widget Parameters

Before running, set the widget parameters:

* `output_database`: Your database name (e.g., `my_database`)
* `target_date`: Leave empty for yesterday, or set specific date
* `slack_channel`: (Optional) Override default alert channel

### Step 5: Run the Notebook

Click "Run All" - the notebook will:

1. Create output tables if they don't exist
2. Backfill 720 days of metrics (first run only)
3. Generate alerts for anomalies
4. Send Slack notifications (if configured)

### Step 6: (Optional) Set Up Slack Notifications

1. Create a Slack app with `chat:write` permission
2. Store the bot token in Databricks secrets:
```python
dbutils.secrets.createScope("slack")
dbutils.secrets.put("slack", "pa-bot-token", "<your-bot-token>")
```
3. Or pass via widget: `slack_bot_token`

### Step 7: Schedule Daily Runs

Create a Databricks Job:

* **Task**: Notebook task
* **Path**: `/Repos/<user>/<repo>/observe/notebooks/observe_daily`
* **Schedule**: Daily at your preferred time
* **Cluster**: Any cluster with access to your data

---

## Widget Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| target_date | yesterday | Date to process (YYYY-MM-DD) |
| output_database | payments_hf | Database for output tables |
| metrics_table | observe_metrics_daily | Metrics table name |
| alerts_table | observe_alerts_daily | Alerts table name |
| threads_table | observe_slack_threads | Slack thread tracking table |
| config_path | /dbfs/observe/config | DBFS path for config files |
| state_path | /dbfs/observe/state | DBFS path for state (hashes) |
| slack_bot_token | (empty) | Optional, uses secrets if empty |
| slack_channel | (empty) | Optional, overrides config default |

First run will backfill 720 days of history. Subsequent runs refresh 30 days.

---

## Configuration Reference

### sources.yml - Data Sources

Define the tables and columns to monitor:

```yaml
sources:
  - name: transactions
    database: my_database
    table: transactions_table
    date_column: transaction_date
    columns:
      - name: region
      - name: channel
      - name: status
      # Column with custom SQL expression
      - name: category
        expression: "CASE WHEN nested_struct.field = 'X' THEN 'a' ELSE 'b' END"
    filters:
      - "is_test = FALSE"
    diagnosis:
      error_column: error_reason
      failure_filter: "status = 'failed'"
```

**Column expressions**: Use `expression` to define computed columns from nested structs or CASE WHEN logic.

**Diagnosis block**: Configures error breakdown for alerts
* `error_column`: Column (or SQL expression) containing error reasons
* `failure_filter`: SQL filter for failed records

### metrics.yml - Metric Definitions

Define what to measure using **PySpark expressions**:

```yaml
metrics:
  - name: success_rate
    source: transactions
    type: ratio
    filter: "F.col('channel') == 'web'"
    numerator: "F.sum(F.when(F.col('status') == 'success', 1).otherwise(0))"
    denominator: "F.sum(F.when(F.col('status').isin('success', 'failed'), 1).otherwise(0))"
    description: "Success rate for web transactions"
    increase_is_good: true
    is_p0: true
    is_ratio: true
    team_ownership: "Platform Team"
```

**Fields**:
| Field | Required | Description |
|-------|----------|-------------|
| name | Yes | Unique metric identifier |
| source | Yes | Source name from sources.yml |
| type | Yes | Metric type (currently `ratio`) |
| filter | No | PySpark filter expression |
| numerator | Yes | PySpark aggregation for numerator |
| denominator | Yes | PySpark aggregation for denominator |
| description | No | Human-readable description |
| increase_is_good | No | Whether increases are positive (default: true) |
| is_p0 | No | Mark as P0 metric |
| is_ratio | No | Indicates ratio type |
| team_ownership | No | Owning team |

### monitors.yml - Monitor Configurations

Configure monitoring rules:

```yaml
defaults:
  historical_lookback_days: 720
  refresh_lookback_days: 30
  alert_channels:
    - "#alerts-channel"

monitors:
  - name: transaction_monitor
    description: "Transaction success monitoring"
    severity: critical
    metrics:
      - success_rate
    dimensions:
      - [region, channel]
    hierarchy:
      - []                    # Global
      - [region]              # By region
      - [region, channel]     # Most granular
    rules:
      zero_when_expected:
        enabled: true
        lookback_weeks: 4
        min_expected_weeks: 3
        min_denominator: 30
      large_deviation:
        enabled: true
        direction: decrease
        threshold_pct: 50
        lookback_weeks: 4
        min_denominator: 30
      auto_threshold:
        enabled: false
        comparison: same_weekday
        calibration_days: 365
        target_flag_rate: 0.03
        min_denominator: 30
        min_effective_volume: 10
        severity_map:
          critical: 3.0
          warning: 1.0
      follow_up:
        enabled: true
```

---

## Hierarchy Suppression

Prevents alert spam by suppressing granular alerts when parent dimensions already alert:

```
Hierarchy: [] → [region] → [region, channel]

If "US" alerts at region level:
  ✓ US (active)
  ✗ US/web (suppressed by US)
  ✗ US/mobile (suppressed by US)
```

---

## Diagnosis Feature

For declining alerts, the system queries error breakdowns and posts them as Slack thread replies:

```
🔍 Diagnosis: Success Rate - US/web (-15.2%)

Top error increases vs last week:
• Timeout Error: 4 → 24 (+20)
• Invalid Input: 3 → 16 (+13)
• Server Error: 2 → 7 (+5)

Total failures: 11 → 68 (+518%)
```

---

## Output Tables

### observe_metrics_daily

| Column | Description |
|--------|-------------|
| date | Metric date |
| monitor_name | Monitor that computed this |
| metric_name | Name of the metric |
| dimension_key | e.g., "region,channel" |
| dimension_value | e.g., "US,web" |
| metric_value | Computed ratio (0-1) |
| metric_numerator | Count matching numerator |
| metric_denominator | Total count |
| rolling_7d_avg | 7-day rolling average |
| rolling_7d_prev_avg | Previous 7-day rolling average |
| rolling_7d_change_pct | Week-over-week change |
| yoy_metric_value | Same day last year |
| yoy_change_pct | Year-over-year change |
| historical_avg_denominator | Historical average volume |
| same_weekday_prev | Same weekday last week value |
| same_weekday_residual | Difference from last week |
| calibrated_k | Auto-calibrated k multiplier |
| volume_tier | high/medium/low based on volume |
| source_name | Source that provided data |
| metric_type | Type of metric (ratio) |
| computed_at | Timestamp of computation |

### observe_alerts_daily

| Column | Description |
|--------|-------------|
| date | Alert date |
| monitor_name | Monitor that generated alert |
| metric_name | Metric that triggered |
| dimension_key | Dimension combination |
| dimension_value | Dimension values |
| rule_name | auto_threshold, zero_when_expected, large_deviation, follow_up |
| severity | critical, warning, or info |
| alert_type | anomaly, missing_data, large_drop, recovered, still_degraded |
| current_value | Current metric value |
| expected_value | Expected value (baseline) |
| lower_bound | Lower threshold (auto_threshold only) |
| upper_bound | Upper threshold (auto_threshold only) |
| deviation_pct | % deviation from expected |
| message | Human-readable alert message |
| suppressed | Whether suppressed by hierarchy |
| suppressed_by | Parent dimension that suppressed |
| hierarchy_level | Level in hierarchy (0=global) |
| calibrated_k | Calibrated k multiplier |
| residual_std | Historical residual std |
| denominator_count | Sample size |
| created_at | Timestamp of alert creation |

### observe_slack_threads

| Column | Description |
|--------|-------------|
| date | Alert date |
| channel | Slack channel |
| thread_ts | Thread timestamp for replies |
| message_type | summary or diagnosis |
| created_at | When saved |

---

## Smart Backfill Logic

The notebook tracks a hash of each monitor's **data-affecting** config:

* Metrics (name, source, numerator, denominator, filter)
* Dimensions
* Source table and filters

**Rule thresholds are NOT included** - changing `target_flag_rate` won't trigger a backfill.

| Scenario | Action |
|----------|--------|
| First run | 720 days backfill |
| Add new metric | 720 days backfill |
| Add new dimension | 720 days backfill |
| Change alert threshold | 30 days refresh (no backfill) |
| Normal daily run | 30 days refresh |

---

## Adding New Metrics

1. Edit `config/sources.yml` - add source if needed
2. Edit `config/metrics.yml` - add metric definition
3. Edit `config/monitors.yml` - add metric to a monitor
4. Push to repository
5. Pull in Databricks Repos
6. Run `observe_daily` - it auto-detects the change and backfills

---

## Folder Structure

```
observe/
├── README.md
├── config/
│   ├── sources.yml      # Data source definitions
│   ├── metrics.yml      # Metric definitions
│   └── monitors.yml     # Monitor configurations
└── notebooks/
    └── observe_daily.py # Single notebook that does everything
```

---

## Slack Integration

Alerts are sent to channels configured in `monitors.yml`:

1. **Summary message**: Overview of all declining alerts grouped by metric
2. **Thread replies**: Diagnosis for each declining alert showing error breakdown
3. **Follow-up replies**: Posted to yesterday's thread with recovery status

Requires Slack bot token via:
* Databricks secret: `dbutils.secrets.get(scope="slack", key="pa-bot-token")`
* Or widget parameter: `slack_bot_token`

---

## Scheduling

Create a Databricks Job:

* **Notebook**: `/Repos/<user>/<repo>/observe/notebooks/observe_daily`
* **Schedule**: Daily at desired time
* **Cluster**: Any shared cluster

---

## Running Independently

### Re-send Slack notifications

```python
send_slack_notifications(alerts_df, target_date, config)
```

### Re-send diagnosis to existing thread

```python
send_diagnosis_to_thread(target_date, "#alerts-channel", config)
```

---

## Troubleshooting

### "No alerts generated"

* Check `min_denominator` - your dimension may have too few records
* For auto_threshold: check `min_effective_volume` - the impact may be below threshold
* Verify data exists for the target date in your source table

### "Config not syncing"

* The notebook syncs config from Workspace to DBFS at startup
* If config changes aren't reflected, manually delete `/dbfs/observe/config/` and re-run

### "Backfill taking too long"

* First run backfills 720 days - this is expected to take time
* Reduce `historical_lookback_days` in monitors.yml for faster initial setup
* Consider running on a larger cluster

### "Diagnosis shows wrong errors"

* Check `error_column` in sources.yml points to the correct column
* Use SQL expressions for complex logic: `"CASE WHEN ... THEN col1 ELSE col2 END"`
* Verify `failure_filter` correctly identifies failed records

### "DATATYPE_MISMATCH error in diagnosis"

* Dimension columns are cast to STRING automatically
* If you see type errors, check your source table schema

### "Slack notifications not sending"

* Verify bot token is set (secret or widget)
* Check bot has `chat:write` permission
* Verify channel name includes `#` prefix
* Check Databricks can reach `slack.com` (network/firewall)

### "Too many alerts"

* Increase `threshold_pct` in large_deviation rule
* Increase `min_denominator` to filter low-volume dimensions
* Add more levels to `hierarchy` for better suppression
* If using auto_threshold: increase `target_flag_rate` or `min_effective_volume`

### "Follow-ups not posting"

* Ensure yesterday's alert thread exists in `observe_slack_threads` table
* Check that `follow_up.enabled: true` in monitor config
* Verify the Slack bot can post to the channel
