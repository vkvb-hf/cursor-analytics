# Databricks notebook source
# MAGIC %md
# MAGIC # Steering Output Generation - Parameterized
# MAGIC 
# MAGIC This notebook generates steering output with multiple comparison types:
# MAGIC - Week-over-week (current_week vs prev_week)
# MAGIC - Year-over-year week (current_week vs prev_yr_week)
# MAGIC - Month-over-month (current_month vs prev_month) - last 4 weeks
# MAGIC - Year-over-year month (current_month vs prev_yr_month) - last 4 weeks
# MAGIC - Quarter-over-quarter (current_quarter vs prev_quarter) - last 13 weeks
# MAGIC - Year-over-year quarter (current_quarter vs prev_yr_quarter) - last 13 weeks

# COMMAND ----------

# Import required libraries
import pyspark.sql.functions as F
from pyspark.sql.types import DoubleType
import math
import os
import errno
import shutil  # For directory removal operations
import pandas as pd  # Explicitly import pandas
from time import time  # For performance tracking

# Modify the path to the workspace folder
WORKSPACE_FOLDER = f'/Workspace/Users/visal.kumar@hellofresh.com'

# Define metrics and constants for reporting
REPORTING_CLUSTERS = ['Overall', 'HF-NA', 'HF-INTL', 'RTE', 'WL']
VALID_REPORTING_CLUSTERS = ['HF-NA', 'HF-INTL', 'RTE', 'WL', 'Overall']

# Comparison configuration
# Set to 'all' to generate all 6 comparisons, or specify individual ones
# Options: 'all', 'week_prev', 'week_yoy', 'month_prev', 'month_yoy', 'quarter_prev', 'quarter_yoy'
COMPARISON_MODES = 'all'  # Options: 'all', ['week_prev', 'week_yoy', 'month_prev', 'month_yoy', 'quarter_prev', 'quarter_yoy']

# List of metrics to generate reports for
STEERING_METRICS = [
    '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess',
    '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 2_SelectToSuccess',
    '1_Activation (Paid + Referrals) - 1_Checkout Funnel (backend) - 1_PaymentPageVisitToSuccess',
    '1_Activation (Paid + Referrals) - 2_Voucher Fraud - 1_Total Duplicate Rate',
    '1_Activation (Paid + Referrals) - 2_Voucher Fraud - 2_Total Duplicate Block Rate',
    '1_Activation (Paid + Referrals) - 3_Payment Fraud - 1_Payment Fraud Block Rate',
    '2_Reactivations - 1_ReactivationFunnel - 1_ReactivationRate',
    '3_Active - 1_1_Overall Total Box Candidates - 2_PreDunningAR',
    '3_Active - 1_2_Loyalty: LL0 (Initial charges) - 2_PreDunningAR',
    '3_Active - 1_3_Loyalty: LL0 and LL1+ (Recurring charges) - 2_PreDunningAR',
    '3_Active - 2_1_Boxes Shipped - 0_ShipRate',
    '3_Active - 2_1_Boxes Shipped - 1_RecoveryW0',
    '3_Active - 2_2_Boxes Shipped - 12wk lag - 2_Recovery_12wkCohort',
    '3_Active - 2_2_Boxes Shipped - 12wk lag - 3_DunningAvgNetProfit_12wkCohort'
]

# COMMAND ----------

# Get the latest complete week and 4-week periods for reporting
start_time = time()
print("Getting latest reporting periods...")

# Get latest complete week
latest_week_query = """
    SELECT
    hellofresh_week
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

# Get latest 4 complete weeks (for "current month" = last 4 weeks)
# This will get the last 4 weeks ending with the latest complete week
latest_4weeks_query = f"""
    SELECT
    COLLECT_LIST(hellofresh_week) AS weeks_list
    FROM (
        SELECT
        hellofresh_week
        FROM dimensions.date_dimension dd
        WHERE
          hellofresh_week >= '2021-W01'
          AND DATE(date_string_backwards) < CURRENT_DATE()
          AND hellofresh_week <= '{latest_week_str if latest_week_str else "2025-W44"}'
        GROUP BY 1
        HAVING COUNT(*)=7
        ORDER BY hellofresh_week DESC
        LIMIT 4
    )
    """
latest_4weeks = spark.sql(latest_4weeks_query)
latest_4weeks_list = latest_4weeks.toPandas().values[0][0] if latest_4weeks.count() > 0 else None
if latest_4weeks_list is not None and len(latest_4weeks_list) > 0:
    latest_4weeks_list = sorted(list(latest_4weeks_list))  # Sort ascending, convert to list
    latest_4weeks_str = f"{latest_4weeks_list[0]}-{latest_4weeks_list[-1]}"  # e.g., "2025-W41-2025-W44"
else:
    latest_4weeks_list = None
    latest_4weeks_str = None

# Get previous 4 weeks (4 weeks before the latest 4 weeks)
prev_4weeks_query = f"""
    SELECT
    COLLECT_LIST(hellofresh_week) AS weeks_list
    FROM (
        SELECT
        hellofresh_week
        FROM dimensions.date_dimension dd
        WHERE
          hellofresh_week >= '2021-W01'
          AND DATE(date_string_backwards) < CURRENT_DATE()
          AND hellofresh_week < '{latest_4weeks_list[0] if latest_4weeks_list else "2025-W41"}'
        GROUP BY 1
        HAVING COUNT(*)=7
        ORDER BY hellofresh_week DESC
        LIMIT 4
    )
    """
prev_4weeks = spark.sql(prev_4weeks_query)
prev_4weeks_list = prev_4weeks.toPandas().values[0][0] if prev_4weeks.count() > 0 else None
if prev_4weeks_list is not None and len(prev_4weeks_list) > 0:
    prev_4weeks_list = sorted(list(prev_4weeks_list))
    prev_4weeks_str = f"{prev_4weeks_list[0]}-{prev_4weeks_list[-1]}"
else:
    prev_4weeks_list = None
    prev_4weeks_str = None

# Get previous year 4 weeks (same weeks from last year)
prev_yr_4weeks_list = None
prev_yr_4weeks_str = None
if latest_4weeks_list:
    # Extract week numbers from current 4 weeks
    week_numbers = [int(w.split('-W')[1]) for w in latest_4weeks_list]
    year = int(latest_4weeks_list[0].split('-W')[0])
    prev_year = year - 1
    
    # Build previous year weeks
    prev_yr_weeks = [f"{prev_year}-W{wn:02d}" for wn in week_numbers]
    
    # Verify these weeks exist in the date dimension
    prev_yr_weeks_str = ','.join([f"'{w}'" for w in prev_yr_weeks])
    prev_yr_4weeks_query = f"""
        SELECT
        COLLECT_LIST(hellofresh_week) AS weeks_list
        FROM (
            SELECT hellofresh_week
            FROM dimensions.date_dimension dd
            WHERE hellofresh_week IN ({prev_yr_weeks_str})
            GROUP BY 1
            HAVING COUNT(*)=7
            ORDER BY hellofresh_week
        )
        """
    prev_yr_4weeks = spark.sql(prev_yr_4weeks_query)
    prev_yr_4weeks_list = prev_yr_4weeks.toPandas().values[0][0] if prev_yr_4weeks.count() > 0 else None
    if prev_yr_4weeks_list is not None and len(prev_yr_4weeks_list) > 0:
        prev_yr_4weeks_list = sorted(list(prev_yr_4weeks_list))
        prev_yr_4weeks_str = f"{prev_yr_4weeks_list[0]}-{prev_yr_4weeks_list[-1]}"
    else:
        prev_yr_4weeks_list = None
        prev_yr_4weeks_str = None

# Get latest 13 complete weeks (for "current quarter" = last 13 weeks)
latest_13weeks_query = f"""
    SELECT
    COLLECT_LIST(hellofresh_week) AS weeks_list
    FROM (
        SELECT
        hellofresh_week
        FROM dimensions.date_dimension dd
        WHERE
          hellofresh_week >= '2021-W01'
          AND DATE(date_string_backwards) < CURRENT_DATE()
          AND hellofresh_week <= '{latest_week_str if latest_week_str else "2025-W44"}'
        GROUP BY 1
        HAVING COUNT(*)=7
        ORDER BY hellofresh_week DESC
        LIMIT 13
    )
    """
latest_13weeks = spark.sql(latest_13weeks_query)
latest_13weeks_list = latest_13weeks.toPandas().values[0][0] if latest_13weeks.count() > 0 else None
if latest_13weeks_list is not None and len(latest_13weeks_list) > 0:
    latest_13weeks_list = sorted(list(latest_13weeks_list))  # Sort ascending, convert to list
    latest_13weeks_str = f"{latest_13weeks_list[0]}-{latest_13weeks_list[-1]}"  # e.g., "2025-W32-2025-W44"
else:
    latest_13weeks_list = None
    latest_13weeks_str = None

# Get previous 13 weeks (13 weeks before the latest 13 weeks)
prev_13weeks_query = f"""
    SELECT
    COLLECT_LIST(hellofresh_week) AS weeks_list
    FROM (
        SELECT
        hellofresh_week
        FROM dimensions.date_dimension dd
        WHERE
          hellofresh_week >= '2021-W01'
          AND DATE(date_string_backwards) < CURRENT_DATE()
          AND hellofresh_week < '{latest_13weeks_list[0] if latest_13weeks_list else "2025-W32"}'
        GROUP BY 1
        HAVING COUNT(*)=7
        ORDER BY hellofresh_week DESC
        LIMIT 13
    )
    """
prev_13weeks = spark.sql(prev_13weeks_query)
prev_13weeks_list = prev_13weeks.toPandas().values[0][0] if prev_13weeks.count() > 0 else None
if prev_13weeks_list is not None and len(prev_13weeks_list) > 0:
    prev_13weeks_list = sorted(list(prev_13weeks_list))
    prev_13weeks_str = f"{prev_13weeks_list[0]}-{prev_13weeks_list[-1]}"
else:
    prev_13weeks_list = None
    prev_13weeks_str = None

# Get previous year 13 weeks (same weeks from last year)
prev_yr_13weeks_list = None
prev_yr_13weeks_str = None
if latest_13weeks_list:
    # Extract week numbers from current 13 weeks
    week_numbers = [int(w.split('-W')[1]) for w in latest_13weeks_list]
    year = int(latest_13weeks_list[0].split('-W')[0])
    prev_year = year - 1
    
    # Build previous year weeks
    prev_yr_weeks = [f"{prev_year}-W{wn:02d}" for wn in week_numbers]
    
    # Verify these weeks exist in the date dimension
    prev_yr_weeks_str = ','.join([f"'{w}'" for w in prev_yr_weeks])
    prev_yr_13weeks_query = f"""
        SELECT
        COLLECT_LIST(hellofresh_week) AS weeks_list
        FROM (
            SELECT hellofresh_week
            FROM dimensions.date_dimension dd
            WHERE hellofresh_week IN ({prev_yr_weeks_str})
            GROUP BY 1
            HAVING COUNT(*)=7
            ORDER BY hellofresh_week
        )
        """
    prev_yr_13weeks = spark.sql(prev_yr_13weeks_query)
    prev_yr_13weeks_list = prev_yr_13weeks.toPandas().values[0][0] if prev_yr_13weeks.count() > 0 else None
    if prev_yr_13weeks_list is not None and len(prev_yr_13weeks_list) > 0:
        prev_yr_13weeks_list = sorted(list(prev_yr_13weeks_list))
        prev_yr_13weeks_str = f"{prev_yr_13weeks_list[0]}-{prev_yr_13weeks_list[-1]}"
    else:
        prev_yr_13weeks_list = None
        prev_yr_13weeks_str = None

print(f"Latest reporting week: {latest_week_str}")
print(f"Latest 4 weeks (current month): {latest_4weeks_str} ({latest_4weeks_list})")
print(f"Previous 4 weeks (prev month): {prev_4weeks_str} ({prev_4weeks_list})")
print(f"Previous year 4 weeks (prev yr month): {prev_yr_4weeks_str} ({prev_yr_4weeks_list})")
print(f"Latest 13 weeks (current quarter): {latest_13weeks_str} ({latest_13weeks_list})")
print(f"Previous 13 weeks (prev quarter): {prev_13weeks_str} ({prev_13weeks_list})")
print(f"Previous year 13 weeks (prev yr quarter): {prev_yr_13weeks_str} ({prev_yr_13weeks_list})")
print(f"Time to get latest dates: {time() - start_time:.2f} seconds")

# Output directory path
OUTPUT_BASE_FOLDER = f'{WORKSPACE_FOLDER}/steering-parametrized-{latest_week_str if latest_week_str else latest_4weeks_str}'
print(f"Reports will be saved to: {OUTPUT_BASE_FOLDER}")

# COMMAND ----------

# Refresh table data to ensure we have the latest metrics
print("Refreshing tables...")
start_time = time()
spark.sql("REFRESH TABLE payments_hf.payments_p0_metrics")

# Define metrics to exclude from analysis
EXCLUDED_METRICS = [
    '5_DunningBadDebtRate_12wkCohort',
    '6_TotalBadDebtRate_12wkCohort',
    '3_PaymentProcessingFees%',
    '1_ChargeBackRate', 
    '3_PostDunningAR'
]

# Metrics that require special dimension handling
SPECIAL_METRICS = ['0_ShipRate', '1_RecoveryW0', '2_Recovery_12wkCohort', '3_DunningAvgNetProfit_12wkCohort']

# Excluded dimensions
EXCLUDED_DIMENSIONS = ['LoyaltySegment', 'PaymentMethod_OrderType']

# COMMAND ----------

# Function to build metrics query for a specific comparison mode
def build_metrics_query(date_granularity, comparison_type, date_value_str, weeks_list=None):
    """
    Build metrics query for a specific comparison type.
    
    Parameters:
    -----------
    date_granularity : str
        'WEEK', '4WEEKS', or '13WEEKS'
    comparison_type : str
        'prev_period' or 'prev_year'
    date_value_str : str
        The date value to filter on (e.g., '2025-W44' or '2025-W41-2025-W44')
    weeks_list : list, optional
        List of week strings for multi-week aggregation (e.g., ['2025-W41', '2025-W42', '2025-W43', '2025-W44'] for 4 weeks, or 13 weeks for quarter)
    
    Returns:
    --------
    str
        SQL query string
    """
    # Determine which previous columns to use
    if comparison_type == 'prev_period':
        prev_num_col = 'prev_metric_value_numerator'
        prev_den_col = 'prev_metric_value_denominator'
        comparison_label = 'vs Previous Period'
    elif comparison_type == 'prev_year':
        prev_num_col = 'prev_yr_metric_value_numerator'
        prev_den_col = 'prev_yr_metric_value_denominator'
        comparison_label = 'vs Previous Year'
    elif comparison_type == 'current':
        # For 4-week aggregation, we'll use current columns
        prev_num_col = 'current_metric_value_numerator'  # Will be renamed later
        prev_den_col = 'current_metric_value_denominator'
        comparison_label = 'Current'  # Placeholder
    else:
        raise ValueError(f"Invalid comparison_type: {comparison_type}")
    
    # Handle multi-week aggregation vs single week
    if date_granularity in ['4WEEKS', '13WEEKS'] and weeks_list:
        # For 4-week periods, we need to aggregate across multiple weeks
        # We'll query WEEK granularity and sum across the weeks
        weeks_list_str = ','.join([f"'{w}'" for w in weeks_list])
        date_filter = f"date_value IN ({weeks_list_str})"
        date_value_display = date_value_str
        # For 4-week aggregation, we sum current_metric_value across weeks
        # The prev columns will be handled separately
        if comparison_type == 'current':
            prev_num_col = 'current_metric_value_numerator'
            prev_den_col = 'current_metric_value_denominator'
    else:
        # Single week
        date_filter = f"date_value = '{date_value_str}'"
        date_value_display = date_value_str
    
    # For multi-week periods, we need to exclude date_value from GROUP BY since we're aggregating across weeks
    if date_granularity in ['4WEEKS', '13WEEKS'] and weeks_list:
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
        group_by_clause = "GROUP BY ALL"
        group_by_clause_bu = "GROUP BY ALL"
    
    # For 'current' comparison type, we only need current columns (no prev columns)
    if comparison_type == 'current':
        prev_cols_select = ""
    else:
        prev_cols_select = f""",
    SUM(a.{prev_num_col}) AS prev_metric_value_numerator,
    SUM(a.{prev_den_col}) AS prev_metric_value_denominator"""
    
    metrics_query = f"""
    -- Query for {date_granularity} granularity, {comparison_label}
    SELECT 
    '{date_value_display}' as date_value,
    '{date_granularity}' as date_granularity,
    '{comparison_type}' as comparison_type,
    '{comparison_label}' as comparison_label,
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
    '{comparison_label}' as comparison_label,
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

# COMMAND ----------

# Function to calculate z-score for statistical significance testing
@F.udf(returnType=DoubleType())
def calculate_z_score(n1, d1, n2, d2, metric_type='proportion'):
    """
    Calculate z-score for difference between two proportions or averages
    """
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

# COMMAND ----------

# Define significance levels
SIGNIFICANCE_LEVELS = [
    (6.361, 7.0, 99.99999),
    (5.612, 6.0, 99.9999),
    (4.892, 5.0, 99.999),
    (4.265, 4.0, 99.99),
    (3.719, 3.5, 99.95),
    (3.291, 3.0, 99.9),
    (3.090, 2.8, 99.8),
    (2.807, 2.5, 99.5),
    (2.576, 2.0, 99.0),
    (2.326, 1.8, 98.0),
    (2.054, 1.6, 96.0),
    (1.96, 1.5, 95.0),
    (1.645, 1.0, 90.0)
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

# COMMAND ----------

# Function to process metrics data for a specific comparison
def process_comparison_data(data_df, comparison_label):
    """
    Process metrics data and calculate significance, changes, and impact.
    
    Parameters:
    -----------
    data_df : pyspark.sql.DataFrame
        Raw metrics data
    comparison_label : str
        Label for this comparison (e.g., "Week vs Previous Week")
    
    Returns:
    --------
    pandas.DataFrame
        Processed metrics with all calculated fields
    """
    print(f"Processing {comparison_label}...")
    start_time = time()
    
    significance_case = build_significance_case("z_score")
    
    processed_df = (
        data_df
        # Calculate current and previous ratios (keep original columns for volume calculations)
        .withColumn("current_ratio", 
                    F.when(F.col("current_metric_value_denominator") > 0,
                           F.col("current_metric_value_numerator") / F.col("current_metric_value_denominator"))
                    .otherwise(0))
        .withColumn("prev_ratio", 
                    F.when(F.col("prev_metric_value_denominator") > 0,
                           F.col("prev_metric_value_numerator") / F.col("prev_metric_value_denominator"))
                    .otherwise(0))
        
        # Calculate z-score
        .withColumn("z_score", 
                    calculate_z_score(
                        F.col("current_metric_value_numerator"),
                        F.col("current_metric_value_denominator"),
                        F.col("prev_metric_value_numerator"),
                        F.col("prev_metric_value_denominator"),
                        F.col("metric_type")
                    ))
        
        # Apply significance level
        .withColumn("significance_level", significance_case)
        
        # Calculate changes
        .withColumn("absolute_change", F.col("current_ratio") - F.col("prev_ratio"))
        .withColumn("relative_change_pct", 
                    F.when(F.col("prev_ratio") > 0,
                           (F.col("absolute_change") / F.col("prev_ratio")) * 100)
                    .otherwise(0))

        # Determine business impact
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
    
    # Convert to Pandas
    result_df = processed_df.toPandas()
    bu_level_count = len(result_df[result_df['reporting_cluster'] == 'bu_level']) if 'reporting_cluster' in result_df.columns else 0
    print(f"  Processed {len(result_df)} rows in {time() - start_time:.2f} seconds ({bu_level_count} bu_level rows)")
    
    return result_df

# COMMAND ----------

# Determine which comparisons to run
# For month comparisons, we use 4-week periods
# For quarter comparisons, we use 13-week periods
if COMPARISON_MODES == 'all':
    comparisons_to_run = [
        ('WEEK', 'prev_period', latest_week_str, 'week_prev', None, None),
        ('WEEK', 'prev_year', latest_week_str, 'week_yoy', None, None),
        ('4WEEKS', 'prev_period', latest_4weeks_str, 'month_prev', latest_4weeks_list, prev_4weeks_list),
        ('4WEEKS', 'prev_year', latest_4weeks_str, 'month_yoy', latest_4weeks_list, prev_yr_4weeks_list),
        ('13WEEKS', 'prev_period', latest_13weeks_str, 'quarter_prev', latest_13weeks_list, prev_13weeks_list),
        ('13WEEKS', 'prev_year', latest_13weeks_str, 'quarter_yoy', latest_13weeks_list, prev_yr_13weeks_list)
    ]
else:
    comparisons_to_run = []
    if isinstance(COMPARISON_MODES, str):
        COMPARISON_MODES = [COMPARISON_MODES]
    
    if 'week_prev' in COMPARISON_MODES and latest_week_str:
        comparisons_to_run.append(('WEEK', 'prev_period', latest_week_str, 'week_prev', None, None))
    if 'week_yoy' in COMPARISON_MODES and latest_week_str:
        comparisons_to_run.append(('WEEK', 'prev_year', latest_week_str, 'week_yoy', None, None))
    if 'month_prev' in COMPARISON_MODES and latest_4weeks_str and prev_4weeks_list:
        comparisons_to_run.append(('4WEEKS', 'prev_period', latest_4weeks_str, 'month_prev', latest_4weeks_list, prev_4weeks_list))
    if 'month_yoy' in COMPARISON_MODES and latest_4weeks_str and prev_yr_4weeks_list:
        comparisons_to_run.append(('4WEEKS', 'prev_year', latest_4weeks_str, 'month_yoy', latest_4weeks_list, prev_yr_4weeks_list))
    if 'quarter_prev' in COMPARISON_MODES and latest_13weeks_str and prev_13weeks_list:
        comparisons_to_run.append(('13WEEKS', 'prev_period', latest_13weeks_str, 'quarter_prev', latest_13weeks_list, prev_13weeks_list))
    if 'quarter_yoy' in COMPARISON_MODES and latest_13weeks_str and prev_yr_13weeks_list:
        comparisons_to_run.append(('13WEEKS', 'prev_year', latest_13weeks_str, 'quarter_yoy', latest_13weeks_list, prev_yr_13weeks_list))

print(f"\nRunning {len(comparisons_to_run)} comparison(s):")
for gran, comp_type, date_val, mode, curr_weeks, prev_weeks in comparisons_to_run:
    print(f"  - {gran} {comp_type} ({mode}) for {date_val}")

# Process each comparison
all_comparison_data = {}
for date_granularity, comparison_type, date_value_str, mode_key, current_weeks_list, prev_weeks_list in comparisons_to_run:
    if not date_value_str:
        print(f"  Skipping {mode_key} - no date value available")
        continue
    
    print(f"\n{'='*80}")
    print(f"Processing: {date_granularity} - {comparison_type}")
    print(f"{'='*80}")
    
    # For multi-week periods (4 or 13 weeks), we need to aggregate current and previous weeks separately
    if date_granularity in ['4WEEKS', '13WEEKS'] and current_weeks_list and prev_weeks_list:
        # For 4-week comparisons:
        # - Current period: aggregate current_metric_value across current 4 weeks
        # - Previous period: aggregate current_metric_value across previous 4 weeks (for prev_period)
        # - Previous year: aggregate prev_yr_metric_value across current 4 weeks (for prev_year)
        
        if comparison_type == 'prev_period':
            # Query current weeks (current period)
            query_current = build_metrics_query(date_granularity, 'current', date_value_str, current_weeks_list)
            data_current = spark.sql(query_current)
            
            # Query previous weeks (previous period) - use their current values
            query_prev = build_metrics_query(date_granularity, 'current', prev_weeks_list[0] + '-' + prev_weeks_list[-1], prev_weeks_list)
            data_prev = spark.sql(query_prev)
            print(f"  Prev {len(prev_weeks_list)} weeks query returned {data_prev.count()} rows")
            
            # Drop any existing prev columns from data_prev (they might exist from the query)
            prev_cols_to_drop = [c for c in data_prev.columns if c.startswith('prev_metric_value')]
            if prev_cols_to_drop:
                data_prev = data_prev.select([c for c in data_prev.columns if c not in prev_cols_to_drop])
            
            # Rename columns in prev data to be the "previous" values
            data_prev = data_prev.withColumnRenamed("current_metric_value_numerator", "prev_metric_value_numerator")
            data_prev = data_prev.withColumnRenamed("current_metric_value_denominator", "prev_metric_value_denominator")
            
            print(f"  Current {len(current_weeks_list)} weeks query returned {data_current.count()} rows")
            
            # Debug: Check if bu_level rows exist in query results
            current_bu_in_query = data_current.filter(F.col('reporting_cluster') == 'bu_level').count()
            prev_bu_in_query = data_prev.filter(F.col('reporting_cluster') == 'bu_level').count()
            print(f"  DEBUG: bu_level rows in query results - current: {current_bu_in_query}, prev: {prev_bu_in_query}")
            
            # Join and combine
            # The query returns both 'Overall' and 'bu_level' reporting_cluster
            # We need to join them separately and then union
            
            join_cols = ['reporting_cluster', 'business_unit', 'metric_final_name', 'dimension_name', 'dimension_value', 
                         'flag_more_is_good', 'flag_is_p0', 'metric_type']
            
            # Process 'Overall' reporting_cluster
            data_current_overall = data_current.filter(F.col('reporting_cluster') == 'Overall')
            data_prev_overall = data_prev.filter(F.col('reporting_cluster') == 'Overall')
            
            print(f"  DEBUG: data_current_overall columns: {data_current_overall.columns}")
            print(f"  DEBUG: data_prev_overall columns: {data_prev_overall.columns}")
            print(f"  DEBUG: data_current_overall count: {data_current_overall.count()}")
            print(f"  DEBUG: data_prev_overall count: {data_prev_overall.count()}")
            
            # Debug: Check a sample row from data_prev_overall to see if rename worked
            if data_prev_overall.count() > 0:
                sample_prev = data_prev_overall.limit(1).toPandas()
                if len(sample_prev) > 0:
                    print(f"  DEBUG: Sample prev row columns: {list(sample_prev.columns)}")
                    if 'prev_metric_value_numerator' in sample_prev.columns:
                        print(f"  DEBUG: prev_metric_value_numerator value: {sample_prev['prev_metric_value_numerator'].iloc[0]}")
                    if 'prev_metric_value_denominator' in sample_prev.columns:
                        print(f"  DEBUG: prev_metric_value_denominator value: {sample_prev['prev_metric_value_denominator'].iloc[0]}")
            
            # Select only the columns we need from data_current (excluding any prev columns)
            data_current_cols = [c for c in data_current_overall.columns if c not in ['prev_metric_value_numerator', 'prev_metric_value_denominator']]
            data_current_clean = data_current_overall.select(data_current_cols)
            
            print(f"  DEBUG: data_current_clean columns: {data_current_clean.columns}")
            
            # Select only needed columns from data_prev
            # First verify the columns exist
            print(f"  DEBUG: Checking if prev columns exist in data_prev_overall...")
            if 'prev_metric_value_numerator' not in data_prev_overall.columns:
                print(f"  ⚠️  ERROR: prev_metric_value_numerator not found in data_prev_overall.columns!")
                print(f"     Available columns: {data_prev_overall.columns}")
            if 'prev_metric_value_denominator' not in data_prev_overall.columns:
                print(f"  ⚠️  ERROR: prev_metric_value_denominator not found in data_prev_overall.columns!")
                print(f"     Available columns: {data_prev_overall.columns}")
            
            # Build select list - ensure all columns exist
            select_list = []
            for c in join_cols:
                if c in data_prev_overall.columns:
                    select_list.append(F.col(c))
                else:
                    print(f"  ⚠️  WARNING: Join column '{c}' not found in data_prev_overall.columns!")
            
            if 'prev_metric_value_numerator' in data_prev_overall.columns:
                select_list.append(F.col('prev_metric_value_numerator'))
            if 'prev_metric_value_denominator' in data_prev_overall.columns:
                select_list.append(F.col('prev_metric_value_denominator'))
            
            data_prev_selected = data_prev_overall.select(select_list)
            
            print(f"  DEBUG: data_prev_selected columns: {data_prev_selected.columns}")
            
            # Debug: Check sample from data_prev_selected
            if data_prev_selected.count() > 0:
                sample_prev_selected = data_prev_selected.limit(1).toPandas()
                if len(sample_prev_selected) > 0:
                    if 'prev_metric_value_numerator' in sample_prev_selected.columns:
                        print(f"  DEBUG: Sample prev_selected prev_metric_value_numerator: {sample_prev_selected['prev_metric_value_numerator'].iloc[0]}")
                    if 'prev_metric_value_denominator' in sample_prev_selected.columns:
                        print(f"  DEBUG: Sample prev_selected prev_metric_value_denominator: {sample_prev_selected['prev_metric_value_denominator'].iloc[0]}")
                    print(f"  DEBUG: Sample prev_selected join keys: {dict(sample_prev_selected[join_cols].iloc[0]) if all(c in sample_prev_selected.columns for c in join_cols) else 'N/A'}")
            
            # Join Overall data
            # Ensure both DataFrames have the same schema for join keys
            # Cast dimension_value to string to handle None consistently
            data_current_clean = data_current_clean.withColumn(
                'dimension_value', 
                F.when(F.col('dimension_value').isNull(), F.lit('None')).otherwise(F.col('dimension_value').cast('string'))
            )
            data_prev_selected = data_prev_selected.withColumn(
                'dimension_value',
                F.when(F.col('dimension_value').isNull(), F.lit('None')).otherwise(F.col('dimension_value').cast('string'))
            )
            
            # Also ensure other string columns are consistent
            for col in ['reporting_cluster', 'business_unit', 'metric_final_name', 'dimension_name', 'flag_more_is_good', 'flag_is_p0', 'metric_type']:
                if col in data_current_clean.columns and col in data_prev_selected.columns:
                    data_current_clean = data_current_clean.withColumn(col, F.col(col).cast('string'))
                    data_prev_selected = data_prev_selected.withColumn(col, F.col(col).cast('string'))
            
            # Perform the join
            data_overall = data_current_clean.join(
                data_prev_selected,
                on=join_cols,
                how='left'
            )
            
            print(f"  DEBUG: data_overall columns after join: {data_overall.columns}")
            
            # Debug: Check if join worked by looking at a specific metric
            test_metric_name = '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
            test_row = data_overall.filter(
                (F.col('reporting_cluster') == 'Overall') & 
                (F.col('metric_final_name') == test_metric_name) &
                (F.col('dimension_name') == '_Overall')
            )
            if test_row.count() > 0:
                test_pd = test_row.limit(1).toPandas()
                if len(test_pd) > 0:
                    row = test_pd.iloc[0]
                    prev_num = row.get('prev_metric_value_numerator', None)
                    prev_den = row.get('prev_metric_value_denominator', None)
                    print(f"  DEBUG: After join - test metric prev values:")
                    print(f"    prev_metric_value_numerator: {prev_num}")
                    print(f"    prev_metric_value_denominator: {prev_den}")
                    if prev_den and prev_den > 0:
                        prev_ratio = (prev_num / prev_den * 100) if prev_num else 0
                        print(f"    prev_ratio: {prev_ratio:.2f}%")
                    else:
                        print(f"    ⚠️  WARNING: prev_den is {prev_den} - join might have failed!")
            else:
                print(f"  DEBUG: ⚠️  WARNING: Test metric not found after join!")
            
            # Process 'bu_level' reporting_cluster
            data_current_bu = data_current.filter(F.col('reporting_cluster') == 'bu_level')
            data_prev_bu = data_prev.filter(F.col('reporting_cluster') == 'bu_level')
            
            current_bu_count = data_current_bu.count()
            prev_bu_count = data_prev_bu.count()
            print(f"  DEBUG: bu_level rows - current: {current_bu_count}, prev: {prev_bu_count}")
            
            if current_bu_count > 0 and prev_bu_count > 0:
                # Cast dimension_value to string for bu_level data as well
                data_current_bu = data_current_bu.withColumn(
                    'dimension_value', 
                    F.when(F.col('dimension_value').isNull(), F.lit('None')).otherwise(F.col('dimension_value').cast('string'))
                )
                data_prev_bu = data_prev_bu.withColumn(
                    'dimension_value',
                    F.when(F.col('dimension_value').isNull(), F.lit('None')).otherwise(F.col('dimension_value').cast('string'))
                )
                
                # Also ensure other string columns are consistent
                for col in ['reporting_cluster', 'business_unit', 'metric_final_name', 'dimension_name', 'flag_more_is_good', 'flag_is_p0', 'metric_type']:
                    if col in data_current_bu.columns and col in data_prev_bu.columns:
                        data_current_bu = data_current_bu.withColumn(col, F.col(col).cast('string'))
                        data_prev_bu = data_prev_bu.withColumn(col, F.col(col).cast('string'))
                
                data_current_bu_cols = [c for c in data_current_bu.columns if c not in ['prev_metric_value_numerator', 'prev_metric_value_denominator']]
                data_current_bu_clean = data_current_bu.select(data_current_bu_cols)
                
                # Build select list for bu_level prev data
                select_list_bu = []
                for c in join_cols:
                    if c in data_prev_bu.columns:
                        select_list_bu.append(F.col(c))
                
                if 'prev_metric_value_numerator' in data_prev_bu.columns:
                    select_list_bu.append(F.col('prev_metric_value_numerator'))
                if 'prev_metric_value_denominator' in data_prev_bu.columns:
                    select_list_bu.append(F.col('prev_metric_value_denominator'))
                
                data_prev_bu_selected = data_prev_bu.select(select_list_bu)
                
                # Join bu_level data
                data_bu = data_current_bu_clean.join(
                    data_prev_bu_selected,
                    on=join_cols,
                    how='left'
                )
                
                # Debug: Check join results
                bu_joined_count = data_bu.count()
                bu_matched_count = data_bu.filter(F.col('prev_metric_value_numerator').isNotNull()).count()
                print(f"  DEBUG: bu_level join - total: {bu_joined_count}, matched: {bu_matched_count}")
                
                # Union Overall and bu_level data - ensure same schema
                # Get all columns from data_overall
                all_cols = data_overall.columns
                # Select same columns from data_bu (fill missing with null)
                data_bu_cols = []
                for col in all_cols:
                    if col in data_bu.columns:
                        data_bu_cols.append(F.col(col))
                    else:
                        data_bu_cols.append(F.lit(None).alias(col))
                data_bu_aligned = data_bu.select(data_bu_cols)
                
                data = data_overall.unionByName(data_bu_aligned)
                bu_after_union = data.filter(F.col('reporting_cluster') == 'bu_level').count()
                bu_with_prev = data.filter((F.col('reporting_cluster') == 'bu_level') & F.col('prev_metric_value_numerator').isNotNull()).count()
                print(f"  Combined Overall and bu_level data: {data.count()} total rows ({bu_after_union} bu_level rows, {bu_with_prev} with prev values)")
                
                # Debug: Check a sample bu_level row
                if bu_after_union > 0:
                    sample_bu = data.filter(F.col('reporting_cluster') == 'bu_level').limit(1).toPandas()
                    if len(sample_bu) > 0:
                        row = sample_bu.iloc[0]
                        print(f"  Sample bu_level row: BU={row.get('business_unit')}, metric={row.get('metric_final_name', '')[:50]}, has_prev={pd.notna(row.get('prev_metric_value_numerator'))}")
            else:
                data = data_overall
                print(f"  Using only Overall data (no bu_level data found): {data.count()} total rows")
                if current_bu_count == 0:
                    print(f"  ⚠️  WARNING: No bu_level rows in current data!")
                if prev_bu_count == 0:
                    print(f"  ⚠️  WARNING: No bu_level rows in prev data!")
            
            # Check join results BEFORE fillna
            matched_count_before = data.filter(F.col('prev_metric_value_numerator').isNotNull()).count()
            print(f"  After join (before fillna): {data.count()} total rows, {matched_count_before} with prev values")
            
            # Debug: Check a specific metric before fillna
            if matched_count_before > 0:
                test_metric_name = '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
                test_row = data.filter(
                    (F.col('reporting_cluster') == 'Overall') & 
                    (F.col('metric_final_name') == test_metric_name) &
                    (F.col('dimension_name') == '_Overall')
                )
                if test_row.count() > 0:
                    test_pd = test_row.limit(1).toPandas()
                    if len(test_pd) > 0:
                        row = test_pd.iloc[0]
                        prev_num = row.get('prev_metric_value_numerator', None)
                        prev_den = row.get('prev_metric_value_denominator', None)
                        print(f"  Sample metric before fillna:")
                        print(f"    prev_metric_value_numerator: {prev_num}")
                        print(f"    prev_metric_value_denominator: {prev_den}")
            
            # If no matches, try to see why
            if matched_count_before == 0:
                print(f"  ⚠️  WARNING: No matches found in join!")
                print(f"     Current Overall rows: {data_current_clean.count()}")
                print(f"     Prev Overall rows: {data_prev_selected.count()}")
                # Check for common metrics
                if data_current_clean.count() > 0:
                    current_metrics = data_current_clean.select('metric_final_name').distinct().toPandas()['metric_final_name'].tolist()[:5]
                    print(f"     Sample current metrics: {current_metrics}")
                if data_prev_selected.count() > 0:
                    prev_metrics = data_prev_selected.select('metric_final_name').distinct().toPandas()['metric_final_name'].tolist()[:5]
                    print(f"     Sample prev metrics: {prev_metrics}")
            else:
                # Only fill nulls for rows that don't have prev values (don't overwrite existing values)
                # Actually, fillna should only affect null values, not existing ones
                # But let's be more careful - only fill nulls, not zeros
                data = data.fillna(0, subset=['prev_metric_value_numerator', 'prev_metric_value_denominator'])
                
                # Debug: Check the same metric after fillna
                test_metric_name = '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
                test_row = data.filter(
                    (F.col('reporting_cluster') == 'Overall') & 
                    (F.col('metric_final_name') == test_metric_name) &
                    (F.col('dimension_name') == '_Overall')
                )
                if test_row.count() > 0:
                    test_pd = test_row.limit(1).toPandas()
                    if len(test_pd) > 0:
                        row = test_pd.iloc[0]
                        prev_num = row.get('prev_metric_value_numerator', None)
                        prev_den = row.get('prev_metric_value_denominator', None)
                        print(f"  Sample metric after fillna:")
                        print(f"    prev_metric_value_numerator: {prev_num}")
                        print(f"    prev_metric_value_denominator: {prev_den}")
                        if prev_den and prev_den > 0:
                            prev_ratio = (prev_num / prev_den * 100) if prev_num else 0
                            print(f"    prev_ratio: {prev_ratio:.2f}%")
            
            # Update the comparison label
            data = data.withColumn("comparison_label", F.lit("vs Previous Period"))
            data = data.withColumn("comparison_type", F.lit('prev_period'))
            
        elif comparison_type == 'prev_year':
            # For year-over-year, we use prev_yr columns from the current weeks
            # Query current weeks with prev_yr columns
            query = build_metrics_query(date_granularity, 'prev_year', date_value_str, current_weeks_list)
            data = spark.sql(query)
        else:
            raise ValueError(f"Invalid comparison_type for {date_granularity}: {comparison_type}")
        
    else:
        # Single week comparison - use existing logic
        query = build_metrics_query(date_granularity, comparison_type, date_value_str)
        data = spark.sql(query)
    
    print(f"Fetched {data.count()} rows")
    
    # Process the data
    processed_data = process_comparison_data(data, f"{date_granularity} {comparison_type}")
    
    # Store for later use
    # Create appropriate label
    if date_granularity == '4WEEKS':
        if comparison_type == 'prev_period':
            label = f"4-Week Period vs Previous 4-Week Period"
        else:
            label = f"4-Week Period vs Previous Year 4-Week Period"
    elif date_granularity == '13WEEKS':
        if comparison_type == 'prev_period':
            label = f"13-Week Period vs Previous 13-Week Period"
        else:
            label = f"13-Week Period vs Previous Year 13-Week Period"
    else:
        label = processed_data['comparison_label'].iloc[0] if len(processed_data) > 0 else f"{date_granularity} {comparison_type}"
    
    # Store weeks information for display
    current_weeks_display = None
    prev_weeks_display = None
    
    if date_granularity == 'WEEK':
        # Single week
        current_weeks_display = date_value_str
        if comparison_type == 'prev_period':
            # Get previous week by querying the date dimension
            prev_week_query = f"""
                SELECT hellofresh_week
                FROM dimensions.date_dimension dd
                WHERE
                  hellofresh_week >= '2021-W01'
                  AND DATE(date_string_backwards) < CURRENT_DATE()
                  AND hellofresh_week < '{date_value_str}'
                GROUP BY 1
                HAVING COUNT(*)=7
                ORDER BY hellofresh_week DESC
                LIMIT 1
            """
            prev_week_df = spark.sql(prev_week_query)
            if prev_week_df.count() > 0:
                prev_weeks_display = prev_week_df.toPandas().values[0][0]
        elif comparison_type == 'prev_year':
            # Previous year same week
            year = int(date_value_str.split('-W')[0])
            week_num = date_value_str.split('-W')[1]
            prev_weeks_display = f"{year-1}-W{week_num}"
    elif date_granularity in ['4WEEKS', '13WEEKS']:
        # Multi-week periods
        if current_weeks_list:
            current_weeks_display = ', '.join(current_weeks_list)
        if comparison_type == 'prev_period' and prev_weeks_list:
            prev_weeks_display = ', '.join(prev_weeks_list)
        elif comparison_type == 'prev_year':
            # For YoY, calculate previous year weeks
            if current_weeks_list:
                prev_yr_weeks = []
                for w in current_weeks_list:
                    year = int(w.split('-W')[0])
                    week_num = w.split('-W')[1]
                    prev_yr_weeks.append(f"{year-1}-W{week_num}")
                prev_weeks_display = ', '.join(prev_yr_weeks)
    
    all_comparison_data[mode_key] = {
        'data': processed_data,
        'date_granularity': date_granularity,
        'comparison_type': comparison_type,
        'date_value': date_value_str,
        'label': label,
        'current_weeks': current_weeks_display,
        'prev_weeks': prev_weeks_display
    }

print(f"\n✅ Processed {len(all_comparison_data)} comparison(s)")

# COMMAND ----------

# Fetch business unit to reporting cluster mapping
print("\nLoading business unit mappings...")
start_time = time()
spark.sql("REFRESH TABLE payments_hf.business_units")

country_mapping_query = """
    SELECT
      business_unit,
      explode(reporting_cluster_array) AS reporting_cluster
    FROM payments_hf.business_units
"""
country_mapping = spark.sql(country_mapping_query)
country_mapping_df = country_mapping.toPandas()

# Ensure business_unit and reporting_cluster are strings and clean
if not country_mapping_df.empty:
    country_mapping_df['business_unit'] = country_mapping_df['business_unit'].astype(str).str.strip()
    country_mapping_df['reporting_cluster'] = country_mapping_df['reporting_cluster'].astype(str).str.strip()
    
    # Filter to only include valid reporting clusters
    print(f"Loaded {len(country_mapping_df)} business unit mappings (before filtering)")
    print(f"All reporting clusters in table: {country_mapping_df['reporting_cluster'].unique().tolist()}")
    
    # Filter to only valid clusters
    country_mapping_df = country_mapping_df[country_mapping_df['reporting_cluster'].isin(VALID_REPORTING_CLUSTERS)].copy()
    
    print(f"Filtered to {len(country_mapping_df)} business unit mappings (valid clusters only)")
    print(f"Valid reporting clusters: {country_mapping_df['reporting_cluster'].unique().tolist()}")
    print(f"Sample mappings: {country_mapping_df.head(10).to_string()}")
else:
    print("⚠️  WARNING: country_mapping_df is empty!")
print(f"Loaded {len(country_mapping_df)} business unit mappings in {time() - start_time:.2f} seconds")

# COMMAND ----------

# Helper functions for formatting and summary generation
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

def generate_summary(row, comparison_label):
    """Generate a formatted summary for a metric"""
    metric_name = row['metric_final_name']
    cluster = row['reporting_cluster']
    metric_type = row['metric_type']
    
    rel_change = row['relative_change_pct']
    abs_change = row['absolute_change'] * 100
    
    try:
        volume_impacted = row['current_metric_value_denominator'] * abs(rel_change) / 100
    except (TypeError, ValueError):
        volume_impacted = 0
    
    sig_level = row.get('significance_level', 0)
    sig_text = "significant" if sig_level >= 3 else "not statistically significant"
    
    if abs(rel_change) >= 20:
        magnitude = "substantial"
    elif abs(rel_change) >= 10:
        magnitude = "notable"
    else:
        magnitude = "slight"
    
    direction = "increased" if abs_change > 0 else "decreased"
    impact = row['impact_direction'].lower()
    
    if metric_type == 'ratio':
        current_ratio = row['current_ratio'] * 100
        prev_ratio = row['prev_ratio'] * 100
        summary = (
            f"For {cluster} cluster, the {metric_name} {direction} from {prev_ratio:.2f}% to {current_ratio:.2f}%, "
            f"a {magnitude} {abs(rel_change):.2f}% {direction[:-1]} (volume impacted: {format_number(volume_impacted)}). "
            f"This change is {sig_text} and has a {impact} business impact. [{comparison_label}]"
        )
    else:
        current_ratio = row['current_ratio']
        prev_ratio = row['prev_ratio']
        summary = (
            f"For {cluster} cluster, the {metric_name} {direction} from €{prev_ratio:.2f} to €{current_ratio:.2f}, "
            f"a {magnitude} {abs(rel_change):.2f}% {direction[:-1]} (volume impacted: {format_number(volume_impacted)}). "
            f"This change is {sig_text} and has a {impact} business impact. [{comparison_label}]"
        )
    
    return summary

# COMMAND ----------

# Function to write individual output for a single comparison
def write_single_comparison_output(comp_info, output_folder, mode_key):
    """
    Write output for a single comparison type.
    
    Parameters:
    -----------
    comp_info : dict
        Dictionary containing 'data', 'label', 'date_value' for the comparison
    output_folder : str
        Base output folder path
    mode_key : str
        Key for the comparison mode (e.g., 'week_prev', 'month_yoy')
    
    Returns:
    --------
    str
        Path to the generated file
    """
    # Create output directory
    output_folder_dir = f'{output_folder}'
    if not os.path.exists(output_folder_dir):
        try:
            os.makedirs(output_folder_dir)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    
    # Map mode_key to filename
    # Only week_prev uses this function, others use merged files
    filename_map = {
        'week_prev': 'detailed_summary.txt',
        'week_yoy': 'detailed_summary_week_vs_prev_yr_week.txt',
        'month_prev': 'detailed_summary_month_vs_prev_month.txt',
        'month_yoy': 'detailed_summary_month_vs_prev_yr_month.txt',
        'quarter_prev': 'detailed_summary_quarter_vs_prev_quarter.txt',
        'quarter_yoy': 'detailed_summary_quarter_vs_prev_yr_quarter.txt'
    }
    
    filename = filename_map.get(mode_key, f'detailed_summary_{mode_key}.txt')
    detailed_summary_path = f'{output_folder_dir}/{filename}'
    
    df = comp_info['data']
    
    with open(detailed_summary_path, 'w') as f:
        f.write(f"Steering Metrics - {comp_info['label']}\n")
        f.write("=" * 80 + "\n\n")
        
        # Write period information
        if comp_info.get('current_weeks'):
            f.write(f"Current Period: {comp_info['current_weeks']}\n")
        if comp_info.get('prev_weeks'):
            f.write(f"Previous Period: {comp_info['prev_weeks']}\n")
        if comp_info.get('current_weeks') or comp_info.get('prev_weeks'):
            f.write("\n" + "=" * 80 + "\n\n")
        
        # Process each metric
        for mn in STEERING_METRICS:
            f.write(f"\n{'='*80}\n")
            f.write(f"{mn}\n")
            f.write(f"{'='*80}\n\n")
            
            df_metric = df[df['metric_final_name'] == mn]
            
            if df_metric.empty:
                continue
            
            # Process each reporting cluster
            for rc in REPORTING_CLUSTERS:
                # Overall summary
                level1_rows = df_metric[(df_metric['reporting_cluster'] == rc) & 
                                       (df_metric['dimension_name'] == '_Overall')]
                
                if not level1_rows.empty:
                    for _, row in level1_rows.iterrows():
                        summary = generate_summary(row, comp_info['label'])
                        f.write(f"{summary}\n\n")
                
                # Dimensions
                level2_dims_rows = df_metric[(df_metric['reporting_cluster'] == rc) & 
                                           (df_metric['dimension_name'] != '_Overall')]
                if not level2_dims_rows.empty:
                    level2_dims_rows = level2_dims_rows.copy()
                    level2_dims_rows.loc[:, 'abs_rel_change'] = abs(level2_dims_rows['relative_change_pct'])
                    level2_dims_rows.loc[:, 'volume_impacted'] = level2_dims_rows['current_metric_value_denominator'] * level2_dims_rows['abs_rel_change'] / 100
                    sorted_dims = level2_dims_rows.sort_values('volume_impacted', ascending=False)
                    filtered_dims = sorted_dims[(sorted_dims['abs_rel_change']>10) | (sorted_dims['volume_impacted']>30)]
                    
                    if not filtered_dims.empty:
                        f.write(f"Top dimensions by change magnitude ({rc} cluster):\n")
                        for _, row in filtered_dims.iterrows():
                            item_name = f"{row['dimension_name']} {row['dimension_value']}"
                            direction = "increase" if row['absolute_change'] > 0 else "decrease"
                            change = abs(row['relative_change_pct'])
                            volume_impacted = row['volume_impacted']
                            metric_type = row['metric_type']
                            
                            if metric_type == 'ratio':
                                current = row['current_ratio'] * 100
                                prev = row['prev_ratio'] * 100
                                f.write(f"- {item_name}: {prev:.2f}% to {current:.2f}% ({change:.2f}% {direction}, volume impacted: {format_number(volume_impacted)})\n")
                            else:
                                current = row['current_ratio']
                                prev = row['prev_ratio']
                                f.write(f"- {item_name}: €{prev:.2f} to €{current:.2f} ({change:.2f}% {direction}, volume impacted: {format_number(volume_impacted)})\n")
                        f.write("\n")
                
                # Business units
                if rc != 'Overall':
                    rc_bu = country_mapping_df[country_mapping_df['reporting_cluster'] == rc].business_unit.tolist()
                    level2_bu_rows = df_metric[(df_metric['business_unit'].isin(rc_bu))]
                    
                    if not level2_bu_rows.empty:
                        level2_bu_rows = level2_bu_rows.copy()
                        level2_bu_rows.loc[:, 'abs_rel_change'] = abs(level2_bu_rows['relative_change_pct'])
                        level2_bu_rows.loc[:, 'volume_impacted'] = level2_bu_rows['current_metric_value_denominator'] * level2_bu_rows['abs_rel_change'] / 100
                        sorted_bu = level2_bu_rows.sort_values('volume_impacted', ascending=False)
                        filtered_bu = sorted_bu[(sorted_bu['abs_rel_change']>10) | (sorted_bu['volume_impacted']>30)]
                        
                        if not filtered_bu.empty:
                            f.write(f"All business units by change magnitude:\n")
                            for _, row in filtered_bu.iterrows():
                                if row['business_unit'] == "Null":
                                    continue
                                item_name = row['business_unit']
                                direction = "increase" if row['absolute_change'] > 0 else "decrease"
                                change = abs(row['relative_change_pct'])
                                volume_impacted = row['volume_impacted']
                                metric_type = row['metric_type']
                                
                                if metric_type == 'ratio':
                                    current = row['current_ratio'] * 100
                                    prev = row['prev_ratio'] * 100
                                    f.write(f"- {item_name}: {prev:.2f}% to {current:.2f}% ({change:.2f}% {direction}, volume impacted: {format_number(volume_impacted)})\n")
                                else:
                                    current = row['current_ratio']
                                    prev = row['prev_ratio']
                                    f.write(f"- {item_name}: €{prev:.2f} to €{current:.2f} ({change:.2f}% {direction}, volume impacted: {format_number(volume_impacted)})\n")
                            f.write("\n")
            
            f.write("\n")
    
    return detailed_summary_path

# COMMAND ----------

# Function to filter data for >10% changes
def filter_significant_changes(df):
    """Filter DataFrame to only include changes with relative_change_pct > 10%"""
    df = df.copy()
    if 'abs_rel_change' not in df.columns:
        df['abs_rel_change'] = abs(df['relative_change_pct'])
    return df[df['abs_rel_change'] > 10].copy()

# Function to create deduplication key
def create_dedup_key(row):
    """Create a key for deduplication: (metric, cluster, dimension, dimension_value, business_unit)"""
    # For bu_level rows, we want to deduplicate by metric, dimension, and business_unit
    # but NOT by reporting_cluster (since all bu_level rows have reporting_cluster='bu_level')
    # Instead, we'll use a special marker to ensure bu_level rows are deduplicated correctly
    reporting_cluster = row.get('reporting_cluster', '')
    if reporting_cluster == 'bu_level':
        # For bu_level, use 'bu_level' as the cluster in the key
        # This ensures bu_level rows are deduplicated separately from Overall rows
        cluster_key = 'bu_level'
    else:
        cluster_key = reporting_cluster
    
    return (
        row['metric_final_name'],
        cluster_key,
        row['dimension_name'],
        str(row.get('dimension_value', '')),
        str(row.get('business_unit', ''))
    )

# Function to get period priority (higher = longer period, should be kept)
def get_period_priority(mode_key):
    """Return priority for period deduplication (higher = keep)"""
    priority_map = {
        'quarter_prev': 3,
        'quarter_yoy': 3,
        'month_prev': 2,
        'month_yoy': 2,
        'week_prev': 1,
        'week_yoy': 1
    }
    return priority_map.get(mode_key, 0)

# Function to deduplicate across periods
def deduplicate_across_periods(comparisons_dict):
    """
    Deduplicate metrics across periods, keeping only the longest period.
    
    Parameters:
    -----------
    comparisons_dict : dict
        Dictionary with mode_key as key and comp_info as value
        
    Returns:
    --------
    dict
        Deduplicated dictionary
    """
    # First pass: collect all rows with their keys and priorities
    all_rows_by_key = {}
    
    for mode_key, comp_info in comparisons_dict.items():
        df = comp_info['data'].copy()
        priority = get_period_priority(mode_key)
        
        for _, row in df.iterrows():
            key = create_dedup_key(row)
            if key not in all_rows_by_key:
                all_rows_by_key[key] = {
                    'row': row,
                    'mode_key': mode_key,
                    'priority': priority,
                    'comp_info': comp_info
                }
            # If key already exists, keep the one with higher priority
            elif priority > all_rows_by_key[key]['priority']:
                all_rows_by_key[key] = {
                    'row': row,
                    'mode_key': mode_key,
                    'priority': priority,
                    'comp_info': comp_info
                }
    
    # Second pass: group rows by mode_key to reconstruct DataFrames
    deduplicated = {}
    for key, data in all_rows_by_key.items():
        mode_key = data['mode_key']
        if mode_key not in deduplicated:
            deduplicated[mode_key] = {
                'rows': [],
                'comp_info': data['comp_info']
            }
        deduplicated[mode_key]['rows'].append(data['row'])
    
    # Convert to DataFrames
    result = {}
    for mode_key, data in deduplicated.items():
        deduplicated_df = pd.DataFrame(data['rows'])
        result[mode_key] = {
            'data': deduplicated_df,
            'label': data['comp_info']['label'],
            'date_value': data['comp_info'].get('date_value', ''),
            'current_weeks': data['comp_info'].get('current_weeks', ''),
            'prev_weeks': data['comp_info'].get('prev_weeks', '')
        }
    
    return result

# Function to write merged long-term impact file
def write_long_term_impact_output(all_comparison_data, output_folder):
    """
    Write merged file for long-term impact (month_prev + quarter_prev, >10% only, deduplicated)
    """
    # Get month_prev and quarter_prev data
    long_term_comparisons = {}
    for mode_key in ['month_prev', 'quarter_prev']:
        if mode_key in all_comparison_data:
            comp_info = all_comparison_data[mode_key]
            # Don't filter for >10% changes - use all data to check if business units exist
            filtered_df = comp_info['data'].copy()
            
            # Debug: Check bu_level rows before deduplication
            if 'reporting_cluster' in filtered_df.columns:
                bu_level_rows = filtered_df[filtered_df['reporting_cluster'] == 'bu_level']
                print(f"DEBUG: {mode_key} - Before deduplication: {len(filtered_df)} total rows, {len(bu_level_rows)} bu_level rows")
                if not bu_level_rows.empty:
                    debug_file = f'{output_folder}/debug_bu_level_{mode_key}_before_dedup.csv'
                    bu_level_rows.to_csv(debug_file, index=False)
            
            if not filtered_df.empty:
                long_term_comparisons[mode_key] = {
                    'data': filtered_df,
                    'label': comp_info['label'],
                    'date_value': comp_info.get('date_value', ''),
                    'current_weeks': comp_info.get('current_weeks', ''),
                    'prev_weeks': comp_info.get('prev_weeks', '')
                }
    
    # Deduplicate
    deduplicated = deduplicate_across_periods(long_term_comparisons)
    
    # Debug: Check bu_level rows after deduplication
    for mode_key in deduplicated:
        df = deduplicated[mode_key]['data']
        if 'reporting_cluster' in df.columns:
            bu_level_rows = df[df['reporting_cluster'] == 'bu_level']
            print(f"DEBUG: {mode_key} - After deduplication: {len(df)} total rows, {len(bu_level_rows)} bu_level rows")
            if not bu_level_rows.empty:
                debug_file = f'{output_folder}/debug_bu_level_{mode_key}_after_dedup.csv'
                bu_level_rows.to_csv(debug_file, index=False)
    
    if not long_term_comparisons:
        return None
    
    # Write merged file
    output_folder_dir = f'{output_folder}'
    if not os.path.exists(output_folder_dir):
        os.makedirs(output_folder_dir)
    
    filename = 'long_term.txt'
    file_path = f'{output_folder_dir}/{filename}'
    
    with open(file_path, 'w') as f:
        f.write("Steering Metrics - Long-Term Impact Analysis\n")
        f.write("=" * 80 + "\n\n")
        f.write("This report shows significant changes (>10%) in month-over-month and quarter-over-quarter comparisons.\n")
        f.write("If a metric appears in both month and quarter comparisons, only the quarter comparison is shown.\n\n")
        f.write("=" * 80 + "\n\n")
        
        # Write by period type (quarter first, then month)
        period_order = ['quarter_prev', 'month_prev']
        for mode_key in period_order:
            if mode_key not in deduplicated:
                continue
            
            comp_info = deduplicated[mode_key]
            df = comp_info['data']
            
            # Debug: Check if bu_level rows exist for this period AFTER deduplication
            if 'reporting_cluster' in df.columns:
                all_bu_rows = df[df['reporting_cluster'] == 'bu_level']
                debug_summary = f"{mode_key}: Total rows={len(df)}, bu_level rows={len(all_bu_rows)}\n"
                with open(f'{output_folder}/debug_dedup_summary.txt', 'a') as debug_f:
                    debug_f.write(debug_summary)
                
                if not all_bu_rows.empty:
                    unique_bus = all_bu_rows['business_unit'].dropna().unique().tolist() if 'business_unit' in all_bu_rows.columns else []
                    print(f"DEBUG long-term: {mode_key} - Found {len(all_bu_rows)} bu_level rows, {len(unique_bus)} unique BUs: {unique_bus[:10]}")
                    # Write sample to verify structure
                    sample_cols = ['reporting_cluster', 'business_unit', 'metric_final_name', 'dimension_name', 
                                  'current_ratio', 'prev_ratio', 'relative_change_pct']
                    available_cols = [c for c in sample_cols if c in all_bu_rows.columns]
                    if available_cols:
                        sample = all_bu_rows[available_cols].head(5)
                        debug_file = f'{output_folder}/debug_bu_sample_{mode_key}.csv'
                        sample.to_csv(debug_file, index=False)
                        print(f"DEBUG: Wrote sample bu_level rows to {debug_file}")
                else:
                    print(f"DEBUG long-term: {mode_key} - NO bu_level rows found in deduplicated data!")
            
            f.write(f"\n{'='*80}\n")
            f.write(f"{comp_info['label']}\n")
            f.write(f"{'='*80}\n\n")
            
            if comp_info.get('current_weeks'):
                f.write(f"Current Period: {comp_info['current_weeks']}\n")
            if comp_info.get('prev_weeks'):
                f.write(f"Previous Period: {comp_info['prev_weeks']}\n")
            f.write("\n")
            
            # Process each metric
            for mn in STEERING_METRICS:
                df_metric = df[df['metric_final_name'] == mn]
                if df_metric.empty:
                    continue
                
                f.write(f"\n{'='*80}\n")
                f.write(f"{mn}\n")
                f.write(f"{'='*80}\n\n")
                
                # First, write all bu_level rows for this metric (bypass lookup for now)
                all_bu_for_metric = df_metric[df_metric['reporting_cluster'] == 'bu_level'].copy()
                if not all_bu_for_metric.empty:
                    all_bu_for_metric = all_bu_for_metric[
                        (all_bu_for_metric['dimension_name'] == '_Overall')
                    ].copy()
                    
                    if not all_bu_for_metric.empty:
                        # Group by business_unit and write
                        all_bu_for_metric['abs_rel_change'] = abs(all_bu_for_metric['relative_change_pct'])
                        all_bu_for_metric['volume_impacted'] = all_bu_for_metric['current_metric_value_denominator'] * all_bu_for_metric['abs_rel_change'] / 100
                        sorted_bu = all_bu_for_metric.sort_values('volume_impacted', ascending=False)
                        
                        # Group by reporting cluster using country_mapping_df
                        bu_by_cluster = {}
                        for _, row in sorted_bu.iterrows():
                            bu = str(row.get('business_unit', '')).strip()
                            if not bu or bu in ['Null', 'None', '']:
                                continue
                            
                            # Find which reporting cluster this BU belongs to
                            bu_clusters = country_mapping_df[country_mapping_df['business_unit'] == bu]['reporting_cluster'].unique().tolist()
                            if not bu_clusters:
                                # If no mapping found, skip
                                continue
                            
                            for cluster in bu_clusters:
                                # Only include valid clusters (exclude 'Overall')
                                if cluster in VALID_REPORTING_CLUSTERS and cluster != 'Overall':
                                    if cluster not in bu_by_cluster:
                                        bu_by_cluster[cluster] = []
                                    bu_by_cluster[cluster].append(row)
                        
                        # Write by cluster (only >10% changes)
                        for cluster, bu_rows_list in bu_by_cluster.items():
                            # Skip 'Overall' cluster for business units
                            if cluster == 'Overall' or cluster not in VALID_REPORTING_CLUSTERS:
                                continue
                            if not bu_rows_list:
                                continue
                            
                            # Filter for >10% changes
                            filtered_bu_list = []
                            for row in bu_rows_list:
                                change = abs(row.get('relative_change_pct', 0))
                                if change > 10:
                                    filtered_bu_list.append(row)
                            
                            if not filtered_bu_list:
                                continue
                            
                            f.write(f"All business units by change magnitude ({cluster} cluster):\n")
                            for row in filtered_bu_list:
                                bu_value = str(row.get('business_unit', '')).strip()
                                direction = "increase" if row.get('absolute_change', 0) > 0 else "decrease"
                                change = abs(row.get('relative_change_pct', 0))
                                volume_impacted = row.get('volume_impacted', 0)
                                metric_type = row.get('metric_type', 'ratio')
                                
                                try:
                                    if metric_type == 'ratio':
                                        current = row.get('current_ratio', 0) * 100
                                        prev = row.get('prev_ratio', 0) * 100
                                        f.write(f"- {bu_value}: {prev:.2f}% to {current:.2f}% ({change:.2f}% {direction}, volume impacted: {format_number(volume_impacted)})\n")
                                    else:
                                        current = row.get('current_ratio', 0)
                                        prev = row.get('prev_ratio', 0)
                                        f.write(f"- {bu_value}: €{prev:.2f} to €{current:.2f} ({change:.2f}% {direction}, volume impacted: {format_number(volume_impacted)})\n")
                                except:
                                    continue
                            f.write("\n")
                
                # Process each reporting cluster (for Overall and dimensions)
                for rc in REPORTING_CLUSTERS:
                    rc_rows = df_metric[df_metric['reporting_cluster'] == rc]
                    if rc_rows.empty:
                        continue
                    
                    # Overall cluster summary
                    overall_rows = rc_rows[rc_rows['dimension_name'] == '_Overall']
                    if not overall_rows.empty:
                        for _, row in overall_rows.iterrows():
                            summary = generate_summary(row, comp_info['label'])
                            f.write(f"{summary}\n\n")
                    
                    # Dimensions
                    dim_rows = rc_rows[(rc_rows['dimension_name'] != '_Overall') & 
                                      (rc_rows['reporting_cluster'] == rc)]
                    if not dim_rows.empty:
                        dim_rows = dim_rows.copy()
                        if 'abs_rel_change' not in dim_rows.columns:
                            dim_rows['abs_rel_change'] = abs(dim_rows['relative_change_pct'])
                        if 'volume_impacted' not in dim_rows.columns:
                            dim_rows['volume_impacted'] = dim_rows['current_metric_value_denominator'] * dim_rows['abs_rel_change'] / 100
                        sorted_dims = dim_rows.sort_values('volume_impacted', ascending=False)
                        # Filter for >10% changes
                        filtered_dims = sorted_dims[sorted_dims['abs_rel_change'] > 10]
                        if not filtered_dims.empty:
                            f.write(f"Top dimensions by change magnitude ({rc} cluster):\n")
                            for _, row in filtered_dims.iterrows():
                                item_name = f"{row['dimension_name']} {row['dimension_value']}"
                                direction = "increase" if row['absolute_change'] > 0 else "decrease"
                                change = abs(row['relative_change_pct'])
                                volume_impacted = row['volume_impacted']
                                metric_type = row['metric_type']
                                
                                if metric_type == 'ratio':
                                    current = row['current_ratio'] * 100
                                    prev = row['prev_ratio'] * 100
                                    f.write(f"- {item_name}: {prev:.2f}% to {current:.2f}% ({change:.2f}% {direction}, volume impacted: {format_number(volume_impacted)})\n")
                                else:
                                    current = row['current_ratio']
                                    prev = row['prev_ratio']
                                    f.write(f"- {item_name}: €{prev:.2f} to €{current:.2f} ({change:.2f}% {direction}, volume impacted: {format_number(volume_impacted)})\n")
                            f.write("\n")
                    
    
    return file_path

# Function to write merged year-over-year file
def write_year_over_year_output(all_comparison_data, output_folder):
    """
    Write merged file for year-over-year comparisons (week_yoy + month_yoy + quarter_yoy, >10% only, deduplicated)
    """
    # Get year-over-year data
    yoy_comparisons = {}
    for mode_key in ['week_yoy', 'month_yoy', 'quarter_yoy']:
        if mode_key in all_comparison_data:
            comp_info = all_comparison_data[mode_key]
            # Filter for >10% changes
            filtered_df = filter_significant_changes(comp_info['data'])
            if not filtered_df.empty:
                yoy_comparisons[mode_key] = {
                    'data': filtered_df,
                    'label': comp_info['label'],
                    'date_value': comp_info.get('date_value', ''),
                    'current_weeks': comp_info.get('current_weeks', ''),
                    'prev_weeks': comp_info.get('prev_weeks', '')
                }
    
    if not yoy_comparisons:
        return None
    
    # Deduplicate (quarter > month > week)
    deduplicated = deduplicate_across_periods(yoy_comparisons)
    
    # Write merged file
    output_folder_dir = f'{output_folder}'
    if not os.path.exists(output_folder_dir):
        os.makedirs(output_folder_dir)
    
    filename = 'comparison_prev_yr.txt'
    file_path = f'{output_folder_dir}/{filename}'
    
    with open(file_path, 'w') as f:
        f.write("Steering Metrics - Year-over-Year Comparison\n")
        f.write("=" * 80 + "\n\n")
        f.write("This report shows significant changes (>10%) comparing current periods to the same periods last year.\n")
        f.write("If a metric appears in multiple period types, only the longest period comparison is shown.\n\n")
        f.write("=" * 80 + "\n\n")
        
        # Write by period type (quarter first, then month, then week)
        period_order = ['quarter_yoy', 'month_yoy', 'week_yoy']
        for mode_key in period_order:
            if mode_key not in deduplicated:
                continue
            
            comp_info = deduplicated[mode_key]
            df = comp_info['data']
            
            f.write(f"\n{'='*80}\n")
            f.write(f"{comp_info['label']}\n")
            f.write(f"{'='*80}\n\n")
            
            if comp_info.get('current_weeks'):
                f.write(f"Current Period: {comp_info['current_weeks']}\n")
            if comp_info.get('prev_weeks'):
                f.write(f"Previous Year Period: {comp_info['prev_weeks']}\n")
            f.write("\n")
            
            # Process each metric (same logic as long-term impact)
            for mn in STEERING_METRICS:
                df_metric = df[df['metric_final_name'] == mn]
                if df_metric.empty:
                    continue
                
                f.write(f"\n{'='*80}\n")
                f.write(f"{mn}\n")
                f.write(f"{'='*80}\n\n")
                
                # First, write all bu_level rows for this metric (same approach as long-term impact)
                all_bu_for_metric = df_metric[df_metric['reporting_cluster'] == 'bu_level'].copy()
                if not all_bu_for_metric.empty:
                    all_bu_for_metric = all_bu_for_metric[
                        (all_bu_for_metric['dimension_name'] == '_Overall')
                    ].copy()
                    
                    if not all_bu_for_metric.empty:
                        # Group by business_unit and write
                        all_bu_for_metric['abs_rel_change'] = abs(all_bu_for_metric['relative_change_pct'])
                        all_bu_for_metric['volume_impacted'] = all_bu_for_metric['current_metric_value_denominator'] * all_bu_for_metric['abs_rel_change'] / 100
                        sorted_bu = all_bu_for_metric.sort_values('volume_impacted', ascending=False)
                        
                        # Group by reporting cluster using country_mapping_df
                        bu_by_cluster = {}
                        for _, row in sorted_bu.iterrows():
                            bu = str(row.get('business_unit', '')).strip()
                            if not bu or bu in ['Null', 'None', '']:
                                continue
                            
                            # Find which reporting cluster this BU belongs to
                            bu_clusters = country_mapping_df[country_mapping_df['business_unit'] == bu]['reporting_cluster'].unique().tolist()
                            if not bu_clusters:
                                continue
                            
                            for cluster in bu_clusters:
                                # Only include valid clusters (exclude 'Overall')
                                if cluster in VALID_REPORTING_CLUSTERS and cluster != 'Overall':
                                    if cluster not in bu_by_cluster:
                                        bu_by_cluster[cluster] = []
                                    bu_by_cluster[cluster].append(row)
                        
                        # Write by cluster (only >10% changes, already filtered by filter_significant_changes)
                        for cluster, bu_rows_list in bu_by_cluster.items():
                            # Skip 'Overall' cluster for business units
                            if cluster == 'Overall' or cluster not in VALID_REPORTING_CLUSTERS:
                                continue
                            if not bu_rows_list:
                                continue
                            
                            f.write(f"All business units by change magnitude ({cluster} cluster):\n")
                            for row in bu_rows_list:
                                bu_value = str(row.get('business_unit', '')).strip()
                                direction = "increase" if row.get('absolute_change', 0) > 0 else "decrease"
                                change = abs(row.get('relative_change_pct', 0))
                                volume_impacted = row.get('volume_impacted', 0)
                                metric_type = row.get('metric_type', 'ratio')
                                
                                try:
                                    if metric_type == 'ratio':
                                        current = row.get('current_ratio', 0) * 100
                                        prev = row.get('prev_ratio', 0) * 100
                                        f.write(f"- {bu_value}: {prev:.2f}% to {current:.2f}% ({change:.2f}% {direction}, volume impacted: {format_number(volume_impacted)})\n")
                                    else:
                                        current = row.get('current_ratio', 0)
                                        prev = row.get('prev_ratio', 0)
                                        f.write(f"- {bu_value}: €{prev:.2f} to €{current:.2f} ({change:.2f}% {direction}, volume impacted: {format_number(volume_impacted)})\n")
                                except:
                                    continue
                            f.write("\n")
                
                # Process each reporting cluster (for Overall and dimensions)
                for rc in REPORTING_CLUSTERS:
                    rc_rows = df_metric[df_metric['reporting_cluster'] == rc]
                    if rc_rows.empty:
                        continue
                    
                    # Overall cluster summary
                    overall_rows = rc_rows[rc_rows['dimension_name'] == '_Overall']
                    if not overall_rows.empty:
                        for _, row in overall_rows.iterrows():
                            summary = generate_summary(row, comp_info['label'])
                            f.write(f"{summary}\n\n")
                    
                    # Dimensions
                    dim_rows = rc_rows[(rc_rows['dimension_name'] != '_Overall') & 
                                      (rc_rows['reporting_cluster'] == rc)]
                    if not dim_rows.empty:
                        dim_rows = dim_rows.copy()
                        if 'abs_rel_change' not in dim_rows.columns:
                            dim_rows['abs_rel_change'] = abs(dim_rows['relative_change_pct'])
                        if 'volume_impacted' not in dim_rows.columns:
                            dim_rows['volume_impacted'] = dim_rows['current_metric_value_denominator'] * dim_rows['abs_rel_change'] / 100
                        sorted_dims = dim_rows.sort_values('volume_impacted', ascending=False)
                        filtered_dims = sorted_dims[sorted_dims['abs_rel_change'] > 10]
                        if not filtered_dims.empty:
                            f.write(f"Top dimensions by change magnitude ({rc} cluster):\n")
                            for _, row in filtered_dims.iterrows():
                                item_name = f"{row['dimension_name']} {row['dimension_value']}"
                                direction = "increase" if row['absolute_change'] > 0 else "decrease"
                                change = abs(row['relative_change_pct'])
                                volume_impacted = row['volume_impacted']
                                metric_type = row['metric_type']
                                
                                if metric_type == 'ratio':
                                    current = row['current_ratio'] * 100
                                    prev = row['prev_ratio'] * 100
                                    f.write(f"- {item_name}: {prev:.2f}% to {current:.2f}% ({change:.2f}% {direction}, volume impacted: {format_number(volume_impacted)})\n")
                                else:
                                    current = row['current_ratio']
                                    prev = row['prev_ratio']
                                    f.write(f"- {item_name}: €{prev:.2f} to €{current:.2f} ({change:.2f}% {direction}, volume impacted: {format_number(volume_impacted)})\n")
                            f.write("\n")
                    
    
    return file_path

# COMMAND ----------

# Generate output files (3 files total)
print("\n" + "="*80)
print("Generating Steering Metrics Reports")
print("="*80)

start_time = time()
generated_files = []

# Create output directory
output_folder_dir = f'{OUTPUT_BASE_FOLDER}'
if os.path.exists(output_folder_dir):
    try:
        shutil.rmtree(output_folder_dir)
    except Exception as e:
        print(f"Warning: Failed to remove directory: {e}")

try:
    os.makedirs(output_folder_dir)
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise

# 1. Generate week vs prev week (unchanged, all data)
if 'week_prev' in all_comparison_data:
    print(f"\nGenerating report for week_prev (all data)...")
    file_path = write_single_comparison_output(all_comparison_data['week_prev'], OUTPUT_BASE_FOLDER, 'week_prev')
    generated_files.append(file_path)
    print(f"  ✅ Generated: {file_path}")

# 2. Generate long-term impact file (month_prev + quarter_prev, >10% only, deduplicated)
print(f"\nGenerating long-term impact report (month_prev + quarter_prev, >10% only)...")
file_path = write_long_term_impact_output(all_comparison_data, OUTPUT_BASE_FOLDER)
if file_path:
    generated_files.append(file_path)
    print(f"  ✅ Generated: {file_path}")
else:
    print(f"  ⚠️  No significant changes found for long-term impact")

# 3. Generate year-over-year file (week_yoy + month_yoy + quarter_yoy, >10% only, deduplicated)
print(f"\nGenerating year-over-year report (week_yoy + month_yoy + quarter_yoy, >10% only)...")
file_path = write_year_over_year_output(all_comparison_data, OUTPUT_BASE_FOLDER)
if file_path:
    generated_files.append(file_path)
    print(f"  ✅ Generated: {file_path}")
else:
    print(f"  ⚠️  No significant changes found for year-over-year")

total_time = time() - start_time
print(f"\n✅ Steering metrics generation completed!")
print(f"Output directory: {OUTPUT_BASE_FOLDER}")
print(f"Generated {len(generated_files)} report file(s):")
for file_path in generated_files:
    print(f"  - {file_path}")
print(f"Total generation time: {total_time:.2f} seconds")

# COMMAND ----------

# Download the detailed_summary files
for file_path in generated_files:
    if os.path.exists(file_path):
        filename = os.path.basename(file_path)
        output_file_path = f"/tmp/{filename}"
        with open(file_path, 'r') as f:
            content = f.read()
        dbutils.fs.put(output_file_path, content, overwrite=True)
        print(f"\n{filename} written to DBFS: {output_file_path}")
        print(f"Local path: {file_path}")
    else:
        print(f"Error: Could not find {file_path}")

