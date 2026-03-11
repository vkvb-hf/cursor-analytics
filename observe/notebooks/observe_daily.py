# Databricks notebook source
# MAGIC %md
# MAGIC # Observe Daily Monitoring
# MAGIC
# MAGIC Single notebook that handles everything:
# MAGIC 1. Setup (config sync, table creation)
# MAGIC 2. Smart backfill (720 days if config changed, 30 days otherwise)
# MAGIC 3. Metric computation with hierarchy roll-ups
# MAGIC 4. Auto-threshold calibration and evaluation
# MAGIC 5. Alert deduplication via hierarchy suppression

# COMMAND ----------

dbutils.widgets.text("target_date", "", "Target Date (YYYY-MM-DD)")
dbutils.widgets.text("slack_bot_token", "", "Slack Bot Token (optional, uses secrets if empty)")
dbutils.widgets.text("output_database", "payments_hf", "Output Database")
dbutils.widgets.text("metrics_table", "observe_metrics_daily", "Metrics Table Name")
dbutils.widgets.text("alerts_table", "observe_alerts_daily", "Alerts Table Name")
dbutils.widgets.text("threads_table", "observe_slack_threads", "Slack Threads Table Name")
dbutils.widgets.text("config_path", "/dbfs/observe/config", "Config Path (DBFS)")
dbutils.widgets.text("state_path", "/dbfs/observe/state", "State Path (DBFS)")

# COMMAND ----------

# Get widget values
OUTPUT_DATABASE = dbutils.widgets.get("output_database")
METRICS_TABLE = dbutils.widgets.get("metrics_table")
ALERTS_TABLE = dbutils.widgets.get("alerts_table")
THREADS_TABLE = dbutils.widgets.get("threads_table")
CONFIG_PATH = dbutils.widgets.get("config_path")
STATE_PATH = dbutils.widgets.get("state_path")

# Target date from widget or default to yesterday
_target_date_str = dbutils.widgets.get("target_date")
if _target_date_str:
    target_date = datetime.strptime(_target_date_str, "%Y-%m-%d")
else:
    target_date = datetime.now() - timedelta(days=1)

# Fully qualified table names
METRICS_TABLE_FQN = f"{OUTPUT_DATABASE}.{METRICS_TABLE}"
ALERTS_TABLE_FQN = f"{OUTPUT_DATABASE}.{ALERTS_TABLE}"
THREADS_TABLE_FQN = f"{OUTPUT_DATABASE}.{THREADS_TABLE}"

print(f"Output tables: {METRICS_TABLE_FQN}, {ALERTS_TABLE_FQN}, {THREADS_TABLE_FQN}")
print(f"Config path: {CONFIG_PATH}")
print(f"State path: {STATE_PATH}")
print(f"Target date: {target_date.strftime('%Y-%m-%d')}")

# COMMAND ----------

import yaml
import hashlib
import json
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
from functools import reduce
from pyspark.sql import functions as F, DataFrame
from pyspark.sql.window import Window
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
    diagnosis: Dict[str, str] = field(default_factory=dict)

@dataclass
class Metric:
    name: str
    source: str
    type: str
    filter: str = None
    numerator: str = None
    denominator: str = None
    description: str = ""
    is_p0: bool = False
    is_ratio: bool = False
    increase_is_good: bool = True
    team_ownership: str = ""

@dataclass
class AutoThresholdRule:
    enabled: bool = True
    comparison: str = "same_weekday"
    calibration_days: int = 365
    target_flag_rate: float = 0.05
    min_denominator: int = 30
    severity_map: Dict[str, float] = field(default_factory=lambda: {"critical": 3.0, "warning": 1.0})

@dataclass
class Monitor:
    name: str
    metrics: List[str]
    dimensions: List[List[str]]
    hierarchy: List[List[str]]
    rule: AutoThresholdRule
    description: str = ""
    severity: str = "warning"

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

os.makedirs(CONFIG_PATH.replace("/dbfs", "/dbfs"), exist_ok=True)
os.makedirs(STATE_PATH.replace("/dbfs", "/dbfs"), exist_ok=True)
print("DBFS directories ready")

# COMMAND ----------

notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
config_synced = False

if notebook_path.startswith("/Repos"):
    repo_path = notebook_path.rsplit("/", 2)[0]
    config_path = f"{repo_path}/config"
    print(f"Syncing config from Repos: {config_path}")
    try:
        for config_file in ["sources.yml", "metrics.yml", "monitors.yml"]:
            with open(f"{config_path}/{config_file}") as f:
                content = f.read()
            with open(f"{CONFIG_PATH}/{config_file}", "w") as f:
                f.write(content)
            print(f"  Synced: {config_file}")
        config_synced = True
    except Exception as e:
        print(f"  Failed: {e}")

if not config_synced and "/Users/" in notebook_path:
    import requests
    import base64
    workspace_base = notebook_path.rsplit("/", 2)[0]
    config_ws_path = f"{workspace_base}/config"
    print(f"Syncing config from Workspace API: {config_ws_path}")
    try:
        ctx = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
        host = ctx.apiUrl().get()
        token = ctx.apiToken().get()
        headers = {"Authorization": f"Bearer {token}"}
        for config_file in ["sources.yml", "metrics.yml", "monitors.yml"]:
            ws_file_path = f"{config_ws_path}/{config_file}"
            response = requests.get(
                f"{host}/api/2.0/workspace/export",
                headers=headers,
                params={"path": ws_file_path, "format": "SOURCE"}
            )
            response.raise_for_status()
            content = base64.b64decode(response.json().get('content', '')).decode('utf-8')
            with open(f"{CONFIG_PATH}/{config_file}", "w") as f:
                f.write(content)
            print(f"  Synced: {config_file}")
        config_synced = True
    except Exception as e:
        print(f"  Failed: {e}")

if not config_synced:
    print("Checking for existing configs on DBFS...")
    try:
        for config_file in ["sources.yml", "metrics.yml", "monitors.yml"]:
            with open(f"{CONFIG_PATH}/{config_file}") as f:
                _ = f.read()
        print("  Using existing DBFS configs")
        config_synced = True
    except:
        raise Exception(f"No config files found! Sync configs to {CONFIG_PATH}/ first.")

# COMMAND ----------

spark.sql(f"""
CREATE TABLE IF NOT EXISTS {METRICS_TABLE_FQN} (
    date DATE,
    monitor_name STRING,
    metric_name STRING,
    dimension_key STRING,
    dimension_value STRING,
    metric_value DOUBLE,
    metric_numerator DOUBLE,
    metric_denominator DOUBLE,
    rolling_7d_avg DOUBLE,
    rolling_7d_prev_avg DOUBLE,
    rolling_7d_change_pct DOUBLE,
    yoy_metric_value DOUBLE,
    yoy_change_pct DOUBLE,
    historical_avg_denominator DOUBLE,
    same_weekday_prev DOUBLE,
    same_weekday_residual DOUBLE,
    calibrated_k DOUBLE,
    volume_tier STRING,
    source_name STRING,
    metric_type STRING,
    computed_at TIMESTAMP
) USING DELTA PARTITIONED BY (date)
""")

spark.sql(f"""
CREATE TABLE IF NOT EXISTS {ALERTS_TABLE_FQN} (
    date DATE,
    monitor_name STRING,
    metric_name STRING,
    dimension_key STRING,
    dimension_value STRING,
    rule_name STRING,
    severity STRING,
    alert_type STRING,
    current_value DOUBLE,
    expected_value DOUBLE,
    lower_bound DOUBLE,
    upper_bound DOUBLE,
    deviation_pct DOUBLE,
    message STRING,
    suppressed BOOLEAN,
    suppressed_by STRING,
    hierarchy_level INT,
    calibrated_k DOUBLE,
    residual_std DOUBLE,
    denominator_count DOUBLE,
    created_at TIMESTAMP
) USING DELTA PARTITIONED BY (date)
""")

spark.sql(f"""
CREATE TABLE IF NOT EXISTS {THREADS_TABLE_FQN} (
    date DATE,
    channel STRING,
    thread_ts STRING,
    message_type STRING,
    created_at TIMESTAMP
) USING DELTA
""")
print(f"Tables ready: {METRICS_TABLE_FQN}, {ALERTS_TABLE_FQN}, {THREADS_TABLE_FQN}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Load Config

# COMMAND ----------

def _filter_fields(data: dict, cls) -> dict:
    return {k: v for k, v in data.items() if k in cls.__dataclass_fields__}

def load_config() -> Config:
    with open(f"{CONFIG_PATH}/sources.yml") as f:
        sources_data = yaml.safe_load(f)
    with open(f"{CONFIG_PATH}/metrics.yml") as f:
        metrics_data = yaml.safe_load(f)
    with open(f"{CONFIG_PATH}/monitors.yml") as f:
        monitors_data = yaml.safe_load(f)

    sources = {s['name']: Source(**_filter_fields(s, Source)) for s in sources_data.get('sources', [])}
    metrics = {m['name']: Metric(**_filter_fields(m, Metric)) for m in metrics_data.get('metrics', [])}
    defaults = monitors_data.get('defaults', {})

    monitors = []
    for m in monitors_data.get('monitors', []):
        rule_cfg = m.get('rules', {}).get('auto_threshold', {})
        rule = AutoThresholdRule(**_filter_fields(rule_cfg, AutoThresholdRule)) if rule_cfg else AutoThresholdRule()
        monitors.append(Monitor(
            name=m['name'],
            metrics=m.get('metrics', []),
            dimensions=m.get('dimensions', [[]]),
            hierarchy=m.get('hierarchy', []),
            rule=rule,
            description=m.get('description', ''),
            severity=m.get('severity', 'warning'),
        ))

    return Config(sources=sources, metrics=metrics, monitors=monitors, defaults=defaults)

config = load_config()
print(f"Loaded {len(config.sources)} sources, {len(config.metrics)} metrics, {len(config.monitors)} monitors")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3: Smart Backfill (Hash-Based)

# COMMAND ----------

def compute_monitor_hash(monitor: Monitor, config: Config) -> str:
    hash_input = {
        "monitor_name": monitor.name,
        "metrics": [],
        "dimensions": monitor.dimensions,
        "hierarchy": monitor.hierarchy,
    }
    for metric_name in monitor.metrics:
        metric = config.metrics.get(metric_name)
        if metric:
            source = config.sources.get(metric.source)
            hash_input["metrics"].append({
                "name": metric.name,
                "source": metric.source,
                "type": metric.type,
                "filter": metric.filter,
                "numerator": metric.numerator,
                "denominator": metric.denominator,
                "source_table": f"{source.database}.{source.table}" if source else None,
                "source_filters": source.filters if source else []
            })
    return hashlib.md5(json.dumps(hash_input, sort_keys=True).encode()).hexdigest()

def load_stored_hashes() -> Dict[str, str]:
    try:
        with open(f"{STATE_PATH}/monitor_hashes.json") as f:
            return json.load(f)
    except:
        return {}

def save_hashes(hashes: Dict[str, str]):
    with open(f"{STATE_PATH}/monitor_hashes.json", "w") as f:
        json.dump(hashes, f)

# COMMAND ----------

stored_hashes = load_stored_hashes()
new_hashes = {}
monitor_lookbacks = {}

historical_days = config.defaults.get('historical_lookback_days', 720)
refresh_days = config.defaults.get('refresh_lookback_days', 30)

print(f"Config: historical={historical_days}d, refresh={refresh_days}d")
print("-" * 50)

for monitor in config.monitors:
    current_hash = compute_monitor_hash(monitor, config)
    stored_hash = stored_hashes.get(monitor.name)
    new_hashes[monitor.name] = current_hash

    if stored_hash != current_hash:
        monitor_lookbacks[monitor.name] = historical_days
        reason = "NEW" if not stored_hash else "CHANGED"
        print(f"{monitor.name}: {reason} -> {historical_days}d backfill")
    else:
        monitor_lookbacks[monitor.name] = refresh_days
        print(f"{monitor.name}: unchanged -> {refresh_days}d refresh")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 4: Compute Metrics

# COMMAND ----------

def compute_metric_granular(
    config: Config,
    metric: Metric,
    dimensions: List[str],
    target_date: datetime,
    lookback_days: int
) -> DataFrame:
    """Compute a single ratio metric at the most granular dimension level."""
    source = config.sources[metric.source]
    start_date = target_date - timedelta(days=lookback_days)

    df = spark.table(f"{source.database}.{source.table}")

    # Build column expression lookup from source config
    # Allows columns to have custom expressions (e.g., nested structs, CASE WHEN)
    column_expressions = {}
    for col_config in source.columns:
        col_name = col_config.get("name")
        col_expr = col_config.get("expression")
        if col_name and col_expr:
            column_expressions[col_name] = col_expr

    # Apply column expressions - create aliased columns for any with expressions
    for col_name, expr in column_expressions.items():
        df = df.withColumn(col_name, F.expr(expr))

    # Date filter
    date_col = F.col(source.date_column)
    if "string" in str(df.schema[source.date_column].dataType).lower():
        date_col = F.to_date(date_col)
    df = df.filter((date_col >= start_date) & (date_col <= target_date))

    # Source-level filters
    for flt in source.filters:
        df = df.filter(flt)

    # Metric-level filter (workflow)
    if metric.filter:
        df = df.filter(eval(metric.filter))

    # Cast boolean dimensions to string
    for dim in dimensions:
        if dim in [f.name for f in df.schema.fields]:
            if str(df.schema[dim].dataType) == "BooleanType":
                df = df.withColumn(dim, F.col(dim).cast("string"))

    # Group by date + dimensions
    group_cols = [F.to_date(F.col(source.date_column)).alias("date")] + [F.col(dim) for dim in dimensions]
    grouped = df.groupBy(group_cols)

    result = grouped.agg(
        eval(metric.numerator).alias("numerator"),
        eval(metric.denominator).alias("denominator")
    )
    result = result.withColumn(
        "metric_value",
        F.when(F.col("denominator") > 0, F.col("numerator") / F.col("denominator")).otherwise(None)
    )

    # Metadata
    result = result.withColumn("metric_name", F.lit(metric.name))
    result = result.withColumn("metric_type", F.lit(metric.type))
    result = result.withColumn("source_name", F.lit(metric.source))

    dim_key = ",".join(dimensions) if dimensions else "global"
    result = result.withColumn("dimension_key", F.lit(dim_key))

    if dimensions:
        dim_value_expr = F.concat_ws(",", *[F.coalesce(F.col(d).cast("string"), F.lit("_null_")) for d in dimensions])
    else:
        dim_value_expr = F.lit("global")
    result = result.withColumn("dimension_value", dim_value_expr)

    return result

# COMMAND ----------

def compute_hierarchy_rollups(
    granular_df: DataFrame,
    hierarchy: List[List[str]],
    granular_dims: List[str],
    monitor_name: str
) -> DataFrame:
    """
    Roll up granular metrics to each hierarchy level.
    Ratio metrics: SUM(numerator) / SUM(denominator).
    """
    # Parse individual dimension values from comma-separated dimension_value
    with_parsed = granular_df
    for i, dim in enumerate(granular_dims):
        with_parsed = with_parsed.withColumn(
            f"_dim_{dim}",
            F.split(F.col("dimension_value"), ",").getItem(i)
        )

    all_levels = []

    for level_dims in hierarchy:
        level_key = ",".join(level_dims) if level_dims else "global"

        if level_dims == granular_dims:
            level_df = with_parsed
            all_levels.append(level_df)
            continue

        group_cols = ["date", "metric_name", "metric_type", "source_name"]
        group_cols += [f"_dim_{d}" for d in level_dims]

        rolled = with_parsed.groupBy(group_cols).agg(
            F.sum("numerator").alias("numerator"),
            F.sum("denominator").alias("denominator"),
        )
        rolled = rolled.withColumn(
            "metric_value",
            F.when(F.col("denominator") > 0, F.col("numerator") / F.col("denominator")).otherwise(None)
        )

        rolled = rolled.withColumn("dimension_key", F.lit(level_key))
        if level_dims:
            rolled = rolled.withColumn(
                "dimension_value",
                F.concat_ws(",", *[F.col(f"_dim_{d}") for d in level_dims])
            )
        else:
            rolled = rolled.withColumn("dimension_value", F.lit("global"))

        # Add missing parsed dim columns for union compatibility
        for dim in granular_dims:
            col_name = f"_dim_{dim}"
            if col_name not in rolled.columns:
                rolled = rolled.withColumn(col_name, F.lit(None).cast("string"))

        all_levels.append(rolled)

    # Standardize columns and union
    standard_cols = [
        "date", "metric_name", "metric_type", "source_name",
        "dimension_key", "dimension_value",
        "metric_value", "numerator", "denominator",
    ]

    standardized = []
    for df in all_levels:
        for col in standard_cols:
            if col not in df.columns:
                df = df.withColumn(col, F.lit(None))
        standardized.append(df.select(standard_cols))

    combined = reduce(DataFrame.unionByName, standardized)
    combined = combined.withColumn("monitor_name", F.lit(monitor_name))
    return combined

# COMMAND ----------

def compute_all_metrics(config: Config, target_date: datetime, monitor_lookbacks: Dict[str, int]) -> DataFrame:
    all_results = []

    for monitor in config.monitors:
        lookback = monitor_lookbacks[monitor.name]
        granular_dims = monitor.dimensions[0] if monitor.dimensions else []
        print(f"\nComputing {monitor.name} ({lookback}d lookback)...")

        for metric_name in monitor.metrics:
            metric = config.metrics.get(metric_name)
            if not metric:
                print(f"  ! Metric {metric_name} not found")
                continue
            try:
                granular_df = compute_metric_granular(config, metric, granular_dims, target_date, lookback)
                rolled_up = compute_hierarchy_rollups(granular_df, monitor.hierarchy, granular_dims, monitor.name)
                all_results.append(rolled_up)
                levels_str = " | ".join([",".join(h) or "global" for h in monitor.hierarchy])
                print(f"  + {metric_name} [{levels_str}]")
            except Exception as e:
                print(f"  ! {metric_name}: {e}")

    if not all_results:
        return None

    base_cols = [
        "date", "monitor_name", "source_name", "metric_name", "metric_type",
        "dimension_key", "dimension_value", "metric_value", "numerator", "denominator"
    ]

    standardized = []
    for df in all_results:
        for col in base_cols:
            if col not in df.columns:
                df = df.withColumn(col, F.lit(None))
        for col in ["metric_value", "numerator", "denominator"]:
            df = df.withColumn(col, F.col(col).cast("double"))
        standardized.append(df.select(base_cols))

    combined = reduce(DataFrame.unionByName, standardized)
    return combined.withColumn("computed_at", F.current_timestamp())

# COMMAND ----------

print("Computing metrics...")
metrics_df = compute_all_metrics(config, target_date, monitor_lookbacks)

if metrics_df:
    metrics_df.cache()
    metrics_count = metrics_df.count()
    print(f"\nTotal: {metrics_count} metric records")
else:
    print("No metrics computed")
    dbutils.notebook.exit("No metrics")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 5: Calibrate Auto-Thresholds

# COMMAND ----------

def calibrate_k_values(
    metrics_df: DataFrame,
    target_date: datetime,
    calibration_days: int,
    target_flag_rate: float,
    min_denominator: int
) -> DataFrame:
    """
    Calibrate k-values from historical same-weekday residuals.

    For each metric x dimension combo:
    1. Pair each day with same weekday 7 days prior
    2. Compute residuals and their std
    3. Find k such that |residual| > k * std for ~target_flag_rate of days
    """
    cal_start = (target_date - timedelta(days=calibration_days)).strftime("%Y-%m-%d")
    cal_end = target_date.strftime("%Y-%m-%d")

    cal_df = metrics_df.filter(
        (F.col("date") >= cal_start) & (F.col("date") <= cal_end)
    )

    # Create separate DataFrames with prefixed column names to avoid ambiguity
    curr = cal_df.select(
        F.col("date").alias("curr_date"),
        F.col("monitor_name").alias("curr_monitor"),
        F.col("metric_name").alias("curr_metric"),
        F.col("dimension_key").alias("curr_dim_key"),
        F.col("dimension_value").alias("curr_dim_value"),
        F.col("metric_value").alias("curr_value"),
        F.col("denominator").alias("curr_denom")
    )

    prev = cal_df.select(
        F.col("date").alias("prev_date"),
        F.col("monitor_name").alias("prev_monitor"),
        F.col("metric_name").alias("prev_metric"),
        F.col("dimension_key").alias("prev_dim_key"),
        F.col("dimension_value").alias("prev_dim_value"),
        F.col("metric_value").alias("prev_value")
    )

    pairs = curr.join(
        prev,
        on=[
            curr["curr_metric"] == prev["prev_metric"],
            curr["curr_monitor"] == prev["prev_monitor"],
            curr["curr_dim_key"] == prev["prev_dim_key"],
            curr["curr_dim_value"] == prev["prev_dim_value"],
            curr["curr_date"] == F.date_add(prev["prev_date"], 7)
        ],
        how="inner"
    ).select(
        F.col("curr_monitor").alias("monitor_name"),
        F.col("curr_metric").alias("metric_name"),
        F.col("curr_dim_key").alias("dimension_key"),
        F.col("curr_dim_value").alias("dimension_value"),
        "curr_date",
        "curr_value",
        "prev_value",
        "curr_denom",
        (F.col("curr_value") - F.col("prev_value")).alias("residual")
    )

    pairs = pairs.filter(
        (F.col("curr_denom").isNotNull()) &
        (F.col("curr_denom") >= min_denominator) &
        (F.col("curr_value").isNotNull()) &
        (F.col("prev_value").isNotNull())
    )

    quantile_target = 1.0 - target_flag_rate

    combo_stats = pairs.groupBy(
        "monitor_name", "metric_name", "dimension_key", "dimension_value"
    ).agg(
        F.stddev("residual").alias("residual_std"),
        F.count("*").alias("n_pairs"),
        F.avg("curr_denom").alias("avg_denominator"),
        F.percentile_approx(F.abs(F.col("residual")), quantile_target).alias("abs_residual_pctile")
    )

    # k = percentile(|residual|) / std. Fall back to k=3.0 if insufficient data.
    combo_stats = combo_stats.withColumn(
        "calibrated_k",
        F.when(
            (F.col("residual_std") > 0) & (F.col("n_pairs") >= 20),
            F.col("abs_residual_pctile") / F.col("residual_std")
        ).otherwise(F.lit(3.0))
    )

    combo_stats = combo_stats.withColumn(
        "volume_tier",
        F.when(F.col("avg_denominator") >= 500, "high")
         .when(F.col("avg_denominator") >= 100, "medium")
         .otherwise("low")
    )

    return combo_stats

# COMMAND ----------

print("Calibrating auto-thresholds...")
k_values_per_monitor = {}

for monitor in config.monitors:
    if not monitor.rule.enabled:
        continue

    monitor_metrics = metrics_df.filter(F.col("monitor_name") == monitor.name)

    k_df = calibrate_k_values(
        monitor_metrics,
        target_date,
        calibration_days=monitor.rule.calibration_days,
        target_flag_rate=monitor.rule.target_flag_rate,
        min_denominator=monitor.rule.min_denominator
    )
    k_df.cache()

    k_count = k_df.count()
    print(f"\n  {monitor.name}: {k_count} combos calibrated")
    if k_count > 0:
        k_df.select(
            F.round(F.avg("calibrated_k"), 2).alias("avg_k"),
            F.round(F.min("calibrated_k"), 2).alias("min_k"),
            F.round(F.max("calibrated_k"), 2).alias("max_k"),
            F.round(F.avg("n_pairs"), 0).alias("avg_pairs"),
        ).show()

    k_values_per_monitor[monitor.name] = k_df

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 6: Evaluate Thresholds and Deduplicate

# COMMAND ----------

def evaluate_auto_threshold(
    metrics_df: DataFrame,
    k_values_df: DataFrame,
    monitor: Monitor,
    target_date: datetime
) -> DataFrame:
    """Compare today's value to same-weekday-last-week against calibrated k * std."""
    target_str = target_date.strftime("%Y-%m-%d")
    prev_week_str = (target_date - timedelta(days=7)).strftime("%Y-%m-%d")

    monitor_metrics = metrics_df.filter(F.col("monitor_name") == monitor.name)

    today = monitor_metrics.filter(F.col("date") == target_str)
    last_week = monitor_metrics.filter(F.col("date") == prev_week_str).select(
        "metric_name", "dimension_key", "dimension_value",
        F.col("metric_value").alias("prev_week_value"),
    )

    compared = today.join(
        last_week,
        on=["metric_name", "dimension_key", "dimension_value"],
        how="inner"
    )

    compared = compared.join(
        k_values_df.select(
            "monitor_name", "metric_name", "dimension_key", "dimension_value",
            "calibrated_k", "residual_std", "avg_denominator", "volume_tier"
        ),
        on=["monitor_name", "metric_name", "dimension_key", "dimension_value"],
        how="inner"
    )

    compared = compared.withColumn(
        "residual", F.col("metric_value") - F.col("prev_week_value")
    ).withColumn(
        "abs_residual", F.abs(F.col("residual"))
    ).withColumn(
        "threshold", F.col("calibrated_k") * F.col("residual_std")
    )

    # Filter: volume >= min_denom AND exceeds threshold
    alerts = compared.filter(
        (F.col("denominator") >= monitor.rule.min_denominator) &
        (F.col("residual_std") > 0) &
        (F.col("abs_residual") > F.col("threshold"))
    )

    # Severity
    critical_k = monitor.rule.severity_map.get("critical", 3.0)
    alerts = alerts.withColumn(
        "severity",
        F.when(
            F.col("abs_residual") > F.lit(critical_k) * F.col("residual_std"), "critical"
        ).otherwise("warning")
    )

    alerts = alerts.withColumn(
        "deviation_pct",
        F.when(F.col("prev_week_value") != 0,
               (F.col("residual") / F.col("prev_week_value")) * 100
        ).otherwise(None)
    ).withColumn(
        "lower_bound", F.col("prev_week_value") - F.col("threshold")
    ).withColumn(
        "upper_bound", F.col("prev_week_value") + F.col("threshold")
    )

    # Hierarchy level mapping
    hierarchy_map = {(",".join(d) if d else "global"): i for i, d in enumerate(monitor.hierarchy)}
    hierarchy_expr = F.lit(None).cast("int")
    for dim_key, level in hierarchy_map.items():
        hierarchy_expr = F.when(F.col("dimension_key") == dim_key, F.lit(level)).otherwise(hierarchy_expr)

    alerts = alerts.withColumn(
        "message",
        F.concat(
            F.col("metric_name"),
            F.when(F.col("residual") < 0, F.lit(" dropped ")).otherwise(F.lit(" increased ")),
            F.format_string("%.2f", F.abs(F.col("deviation_pct"))),
            F.lit("% vs same weekday last week ("),
            F.format_string("%.4f", F.col("metric_value")),
            F.lit(" vs "),
            F.format_string("%.4f", F.col("prev_week_value")),
            F.lit(", k="),
            F.format_string("%.2f", F.col("calibrated_k")),
            F.lit(")")
        )
    )

    return alerts.select(
        F.lit(target_str).cast("date").alias("date"),
        "monitor_name", "metric_name", "dimension_key", "dimension_value",
        F.lit("auto_threshold").alias("rule_name"),
        "severity",
        F.lit("anomaly").alias("alert_type"),
        F.col("metric_value").alias("current_value"),
        F.col("prev_week_value").alias("expected_value"),
        "lower_bound", "upper_bound", "deviation_pct", "message",
        F.lit(False).alias("suppressed"),
        F.lit(None).cast("string").alias("suppressed_by"),
        hierarchy_expr.alias("hierarchy_level"),
        "calibrated_k", "residual_std",
        F.col("denominator").alias("denominator_count"),
        F.current_timestamp().alias("created_at")
    )

# COMMAND ----------

def deduplicate_alerts(alerts_df: DataFrame, hierarchy: List[List[str]]) -> DataFrame:
    """
    Suppress child alerts when a parent level also fires for the same metric.

    Walks from coarsest to finest. If global fires, suppress country-level etc.
    If only NL fires at country level, suppress NL's children but not DE's.
    """
    if not hierarchy or alerts_df.rdd.isEmpty():
        return alerts_df

    level_keys = [",".join(dims) if dims else "global" for dims in hierarchy]
    result = alerts_df

    for child_idx in range(1, len(hierarchy)):
        parent_key = level_keys[child_idx - 1]
        child_key = level_keys[child_idx]
        parent_dims = hierarchy[child_idx - 1]

        # Parent alerts that fired and are not themselves suppressed
        parent_fired = result.filter(
            (F.col("dimension_key") == parent_key) &
            (F.col("suppressed") == False)
        ).select(
            F.col("metric_name").alias("_p_metric"),
            F.col("dimension_value").alias("_p_dim_value"),
            F.lit(True).alias("_parent_fired")
        ).distinct()

        if parent_fired.rdd.isEmpty():
            continue

        # Split child and non-child alerts
        child_alerts = result.filter(F.col("dimension_key") == child_key)
        other_alerts = result.filter(F.col("dimension_key") != child_key)

        # Build the parent-matching portion of the child's dimension_value
        if not parent_dims:
            # Parent is global: all children match
            child_alerts = child_alerts.withColumn("_match_value", F.lit("global"))
        else:
            n = len(parent_dims)
            split_col = F.split(F.col("dimension_value"), ",")
            child_alerts = child_alerts.withColumn(
                "_match_value",
                F.concat_ws(",", *[split_col.getItem(i) for i in range(n)])
            )

        # Join
        child_alerts = child_alerts.join(
            parent_fired,
            on=[
                child_alerts["metric_name"] == parent_fired["_p_metric"],
                child_alerts["_match_value"] == parent_fired["_p_dim_value"]
            ],
            how="left"
        )

        child_alerts = child_alerts.withColumn(
            "suppressed",
            F.when(F.col("_parent_fired") == True, True).otherwise(F.col("suppressed"))
        ).withColumn(
            "suppressed_by",
            F.when(
                F.col("_parent_fired") == True,
                F.concat(F.lit(parent_key), F.lit("="), F.col("_match_value"))
            ).otherwise(F.col("suppressed_by"))
        ).drop("_match_value", "_p_metric", "_p_dim_value", "_parent_fired")

        result = other_alerts.unionByName(child_alerts)

    return result

# COMMAND ----------

print("Evaluating thresholds...")
all_alerts = []

for monitor in config.monitors:
    if not monitor.rule.enabled:
        continue

    k_df = k_values_per_monitor.get(monitor.name)
    if k_df is None:
        continue

    print(f"\n  {monitor.name}:")
    raw_alerts = evaluate_auto_threshold(metrics_df, k_df, monitor, target_date)
    raw_count = raw_alerts.count()
    print(f"    Raw alerts: {raw_count}")

    if raw_count > 0 and monitor.hierarchy:
        deduped = deduplicate_alerts(raw_alerts, monitor.hierarchy)
        active = deduped.filter(F.col("suppressed") == False).count()
        suppressed = raw_count - active
        print(f"    Active: {active}, Suppressed: {suppressed}")
        all_alerts.append(deduped)
    elif raw_count > 0:
        all_alerts.append(raw_alerts)

if all_alerts:
    alerts_df = reduce(DataFrame.unionByName, all_alerts)
    alerts_count = alerts_df.count()
    active_count = alerts_df.filter(F.col("suppressed") == False).count()
    print(f"\nTotal: {alerts_count} alerts ({active_count} active, {alerts_count - active_count} suppressed)")
else:
    alerts_df = None
    alerts_count = 0
    print("\nNo alerts generated")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 7: Enrich Metrics and Write

# COMMAND ----------

max_lookback = max(monitor_lookbacks.values())
start_date = (target_date - timedelta(days=max_lookback)).strftime("%Y-%m-%d")
end_date = target_date.strftime("%Y-%m-%d")

spark.sql(f"DELETE FROM {METRICS_TABLE_FQN} WHERE date BETWEEN '{start_date}' AND '{end_date}'")
print(f"Cleared metrics for {start_date} to {end_date}")

# COMMAND ----------

# Rolling 7d averages
partition_cols = ["monitor_name", "metric_name", "dimension_key", "dimension_value"]
rolling_window = Window.partitionBy(partition_cols).orderBy("date").rowsBetween(-6, 0)
prev_window = Window.partitionBy(partition_cols).orderBy("date").rowsBetween(-13, -7)

enriched = metrics_df.withColumn(
    "rolling_7d_avg", F.avg("metric_value").over(rolling_window)
).withColumn(
    "rolling_7d_prev_avg", F.avg("metric_value").over(prev_window)
).withColumn(
    "rolling_7d_change_pct",
    F.when(
        (F.col("rolling_7d_prev_avg").isNotNull()) & (F.col("rolling_7d_prev_avg") != 0),
        (F.col("rolling_7d_avg") - F.col("rolling_7d_prev_avg")) / F.col("rolling_7d_prev_avg")
    )
)

# YoY via self-join
yoy_source = metrics_df.select(
    *partition_cols,
    F.date_add(F.col("date"), 365).alias("yoy_join_date"),
    F.col("metric_value").alias("yoy_metric_value")
)
enriched = enriched.join(
    yoy_source,
    on=[enriched[c] == yoy_source[c] for c in partition_cols] + [enriched["date"] == yoy_source["yoy_join_date"]],
    how="left"
).select(enriched["*"], yoy_source["yoy_metric_value"])

enriched = enriched.withColumn(
    "yoy_change_pct",
    F.when(
        (F.col("yoy_metric_value").isNotNull()) & (F.col("yoy_metric_value") != 0),
        (F.col("metric_value") - F.col("yoy_metric_value")) / F.col("yoy_metric_value")
    )
)

# Same-weekday previous via self-join
sw_source = metrics_df.select(
    *partition_cols,
    F.date_add(F.col("date"), 7).alias("sw_join_date"),
    F.col("metric_value").alias("same_weekday_prev")
)
enriched = enriched.join(
    sw_source,
    on=[enriched[c] == sw_source[c] for c in partition_cols] + [enriched["date"] == sw_source["sw_join_date"]],
    how="left"
).select(enriched["*"], sw_source["same_weekday_prev"])

enriched = enriched.withColumn(
    "same_weekday_residual",
    F.when(F.col("same_weekday_prev").isNotNull(), F.col("metric_value") - F.col("same_weekday_prev"))
)

# Join calibrated k-values
all_k = None
for monitor_name, k_df in k_values_per_monitor.items():
    subset = k_df.select(
        "monitor_name", "metric_name", "dimension_key", "dimension_value",
        F.col("calibrated_k").alias("_cal_k"),
        "volume_tier"
    )
    all_k = subset if all_k is None else all_k.unionByName(subset)

if all_k is not None:
    enriched = enriched.join(
        all_k,
        on=["monitor_name", "metric_name", "dimension_key", "dimension_value"],
        how="left"
    ).withColumnRenamed("_cal_k", "calibrated_k")
else:
    enriched = enriched.withColumn("calibrated_k", F.lit(None).cast("double"))
    enriched = enriched.withColumn("volume_tier", F.lit(None).cast("string"))

# Historical avg denominator
hist_avg = metrics_df.groupBy(partition_cols).agg(
    F.avg("denominator").alias("historical_avg_denominator")
)
enriched = enriched.join(hist_avg, on=partition_cols, how="left")

# Final select
enriched = enriched.select(
    "date", "monitor_name", "metric_name", "dimension_key", "dimension_value",
    "metric_value",
    F.col("numerator").alias("metric_numerator"),
    F.col("denominator").alias("metric_denominator"),
    "rolling_7d_avg", "rolling_7d_prev_avg", "rolling_7d_change_pct",
    "yoy_metric_value", "yoy_change_pct",
    "historical_avg_denominator",
    "same_weekday_prev", "same_weekday_residual",
    "calibrated_k", "volume_tier",
    "source_name", "metric_type",
    F.current_timestamp().alias("computed_at")
)

enriched.write.format("delta").mode("append").option("mergeSchema", "true").partitionBy("date").saveAsTable(METRICS_TABLE_FQN)
enriched_count = enriched.count()
print(f"Written {enriched_count} enriched metrics")

# COMMAND ----------

if alerts_df is not None and alerts_count > 0:
    spark.sql(f"DELETE FROM {ALERTS_TABLE_FQN} WHERE date = '{end_date}'")
    alerts_df.write.format("delta").mode("append").option("mergeSchema", "true").saveAsTable(ALERTS_TABLE_FQN)
    active = alerts_df.filter(F.col("suppressed") == False).count()
    print(f"Written {alerts_count} alerts ({active} active)")
else:
    print("No alerts to write")

# COMMAND ----------

save_hashes(new_hashes)
print("Saved monitor hashes")

metrics_df.unpersist()
for k_df in k_values_per_monitor.values():
    k_df.unpersist()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 8: Diagnosis Functions

# COMMAND ----------

def get_error_breakdown(
    source: Source,
    dimension_filters: Dict[str, str],
    target_date: str,
    prev_date: str,
    config: Config,
    top_n: int = 5
) -> List[Dict]:
    """
    Query error breakdown for a source, comparing target_date vs prev_date.
    Returns list of dicts with: error, current_cnt, prev_cnt, delta
    """
    diagnosis_cfg = source.diagnosis
    if not diagnosis_cfg:
        return []
    
    error_column = diagnosis_cfg.get("error_column")
    failure_filter = diagnosis_cfg.get("failure_filter")
    
    if not error_column or not failure_filter:
        return []
    
    table_fqn = f"{source.database}.{source.table}"
    date_col = source.date_column
    
    # Build dimension filter clause
    dim_clauses = []
    for dim_key, dim_value in dimension_filters.items():
        if dim_value and dim_value != "global":
            dim_clauses.append(f"{dim_key} = '{dim_value}'")
    dim_filter = " AND ".join(dim_clauses) if dim_clauses else "1=1"
    
    query = f"""
    WITH current AS (
        SELECT {error_column} as error, COUNT(*) as current_cnt
        FROM {table_fqn}
        WHERE {date_col} = '{target_date}'
          AND {failure_filter}
          AND {dim_filter}
        GROUP BY {error_column}
    ),
    prev AS (
        SELECT {error_column} as error, COUNT(*) as prev_cnt
        FROM {table_fqn}
        WHERE {date_col} = '{prev_date}'
          AND {failure_filter}
          AND {dim_filter}
        GROUP BY {error_column}
    )
    SELECT 
        COALESCE(c.error, p.error) as error,
        COALESCE(c.current_cnt, 0) as current_cnt,
        COALESCE(p.prev_cnt, 0) as prev_cnt,
        COALESCE(c.current_cnt, 0) - COALESCE(p.prev_cnt, 0) as delta
    FROM current c
    FULL OUTER JOIN prev p ON c.error = p.error
    WHERE COALESCE(c.current_cnt, 0) - COALESCE(p.prev_cnt, 0) > 0
    ORDER BY delta DESC
    LIMIT {top_n}
    """
    
    try:
        result = spark.sql(query).collect()
        return [row.asDict() for row in result]
    except Exception as e:
        print(f"Error querying diagnosis for {source.name}: {e}")
        return []

def shorten_error(error: str, max_len: int = 30) -> str:
    """Shorten error message for display."""
    if not error:
        return "Unknown"
    
    # Remove common prefixes
    prefixes = [
        "Failed Verification: ",
        "CHARGE_STATE_FAILURE: ",
        "Refused: ",
        "Refused(",
        "Failed Verification: Refused(",
    ]
    for prefix in prefixes:
        if error.startswith(prefix):
            error = error[len(prefix):]
            break
    
    # Remove trailing parenthesis if we removed "Refused("
    if error.endswith(")"):
        error = error[:-1]
    
    # Truncate if still too long
    if len(error) > max_len:
        error = error[:max_len-3] + "..."
    
    return error

def build_diagnosis_for_alert(
    alert_row: Dict,
    target_date: datetime,
    config: Config
) -> Optional[str]:
    """Build diagnosis message for a single declining alert."""
    metric_name = alert_row["metric_name"]
    dimension_key = alert_row["dimension_key"]
    dimension_value = alert_row["dimension_value"]
    deviation_pct = alert_row["deviation_pct"]
    
    # Get metric and source
    metric = config.metrics.get(metric_name)
    if not metric:
        return None
    
    source = config.sources.get(metric.source)
    if not source or not source.diagnosis:
        return None
    
    # Parse dimensions
    dim_keys = dimension_key.split(",") if dimension_key else []
    dim_values = dimension_value.split(",") if dimension_value else []
    dimension_filters = dict(zip(dim_keys, dim_values))
    
    # Get dates
    target_date_str = target_date.strftime("%Y-%m-%d")
    prev_date = target_date - timedelta(days=7)
    prev_date_str = prev_date.strftime("%Y-%m-%d")
    
    # Query error breakdown
    errors = get_error_breakdown(source, dimension_filters, target_date_str, prev_date_str, config)
    
    if not errors:
        return None
    
    # Format dimension for display
    dim_display = dimension_value.replace(",", "/") if dimension_value else "global"
    
    # Build message
    lines = [f"🔍 *Diagnosis: {dim_display} ({deviation_pct:+.1f}%)*", "", "Top error increases vs last week:"]
    
    total_current = 0
    total_prev = 0
    
    for err in errors:
        error_short = shorten_error(err["error"])
        current = err["current_cnt"]
        prev = err["prev_cnt"]
        delta = err["delta"]
        total_current += current
        total_prev += prev
        lines.append(f"• {error_short}: {prev} → {current} (+{delta})")
    
    # Add total
    if total_prev > 0:
        total_pct = ((total_current - total_prev) / total_prev) * 100
        lines.append(f"\n_Total failures: {total_prev} → {total_current} (+{total_pct:.0f}%)_")
    else:
        lines.append(f"\n_Total failures: {total_prev} → {total_current}_")
    
    return "\n".join(lines)

# COMMAND ----------

def save_thread_ts(date_str: str, channel: str, thread_ts: str, message_type: str = "summary"):
    """Save thread_ts to table for later replies."""
    from datetime import datetime as dt
    spark.sql(f"""
        INSERT INTO {THREADS_TABLE_FQN} (date, channel, thread_ts, message_type, created_at)
        VALUES ('{date_str}', '{channel}', '{thread_ts}', '{message_type}', current_timestamp())
    """)

def get_thread_ts(date_str: str, channel: str) -> Optional[str]:
    """Get thread_ts for a date/channel to post replies."""
    result = spark.sql(f"""
        SELECT thread_ts FROM {THREADS_TABLE_FQN}
        WHERE date = '{date_str}' AND channel = '{channel}' AND message_type = 'summary'
        ORDER BY created_at DESC LIMIT 1
    """).collect()
    return result[0]["thread_ts"] if result else None

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 9: Send Slack Summary

# COMMAND ----------

def send_slack_alert(
    channel: str,
    message: str,
    bot_token: str,
    title: str = "Data Quality Alert",
    severity: str = "warning",
    details: Optional[Dict[str, str]] = None
) -> dict:
    """Send an alert to Slack using the pa_slack_app bot."""
    import requests
    
    colors = {
        "info": "#36a64f",
        "warning": "#ff9800",
        "error": "#dc3545"
    }
    
    blocks = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": title, "emoji": True}
        },
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": message}
        }
    ]
    
    if details:
        fields = [
            {"type": "mrkdwn", "text": f"*{k}:*\n{v}"}
            for k, v in details.items()
        ]
        blocks.append({"type": "section", "fields": fields})
    
    blocks.append({
        "type": "context",
        "elements": [
            {"type": "mrkdwn", "text": f"Sent at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC"}
        ]
    })
    
    payload = {
        "channel": channel,
        "attachments": [{
            "color": colors.get(severity, colors["warning"]),
            "blocks": blocks
        }]
    }
    
    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        json=payload,
        headers={
            "Authorization": f"Bearer {bot_token}",
            "Content-Type": "application/json"
        }
    )
    
    result = response.json()
    if not result.get("ok"):
        raise Exception(f"Slack API error: {result.get('error')}")
    
    return result

def post_to_slack(channel: str, message: str, bot_token: str, thread_ts: str = None) -> dict:
    """Post a simple message to Slack, optionally as a thread reply."""
    payload = {
        "channel": channel,
        "text": message,
    }
    if thread_ts:
        payload["thread_ts"] = thread_ts
    
    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        json=payload,
        headers={
            "Authorization": f"Bearer {bot_token}",
            "Content-Type": "application/json"
        }
    )
    
    result = response.json()
    if not result.get("ok"):
        raise Exception(f"Slack API error: {result.get('error')}")
    
    return result

# COMMAND ----------

def build_slack_summary(alerts_rows: list, target_date: datetime) -> str:
    """Build Slack message from collected alert rows."""
    date_str = target_date.strftime("%Y-%m-%d")
    prev_week_str = (target_date - timedelta(days=7)).strftime("%Y-%m-%d")
    
    if not alerts_rows:
        return f"*No alerts for {date_str}* ✅"
    
    # Filter in Python (already collected)
    active_alerts = [r for r in alerts_rows if not r["suppressed"]]
    suppressed_count = len(alerts_rows) - len(active_alerts)
    
    if not active_alerts:
        return f"*No active alerts for {date_str}* ✅\n_{suppressed_count} alerts suppressed by hierarchy_"
    
    # Count by severity
    critical_alerts = [r for r in active_alerts if r["severity"] == "critical"]
    warning_alerts = [r for r in active_alerts if r["severity"] == "warning"]
    
    # Calculate total volume
    total_volume = sum(r["denominator_count"] or 0 for r in active_alerts)
    
    # Split alerts into downward and upward trends (filter out nulls)
    downward_alerts = [r for r in active_alerts if r["deviation_pct"] is not None and r["deviation_pct"] < 0]
    upward_alerts = [r for r in active_alerts if r["deviation_pct"] is not None and r["deviation_pct"] >= 0]
    
    # Sort each by absolute deviation (most severe first)
    downward_alerts.sort(key=lambda x: x["deviation_pct"])  # Most negative first
    upward_alerts.sort(key=lambda x: -x["deviation_pct"])   # Most positive first
    
    def humanize_metric_name(name: str) -> str:
        """Convert metric_name to human readable format."""
        name = name.replace("_", " ").replace("tsr", "TSR").title().replace("Tsr", "TSR")
        name = name.replace("Checkout Tokenisation", "Checkout").replace("Tokenisation", "Token")
        return name
    
    def humanize_dimension_value(dim_key: str, dim_value: str) -> str:
        """Convert dimension values to human readable format with / separator."""
        if not dim_value or dim_value == "global":
            return "(all)"
        
        keys = dim_key.split(",") if dim_key else []
        values = dim_value.split(",") if dim_value else []
        
        formatted_parts = []
        for i, val in enumerate(values):
            key = keys[i] if i < len(keys) else ""
            if key == "new_payment_method":
                val = "new_pm" if val.lower() == "true" else "existing_pm"
            formatted_parts.append(val)
        
        return "/".join(formatted_parts)
    
    def format_alert_line(row):
        severity_icon = " 🔴" if row["severity"] == "critical" else ""
        current = row["current_value"] * 100
        expected = row["expected_value"] * 100
        deviation = row["deviation_pct"]
        dim_value = humanize_dimension_value(row["dimension_key"], row["dimension_value"])
        volume = row["denominator_count"] or 0
        volume_str = f"{int(volume):,}" if volume >= 1000 else str(int(volume))
        return f"• {dim_value} | {deviation:+.1f}% ({current:.1f}% vs {expected:.1f}%) | n={volume_str}{severity_icon}"
    
    def format_metric_group(alerts_list):
        """Group alerts by metric and format."""
        from collections import defaultdict
        grouped = defaultdict(list)
        for row in alerts_list:
            metric = humanize_metric_name(row["metric_name"])
            grouped[metric].append(row)
        
        lines = []
        for metric, rows in grouped.items():
            if lines:
                lines.append("")
            lines.append(f"*{metric}:*")
            for row in rows:
                lines.append(format_alert_line(row))
        return "\n".join(lines)
    
    total_volume_str = f"{int(total_volume):,}" if total_volume >= 1000 else str(int(total_volume))
    
    # Only show downward trends (declines)
    if not downward_alerts:
        return f"*No declining alerts for {date_str}* ✅\n_{len(active_alerts)} increases, {suppressed_count} suppressed_"
    
    # Recalculate counts for downward only
    downward_critical = len([r for r in downward_alerts if r["severity"] == "critical"])
    downward_warning = len([r for r in downward_alerts if r["severity"] == "warning"])
    downward_volume = sum(r["denominator_count"] or 0 for r in downward_alerts)
    downward_volume_str = f"{int(downward_volume):,}" if downward_volume >= 1000 else str(int(downward_volume))
    
    message = f"""*Overview:*
• Declines: {len(downward_alerts)} ({downward_critical} critical, {downward_warning} warning) | Increases: {len(upward_alerts)} | Suppressed: {suppressed_count}
• Volume Impacted: {downward_volume_str} txns
"""
    
    message += f"\n*📉 Declines ({len(downward_alerts)}):*\n{format_metric_group(downward_alerts)}"
    
    return message

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 8: Send Slack Notifications

# COMMAND ----------

def get_alerts_for_date(alert_date: str) -> DataFrame:
    """Load alerts from table for a specific date. Useful for re-sending notifications."""
    return spark.table(ALERTS_TABLE_FQN).filter(F.col("date") == alert_date)

def get_slack_bot_token() -> Optional[str]:
    """Get Slack bot token from secrets or widget."""
    try:
        return dbutils.secrets.get(scope="slack", key="pa-bot-token")
    except Exception:
        widget_token = dbutils.widgets.get("slack_bot_token")
        return widget_token if widget_token else None

def send_slack_notifications(alerts_df: DataFrame, target_date: datetime, config: Config):
    """Send Slack notifications for alerts. Can be called independently."""
    if alerts_df is None:
        print("No alerts to notify")
        return
    
    # Single collect - all processing done in Python
    all_alerts = alerts_df.collect()
    
    if not all_alerts:
        print("No alerts to notify")
        return
    
    active_alerts = [r for r in all_alerts if not r["suppressed"]]
    active_count = len(active_alerts)
    
    if active_count == 0:
        print("No active alerts - skipping Slack notification")
        return
    
    bot_token = get_slack_bot_token()
    if not bot_token:
        print("Slack bot token not configured - skipping notification")
        print("Set via: dbutils.secrets(scope='slack', key='pa-bot-token') or widget 'slack_bot_token'")
        return
    
    # Build message from collected rows
    slack_message = build_slack_summary(all_alerts, target_date)
    alert_channels = config.defaults.get("alert_channels", ["#growth-pa-payments-alerts"])
    
    critical_count = len([r for r in active_alerts if r["severity"] == "critical"])
    severity = "error" if critical_count > 0 else "warning"
    
    date_str = target_date.strftime("%Y-%m-%d")
    prev_week_str = (target_date - timedelta(days=7)).strftime("%Y-%m-%d")
    
    # Get declining alerts for diagnosis
    declining_alerts = [r for r in active_alerts if r["deviation_pct"] is not None and r["deviation_pct"] < 0]
    
    for channel in alert_channels:
        try:
            result = send_slack_alert(
                channel=channel,
                title=f"🔔 Observe Daily Alerts - {date_str} (vs {prev_week_str})",
                message=slack_message,
                bot_token=bot_token,
                severity=severity,
                details={
                    "Source": ALERTS_TABLE_FQN,
                    "Active Alerts": str(active_count),
                    "Run Date": date_str
                }
            )
            parent_ts = result.get("ts")
            print(f"Slack alert sent to {channel} (ts: {parent_ts})")
            
            # Save thread_ts for later replies
            if parent_ts:
                try:
                    save_thread_ts(date_str, channel, parent_ts, "summary")
                    print(f"  └─ Thread ts saved to table")
                except Exception as save_e:
                    print(f"  └─ Failed to save thread ts: {save_e}")
                
                # Post diagnosis for each declining alert
                diagnosis_count = 0
                for alert_row in declining_alerts:
                    try:
                        diagnosis_msg = build_diagnosis_for_alert(alert_row.asDict(), target_date, config)
                        if diagnosis_msg:
                            post_to_slack(
                                channel=channel,
                                message=diagnosis_msg,
                                bot_token=bot_token,
                                thread_ts=parent_ts
                            )
                            diagnosis_count += 1
                    except Exception as diag_e:
                        print(f"  └─ Failed to post diagnosis for {alert_row['dimension_value']}: {diag_e}")
                
                if diagnosis_count > 0:
                    print(f"  └─ Posted {diagnosis_count} diagnosis replies to thread")
        except Exception as e:
            print(f"Failed to send Slack alert to {channel}: {e}")

def send_diagnosis_to_thread(target_date: datetime, channel: str, config: Config):
    """
    Send diagnosis replies to an existing thread. 
    Use this to re-run diagnosis independently after alerts have been sent.
    """
    date_str = target_date.strftime("%Y-%m-%d")
    
    # Get thread_ts from table
    thread_ts = get_thread_ts(date_str, channel)
    if not thread_ts:
        print(f"No thread found for {date_str} in {channel}")
        return
    
    # Get bot token
    bot_token = get_slack_bot_token()
    if not bot_token:
        print("Slack bot token not configured")
        return
    
    # Load alerts for the date
    alerts_df = get_alerts_for_date(date_str)
    all_alerts = alerts_df.collect()
    
    # Filter to declining, active alerts
    declining_alerts = [
        r for r in all_alerts 
        if not r["suppressed"] and r["deviation_pct"] is not None and r["deviation_pct"] < 0
    ]
    
    print(f"Found {len(declining_alerts)} declining alerts for {date_str}")
    
    diagnosis_count = 0
    for alert_row in declining_alerts:
        try:
            diagnosis_msg = build_diagnosis_for_alert(alert_row.asDict(), target_date, config)
            if diagnosis_msg:
                post_to_slack(
                    channel=channel,
                    message=diagnosis_msg,
                    bot_token=bot_token,
                    thread_ts=thread_ts
                )
                diagnosis_count += 1
                print(f"  ✓ {alert_row['dimension_value']}")
        except Exception as e:
            print(f"  ✗ {alert_row['dimension_value']}: {e}")
    
    print(f"Posted {diagnosis_count} diagnosis replies to thread {thread_ts}")

# COMMAND ----------

# Send notifications - use alerts_df if available, otherwise load from table
try:
    _alerts_to_notify = alerts_df
except NameError:
    print("alerts_df not defined - loading from table...")
    _target_date_str = target_date.strftime("%Y-%m-%d")
    _alerts_to_notify = get_alerts_for_date(_target_date_str)

send_slack_notifications(_alerts_to_notify, target_date, config)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Diagnosis Independently (Optional)
# MAGIC 
# MAGIC Use this cell to re-send diagnosis replies to an existing thread.
# MAGIC Useful when diagnosis logic is updated or if initial diagnosis failed.

# COMMAND ----------

# Uncomment to run diagnosis independently for a specific date/channel:
# send_diagnosis_to_thread(target_date, "#temp-test-alerts", config)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary

# COMMAND ----------

print(f"\n{'='*50}")
print(f"OBSERVE DAILY COMPLETE - {end_date}")
print(f"{'='*50}")

try:
    print(f"Metrics: {metrics_count}")
except NameError:
    print("Metrics: (not computed in this run)")

try:
    print(f"Alerts: {alerts_count}")
    if alerts_df is not None:
        active = alerts_df.filter(F.col("suppressed") == False).count()
        print(f"  Active: {active}")
        print(f"  Suppressed: {alerts_count - active}")
except NameError:
    print("Alerts: (not computed in this run)")

try:
    for name, days in monitor_lookbacks.items():
        print(f"  {name}: {days}d lookback")
except NameError:
    pass
