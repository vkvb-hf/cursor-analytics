# Observe - Config-Based Monitoring System

A config-driven monitoring system for tracking metrics and detecting anomalies in payment data pipelines.

## Overview

Observe monitors daily metrics across different dimensions and alerts when values deviate from expected patterns using:
- **Period-over-Period**: Compare last 7 days avg vs previous 7 days avg
- **Year-over-Year**: Compare today vs same day last year

## How It Works

**One notebook does everything**: `observe_daily`

1. Syncs config from repo to DBFS
2. Creates tables if they don't exist
3. Checks if monitor config changed (hash of metrics, dimensions, source)
   - **Changed** → backfill 720 days (configurable)
   - **Unchanged** → refresh last 30 days (configurable)
4. Evaluates rules and generates alerts
5. Writes to Delta tables

## Quick Start

### 1. Connect Repo to Databricks
- Databricks → Repos → Add Repo
- Connect: `https://github.com/vkvb-hf/cursor-analytics.git`

### 2. Run Daily Monitoring
Run `observe/notebooks/observe_daily` - it handles everything automatically.

```
Parameters:
  target_date: YYYY-MM-DD (optional, defaults to yesterday)
```

First run will backfill 720 days of history. Subsequent runs refresh 30 days.

## Configuration

### monitors.yml - Defaults

```yaml
defaults:
  historical_lookback_days: 720  # Days to backfill when config changes
  refresh_lookback_days: 30      # Days to refresh on normal runs
  min_volume: 15                 # Minimum data points for rules
  alert_channels:
    - "#growth-pa-payments-alerts"
```

### sources.yml - Data Sources

```yaml
sources:
  - name: verifications
    database: payments_hf
    table: verifications
    date_column: created_at
    filters: []
```

### metrics.yml - Metric Definitions

```yaml
metrics:
  - name: verification_count
    source: verifications
    type: count
    expression: "F.count('*')"

  - name: success_rate
    source: verifications
    type: ratio
    numerator: "F.sum(F.when(F.col('status') == 'Success', 1).otherwise(0))"
    denominator: "F.count('*')"
```

### monitors.yml - Monitor Configurations

```yaml
monitors:
  - name: verifications_overall
    metrics:
      - verification_count
      - success_rate
    dimensions:
      - []                        # Global aggregate
      - [country]                 # By country
      - [country, payment_method] # By country + payment method
    rules:
      period_over_period:
        enabled: true
        period_days: 7
        max_change_pct: 0.3       # Alert if >30% change
      day_over_year:
        enabled: true
        max_change_pct: 0.5       # Alert if >50% YoY change
```

## Smart Backfill Logic

The notebook tracks a hash of each monitor's **data-affecting** config:
- Metrics (name, expression, source)
- Dimensions
- Source table and filters

**Rule thresholds are NOT included** - changing `max_change_pct` won't trigger a backfill.

| Scenario | Action |
|----------|--------|
| First run | 720 days backfill |
| Add new metric | 720 days backfill |
| Add new dimension | 720 days backfill |
| Change alert threshold | 30 days refresh (no backfill) |
| Normal daily run | 30 days refresh |

## Output Tables

### payments_hf.observe_metrics_daily
| Column | Description |
|--------|-------------|
| date | Metric date |
| monitor_name | Monitor that computed this |
| metric_name | Name of the metric |
| dimension_key | e.g., "country,payment_method" |
| dimension_value | e.g., "DE,card" |
| metric_value | Computed value |

### payments_hf.observe_alerts_daily
| Column | Description |
|--------|-------------|
| date | Alert date |
| metric_name | Metric that triggered |
| rule_name | Rule that fired |
| severity | critical, warning, info |
| current_value | Current metric value |
| expected_value | Expected/baseline value |
| deviation_pct | % deviation from expected |
| message | Human-readable alert message |

## Adding New Metrics

1. Edit `config/metrics.yml` - add metric definition
2. Edit `config/monitors.yml` - add metric to a monitor
3. Push to GitHub
4. Pull in Databricks Repos
5. Run `observe_daily` - it auto-detects the change and backfills

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

## Scheduling

Create a Databricks Job:
- **Notebook**: `/Repos/<user>/cursor-analytics/observe/notebooks/observe_daily`
- **Schedule**: Daily at 6:00 AM UTC
- **Cluster**: Any shared cluster

## Future Enhancements

- [ ] Slack alert integration
- [ ] Prophet-based anomaly detection
- [ ] Streamlit dashboard
