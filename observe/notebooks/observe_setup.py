# Databricks notebook source
# MAGIC %md
# MAGIC # Observe Setup
# MAGIC 
# MAGIC One-time setup notebook that:
# MAGIC 1. Creates DBFS folder structure
# MAGIC 2. Writes initial YAML config files
# MAGIC 3. Creates Delta tables for metrics and alerts
# MAGIC 4. Verifies source tables are accessible

# COMMAND ----------

import os

os.makedirs("/dbfs/observe/config", exist_ok=True)
os.makedirs("/dbfs/observe/logs", exist_ok=True)
print("Created DBFS directories")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Write Config Files
# MAGIC 
# MAGIC Copy config from repo to DBFS (DBFS is needed for job execution outside of Repos context)

# COMMAND ----------

import yaml

# Get the repo path dynamically
repo_path = "/Workspace" + dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get().rsplit("/", 2)[0]
config_path = f"{repo_path}/config"

print(f"Reading configs from: {config_path}")

# Copy each config file to DBFS
for config_file in ["sources.yml", "metrics.yml", "monitors.yml"]:
    with open(f"{config_path}/{config_file}") as f:
        content = f.read()
    with open(f"/dbfs/observe/config/{config_file}", "w") as f:
        f.write(content)
    print(f"Copied: {config_file}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Delta Tables

# COMMAND ----------

spark.sql("""
CREATE TABLE IF NOT EXISTS payments_hf.observe_metrics_daily (
    date DATE COMMENT 'Date of the metric',
    monitor_name STRING COMMENT 'Name of the monitor',
    source_name STRING COMMENT 'Name of the source',
    metric_name STRING COMMENT 'Name of the metric',
    metric_type STRING COMMENT 'Type of metric (count, ratio)',
    dimension_key STRING COMMENT 'Comma-separated dimension column names',
    dimension_value STRING COMMENT 'Comma-separated dimension values',
    metric_value DOUBLE COMMENT 'Computed metric value',
    numerator DOUBLE COMMENT 'Numerator for ratio metrics',
    denominator DOUBLE COMMENT 'Denominator for ratio metrics',
    computed_at TIMESTAMP COMMENT 'When this metric was computed'
) USING DELTA PARTITIONED BY (date)
COMMENT 'Daily computed metrics for Observe monitoring'
""")
print("Created: payments_hf.observe_metrics_daily")

spark.sql("""
CREATE TABLE IF NOT EXISTS payments_hf.observe_alerts_daily (
    date DATE COMMENT 'Date of the alert',
    monitor_name STRING COMMENT 'Name of the monitor',
    metric_name STRING COMMENT 'Name of the metric',
    dimension_key STRING COMMENT 'Comma-separated dimension column names',
    dimension_value STRING COMMENT 'Comma-separated dimension values',
    rule_name STRING COMMENT 'Name of the rule that triggered',
    severity STRING COMMENT 'Alert severity (critical, warning, info)',
    alert_type STRING COMMENT 'Type of alert (anomaly, threshold, missing_data)',
    current_value DOUBLE COMMENT 'Current metric value',
    expected_value DOUBLE COMMENT 'Expected value (from model or baseline)',
    lower_bound DOUBLE COMMENT 'Lower bound of expected range',
    upper_bound DOUBLE COMMENT 'Upper bound of expected range',
    deviation_pct DOUBLE COMMENT 'Percentage deviation from expected',
    message STRING COMMENT 'Human-readable alert message',
    created_at TIMESTAMP COMMENT 'When this alert was created'
) USING DELTA PARTITIONED BY (date)
COMMENT 'Daily alerts from Observe monitoring rules'
""")
print("Created: payments_hf.observe_alerts_daily")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Verify Source Tables

# COMMAND ----------

from pyspark.sql import functions as F

print("Verifying source tables...")

df = spark.table("payments_hf.verifications")
count = df.count()
print(f"  verifications: {count:,} rows")

df = spark.table("payments_hf.payments_p0_metrics_checkout_funnel")
count = df.count()
print(f"  checkout_funnel: {count:,} rows")

print("\nSetup complete!")
