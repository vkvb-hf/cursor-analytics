# Databricks notebook source
# MAGIC %md
# MAGIC # Steering Output Generation - Parameterized
# MAGIC 
# MAGIC This notebook generates steering output with multiple comparison types:
# MAGIC - Week-over-week (current_week vs prev_week)
# MAGIC - Year-over-year week (current_week vs prev_yr_week)
# MAGIC - Month-over-month (current_month vs prev_month)
# MAGIC - Year-over-year month (current_month vs prev_yr_month)

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
WORKSPACE_FOLDER = f'/Workspace/Users/elizaveta.dmitrieva@hellofresh.com'

# Define metrics and constants for reporting
REPORTING_CLUSTERS = ['Overall', 'HF-NA', 'HF-INTL', 'US-HF', 'RTE', 'WL']

# Comparison configuration
# Set to 'all' to generate all 4 comparisons, or specify individual ones
# Options: 'all', 'week_prev', 'week_yoy', 'month_prev', 'month_yoy'
COMPARISON_MODES = 'all'  # Options: 'all', ['week_prev', 'week_yoy', 'month_prev', 'month_yoy']

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

print(f"Latest reporting week: {latest_week_str}")
print(f"Latest 4 weeks (current month): {latest_4weeks_str} ({latest_4weeks_list})")
print(f"Previous 4 weeks (prev month): {prev_4weeks_str} ({prev_4weeks_list})")
print(f"Previous year 4 weeks (prev yr month): {prev_yr_4weeks_str} ({prev_yr_4weeks_list})")
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
        'WEEK' or '4WEEKS'
    comparison_type : str
        'prev_period' or 'prev_year'
    date_value_str : str
        The date value to filter on (e.g., '2025-W44' or '2025-W41-2025-W44')
    weeks_list : list, optional
        List of week strings for 4-week aggregation (e.g., ['2025-W41', '2025-W42', '2025-W43', '2025-W44'])
    
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
    
    # Handle 4-week aggregation vs single week
    if date_granularity == '4WEEKS' and weeks_list:
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
    
    # For 4-week periods, we need to exclude date_value from GROUP BY since we're aggregating across weeks
    if date_granularity == '4WEEKS' and weeks_list:
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
    SUM(a.current_metric_value_denominator) AS current_metric_value_denominator,
    SUM(a.{prev_num_col}) AS prev_metric_value_numerator,
    SUM(a.{prev_den_col}) AS prev_metric_value_denominator
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
    SUM(a.current_metric_value_denominator) AS current_metric_value_denominator,
    SUM(a.{prev_num_col}) AS prev_metric_value_numerator,
    SUM(a.{prev_den_col}) AS prev_metric_value_denominator
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
    print(f"  Processed {len(result_df)} rows in {time() - start_time:.2f} seconds")
    
    return result_df

# COMMAND ----------

# Determine which comparisons to run
# For month comparisons, we now use 4-week periods
if COMPARISON_MODES == 'all':
    comparisons_to_run = [
        ('WEEK', 'prev_period', latest_week_str, 'week_prev', None, None),
        ('WEEK', 'prev_year', latest_week_str, 'week_yoy', None, None),
        ('4WEEKS', 'prev_period', latest_4weeks_str, 'month_prev', latest_4weeks_list, prev_4weeks_list),
        ('4WEEKS', 'prev_year', latest_4weeks_str, 'month_yoy', latest_4weeks_list, prev_yr_4weeks_list)
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
    
    # For 4-week periods, we need to aggregate current and previous weeks separately
    if date_granularity == '4WEEKS' and current_weeks_list and prev_weeks_list:
        # For 4-week comparisons:
        # - Current period: aggregate current_metric_value across current 4 weeks
        # - Previous period: aggregate current_metric_value across previous 4 weeks (for prev_period)
        # - Previous year: aggregate prev_yr_metric_value across current 4 weeks (for prev_year)
        
        if comparison_type == 'prev_period':
            # Query current 4 weeks (current period)
            query_current = build_metrics_query('4WEEKS', 'current', date_value_str, current_weeks_list)
            data_current = spark.sql(query_current)
            
            # Query previous 4 weeks (previous period) - use their current values
            query_prev = build_metrics_query('4WEEKS', 'current', prev_weeks_list[0] + '-' + prev_weeks_list[-1], prev_weeks_list)
            data_prev = spark.sql(query_prev)
            print(f"  Prev 4 weeks query returned {data_prev.count()} rows")
            
            # Drop any existing prev columns from data_prev (they might exist from the query)
            prev_cols_to_drop = [c for c in data_prev.columns if c.startswith('prev_metric_value')]
            if prev_cols_to_drop:
                data_prev = data_prev.select([c for c in data_prev.columns if c not in prev_cols_to_drop])
            
            # Rename columns in prev data to be the "previous" values
            data_prev = data_prev.withColumnRenamed("current_metric_value_numerator", "prev_metric_value_numerator")
            data_prev = data_prev.withColumnRenamed("current_metric_value_denominator", "prev_metric_value_denominator")
            
            print(f"  Current 4 weeks query returned {data_current.count()} rows")
            
            # Join and combine
            join_cols = ['reporting_cluster', 'business_unit', 'metric_final_name', 'dimension_name', 'dimension_value', 
                         'flag_more_is_good', 'flag_is_p0', 'metric_type']
            
            # Select only the columns we need from data_current (excluding any prev columns)
            data_current_cols = [c for c in data_current.columns if c not in ['prev_metric_value_numerator', 'prev_metric_value_denominator']]
            data_current_clean = data_current.select(data_current_cols)
            
            # Select only needed columns from data_prev
            data_prev_selected = data_prev.select(
                [F.col(c) for c in join_cols] + 
                [F.col('prev_metric_value_numerator'), F.col('prev_metric_value_denominator')]
            )
            
            data = data_current_clean.join(
                data_prev_selected,
                on=join_cols,
                how='left'
            )
            
            # Check join results
            matched_count = data.filter(F.col('prev_metric_value_numerator').isNotNull()).count()
            print(f"  After join: {data.count()} total rows, {matched_count} with prev values")
            
            # Fill nulls with 0 for prev values
            data = data.fillna(0, subset=['prev_metric_value_numerator', 'prev_metric_value_denominator'])
            
            # Update the comparison label
            data = data.withColumn("comparison_label", F.lit("vs Previous Period"))
            data = data.withColumn("comparison_type", F.lit('prev_period'))
            
        elif comparison_type == 'prev_year':
            # For year-over-year, we use prev_yr columns from the current 4 weeks
            # Query current 4 weeks with prev_yr columns
            query = build_metrics_query('4WEEKS', 'prev_year', date_value_str, current_weeks_list)
            data = spark.sql(query)
        else:
            raise ValueError(f"Invalid comparison_type for 4WEEKS: {comparison_type}")
        
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
    else:
        label = processed_data['comparison_label'].iloc[0] if len(processed_data) > 0 else f"{date_granularity} {comparison_type}"
    
    all_comparison_data[mode_key] = {
        'data': processed_data,
        'date_granularity': date_granularity,
        'comparison_type': comparison_type,
        'date_value': date_value_str,
        'label': label
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

# Function to write combined output
def write_combined_output(all_comparison_data, output_folder):
    """
    Write combined output that merges all comparisons in a meaningful way.
    """
    print(f"\nGenerating combined reports in {output_folder}...")
    start_time = time()
    
    # Create output directory
    output_folder_dir = f'{output_folder}'
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
    
    # Create main detailed summary file
    detailed_summary_path = f'{output_folder_dir}/detailed_summary_combined.txt'
    
    with open(detailed_summary_path, 'w') as f:
        f.write("Steering Metrics - Combined Comparison Report\n")
        f.write("=" * 80 + "\n\n")
        
        # Write header with all comparison types
        f.write("Comparison Types Included:\n")
        for mode_key, comp_info in all_comparison_data.items():
            f.write(f"  - {comp_info['label']} ({comp_info['date_value']})\n")
        f.write("\n" + "=" * 80 + "\n\n")
        
        # Process each metric
        for mn in STEERING_METRICS:
            f.write(f"\n{'='*80}\n")
            f.write(f"{mn}\n")
            f.write(f"{'='*80}\n\n")
            
            # For each comparison, write the relevant data
            for mode_key, comp_info in all_comparison_data.items():
                df = comp_info['data']
                df_metric = df[df['metric_final_name'] == mn]
                
                if df_metric.empty:
                    continue
                
                f.write(f"\n--- {comp_info['label']} ({comp_info['date_value']}) ---\n\n")
                
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
                            f.write(f"Top dimensions by change magnitude:\n")
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
    
    total_time = time() - start_time
    print(f"Report generation complete:")
    print(f"  - Combined summary file: {detailed_summary_path}")
    print(f"  - Total generation time: {total_time:.2f} seconds")
    
    return detailed_summary_path

# COMMAND ----------

# Generate combined output
print("\n" + "="*80)
print("Generating Combined Output")
print("="*80)

detailed_summary_path = write_combined_output(all_comparison_data, OUTPUT_BASE_FOLDER)

print(f"\n✅ Steering metrics generation completed!")
print(f"Output directory: {OUTPUT_BASE_FOLDER}")
print(f"Combined summary: {detailed_summary_path}")

# COMMAND ----------

# Download the detailed_summary file
output_file_path = f"/tmp/steering_detailed_summary_combined.txt"
if os.path.exists(detailed_summary_path):
    with open(detailed_summary_path, 'r') as f:
        content = f.read()
    dbutils.fs.put(output_file_path, content, overwrite=True)
    print(f"\nDetailed summary written to DBFS: {output_file_path}")
    print(f"Local path: {detailed_summary_path}")
else:
    print(f"Error: Could not find detailed_summary.txt at {detailed_summary_path}")

