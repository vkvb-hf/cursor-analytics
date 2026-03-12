# Observe - Config-Based Monitoring System

A config-driven monitoring system for tracking payment metrics and detecting anomalies using auto-calibrated thresholds.

## Overview

Observe monitors daily metrics across different dimensions and alerts when values deviate from expected patterns using **auto-threshold calibration**:
- Compares current day vs same weekday last week
- Calibrates alert thresholds from 365 days of historical data
- Targets a configurable flag rate (default 3%) to avoid alert fatigue
- Suppresses redundant alerts via hierarchy (e.g., if country-level alerts, don't also alert on country+provider)

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

### 1. Connect Repo to Databricks
- Databricks → Repos → Add Repo
- Connect: `https://github.com/vkvb-hf/cursor-analytics.git`

### 2. Run Daily Monitoring
Run `observe/notebooks/observe_daily` - it handles everything automatically.

### Widget Parameters

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

```yaml
sources:
  - name: verifications
    database: payments_hf
    table: f_pvs_replica
    date_column: date
    columns:
      - name: country
      - name: provider
      - name: payment_method
      - name: new_payment_method
    filters: []
    diagnosis:
      error_column: decline_response
      failure_filter: "verification_result = 'failed'"

  - name: orders
    database: payments_hf
    table: f_orders
    date_column: delivery_date
    columns:
      - name: country
      - name: first_provider
      - name: first_token
      - name: type_order
    filters: []
    diagnosis:
      error_column: "CASE WHEN bob_status = 'clarify_payment_error' THEN REGEXP_EXTRACT(first_note, '^([^|]+)', 1) ELSE latest_note END"
      failure_filter: "latest_status = 'canceled'"
```

**Diagnosis block**: Configures error breakdown for alerts
- `error_column`: Column (or expression) containing error reasons
- `failure_filter`: SQL filter for failed records

### metrics.yml - Metric Definitions

```yaml
metrics:
  - name: tsr_checkout_tokenisation
    source: verifications
    type: ratio
    numerator: "verification_result = 'success'"
    denominator: "1=1"
    filter: "workflow = 'checkout_tokenisation'"
    description: "Token Success Rate for checkout"
    increase_is_good: true

  - name: payment_approval_rate
    source: orders
    type: ratio
    numerator: "latest_status != 'canceled'"
    denominator: "1=1"
    filter: "product_type = 'mealbox'"
    description: "Payment Approval Rate"
```

### monitors.yml - Monitor Configurations

```yaml
defaults:
  historical_lookback_days: 720
  refresh_lookback_days: 30
  alert_channels:
    - "#temp-test-alerts"

monitors:
  - name: tokenisation_monitor
    description: "TSR monitoring with auto-thresholds"
    severity: critical
    metrics:
      - tsr_checkout_tokenisation
      - tsr_reactivation
    dimensions:
      - [country, payment_method, new_payment_method]
    hierarchy:
      - []                                        # Global
      - [country]                                 # By country
      - [country, payment_method]                 # By country + PM
      - [country, payment_method, new_payment_method]  # Most granular
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
Hierarchy: [] → [country] → [country, provider] → [country, provider, token]

If "DE" alerts at country level:
  ✓ DE (active)
  ✗ DE/Adyen (suppressed by DE)
  ✗ DE/Adyen/CreditCard (suppressed by DE)
```

## Diagnosis Feature

For declining alerts, the system queries error breakdowns and posts them as Slack thread replies:

```
🔍 Diagnosis: TSR Reactivation - IE/Adyen_CreditCard/existing_pm (-36.4%)

Top error increases vs last week:
• Refused(CVC Declined): 4 → 24 (+20)
• Refused(FRAUD): 3 → 16 (+13)
• Refused(Refused): 2 → 7 (+5)

Total failures: 11 → 68 (+518%)
```

## Output Tables

### payments_hf.observe_metrics_daily
| Column | Description |
|--------|-------------|
| date | Metric date |
| monitor_name | Monitor that computed this |
| metric_name | Name of the metric |
| dimension_key | e.g., "country,payment_method" |
| dimension_value | e.g., "DE,Adyen_CreditCard" |
| metric_value | Computed ratio (0-1) |
| numerator_count | Count matching numerator |
| denominator_count | Total count |

### payments_hf.observe_alerts_daily
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

### payments_hf.observe_slack_threads
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
4. Push to GitHub
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
- Databricks secret: `dbutils.secrets.get(scope="slack", key="pa-bot-token")`
- Or widget parameter: `slack_bot_token`

## Scheduling

Create a Databricks Job:
- **Notebook**: `/Repos/<user>/cursor-analytics/observe/notebooks/observe_daily`
- **Schedule**: Daily at 6:00 AM UTC
- **Cluster**: Any shared cluster

## Running Independently

### Re-send Slack notifications
```python
send_slack_notifications(alerts_df, target_date, config)
```

### Re-send diagnosis to existing thread
```python
send_diagnosis_to_thread(target_date, "#temp-test-alerts", config)
```
