# Steering Dashboard

A Streamlit dashboard for viewing weekly steering reports and triggering AI-powered metric diagnosis.

## Overview

This dashboard provides:

1. **Steering Report Viewer** - View weekly steering reports with a week selector
2. **AI-Powered Diagnosis** - Click "Diagnose" to run an iterative analysis of any metric anomaly

The diagnosis feature uses AWS Bedrock Claude with direct Databricks SQL access to perform multi-level drill-down analysis following the steering-metric-diagnosis methodology.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Streamlit App                           │
│  ┌─────────────────┐    ┌─────────────────────────────────┐ │
│  │ Report Viewer   │    │ Diagnosis Panel                 │ │
│  │ - Week selector │    │ - Query input                   │ │
│  │ - MD display    │    │ - Progress display              │ │
│  └─────────────────┘    │ - Report output                 │ │
│                         └─────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
           ┌───────────────┐               ┌───────────────┐
           │ AWS Bedrock   │               │  Databricks   │
           │ (Claude)      │◄─────────────►│  SQL          │
           │               │  Tool Loop    │               │
           └───────────────┘               └───────────────┘
```

## Prerequisites

- Python 3.11+
- AWS SSO access with `sso-bedrock` profile
- Databricks access credentials (`~/.databrickscfg`)

## Setup

1. **Clone and navigate to the app:**
   ```bash
   cd ~/Documents/GitHub/cursor-analytics/apps/steering-dashboard/src
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS SSO:**
   ```bash
   aws sso login --profile sso-bedrock
   ```

4. **Configure Databricks** (if not already done):
   
   Create `~/.databrickscfg`:
   ```ini
   [DEFAULT]
   host = https://your-workspace.cloud.databricks.com
   token = your-token
   ```
   
   Set environment variable:
   ```bash
   export DATABRICKS_HTTP_PATH=/sql/1.0/warehouses/your-warehouse-id
   ```

5. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Select a week** from the sidebar dropdown
2. **View the steering report** in the left panel
3. **Enter a diagnosis query** in the right panel, e.g.:
   - "Acceptance LL0 dropped 2.32% in HF-INTL"
   - "Recovery W0 increased 17.61% overall"
4. **Click "Diagnose"** to start the AI-powered analysis
5. **Wait 2-5 minutes** while the agent runs iterative SQL queries
6. **Review the diagnosis report** with root cause analysis

## Configuration

| Variable | Purpose | Default |
|----------|---------|---------|
| `STEERING_REPORTS_DIR` | Path to steering report markdown files | `~/Documents/GitHub/cursor-analytics/projects/long_term_steering_report` |
| `DATABRICKS_HOST` | Databricks workspace URL | From `~/.databrickscfg` |
| `DATABRICKS_TOKEN` | Databricks PAT | From `~/.databrickscfg` |
| `DATABRICKS_HTTP_PATH` | SQL warehouse path | From env |
| `AWS_PROFILE` | AWS profile for Bedrock | `sso-bedrock` |
| `AWS_REGION` | AWS region | `eu-west-1` |
| `BEDROCK_MODEL_ID` | Claude model ID | `eu.anthropic.claude-sonnet-4-20250514-v1:0` |

## Diagnosis Output

The diagnosis produces a comprehensive markdown report with:

- **Executive Summary** - Root cause in one sentence
- **Level 0: Cluster Comparison** - All clusters side-by-side
- **Level 1: Dimension Scan** - All segments with >1pp change
- **Level 2: Country Breakdown** - Country-level drill-down
- **Level 2: Decline Reasons** - Decline reason analysis
- **Level 4: Cross-Validation** - Related metrics check
- **Diagnostic Summary** - Key findings by level

Reports are automatically saved to `~/Documents/temp/`.

## File Structure

```
apps/steering-dashboard/
├── README.md
└── src/
    ├── app.py                      # Main Streamlit app
    ├── requirements.txt            # Python dependencies
    └── utils/
        ├── __init__.py
        ├── report_loader.py        # Load steering report markdown files
        ├── databricks_reader.py    # Databricks SQL connection
        ├── diagnosis_agent.py      # LLM tool loop with Bedrock
        └── diagnosis_prompts.py    # System prompt and tool definitions
```

## Troubleshooting

### AWS Bedrock connection failed
```bash
aws sso login --profile sso-bedrock
```

### Databricks connection failed
1. Check `~/.databrickscfg` exists with valid host/token
2. Ensure `DATABRICKS_HTTP_PATH` is set
3. Verify your token hasn't expired

### No steering reports found
1. Ensure you're on the correct git branch: `feature/long-term-steering-report`
2. Check `STEERING_REPORTS_DIR` points to the correct location
