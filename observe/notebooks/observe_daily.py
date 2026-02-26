# Databricks notebook source
# MAGIC %md
# MAGIC # Observe Daily Monitoring
# MAGIC 
# MAGIC Single notebook that handles everything:
# MAGIC 1. Setup (config sync, table creation)
# MAGIC 2. Smart backfill (720 days if config changed, 30 days otherwise)
# MAGIC 3. Rule evaluation and alerting

# COMMAND ----------

dbutils.widgets.text("target_date", "", "Target Date (YYYY-MM-DD)")

# COMMAND ----------

import yaml
import hashlib
import json
from dataclasses import dataclass, field
from typing import List, Dict, Any
from datetime import datetime, timedelta
from pyspark.sql import functions as F, DataFrame
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC ## Configuration Classes

# COMMAND ----------

@dataclass
class Source:
    name: str
    database: str
    table: str
    date_column: str
    description: str = ""
    columns: List[Dict] = field(default_factory=list)
    filters: List[str] = field(default_factory=list)

@dataclass
class Metric:
    name: str
    source: str
    type: str
    description: str = ""
    expression: str = None
    numerator: str = None
    denominator: str = None
    is_p0: bool = False
    team_ownership: str = ""

@dataclass
class RuleConfig:
    enabled: bool = True
    severity: str = "warning"
    min_records: int = 1
    period_days: int = 7
    max_change_pct: float = 0.3

@dataclass
class Monitor:
    name: str
    metrics: List[str]
    dimensions: List[List[str]]
    rules: Dict[str, RuleConfig]
    description: str = ""
    severity: str = "warning"
    min_volume: int = 15

@dataclass
class Config:
    sources: Dict[str, Source]
    metrics: Dict[str, Metric]
    monitors: List[Monitor]
    defaults: Dict[str, Any]

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Setup (Config Sync + Table Creation)

# COMMAND ----------

import os

# Create DBFS directories
os.makedirs("/dbfs/observe/config", exist_ok=True)
os.makedirs("/dbfs/observe/state", exist_ok=True)
print("DBFS directories ready")

# COMMAND ----------

# Copy config from repo to DBFS
repo_path = "/Workspace" + dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get().rsplit("/", 2)[0]
config_path = f"{repo_path}/config"

print(f"Syncing config from: {config_path}")

for config_file in ["sources.yml", "metrics.yml", "monitors.yml"]:
    with open(f"{config_path}/{config_file}") as f:
        content = f.read()
    with open(f"/dbfs/observe/config/{config_file}", "w") as f:
        f.write(content)
    print(f"  Synced: {config_file}")

# COMMAND ----------

# Ensure tables exist
spark.sql("""
CREATE TABLE IF NOT EXISTS payments_hf.observe_metrics_daily (
    date DATE, monitor_name STRING, source_name STRING, metric_name STRING,
    metric_type STRING, dimension_key STRING, dimension_value STRING,
    metric_value DOUBLE, numerator DOUBLE, denominator DOUBLE, computed_at TIMESTAMP
) USING DELTA PARTITIONED BY (date)
""")

spark.sql("""
CREATE TABLE IF NOT EXISTS payments_hf.observe_alerts_daily (
    date DATE, monitor_name STRING, metric_name STRING, dimension_key STRING,
    dimension_value STRING, rule_name STRING, severity STRING, alert_type STRING,
    current_value DOUBLE, expected_value DOUBLE, lower_bound DOUBLE, upper_bound DOUBLE,
    deviation_pct DOUBLE, message STRING, created_at TIMESTAMP
) USING DELTA PARTITIONED BY (date)
""")
print("Tables ready")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Load Config

# COMMAND ----------

def load_config() -> Config:
    """Load all YAML configs from DBFS"""
    config_path = "/dbfs/observe/config"
    
    with open(f"{config_path}/sources.yml") as f:
        sources_data = yaml.safe_load(f)
    with open(f"{config_path}/metrics.yml") as f:
        metrics_data = yaml.safe_load(f)
    with open(f"{config_path}/monitors.yml") as f:
        monitors_data = yaml.safe_load(f)
    
    sources = {s['name']: Source(**s) for s in sources_data.get('sources', [])}
    metrics = {m['name']: Metric(**m) for m in metrics_data.get('metrics', [])}
    defaults = monitors_data.get('defaults', {})
    
    monitors = []
    for m in monitors_data.get('monitors', []):
        rules = {}
        for rule_name, rule_cfg in m.get('rules', {}).items():
            rules[rule_name] = RuleConfig(**rule_cfg) if isinstance(rule_cfg, dict) else RuleConfig()
        monitors.append(Monitor(
            name=m['name'],
            metrics=m.get('metrics', []),
            dimensions=m.get('dimensions', [[]]),
            rules=rules,
            description=m.get('description', ''),
            severity=m.get('severity', 'warning'),
            min_volume=m.get('min_volume', defaults.get('min_volume', 15))
        ))
    
    return Config(sources=sources, metrics=metrics, monitors=monitors, defaults=defaults)

config = load_config()
print(f"Loaded {len(config.sources)} sources, {len(config.metrics)} metrics, {len(config.monitors)} monitors")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3: Compute Monitor Hash (Data-Affecting Parts Only)

# COMMAND ----------

def compute_monitor_hash(monitor: Monitor, config: Config) -> str:
    """Hash only data-affecting parts: metrics, dimensions, source configs"""
    hash_input = {
        "monitor_name": monitor.name,
        "metrics": [],
        "dimensions": monitor.dimensions
    }
    
    for metric_name in monitor.metrics:
        metric = config.metrics.get(metric_name)
        if metric:
            source = config.sources.get(metric.source)
            hash_input["metrics"].append({
                "name": metric.name,
                "source": metric.source,
                "type": metric.type,
                "expression": metric.expression,
                "numerator": metric.numerator,
                "denominator": metric.denominator,
                "source_table": f"{source.database}.{source.table}" if source else None,
                "source_filters": source.filters if source else []
            })
    
    hash_str = json.dumps(hash_input, sort_keys=True)
    return hashlib.md5(hash_str.encode()).hexdigest()


def load_stored_hashes() -> Dict[str, str]:
    """Load previously stored hashes"""
    hash_file = "/dbfs/observe/state/monitor_hashes.json"
    try:
        with open(hash_file) as f:
            return json.load(f)
    except:
        return {}


def save_hashes(hashes: Dict[str, str]):
    """Save current hashes"""
    hash_file = "/dbfs/observe/state/monitor_hashes.json"
    with open(hash_file, "w") as f:
        json.dump(hashes, f)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 4: Determine Lookback Per Monitor

# COMMAND ----------

# Get target date
target_date_str = dbutils.widgets.get("target_date")
if target_date_str:
    target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
else:
    target_date = datetime.now() - timedelta(days=1)

print(f"Target date: {target_date.strftime('%Y-%m-%d')}")

# COMMAND ----------

# Determine lookback for each monitor
stored_hashes = load_stored_hashes()
new_hashes = {}
monitor_lookbacks = {}

historical_days = config.defaults.get('historical_lookback_days', 720)
refresh_days = config.defaults.get('refresh_lookback_days', 30)

print(f"\nConfig: historical={historical_days} days, refresh={refresh_days} days")
print("-" * 50)

for monitor in config.monitors:
    current_hash = compute_monitor_hash(monitor, config)
    stored_hash = stored_hashes.get(monitor.name)
    new_hashes[monitor.name] = current_hash
    
    if stored_hash != current_hash:
        monitor_lookbacks[monitor.name] = historical_days
        reason = "NEW" if not stored_hash else "CHANGED"
        print(f"{monitor.name}: {reason} → {historical_days} days backfill")
    else:
        monitor_lookbacks[monitor.name] = refresh_days
        print(f"{monitor.name}: unchanged → {refresh_days} days refresh")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 5: Compute Metrics

# COMMAND ----------

def compute_metric(
    config: Config,
    metric: Metric,
    dimensions: List[str],
    target_date: datetime,
    lookback_days: int
) -> DataFrame:
    """Compute a single metric for given dimensions over lookback period"""
    source = config.sources[metric.source]
    start_date = target_date - timedelta(days=lookback_days)
    
    df = spark.table(f"{source.database}.{source.table}")
    
    # Apply date filter
    date_col = F.col(source.date_column)
    if "string" in str(df.schema[source.date_column].dataType).lower():
        date_col = F.to_date(date_col)
    df = df.filter((date_col >= start_date) & (date_col <= target_date))
    
    # Apply source filters
    for flt in source.filters:
        df = df.filter(flt)
    
    # Group by date + dimensions
    group_cols = [F.to_date(F.col(source.date_column)).alias("date")]
    for dim in dimensions:
        group_cols.append(F.col(dim))
    
    grouped = df.groupBy(group_cols)
    
    # Compute metric
    if metric.type == "count":
        result = grouped.agg(eval(metric.expression).alias("metric_value"))
    else:  # ratio
        result = grouped.agg(
            eval(metric.numerator).alias("numerator"),
            eval(metric.denominator).alias("denominator")
        )
        result = result.withColumn(
            "metric_value",
            F.when(F.col("denominator") > 0, F.col("numerator") / F.col("denominator")).otherwise(None)
        )
    
    # Add metadata
    result = result.withColumn("metric_name", F.lit(metric.name))
    result = result.withColumn("metric_type", F.lit(metric.type))
    result = result.withColumn("source_name", F.lit(metric.source))
    
    dim_key = ",".join(dimensions) if dimensions else "global"
    result = result.withColumn("dimension_key", F.lit(dim_key))
    
    if dimensions:
        dim_value_expr = F.concat_ws(",", *[F.col(d) for d in dimensions])
    else:
        dim_value_expr = F.lit("global")
    result = result.withColumn("dimension_value", dim_value_expr)
    
    return result

# COMMAND ----------

def compute_all_metrics(config: Config, target_date: datetime, monitor_lookbacks: Dict[str, int]) -> DataFrame:
    """Compute all metrics for all monitors with appropriate lookback"""
    all_results = []
    
    for monitor in config.monitors:
        lookback = monitor_lookbacks[monitor.name]
        print(f"\nComputing {monitor.name} ({lookback} days)...")
        
        for metric_name in monitor.metrics:
            metric = config.metrics.get(metric_name)
            if not metric:
                continue
            for dims in monitor.dimensions:
                try:
                    result = compute_metric(config, metric, dims, target_date, lookback)
                    result = result.withColumn("monitor_name", F.lit(monitor.name))
                    all_results.append(result)
                    print(f"  ✓ {metric_name} [{','.join(dims) or 'global'}]")
                except Exception as e:
                    print(f"  ✗ {metric_name} [{','.join(dims) or 'global'}]: {e}")
    
    if not all_results:
        return None
    
    # Standardize columns
    standard_cols = ["date", "monitor_name", "source_name", "metric_name", "metric_type",
                     "dimension_key", "dimension_value", "metric_value"]
    
    standardized = []
    for df in all_results:
        if "numerator" not in df.columns:
            df = df.withColumn("numerator", F.lit(None).cast("double"))
        if "denominator" not in df.columns:
            df = df.withColumn("denominator", F.lit(None).cast("double"))
        standardized.append(df.select(standard_cols + ["numerator", "denominator"]))
    
    from functools import reduce
    combined = reduce(DataFrame.unionByName, standardized)
    return combined.withColumn("computed_at", F.current_timestamp())

# COMMAND ----------

print("Computing metrics...")
metrics_df = compute_all_metrics(config, target_date, monitor_lookbacks)

if metrics_df:
    metrics_count = metrics_df.count()
    print(f"\nTotal: {metrics_count} metric records")
else:
    print("No metrics computed")
    dbutils.notebook.exit("No metrics")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 6: Evaluate Rules

# COMMAND ----------

def check_period_over_period(
    metrics_df: DataFrame,
    target_date: datetime,
    period_days: int = 7,
    max_change_pct: float = 0.3,
    min_volume: int = 15
) -> List[Dict]:
    """Compare last N days avg with previous N days avg"""
    alerts = []
    
    current_start = target_date - timedelta(days=period_days - 1)
    previous_start = current_start - timedelta(days=period_days)
    previous_end = current_start - timedelta(days=1)
    
    for row in metrics_df.select("monitor_name", "metric_name", "dimension_key", "dimension_value").distinct().collect():
        slice_df = metrics_df.filter(
            (F.col("monitor_name") == row.monitor_name) &
            (F.col("metric_name") == row.metric_name) &
            (F.col("dimension_key") == row.dimension_key) &
            (F.col("dimension_value") == row.dimension_value)
        )
        
        current_avg = slice_df.filter(
            (F.col("date") >= current_start) & (F.col("date") <= target_date)
        ).agg(F.avg("metric_value").alias("avg"), F.count("*").alias("cnt")).collect()[0]
        
        previous_avg = slice_df.filter(
            (F.col("date") >= previous_start) & (F.col("date") <= previous_end)
        ).agg(F.avg("metric_value").alias("avg"), F.count("*").alias("cnt")).collect()[0]
        
        if current_avg.cnt < min_volume or previous_avg.cnt < min_volume:
            continue
        if current_avg.avg is None or previous_avg.avg is None or previous_avg.avg == 0:
            continue
        
        change_pct = (current_avg.avg - previous_avg.avg) / previous_avg.avg
        
        if abs(change_pct) > max_change_pct:
            direction = "increased" if change_pct > 0 else "decreased"
            alerts.append({
                "monitor_name": row.monitor_name,
                "metric_name": row.metric_name,
                "dimension_key": row.dimension_key,
                "dimension_value": row.dimension_value,
                "rule_name": "period_over_period",
                "alert_type": "anomaly",
                "current_value": current_avg.avg,
                "expected_value": previous_avg.avg,
                "deviation_pct": change_pct * 100,
                "message": f"{row.metric_name} {direction} by {abs(change_pct)*100:.1f}% (current: {current_avg.avg:.4f}, previous: {previous_avg.avg:.4f})"
            })
    
    return alerts


def check_day_over_year(
    metrics_df: DataFrame,
    target_date: datetime,
    max_change_pct: float = 0.5
) -> List[Dict]:
    """Compare today with same day last year"""
    alerts = []
    yoy_date = target_date - timedelta(days=365)
    
    for row in metrics_df.select("monitor_name", "metric_name", "dimension_key", "dimension_value").distinct().collect():
        slice_df = metrics_df.filter(
            (F.col("monitor_name") == row.monitor_name) &
            (F.col("metric_name") == row.metric_name) &
            (F.col("dimension_key") == row.dimension_key) &
            (F.col("dimension_value") == row.dimension_value)
        )
        
        current = slice_df.filter(F.col("date") == target_date).select("metric_value").collect()
        yoy = slice_df.filter(F.col("date") == yoy_date).select("metric_value").collect()
        
        if not current or not yoy:
            continue
        current_val, yoy_val = current[0].metric_value, yoy[0].metric_value
        if current_val is None or yoy_val is None or yoy_val == 0:
            continue
        
        change_pct = (current_val - yoy_val) / yoy_val
        
        if abs(change_pct) > max_change_pct:
            direction = "increased" if change_pct > 0 else "decreased"
            alerts.append({
                "monitor_name": row.monitor_name,
                "metric_name": row.metric_name,
                "dimension_key": row.dimension_key,
                "dimension_value": row.dimension_value,
                "rule_name": "day_over_year",
                "alert_type": "anomaly",
                "current_value": current_val,
                "expected_value": yoy_val,
                "deviation_pct": change_pct * 100,
                "message": f"{row.metric_name} {direction} by {abs(change_pct)*100:.1f}% YoY (current: {current_val:.4f}, last year: {yoy_val:.4f})"
            })
    
    return alerts


def evaluate_all_rules(config: Config, metrics_df: DataFrame, target_date: datetime) -> DataFrame:
    """Evaluate all rules and return alerts DataFrame"""
    all_alerts = []
    
    for monitor in config.monitors:
        monitor_metrics = metrics_df.filter(F.col("monitor_name") == monitor.name)
        
        if "period_over_period" in monitor.rules and monitor.rules["period_over_period"].enabled:
            rule = monitor.rules["period_over_period"]
            alerts = check_period_over_period(
                monitor_metrics, target_date,
                period_days=rule.period_days,
                max_change_pct=rule.max_change_pct,
                min_volume=monitor.min_volume
            )
            for a in alerts:
                a["severity"] = rule.severity
            all_alerts.extend(alerts)
        
        if "day_over_year" in monitor.rules and monitor.rules["day_over_year"].enabled:
            rule = monitor.rules["day_over_year"]
            alerts = check_day_over_year(
                monitor_metrics, target_date,
                max_change_pct=rule.max_change_pct
            )
            for a in alerts:
                a["severity"] = rule.severity
            all_alerts.extend(alerts)
    
    if not all_alerts:
        return None
    
    schema = StructType([
        StructField("monitor_name", StringType()),
        StructField("metric_name", StringType()),
        StructField("dimension_key", StringType()),
        StructField("dimension_value", StringType()),
        StructField("rule_name", StringType()),
        StructField("severity", StringType()),
        StructField("alert_type", StringType()),
        StructField("current_value", DoubleType()),
        StructField("expected_value", DoubleType()),
        StructField("deviation_pct", DoubleType()),
        StructField("message", StringType()),
    ])
    
    alerts_df = spark.createDataFrame(all_alerts, schema)
    alerts_df = alerts_df.withColumn("date", F.lit(target_date.strftime("%Y-%m-%d")).cast("date"))
    alerts_df = alerts_df.withColumn("lower_bound", F.lit(None).cast("double"))
    alerts_df = alerts_df.withColumn("upper_bound", F.lit(None).cast("double"))
    alerts_df = alerts_df.withColumn("created_at", F.current_timestamp())
    
    return alerts_df

# COMMAND ----------

print("Evaluating rules...")
alerts_df = evaluate_all_rules(config, metrics_df, target_date)

if alerts_df:
    alerts_count = alerts_df.count()
    print(f"Generated {alerts_count} alerts")
    display(alerts_df)
else:
    alerts_count = 0
    print("No alerts generated")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 7: Write Results

# COMMAND ----------

# Get date range to delete (based on max lookback used)
max_lookback = max(monitor_lookbacks.values())
start_date = (target_date - timedelta(days=max_lookback)).strftime("%Y-%m-%d")
end_date = target_date.strftime("%Y-%m-%d")

# Delete existing data for the date range
spark.sql(f"DELETE FROM payments_hf.observe_metrics_daily WHERE date BETWEEN '{start_date}' AND '{end_date}'")
print(f"Cleared metrics for {start_date} to {end_date}")

# Write new metrics
metrics_df.write.format("delta").mode("append").saveAsTable("payments_hf.observe_metrics_daily")
print(f"Written {metrics_count} metrics")

# COMMAND ----------

# Write alerts (only for target date)
if alerts_df:
    spark.sql(f"DELETE FROM payments_hf.observe_alerts_daily WHERE date = '{end_date}'")
    alerts_df.write.format("delta").mode("append").saveAsTable("payments_hf.observe_alerts_daily")
    print(f"Written {alerts_count} alerts")

# COMMAND ----------

# Save hashes for next run
save_hashes(new_hashes)
print("Saved monitor hashes")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary

# COMMAND ----------

print(f"\n{'='*50}")
print(f"OBSERVE DAILY COMPLETE - {end_date}")
print(f"{'='*50}")
print(f"Metrics computed: {metrics_count}")
print(f"Alerts generated: {alerts_count}")
print(f"\nMonitor lookbacks used:")
for name, days in monitor_lookbacks.items():
    print(f"  - {name}: {days} days")
print(f"\nTables updated:")
print(f"  - payments_hf.observe_metrics_daily")
print(f"  - payments_hf.observe_alerts_daily")
