# Databricks notebook source
# MAGIC %md
# MAGIC # Long Term Steering Report - Parameterized
# MAGIC 
# MAGIC This notebook generates steering output for different comparison types.
# MAGIC 
# MAGIC **Comparison Types:**
# MAGIC - `week_prev`: Current week vs previous week
# MAGIC - `week_yoy`: Current week vs previous year same week
# MAGIC - `quarter_prev`: Current quarter (last 13 weeks) vs previous quarter (previous 13 weeks)

# COMMAND ----------

# ============================================================================
# CONFIGURATION
# ============================================================================
# Set the comparison type: 'week_prev', 'week_yoy', or 'quarter_prev'
COMPARISON_TYPE = 'week_yoy'  # Options: 'week_prev', 'week_yoy', 'quarter_prev'

# COMMAND ----------

# Import required libraries
import pyspark.sql.functions as F
from pyspark.sql.types import DoubleType
import math
import os
import errno
import pandas as pd
from time import time

# Modify the path to the workspace folder
WORKSPACE_FOLDER = f'/Workspace/Users/visal.kumar@hellofresh.com'

# Define metrics and constants for reporting
REPORTING_CLUSTERS = ['Overall', 'HF-NA', 'HF-INTL', 'RTE', 'WL']
VALID_REPORTING_CLUSTERS = ['HF-NA', 'HF-INTL', 'RTE', 'WL', 'Overall']

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

# Validate comparison type
if COMPARISON_TYPE not in ['week_prev', 'week_yoy', 'quarter_prev']:
    raise ValueError(f"Invalid COMPARISON_TYPE: {COMPARISON_TYPE}. Must be 'week_prev', 'week_yoy', or 'quarter_prev'")

print(f"Running comparison type: {COMPARISON_TYPE}")

# COMMAND ----------

# Get the latest complete week and periods for reporting
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

# Get 13-week periods if needed for quarter comparison
latest_13weeks_list = None
latest_13weeks_str = None
prev_13weeks_list = None
prev_13weeks_str = None

if COMPARISON_TYPE == 'quarter_prev':
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
        latest_13weeks_list = sorted(list(latest_13weeks_list))
        latest_13weeks_str = f"{latest_13weeks_list[0]}-{latest_13weeks_list[-1]}"
    
    # Get previous 13 weeks
    if latest_13weeks_list:
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
                  AND hellofresh_week < '{latest_13weeks_list[0]}'
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

print(f"Latest reporting week: {latest_week_str}")
if COMPARISON_TYPE == 'quarter_prev':
    print(f"Latest 13 weeks (current quarter): {latest_13weeks_str} ({latest_13weeks_list})")
    print(f"Previous 13 weeks (prev quarter): {prev_13weeks_str} ({prev_13weeks_list})")
print(f"Time to get latest dates: {time() - start_time:.2f} seconds")

# Output directory path - use a single folder for all comparison types
OUTPUT_BASE_FOLDER = f'{WORKSPACE_FOLDER}/long-term-steering-{latest_week_str if latest_week_str else "unknown"}'
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

# Function to build metrics query
def build_metrics_query(date_granularity, comparison_type, date_value_str, weeks_list=None):
    """
    Build metrics query for a specific comparison type.
    
    Parameters:
    -----------
    date_granularity : str
        'WEEK' or '13WEEKS'
    comparison_type : str
        'prev_year' for week_yoy, 'current' for quarter_prev aggregation
    date_value_str : str
        The date value to filter on
    weeks_list : list, optional
        List of week strings for multi-week aggregation
    """
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
        # For week_prev, use prev_metric_value columns
        prev_cols_select = f""",
    SUM(a.prev_metric_value_numerator) AS prev_metric_value_numerator,
    SUM(a.prev_metric_value_denominator) AS prev_metric_value_denominator"""
    else:
        # For prev_year, use prev_yr_metric_value columns
        prev_cols_select = f""",
    SUM(a.prev_yr_metric_value_numerator) AS prev_metric_value_numerator,
    SUM(a.prev_yr_metric_value_denominator) AS prev_metric_value_denominator"""
    
    metrics_query = f"""
    -- Query for {date_granularity} granularity, {comparison_type}
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

# Function to process metrics data
def process_comparison_data(data_df, comparison_label):
    """
    Process metrics data and calculate significance, changes, and impact.
    """
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
    bu_level_count = len(result_df[result_df['reporting_cluster'] == 'bu_level']) if 'reporting_cluster' in result_df.columns else 0
    print(f"  Processed {len(result_df)} rows in {time() - start_time:.2f} seconds ({bu_level_count} bu_level rows)")
    
    return result_df

# COMMAND ----------

# Process the comparison based on type
print(f"\n{'='*80}")
print(f"Processing: {COMPARISON_TYPE}")
print(f"{'='*80}")

if COMPARISON_TYPE == 'week_prev':
    # Week vs Previous Week
    if not latest_week_str:
        print("  Skipping - no date value available")
        comparison_info = None
    else:
        query = build_metrics_query('WEEK', 'prev_period', latest_week_str)
        data = spark.sql(query)
        print(f"Fetched {data.count()} rows")
        
        # Process the data
        processed_data = process_comparison_data(data, "Week vs Previous Week")
        
        # Get previous week by querying the date dimension
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
        prev_week_df = spark.sql(prev_week_query)
        prev_week_str = prev_week_df.toPandas().values[0][0] if prev_week_df.count() > 0 else None
        
        comparison_info = {
            'data': processed_data,
            'date_granularity': 'WEEK',
            'comparison_type': 'prev_period',
            'date_value': latest_week_str,
            'label': 'Current Week vs Previous Week',
            'current_weeks': latest_week_str,
            'prev_weeks': prev_week_str
        }

elif COMPARISON_TYPE == 'week_yoy':
    # Week vs Previous Year Week
    if not latest_week_str:
        print("  Skipping - no date value available")
        comparison_info = None
    else:
        query = build_metrics_query('WEEK', 'prev_year', latest_week_str)
        data = spark.sql(query)
        print(f"Fetched {data.count()} rows")
        
        # Process the data
        processed_data = process_comparison_data(data, "Week vs Previous Year Week")
        
        # Calculate previous year week for display
        year = int(latest_week_str.split('-W')[0])
        week_num = latest_week_str.split('-W')[1]
        prev_year_week = f"{year-1}-W{week_num}"
        
        comparison_info = {
            'data': processed_data,
            'date_granularity': 'WEEK',
            'comparison_type': 'prev_year',
            'date_value': latest_week_str,
            'label': 'Current Week vs Previous Year Week',
            'current_weeks': latest_week_str,
            'prev_weeks': prev_year_week
        }

elif COMPARISON_TYPE == 'quarter_prev':
    # Quarter vs Previous Quarter
    if not latest_13weeks_str or not prev_13weeks_list:
        print("  Skipping - no date values available")
        comparison_info = None
    else:
        # Query current weeks (current period)
        query_current = build_metrics_query('13WEEKS', 'current', latest_13weeks_str, latest_13weeks_list)
        data_current = spark.sql(query_current)
        
        # Query previous weeks (previous period) - use their current values
        query_prev = build_metrics_query('13WEEKS', 'current', prev_13weeks_str, prev_13weeks_list)
        data_prev = spark.sql(query_prev)
        print(f"  Prev {len(prev_13weeks_list)} weeks query returned {data_prev.count()} rows")
        
        # Drop any existing prev columns from data_prev
        prev_cols_to_drop = [c for c in data_prev.columns if c.startswith('prev_metric_value')]
        if prev_cols_to_drop:
            data_prev = data_prev.select([c for c in data_prev.columns if c not in prev_cols_to_drop])
        
        # Rename columns in prev data to be the "previous" values
        data_prev = data_prev.withColumnRenamed("current_metric_value_numerator", "prev_metric_value_numerator")
        data_prev = data_prev.withColumnRenamed("current_metric_value_denominator", "prev_metric_value_denominator")
        
        print(f"  Current {len(latest_13weeks_list)} weeks query returned {data_current.count()} rows")
        
        # Join and combine
        join_cols = ['reporting_cluster', 'business_unit', 'metric_final_name', 'dimension_name', 'dimension_value', 
                     'flag_more_is_good', 'flag_is_p0', 'metric_type']
        
        # Process 'Overall' reporting_cluster
        data_current_overall = data_current.filter(F.col('reporting_cluster') == 'Overall')
        data_prev_overall = data_prev.filter(F.col('reporting_cluster') == 'Overall')
        
        # Select only the columns we need from data_current
        data_current_cols = [c for c in data_current_overall.columns if c not in ['prev_metric_value_numerator', 'prev_metric_value_denominator']]
        data_current_clean = data_current_overall.select(data_current_cols)
        
        # Build select list for prev data
        select_list = []
        for c in join_cols:
            if c in data_prev_overall.columns:
                select_list.append(F.col(c))
        
        if 'prev_metric_value_numerator' in data_prev_overall.columns:
            select_list.append(F.col('prev_metric_value_numerator'))
        if 'prev_metric_value_denominator' in data_prev_overall.columns:
            select_list.append(F.col('prev_metric_value_denominator'))
        
        data_prev_selected = data_prev_overall.select(select_list)
        
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
        
        # Process 'bu_level' reporting_cluster
        data_current_bu = data_current.filter(F.col('reporting_cluster') == 'bu_level')
        data_prev_bu = data_prev.filter(F.col('reporting_cluster') == 'bu_level')
        
        current_bu_count = data_current_bu.count()
        prev_bu_count = data_prev_bu.count()
        print(f"  bu_level rows - current: {current_bu_count}, prev: {prev_bu_count}")
        
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
            
            # Union Overall and bu_level data - ensure same schema
            all_cols = data_overall.columns
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
        else:
            data = data_overall
            print(f"  Using only Overall data (no bu_level data found): {data.count()} total rows")
        
        # Fill nulls
        matched_count_before = data.filter(F.col('prev_metric_value_numerator').isNotNull()).count()
        print(f"  After join (before fillna): {data.count()} total rows, {matched_count_before} with prev values")
        
        if matched_count_before > 0:
            data = data.fillna(0, subset=['prev_metric_value_numerator', 'prev_metric_value_denominator'])
        
        # Update the comparison label
        data = data.withColumn("comparison_label", F.lit("vs Previous Period"))
        data = data.withColumn("comparison_type", F.lit('prev_period'))
        
        print(f"Fetched {data.count()} rows")
        
        # Process the data
        processed_data = process_comparison_data(data, "13-Week Period vs Previous 13-Week Period")
        
        # Store weeks information for display
        current_weeks_display = ', '.join(latest_13weeks_list) if latest_13weeks_list else None
        prev_weeks_display = ', '.join(prev_13weeks_list) if prev_13weeks_list else None
        
        comparison_info = {
            'data': processed_data,
            'date_granularity': '13WEEKS',
            'comparison_type': 'prev_period',
            'date_value': latest_13weeks_str,
            'label': '13-Week Period vs Previous 13-Week Period',
            'current_weeks': current_weeks_display,
            'prev_weeks': prev_weeks_display
        }

print(f"\n✅ Processed comparison")

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

if not country_mapping_df.empty:
    country_mapping_df['business_unit'] = country_mapping_df['business_unit'].astype(str).str.strip()
    country_mapping_df['reporting_cluster'] = country_mapping_df['reporting_cluster'].astype(str).str.strip()
    country_mapping_df = country_mapping_df[country_mapping_df['reporting_cluster'].isin(VALID_REPORTING_CLUSTERS)].copy()
    print(f"Loaded {len(country_mapping_df)} business unit mappings")
else:
    print("⚠️  WARNING: country_mapping_df is empty!")

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

# Function to write output
def write_output(comp_info, output_folder, comparison_type):
    """Write output for the comparison"""
    # Create output directory
    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    
    # Determine filename based on comparison type
    filename_map = {
        'week_prev': 'detailed_summary_week_vs_prev_week.txt',
        'week_yoy': 'detailed_summary_week_vs_prev_yr_week.txt',
        'quarter_prev': 'detailed_summary_quarter_vs_prev_quarter.txt'
    }
    filename = filename_map.get(comparison_type, f'detailed_summary_{comparison_type}.txt')
    
    detailed_summary_path = f'{output_folder}/{filename}'
    
    df = comp_info['data']
    
    with open(detailed_summary_path, 'w') as f:
        f.write(f"Steering Metrics - {comp_info['label']}\n")
        f.write("=" * 80 + "\n\n")
        
        # Write period information
        if comparison_type == 'week_prev':
            if comp_info.get('current_weeks'):
                f.write(f"Current Week: {comp_info['current_weeks']}\n")
            if comp_info.get('prev_weeks'):
                f.write(f"Previous Week: {comp_info['prev_weeks']}\n")
        elif comparison_type == 'week_yoy':
            if comp_info.get('current_weeks'):
                f.write(f"Current Week: {comp_info['current_weeks']}\n")
            if comp_info.get('prev_weeks'):
                f.write(f"Previous Year Week: {comp_info['prev_weeks']}\n")
        elif comparison_type == 'quarter_prev':
            if comp_info.get('current_weeks'):
                f.write(f"Current Quarter (13 weeks): {comp_info['current_weeks']}\n")
            if comp_info.get('prev_weeks'):
                f.write(f"Previous Quarter (13 weeks): {comp_info['prev_weeks']}\n")
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

# Generate output file
print("\n" + "="*80)
print(f"Generating Steering Metrics Report - {COMPARISON_TYPE}")
print("="*80)

start_time = time()

# Create output directory
output_folder_dir = f'{OUTPUT_BASE_FOLDER}'
if not os.path.exists(output_folder_dir):
    os.makedirs(output_folder_dir)

if 'comparison_info' in locals() and comparison_info is not None:
    print(f"\nGenerating report for {COMPARISON_TYPE}...")
    file_path = write_output(comparison_info, OUTPUT_BASE_FOLDER, COMPARISON_TYPE)
    print(f"  ✅ Generated: {file_path}")
    
    total_time = time() - start_time
    print(f"\n✅ Steering metrics generation completed!")
    print(f"Output directory: {OUTPUT_BASE_FOLDER}")
    print(f"Generated report file: {file_path}")
    print(f"Total generation time: {total_time:.2f} seconds")
else:
    print("⚠️  No comparison data available to generate report")

# COMMAND ----------

# Download the file to DBFS
if 'file_path' in locals() and os.path.exists(file_path):
    filename = os.path.basename(file_path)
    output_file_path = f"/tmp/{filename}"
    with open(file_path, 'r') as f:
        content = f.read()
    dbutils.fs.put(output_file_path, content, overwrite=True)
    print(f"\n{filename} written to DBFS: {output_file_path}")
    print(f"Local path: {file_path}")
else:
    print(f"Error: Could not find report file")

