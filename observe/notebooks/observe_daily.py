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
    increase_is_good: bool = True

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

# Sync config to DBFS
# Try multiple methods: Repos path, Workspace files API, or skip if already on DBFS
notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()

config_synced = False

# Method 1: If running from Repos, read directly
if notebook_path.startswith("/Repos"):
    repo_path = notebook_path.rsplit("/", 2)[0]
    config_path = f"{repo_path}/config"
    print(f"Syncing config from Repos: {config_path}")
    try:
        for config_file in ["sources.yml", "metrics.yml", "monitors.yml"]:
            with open(f"{config_path}/{config_file}") as f:
                content = f.read()
            with open(f"/dbfs/observe/config/{config_file}", "w") as f:
                f.write(content)
            print(f"  Synced: {config_file}")
        config_synced = True
    except Exception as e:
        print(f"  Failed: {e}")

# Method 2: If running from Workspace, use Workspace REST API
if not config_synced and "/Users/" in notebook_path:
    import requests
    import base64
    
    # Get the workspace base path from notebook_path
    workspace_base = notebook_path.rsplit("/", 2)[0]  # /Users/user@example.com/observe
    config_ws_path = f"{workspace_base}/config"
    print(f"Syncing config from Workspace API: {config_ws_path}")
    
    try:
        # Get workspace host and token from notebook context
        ctx = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
        host = ctx.apiUrl().get()
        token = ctx.apiToken().get()
        headers = {"Authorization": f"Bearer {token}"}
        
        for config_file in ["sources.yml", "metrics.yml", "monitors.yml"]:
            ws_file_path = f"{config_ws_path}/{config_file}"
            export_url = f"{host}/api/2.0/workspace/export"
            params = {"path": ws_file_path, "format": "SOURCE"}
            
            response = requests.get(export_url, headers=headers, params=params)
            response.raise_for_status()
            
            content_b64 = response.json().get('content', '')
            content = base64.b64decode(content_b64).decode('utf-8')
            
            with open(f"/dbfs/observe/config/{config_file}", "w") as f:
                f.write(content)
            print(f"  Synced: {config_file}")
        config_synced = True
    except Exception as e:
        print(f"  Failed: {e}")

# Method 3: Check if configs already exist on DBFS
if not config_synced:
    print("Checking for existing configs on DBFS...")
    try:
        for config_file in ["sources.yml", "metrics.yml", "monitors.yml"]:
            with open(f"/dbfs/observe/config/{config_file}") as f:
                _ = f.read()
        print("  Using existing DBFS configs")
        config_synced = True
    except:
        raise Exception("No config files found! Please sync configs to /dbfs/observe/config/ first.")

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
    metrics_df.cache()  # Cache for reuse in rule evaluation
    metrics_count = metrics_df.count()
    print(f"\nTotal: {metrics_count} metric records")
else:
    print("No metrics computed")
    dbutils.notebook.exit("No metrics")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 6: Evaluate Rules (Single Query)

# COMMAND ----------

def compute_rule_aggregations(metrics_df: DataFrame, target_date: datetime, period_days: int = 7) -> DataFrame:
    """
    Compute all aggregations needed for rules in ONE query.
    Returns DataFrame with: current_avg, previous_avg, target_day_value, yoy_value per metric/dimension combo.
    """
    target_date_lit = F.lit(target_date.strftime("%Y-%m-%d")).cast("date")
    
    # Date boundaries
    current_start = (target_date - timedelta(days=period_days - 1)).strftime("%Y-%m-%d")
    previous_start = (target_date - timedelta(days=2 * period_days - 1)).strftime("%Y-%m-%d")
    previous_end = (target_date - timedelta(days=period_days)).strftime("%Y-%m-%d")
    yoy_date = (target_date - timedelta(days=365)).strftime("%Y-%m-%d")
    target_date_str = target_date.strftime("%Y-%m-%d")
    
    # Single aggregation query
    agg_df = metrics_df.groupBy(
        "monitor_name", "metric_name", "dimension_key", "dimension_value"
    ).agg(
        # Period over period: current period avg (last 7 days)
        F.avg(F.when(
            (F.col("date") >= current_start) & (F.col("date") <= target_date_str),
            F.col("metric_value")
        )).alias("current_avg"),
        
        # Period over period: current period count
        F.sum(F.when(
            (F.col("date") >= current_start) & (F.col("date") <= target_date_str),
            F.lit(1)
        ).otherwise(0)).alias("current_count"),
        
        # Period over period: previous period avg (7 days before that)
        F.avg(F.when(
            (F.col("date") >= previous_start) & (F.col("date") <= previous_end),
            F.col("metric_value")
        )).alias("previous_avg"),
        
        # Period over period: previous period count
        F.sum(F.when(
            (F.col("date") >= previous_start) & (F.col("date") <= previous_end),
            F.lit(1)
        ).otherwise(0)).alias("previous_count"),
        
        # Day over year: target day value
        F.first(F.when(
            F.col("date") == target_date_str,
            F.col("metric_value")
        )).alias("target_day_value"),
        
        # Day over year: same day last year value
        F.first(F.when(
            F.col("date") == yoy_date,
            F.col("metric_value")
        )).alias("yoy_value")
    )
    
    # Compute deviations
    agg_df = agg_df.withColumn(
        "pop_change_pct",
        F.when(
            (F.col("previous_avg").isNotNull()) & (F.col("previous_avg") != 0),
            (F.col("current_avg") - F.col("previous_avg")) / F.col("previous_avg")
        )
    ).withColumn(
        "yoy_change_pct",
        F.when(
            (F.col("yoy_value").isNotNull()) & (F.col("yoy_value") != 0),
            (F.col("target_day_value") - F.col("yoy_value")) / F.col("yoy_value")
        )
    )
    
    return agg_df

# COMMAND ----------

def build_monitor_thresholds(config: Config) -> DataFrame:
    """Build a DataFrame of monitor thresholds from config"""
    rows = []
    for monitor in config.monitors:
        row = {
            "monitor_name": monitor.name,
            "min_volume": monitor.min_volume,
            "pop_enabled": False,
            "pop_max_change_pct": 0.3,
            "pop_severity": "warning",
            "yoy_enabled": False,
            "yoy_max_change_pct": 0.5,
            "yoy_severity": "info"
        }
        
        if "period_over_period" in monitor.rules:
            rule = monitor.rules["period_over_period"]
            row["pop_enabled"] = rule.enabled
            row["pop_max_change_pct"] = rule.max_change_pct
            row["pop_severity"] = rule.severity
        
        if "day_over_year" in monitor.rules:
            rule = monitor.rules["day_over_year"]
            row["yoy_enabled"] = rule.enabled
            row["yoy_max_change_pct"] = rule.max_change_pct
            row["yoy_severity"] = rule.severity
        
        rows.append(row)
    
    return spark.createDataFrame(rows)

# COMMAND ----------

def evaluate_rules_single_query(metrics_df: DataFrame, config: Config, target_date: datetime) -> DataFrame:
    """
    Evaluate all rules in a single pass:
    1. Compute all aggregations in one query
    2. Join with thresholds
    3. Filter where deviation > threshold
    """
    # Step 1: Compute aggregations
    print("Computing aggregations...")
    agg_df = compute_rule_aggregations(metrics_df, target_date)
    
    # Step 2: Build thresholds DataFrame
    thresholds_df = build_monitor_thresholds(config)
    
    # Step 3: Join aggregations with thresholds
    joined_df = agg_df.join(thresholds_df, on="monitor_name", how="inner")
    
    # Step 4: Generate period_over_period alerts
    pop_alerts = joined_df.filter(
        (F.col("pop_enabled") == True) &
        (F.col("current_count") >= F.col("min_volume")) &
        (F.col("previous_count") >= F.col("min_volume")) &
        (F.col("pop_change_pct").isNotNull()) &
        (F.abs(F.col("pop_change_pct")) > F.col("pop_max_change_pct"))
    ).select(
        F.col("monitor_name"),
        F.col("metric_name"),
        F.col("dimension_key"),
        F.col("dimension_value"),
        F.lit("period_over_period").alias("rule_name"),
        F.col("pop_severity").alias("severity"),
        F.lit("anomaly").alias("alert_type"),
        F.col("current_avg").alias("current_value"),
        F.col("previous_avg").alias("expected_value"),
        (F.col("pop_change_pct") * 100).alias("deviation_pct"),
        F.concat(
            F.col("metric_name"),
            F.when(F.col("pop_change_pct") > 0, F.lit(" increased by ")).otherwise(F.lit(" decreased by ")),
            F.format_string("%.1f", F.abs(F.col("pop_change_pct") * 100)),
            F.lit("% (current: "),
            F.format_string("%.4f", F.col("current_avg")),
            F.lit(", previous: "),
            F.format_string("%.4f", F.col("previous_avg")),
            F.lit(")")
        ).alias("message")
    )
    
    # Step 5: Generate day_over_year alerts
    yoy_alerts = joined_df.filter(
        (F.col("yoy_enabled") == True) &
        (F.col("target_day_value").isNotNull()) &
        (F.col("yoy_value").isNotNull()) &
        (F.col("yoy_change_pct").isNotNull()) &
        (F.abs(F.col("yoy_change_pct")) > F.col("yoy_max_change_pct"))
    ).select(
        F.col("monitor_name"),
        F.col("metric_name"),
        F.col("dimension_key"),
        F.col("dimension_value"),
        F.lit("day_over_year").alias("rule_name"),
        F.col("yoy_severity").alias("severity"),
        F.lit("anomaly").alias("alert_type"),
        F.col("target_day_value").alias("current_value"),
        F.col("yoy_value").alias("expected_value"),
        (F.col("yoy_change_pct") * 100).alias("deviation_pct"),
        F.concat(
            F.col("metric_name"),
            F.when(F.col("yoy_change_pct") > 0, F.lit(" increased by ")).otherwise(F.lit(" decreased by ")),
            F.format_string("%.1f", F.abs(F.col("yoy_change_pct") * 100)),
            F.lit("% YoY (current: "),
            F.format_string("%.4f", F.col("target_day_value")),
            F.lit(", last year: "),
            F.format_string("%.4f", F.col("yoy_value")),
            F.lit(")")
        ).alias("message")
    )
    
    # Step 6: Union all alerts
    all_alerts = pop_alerts.unionByName(yoy_alerts)
    
    # Add metadata columns
    all_alerts = all_alerts.withColumn("date", F.lit(target_date.strftime("%Y-%m-%d")).cast("date"))
    all_alerts = all_alerts.withColumn("lower_bound", F.lit(None).cast("double"))
    all_alerts = all_alerts.withColumn("upper_bound", F.lit(None).cast("double"))
    all_alerts = all_alerts.withColumn("created_at", F.current_timestamp())
    
    return all_alerts

# COMMAND ----------

print("Evaluating rules...")
alerts_df = evaluate_rules_single_query(metrics_df, config, target_date)
alerts_count = alerts_df.count()

if alerts_count > 0:
    print(f"Generated {alerts_count} alerts")
    display(alerts_df)
else:
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
if alerts_count > 0:
    spark.sql(f"DELETE FROM payments_hf.observe_alerts_daily WHERE date = '{end_date}'")
    alerts_df.write.format("delta").mode("append").saveAsTable("payments_hf.observe_alerts_daily")
    print(f"Written {alerts_count} alerts")

# COMMAND ----------

# Save hashes for next run
save_hashes(new_hashes)
print("Saved monitor hashes")

# Unpersist cached DataFrame
metrics_df.unpersist()

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
