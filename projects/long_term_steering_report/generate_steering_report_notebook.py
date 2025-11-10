# Databricks notebook source
# MAGIC %md
# MAGIC # Generate Steering Report from Source
# MAGIC 
# MAGIC This notebook generates a steering report directly from `payments_hf.payments_p0_metrics` table
# MAGIC following the REPORT_PROMPT_V2.md format.
# MAGIC 
# MAGIC It queries the data for all three comparison types (week_prev, week_yoy, quarter_prev) and
# MAGIC generates a comprehensive steering report.

# COMMAND ----------

# Import required libraries
import pyspark.sql.functions as F
from pyspark.sql.types import DoubleType
import math
from time import time
import os
import errno

# Import functions from the main notebook
# (These would need to be available in the same notebook or imported)
# For now, we'll include the necessary functions inline

# COMMAND ----------

# Configuration
VALID_REPORTING_CLUSTERS = ['HF-NA', 'HF-INTL', 'RTE', 'WL', 'Overall']
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

# COMMAND ----------

# Get latest week and periods
print("Getting latest reporting periods...")
start_time = time()

# Get latest complete week
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

# Get previous week
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

# Get previous year week
year = int(latest_week_str.split('-W')[0])
week_num = latest_week_str.split('-W')[1]
prev_year_week_str = f"{year-1}-W{week_num}"

# Get latest 13 weeks
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

# Get previous 13 weeks
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
print(f"Time to get latest dates: {time() - start_time:.2f} seconds")

# COMMAND ----------

# Refresh tables
print("Refreshing tables...")
spark.sql("REFRESH TABLE payments_hf.payments_p0_metrics")
spark.sql("REFRESH TABLE payments_hf.business_units")

# COMMAND ----------

# Import the build_metrics_query and process_comparison_data functions
# These should be available from the main notebook or we need to include them here
# For now, we'll reference the existing notebook's functions

# COMMAND ----------

# Query data for all three comparison types
print("\n" + "="*80)
print("Querying data for all comparison types...")
print("="*80)

# Week vs Prev Week
print("\n1. Week vs Previous Week...")
week_prev_query = build_metrics_query('WEEK', 'prev_period', latest_week_str)
week_prev_data = spark.sql(week_prev_query)
week_prev_processed = process_comparison_data(week_prev_data, "Week vs Previous Week")
print(f"   Processed {len(week_prev_processed)} rows")

# Week vs Prev Year Week
print("\n2. Week vs Previous Year Week...")
week_yoy_query = build_metrics_query('WEEK', 'prev_year', latest_week_str)
week_yoy_data = spark.sql(week_yoy_query)
week_yoy_processed = process_comparison_data(week_yoy_data, "Week vs Previous Year Week")
print(f"   Processed {len(week_yoy_processed)} rows")

# Quarter vs Prev Quarter
print("\n3. Quarter vs Previous Quarter...")
# Query current period
query_current = build_metrics_query('13WEEKS', 'current', latest_13weeks_str, latest_13weeks_list)
data_current = spark.sql(query_current)

# Query previous period
query_prev = build_metrics_query('13WEEKS', 'current', prev_13weeks_str, prev_13weeks_list)
data_prev = spark.sql(query_prev)

# Process quarter comparison (similar to the main notebook logic)
data_prev = data_prev.withColumnRenamed("current_metric_value_numerator", "prev_metric_value_numerator")
data_prev = data_prev.withColumnRenamed("current_metric_value_denominator", "prev_metric_value_denominator")

join_cols = ['reporting_cluster', 'business_unit', 'metric_final_name', 'dimension_name', 'dimension_value', 
             'flag_more_is_good', 'flag_is_p0', 'metric_type']

data_current_clean = data_current.select([c for c in data_current.columns if c not in ['prev_metric_value_numerator', 'prev_metric_value_denominator']])
data_prev_selected = data_prev.select(join_cols + ['prev_metric_value_numerator', 'prev_metric_value_denominator'])

# Cast to ensure consistent types
for col in join_cols:
    if col in data_current_clean.columns and col in data_prev_selected.columns:
        data_current_clean = data_current_clean.withColumn(col, F.col(col).cast('string'))
        data_prev_selected = data_prev_selected.withColumn(col, F.col(col).cast('string'))

data_combined = data_current_clean.join(data_prev_selected, on=join_cols, how='left')
data_combined = data_combined.fillna(0, subset=['prev_metric_value_numerator', 'prev_metric_value_denominator'])

quarter_prev_processed = process_comparison_data(data_combined, "Quarter vs Previous Quarter")
print(f"   Processed {len(quarter_prev_processed)} rows")

# COMMAND ----------

# Generate steering report
print("\n" + "="*80)
print("Generating Steering Report...")
print("="*80)

def format_arrow(rel_change):
    """Return arrow based on relative change"""
    return '↑' if rel_change > 0 else '↓'

def format_significance(sig_level):
    """Format significance"""
    return 'significant' if sig_level >= 3 else 'not significant'

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
                parts.append(f"- **{cluster}**: {row['prev_ratio']*100:.2f}% to {row['current_ratio']*100:.2f}% ({arrow}{abs(row['relative_change_pct']):.2f}%, {sig}, volume: {volume})")
        
        # Deep Insights - top business units
        parts.append("<br><br>**Deep Insights**")
        insights = []
        for cluster in ['Overall', 'HF-NA', 'HF-INTL', 'RTE', 'WL']:
            cluster_data = week_prev_df[week_prev_df['reporting_cluster'] == cluster]
            if not cluster_data.empty and 'business_unit' in cluster_data.columns:
                bu_data = cluster_data[cluster_data['business_unit'].notna() & (cluster_data['business_unit'] != 'Null')]
                if not bu_data.empty:
                    top_bu = bu_data.nlargest(3, 'relative_change_pct', keep='all')
                    for _, bu_row in top_bu.iterrows():
                        arrow = format_arrow(bu_row['relative_change_pct'])
                        volume = format_number(bu_row.get('current_metric_value_denominator', 0) * abs(bu_row['relative_change_pct']) / 100)
                        insights.append(f"- **{cluster}** {bu_row['business_unit']}: {bu_row['prev_ratio']*100:.2f}% to {bu_row['current_ratio']*100:.2f}% ({arrow}{abs(bu_row['relative_change_pct']):.2f}%, volume: {volume})")
        
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
                parts.append("<br><br>**Long Term Impact**")
                parts.append(f"- **Current Quarter vs Prev Quarter**: {row['prev_ratio']*100:.2f}% to {row['current_ratio']*100:.2f}% ({arrow}{abs(row['relative_change_pct']):.2f}%, volume: {volume})")
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
                parts.append("<br><br>**Comparison vs Prev Year**")
                parts.append(f"- **Current Week vs Prev Year Week**: {row['prev_ratio']*100:.2f}% to {row['current_ratio']*100:.2f}% ({arrow}{abs(row['relative_change_pct']):.2f}%, volume: {volume})")
            else:
                parts.append("<br><br>**Comparison vs Prev Year**<br>- No significant year-over-year impact (all changes <10%)")
        else:
            parts.append("<br><br>**Comparison vs Prev Year**<br>- No significant year-over-year impact (all changes <10%)")
    else:
        parts.append("<br><br>**Comparison vs Prev Year**<br>- No significant year-over-year impact (all changes <10%)")
    
    return "<br>".join(parts)

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

# Generate report
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
WORKSPACE_FOLDER = '/Workspace/Users/visal.kumar@hellofresh.com'
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

