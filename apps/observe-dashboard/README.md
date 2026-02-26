# Observe Dashboard

A Streamlit dashboard for visualizing the Observe monitoring system data.

## Overview

This dashboard provides two main views:

1. **Alerts Overview** - View and filter alerts from the Observe monitoring system
   - KPI cards showing alert counts by severity
   - Filterable alerts table
   - Drill-down to see alert details

2. **Metrics Explorer** - Explore metrics trends and patterns
   - Time series visualization with PoP and YoY reference lines
   - Heatmap view across dimensions

## Data Sources

- `payments_hf.observe_alerts_daily` - Alert records from Observe
- `payments_hf.observe_metrics_daily` - Daily metric values from Observe

## Local Development

### Prerequisites

- Python 3.11+
- Databricks access credentials

### Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r src/requirements.txt
   ```

3. Set environment variables:
   ```bash
   export DATABRICKS_HOST=https://your-workspace.cloud.databricks.com
   export DATABRICKS_TOKEN=your-token
   export DATABRICKS_HTTP_PATH=/sql/1.0/warehouses/your-warehouse-id
   export OBSERVE_ALERTS_TABLE=payments_hf.observe_alerts_daily
   export OBSERVE_METRICS_TABLE=payments_hf.observe_metrics_daily
   ```

4. Run the app:
   ```bash
   cd src
   streamlit run app.py
   ```

## Docker

Build and run with Docker:

```bash
docker build -t observe-dashboard .
docker run -p 8501:8501 \
  -e DATABRICKS_HOST=... \
  -e DATABRICKS_TOKEN=... \
  -e DATABRICKS_HTTP_PATH=... \
  observe-dashboard
```

## Architecture

```
src/
├── app.py                    # Main entry point
├── data/
│   ├── data_loading.py       # Databricks connection + caching
│   ├── data_transforming.py  # Data transformations
│   └── query_bank.py         # SQL query templates
├── ui/
│   ├── pages/
│   │   ├── alerts_overview.py
│   │   └── metrics_explorer.py
│   ├── user_interfaces/
│   │   ├── filters.py
│   │   └── parameters.py
│   └── views/
│       ├── kpi_cards.py
│       ├── alerts_table.py
│       ├── time_series.py
│       └── heatmap.py
└── utils/
    └── databricks_reader.py
```
