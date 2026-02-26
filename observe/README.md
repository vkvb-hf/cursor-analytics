# Observe - Config-Based Monitoring System

A config-driven monitoring system for tracking metrics and detecting anomalies in payment data pipelines.

## Overview

Observe monitors daily metrics across different dimensions and alerts when values deviate from expected patterns using:
- **Period-over-Period**: Compare last 7 days avg vs previous 7 days avg
- **Year-over-Year**: Compare today vs same day last year
- **Data Presence**: Ensure minimum records exist

## Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Config (YAML)  │────▶│  observe_daily  │────▶│  Delta Tables   │
│  sources.yml    │     │    notebook     │     │  metrics_daily  │
│  metrics.yml    │     │                 │     │  alerts_daily   │
│  monitors.yml   │     └─────────────────┘     └─────────────────┘
└─────────────────┘
```

## Quick Start

### 1. Connect Repo to Databricks
- Go to Databricks → Repos → Add Repo
- Connect this GitHub repo
- Notebooks will be at `/Repos/<user>/cursor-analytics/observe/notebooks/`

### 2. Run Setup (One-time)
Run `observe_setup` notebook to:
- Create DBFS config folder (`/dbfs/observe/config/`)
- Write YAML configs to DBFS
- Create Delta tables

### 3. Run Daily Monitoring
Run `observe_daily` notebook manually or schedule as a job:
```
Parameters:
  target_date: YYYY-MM-DD (optional, defaults to yesterday)
```

### 4. Backfill Historical Data
Run `observe_backfill` notebook to process a date range.

## Configuration

### sources.yml
Define data sources with their location and date column:

```yaml
sources:
  - name: verifications
    database: payments_hf
    table: verifications
    date_column: created_at
    filters: []
```

### metrics.yml
Define metrics with PySpark expressions:

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

### monitors.yml
Group metrics with dimensions and rules:

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
| rule_name | Rule that fired (period_over_period, day_over_year) |
| severity | critical, warning, info |
| current_value | Current metric value |
| expected_value | Expected/baseline value |
| deviation_pct | % deviation from expected |
| message | Human-readable alert message |

## Adding New Metrics

1. **Add source** (if new table) in `config/sources.yml`
2. **Add metric** in `config/metrics.yml`
3. **Add to monitor** in `config/monitors.yml`
4. **Sync config to DBFS**: Re-run `observe_setup` or manually copy files

## Folder Structure

```
observe/
├── README.md
├── config/
│   ├── sources.yml      # Data source definitions
│   ├── metrics.yml      # Metric definitions
│   └── monitors.yml     # Monitor configurations
└── notebooks/
    ├── observe_setup.py    # One-time setup
    ├── observe_daily.py    # Daily monitoring job
    └── observe_backfill.py # Backfill historical data
```

## Scheduling

Create a Databricks Job to run `observe_daily` notebook:
- **Schedule**: Daily at 6:00 AM UTC
- **Cluster**: Any shared cluster
- **Parameters**: Leave `target_date` empty for yesterday

## Future Enhancements

- [ ] Prophet-based anomaly detection
- [ ] Slack alert integration
- [ ] Streamlit dashboard
- [ ] AI-powered alert summarization
