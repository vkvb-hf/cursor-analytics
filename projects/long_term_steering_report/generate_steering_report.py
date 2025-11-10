# Databricks notebook source
# MAGIC %md
# MAGIC # Generate Steering Report from Source
# MAGIC 
# MAGIC This notebook generates a steering report directly from `payments_hf.payments_p0_metrics` table
# MAGIC following the REPORT_PROMPT_V2.md format.
# MAGIC 
# MAGIC It queries data for all three comparison types (week_prev, week_yoy, quarter_prev) and
# MAGIC generates a comprehensive steering report.

# COMMAND ----------

# Import required libraries
import pyspark.sql.functions as F
from pyspark.sql.types import DoubleType
import math
from time import time
import os
import errno
import pandas as pd
import sys
from io import StringIO

# Set up debug output capture
debug_output = StringIO()
debug_original_stdout = sys.stdout

def debug_print(*args, **kwargs):
    """Print to both console and debug file"""
    print(*args, **kwargs)  # Print to console
    print(*args, **kwargs, file=debug_output)  # Print to debug file

# Replace print with debug_print for debug statements
# We'll use debug_print() for debug statements and regular print() for normal output

# COMMAND ----------

# Configuration - same as main notebook
VALID_REPORTING_CLUSTERS = ['HF-NA', 'HF-INTL', 'RTE', 'WL', 'Overall']
REPORTING_CLUSTERS = ['Overall', 'HF-NA', 'HF-INTL', 'RTE', 'WL']

EXCLUDED_METRICS = [
    '1_ChargeBackRate', 
    '3_PostDunningAR'
]

SPECIAL_METRICS = ['0_ShipRate', '1_RecoveryW0', '2_Recovery_12wkCohort', '3_DunningAvgNetProfit_12wkCohort']

EXCLUDED_DIMENSIONS = ['LoyaltySegment', 'PaymentMethod_OrderType']

# Metric groups in order (matching REPORT_PROMPT_V2.md)
METRIC_GROUPS = [
    ('Payment Page Visit to Success', '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'),
    ('Payment Page Visit to Success (Backend)', '1_Activation (Paid + Referrals) - 1_Checkout Funnel (backend) - 1_PaymentPageVisitToSuccess'),
    ('Select to Success', '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 2_SelectToSuccess'),
    ('Total Duplicate Rate', '1_Activation (Paid + Referrals) - 2_Voucher Fraud - 1_Total Duplicate Rate'),
    ('Total Duplicate Block Rate', '1_Activation (Paid + Referrals) - 2_Voucher Fraud - 2_Total Duplicate Block Rate'),
    ('Payment Fraud Block Rate', '1_Activation (Paid + Referrals) - 3_Payment Fraud - 1_Payment Fraud Block Rate'),
    ('Reactivation Rate', '2_Reactivations - 1_ReactivationFunnel - 1_ReactivationRate'),
    ('AR Pre Dunning', '3_Active - 1_1_Overall Total Box Candidates - 2_PreDunningAR'),
    ('Acceptance LL0 (Initial Charge)', '3_Active - 1_2_Loyalty: LL0 (Initial charges) - 2_PreDunningAR'),
    ('Acceptance LL0 and LL1+ (Recurring Charge)', '3_Active - 1_3_Loyalty: LL0 and LL1+ (Recurring charges) - 2_PreDunningAR'),
    ('Ship Rate', '3_Active - 2_1_Boxes Shipped - 0_ShipRate'),
    ('Recovery W0', '3_Active - 2_1_Boxes Shipped - 1_RecoveryW0'),
    ('Recovery W12', '3_Active - 2_2_Boxes Shipped - 12wk lag - 2_Recovery_12wkCohort'),
    ('Dunning Profit', '3_Active - 2_2_Boxes Shipped - 12wk lag - 3_DunningAvgNetProfit_12wkCohort')
]

WORKSPACE_FOLDER = '/Workspace/Users/visal.kumar@hellofresh.com'

# COMMAND ----------

# Get latest week and periods (same logic as main notebook)
print("Getting latest reporting periods...")
start_time = time()

latest_week_query = """
    SELECT hellofresh_week
    FROM dimensions.date_dimension dd
    WHERE
      hellofresh_week >= '2021-W01'
      AND DATE(date_string_backwards) < CURRENT_DATE()
    GROUP BY 1
    HAVING COUNT(*)=7
    ORDER BY hellofresh_week DESC
    LIMIT 1
"""
latest_week = spark.sql(latest_week_query)
latest_week_str = latest_week.toPandas().values[0][0] if latest_week.count() > 0 else None

prev_week_query = f"""
    SELECT hellofresh_week
    FROM dimensions.date_dimension dd
    WHERE
      hellofresh_week >= '2021-W01'
      AND DATE(date_string_backwards) < CURRENT_DATE()
      AND hellofresh_week < '{latest_week_str}'
    GROUP BY 1
    HAVING COUNT(*)=7
    ORDER BY hellofresh_week DESC
    LIMIT 1
"""
prev_week = spark.sql(prev_week_query)
prev_week_str = prev_week.toPandas().values[0][0] if prev_week.count() > 0 else None

year = int(latest_week_str.split('-W')[0])
week_num_str = latest_week_str.split('-W')[1]
prev_year_week_str = f"{year-1}-W{week_num_str}"

latest_13weeks_query = """
    SELECT hellofresh_week
    FROM dimensions.date_dimension dd
    WHERE
      hellofresh_week >= '2021-W01'
      AND DATE(date_string_backwards) < CURRENT_DATE()
    GROUP BY 1
    HAVING COUNT(*)=7
    ORDER BY hellofresh_week DESC
    LIMIT 13
"""
latest_13weeks = spark.sql(latest_13weeks_query)
latest_13weeks_list = [row[0] for row in latest_13weeks.collect()] if latest_13weeks.count() > 0 else []
latest_13weeks_str = ', '.join(latest_13weeks_list) if latest_13weeks_list else None

prev_13weeks_query = f"""
    SELECT hellofresh_week
    FROM dimensions.date_dimension dd
    WHERE
      hellofresh_week >= '2021-W01'
      AND DATE(date_string_backwards) < CURRENT_DATE()
      AND hellofresh_week < '{latest_13weeks_list[-1] if latest_13weeks_list else latest_week_str}'
    GROUP BY 1
    HAVING COUNT(*)=7
    ORDER BY hellofresh_week DESC
    LIMIT 13
"""
prev_13weeks = spark.sql(prev_13weeks_query)
prev_13weeks_list = [row[0] for row in prev_13weeks.collect()] if prev_13weeks.count() > 0 else []
prev_13weeks_str = ', '.join(prev_13weeks_list) if prev_13weeks_list else None

print(f"Latest week: {latest_week_str}")
print(f"Previous week: {prev_week_str}")
print(f"Previous year week: {prev_year_week_str}")
print(f"Latest 13 weeks: {len(latest_13weeks_list)} weeks")
print(f"Previous 13 weeks: {len(prev_13weeks_list)} weeks")

# COMMAND ----------

# Refresh tables
print("Refreshing tables...")
spark.sql("REFRESH TABLE payments_hf.payments_p0_metrics")
spark.sql("REFRESH TABLE payments_hf.business_units")

# COMMAND ----------

# Load business unit mappings
country_mapping_query = """
    SELECT
      business_unit,
      explode(reporting_cluster_array) AS reporting_cluster
    FROM payments_hf.business_units
"""
country_mapping = spark.sql(country_mapping_query)
country_mapping_df = country_mapping.toPandas()
if not country_mapping_df.empty:
    country_mapping_df['business_unit'] = country_mapping_df['business_unit'].astype(str).str.strip()
    country_mapping_df['reporting_cluster'] = country_mapping_df['reporting_cluster'].astype(str).str.strip()
    country_mapping_df = country_mapping_df[country_mapping_df['reporting_cluster'].isin(VALID_REPORTING_CLUSTERS)].copy()
    print(f"Loaded {len(country_mapping_df)} business unit mappings")

# COMMAND ----------

# Include the build_metrics_query and process_comparison_data functions from the main notebook
# Copy the essential functions here so this notebook is self-contained

# Build metrics query function (from long_term_steering_report.py)
def build_metrics_query(date_granularity, comparison_type, date_value_str, weeks_list=None):
    """Build metrics query for a specific comparison type."""
    # Handle multi-week aggregation vs single week
    if date_granularity == '13WEEKS' and weeks_list:
        weeks_list_str = ','.join([f"'{w}'" for w in weeks_list])
        date_filter = f"date_value IN ({weeks_list_str})"
        date_value_display = date_value_str
        group_by_clause = """
      GROUP BY a.reporting_cluster,
        CASE WHEN a.reporting_cluster = 'Overall' THEN "Null" ELSE a.business_unit END,
        CONCAT(a.focus_group, ' - ', a.metric_group, ' - ',a.metric_name),
        CASE 
          WHEN a.metric_name IN ({special_metrics}) THEN '_Overall' 
          ELSE dimension_name 
        END,
        a.dimension_value,
        a.flag_more_is_good,
        a.flag_is_p0,
        a.metric_type
        """.replace('{special_metrics}', ','.join([f"'{m}'" for m in SPECIAL_METRICS]))
        group_by_clause_bu = """
      GROUP BY a.business_unit,
        CONCAT(a.focus_group, ' - ', a.metric_group, ' - ',a.metric_name),
        a.dimension_name,
        a.dimension_value,
        a.flag_more_is_good,
        a.flag_is_p0,
        a.metric_type
        """
    else:
        date_filter = f"date_value = '{date_value_str}'"
        date_value_display = date_value_str
        group_by_clause = "GROUP BY ALL"
        group_by_clause_bu = "GROUP BY ALL"
    
    # For 'current' comparison type, we only need current columns (no prev columns)
    if comparison_type == 'current':
        prev_cols_select = ""
    elif comparison_type == 'prev_period':
        prev_cols_select = f""",
    SUM(a.prev_metric_value_numerator) AS prev_metric_value_numerator,
    SUM(a.prev_metric_value_denominator) AS prev_metric_value_denominator"""
    else:
        prev_cols_select = f""",
    SUM(a.prev_yr_metric_value_numerator) AS prev_metric_value_numerator,
    SUM(a.prev_yr_metric_value_denominator) AS prev_metric_value_denominator"""
    
    metrics_query = f"""
    SELECT 
    '{date_value_display}' as date_value,
    '{date_granularity}' as date_granularity,
    '{comparison_type}' as comparison_type,
    'Current' as comparison_label,
    a.reporting_cluster,
    CASE WHEN a.reporting_cluster = 'Overall' THEN "Null" ELSE a.business_unit END AS business_unit,
    CONCAT(a.focus_group, ' - ', a.metric_group, ' - ',a.metric_name) as metric_final_name,
    CASE 
      WHEN a.metric_name IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])}) THEN '_Overall' 
      ELSE dimension_name 
    END AS dimension_name,
    a.dimension_value,
    a.flag_more_is_good,
    a.flag_is_p0,
    a.metric_type,
    SUM(a.current_metric_value_numerator) AS current_metric_value_numerator,
    SUM(a.current_metric_value_denominator) AS current_metric_value_denominator{prev_cols_select}
    FROM payments_hf.payments_p0_metrics a
    WHERE 1=1
      AND metric_type IN ('ratio', 'dollar-ratio')
      AND metric_name not in ({','.join([f"'{m}'" for m in EXCLUDED_METRICS])})
      AND flag_is_p0 = 'TRUE'
      AND date_granularity = 'WEEK'
      AND dimension_name NOT LIKE '%DeclineReason%'
      AND dimension_name not in ({','.join([f"'{d}'" for d in EXCLUDED_DIMENSIONS])})
      AND (
        (a.metric_name not IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])})) 
        OR (a.metric_name IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])}) AND dimension_value in ('Good'))
        )
      AND {date_filter}
      {group_by_clause}
    UNION ALL
    SELECT 
    '{date_value_display}' as date_value,
    '{date_granularity}' as date_granularity,
    '{comparison_type}' as comparison_type,
    'Current' as comparison_label,
    'bu_level' AS reporting_cluster,
    a.business_unit,
    CONCAT(a.focus_group, ' - ', a.metric_group, ' - ',a.metric_name) as metric_final_name,
    a.dimension_name,
    a.dimension_value,
    a.flag_more_is_good,
    a.flag_is_p0,
    a.metric_type,
    SUM(a.current_metric_value_numerator) AS current_metric_value_numerator,
    SUM(a.current_metric_value_denominator) AS current_metric_value_denominator{prev_cols_select}
    FROM payments_hf.payments_p0_metrics a
    WHERE 1=1
      AND metric_type IN ('ratio', 'dollar-ratio')
      AND metric_name not in ({','.join([f"'{m}'" for m in EXCLUDED_METRICS])})
      AND flag_is_p0 = 'TRUE'
      AND date_granularity = 'WEEK'
      AND (
        (a.dimension_name = '_Overall' AND a.metric_name not IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])})) 
        OR (a.metric_name IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])}) AND dimension_value in ('Good'))
        )
      AND reporting_cluster = 'Overall'
      AND a.business_unit IS NOT NULL
      AND a.business_unit != 'Null'
      AND {date_filter}
      {group_by_clause_bu}
    """
    return metrics_query

# Z-score calculation UDF
@F.udf(returnType=DoubleType())
def calculate_z_score(n1, d1, n2, d2, metric_type='proportion'):
    """Calculate z-score for difference between two proportions or averages"""
    MIN_SAMPLE_SIZE = 30
    if d1 is None or d2 is None or d1 < MIN_SAMPLE_SIZE or d2 < MIN_SAMPLE_SIZE:
        return None
    try:
        n1, d1, n2, d2 = float(n1), float(d1), float(n2), float(d2)
        value1 = n1 / d1 if d1 > 0 else 0
        value2 = n2 / d2 if d2 > 0 else 0
        if metric_type.lower() == 'ratio':
            pooled_p = (n1 + n2) / (d1 + d2)
            if pooled_p == 0 or pooled_p == 1:
                return None
            se = math.sqrt(pooled_p * (1 - pooled_p) * (1/d1 + 1/d2))
        else:
            pooled_var = max((abs(value1 - value2) / 2) ** 2, 0.0001)
            se = math.sqrt(pooled_var * (1/d1 + 1/d2))
        if se > 0:
            z_score = (value1 - value2) / se
            return z_score
    except (ValueError, ZeroDivisionError, TypeError):
        return None
    return None

# Significance levels
SIGNIFICANCE_LEVELS = [
    (6.361, 7.0, 99.99999), (5.612, 6.0, 99.9999), (4.892, 5.0, 99.999),
    (4.265, 4.0, 99.99), (3.719, 3.5, 99.95), (3.291, 3.0, 99.9),
    (3.090, 2.8, 99.8), (2.807, 2.5, 99.5), (2.576, 2.0, 99.0),
    (2.326, 1.8, 98.0), (2.054, 1.6, 96.0), (1.96, 1.5, 95.0), (1.645, 1.0, 90.0)
]

def build_significance_case(column_name="z_score"):
    """Build significance level case expression dynamically"""
    significance_case = None
    for threshold, level, percentage in SIGNIFICANCE_LEVELS:
        if significance_case is None:
            significance_case = F.when(F.abs(F.col(column_name)) > threshold, level)
        else:
            significance_case = significance_case.when(F.abs(F.col(column_name)) > threshold, level)
    return significance_case.otherwise(0.0)

# Process comparison data function
def process_comparison_data(data_df, comparison_label):
    """Process metrics data and calculate significance, changes, and impact."""
    print(f"Processing {comparison_label}...")
    start_time = time()
    significance_case = build_significance_case("z_score")
    processed_df = (
        data_df
        .withColumn("current_ratio", 
                    F.when(F.col("current_metric_value_denominator") > 0,
                           F.col("current_metric_value_numerator") / F.col("current_metric_value_denominator"))
                    .otherwise(0))
        .withColumn("prev_ratio", 
                    F.when(F.col("prev_metric_value_denominator") > 0,
                           F.col("prev_metric_value_numerator") / F.col("prev_metric_value_denominator"))
                    .otherwise(0))
        .withColumn("z_score", 
                    calculate_z_score(
                        F.col("current_metric_value_numerator"),
                        F.col("current_metric_value_denominator"),
                        F.col("prev_metric_value_numerator"),
                        F.col("prev_metric_value_denominator"),
                        F.col("metric_type")
                    ))
        .withColumn("significance_level", significance_case)
        .withColumn("absolute_change", F.col("current_ratio") - F.col("prev_ratio"))
        .withColumn("relative_change_pct", 
                    F.when(F.col("prev_ratio") > 0,
                           (F.col("absolute_change") / F.col("prev_ratio")) * 100)
                    .otherwise(0))
        .withColumn("impact_direction",
                    F.when(
                        (F.col("flag_more_is_good") == "TRUE") & (F.col("absolute_change") > 0), "Positive"
                    ).when(
                        (F.col("flag_more_is_good") == "TRUE") & (F.col("absolute_change") < 0), "Negative"
                    ).when(
                        (F.col("flag_more_is_good") == "FALSE") & (F.col("absolute_change") > 0), "Negative"
                    ).when(
                        (F.col("flag_more_is_good") == "FALSE") & (F.col("absolute_change") < 0), "Positive"
                    ).otherwise("Neutral"))
    )
    result_df = processed_df.toPandas()
    print(f"  Processed {len(result_df)} rows in {time() - start_time:.2f} seconds")
    return result_df

# COMMAND ----------

# Query and process all three comparison types
print("\n" + "="*80)
print("Querying and processing all comparison types...")
print("="*80)

# Week vs Prev Week
print("\n1. Processing Week vs Previous Week...")
week_prev_query = build_metrics_query('WEEK', 'prev_period', latest_week_str)
week_prev_data = spark.sql(week_prev_query)
week_prev_processed = process_comparison_data(week_prev_data, "Week vs Previous Week")
print(f"   Processed {len(week_prev_processed)} rows")

# Week vs Prev Year Week
print("\n2. Processing Week vs Previous Year Week...")
week_yoy_query = build_metrics_query('WEEK', 'prev_year', latest_week_str)
week_yoy_data = spark.sql(week_yoy_query)
week_yoy_processed = process_comparison_data(week_yoy_data, "Week vs Previous Year Week")
print(f"   Processed {len(week_yoy_processed)} rows")

# ============================================================================
# Quarter vs Prev Quarter Processing
# ============================================================================
# This section:
# 1. Queries current 13-week period data (data_current)
# 2. Queries previous 13-week period data (data_prev)
# 3. Joins them on: reporting_cluster, business_unit, metric_final_name, 
#    dimension_name, dimension_value, flag_more_is_good, flag_is_p0, metric_type
# 4. Processes the joined data to calculate changes
# 
# Note: Business units come from rows where reporting_cluster = 'bu_level'
# (from the second UNION in build_metrics_query). These rows need to match
# between current and previous periods for the join to succeed.
# ============================================================================
print("\n3. Processing Quarter vs Previous Quarter...")
debug_print("   [DEBUG] Building queries for current and previous quarters...")
query_current = build_metrics_query('13WEEKS', 'current', latest_13weeks_str, latest_13weeks_list)
data_current = spark.sql(query_current)
debug_print(f"   [DEBUG] data_current count: {data_current.count()}")

query_prev = build_metrics_query('13WEEKS', 'current', prev_13weeks_str, prev_13weeks_list)
data_prev = spark.sql(query_prev)
debug_print(f"   [DEBUG] data_prev count: {data_prev.count()}")

# DEBUG: Check reporting_cluster distribution BEFORE join
debug_print("   [DEBUG] BEFORE JOIN - Checking reporting_cluster distribution:")
debug_print(f"   [DEBUG] data_current reporting_cluster distribution:")
data_current.groupBy('reporting_cluster').count().orderBy('reporting_cluster').show(truncate=False)
debug_print(f"   [DEBUG] data_prev reporting_cluster distribution:")
data_prev.groupBy('reporting_cluster').count().orderBy('reporting_cluster').show(truncate=False)

# DEBUG: Check bu_level rows specifically
bu_level_current_count = data_current.filter(F.col('reporting_cluster') == 'bu_level').count()
bu_level_prev_count = data_prev.filter(F.col('reporting_cluster') == 'bu_level').count()
debug_print(f"   [DEBUG] BEFORE JOIN - bu_level rows in data_current: {bu_level_current_count}")
debug_print(f"   [DEBUG] BEFORE JOIN - bu_level rows in data_prev: {bu_level_prev_count}")

# DEBUG: Check sample business unit in both datasets to see if join keys match
test_metric_name = '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
test_bu = 'IT'
test_dimension = '_Overall'

bu_current_sample = data_current.filter(
    (F.col('reporting_cluster') == 'bu_level') &
    (F.col('business_unit') == test_bu) &
    (F.col('metric_final_name') == test_metric_name) &
    (F.col('dimension_name') == test_dimension)
).limit(1)

bu_prev_sample = data_prev.filter(
    (F.col('reporting_cluster') == 'bu_level') &
    (F.col('business_unit') == test_bu) &
    (F.col('metric_final_name') == test_metric_name) &
    (F.col('dimension_name') == test_dimension)
).limit(1)

if bu_current_sample.count() > 0:
    current_row = bu_current_sample.collect()[0]
    debug_print(f"   [DEBUG] Sample bu_level row in data_current (IT):")
    debug_print(f"     - business_unit: {current_row['business_unit']}")
    debug_print(f"     - metric_final_name: {current_row['metric_final_name']}")
    debug_print(f"     - dimension_name: {current_row['dimension_name']}")
    debug_print(f"     - dimension_value: {current_row['dimension_value']}")
    debug_print(f"     - current_metric_value_numerator: {current_row['current_metric_value_numerator']}")
    debug_print(f"     - current_metric_value_denominator: {current_row['current_metric_value_denominator']}")
else:
    debug_print(f"   [DEBUG] No bu_level row found in data_current for IT")

if bu_prev_sample.count() > 0:
    prev_row = bu_prev_sample.collect()[0]
    debug_print(f"   [DEBUG] Sample bu_level row in data_prev (IT):")
    debug_print(f"     - business_unit: {prev_row['business_unit']}")
    debug_print(f"     - metric_final_name: {prev_row['metric_final_name']}")
    debug_print(f"     - dimension_name: {prev_row['dimension_name']}")
    debug_print(f"     - dimension_value: {prev_row['dimension_value']}")
    debug_print(f"     - flag_more_is_good: {prev_row['flag_more_is_good']}")
    debug_print(f"     - flag_is_p0: {prev_row['flag_is_p0']}")
    debug_print(f"     - metric_type: {prev_row['metric_type']}")
    debug_print(f"     - current_metric_value_numerator: {prev_row['current_metric_value_numerator']}")
    debug_print(f"     - current_metric_value_denominator: {prev_row['current_metric_value_denominator']}")
    
    # Check if join keys match exactly
    if bu_current_sample.count() > 0:
        current_row = bu_current_sample.collect()[0]
        debug_print(f"   [DEBUG] Comparing join keys for IT:")
        debug_print(f"     - business_unit match: {current_row['business_unit'] == prev_row['business_unit']}")
        debug_print(f"     - metric_final_name match: {current_row['metric_final_name'] == prev_row['metric_final_name']}")
        debug_print(f"     - dimension_name match: {current_row['dimension_name'] == prev_row['dimension_name']}")
        debug_print(f"     - dimension_value match: {current_row['dimension_value'] == prev_row['dimension_value']} (current: {current_row['dimension_value']}, prev: {prev_row['dimension_value']})")
        debug_print(f"     - flag_more_is_good match: {current_row['flag_more_is_good'] == prev_row['flag_more_is_good']}")
        debug_print(f"     - flag_is_p0 match: {current_row['flag_is_p0'] == prev_row['flag_is_p0']}")
        debug_print(f"     - metric_type match: {current_row['metric_type'] == prev_row['metric_type']}")
else:
    debug_print(f"   [DEBUG] ⚠️  No bu_level row found in data_prev for IT - THIS IS THE PROBLEM!")

# Process quarter comparison
data_prev = data_prev.withColumnRenamed("current_metric_value_numerator", "prev_metric_value_numerator")
data_prev = data_prev.withColumnRenamed("current_metric_value_denominator", "prev_metric_value_denominator")

join_cols = ['reporting_cluster', 'business_unit', 'metric_final_name', 'dimension_name', 'dimension_value', 
             'flag_more_is_good', 'flag_is_p0', 'metric_type']

data_current_clean = data_current.select([c for c in data_current.columns if c not in ['prev_metric_value_numerator', 'prev_metric_value_denominator']])
data_prev_selected = data_prev.select(join_cols + ['prev_metric_value_numerator', 'prev_metric_value_denominator'])

debug_print(f"   [DEBUG] BEFORE JOIN - data_current_clean count: {data_current_clean.count()}")
debug_print(f"   [DEBUG] BEFORE JOIN - data_prev_selected count: {data_prev_selected.count()}")

# Handle NULL values in join columns - convert NULL to empty string for consistent matching
for col in join_cols:
    if col in data_current_clean.columns and col in data_prev_selected.columns:
        # Cast to string and replace NULL with empty string for consistent matching
        data_current_clean = data_current_clean.withColumn(
            col, 
            F.coalesce(F.col(col).cast('string'), F.lit(''))
        )
        data_prev_selected = data_prev_selected.withColumn(
            col, 
            F.coalesce(F.col(col).cast('string'), F.lit(''))
        )

debug_print("   [DEBUG] Performing LEFT JOIN on columns:", join_cols)
data_combined = data_current_clean.join(data_prev_selected, on=join_cols, how='left')
debug_print(f"   [DEBUG] AFTER JOIN - data_combined count: {data_combined.count()}")

# DEBUG: Check bu_level rows after join
bu_level_after_join = data_combined.filter(F.col('reporting_cluster') == 'bu_level').count()
debug_print(f"   [DEBUG] AFTER JOIN - bu_level rows in data_combined: {bu_level_after_join}")

# DEBUG: Check if prev values are NULL (meaning join didn't match) before fillna
bu_level_before_fillna = data_combined.filter(F.col('reporting_cluster') == 'bu_level')
null_prev_num = bu_level_before_fillna.filter(F.col('prev_metric_value_numerator').isNull()).count()
null_prev_den = bu_level_before_fillna.filter(F.col('prev_metric_value_denominator').isNull()).count()
debug_print(f"   [DEBUG] BEFORE fillna - bu_level rows with NULL prev_metric_value_numerator: {null_prev_num}")
debug_print(f"   [DEBUG] BEFORE fillna - bu_level rows with NULL prev_metric_value_denominator: {null_prev_den}")

# DEBUG: Check sample values before fillna for a specific business unit
test_bu_sample = bu_level_before_fillna.filter(F.col('business_unit') == 'IT').limit(1)
if test_bu_sample.count() > 0:
    test_row = test_bu_sample.collect()[0]
    debug_print(f"   [DEBUG] Sample bu_level row (IT) before fillna:")
    debug_print(f"     - current_metric_value_numerator: {test_row['current_metric_value_numerator']}")
    debug_print(f"     - current_metric_value_denominator: {test_row['current_metric_value_denominator']}")
    debug_print(f"     - prev_metric_value_numerator: {test_row['prev_metric_value_numerator']}")
    debug_print(f"     - prev_metric_value_denominator: {test_row['prev_metric_value_denominator']}")
    debug_print(f"     - business_unit: {test_row['business_unit']}")
    debug_print(f"     - metric_final_name: {test_row['metric_final_name']}")

data_combined = data_combined.fillna(0, subset=['prev_metric_value_numerator', 'prev_metric_value_denominator'])

quarter_prev_processed = process_comparison_data(data_combined, "Quarter vs Previous Quarter")
print(f"   Processed {len(quarter_prev_processed)} rows")

# DEBUG: Check if bu_level rows are present after processing
if quarter_prev_processed is not None and not quarter_prev_processed.empty:
    bu_level_count = len(quarter_prev_processed[quarter_prev_processed['reporting_cluster'] == 'bu_level'])
    debug_print(f"   [DEBUG] AFTER PROCESSING - bu_level rows in quarter_prev_processed: {bu_level_count}")
    debug_print(f"   [DEBUG] AFTER PROCESSING - reporting_cluster distribution:")
    debug_print(str(quarter_prev_processed['reporting_cluster'].value_counts()))
    
    if bu_level_count > 0:
        test_metric = '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
        test_metric_df = quarter_prev_processed[quarter_prev_processed['metric_final_name'] == test_metric]
        debug_print(f"   [DEBUG] AFTER PROCESSING - test_metric_df count: {len(test_metric_df)}")
        bu_level_in_test = test_metric_df[test_metric_df['reporting_cluster'] == 'bu_level']
        debug_print(f"   [DEBUG] AFTER PROCESSING - bu_level rows for {test_metric}: {len(bu_level_in_test)}")
        if not bu_level_in_test.empty:
            debug_print(f"   [DEBUG] Sample bu_level business units: {bu_level_in_test['business_unit'].head(10).tolist()}")

# COMMAND ----------

# Helper functions for report generation
def format_number(num):
    """Format numbers for readability"""
    if num is None:
        return "0"
    try:
        num = float(num)
        abs_num = abs(num)
        if abs_num < 1000:
            return f"{num:.0f}" if num == int(num) else f"{num:.1f}"
        elif abs_num < 1000000:
            return f"{num/1000:.1f}K"
        else:
            return f"{num/1000000:.1f}M"
    except (TypeError, ValueError):
        return "0"

def format_arrow(rel_change):
    """Return arrow based on relative change"""
    return '↑' if rel_change > 0 else '↓'

def format_significance(sig_level):
    """Format significance"""
    return 'significant' if sig_level >= 3 else 'not significant'

# COMMAND ----------

# Generate key insights
def generate_key_insights(week_prev_df, week_yoy_df, quarter_prev_df):
    """Generate key insights section"""
    insights = []
    
    # Critical Issues
    critical = []
    if week_prev_df is not None and not week_prev_df.empty:
        overall = week_prev_df[week_prev_df['reporting_cluster'] == 'Overall']
        if not overall.empty:
            for _, row in overall.iterrows():
                if row['relative_change_pct'] < -5:
                    metric_short = row.get('metric_final_name', '').split(' - ')[-1]
                    critical.append(f"{metric_short} decreased {abs(row['relative_change_pct']):.2f}% ({row['prev_ratio']*100:.2f}% to {row['current_ratio']*100:.2f}%)")
    
    if critical:
        insights.append(f"- **Critical Issues:** {', '.join(critical[:2])}")
    else:
        insights.append("- **Critical Issues:** None identified")
    
    # Positive Trends
    positive = []
    if week_prev_df is not None and not week_prev_df.empty:
        overall = week_prev_df[week_prev_df['reporting_cluster'] == 'Overall']
        if not overall.empty:
            for _, row in overall.iterrows():
                if row['relative_change_pct'] > 5:
                    metric_short = row.get('metric_final_name', '').split(' - ')[-1]
                    positive.append(f"{metric_short} increased {row['relative_change_pct']:.2f}% ({row['prev_ratio']*100:.2f}% to {row['current_ratio']*100:.2f}%)")
    
    if positive:
        insights.append(f"- **Positive Trends:** {', '.join(positive[:2])}")
    else:
        insights.append("- **Positive Trends:** Overall metrics stable")
    
    # Risk Shifts
    risks = []
    if week_prev_df is not None and not week_prev_df.empty:
        hfna = week_prev_df[week_prev_df['reporting_cluster'] == 'HF-NA']
        hfintl = week_prev_df[week_prev_df['reporting_cluster'] == 'HF-INTL']
        if not hfna.empty and not hfintl.empty:
            for metric in hfna['metric_final_name'].unique():
                hfna_metric = hfna[hfna['metric_final_name'] == metric]
                hfintl_metric = hfintl[hfintl['metric_final_name'] == metric]
                if not hfna_metric.empty and not hfintl_metric.empty:
                    hfna_change = hfna_metric.iloc[0]['relative_change_pct']
                    hfintl_change = hfintl_metric.iloc[0]['relative_change_pct']
                    if (hfna_change > 0 and hfintl_change < 0) or (hfna_change < 0 and hfintl_change > 0):
                        metric_short = metric.split(' - ')[-1]
                        risks.append(f"{metric_short} showing diverging trends")
    
    if risks:
        insights.append(f"- **Risk Shifts:** {', '.join(risks[:1])}")
    else:
        insights.append("- **Risk Shifts:** No major shifts detected")
    
    # Emerging Concerns
    concerns = []
    if week_yoy_df is not None and not week_yoy_df.empty:
        overall = week_yoy_df[week_yoy_df['reporting_cluster'] == 'Overall']
        if not overall.empty:
            for _, row in overall.iterrows():
                if row['relative_change_pct'] < -10:
                    metric_short = row.get('metric_final_name', '').split(' - ')[-1]
                    concerns.append(f"{metric_short} down {abs(row['relative_change_pct']):.2f}% YoY")
    
    if concerns:
        insights.append(f"- **Emerging Concerns:** {', '.join(concerns[:1])}")
    else:
        insights.append("- **Emerging Concerns:** Monitor long-term trends")
    
    return "\n".join(insights)

# COMMAND ----------

# Build callout for a metric - rewritten from scratch following write_formatted_summaries pattern
def build_callout_for_metric(metric_full_name, week_prev_df, week_yoy_df, quarter_prev_df):
    """Build callout text for a metric following write_formatted_summaries pattern"""
    parts = []
    
    # Week vs Prev Week - Level 1 (Overall summary)
    if week_prev_df is not None and not week_prev_df.empty:
        parts.append("**Current Week vs Prev Week:**")
        
        # Process each reporting cluster - Level 1
        for rc in REPORTING_CLUSTERS:
            level1_rows = week_prev_df[
                (week_prev_df['reporting_cluster'] == rc) & 
                (week_prev_df['dimension_name'] == '_Overall')
            ]
            
            if not level1_rows.empty:
                row = level1_rows.iloc[0]
                arrow = format_arrow(row['relative_change_pct'])
                sig = format_significance(row.get('significance_level', 0))
                volume = format_number(row.get('current_metric_value_denominator', 0) * abs(row['relative_change_pct']) / 100)
                prev_pct = row['prev_ratio'] * 100 if row['metric_type'] == 'ratio' else row['prev_ratio']
                curr_pct = row['current_ratio'] * 100 if row['metric_type'] == 'ratio' else row['current_ratio']
                
                if row['metric_type'] == 'ratio':
                    parts.append(f"- **{rc}**: {prev_pct:.2f}% to {curr_pct:.2f}% ({arrow}{abs(row['relative_change_pct']):.2f}%, {sig}, volume: {volume})")
                else:
                    parts.append(f"- **{rc}**: €{prev_pct:.2f} to €{curr_pct:.2f} ({arrow}{abs(row['relative_change_pct']):.2f}%, {sig}, volume: {volume})")
        
        # Deep Insights - Level 2 (Dimensions and Business Units)
        parts.append("<br><br>**Deep Insights**")
        insights = []
        
        for rc in REPORTING_CLUSTERS:
            # Level 2 - Dimensions
            level2_dims_rows = week_prev_df[
                (week_prev_df['reporting_cluster'] == rc) & 
                (week_prev_df['dimension_name'] != '_Overall')
            ]
            
            if not level2_dims_rows.empty:
                level2_dims_rows = level2_dims_rows.copy()
                level2_dims_rows.loc[:, 'abs_rel_change'] = abs(level2_dims_rows['relative_change_pct'])
                level2_dims_rows.loc[:, 'volume_impacted'] = level2_dims_rows['current_metric_value_denominator'] * level2_dims_rows['abs_rel_change'] / 100
                sorted_dims = level2_dims_rows.sort_values(['dimension_name', 'volume_impacted'], ascending=False)
                filtered_dims = sorted_dims[(sorted_dims['abs_rel_change']>10) | (sorted_dims['volume_impacted']>30)]
                
                for _, dim_row in filtered_dims.head(3).iterrows():
                    arrow = format_arrow(dim_row['relative_change_pct'])
                    volume = format_number(dim_row.get('volume_impacted', 0))
                    prev_pct = dim_row['prev_ratio'] * 100 if dim_row['metric_type'] == 'ratio' else dim_row['prev_ratio']
                    curr_pct = dim_row['current_ratio'] * 100 if dim_row['metric_type'] == 'ratio' else dim_row['current_ratio']
                    item_name = f"{dim_row['dimension_name']} {dim_row['dimension_value']}"
                    
                    if dim_row['metric_type'] == 'ratio':
                        insights.append(f"- **{rc}** {item_name}: {prev_pct:.2f}% to {curr_pct:.2f}% ({arrow}{abs(dim_row['relative_change_pct']):.2f}%, volume: {volume})")
                    else:
                        insights.append(f"- **{rc}** {item_name}: €{prev_pct:.2f} to €{curr_pct:.2f} ({arrow}{abs(dim_row['relative_change_pct']):.2f}%, volume: {volume})")
            
            # Level 2 - Business Units (only for non-Overall clusters)
            # This is where we get business unit data for Week vs Prev Week
            if rc != 'Overall':
                # DEBUG: Check if we have business unit data for this metric
                is_debug_metric = metric_full_name == '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
                
                if is_debug_metric:
                    debug_print(f"\n[DEBUG Week vs Prev Week - Level 2 BU] Processing reporting cluster: {rc}")
                    debug_print(f"[DEBUG] week_prev_df shape: {week_prev_df.shape}")
                    debug_print(f"[DEBUG] week_prev_df reporting_cluster values: {week_prev_df['reporting_cluster'].unique()}")
                    debug_print(f"[DEBUG] week_prev_df business_unit sample: {week_prev_df['business_unit'].head(10).tolist()}")
                
                # Get business units for this reporting cluster from country mapping
                rc_bu = country_mapping_df[country_mapping_df['reporting_cluster'] == rc].business_unit.tolist()
                
                if is_debug_metric:
                    debug_print(f"[DEBUG] Business units in {rc} from country_mapping_df: {len(rc_bu)} ({rc_bu[:10]}...)")
                
                # Filter week_prev_df for business units in this cluster
                # Note: For week comparisons, business units might come from rows where
                # reporting_cluster = rc (not 'bu_level'), so we filter by business_unit directly
                level2_bu_rows = week_prev_df[week_prev_df['business_unit'].isin(rc_bu)]
                
                if is_debug_metric:
                    debug_print(f"[DEBUG] level2_bu_rows count after filtering by business_unit.isin(rc_bu): {len(level2_bu_rows)}")
                    if not level2_bu_rows.empty:
                        debug_print(f"[DEBUG] level2_bu_rows reporting_cluster values: {level2_bu_rows['reporting_cluster'].unique()}")
                        debug_print(f"[DEBUG] level2_bu_rows business_unit values: {level2_bu_rows['business_unit'].unique()}")
                        debug_print(f"[DEBUG] level2_bu_rows sample relative_change_pct: {level2_bu_rows['relative_change_pct'].head(10).tolist()}")
                    else:
                        debug_print(f"[DEBUG] ⚠️  level2_bu_rows is EMPTY! No business unit data found for {rc}")
                        # Check if business units exist in week_prev_df at all
                        all_bu_in_df = week_prev_df['business_unit'].unique()
                        matching_bu = [bu for bu in rc_bu if bu in all_bu_in_df]
                        debug_print(f"[DEBUG] Business units in week_prev_df that match {rc}: {len(matching_bu)} ({matching_bu[:10]}...)")
                
                if not level2_bu_rows.empty:
                    level2_bu_rows = level2_bu_rows.copy()
                    level2_bu_rows.loc[:, 'abs_rel_change'] = abs(level2_bu_rows['relative_change_pct'])
                    level2_bu_rows.loc[:, 'volume_impacted'] = level2_bu_rows['current_metric_value_denominator'] * level2_bu_rows['abs_rel_change'] / 100
                    
                    if is_debug_metric:
                        debug_print(f"[DEBUG] After calculating abs_rel_change and volume_impacted")
                        debug_print(f"[DEBUG] Sample abs_rel_change: {level2_bu_rows['abs_rel_change'].head(10).tolist()}")
                        debug_print(f"[DEBUG] Sample volume_impacted: {level2_bu_rows['volume_impacted'].head(10).tolist()}")
                    
                    sorted_bu = level2_bu_rows.sort_values('volume_impacted', ascending=False)
                    filtered_bu = sorted_bu[(sorted_bu['abs_rel_change']>10) | (sorted_bu['volume_impacted']>30)]
                    
                    if is_debug_metric:
                        debug_print(f"[DEBUG] After filtering (abs_rel_change>10 OR volume_impacted>30): {len(filtered_bu)} rows")
                        if not filtered_bu.empty:
                            debug_print(f"[DEBUG] Significant business units for {rc}: {filtered_bu['business_unit'].tolist()}")
                    
                    for _, bu_row in filtered_bu.head(2).iterrows():
                        if bu_row['business_unit'] == "Null":
                            continue
                        arrow = format_arrow(bu_row['relative_change_pct'])
                        volume = format_number(bu_row.get('volume_impacted', 0))
                        prev_pct = bu_row['prev_ratio'] * 100 if bu_row['metric_type'] == 'ratio' else bu_row['prev_ratio']
                        curr_pct = bu_row['current_ratio'] * 100 if bu_row['metric_type'] == 'ratio' else bu_row['current_ratio']
                        
                        if bu_row['metric_type'] == 'ratio':
                            insights.append(f"- **{rc}** {bu_row['business_unit']}: {prev_pct:.2f}% to {curr_pct:.2f}% ({arrow}{abs(bu_row['relative_change_pct']):.2f}%, volume: {volume})")
                        else:
                            insights.append(f"- **{rc}** {bu_row['business_unit']}: €{prev_pct:.2f} to €{curr_pct:.2f} ({arrow}{abs(bu_row['relative_change_pct']):.2f}%, volume: {volume})")
        
        if insights:
            parts.extend(insights[:5])
        else:
            parts.append("- No significant insights")
    
    # ============================================================================
    # Long Term Impact (Quarter) - following write_formatted_summaries pattern
    # ============================================================================
    # This section processes quarter-over-quarter comparison data to identify
    # significant business unit changes. The data flow is:
    # 1. Input: quarter_prev_df (already filtered by metric)
    # 2. Filter for bu_level rows (business units come from second UNION in query)
    # 3. For each reporting cluster (HF-NA, HF-INTL, RTE, WL):
    #    - Get business units from country_mapping_df
    #    - Filter bu_level rows by business_unit.isin(rc_bu)
    #    - Calculate abs_rel_change and volume_impacted
    #    - Filter for significance: (abs_rel_change>10) | (volume_impacted>30)
    # 4. Collect all significant business units
    # 5. Display if has_significant_overall OR has_significant_bu
    # ============================================================================
    if quarter_prev_df is not None and not quarter_prev_df.empty:
        # DEBUG: Track data flow for Payment Page Visit to Success
        is_debug_metric = metric_full_name == '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
        
        if is_debug_metric:
            debug_print(f"\n[DEBUG build_callout_for_metric] Starting Long Term Impact for: {metric_full_name}")
            debug_print(f"[DEBUG] STEP 1 - Input quarter_prev_df shape: {quarter_prev_df.shape}")
            debug_print(f"[DEBUG] STEP 1 - Input quarter_prev_df reporting_cluster values: {quarter_prev_df['reporting_cluster'].unique()}")
            bu_level_input = quarter_prev_df[quarter_prev_df['reporting_cluster'] == 'bu_level']
            debug_print(f"[DEBUG] STEP 1 - bu_level rows in input: {len(bu_level_input)}")
        
        df_metric = quarter_prev_df.copy()
        
        # Ensure data types are consistent (should already be done, but be defensive)
        if 'business_unit' in df_metric.columns:
            df_metric['business_unit'] = df_metric['business_unit'].astype(str).str.strip()
        if 'reporting_cluster' in df_metric.columns:
            df_metric['reporting_cluster'] = df_metric['reporting_cluster'].astype(str).str.strip()
        if 'dimension_name' in df_metric.columns:
            df_metric['dimension_name'] = df_metric['dimension_name'].astype(str).str.strip()
        
        if is_debug_metric:
            debug_print(f"[DEBUG] STEP 2 - After data type normalization, df_metric shape: {df_metric.shape}")
            debug_print(f"[DEBUG] STEP 2 - reporting_cluster distribution:")
            debug_print(str(df_metric['reporting_cluster'].value_counts()))
        
        # Process each reporting cluster - Level 1 (Overall summary)
        overall_rows = df_metric[
            (df_metric['reporting_cluster'] == 'Overall') & 
            (df_metric['dimension_name'] == '_Overall')
        ]
        
        if is_debug_metric:
            debug_print(f"[DEBUG] STEP 3 - Overall rows count: {len(overall_rows)}")
            if not overall_rows.empty:
                debug_print(f"[DEBUG] STEP 3 - Overall relative_change_pct: {overall_rows.iloc[0]['relative_change_pct']:.2f}%")
        
        # Collect all significant business units from all clusters
        # Business units come from rows where reporting_cluster = 'bu_level' (from second UNION)
        # We need to filter for bu_level rows and map them to clusters using country_mapping_df
        all_significant_bu = []
        
        # Get all business unit rows (reporting_cluster = 'bu_level')
        # For non-special metrics, bu_level rows should have dimension_name = '_Overall'
        # For special metrics, they should have dimension_value = 'Good'
        # But since we're already filtering by metric, we can just get all bu_level rows
        bu_level_rows = df_metric[df_metric['reporting_cluster'] == 'bu_level'].copy()
        
        if is_debug_metric:
            debug_print(f"[DEBUG] STEP 4 - bu_level_rows count: {len(bu_level_rows)}")
            if not bu_level_rows.empty:
                debug_print(f"[DEBUG] STEP 4 - bu_level_rows dimension_name values: {bu_level_rows['dimension_name'].unique()}")
                debug_print(f"[DEBUG] STEP 4 - Sample business units: {bu_level_rows['business_unit'].head(10).tolist()}")
                debug_print(f"[DEBUG] STEP 4 - Sample relative_change_pct values: {bu_level_rows['relative_change_pct'].head(10).tolist()}")
        
        # Also check if there are business units in other reporting_cluster rows (from first UNION)
        # These would have actual reporting_cluster values (HF-NA, HF-INTL, etc.) and business_unit populated
        # But based on the query structure, business units only come from bu_level rows
        # So we only need to check bu_level
        
        if not bu_level_rows.empty:
            if is_debug_metric:
                debug_print(f"[DEBUG] STEP 5 - Processing reporting clusters to find business units...")
            
            # Process each reporting cluster to find its business units
            for rc in REPORTING_CLUSTERS:
                if rc != 'Overall':
                    # Get business units for this reporting cluster from country mapping
                    rc_bu = country_mapping_df[country_mapping_df['reporting_cluster'] == rc].business_unit.tolist()
                    # Convert to string and strip for matching (country_mapping_df is already normalized, but be defensive)
                    rc_bu = [str(bu).strip() for bu in rc_bu]
                    
                    if is_debug_metric:
                        debug_print(f"[DEBUG] STEP 5.{rc} - Business units in {rc}: {len(rc_bu)} ({rc_bu[:5]}...)")
                    
                    # Filter bu_level rows for business units in this cluster
                    # bu_level_rows is already normalized at the start of the function
                    level2_bu_rows = bu_level_rows[bu_level_rows['business_unit'].isin(rc_bu)]
                    
                    if is_debug_metric:
                        debug_print(f"[DEBUG] STEP 5.{rc} - After filtering by business_unit.isin(rc_bu): {len(level2_bu_rows)} rows")
                    
                    if not level2_bu_rows.empty:
                        level2_bu_rows = level2_bu_rows.copy()
                        level2_bu_rows.loc[:, 'abs_rel_change'] = abs(level2_bu_rows['relative_change_pct'])
                        level2_bu_rows.loc[:, 'volume_impacted'] = level2_bu_rows['current_metric_value_denominator'] * level2_bu_rows['abs_rel_change'] / 100
                        
                        if is_debug_metric:
                            debug_print(f"[DEBUG] STEP 5.{rc} - After calculating abs_rel_change and volume_impacted")
                            debug_print(f"[DEBUG] STEP 5.{rc} - Sample abs_rel_change: {level2_bu_rows['abs_rel_change'].head(5).tolist()}")
                            debug_print(f"[DEBUG] STEP 5.{rc} - Sample volume_impacted: {level2_bu_rows['volume_impacted'].head(5).tolist()}")
                        
                        sorted_bu = level2_bu_rows.sort_values('volume_impacted', ascending=False)
                        filtered_bu = sorted_bu[(sorted_bu['abs_rel_change']>10) | (sorted_bu['volume_impacted']>30)]
                        
                        if is_debug_metric:
                            debug_print(f"[DEBUG] STEP 5.{rc} - After filtering (abs_rel_change>10 OR volume_impacted>30): {len(filtered_bu)} rows")
                            if not filtered_bu.empty:
                                debug_print(f"[DEBUG] STEP 5.{rc} - Significant business units: {filtered_bu['business_unit'].tolist()}")
                        
                        for _, row in filtered_bu.iterrows():
                            if row['business_unit'] == "Null" or pd.isna(row['business_unit']) or row['business_unit'] == '':
                                continue
                            all_significant_bu.append(row)
        
        if is_debug_metric:
            debug_print(f"[DEBUG] STEP 6 - Total significant business units collected: {len(all_significant_bu)}")
            if all_significant_bu:
                bu_names = [r['business_unit'] for r in all_significant_bu]
                debug_print(f"[DEBUG] STEP 6 - Significant business units: {bu_names}")
        
        # Check if we should show Long Term Impact
        has_significant_overall = not overall_rows.empty and abs(overall_rows.iloc[0]['relative_change_pct']) > 10
        has_significant_bu = len(all_significant_bu) > 0
        
        if is_debug_metric:
            debug_print(f"[DEBUG] STEP 7 - has_significant_overall: {has_significant_overall}, has_significant_bu: {has_significant_bu}")
        
        if has_significant_overall or has_significant_bu:
            parts.append("<br><br>**Long Term Impact**")
            
            # Add Overall if it exists
            if not overall_rows.empty:
                row = overall_rows.iloc[0]
                arrow = format_arrow(row['relative_change_pct'])
                volume = format_number(row.get('current_metric_value_denominator', 0) * abs(row['relative_change_pct']) / 100)
                prev_pct = row['prev_ratio'] * 100 if row['metric_type'] == 'ratio' else row['prev_ratio']
                curr_pct = row['current_ratio'] * 100 if row['metric_type'] == 'ratio' else row['current_ratio']
                
                if row['metric_type'] == 'ratio':
                    parts.append(f"- **Overall**: {prev_pct:.2f}% to {curr_pct:.2f}% ({arrow}{abs(row['relative_change_pct']):.2f}%, volume: {volume})")
                else:
                    parts.append(f"- **Overall**: €{prev_pct:.2f} to €{curr_pct:.2f} ({arrow}{abs(row['relative_change_pct']):.2f}%, volume: {volume})")
            
            # Add significant business units (sort by abs_rel_change for display)
            if all_significant_bu:
                # Convert to DataFrame for easier sorting
                bu_df = pd.DataFrame(all_significant_bu)
                bu_df = bu_df.sort_values('abs_rel_change', ascending=False)
                
                for _, bu_row in bu_df.head(15).iterrows():
                    arrow = format_arrow(bu_row['relative_change_pct'])
                    volume = format_number(bu_row.get('volume_impacted', 0))
                    prev_pct = bu_row['prev_ratio'] * 100 if bu_row['metric_type'] == 'ratio' else bu_row['prev_ratio']
                    curr_pct = bu_row['current_ratio'] * 100 if bu_row['metric_type'] == 'ratio' else bu_row['current_ratio']
                    bu_name = bu_row.get('business_unit', 'Unknown')
                    
                    if bu_row['metric_type'] == 'ratio':
                        parts.append(f"- **{bu_name}**: {prev_pct:.2f}% to {curr_pct:.2f}% ({arrow}{abs(bu_row['relative_change_pct']):.2f}%, volume: {volume})")
                    else:
                        parts.append(f"- **{bu_name}**: €{prev_pct:.2f} to €{curr_pct:.2f} ({arrow}{abs(bu_row['relative_change_pct']):.2f}%, volume: {volume})")
        else:
            parts.append("<br><br>**Long Term Impact**<br>- No significant long-term impact (all changes <10%)")
    else:
        parts.append("<br><br>**Long Term Impact**<br>- No significant long-term impact (all changes <10%)")
    
    # Comparison vs Prev Year
    if week_yoy_df is not None and not week_yoy_df.empty:
        overall_yoy = week_yoy_df[
            (week_yoy_df['reporting_cluster'] == 'Overall') & 
            (week_yoy_df['dimension_name'] == '_Overall')
        ]
        if not overall_yoy.empty:
            row = overall_yoy.iloc[0]
            if abs(row['relative_change_pct']) > 10:
                arrow = format_arrow(row['relative_change_pct'])
                volume = format_number(row.get('current_metric_value_denominator', 0) * abs(row['relative_change_pct']) / 100)
                prev_pct = row['prev_ratio'] * 100 if row['metric_type'] == 'ratio' else row['prev_ratio']
                curr_pct = row['current_ratio'] * 100 if row['metric_type'] == 'ratio' else row['current_ratio']
                
                parts.append("<br><br>**Comparison vs Prev Year**")
                if row['metric_type'] == 'ratio':
                    parts.append(f"- **Current Week vs Prev Year Week**: {prev_pct:.2f}% to {curr_pct:.2f}% ({arrow}{abs(row['relative_change_pct']):.2f}%, volume: {volume})")
                else:
                    parts.append(f"- **Current Week vs Prev Year Week**: €{prev_pct:.2f} to €{curr_pct:.2f} ({arrow}{abs(row['relative_change_pct']):.2f}%, volume: {volume})")
            else:
                parts.append("<br><br>**Comparison vs Prev Year**<br>- No significant year-over-year impact (all changes <10%)")
        else:
            parts.append("<br><br>**Comparison vs Prev Year**<br>- No significant year-over-year impact (all changes <10%)")
    else:
        parts.append("<br><br>**Comparison vs Prev Year**<br>- No significant year-over-year impact (all changes <10%)")
    
    return "<br>".join(parts)

# COMMAND ----------

# Generate steering report
print("\n" + "="*80)
print("Generating Steering Report...")
print("="*80)

# Define OUTPUT_BASE_FOLDER before calling build_callout_for_metric so it's available in the function
OUTPUT_BASE_FOLDER = f'{WORKSPACE_FOLDER}/long-term-steering-{latest_week_str if latest_week_str else "unknown"}'

week_num = latest_week_str.split('-W')[1] if latest_week_str else 'XX'
report = f"# {latest_week_str} Weekly Payments Metrics Steering\n\n"
report += "## Key Insights\n"
report += generate_key_insights(week_prev_processed, week_yoy_processed, quarter_prev_processed)
report += "\n\n"
report += "| Metrics | Anomaly/Callout | Notes |\n"
report += "| :--- | :--- | :--- |\n"

# Normalize data types once before the loop to ensure consistent filtering
if quarter_prev_processed is not None and not quarter_prev_processed.empty:
    quarter_prev_processed = quarter_prev_processed.copy()
    quarter_prev_processed['metric_final_name'] = quarter_prev_processed['metric_final_name'].astype(str).str.strip()
    quarter_prev_processed['reporting_cluster'] = quarter_prev_processed['reporting_cluster'].astype(str).str.strip()
    quarter_prev_processed['business_unit'] = quarter_prev_processed['business_unit'].astype(str).str.strip()

if week_prev_processed is not None and not week_prev_processed.empty:
    week_prev_processed = week_prev_processed.copy()
    week_prev_processed['metric_final_name'] = week_prev_processed['metric_final_name'].astype(str).str.strip()

if week_yoy_processed is not None and not week_yoy_processed.empty:
    week_yoy_processed = week_yoy_processed.copy()
    week_yoy_processed['metric_final_name'] = week_yoy_processed['metric_final_name'].astype(str).str.strip()

# Add each metric
for metric_display, metric_full in METRIC_GROUPS:
    # DEBUG for Payment Page Visit to Success - check BEFORE filtering
    is_debug_metric = metric_full == '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
    
    if is_debug_metric:
        debug_print(f"\n{'='*80}")
        debug_print(f"[DEBUG METRIC FILTERING] Processing metric: {metric_full}")
        debug_print(f"{'='*80}")
        if quarter_prev_processed is not None and not quarter_prev_processed.empty:
            debug_print(f"[DEBUG] BEFORE FILTERING - quarter_prev_processed shape: {quarter_prev_processed.shape}")
            debug_print(f"[DEBUG] BEFORE FILTERING - Unique metric_final_name values (first 10):")
            unique_metrics = quarter_prev_processed['metric_final_name'].unique()[:10]
            for um in unique_metrics:
                print(f"  - {um}")
            debug_print(f"[DEBUG] BEFORE FILTERING - Checking if our metric exists in quarter_prev_processed:")
            metric_exists = (quarter_prev_processed['metric_final_name'] == metric_full).any()
            debug_print(f"[DEBUG] BEFORE FILTERING - Metric exists: {metric_exists}")
            if metric_exists:
                matching_rows = quarter_prev_processed[quarter_prev_processed['metric_final_name'] == metric_full]
                debug_print(f"[DEBUG] BEFORE FILTERING - Matching rows count: {len(matching_rows)}")
                debug_print(f"[DEBUG] BEFORE FILTERING - reporting_cluster distribution in matching rows:")
                print(matching_rows['reporting_cluster'].value_counts())
                bu_level_before = matching_rows[matching_rows['reporting_cluster'] == 'bu_level']
                debug_print(f"[DEBUG] BEFORE FILTERING - bu_level rows in matching: {len(bu_level_before)}")
    
    # Filter dataframes for this metric
    week_prev_metric = week_prev_processed[week_prev_processed['metric_final_name'] == metric_full] if week_prev_processed is not None and not week_prev_processed.empty else None
    week_yoy_metric = week_yoy_processed[week_yoy_processed['metric_final_name'] == metric_full] if week_yoy_processed is not None and not week_yoy_processed.empty else None
    quarter_prev_metric = quarter_prev_processed[quarter_prev_processed['metric_final_name'] == metric_full] if quarter_prev_processed is not None and not quarter_prev_processed.empty else None
    
    # DEBUG for Payment Page Visit to Success - check AFTER filtering
    if is_debug_metric:
        debug_print(f"[DEBUG] AFTER FILTERING - quarter_prev_metric:")
        if quarter_prev_metric is not None and not quarter_prev_metric.empty:
            debug_print(f"[DEBUG] AFTER FILTERING - quarter_prev_metric shape: {quarter_prev_metric.shape}")
            debug_print(f"[DEBUG] AFTER FILTERING - reporting_cluster values: {quarter_prev_metric['reporting_cluster'].unique()}")
            debug_print(f"[DEBUG] AFTER FILTERING - reporting_cluster distribution:")
            print(quarter_prev_metric['reporting_cluster'].value_counts())
            bu_level_in_metric = quarter_prev_metric[quarter_prev_metric['reporting_cluster'] == 'bu_level']
            debug_print(f"[DEBUG] AFTER FILTERING - bu_level rows in quarter_prev_metric: {len(bu_level_in_metric)}")
            if not bu_level_in_metric.empty:
                debug_print(f"[DEBUG] AFTER FILTERING - Sample business units: {bu_level_in_metric['business_unit'].head(10).tolist()}")
                debug_print(f"[DEBUG] AFTER FILTERING - Sample relative_change_pct: {bu_level_in_metric['relative_change_pct'].head(10).tolist()}")
        else:
            debug_print(f"[DEBUG] AFTER FILTERING - quarter_prev_metric is None or empty!")
    
    callout = build_callout_for_metric(metric_full, week_prev_metric, week_yoy_metric, quarter_prev_metric)
    
    # Truncate if too long (but allow more for Long Term Impact section)
    if len(callout) > 2000:
        callout = callout[:1997] + "..."
    
    report += f"| **{metric_display}** | {callout} | |\n"

# COMMAND ----------

# Write output
output_folder = OUTPUT_BASE_FOLDER
if not os.path.exists(output_folder):
    try:
        os.makedirs(output_folder)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise

output_file = f'{output_folder}/W{week_num}_steering_report.md'
with open(output_file, 'w') as f:
    f.write(report)

print(f"\n✅ Generated steering report: {output_file}")
print(f"   Week: {latest_week_str}")
print(f"   Metrics processed: {len(METRIC_GROUPS)}")

# Also save to DBFS
dbfs_path = f'/tmp/W{week_num}_steering_report.md'
dbutils.fs.put(dbfs_path, report, overwrite=True)
print(f"   Also saved to DBFS: {dbfs_path}")

# Save debug output to file and DBFS
debug_content = debug_output.getvalue()
if debug_content:
    debug_file = f'{output_folder}/debug_output.txt'
    with open(debug_file, 'w') as f:
        f.write(debug_content)
    print(f"   Debug output saved to: {debug_file}")
    
    # Also save to DBFS
    debug_dbfs_path = f'/tmp/W{week_num}_debug_output.txt'
    dbutils.fs.put(debug_dbfs_path, debug_content, overwrite=True)
    print(f"   Debug output also saved to DBFS: {debug_dbfs_path}")
else:
    print(f"   No debug output captured")
