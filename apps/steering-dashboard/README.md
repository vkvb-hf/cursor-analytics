# Steering Dashboard

Streamlit dashboard for viewing weekly steering reports and AI-powered metric diagnosis.

## Features

- **Weekly Report Viewer** - Browse steering reports by week
- **AI Diagnosis** - Iterative drill-down analysis of metric anomalies using Bedrock Claude + Databricks SQL

## Quick Start

```bash
cd ~/Documents/GitHub/cursor-analytics/apps/steering-dashboard/src

# Install dependencies
pip install -r requirements.txt

# Login to AWS (required for Bedrock)
aws sso login --profile sso-bedrock

# Run
python3 -m streamlit run app.py --server.headless true
```

## Prerequisites

| Requirement | Setup |
|-------------|-------|
| AWS SSO | `aws sso login --profile sso-bedrock` |
| Databricks | `~/.databrickscfg` with `host`, `token`, `warehouse_id` |

### Databricks Config (`~/.databrickscfg`)

```ini
[DEFAULT]
host = https://hf-gp.cloud.databricks.com/
token = dapi...
warehouse_id = d2541ca06ccda636
```

## Usage

1. Select week from sidebar
2. View report in **Weekly Report** tab
3. In **Diagnosis** tab, enter a metric query:
   ```
   Acceptance LL0: HF-INTL: 90.28% to 88.18% (↓2.32%)
   ```
4. Click **Diagnose** and wait 2-5 minutes
5. Download the generated report

## Diagnosis Levels

| Level | Purpose |
|-------|---------|
| L0 | Cluster comparison + trend check |
| L1 | Dimension scan (all segments >1pp change) |
| L2 | Country breakdown + decline reasons |
| L4 | Cross-validation with related metrics |

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `STEERING_REPORTS_DIR` | `~/Documents/GitHub/cursor-analytics/projects/long_term_steering_report` | Report files location |
| `AWS_PROFILE` | `sso-bedrock` | AWS profile for Bedrock |
| `AWS_REGION` | `eu-west-1` | Bedrock region |
| `BEDROCK_MODEL_ID` | `eu.anthropic.claude-sonnet-4-20250514-v1:0` | Claude model |

## File Structure

```
apps/steering-dashboard/
├── README.md
└── src/
    ├── app.py                    # Streamlit app
    ├── requirements.txt
    └── utils/
        ├── report_loader.py      # Load markdown reports
        ├── databricks_reader.py  # Databricks Statement Execution API
        ├── diagnosis_agent.py    # Bedrock tool loop
        └── diagnosis_prompts.py  # System prompt + SQL templates
```

## Troubleshooting

**AWS Bedrock fails**: Run `aws sso login --profile sso-bedrock`

**Databricks fails**: Check `~/.databrickscfg` has valid `host`, `token`, `warehouse_id`

**No reports found**: Ensure branch is `feature/long-term-steering-report`

**Level 2 wrong volumes**: Source tables are aggregated. For `checkout_funnel_backend`, multiply by `customer_count`:
```sql
SUM(event_attempted_payment_verification * customer_count)  -- correct
SUM(event_attempted_payment_verification)                   -- wrong (64 vs 16,952)
```
