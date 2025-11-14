#!/usr/bin/env python3
"""
Local script to analyze thresholds by querying Databricks directly.
This shows thresholds immediately without needing to run a Databricks job.
"""
import sys
import os
import pandas as pd
import numpy as np
from pathlib import Path

# Add cursor_databricks directory to path
cursor_databricks_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_dir)

from databricks_api import DatabricksAPI

# Configuration
SPECIAL_METRICS = ['0_ShipRate', '1_RecoveryW0', '2_Recovery_12wkCohort', '3_DunningAvgNetProfit_12wkCohort']

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

HISTORICAL_WEEKS = 52

def get_historical_data(db, metric_full_name, num_weeks=52):
    """Get historical metric data from Databricks."""
    parts = metric_full_name.split(' - ')
    if len(parts) < 3:
        return pd.DataFrame()
    
    focus_group = parts[0]
    metric_group = parts[1]
    metric_name = parts[2]
    
    query = f"""
    SELECT 
        a.date_value,
        CASE 
            WHEN a.current_metric_value_denominator > 0 
            THEN a.current_metric_value_numerator / a.current_metric_value_denominator
            ELSE 0 
        END AS metric_value
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
    ORDER BY a.date_value DESC
    LIMIT {num_weeks}
    """
    
    try:
        result = db.run_sql(query, display=False)
        if result and len(result) > 0:
            # Convert result to DataFrame
            # result is a list of Row objects or tuples
            if hasattr(result[0], '__fields__'):
                # It's a Row object with named fields
                columns = list(result[0].__fields__)
                data = [[getattr(row, col) for col in columns] for row in result]
                df = pd.DataFrame(data, columns=columns)
            else:
                # It's a list of tuples or dicts
                df = pd.DataFrame(result)
                if 'date_value' not in df.columns and len(df.columns) >= 2:
                    df.columns = ['date_value', 'metric_value']
            
            if 'date_value' in df.columns:
                df = df.sort_values('date_value')
                df['prev_metric_value'] = df['metric_value'].shift(1)
                df['week_over_week_change_pct'] = (
                    (df['metric_value'] - df['prev_metric_value']) / 
                    df['prev_metric_value'] * 100
                ).fillna(0)
                df['abs_week_over_week_change_pct'] = df['week_over_week_change_pct'].abs()
                return df
    except Exception as e:
        print(f"Error querying {metric_full_name}: {e}")
        import traceback
        traceback.print_exc()
    
    return pd.DataFrame()

def calculate_thresholds(historical_df):
    """Calculate thresholds using different methods."""
    if historical_df.empty or 'abs_week_over_week_change_pct' not in historical_df.columns:
        return {}
    
    changes = historical_df['abs_week_over_week_change_pct'].dropna()
    
    if len(changes) < 10:
        return {}
    
    # Filter out infinite and extremely large values (likely data issues)
    changes = changes[changes != np.inf]
    changes = changes[changes < 10000]  # Filter out values > 10000%
    
    if len(changes) < 10:
        return {}
    
    mean_change = changes.mean()
    std_dev = changes.std()
    p95 = changes.quantile(0.95)
    
    # Handle edge cases
    if np.isnan(mean_change) or np.isinf(mean_change):
        mean_change = 0
    if np.isnan(std_dev) or np.isinf(std_dev):
        std_dev = 0
    if np.isnan(p95) or np.isinf(p95):
        p95 = 100  # Default high threshold
    
    std_dev_2sigma = mean_change + (2.0 * std_dev) if not np.isnan(std_dev) else p95
    z_score_99 = mean_change + (2.576 * std_dev) if std_dev > 0 and not np.isnan(std_dev) else p95
    hybrid = (std_dev_2sigma + p95) / 2.0 if not (np.isnan(std_dev_2sigma) or np.isnan(p95)) else p95
    
    # Cap thresholds at reasonable maximum (1000%)
    std_dev_2sigma = min(std_dev_2sigma, 1000) if not np.isnan(std_dev_2sigma) else p95
    z_score_99 = min(z_score_99, 1000) if not np.isnan(z_score_99) else p95
    hybrid = min(hybrid, 1000) if not np.isnan(hybrid) else p95
    
    thresholds = {
        'mean': mean_change,
        'std_dev': std_dev,
        'p95': p95,
        'std_dev_2sigma': std_dev_2sigma,
        'percentile_95': p95,
        'z_score_99': z_score_99,
        'hybrid': hybrid
    }
    
    return thresholds

def get_fixed_threshold(metric_full_name, comparison_type):
    """Get fixed threshold."""
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

def main():
    print("="*80)
    print("THRESHOLD ANALYSIS FOR ALL METRICS")
    print("="*80)
    print(f"\nAnalyzing {len(METRIC_GROUPS)} metrics using {HISTORICAL_WEEKS} weeks of historical data...")
    print("Connecting to Databricks...\n")
    
    db = DatabricksAPI()
    
    results = []
    
    for metric_display, metric_full in METRIC_GROUPS:
        print(f"\n{'='*80}")
        print(f"Analyzing: {metric_display}")
        print(f"Metric: {metric_full}")
        print(f"{'='*80}")
        
        # Get historical data
        historical_df = get_historical_data(db, metric_full, HISTORICAL_WEEKS)
        
        if historical_df.empty:
            print(f"⚠️  No historical data found")
            continue
        
        print(f"✅ Retrieved {len(historical_df)} weeks of historical data")
        
        # Calculate thresholds
        thresholds = calculate_thresholds(historical_df)
        
        if not thresholds:
            print(f"⚠️  Insufficient data for threshold calculation")
            continue
        
        # Get fixed thresholds
        fixed_wow = get_fixed_threshold(metric_full, 'week_prev')
        fixed_lt = get_fixed_threshold(metric_full, 'long_term')
        
        print(f"\n📊 Historical Statistics:")
        print(f"   Mean Change: {thresholds['mean']:.2f}%")
        print(f"   Std Dev: {thresholds['std_dev']:.2f}%")
        print(f"   95th Percentile: {thresholds['p95']:.2f}%")
        
        print(f"\n📈 Week-over-Week Thresholds:")
        print(f"   Fixed (current):        {fixed_wow:.1f}%")
        print(f"   Std Dev (2σ):           {thresholds['std_dev_2sigma']:.1f}%")
        print(f"   Percentile (95th):      {thresholds['percentile_95']:.1f}%")
        print(f"   Z-Score (99%):          {thresholds['z_score_99']:.1f}%")
        print(f"   Hybrid (avg):           {thresholds['hybrid']:.1f}%")
        
        print(f"\n📈 Long-Term Thresholds:")
        print(f"   Fixed (current):        {fixed_lt:.1f}%")
        print(f"   Std Dev (2σ):           {thresholds['std_dev_2sigma'] * 1.5:.1f}%")
        print(f"   Percentile (95th):      {thresholds['percentile_95'] * 1.5:.1f}%")
        print(f"   Z-Score (99%):          {thresholds['z_score_99'] * 1.5:.1f}%")
        print(f"   Hybrid (avg):           {thresholds['hybrid'] * 1.5:.1f}%")
        
        results.append({
            'metric': metric_display,
            'fixed_wow': fixed_wow,
            'fixed_lt': fixed_lt,
            'std_dev_wow': thresholds['std_dev_2sigma'],
            'percentile_wow': thresholds['percentile_95'],
            'z_score_wow': thresholds['z_score_99'],
            'hybrid_wow': thresholds['hybrid'],
            'std_dev_lt': thresholds['std_dev_2sigma'] * 1.5,
            'percentile_lt': thresholds['percentile_95'] * 1.5,
            'z_score_lt': thresholds['z_score_99'] * 1.5,
            'hybrid_lt': thresholds['hybrid'] * 1.5
        })
    
    # Create summary table
    if results:
        print("\n" + "="*80)
        print("SUMMARY TABLE: Week-over-Week Thresholds")
        print("="*80)
        
        summary_data = []
        for r in results:
            summary_data.append({
                'Metric': r['metric'],
                'Fixed': f"{r['fixed_wow']:.1f}%",
                'Std Dev': f"{r['std_dev_wow']:.1f}%",
                'Percentile': f"{r['percentile_wow']:.1f}%",
                'Z-Score': f"{r['z_score_wow']:.1f}%",
                'Hybrid': f"{r['hybrid_wow']:.1f}%"
            })
        
        summary_df = pd.DataFrame(summary_data)
        print(summary_df.to_string(index=False))
        
        print("\n" + "="*80)
        print("SUMMARY TABLE: Long-Term Thresholds")
        print("="*80)
        
        summary_data_lt = []
        for r in results:
            summary_data_lt.append({
                'Metric': r['metric'],
                'Fixed': f"{r['fixed_lt']:.1f}%",
                'Std Dev': f"{r['std_dev_lt']:.1f}%",
                'Percentile': f"{r['percentile_lt']:.1f}%",
                'Z-Score': f"{r['z_score_lt']:.1f}%",
                'Hybrid': f"{r['hybrid_lt']:.1f}%"
            })
        
        summary_df_lt = pd.DataFrame(summary_data_lt)
        print(summary_df_lt.to_string(index=False))
        
        # Save to CSV
        output_file = Path(__file__).parent / 'threshold_analysis_summary.csv'
        summary_df.to_csv(output_file, index=False)
        print(f"\n✅ Summary saved to: {output_file}")
    else:
        print("\n⚠️  No results to display")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())

