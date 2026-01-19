# Databricks notebook source
# MAGIC %md
# MAGIC # Analyze Thresholds for All Metrics
# MAGIC 
# MAGIC This notebook analyzes historical trends and calculates data-driven thresholds for all steering metrics.
# MAGIC It shows thresholds for each metric and comparison type using different methods.

# COMMAND ----------

# Import required libraries
import pyspark.sql.functions as F
from pyspark.sql.types import DoubleType
import pandas as pd
import sys
from io import StringIO

# COMMAND ----------

# Configuration - same as main notebook
SPECIAL_METRICS = ['0_ShipRate', '1_RecoveryW0', '2_Recovery_12wkCohort', '3_DunningAvgNetProfit_12wkCohort']

# Metric groups in order
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

AR_METRICS = [
    '3_Active - 1_1_Overall Total Box Candidates - 2_PreDunningAR',
    '3_Active - 1_2_Loyalty: LL0 (Initial charges) - 2_PreDunningAR',
    '3_Active - 1_3_Loyalty: LL0 and LL1+ (Recurring charges) - 2_PreDunningAR'
]

# Number of historical weeks to analyze
HISTORICAL_WEEKS_FOR_ANALYSIS = 52

# COMMAND ----------

def get_historical_metric_data(metric_full_name, num_weeks=52):
    """Get historical metric data at Overall level for trend analysis."""
    try:
        # Extract metric components from metric_final_name
        parts = metric_full_name.split(' - ')
        if len(parts) < 3:
            print(f"[ERROR] Could not parse metric name: {metric_full_name}")
            return pd.DataFrame()
        
        focus_group = parts[0]
        metric_group = parts[1]
        metric_name = parts[2]
        
        # Build query to get historical data at Overall level
        historical_query = f"""
        SELECT 
            a.date_value,
            CASE 
                WHEN a.current_metric_value_denominator > 0 
                THEN a.current_metric_value_numerator / a.current_metric_value_denominator
                ELSE 0 
            END AS metric_value,
            a.current_metric_value_numerator,
            a.current_metric_value_denominator
        FROM payments_hf.payments_p0_metrics a
        WHERE 1=1
            AND a.focus_group = '{focus_group}'
            AND a.metric_group = '{metric_group}'
            AND a.metric_name = '{metric_name}'
            AND a.metric_type IN ('ratio', 'dollar-ratio')
            AND a.flag_is_p0 = 'TRUE'
            AND a.date_granularity = 'WEEK'
            AND a.reporting_cluster = 'Overall'
            AND (
                (a.metric_name not IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])})) 
                OR (a.metric_name IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])}) AND a.dimension_value in ('Good'))
            )
            AND (
                (a.metric_name not IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])}) AND a.dimension_name = '_Overall')
                OR (a.metric_name IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])}) AND a.dimension_value = 'Good')
            )
            AND DATE(a.date_string_backwards) < CURRENT_DATE()
        ORDER BY a.date_value DESC
        LIMIT {num_weeks}
        """
        
        result_df = spark.sql(historical_query).toPandas()
        
        if result_df.empty:
            return pd.DataFrame()
        
        # Calculate week-over-week changes
        result_df = result_df.sort_values('date_value')
        result_df['prev_metric_value'] = result_df['metric_value'].shift(1)
        result_df['week_over_week_change_pct'] = (
            (result_df['metric_value'] - result_df['prev_metric_value']) / 
            result_df['prev_metric_value'] * 100
        ).fillna(0)
        result_df['abs_week_over_week_change_pct'] = result_df['week_over_week_change_pct'].abs()
        
        return result_df
        
    except Exception as e:
        print(f"[ERROR] Error getting historical data for {metric_full_name}: {e}")
        return pd.DataFrame()

def calculate_threshold_std_dev(historical_df, std_dev_multiplier=2.0):
    """Calculate threshold based on standard deviation."""
    if historical_df.empty or 'abs_week_over_week_change_pct' not in historical_df.columns:
        return None
    
    changes = historical_df['abs_week_over_week_change_pct'].dropna()
    
    if len(changes) < 10:
        return None
    
    mean_change = changes.mean()
    std_dev = changes.std()
    threshold = mean_change + (std_dev_multiplier * std_dev)
    
    return max(threshold, 1.0)

def calculate_threshold_percentile(historical_df, percentile=95):
    """Calculate threshold based on percentile."""
    if historical_df.empty or 'abs_week_over_week_change_pct' not in historical_df.columns:
        return None
    
    changes = historical_df['abs_week_over_week_change_pct'].dropna()
    
    if len(changes) < 10:
        return None
    
    threshold = changes.quantile(percentile / 100.0)
    return max(threshold, 1.0)

def calculate_threshold_z_score(historical_df, z_score_threshold=2.576):
    """Calculate threshold based on z-score."""
    if historical_df.empty or 'abs_week_over_week_change_pct' not in historical_df.columns:
        return None
    
    changes = historical_df['abs_week_over_week_change_pct'].dropna()
    
    if len(changes) < 10:
        return None
    
    mean_change = changes.mean()
    std_dev = changes.std()
    
    if std_dev == 0:
        return max(mean_change, 1.0)
    
    threshold = mean_change + (z_score_threshold * std_dev)
    return max(threshold, 1.0)

def calculate_threshold_combined(historical_df, method='hybrid'):
    """Calculate threshold using a combination of methods."""
    std_dev_threshold = calculate_threshold_std_dev(historical_df, std_dev_multiplier=2.0)
    percentile_threshold = calculate_threshold_percentile(historical_df, percentile=95)
    
    if std_dev_threshold is None and percentile_threshold is None:
        return None
    
    if std_dev_threshold is None:
        return percentile_threshold
    
    if percentile_threshold is None:
        return std_dev_threshold
    
    if method == 'conservative':
        return max(std_dev_threshold, percentile_threshold)
    elif method == 'aggressive':
        return min(std_dev_threshold, percentile_threshold)
    else:  # hybrid - average
        return (std_dev_threshold + percentile_threshold) / 2.0

def get_fixed_threshold(metric_full_name, comparison_type):
    """Get fixed threshold (original logic)."""
    is_ar = metric_full_name in AR_METRICS
    
    if is_ar:
        return 5
    else:
        if comparison_type == 'week_prev':
            return 10
        elif comparison_type in ['long_term', 'yoy']:
            return 20
        else:
            return 10

def analyze_metric_thresholds(metric_full_name, metric_display_name):
    """Analyze thresholds for a single metric using all methods."""
    print(f"\n{'='*80}")
    print(f"Analyzing: {metric_display_name}")
    print(f"Metric: {metric_full_name}")
    print(f"{'='*80}")
    
    # Get historical data
    historical_df = get_historical_metric_data(metric_full_name, HISTORICAL_WEEKS_FOR_ANALYSIS)
    
    if historical_df.empty:
        print(f"⚠️  No historical data found")
        return None
    
    print(f"✅ Retrieved {len(historical_df)} weeks of historical data")
    
    # Calculate statistics
    changes = historical_df['abs_week_over_week_change_pct'].dropna()
    if len(changes) < 10:
        print(f"⚠️  Insufficient data points ({len(changes)} < 10)")
        return None
    
    mean_change = changes.mean()
    std_dev = changes.std()
    median_change = changes.median()
    p95_change = changes.quantile(0.95)
    p99_change = changes.quantile(0.99)
    
    print(f"\n📊 Historical Change Statistics:")
    print(f"   Mean: {mean_change:.2f}%")
    print(f"   Median: {median_change:.2f}%")
    print(f"   Std Dev: {std_dev:.2f}%")
    print(f"   95th Percentile: {p95_change:.2f}%")
    print(f"   99th Percentile: {p99_change:.2f}%")
    
    # Calculate thresholds for each method
    thresholds = {}
    
    # Week-over-week thresholds
    std_dev_wow = calculate_threshold_std_dev(historical_df, 2.0)
    percentile_wow = calculate_threshold_percentile(historical_df, 95)
    z_score_wow = calculate_threshold_z_score(historical_df, 2.576)
    hybrid_wow = calculate_threshold_combined(historical_df, 'hybrid')
    conservative_wow = calculate_threshold_combined(historical_df, 'conservative')
    aggressive_wow = calculate_threshold_combined(historical_df, 'aggressive')
    
    # Long-term thresholds (1.5x week-over-week)
    std_dev_lt = std_dev_wow * 1.5 if std_dev_wow else None
    percentile_lt = percentile_wow * 1.5 if percentile_wow else None
    z_score_lt = z_score_wow * 1.5 if z_score_wow else None
    hybrid_lt = hybrid_wow * 1.5 if hybrid_wow else None
    conservative_lt = conservative_wow * 1.5 if conservative_wow else None
    aggressive_lt = aggressive_wow * 1.5 if aggressive_wow else None
    
    # Fixed thresholds
    fixed_wow = get_fixed_threshold(metric_full_name, 'week_prev')
    fixed_lt = get_fixed_threshold(metric_full_name, 'long_term')
    
    print(f"\n📈 Calculated Thresholds:")
    print(f"\n   Week-over-Week (Current vs Prev Week):")
    print(f"      Fixed (current):        {fixed_wow:.1f}%")
    if std_dev_wow:
        print(f"      Std Dev (2σ):           {std_dev_wow:.1f}%")
    if percentile_wow:
        print(f"      Percentile (95th):      {percentile_wow:.1f}%")
    if z_score_wow:
        print(f"      Z-Score (99%):          {z_score_wow:.1f}%")
    if hybrid_wow:
        print(f"      Hybrid (avg):           {hybrid_wow:.1f}%")
    if conservative_wow:
        print(f"      Conservative (max):     {conservative_wow:.1f}%")
    if aggressive_wow:
        print(f"      Aggressive (min):       {aggressive_wow:.1f}%")
    
    print(f"\n   Long-Term (Quarter vs Prev Quarter):")
    print(f"      Fixed (current):        {fixed_lt:.1f}%")
    if std_dev_lt:
        print(f"      Std Dev (2σ):           {std_dev_lt:.1f}%")
    if percentile_lt:
        print(f"      Percentile (95th):      {percentile_lt:.1f}%")
    if z_score_lt:
        print(f"      Z-Score (99%):          {z_score_lt:.1f}%")
    if hybrid_lt:
        print(f"      Hybrid (avg):           {hybrid_lt:.1f}%")
    if conservative_lt:
        print(f"      Conservative (max):     {conservative_lt:.1f}%")
    if aggressive_lt:
        print(f"      Aggressive (min):       {aggressive_lt:.1f}%")
    
    return {
        'metric_display': metric_display_name,
        'metric_full': metric_full_name,
        'weeks_analyzed': len(historical_df),
        'mean_change': mean_change,
        'std_dev': std_dev,
        'p95_change': p95_change,
        'fixed_wow': fixed_wow,
        'fixed_lt': fixed_lt,
        'std_dev_wow': std_dev_wow,
        'percentile_wow': percentile_wow,
        'z_score_wow': z_score_wow,
        'hybrid_wow': hybrid_wow,
        'conservative_wow': conservative_wow,
        'aggressive_wow': aggressive_wow,
        'std_dev_lt': std_dev_lt,
        'percentile_lt': percentile_lt,
        'z_score_lt': z_score_lt,
        'hybrid_lt': hybrid_lt,
        'conservative_lt': conservative_lt,
        'aggressive_lt': aggressive_lt
    }

# COMMAND ----------

# Analyze all metrics
print("="*80)
print("THRESHOLD ANALYSIS FOR ALL METRICS")
print("="*80)
print(f"\nAnalyzing {len(METRIC_GROUPS)} metrics using {HISTORICAL_WEEKS_FOR_ANALYSIS} weeks of historical data...")

results = []
for metric_display, metric_full in METRIC_GROUPS:
    result = analyze_metric_thresholds(metric_full, metric_display)
    if result:
        results.append(result)

# COMMAND ----------

# Create summary table
if results:
    print("\n" + "="*80)
    print("SUMMARY TABLE: Week-over-Week Thresholds")
    print("="*80)
    
    summary_data = []
    for r in results:
        summary_data.append({
            'Metric': r['metric_display'],
            'Fixed': f"{r['fixed_wow']:.1f}%",
            'Std Dev': f"{r['std_dev_wow']:.1f}%" if r['std_dev_wow'] else 'N/A',
            'Percentile': f"{r['percentile_wow']:.1f}%" if r['percentile_wow'] else 'N/A',
            'Z-Score': f"{r['z_score_wow']:.1f}%" if r['z_score_wow'] else 'N/A',
            'Hybrid': f"{r['hybrid_wow']:.1f}%" if r['hybrid_wow'] else 'N/A',
            'Conservative': f"{r['conservative_wow']:.1f}%" if r['conservative_wow'] else 'N/A',
            'Aggressive': f"{r['aggressive_wow']:.1f}%" if r['aggressive_wow'] else 'N/A',
            'Mean Change': f"{r['mean_change']:.2f}%",
            'Std Dev': f"{r['std_dev']:.2f}%",
            '95th Pct': f"{r['p95_change']:.2f}%"
        })
    
    summary_df = pd.DataFrame(summary_data)
    print(summary_df.to_string(index=False))
    
    print("\n" + "="*80)
    print("SUMMARY TABLE: Long-Term Thresholds")
    print("="*80)
    
    summary_data_lt = []
    for r in results:
        summary_data_lt.append({
            'Metric': r['metric_display'],
            'Fixed': f"{r['fixed_lt']:.1f}%",
            'Std Dev': f"{r['std_dev_lt']:.1f}%" if r['std_dev_lt'] else 'N/A',
            'Percentile': f"{r['percentile_lt']:.1f}%" if r['percentile_lt'] else 'N/A',
            'Z-Score': f"{r['z_score_lt']:.1f}%" if r['z_score_lt'] else 'N/A',
            'Hybrid': f"{r['hybrid_lt']:.1f}%" if r['hybrid_lt'] else 'N/A',
            'Conservative': f"{r['conservative_lt']:.1f}%" if r['conservative_lt'] else 'N/A',
            'Aggressive': f"{r['aggressive_lt']:.1f}%" if r['aggressive_lt'] else 'N/A'
        })
    
    summary_df_lt = pd.DataFrame(summary_data_lt)
    print(summary_df_lt.to_string(index=False))
    
    # Save to CSV files (both local and DBFS)
    output_path = '/tmp/threshold_analysis_summary.csv'
    summary_df.to_csv(output_path, index=False)
    print(f"\n✅ Summary saved to: {output_path}")
    
    # Also save to DBFS
    summary_csv_content = summary_df.to_csv(index=False)
    dbutils.fs.put('/tmp/threshold_analysis_summary.csv', summary_csv_content, overwrite=True)
    print(f"✅ Summary also saved to DBFS: /tmp/threshold_analysis_summary.csv")
    
    # Also save detailed results
    detailed_df = pd.DataFrame(results)
    detailed_path = '/tmp/threshold_analysis_detailed.csv'
    detailed_df.to_csv(detailed_path, index=False)
    print(f"✅ Detailed results saved to: {detailed_path}")
    
    # Also save to DBFS
    detailed_csv_content = detailed_df.to_csv(index=False)
    dbutils.fs.put('/tmp/threshold_analysis_detailed.csv', detailed_csv_content, overwrite=True)
    print(f"✅ Detailed results also saved to DBFS: /tmp/threshold_analysis_detailed.csv")
    
    # Create a formatted text report
    report_lines = []
    report_lines.append("="*80)
    report_lines.append("THRESHOLD ANALYSIS REPORT")
    report_lines.append("="*80)
    report_lines.append(f"\nGenerated: {pd.Timestamp.now()}")
    report_lines.append(f"Metrics Analyzed: {len(results)}")
    report_lines.append(f"Historical Weeks: {HISTORICAL_WEEKS_FOR_ANALYSIS}")
    report_lines.append("\n" + "="*80)
    report_lines.append("WEEK-OVER-WEEK THRESHOLDS")
    report_lines.append("="*80)
    report_lines.append(summary_df.to_string(index=False))
    report_lines.append("\n" + "="*80)
    report_lines.append("LONG-TERM THRESHOLDS")
    report_lines.append("="*80)
    report_lines.append(summary_df_lt.to_string(index=False))
    
    report_content = "\n".join(report_lines)
    
    # Save report to DBFS
    dbutils.fs.put('/tmp/threshold_analysis_report.txt', report_content, overwrite=True)
    print(f"\n✅ Full report saved to DBFS: /tmp/threshold_analysis_report.txt")
    
    # Also save to DBFS in a location that's easier to access
    # Use dbfs:/ prefix for absolute path
    dbutils.fs.put('dbfs:/tmp/threshold_analysis_report.txt', report_content, overwrite=True)
    print(f"✅ Full report saved to DBFS: dbfs:/tmp/threshold_analysis_report.txt")
    
    # Also print the full report
    print("\n" + report_content)
else:
    print("\n⚠️  No results to display")


