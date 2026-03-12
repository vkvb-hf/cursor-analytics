# Observe - Config-Based Monitoring System

A config-driven monitoring system for tracking metrics and detecting anomalies using auto-calibrated thresholds.

## Overview

Observe monitors daily metrics across different dimensions and alerts when values deviate from expected patterns using **auto-threshold calibration**:
- Compares current day vs same weekday last week
- Calibrates alert thresholds from 365 days of historical data
- Targets a configurable flag rate (default 3%) to avoid alert fatigue
- Suppresses redundant alerts via hierarchy (e.g., if country-level alerts, don't also alert on country+region)

## How It Works

**One notebook does everything**: `observe_daily.py`

1. Syncs config from Workspace to DBFS
2. Creates tables if they don't exist
3. Checks if monitor config changed (hash of metrics, dimensions, source)
   - **Changed** → backfill 720 days
   - **Unchanged** → refresh last 30 days
4. Calibrates k-values from historical residuals
5. Evaluates thresholds and generates alerts
6. Deduplicates via hierarchy suppression
7. Sends Slack notifications with diagnosis

## Quick Start

### Prerequisites

- Databricks workspace with access to your data tables
- (Optional) Slack bot token for notifications

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
    filters: []
```

**metrics.yml** - Define what to measure:
```yaml
version: 1

metrics:
  - name: success_rate
    source: my_events
    type: ratio
    numerator: "status = 'success'"
    denominator: "1=1"
    description: "Overall success rate"
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
      auto_threshold:
        enabled: true
        comparison: same_weekday
        calibration_days: 365
        target_flag_rate: 0.03
        min_denominator: 30
        min_effective_volume: 10
        severity_map:
          critical: 3.0
          warning: 1.0
```

### Step 3: Connect to Databricks

1. Go to Databricks → Repos → Add Repo
2. Connect your repository URL
3. Navigate to `observe/notebooks/observe_daily`

### Step 4: Configure Widget Parameters

Before running, set the widget parameters:
- `output_database`: Your database name (e.g., `my_database`)
- `target_date`: Leave empty for yesterday, or set specific date

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
   dbutils.secrets.put("slack", "bot-token", "<your-bot-token>")
   ```
3. Or pass via widget: `slack_bot_token`

### Step 7: Schedule Daily Runs

Create a Databricks Job:
- **Task**: Notebook task
- **Path**: `/Repos/<user>/<repo>/observe/notebooks/observe_daily`
- **Schedule**: Daily at your preferred time
- **Cluster**: Any cluster with access to your data

---

## Widget Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `target_date` | yesterday | Date to process (YYYY-MM-DD) |
| `output_database` | payments_hf | Database for output tables |
| `metrics_table` | observe_metrics_daily | Metrics table name |
| `alerts_table` | observe_alerts_daily | Alerts table name |
| `threads_table` | observe_slack_threads | Slack thread tracking table |
| `config_path` | /dbfs/observe/config | DBFS path for config files |
| `state_path` | /dbfs/observe/state | DBFS path for state (hashes) |
| `slack_bot_token` | (empty) | Optional, uses secrets if empty |

First run will backfill 720 days of history. Subsequent runs refresh 30 days.

## Configuration

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
    filters: []
    diagnosis:
      error_column: error_reason
      failure_filter: "status = 'failed'"
```

**Diagnosis block**: Configures error breakdown for alerts
- `error_column`: Column (or SQL expression) containing error reasons
- `failure_filter`: SQL filter for failed records

### metrics.yml - Metric Definitions

Define what to measure:

```yaml
metrics:
  - name: success_rate
    source: transactions
    type: ratio
    numerator: "status = 'success'"
    denominator: "1=1"
    filter: "channel = 'web'"
    description: "Success rate for web transactions"
    increase_is_good: true

  - name: conversion_rate
    source: events
    type: ratio
    numerator: "event_type = 'purchase'"
    denominator: "event_type = 'visit'"
    description: "Visit to purchase conversion"
```

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
      - conversion_rate
    dimensions:
      - [region, channel]
    hierarchy:
      - []                    # Global
      - [region]              # By region
      - [region, channel]     # Most granular
    rules:
      auto_threshold:
        enabled: true
        comparison: same_weekday
        calibration_days: 365
        target_flag_rate: 0.03      # Target 3% of days flagged
        min_denominator: 30         # Minimum sample size
        min_effective_volume: 10    # Minimum impact (denom × |deviation|)
        severity_map:
          critical: 3.0             # k multiplier for critical
          warning: 1.0              # k multiplier for warning
```

**Key parameters:**
- `target_flag_rate`: Calibrates thresholds so ~3% of historical days would have triggered
- `min_denominator`: Filters out low-volume dimension combinations
- `min_effective_volume`: Filters out low-impact alerts (e.g., 2 failures out of 100)
- `hierarchy`: Defines suppression order - alerts at higher levels suppress lower levels

## Auto-Threshold Calibration

The system automatically calibrates alert thresholds:

1. **Collect historical pairs**: For each metric × dimension, pair each day with same weekday 7 days prior
2. **Compute residuals**: `residual = current_value - prev_week_value`
3. **Calculate std**: Standard deviation of residuals
4. **Find k**: The multiplier where `|residual| > k × std` for ~`target_flag_rate` of days

**Alert triggers when**: `|current - expected| > calibrated_k × residual_std`

## Hierarchy Suppression

Prevents alert spam by suppressing granular alerts when parent dimensions already alert:

```
Hierarchy: [] → [region] → [region, channel]

If "US" alerts at region level:
  ✓ US (active)
  ✗ US/web (suppressed by US)
  ✗ US/mobile (suppressed by US)
```

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
| numerator_count | Count matching numerator |
| denominator_count | Total count |

### observe_alerts_daily
| Column | Description |
|--------|-------------|
| date | Alert date |
| monitor_name | Monitor that generated alert |
| metric_name | Metric that triggered |
| dimension_key | Dimension combination |
| dimension_value | Dimension values |
| rule_name | auto_threshold |
| severity | critical or warning |
| current_value | Current metric value |
| expected_value | Same weekday last week |
| deviation_pct | % deviation from expected |
| calibrated_k | Calibrated k multiplier |
| residual_std | Historical residual std |
| suppressed | Whether suppressed by hierarchy |
| suppressed_by | Parent dimension that suppressed |
| denominator_count | Sample size |

### observe_slack_threads
| Column | Description |
|--------|-------------|
| date | Alert date |
| channel | Slack channel |
| thread_ts | Thread timestamp for replies |
| message_type | summary or diagnosis |
| created_at | When saved |

## Smart Backfill Logic

The notebook tracks a hash of each monitor's **data-affecting** config:
- Metrics (name, source, numerator, denominator, filter)
- Dimensions
- Source table and filters

**Rule thresholds are NOT included** - changing `target_flag_rate` won't trigger a backfill.

| Scenario | Action |
|----------|--------|
| First run | 720 days backfill |
| Add new metric | 720 days backfill |
| Add new dimension | 720 days backfill |
| Change alert threshold | 30 days refresh (no backfill) |
| Normal daily run | 30 days refresh |

## Adding New Metrics

1. Edit `config/sources.yml` - add source if needed
2. Edit `config/metrics.yml` - add metric definition
3. Edit `config/monitors.yml` - add metric to a monitor
4. Push to repository
5. Pull in Databricks Repos
6. Run `observe_daily` - it auto-detects the change and backfills

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

## Slack Integration

Alerts are sent to channels configured in `monitors.yml`:

1. **Summary message**: Overview of all declining alerts grouped by metric
2. **Thread replies**: Diagnosis for each declining alert showing error breakdown

Requires Slack bot token via:
- Databricks secret: `dbutils.secrets.get(scope="slack", key="bot-token")`
- Or widget parameter: `slack_bot_token`

## Scheduling

Create a Databricks Job:
- **Notebook**: `/Repos/<user>/<repo>/observe/notebooks/observe_daily`
- **Schedule**: Daily at desired time
- **Cluster**: Any shared cluster

## Running Independently

### Re-send Slack notifications
```python
send_slack_notifications(alerts_df, target_date, config)
```

### Re-send diagnosis to existing thread
```python
send_diagnosis_to_thread(target_date, "#alerts-channel", config)
```

## Troubleshooting

### "No alerts generated"
- Check `min_denominator` - your dimension may have too few records
- Check `min_effective_volume` - the impact may be below threshold
- Verify data exists for the target date in your source table

### "Config not syncing"
- The notebook syncs config from Workspace to DBFS at startup
- If config changes aren't reflected, manually delete `/dbfs/observe/config/` and re-run

### "Backfill taking too long"
- First run backfills 720 days - this is expected to take time
- Reduce `historical_lookback_days` in monitors.yml for faster initial setup
- Consider running on a larger cluster

### "Diagnosis shows wrong errors"
- Check `error_column` in sources.yml points to the correct column
- Use SQL expressions for complex logic: `"CASE WHEN ... THEN col1 ELSE col2 END"`
- Verify `failure_filter` correctly identifies failed records

### "DATATYPE_MISMATCH error in diagnosis"
- Dimension columns are cast to STRING automatically
- If you see type errors, check your source table schema

### "Slack notifications not sending"
- Verify bot token is set (secret or widget)
- Check bot has `chat:write` permission
- Verify channel name includes `#` prefix
- Check Databricks can reach `slack.com` (network/firewall)

### "Too many alerts"
- Increase `target_flag_rate` (e.g., 0.05 for 5%)
- Increase `min_effective_volume` to filter low-impact alerts
- Add more levels to `hierarchy` for better suppression
