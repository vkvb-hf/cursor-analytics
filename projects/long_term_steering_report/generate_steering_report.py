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
REPORTING_CLUSTERS = ['Overall', 'HF-NA', 'HF-INTL', 'US-HF', 'RTE', 'WL']

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

# Dimension abbreviations mapping
DIMENSION_ABBREVIATIONS = {
    'PaymentMethod': 'PM',
    'ChannelCategory': 'CC',
    'DeviceType': 'DT',
    'PaymentProvider': 'PP',
    'LoyaltyLevel': 'LL',
    'Country': 'CN',
    'Region': 'RG'
}

def abbreviate_dimension_name(dim_name):
    """Abbreviate dimension name if mapping exists, otherwise return original"""
    if dim_name in DIMENSION_ABBREVIATIONS:
        return DIMENSION_ABBREVIATIONS[dim_name]
    return dim_name

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

# Format week ranges for display
def format_quarter_range(current_weeks, prev_weeks):
    """Format quarter range as '2025 W14-26 vs 2025 W1-13'"""
    if not current_weeks or not prev_weeks:
        return ""
    # Get first and last week from each list
    current_first = current_weeks[-1]  # Last in list is first chronologically
    current_last = current_weeks[0]     # First in list is last chronologically
    prev_first = prev_weeks[-1]
    prev_last = prev_weeks[0]
    
    # Extract year and week number
    def extract_week_num(week_str):
        parts = week_str.split('-W')
        return int(parts[1]) if len(parts) > 1 else None
    
    current_first_num = extract_week_num(current_first)
    current_last_num = extract_week_num(current_last)
    prev_first_num = extract_week_num(prev_first)
    prev_last_num = extract_week_num(prev_last)
    
    if current_first_num and current_last_num and prev_first_num and prev_last_num:
        current_year = current_first.split('-W')[0]
        prev_year = prev_first.split('-W')[0]
        return f"{current_year} W{current_first_num}-{current_last_num} vs {prev_year} W{prev_first_num}-{prev_last_num}"
    return ""

def format_year_range(current_week, prev_year_week):
    """Format year range as '2025 W45 vs 2024 W45'"""
    if not current_week or not prev_year_week:
        return ""
    return f"{current_week} vs {prev_year_week}"

# Create formatted ranges
quarter_range_str = format_quarter_range(latest_13weeks_list, prev_13weeks_list)
year_range_str = format_year_range(latest_week_str, prev_year_week_str)

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
debug_print("   [DEBUG YOY] Building query for year-over-year comparison...")
week_yoy_query = build_metrics_query('WEEK', 'prev_year', latest_week_str)
debug_print(f"   [DEBUG YOY] Query built for date_value: {latest_week_str}")
week_yoy_data = spark.sql(week_yoy_query)
debug_print(f"   [DEBUG YOY] Raw query returned {week_yoy_data.count()} rows")
debug_print(f"   [DEBUG YOY] Columns in week_yoy_data: {week_yoy_data.columns}")

# DEBUG: Check if prev_metric_value columns exist and have data
if 'prev_metric_value_numerator' in week_yoy_data.columns:
    null_prev_num = week_yoy_data.filter(F.col('prev_metric_value_numerator').isNull()).count()
    null_prev_den = week_yoy_data.filter(F.col('prev_metric_value_denominator').isNull()).count()
    debug_print(f"   [DEBUG YOY] Rows with NULL prev_metric_value_numerator: {null_prev_num}")
    debug_print(f"   [DEBUG YOY] Rows with NULL prev_metric_value_denominator: {null_prev_den}")
    
    # Check sample row
    sample_row = week_yoy_data.limit(1)
    if sample_row.count() > 0:
        row = sample_row.collect()[0]
        debug_print(f"   [DEBUG YOY] Sample row:")
        try:
            debug_print(f"     - reporting_cluster: {row['reporting_cluster']}")
            debug_print(f"     - business_unit: {row['business_unit']}")
            metric_name = str(row['metric_final_name'])[:50] if row['metric_final_name'] else 'N/A'
            debug_print(f"     - metric_final_name: {metric_name}...")
            debug_print(f"     - current_metric_value_numerator: {row['current_metric_value_numerator']}")
            debug_print(f"     - current_metric_value_denominator: {row['current_metric_value_denominator']}")
            debug_print(f"     - prev_metric_value_numerator: {row['prev_metric_value_numerator']}")
            debug_print(f"     - prev_metric_value_denominator: {row['prev_metric_value_denominator']}")
        except Exception as e:
            debug_print(f"     - Error accessing row fields: {e}")
    
    # Check reporting_cluster distribution
    debug_print(f"   [DEBUG YOY] reporting_cluster distribution:")
    week_yoy_data.groupBy('reporting_cluster').count().orderBy('reporting_cluster').show(truncate=False)
    
    # Check bu_level rows
    bu_level_count = week_yoy_data.filter(F.col('reporting_cluster') == 'bu_level').count()
    debug_print(f"   [DEBUG YOY] bu_level rows: {bu_level_count}")
    
    # Check Overall rows
    overall_count = week_yoy_data.filter(F.col('reporting_cluster') == 'Overall').count()
    debug_print(f"   [DEBUG YOY] Overall rows: {overall_count}")
else:
    debug_print(f"   [DEBUG YOY] ⚠️  prev_metric_value_numerator column NOT FOUND in week_yoy_data!")

week_yoy_processed = process_comparison_data(week_yoy_data, "Week vs Previous Year Week")
print(f"   Processed {len(week_yoy_processed)} rows")

# DEBUG: Check processed data
if week_yoy_processed is not None and not week_yoy_processed.empty:
    debug_print(f"   [DEBUG YOY] AFTER PROCESSING - week_yoy_processed shape: {week_yoy_processed.shape}")
    debug_print(f"   [DEBUG YOY] AFTER PROCESSING - reporting_cluster distribution:")
    debug_print(str(week_yoy_processed['reporting_cluster'].value_counts()))
    
    # Check Overall rows with _Overall dimension
    overall_yoy = week_yoy_processed[
        (week_yoy_processed['reporting_cluster'] == 'Overall') & 
        (week_yoy_processed['dimension_name'] == '_Overall')
    ]
    debug_print(f"   [DEBUG YOY] AFTER PROCESSING - Overall rows with _Overall dimension: {len(overall_yoy)}")
    if not overall_yoy.empty:
        debug_print(f"   [DEBUG YOY] Sample Overall row relative_change_pct: {overall_yoy.iloc[0]['relative_change_pct']}")
        debug_print(f"   [DEBUG YOY] Sample Overall row prev_ratio: {overall_yoy.iloc[0]['prev_ratio']}")
        debug_print(f"   [DEBUG YOY] Sample Overall row current_ratio: {overall_yoy.iloc[0]['current_ratio']}")
    else:
        debug_print(f"   [DEBUG YOY] ⚠️  No Overall rows with _Overall dimension found!")
else:
    debug_print(f"   [DEBUG YOY] ⚠️  week_yoy_processed is None or empty!")

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
    return 'sig.' if sig_level >= 3 else 'not sig.'

# COMMAND ----------

# Generate key insights
def get_metric_display_name(metric_final_name):
    """Get human-readable metric name from METRIC_GROUPS"""
    for display_name, full_name in METRIC_GROUPS:
        if full_name == metric_final_name:
            return display_name
    # Fallback to last part of metric name if not found
    return metric_final_name.split(' - ')[-1]

def format_metric_value(prev_val, curr_val, metric_type, relative_change_pct):
    """Format metric value based on type (ratio or dollar-ratio)"""
    if metric_type == 'ratio':
        return f"{prev_val*100:.2f}% to {curr_val*100:.2f}%"
    else:
        # For dollar-ratio (euros), don't multiply by 100
        return f"€{prev_val:.2f} to €{curr_val:.2f}"

def generate_key_insights(week_prev_df, week_yoy_df, quarter_prev_df):
    """Generate key insights section"""
    insights = []
    
    # Critical Issues - metrics with significant decreases (week vs prev week)
    critical = []
    if week_prev_df is not None and not week_prev_df.empty:
        overall = week_prev_df[
            (week_prev_df['reporting_cluster'] == 'Overall') & 
            (week_prev_df['dimension_name'] == '_Overall')
        ]
        if not overall.empty:
            for _, row in overall.iterrows():
                if row['relative_change_pct'] < -5:
                    metric_name = get_metric_display_name(row.get('metric_final_name', ''))
                    value_str = format_metric_value(row['prev_ratio'], row['current_ratio'], row.get('metric_type', 'ratio'), row['relative_change_pct'])
                    critical.append(f"{metric_name} decreased {abs(row['relative_change_pct']):.2f}% ({value_str})")
    
    if critical:
        insights.append(f"**Critical Issues:** {', '.join(critical)}")
    else:
        insights.append("**Critical Issues:** None identified")
    
    # Positive Trends - metrics with significant increases (week vs prev week)
    positive = []
    if week_prev_df is not None and not week_prev_df.empty:
        overall = week_prev_df[
            (week_prev_df['reporting_cluster'] == 'Overall') & 
            (week_prev_df['dimension_name'] == '_Overall')
        ]
        if not overall.empty:
            for _, row in overall.iterrows():
                if row['relative_change_pct'] > 5:
                    metric_name = get_metric_display_name(row.get('metric_final_name', ''))
                    value_str = format_metric_value(row['prev_ratio'], row['current_ratio'], row.get('metric_type', 'ratio'), row['relative_change_pct'])
                    positive.append(f"{metric_name} increased {row['relative_change_pct']:.2f}% ({value_str})")
    
    if positive:
        insights.append(f"**Positive Trends:** {', '.join(positive)}")
    else:
        insights.append("**Positive Trends:** Overall metrics stable")
    
    # Risk Shifts - metrics showing diverging trends between HF-NA and HF-INTL
    risks = []
    if week_prev_df is not None and not week_prev_df.empty:
        hfna = week_prev_df[
            (week_prev_df['reporting_cluster'] == 'HF-NA') & 
            (week_prev_df['dimension_name'] == '_Overall')
        ]
        hfintl = week_prev_df[
            (week_prev_df['reporting_cluster'] == 'HF-INTL') & 
            (week_prev_df['dimension_name'] == '_Overall')
        ]
        if not hfna.empty and not hfintl.empty:
            for metric in hfna['metric_final_name'].unique():
                hfna_metric = hfna[hfna['metric_final_name'] == metric]
                hfintl_metric = hfintl[hfintl['metric_final_name'] == metric]
                if not hfna_metric.empty and not hfintl_metric.empty:
                    hfna_change = hfna_metric.iloc[0]['relative_change_pct']
                    hfintl_change = hfintl_metric.iloc[0]['relative_change_pct']
                    if (hfna_change > 0 and hfintl_change < 0) or (hfna_change < 0 and hfintl_change > 0):
                        metric_name = get_metric_display_name(metric)
                        risks.append(f"{metric_name} showing diverging trends")
    
    if risks:
        insights.append(f"**Risk Shifts:** {', '.join(risks)}")
    else:
        insights.append("**Risk Shifts:** No major shifts detected")
    
    # Emerging Concerns - metrics down YoY
    concerns = []
    if week_yoy_df is not None and not week_yoy_df.empty:
        overall = week_yoy_df[
            (week_yoy_df['reporting_cluster'] == 'Overall') & 
            (week_yoy_df['dimension_name'] == '_Overall')
        ]
        if not overall.empty:
            for _, row in overall.iterrows():
                if row['relative_change_pct'] < -10:
                    metric_name = get_metric_display_name(row.get('metric_final_name', ''))
                    concerns.append(f"{metric_name} down {abs(row['relative_change_pct']):.2f}% YoY")
    
    if concerns:
        insights.append(f"**Emerging Concerns:** {', '.join(concerns)}")
    else:
        insights.append("**Emerging Concerns:** Monitor long-term trends")
    
    return "\n".join(insights)

# COMMAND ----------

# Helper function to bucket items by relative_change_pct
def bucket_by_percentage(items_df, item_type='business_unit'):
    """Bucket items into percentage ranges: [+50%], [20%-49%], [10%-19%]
    Only includes items with abs_rel_change >= 10%
    """
    buckets = {
        'high': [],  # >= 50%
        'medium': [],  # 20% - 49%
        'low': []  # 10% - 19%
    }
    
    if items_df is None or items_df.empty:
        return buckets
    
    for _, row in items_df.iterrows():
        # Use abs_rel_change if available, otherwise calculate from relative_change_pct
        if 'abs_rel_change' in row and pd.notna(row['abs_rel_change']):
            abs_rel_change = row['abs_rel_change']
        else:
            rel_change = row['relative_change_pct']
            abs_rel_change = abs(rel_change) if pd.notna(rel_change) else 0
        
        # Only bucket items with abs_rel_change >= 10%
        if abs_rel_change >= 50:
            buckets['high'].append(row)
        elif abs_rel_change >= 20:
            buckets['medium'].append(row)
        elif abs_rel_change >= 10:
            buckets['low'].append(row)
    
    return buckets

# Build callout for a metric - rewritten from scratch following write_formatted_summaries pattern
def build_callout_for_metric(metric_full_name, week_prev_df, week_yoy_df, quarter_prev_df, quarter_range="", year_range=""):
    """Build callout text for a metric following write_formatted_summaries pattern
    Returns: (anomaly_callout, long_term_callout) tuple
    - anomaly_callout: Current Week vs Prev Week and Deep Insights
    - long_term_callout: Long Term Impact and Comparison vs Prev Year
    """
    anomaly_parts = []
    long_term_parts = []
    is_first_anomaly_section = True
    is_first_long_term_section = True
    
    # DEBUG for AR Pre Dunning - define at function start
    is_debug_ar = metric_full_name == '3_Active - 1_1_Overall Total Box Candidates - 2_PreDunningAR'
    
    # Week vs Prev Week - Level 1 (Overall summary) - goes to Anomaly/Callout column
    if week_prev_df is not None and not week_prev_df.empty:
        if not is_first_anomaly_section:
            anomaly_parts.append("")  # Add blank line before section header
        anomaly_parts.append("**Current Week vs Prev Week:**")
        is_first_anomaly_section = False
        
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
                    anomaly_parts.append(f"- **{rc}**: {prev_pct:.2f}% to {curr_pct:.2f}% ({arrow}{abs(row['relative_change_pct']):.2f}%, {sig}, vol: {volume})")
                else:
                    anomaly_parts.append(f"- **{rc}**: €{prev_pct:.2f} to €{curr_pct:.2f} ({arrow}{abs(row['relative_change_pct']):.2f}%, {sig}, vol: {volume})")
        
        # Deep Insights - Level 2 (Dimensions and Business Units) - Same format as Long Term Impact - goes to Anomaly/Callout column
        if not is_first_anomaly_section:
            anomaly_parts.append("")  # Add blank line before section header
        anomaly_parts.append("**Deep Insights**")
        is_first_anomaly_section = False
        
        # Collect all significant dimensions
        all_significant_dims_deep = []
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
                
                if is_debug_ar:
                    debug_print(f"[DEBUG AR] {rc} - After filtering (abs_rel_change>10 OR volume_impacted>30): {len(filtered_dims)} rows")
                    if not filtered_dims.empty:
                        debug_print(f"[DEBUG AR] {rc} - Top filtered dimensions:")
                        for idx, (_, row) in enumerate(filtered_dims.head(5).iterrows()):
                            debug_print(f"  {idx+1}. {row['dimension_name']} {row['dimension_value']}: {row['abs_rel_change']:.2f}%, vol: {row['volume_impacted']:.2f}")
                
                for _, dim_row in filtered_dims.head(3).iterrows():
                    # Exclude PaymentProvider Unknown and PaymentMethod Unknown from insights
                    if (dim_row['dimension_name'] == 'PaymentProvider' and dim_row['dimension_value'] == 'Unknown') or \
                       (dim_row['dimension_name'] == 'PaymentMethod' and dim_row['dimension_value'] == 'Unknown'):
                        continue
                    all_significant_dims_deep.append({
                        'reporting_cluster': rc,
                        'dimension_name': dim_row['dimension_name'],
                        'dimension_value': dim_row['dimension_value'],
                        'relative_change_pct': dim_row['relative_change_pct'],
                        'abs_rel_change': dim_row['abs_rel_change'],
                        'volume_impacted': dim_row['volume_impacted'],
                        'prev_ratio': dim_row['prev_ratio'],
                        'current_ratio': dim_row['current_ratio'],
                        'metric_type': dim_row['metric_type']
                    })
        
        # Collect all significant business units
        all_significant_bu_deep = []
        for rc in REPORTING_CLUSTERS:
            if rc != 'Overall':
                # Get business units for this reporting cluster from country mapping
                rc_bu = country_mapping_df[country_mapping_df['reporting_cluster'] == rc].business_unit.tolist()
                
                # Filter week_prev_df for business units in this cluster
                # Business units can come from bu_level rows OR from rows with actual reporting_cluster and business_unit populated
                bu_level_rows_deep = week_prev_df[week_prev_df['reporting_cluster'] == 'bu_level']
                cluster_bu_rows = week_prev_df[
                    (week_prev_df['reporting_cluster'] == rc) & 
                    (week_prev_df['business_unit'].isin(rc_bu))
                ]
                level2_bu_rows = pd.concat([bu_level_rows_deep[bu_level_rows_deep['business_unit'].isin(rc_bu)], cluster_bu_rows]).drop_duplicates()
                
                if is_debug_ar:
                    debug_print(f"[DEBUG AR] {rc} - bu_level_rows count: {len(bu_level_rows_deep[bu_level_rows_deep['business_unit'].isin(rc_bu)])}")
                    debug_print(f"[DEBUG AR] {rc} - cluster_bu_rows count: {len(cluster_bu_rows)}")
                    debug_print(f"[DEBUG AR] {rc} - level2_bu_rows count: {len(level2_bu_rows)}")
                
                if not level2_bu_rows.empty:
                    level2_bu_rows = level2_bu_rows.copy()
                    level2_bu_rows.loc[:, 'abs_rel_change'] = abs(level2_bu_rows['relative_change_pct'])
                    level2_bu_rows.loc[:, 'volume_impacted'] = level2_bu_rows['current_metric_value_denominator'] * level2_bu_rows['abs_rel_change'] / 100
                    sorted_bu = level2_bu_rows.sort_values('volume_impacted', ascending=False)
                    filtered_bu = sorted_bu[(sorted_bu['abs_rel_change']>10) | (sorted_bu['volume_impacted']>30)]
                    
                    for _, bu_row in filtered_bu.head(2).iterrows():
                        if bu_row['business_unit'] == "Null":
                            continue
                        all_significant_bu_deep.append({
                            'business_unit': bu_row['business_unit'],
                            'relative_change_pct': bu_row['relative_change_pct'],
                            'abs_rel_change': bu_row['abs_rel_change'],
                            'volume_impacted': bu_row['volume_impacted'],
                            'prev_ratio': bu_row['prev_ratio'],
                            'current_ratio': bu_row['current_ratio'],
                            'metric_type': bu_row['metric_type']
                        })
        
        # Bucket and display in specific order: BU [+50%], BU [20-49%], Dims [+50%], Dims [20-49%]
        # First, bucket business units
        bu_buckets_deep = {}
        if all_significant_bu_deep:
            bu_df_deep = pd.DataFrame(all_significant_bu_deep)
            bu_buckets_deep = bucket_by_percentage(bu_df_deep, 'business_unit')
        
        # Then, bucket dimensions
        dim_buckets_deep = {}
        if all_significant_dims_deep:
            dims_df_deep = pd.DataFrame(all_significant_dims_deep)
            dim_buckets_deep = bucket_by_percentage(dims_df_deep, 'dimension')
        
        # Display in specified order: [+50%] BU, [20-49%] BU, [10-19%] BU, [+50%] Dims, [20-49%] Dims, [10-19%] Dims
        # [+50%] - Business Units
        if bu_buckets_deep.get('high'):
            bu_items = []
            for bu_row in bu_buckets_deep['high']:
                arrow = format_arrow(bu_row['relative_change_pct'])
                bu_name = bu_row.get('business_unit', 'Unknown')
                bu_items.append(f"**{bu_name}** ({arrow}{abs(bu_row['relative_change_pct']):.2f}%)")
            anomaly_parts.append(f"[+50%] - Business Units: {', '.join(bu_items)}")
        
        # [20% - 49%] - Business Units
        if bu_buckets_deep.get('medium'):
            bu_items = []
            for bu_row in bu_buckets_deep['medium']:
                arrow = format_arrow(bu_row['relative_change_pct'])
                bu_name = bu_row.get('business_unit', 'Unknown')
                bu_items.append(f"**{bu_name}** ({arrow}{abs(bu_row['relative_change_pct']):.2f}%)")
            anomaly_parts.append(f"[20% - 49%] - Business Units: {', '.join(bu_items)}")
        
        # [10% - 19%] - Business Units
        if bu_buckets_deep.get('low'):
            bu_items = []
            for bu_row in bu_buckets_deep['low']:
                arrow = format_arrow(bu_row['relative_change_pct'])
                bu_name = bu_row.get('business_unit', 'Unknown')
                bu_items.append(f"**{bu_name}** ({arrow}{abs(bu_row['relative_change_pct']):.2f}%)")
            anomaly_parts.append(f"[10% - 19%] - Business Units: {', '.join(bu_items)}")
        
        # [+50%] - Dimensions
        if dim_buckets_deep.get('high'):
            dim_items = []
            for dim_row in dim_buckets_deep['high']:
                arrow = format_arrow(dim_row['relative_change_pct'])
                dim_abbrev = abbreviate_dimension_name(dim_row['dimension_name'])
                item_name = f"{dim_abbrev} {dim_row['dimension_value']}"
                rc_name = dim_row['reporting_cluster']
                dim_items.append(f"**{rc_name}** {item_name} ({arrow}{abs(dim_row['relative_change_pct']):.2f}%)")
            anomaly_parts.append(f"[+50%] - Dimensions: {', '.join(dim_items)}")
        
        # [20% - 49%] - Dimensions
        if dim_buckets_deep.get('medium'):
            dim_items = []
            for dim_row in dim_buckets_deep['medium']:
                arrow = format_arrow(dim_row['relative_change_pct'])
                dim_abbrev = abbreviate_dimension_name(dim_row['dimension_name'])
                item_name = f"{dim_abbrev} {dim_row['dimension_value']}"
                rc_name = dim_row['reporting_cluster']
                dim_items.append(f"**{rc_name}** {item_name} ({arrow}{abs(dim_row['relative_change_pct']):.2f}%)")
            anomaly_parts.append(f"[20% - 49%] - Dimensions: {', '.join(dim_items)}")
        
        # [10% - 19%] - Dimensions
        if dim_buckets_deep.get('low'):
            dim_items = []
            for dim_row in dim_buckets_deep['low']:
                arrow = format_arrow(dim_row['relative_change_pct'])
                dim_abbrev = abbreviate_dimension_name(dim_row['dimension_name'])
                item_name = f"{dim_abbrev} {dim_row['dimension_value']}"
                rc_name = dim_row['reporting_cluster']
                dim_items.append(f"**{rc_name}** {item_name} ({arrow}{abs(dim_row['relative_change_pct']):.2f}%)")
            anomaly_parts.append(f"[10% - 19%] - Dimensions: {', '.join(dim_items)}")
        
        # Check for Overall-level changes in PaymentProvider Unknown and PaymentMethod Unknown
        unknown_callouts = []
        if week_prev_df is not None and not week_prev_df.empty:
            # Check PaymentProvider Unknown at Overall level
            pp_unknown = week_prev_df[
                (week_prev_df['reporting_cluster'] == 'Overall') &
                (week_prev_df['dimension_name'] == 'PaymentProvider') &
                (week_prev_df['dimension_value'] == 'Unknown')
            ]
            if not pp_unknown.empty:
                row = pp_unknown.iloc[0]
                abs_change = abs(row['relative_change_pct'])
                if abs_change >= 10:  # Only show if significant change
                    arrow = format_arrow(row['relative_change_pct'])
                    volume = format_number(row.get('current_metric_value_denominator', 0) * abs_change / 100)
                    prev_pct = row['prev_ratio'] * 100 if row['metric_type'] == 'ratio' else row['prev_ratio']
                    curr_pct = row['current_ratio'] * 100 if row['metric_type'] == 'ratio' else row['current_ratio']
                    # For extreme changes (>500%), also show absolute change in percentage points
                    abs_change_pp = abs(curr_pct - prev_pct)
                    if abs_change > 500:
                        change_str = f"({arrow}{abs_change:.2f}%, {arrow}{abs_change_pp:.2f}pp, vol: {volume})"
                    else:
                        change_str = f"({arrow}{abs_change:.2f}%, vol: {volume})"
                    if row['metric_type'] == 'ratio':
                        unknown_callouts.append(f"**Overall PaymentProvider Unknown**: {prev_pct:.2f}% to {curr_pct:.2f}% {change_str}")
                    else:
                        unknown_callouts.append(f"**Overall PaymentProvider Unknown**: €{prev_pct:.2f} to €{curr_pct:.2f} {change_str}")
            
            # Check PaymentMethod Unknown at Overall level
            pm_unknown = week_prev_df[
                (week_prev_df['reporting_cluster'] == 'Overall') &
                (week_prev_df['dimension_name'] == 'PaymentMethod') &
                (week_prev_df['dimension_value'] == 'Unknown')
            ]
            if not pm_unknown.empty:
                row = pm_unknown.iloc[0]
                abs_change = abs(row['relative_change_pct'])
                if abs_change >= 10:  # Only show if significant change
                    arrow = format_arrow(row['relative_change_pct'])
                    volume = format_number(row.get('current_metric_value_denominator', 0) * abs_change / 100)
                    prev_pct = row['prev_ratio'] * 100 if row['metric_type'] == 'ratio' else row['prev_ratio']
                    curr_pct = row['current_ratio'] * 100 if row['metric_type'] == 'ratio' else row['current_ratio']
                    # For extreme changes (>500%), also show absolute change in percentage points
                    abs_change_pp = abs(curr_pct - prev_pct)
                    if abs_change > 500:
                        change_str = f"({arrow}{abs_change:.2f}%, {arrow}{abs_change_pp:.2f}pp, vol: {volume})"
                    else:
                        change_str = f"({arrow}{abs_change:.2f}%, vol: {volume})"
                    if row['metric_type'] == 'ratio':
                        unknown_callouts.append(f"**Overall PaymentMethod Unknown**: {prev_pct:.2f}% to {curr_pct:.2f}% {change_str}")
                    else:
                        unknown_callouts.append(f"**Overall PaymentMethod Unknown**: €{prev_pct:.2f} to €{curr_pct:.2f} {change_str}")
        
        if unknown_callouts:
            anomaly_parts.append("**Unknown Dimensions Callout:**")
            anomaly_parts.extend(unknown_callouts)
        
        if not bu_buckets_deep.get('high') and not bu_buckets_deep.get('medium') and not bu_buckets_deep.get('low') and not dim_buckets_deep.get('high') and not dim_buckets_deep.get('medium') and not dim_buckets_deep.get('low'):
            if is_debug_ar:
                debug_print(f"[DEBUG AR] ⚠️  No significant insights found!")
                debug_print(f"[DEBUG AR] - all_significant_dims_deep count: {len(all_significant_dims_deep)}")
                debug_print(f"[DEBUG AR] - all_significant_bu_deep count: {len(all_significant_bu_deep)}")
            if not unknown_callouts:  # Only show "No significant insights" if there are no Unknown callouts either
                anomaly_parts.append("- No significant insights")
    
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
        # DEBUG: Track data flow for Payment Page Visit to Success and AR Pre Dunning
        is_debug_metric = metric_full_name == '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
        is_debug_ar_lt = metric_full_name == '3_Active - 1_1_Overall Total Box Candidates - 2_PreDunningAR'
        
        if is_debug_metric or is_debug_ar_lt:
            debug_print(f"\n[DEBUG build_callout_for_metric] Starting Long Term Impact for: {metric_full_name}")
            debug_print(f"[DEBUG] STEP 1 - Input quarter_prev_df shape: {quarter_prev_df.shape}")
            debug_print(f"[DEBUG] STEP 1 - Input quarter_prev_df reporting_cluster values: {quarter_prev_df['reporting_cluster'].unique()}")
            bu_level_input = quarter_prev_df[quarter_prev_df['reporting_cluster'] == 'bu_level']
            debug_print(f"[DEBUG] STEP 1 - bu_level rows in input: {len(bu_level_input)}")
            # Also check for business units in other reporting_cluster rows
            other_bu_rows = quarter_prev_df[
                (quarter_prev_df['reporting_cluster'] != 'bu_level') & 
                (quarter_prev_df['business_unit'].notna()) & 
                (quarter_prev_df['business_unit'] != 'Null') & 
                (quarter_prev_df['business_unit'] != '')
            ]
            debug_print(f"[DEBUG] STEP 1 - Business units in other reporting_cluster rows: {len(other_bu_rows)}")
            if not other_bu_rows.empty:
                debug_print(f"[DEBUG] STEP 1 - Sample business units from other rows: {other_bu_rows['business_unit'].unique()[:10]}")
        
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
        
        # Also check for business units in other reporting_cluster rows (from first UNION)
        # These would have actual reporting_cluster values (HF-NA, HF-INTL, etc.) and business_unit populated
        other_bu_rows = df_metric[
            (df_metric['reporting_cluster'] != 'bu_level') & 
            (df_metric['reporting_cluster'] != 'Overall') &
            (df_metric['business_unit'].notna()) & 
            (df_metric['business_unit'] != 'Null') & 
            (df_metric['business_unit'] != '') &
            (df_metric['dimension_name'] == '_Overall')
        ].copy()
        
        if is_debug_metric or is_debug_ar_lt:
            debug_print(f"[DEBUG] STEP 4 - bu_level_rows count: {len(bu_level_rows)}")
            debug_print(f"[DEBUG] STEP 4 - other_bu_rows count: {len(other_bu_rows)}")
            if not bu_level_rows.empty:
                debug_print(f"[DEBUG] STEP 4 - bu_level_rows dimension_name values: {bu_level_rows['dimension_name'].unique()}")
                debug_print(f"[DEBUG] STEP 4 - Sample business units from bu_level: {bu_level_rows['business_unit'].head(10).tolist()}")
                debug_print(f"[DEBUG] STEP 4 - Sample relative_change_pct from bu_level: {bu_level_rows['relative_change_pct'].head(10).tolist()}")
            if not other_bu_rows.empty:
                debug_print(f"[DEBUG] STEP 4 - Sample business units from other rows: {other_bu_rows['business_unit'].unique()[:10]}")
                debug_print(f"[DEBUG] STEP 4 - Sample relative_change_pct from other rows: {other_bu_rows['relative_change_pct'].head(10).tolist()}")
        
        # Also check if there are business units in other reporting_cluster rows (from first UNION)
        # These would have actual reporting_cluster values (HF-NA, HF-INTL, etc.) and business_unit populated
        # But based on the query structure, business units only come from bu_level rows
        # So we only need to check bu_level
        
        # Combine bu_level_rows and other_bu_rows for processing
        all_bu_rows = pd.concat([bu_level_rows, other_bu_rows]).drop_duplicates() if not bu_level_rows.empty or not other_bu_rows.empty else pd.DataFrame()
        
        if not all_bu_rows.empty:
            if is_debug_metric or is_debug_ar_lt:
                debug_print(f"[DEBUG] STEP 5 - Processing reporting clusters to find business units...")
                debug_print(f"[DEBUG] STEP 5 - Total combined bu rows: {len(all_bu_rows)}")
            
            # Process each reporting cluster to find its business units
            for rc in REPORTING_CLUSTERS:
                if rc != 'Overall':
                    # Get business units for this reporting cluster from country mapping
                    rc_bu = country_mapping_df[country_mapping_df['reporting_cluster'] == rc].business_unit.tolist()
                    # Convert to string and strip for matching (country_mapping_df is already normalized, but be defensive)
                    rc_bu = [str(bu).strip() for bu in rc_bu]
                    
                    if is_debug_metric or is_debug_ar_lt:
                        debug_print(f"[DEBUG] STEP 5.{rc} - Business units in {rc}: {len(rc_bu)} ({rc_bu[:5]}...)")
                    
                    # Filter all_bu_rows for business units in this cluster
                    # all_bu_rows is already normalized at the start of the function
                    level2_bu_rows = all_bu_rows[all_bu_rows['business_unit'].isin(rc_bu)]
                    
                    if is_debug_metric or is_debug_ar_lt:
                        debug_print(f"[DEBUG] STEP 5.{rc} - After filtering by business_unit.isin(rc_bu): {len(level2_bu_rows)} rows")
                    
                    if not level2_bu_rows.empty:
                        level2_bu_rows = level2_bu_rows.copy()
                        level2_bu_rows.loc[:, 'abs_rel_change'] = abs(level2_bu_rows['relative_change_pct'])
                        level2_bu_rows.loc[:, 'volume_impacted'] = level2_bu_rows['current_metric_value_denominator'] * level2_bu_rows['abs_rel_change'] / 100
                        
                        if is_debug_metric or is_debug_ar_lt:
                            debug_print(f"[DEBUG] STEP 5.{rc} - After calculating abs_rel_change and volume_impacted")
                            debug_print(f"[DEBUG] STEP 5.{rc} - Sample abs_rel_change: {level2_bu_rows['abs_rel_change'].head(5).tolist()}")
                            debug_print(f"[DEBUG] STEP 5.{rc} - Sample volume_impacted: {level2_bu_rows['volume_impacted'].head(5).tolist()}")
                        
                        sorted_bu = level2_bu_rows.sort_values('volume_impacted', ascending=False)
                        filtered_bu = sorted_bu[(sorted_bu['abs_rel_change']>10) | (sorted_bu['volume_impacted']>30)]
                        
                        if is_debug_metric or is_debug_ar_lt:
                            debug_print(f"[DEBUG] STEP 5.{rc} - After filtering (abs_rel_change>10 OR volume_impacted>30): {len(filtered_bu)} rows")
                            if not filtered_bu.empty:
                                debug_print(f"[DEBUG] STEP 5.{rc} - Significant business units: {filtered_bu['business_unit'].tolist()}")
                                debug_print(f"[DEBUG] STEP 5.{rc} - Sample volume_impacted: {filtered_bu['volume_impacted'].head(5).tolist()}")
                        
                        for _, row in filtered_bu.iterrows():
                            if row['business_unit'] == "Null" or pd.isna(row['business_unit']) or row['business_unit'] == '':
                                continue
                            all_significant_bu.append(row)
        
        if is_debug_metric or is_debug_ar_lt:
            debug_print(f"[DEBUG] STEP 6 - Total significant business units collected: {len(all_significant_bu)}")
            if all_significant_bu:
                bu_names = [r['business_unit'] if isinstance(r, dict) else r.get('business_unit', 'Unknown') for r in all_significant_bu]
                debug_print(f"[DEBUG] STEP 6 - Significant business units: {bu_names}")
        
        # Check if we should show Long Term Impact
        has_significant_overall = not overall_rows.empty and abs(overall_rows.iloc[0]['relative_change_pct']) > 10
        has_significant_bu = len(all_significant_bu) > 0
        
        # Collect significant dimensions (similar to Deep Insights)
        all_significant_dims = []
        
        # Process each reporting cluster for dimensions
        for rc in REPORTING_CLUSTERS:
            # Level 2 - Dimensions (excluding _Overall)
            level2_dims_rows = df_metric[
                (df_metric['reporting_cluster'] == rc) & 
                (df_metric['dimension_name'] != '_Overall')
            ]
            
            if not level2_dims_rows.empty:
                level2_dims_rows = level2_dims_rows.copy()
                level2_dims_rows.loc[:, 'abs_rel_change'] = abs(level2_dims_rows['relative_change_pct'])
                level2_dims_rows.loc[:, 'volume_impacted'] = level2_dims_rows['current_metric_value_denominator'] * level2_dims_rows['abs_rel_change'] / 100
                sorted_dims = level2_dims_rows.sort_values(['dimension_name', 'volume_impacted'], ascending=False)
                filtered_dims = sorted_dims[(sorted_dims['abs_rel_change']>10) | (sorted_dims['volume_impacted']>30)]
                
                # Collect significant dimensions
                for _, dim_row in filtered_dims.head(3).iterrows():
                    # Exclude PaymentProvider Unknown and PaymentMethod Unknown from insights
                    if (dim_row['dimension_name'] == 'PaymentProvider' and dim_row['dimension_value'] == 'Unknown') or \
                       (dim_row['dimension_name'] == 'PaymentMethod' and dim_row['dimension_value'] == 'Unknown'):
                        continue
                    all_significant_dims.append({
                        'reporting_cluster': rc,
                        'dimension_name': dim_row['dimension_name'],
                        'dimension_value': dim_row['dimension_value'],
                        'relative_change_pct': dim_row['relative_change_pct'],
                        'abs_rel_change': dim_row['abs_rel_change'],
                        'volume_impacted': dim_row['volume_impacted'],
                        'prev_ratio': dim_row['prev_ratio'],
                        'current_ratio': dim_row['current_ratio'],
                        'metric_type': dim_row['metric_type']
                    })
        
        # Check if we should show Long Term Impact (including dimensions)
        has_significant_dims = len(all_significant_dims) > 0
        
        if is_debug_metric or is_debug_ar_lt:
            debug_print(f"[DEBUG] STEP 7 - has_significant_overall: {has_significant_overall}, has_significant_bu: {has_significant_bu}, has_significant_dims: {has_significant_dims}")
            if all_significant_dims:
                debug_print(f"[DEBUG] STEP 7 - Significant dimensions count: {len(all_significant_dims)}")
            if not has_significant_overall and not has_significant_bu and not has_significant_dims:
                debug_print(f"[DEBUG] STEP 7 - ⚠️  No significant data found for Long Term Impact!")
        
        if has_significant_overall or has_significant_bu or has_significant_dims:
            # Format header with range - goes to Long Term Impact column
            if not is_first_long_term_section:
                long_term_parts.append("")  # Add blank line before section header
            header = "**Long Term Impact**"
            if quarter_range:
                header += f" ({quarter_range})"
            long_term_parts.append(header)
            is_first_long_term_section = False
            
            # Add Overall if it exists
            if not overall_rows.empty:
                row = overall_rows.iloc[0]
                arrow = format_arrow(row['relative_change_pct'])
                volume = format_number(row.get('current_metric_value_denominator', 0) * abs(row['relative_change_pct']) / 100)
                prev_pct = row['prev_ratio'] * 100 if row['metric_type'] == 'ratio' else row['prev_ratio']
                curr_pct = row['current_ratio'] * 100 if row['metric_type'] == 'ratio' else row['current_ratio']
                
                if row['metric_type'] == 'ratio':
                    long_term_parts.append(f"- **Overall**: {prev_pct:.2f}% to {curr_pct:.2f}% ({arrow}{abs(row['relative_change_pct']):.2f}%, volume: {volume})")
                else:
                    long_term_parts.append(f"- **Overall**: €{prev_pct:.2f} to €{curr_pct:.2f} ({arrow}{abs(row['relative_change_pct']):.2f}%, volume: {volume})")
            
            # Bucket and display in specific order: BU [+50%], BU [20-49%], Dims [+50%], Dims [20-49%]
            # First, bucket business units
            bu_buckets = {}
            if all_significant_bu:
                bu_df = pd.DataFrame(all_significant_bu)
                bu_buckets = bucket_by_percentage(bu_df, 'business_unit')
            
            # Then, bucket dimensions
            dim_buckets = {}
            if all_significant_dims:
                dims_df = pd.DataFrame(all_significant_dims)
                dim_buckets = bucket_by_percentage(dims_df, 'dimension')
            
            # Display in specified order: [+50%] BU, [20-49%] BU, [10-19%] BU, [+50%] Dims, [20-49%] Dims, [10-19%] Dims
            # [+50%] - Business Units
            if bu_buckets.get('high'):
                bu_items = []
                for bu_row in bu_buckets['high']:
                    arrow = format_arrow(bu_row['relative_change_pct'])
                    bu_name = bu_row.get('business_unit', 'Unknown')
                    bu_items.append(f"**{bu_name}** ({arrow}{abs(bu_row['relative_change_pct']):.2f}%)")
                long_term_parts.append(f"[+50%] - Business Units: {', '.join(bu_items)}")
            
            # [20% - 49%] - Business Units
            if bu_buckets.get('medium'):
                bu_items = []
                for bu_row in bu_buckets['medium']:
                    arrow = format_arrow(bu_row['relative_change_pct'])
                    bu_name = bu_row.get('business_unit', 'Unknown')
                    bu_items.append(f"**{bu_name}** ({arrow}{abs(bu_row['relative_change_pct']):.2f}%)")
                long_term_parts.append(f"[20% - 49%] - Business Units: {', '.join(bu_items)}")
            
            # [10% - 19%] - Business Units
            if bu_buckets.get('low'):
                bu_items = []
                for bu_row in bu_buckets['low']:
                    arrow = format_arrow(bu_row['relative_change_pct'])
                    bu_name = bu_row.get('business_unit', 'Unknown')
                    bu_items.append(f"**{bu_name}** ({arrow}{abs(bu_row['relative_change_pct']):.2f}%)")
                long_term_parts.append(f"[10% - 19%] - Business Units: {', '.join(bu_items)}")
            
            # [+50%] - Dimensions
            if dim_buckets.get('high'):
                dim_items = []
                for dim_row in dim_buckets['high']:
                    arrow = format_arrow(dim_row['relative_change_pct'])
                    dim_abbrev = abbreviate_dimension_name(dim_row['dimension_name'])
                    item_name = f"{dim_abbrev} {dim_row['dimension_value']}"
                    rc_name = dim_row['reporting_cluster']
                    dim_items.append(f"**{rc_name}** {item_name} ({arrow}{abs(dim_row['relative_change_pct']):.2f}%)")
                long_term_parts.append(f"[+50%] - Dimensions: {', '.join(dim_items)}")
            
            # [20% - 49%] - Dimensions
            if dim_buckets.get('medium'):
                dim_items = []
                for dim_row in dim_buckets['medium']:
                    arrow = format_arrow(dim_row['relative_change_pct'])
                    dim_abbrev = abbreviate_dimension_name(dim_row['dimension_name'])
                    item_name = f"{dim_abbrev} {dim_row['dimension_value']}"
                    rc_name = dim_row['reporting_cluster']
                    dim_items.append(f"**{rc_name}** {item_name} ({arrow}{abs(dim_row['relative_change_pct']):.2f}%)")
                long_term_parts.append(f"[20% - 49%] - Dimensions: {', '.join(dim_items)}")
            
            # [10% - 19%] - Dimensions
            if dim_buckets.get('low'):
                dim_items = []
                for dim_row in dim_buckets['low']:
                    arrow = format_arrow(dim_row['relative_change_pct'])
                    dim_abbrev = abbreviate_dimension_name(dim_row['dimension_name'])
                    item_name = f"{dim_abbrev} {dim_row['dimension_value']}"
                    rc_name = dim_row['reporting_cluster']
                    dim_items.append(f"**{rc_name}** {item_name} ({arrow}{abs(dim_row['relative_change_pct']):.2f}%)")
                long_term_parts.append(f"[10% - 19%] - Dimensions: {', '.join(dim_items)}")
            
            # Check for Overall-level changes in PaymentProvider Unknown and PaymentMethod Unknown (Long Term Impact)
            unknown_callouts_lt = []
            if df_metric is not None and not df_metric.empty:
                # Check PaymentProvider Unknown at Overall level
                pp_unknown_lt = df_metric[
                    (df_metric['reporting_cluster'] == 'Overall') &
                    (df_metric['dimension_name'] == 'PaymentProvider') &
                    (df_metric['dimension_value'] == 'Unknown')
                ]
                if not pp_unknown_lt.empty:
                    row = pp_unknown_lt.iloc[0]
                    abs_change = abs(row['relative_change_pct'])
                    if abs_change >= 10:  # Only show if significant change
                        arrow = format_arrow(row['relative_change_pct'])
                        volume = format_number(row.get('current_metric_value_denominator', 0) * abs_change / 100)
                        prev_pct = row['prev_ratio'] * 100 if row['metric_type'] == 'ratio' else row['prev_ratio']
                        curr_pct = row['current_ratio'] * 100 if row['metric_type'] == 'ratio' else row['current_ratio']
                        # For extreme changes (>500%), also show absolute change in percentage points
                        abs_change_pp = abs(curr_pct - prev_pct)
                        if abs_change > 500:
                            change_str = f"({arrow}{abs_change:.2f}%, {arrow}{abs_change_pp:.2f}pp, vol: {volume})"
                        else:
                            change_str = f"({arrow}{abs_change:.2f}%, vol: {volume})"
                        if row['metric_type'] == 'ratio':
                            unknown_callouts_lt.append(f"**Overall PaymentProvider Unknown**: {prev_pct:.2f}% to {curr_pct:.2f}% {change_str}")
                        else:
                            unknown_callouts_lt.append(f"**Overall PaymentProvider Unknown**: €{prev_pct:.2f} to €{curr_pct:.2f} {change_str}")
                
                # Check PaymentMethod Unknown at Overall level
                pm_unknown_lt = df_metric[
                    (df_metric['reporting_cluster'] == 'Overall') &
                    (df_metric['dimension_name'] == 'PaymentMethod') &
                    (df_metric['dimension_value'] == 'Unknown')
                ]
                if not pm_unknown_lt.empty:
                    row = pm_unknown_lt.iloc[0]
                    abs_change = abs(row['relative_change_pct'])
                    if abs_change >= 10:  # Only show if significant change
                        arrow = format_arrow(row['relative_change_pct'])
                        volume = format_number(row.get('current_metric_value_denominator', 0) * abs_change / 100)
                        prev_pct = row['prev_ratio'] * 100 if row['metric_type'] == 'ratio' else row['prev_ratio']
                        curr_pct = row['current_ratio'] * 100 if row['metric_type'] == 'ratio' else row['current_ratio']
                        # For extreme changes (>500%), also show absolute change in percentage points
                        abs_change_pp = abs(curr_pct - prev_pct)
                        if abs_change > 500:
                            change_str = f"({arrow}{abs_change:.2f}%, {arrow}{abs_change_pp:.2f}pp, vol: {volume})"
                        else:
                            change_str = f"({arrow}{abs_change:.2f}%, vol: {volume})"
                        if row['metric_type'] == 'ratio':
                            unknown_callouts_lt.append(f"**Overall PaymentMethod Unknown**: {prev_pct:.2f}% to {curr_pct:.2f}% {change_str}")
                        else:
                            unknown_callouts_lt.append(f"**Overall PaymentMethod Unknown**: €{prev_pct:.2f} to €{curr_pct:.2f} {change_str}")
            
            if unknown_callouts_lt:
                long_term_parts.append("**Unknown Dimensions Callout:**")
                long_term_parts.extend(unknown_callouts_lt)
        else:
            if not is_first_long_term_section:
                long_term_parts.append("")  # Add blank line before section header
            header = "**Long Term Impact**"
            if quarter_range:
                header += f" ({quarter_range})"
            long_term_parts.append(header)
            is_first_long_term_section = False
            long_term_parts.append("- No significant long-term impact (all changes <10%)")
    else:
        if not is_first_long_term_section:
            long_term_parts.append("")  # Add blank line before section header
        header = "**Long Term Impact**"
        if quarter_range:
            header += f" ({quarter_range})"
        long_term_parts.append(header)
        is_first_long_term_section = False
        long_term_parts.append("- No significant long-term impact (all changes <10%)")
    
    # Comparison vs Prev Year
    is_debug_metric_yoy = metric_full_name == '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
    
    if is_debug_metric_yoy:
        debug_print(f"\n[DEBUG YOY - build_callout_for_metric] Processing metric: {metric_full_name}")
        debug_print(f"[DEBUG YOY] week_yoy_df is None: {week_yoy_df is None}")
        if week_yoy_df is not None:
            debug_print(f"[DEBUG YOY] week_yoy_df.empty: {week_yoy_df.empty}")
            debug_print(f"[DEBUG YOY] week_yoy_df.shape: {week_yoy_df.shape}")
            debug_print(f"[DEBUG YOY] week_yoy_df reporting_cluster values: {week_yoy_df['reporting_cluster'].unique()}")
            debug_print(f"[DEBUG YOY] week_yoy_df dimension_name values: {week_yoy_df['dimension_name'].unique()}")
    
    if week_yoy_df is not None and not week_yoy_df.empty:
        # Normalize data types for consistent filtering
        week_yoy_df = week_yoy_df.copy()
        week_yoy_df['reporting_cluster'] = week_yoy_df['reporting_cluster'].astype(str).str.strip()
        week_yoy_df['business_unit'] = week_yoy_df['business_unit'].astype(str).str.strip()
        
        overall_yoy = week_yoy_df[
            (week_yoy_df['reporting_cluster'] == 'Overall') & 
            (week_yoy_df['dimension_name'] == '_Overall')
        ]
        
        if is_debug_metric_yoy:
            debug_print(f"[DEBUG YOY] overall_yoy.empty: {overall_yoy.empty}")
            debug_print(f"[DEBUG YOY] overall_yoy.shape: {overall_yoy.shape}")
            if not overall_yoy.empty:
                debug_print(f"[DEBUG YOY] overall_yoy.iloc[0] relative_change_pct: {overall_yoy.iloc[0]['relative_change_pct']}")
        
        # Collect significant business units (similar to Long Term Impact)
        all_significant_bu_yoy = []
        
        # Get bu_level rows
        bu_level_rows_yoy = week_yoy_df[week_yoy_df['reporting_cluster'] == 'bu_level']
        
        if is_debug_metric_yoy:
            debug_print(f"[DEBUG YOY] bu_level_rows_yoy count: {len(bu_level_rows_yoy)}")
        
        if not bu_level_rows_yoy.empty:
            # Process each reporting cluster to find business units
            for rc in REPORTING_CLUSTERS:
                if rc == 'Overall':
                    continue
                
                # Get business units for this reporting cluster
                rc_bu = country_mapping_df[country_mapping_df['reporting_cluster'] == rc].business_unit.tolist()
                
                # Filter bu_level rows for this cluster's business units
                rc_bu_rows = bu_level_rows_yoy[bu_level_rows_yoy['business_unit'].isin(rc_bu)]
                
                if not rc_bu_rows.empty:
                    rc_bu_rows = rc_bu_rows.copy()
                    rc_bu_rows.loc[:, 'abs_rel_change'] = abs(rc_bu_rows['relative_change_pct'])
                    rc_bu_rows.loc[:, 'volume_impacted'] = rc_bu_rows['current_metric_value_denominator'] * rc_bu_rows['abs_rel_change'] / 100
                    
                    # Filter for significant business units
                    filtered_bu = rc_bu_rows[(rc_bu_rows['abs_rel_change'] > 10) | (rc_bu_rows['volume_impacted'] > 30)]
                    
                    if is_debug_metric_yoy:
                        debug_print(f"[DEBUG YOY] {rc} - Significant business units: {len(filtered_bu)}")
                    
                    # Collect significant business units
                    for _, bu_row in filtered_bu.iterrows():
                        if bu_row['business_unit'] != "Null":
                            all_significant_bu_yoy.append({
                                'business_unit': bu_row['business_unit'],
                                'relative_change_pct': bu_row['relative_change_pct'],
                                'abs_rel_change': bu_row['abs_rel_change'],
                                'volume_impacted': bu_row['volume_impacted'],
                                'prev_ratio': bu_row['prev_ratio'],
                                'current_ratio': bu_row['current_ratio'],
                                'metric_type': bu_row['metric_type']
                            })
        
        # Collect significant dimensions (similar to Long Term Impact)
        all_significant_dims_yoy = []
        
        # Process each reporting cluster for dimensions
        for rc in REPORTING_CLUSTERS:
            # Level 2 - Dimensions (excluding _Overall)
            level2_dims_rows = week_yoy_df[
                (week_yoy_df['reporting_cluster'] == rc) & 
                (week_yoy_df['dimension_name'] != '_Overall')
            ]
            
            if not level2_dims_rows.empty:
                level2_dims_rows = level2_dims_rows.copy()
                level2_dims_rows.loc[:, 'abs_rel_change'] = abs(level2_dims_rows['relative_change_pct'])
                level2_dims_rows.loc[:, 'volume_impacted'] = level2_dims_rows['current_metric_value_denominator'] * level2_dims_rows['abs_rel_change'] / 100
                sorted_dims = level2_dims_rows.sort_values(['dimension_name', 'volume_impacted'], ascending=False)
                filtered_dims = sorted_dims[(sorted_dims['abs_rel_change']>10) | (sorted_dims['volume_impacted']>30)]
                
                # Collect significant dimensions
                for _, dim_row in filtered_dims.head(3).iterrows():
                    # Exclude PaymentProvider Unknown and PaymentMethod Unknown from insights
                    if (dim_row['dimension_name'] == 'PaymentProvider' and dim_row['dimension_value'] == 'Unknown') or \
                       (dim_row['dimension_name'] == 'PaymentMethod' and dim_row['dimension_value'] == 'Unknown'):
                        continue
                    all_significant_dims_yoy.append({
                        'reporting_cluster': rc,
                        'dimension_name': dim_row['dimension_name'],
                        'dimension_value': dim_row['dimension_value'],
                        'relative_change_pct': dim_row['relative_change_pct'],
                        'abs_rel_change': dim_row['abs_rel_change'],
                        'volume_impacted': dim_row['volume_impacted'],
                        'prev_ratio': dim_row['prev_ratio'],
                        'current_ratio': dim_row['current_ratio'],
                        'metric_type': dim_row['metric_type']
                    })
        
        if is_debug_metric_yoy:
            debug_print(f"[DEBUG YOY] Total significant business units: {len(all_significant_bu_yoy)}")
            debug_print(f"[DEBUG YOY] Total significant dimensions: {len(all_significant_dims_yoy)}")
        
        # Show year-over-year section if we have Overall data, significant business units, or dimensions - goes to Long Term Impact column
        has_significant_dims_yoy = len(all_significant_dims_yoy) > 0
        if not overall_yoy.empty or all_significant_bu_yoy or has_significant_dims_yoy:
            # Format header with range
            if not is_first_long_term_section:
                long_term_parts.append("")  # Add blank line before section header
            header = "**Comparison vs Prev Year**"
            if year_range:
                header += f" ({year_range})"
            long_term_parts.append(header)
            is_first_long_term_section = False
            
            # Add Overall if it exists
            if not overall_yoy.empty:
                row = overall_yoy.iloc[0]
                arrow = format_arrow(row['relative_change_pct'])
                volume = format_number(row.get('current_metric_value_denominator', 0) * abs(row['relative_change_pct']) / 100)
                prev_pct = row['prev_ratio'] * 100 if row['metric_type'] == 'ratio' else row['prev_ratio']
                curr_pct = row['current_ratio'] * 100 if row['metric_type'] == 'ratio' else row['current_ratio']
                
                if row['metric_type'] == 'ratio':
                    long_term_parts.append(f"- **Overall**: {prev_pct:.2f}% to {curr_pct:.2f}% ({arrow}{abs(row['relative_change_pct']):.2f}%, volume: {volume})")
                else:
                    long_term_parts.append(f"- **Overall**: €{prev_pct:.2f} to €{curr_pct:.2f} ({arrow}{abs(row['relative_change_pct']):.2f}%, volume: {volume})")
            
            # Bucket and display in specific order: BU [+50%], BU [20-49%], Dims [+50%], Dims [20-49%]
            # First, bucket business units
            bu_buckets_yoy = {}
            if all_significant_bu_yoy:
                bu_df_yoy = pd.DataFrame(all_significant_bu_yoy)
                bu_buckets_yoy = bucket_by_percentage(bu_df_yoy, 'business_unit')
            
            # Then, bucket dimensions
            dim_buckets_yoy = {}
            if all_significant_dims_yoy:
                dims_df_yoy = pd.DataFrame(all_significant_dims_yoy)
                dim_buckets_yoy = bucket_by_percentage(dims_df_yoy, 'dimension')
            
            # Display in specified order: [+50%] BU, [20-49%] BU, [+50%] Dims, [20-49%] Dims
            # [+50%] - Business Units
            if bu_buckets_yoy.get('high'):
                bu_items = []
                for bu_row in bu_buckets_yoy['high']:
                    arrow = format_arrow(bu_row['relative_change_pct'])
                    bu_name = bu_row.get('business_unit', 'Unknown')
                    bu_items.append(f"**{bu_name}** ({arrow}{abs(bu_row['relative_change_pct']):.2f}%)")
                long_term_parts.append(f"[+50%] - Business Units: {', '.join(bu_items)}")
            
            # [20% - 49%] - Business Units
            if bu_buckets_yoy.get('medium'):
                bu_items = []
                for bu_row in bu_buckets_yoy['medium']:
                    arrow = format_arrow(bu_row['relative_change_pct'])
                    bu_name = bu_row.get('business_unit', 'Unknown')
                    bu_items.append(f"**{bu_name}** ({arrow}{abs(bu_row['relative_change_pct']):.2f}%)")
                long_term_parts.append(f"[20% - 49%] - Business Units: {', '.join(bu_items)}")
            
            # [+50%] - Dimensions
            if dim_buckets_yoy.get('high'):
                dim_items = []
                for dim_row in dim_buckets_yoy['high']:
                    arrow = format_arrow(dim_row['relative_change_pct'])
                    dim_abbrev = abbreviate_dimension_name(dim_row['dimension_name'])
                    item_name = f"{dim_abbrev} {dim_row['dimension_value']}"
                    rc_name = dim_row['reporting_cluster']
                    dim_items.append(f"**{rc_name}** {item_name} ({arrow}{abs(dim_row['relative_change_pct']):.2f}%)")
                long_term_parts.append(f"[+50%] - Dimensions: {', '.join(dim_items)}")
            
            # [20% - 49%] - Dimensions
            if dim_buckets_yoy.get('medium'):
                dim_items = []
                for dim_row in dim_buckets_yoy['medium']:
                    arrow = format_arrow(dim_row['relative_change_pct'])
                    dim_abbrev = abbreviate_dimension_name(dim_row['dimension_name'])
                    item_name = f"{dim_abbrev} {dim_row['dimension_value']}"
                    rc_name = dim_row['reporting_cluster']
                    dim_items.append(f"**{rc_name}** {item_name} ({arrow}{abs(dim_row['relative_change_pct']):.2f}%)")
                long_term_parts.append(f"[20% - 49%] - Dimensions: {', '.join(dim_items)}")
            
            # Check for Overall-level changes in PaymentProvider Unknown and PaymentMethod Unknown (Year-over-Year)
            unknown_callouts_yoy = []
            if week_yoy_df is not None and not week_yoy_df.empty:
                # Check PaymentProvider Unknown at Overall level
                pp_unknown_yoy = week_yoy_df[
                    (week_yoy_df['reporting_cluster'] == 'Overall') &
                    (week_yoy_df['dimension_name'] == 'PaymentProvider') &
                    (week_yoy_df['dimension_value'] == 'Unknown')
                ]
                if not pp_unknown_yoy.empty:
                    row = pp_unknown_yoy.iloc[0]
                    abs_change = abs(row['relative_change_pct'])
                    if abs_change >= 10:  # Only show if significant change
                        arrow = format_arrow(row['relative_change_pct'])
                        volume = format_number(row.get('current_metric_value_denominator', 0) * abs_change / 100)
                        prev_pct = row['prev_ratio'] * 100 if row['metric_type'] == 'ratio' else row['prev_ratio']
                        curr_pct = row['current_ratio'] * 100 if row['metric_type'] == 'ratio' else row['current_ratio']
                        # For extreme changes (>500%), also show absolute change in percentage points
                        abs_change_pp = abs(curr_pct - prev_pct)
                        if abs_change > 500:
                            change_str = f"({arrow}{abs_change:.2f}%, {arrow}{abs_change_pp:.2f}pp, vol: {volume})"
                        else:
                            change_str = f"({arrow}{abs_change:.2f}%, vol: {volume})"
                        if row['metric_type'] == 'ratio':
                            unknown_callouts_yoy.append(f"**Overall PaymentProvider Unknown**: {prev_pct:.2f}% to {curr_pct:.2f}% {change_str}")
                        else:
                            unknown_callouts_yoy.append(f"**Overall PaymentProvider Unknown**: €{prev_pct:.2f} to €{curr_pct:.2f} {change_str}")
                
                # Check PaymentMethod Unknown at Overall level
                pm_unknown_yoy = week_yoy_df[
                    (week_yoy_df['reporting_cluster'] == 'Overall') &
                    (week_yoy_df['dimension_name'] == 'PaymentMethod') &
                    (week_yoy_df['dimension_value'] == 'Unknown')
                ]
                if not pm_unknown_yoy.empty:
                    row = pm_unknown_yoy.iloc[0]
                    abs_change = abs(row['relative_change_pct'])
                    if abs_change >= 10:  # Only show if significant change
                        arrow = format_arrow(row['relative_change_pct'])
                        volume = format_number(row.get('current_metric_value_denominator', 0) * abs_change / 100)
                        prev_pct = row['prev_ratio'] * 100 if row['metric_type'] == 'ratio' else row['prev_ratio']
                        curr_pct = row['current_ratio'] * 100 if row['metric_type'] == 'ratio' else row['current_ratio']
                        # For extreme changes (>500%), also show absolute change in percentage points
                        abs_change_pp = abs(curr_pct - prev_pct)
                        if abs_change > 500:
                            change_str = f"({arrow}{abs_change:.2f}%, {arrow}{abs_change_pp:.2f}pp, vol: {volume})"
                        else:
                            change_str = f"({arrow}{abs_change:.2f}%, vol: {volume})"
                        if row['metric_type'] == 'ratio':
                            unknown_callouts_yoy.append(f"**Overall PaymentMethod Unknown**: {prev_pct:.2f}% to {curr_pct:.2f}% {change_str}")
                        else:
                            unknown_callouts_yoy.append(f"**Overall PaymentMethod Unknown**: €{prev_pct:.2f} to €{curr_pct:.2f} {change_str}")
            
            if unknown_callouts_yoy:
                long_term_parts.append("**Unknown Dimensions Callout:**")
                long_term_parts.extend(unknown_callouts_yoy)
        else:
            if is_debug_metric_yoy:
                debug_print(f"[DEBUG YOY] ⚠️  No Overall data and no significant business units")
            if not is_first_long_term_section:
                long_term_parts.append("")  # Add blank line before section header
            header = "**Comparison vs Prev Year**"
            if year_range:
                header += f" ({year_range})"
            long_term_parts.append(header)
            is_first_long_term_section = False
            long_term_parts.append("- No year-over-year data available")
    else:
        if is_debug_metric_yoy:
            debug_print(f"[DEBUG YOY] ⚠️  week_yoy_df is None or empty")
        if not is_first_long_term_section:
            long_term_parts.append("")  # Add blank line before section header
        header = "**Comparison vs Prev Year**"
        if year_range:
            header += f" ({year_range})"
        long_term_parts.append(header)
        is_first_long_term_section = False
        long_term_parts.append("- No year-over-year data available")
    
    # Return both parts as tuple
    anomaly_callout = "<br>".join(anomaly_parts) if anomaly_parts else ""
    long_term_callout = "<br>".join(long_term_parts) if long_term_parts else ""
    return (anomaly_callout, long_term_callout)

# COMMAND ----------

# Generate steering report
print("\n" + "="*80)
print("Generating Steering Report...")
print("="*80)

# Define OUTPUT_BASE_FOLDER before calling build_callout_for_metric so it's available in the function
OUTPUT_BASE_FOLDER = f'{WORKSPACE_FOLDER}/long-term-steering-{latest_week_str if latest_week_str else "unknown"}'

week_num = latest_week_str.split('-W')[1] if latest_week_str else 'XX'
report = f"# {latest_week_str} Weekly Payments Metrics Steering\n\n"

# Add dimension abbreviations legend
report += "### Dimension Abbreviations\n"
report += "| Abbreviation | Full Name |\n"
report += "| :--- | :--- |\n"
for full_name, abbrev in sorted(DIMENSION_ABBREVIATIONS.items()):
    report += f"| {abbrev} | {full_name} |\n"
report += "\n"

report += "## Key Insights\n"
report += generate_key_insights(week_prev_processed, week_yoy_processed, quarter_prev_processed)
report += "\n\n"
report += "| Metrics | Anomaly/Callout | Long Term Impact | Notes |\n"
report += "| :--- | :--- | :--- | :--- |\n"

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
    
    # DEBUG for year-over-year filtering
    if is_debug_metric:
        debug_print(f"[DEBUG YOY FILTERING] Before filtering for {metric_full}:")
        if week_yoy_processed is not None and not week_yoy_processed.empty:
            debug_print(f"[DEBUG YOY FILTERING] week_yoy_processed shape: {week_yoy_processed.shape}")
            debug_print(f"[DEBUG YOY FILTERING] Unique metric_final_name values (first 5):")
            unique_yoy_metrics = week_yoy_processed['metric_final_name'].unique()[:5]
            for um in unique_yoy_metrics:
                print(f"  - {um}")
            metric_exists_yoy = (week_yoy_processed['metric_final_name'] == metric_full).any()
            debug_print(f"[DEBUG YOY FILTERING] Metric exists in week_yoy_processed: {metric_exists_yoy}")
            if metric_exists_yoy:
                matching_yoy = week_yoy_processed[week_yoy_processed['metric_final_name'] == metric_full]
                debug_print(f"[DEBUG YOY FILTERING] Matching rows count: {len(matching_yoy)}")
                debug_print(f"[DEBUG YOY FILTERING] reporting_cluster distribution:")
                print(matching_yoy['reporting_cluster'].value_counts())
        else:
            debug_print(f"[DEBUG YOY FILTERING] week_yoy_processed is None or empty!")
    
    week_yoy_metric = week_yoy_processed[week_yoy_processed['metric_final_name'] == metric_full] if week_yoy_processed is not None and not week_yoy_processed.empty else None
    
    # DEBUG for year-over-year after filtering
    if is_debug_metric:
        debug_print(f"[DEBUG YOY FILTERING] After filtering:")
        if week_yoy_metric is not None and not week_yoy_metric.empty:
            debug_print(f"[DEBUG YOY FILTERING] week_yoy_metric shape: {week_yoy_metric.shape}")
            debug_print(f"[DEBUG YOY FILTERING] reporting_cluster values: {week_yoy_metric['reporting_cluster'].unique()}")
            overall_yoy_check = week_yoy_metric[
                (week_yoy_metric['reporting_cluster'] == 'Overall') & 
                (week_yoy_metric['dimension_name'] == '_Overall')
            ]
            debug_print(f"[DEBUG YOY FILTERING] Overall rows with _Overall dimension: {len(overall_yoy_check)}")
            if not overall_yoy_check.empty:
                debug_print(f"[DEBUG YOY FILTERING] Sample relative_change_pct: {overall_yoy_check.iloc[0]['relative_change_pct']}")
        else:
            debug_print(f"[DEBUG YOY FILTERING] ⚠️  week_yoy_metric is None or empty after filtering!")
    
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
    
    anomaly_callout, long_term_callout = build_callout_for_metric(metric_full, week_prev_metric, week_yoy_metric, quarter_prev_metric, quarter_range_str, year_range_str)
    
    report += f"| **{metric_display}** | {anomaly_callout} | {long_term_callout} | |\n"

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
