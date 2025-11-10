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

# Quarter vs Prev Quarter
print("\n3. Processing Quarter vs Previous Quarter...")
query_current = build_metrics_query('13WEEKS', 'current', latest_13weeks_str, latest_13weeks_list)
data_current = spark.sql(query_current)

query_prev = build_metrics_query('13WEEKS', 'current', prev_13weeks_str, prev_13weeks_list)
data_prev = spark.sql(query_prev)

# Process quarter comparison
data_prev = data_prev.withColumnRenamed("current_metric_value_numerator", "prev_metric_value_numerator")
data_prev = data_prev.withColumnRenamed("current_metric_value_denominator", "prev_metric_value_denominator")

join_cols = ['reporting_cluster', 'business_unit', 'metric_final_name', 'dimension_name', 'dimension_value', 
             'flag_more_is_good', 'flag_is_p0', 'metric_type']

data_current_clean = data_current.select([c for c in data_current.columns if c not in ['prev_metric_value_numerator', 'prev_metric_value_denominator']])
data_prev_selected = data_prev.select(join_cols + ['prev_metric_value_numerator', 'prev_metric_value_denominator'])

for col in join_cols:
    if col in data_current_clean.columns and col in data_prev_selected.columns:
        data_current_clean = data_current_clean.withColumn(col, F.col(col).cast('string'))
        data_prev_selected = data_prev_selected.withColumn(col, F.col(col).cast('string'))

data_combined = data_current_clean.join(data_prev_selected, on=join_cols, how='left')
data_combined = data_combined.fillna(0, subset=['prev_metric_value_numerator', 'prev_metric_value_denominator'])

quarter_prev_processed = process_comparison_data(data_combined, "Quarter vs Previous Quarter")
print(f"   Processed {len(quarter_prev_processed)} rows")

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

# Build callout for a metric
def build_callout_for_metric(metric_full_name, week_prev_df, week_yoy_df, quarter_prev_df):
    """Build callout text for a metric"""
    parts = []
    
    # Week vs Prev Week
    if week_prev_df is not None and not week_prev_df.empty:
        parts.append("**Current Week vs Prev Week:**")
        
        for cluster in ['Overall', 'HF-NA', 'HF-INTL', 'RTE', 'WL']:
            cluster_data = week_prev_df[week_prev_df['reporting_cluster'] == cluster]
            if not cluster_data.empty:
                row = cluster_data.iloc[0]
                arrow = format_arrow(row['relative_change_pct'])
                sig = format_significance(row.get('significance_level', 0))
                volume = format_number(row.get('current_metric_value_denominator', 0) * abs(row['relative_change_pct']) / 100)
                prev_pct = row['prev_ratio'] * 100 if row['metric_type'] == 'ratio' else row['prev_ratio']
                curr_pct = row['current_ratio'] * 100 if row['metric_type'] == 'ratio' else row['current_ratio']
                
                if row['metric_type'] == 'ratio':
                    parts.append(f"- **{cluster}**: {prev_pct:.2f}% to {curr_pct:.2f}% ({arrow}{abs(row['relative_change_pct']):.2f}%, {sig}, volume: {volume})")
                else:
                    parts.append(f"- **{cluster}**: €{prev_pct:.2f} to €{curr_pct:.2f} ({arrow}{abs(row['relative_change_pct']):.2f}%, {sig}, volume: {volume})")
        
        # Deep Insights - top business units
        parts.append("<br><br>**Deep Insights**")
        insights = []
        for cluster in ['Overall', 'HF-NA', 'HF-INTL', 'RTE', 'WL']:
            cluster_data = week_prev_df[week_prev_df['reporting_cluster'] == cluster]
            if not cluster_data.empty:
                # Get business units for this cluster
                if cluster != 'Overall':
                    rc_bu = country_mapping_df[country_mapping_df['reporting_cluster'] == cluster].business_unit.tolist()
                    bu_data = week_prev_df[(week_prev_df['business_unit'].isin(rc_bu)) & 
                                          (week_prev_df['metric_final_name'] == metric_full_name)]
                else:
                    bu_data = week_prev_df[(week_prev_df['reporting_cluster'] == 'bu_level') & 
                                          (week_prev_df['metric_final_name'] == metric_full_name)]
                
                if not bu_data.empty:
                    bu_data = bu_data.copy()
                    bu_data.loc[:, 'abs_rel_change'] = abs(bu_data['relative_change_pct'])
                    top_bu = bu_data.nlargest(3, 'abs_rel_change', keep='all')
                    for _, bu_row in top_bu.iterrows():
                        arrow = format_arrow(bu_row['relative_change_pct'])
                        volume = format_number(bu_row.get('current_metric_value_denominator', 0) * abs(bu_row['relative_change_pct']) / 100)
                        prev_pct = bu_row['prev_ratio'] * 100 if bu_row['metric_type'] == 'ratio' else bu_row['prev_ratio']
                        curr_pct = bu_row['current_ratio'] * 100 if bu_row['metric_type'] == 'ratio' else bu_row['current_ratio']
                        
                        if bu_row['metric_type'] == 'ratio':
                            insights.append(f"- **{cluster}** {bu_row['business_unit']}: {prev_pct:.2f}% to {curr_pct:.2f}% ({arrow}{abs(bu_row['relative_change_pct']):.2f}%, volume: {volume})")
                        else:
                            insights.append(f"- **{cluster}** {bu_row['business_unit']}: €{prev_pct:.2f} to €{curr_pct:.2f} ({arrow}{abs(bu_row['relative_change_pct']):.2f}%, volume: {volume})")
        
        if insights:
            parts.extend(insights[:5])
        else:
            parts.append("- No significant business unit insights")
    
    # Long Term Impact (Quarter)
    if quarter_prev_df is not None and not quarter_prev_df.empty:
        overall_q = quarter_prev_df[quarter_prev_df['reporting_cluster'] == 'Overall']
        if not overall_q.empty:
            row = overall_q.iloc[0]
            if abs(row['relative_change_pct']) > 10:
                arrow = format_arrow(row['relative_change_pct'])
                volume = format_number(row.get('current_metric_value_denominator', 0) * abs(row['relative_change_pct']) / 100)
                prev_pct = row['prev_ratio'] * 100 if row['metric_type'] == 'ratio' else row['prev_ratio']
                curr_pct = row['current_ratio'] * 100 if row['metric_type'] == 'ratio' else row['current_ratio']
                
                parts.append("<br><br>**Long Term Impact**")
                if row['metric_type'] == 'ratio':
                    parts.append(f"- **Current Quarter vs Prev Quarter**: {prev_pct:.2f}% to {curr_pct:.2f}% ({arrow}{abs(row['relative_change_pct']):.2f}%, volume: {volume})")
                else:
                    parts.append(f"- **Current Quarter vs Prev Quarter**: €{prev_pct:.2f} to €{curr_pct:.2f} ({arrow}{abs(row['relative_change_pct']):.2f}%, volume: {volume})")
            else:
                parts.append("<br><br>**Long Term Impact**<br>- No significant long-term impact (all changes <10%)")
        else:
            parts.append("<br><br>**Long Term Impact**<br>- No significant long-term impact (all changes <10%)")
    else:
        parts.append("<br><br>**Long Term Impact**<br>- No significant long-term impact (all changes <10%)")
    
    # Comparison vs Prev Year
    if week_yoy_df is not None and not week_yoy_df.empty:
        overall_yoy = week_yoy_df[week_yoy_df['reporting_cluster'] == 'Overall']
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

week_num = latest_week_str.split('-W')[1] if latest_week_str else 'XX'
report = f"# {latest_week_str} Weekly Payments Metrics Steering\n\n"
report += "## Key Insights\n"
report += generate_key_insights(week_prev_processed, week_yoy_processed, quarter_prev_processed)
report += "\n\n"
report += "| Metrics | Anomaly/Callout | Notes |\n"
report += "| :--- | :--- | :--- |\n"

# Add each metric
for metric_display, metric_full in METRIC_GROUPS:
    # Filter dataframes for this metric
    week_prev_metric = week_prev_processed[week_prev_processed['metric_final_name'] == metric_full] if week_prev_processed is not None and not week_prev_processed.empty else None
    week_yoy_metric = week_yoy_processed[week_yoy_processed['metric_final_name'] == metric_full] if week_yoy_processed is not None and not week_yoy_processed.empty else None
    quarter_prev_metric = quarter_prev_processed[quarter_prev_processed['metric_final_name'] == metric_full] if quarter_prev_processed is not None and not quarter_prev_processed.empty else None
    
    callout = build_callout_for_metric(metric_full, week_prev_metric, week_yoy_metric, quarter_prev_metric)
    
    # Truncate if too long
    if len(callout) > 1000:
        callout = callout[:997] + "..."
    
    report += f"| **{metric_display}** | {callout} | |\n"

# COMMAND ----------

# Write output
OUTPUT_BASE_FOLDER = f'{WORKSPACE_FOLDER}/long-term-steering-{latest_week_str if latest_week_str else "unknown"}'

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
