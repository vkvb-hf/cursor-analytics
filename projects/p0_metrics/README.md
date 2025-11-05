# P0 Metrics - Steering Metrics Generation

This project contains the Databricks notebook for generating steering metrics reports.

## Overview

The steering metrics notebook generates weekly reports for P0 payment metrics, including:
- Activation metrics (Checkout Funnel, Payment Page Visit to Success)
- Fraud metrics (Duplicate Rate, Payment Fraud Block Rate)
- Reactivation metrics
- Active customer metrics (AR, Ship Rate, Recovery, Dunning Profit)

## Files

- `steering_metrics_notebook.py` - The main Databricks notebook that generates steering metrics reports

## Key Features

1. **Statistical Significance Testing**: Uses z-scores to determine statistical significance of metric changes
2. **Multi-level Reporting**: Generates reports at:
   - Overall cluster level
   - Dimension level (by PaymentMethod, ChannelCategory, etc.)
   - Business unit level
3. **Automated Report Generation**: Creates structured output files for each metric and reporting cluster

## Reporting Clusters

- Overall
- HF-NA
- HF-INTL
- US-HF
- RTE
- WL

## Metrics Tracked

14 steering metrics covering:
- Checkout funnel metrics (frontend and backend)
- Voucher fraud metrics
- Payment fraud metrics
- Reactivation rates
- Pre-dunning AR metrics
- Ship rates and recovery metrics
- Dunning profit metrics

## Output Structure

The notebook generates reports in the format:
```
/Workspace/Users/{username}/steering-{YYYY-Www}/
├── detailed_summary.txt
└── {metric_name}/
    └── summary.txt
```

## Source

This notebook was retrieved from Databricks:
- Job ID: 863174042909812
- Notebook ID: 3549820133656532

