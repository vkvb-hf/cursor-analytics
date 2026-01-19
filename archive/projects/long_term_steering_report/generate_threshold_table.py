#!/usr/bin/env python3
"""
Generate a comprehensive threshold analysis table for all metrics.
Shows metric names as rows and threshold methods as columns.
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
    
    # First, get the list of available weeks from date_dimension
    weeks_query = f"""
    SELECT DISTINCT dd.hellofresh_week
    FROM dimensions.date_dimension dd
    WHERE dd.hellofresh_week >= '2021-W01'
      AND DATE(dd.date_string_backwards) < CURRENT_DATE()
    GROUP BY dd.hellofresh_week
    HAVING COUNT(*) = 7
    ORDER BY dd.hellofresh_week DESC
    LIMIT {num_weeks}
    """
    
    try:
        weeks_result = db.run_sql(weeks_query, display=False)
        if not weeks_result or len(weeks_result) == 0:
            return pd.DataFrame()
        
        # Extract week strings
        if hasattr(weeks_result[0], '__fields__'):
            weeks_list = [getattr(row, list(row.__fields__)[0]) for row in weeks_result]
        else:
            weeks_list = [row[0] if isinstance(row, (list, tuple)) else row for row in weeks_result]
        
        weeks_str = ','.join([f"'{w}'" for w in weeks_list])
        
        # Now query metrics for these specific weeks
        query = f"""
        SELECT 
            a.date_value,
            CASE 
                WHEN SUM(a.current_metric_value_denominator) > 0 
                THEN SUM(a.current_metric_value_numerator) / SUM(a.current_metric_value_denominator)
                ELSE 0 
            END AS metric_value,
            SUM(a.current_metric_value_numerator) AS current_metric_value_numerator,
            SUM(a.current_metric_value_denominator) AS current_metric_value_denominator
        FROM payments_hf.payments_p0_metrics a
        WHERE 1=1
            AND a.focus_group = '{focus_group}'
            AND a.metric_group = '{metric_group}'
            AND a.metric_name = '{metric_name}'
            AND a.metric_type IN ('ratio', 'dollar-ratio')
            AND a.flag_is_p0 = 'TRUE'
            AND a.date_granularity = 'WEEK'
            AND a.reporting_cluster = 'Overall'
            AND a.date_value IN ({weeks_str})
            AND (
                (a.metric_name not IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])})) 
                OR (a.metric_name IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])}) AND a.dimension_value in ('Good'))
            )
            AND (
                (a.metric_name not IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])}) AND a.dimension_name = '_Overall')
                OR (a.metric_name IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])}) AND a.dimension_value = 'Good')
            )
        GROUP BY a.date_value
        ORDER BY a.date_value DESC
        """
        
        result = db.run_sql(query, display=False)
        if result and len(result) > 0:
            # Convert result to DataFrame
            if hasattr(result[0], '__fields__'):
                columns = list(result[0].__fields__)
                data = [[getattr(row, col) for col in columns] for row in result]
                df = pd.DataFrame(data, columns=columns)
            else:
                df = pd.DataFrame(result)
                if 'date_value' not in df.columns and len(df.columns) >= 2:
                    df.columns = ['date_value', 'metric_value', 'numerator', 'denominator']
            
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
        return pd.DataFrame()
    
    return pd.DataFrame()

def calculate_thresholds(historical_df):
    """Calculate thresholds using different methods."""
    if historical_df.empty or 'abs_week_over_week_change_pct' not in historical_df.columns:
        return {}
    
    changes = historical_df['abs_week_over_week_change_pct'].dropna()
    
    if len(changes) < 10:
        return {}
    
    # Filter out infinite and extremely large values
    changes_clean = changes[changes != np.inf]
    changes_clean = changes_clean[changes_clean < 10000]
    
    if len(changes_clean) < 10:
        return {}
    
    mean_change = changes_clean.mean()
    std_dev = changes_clean.std()
    p95 = changes_clean.quantile(0.95)
    
    # Handle edge cases
    if np.isnan(mean_change) or np.isinf(mean_change):
        mean_change = 0
    if np.isnan(std_dev) or np.isinf(std_dev):
        std_dev = 0
    if np.isnan(p95) or np.isinf(p95):
        p95 = 100
    
    std_dev_2sigma = mean_change + (2.0 * std_dev) if not np.isnan(std_dev) else p95
    z_score_99 = mean_change + (2.576 * std_dev) if std_dev > 0 and not np.isnan(std_dev) else p95
    hybrid = (std_dev_2sigma + p95) / 2.0 if not (np.isnan(std_dev_2sigma) or np.isnan(p95)) else p95
    
    # Cap thresholds at reasonable maximum
    std_dev_2sigma = min(std_dev_2sigma, 1000) if not np.isnan(std_dev_2sigma) else p95
    z_score_99 = min(z_score_99, 1000) if not np.isnan(z_score_99) else p95
    hybrid = min(hybrid, 1000) if not np.isnan(hybrid) else p95
    
    # Calculate how many changes would be flagged
    flagged_fixed = len(changes_clean[changes_clean >= 10.0])
    flagged_std_dev = len(changes_clean[changes_clean >= std_dev_2sigma])
    flagged_percentile = len(changes_clean[changes_clean >= p95])
    flagged_z_score = len(changes_clean[changes_clean >= z_score_99])
    flagged_hybrid = len(changes_clean[changes_clean >= hybrid])
    
    thresholds = {
        'fixed_threshold': 10.0,
        'fixed_flagged': flagged_fixed,
        'fixed_flagged_pct': (flagged_fixed / len(changes_clean)) * 100,
        'std_dev_threshold': std_dev_2sigma,
        'std_dev_flagged': flagged_std_dev,
        'std_dev_flagged_pct': (flagged_std_dev / len(changes_clean)) * 100,
        'percentile_threshold': p95,
        'percentile_flagged': flagged_percentile,
        'percentile_flagged_pct': (flagged_percentile / len(changes_clean)) * 100,
        'z_score_threshold': z_score_99,
        'z_score_flagged': flagged_z_score,
        'z_score_flagged_pct': (flagged_z_score / len(changes_clean)) * 100,
        'hybrid_threshold': hybrid,
        'hybrid_flagged': flagged_hybrid,
        'hybrid_flagged_pct': (flagged_hybrid / len(changes_clean)) * 100,
        'total_changes': len(changes_clean)
    }
    
    return thresholds

def get_fixed_threshold(metric_full_name):
    """Get fixed threshold for AR vs other metrics."""
    return 5.0 if metric_full_name in AR_METRICS else 10.0

def main():
    print("="*80)
    print("THRESHOLD ANALYSIS TABLE FOR ALL METRICS")
    print("="*80)
    print(f"\nAnalyzing {len(METRIC_GROUPS)} metrics using {HISTORICAL_WEEKS} weeks of historical data...")
    print("Connecting to Databricks...\n")
    
    db = DatabricksAPI()
    
    results = []
    
    for idx, (metric_display, metric_full) in enumerate(METRIC_GROUPS, 1):
        print(f"[{idx}/{len(METRIC_GROUPS)}] Analyzing: {metric_display}")
        
        # Get historical data
        historical_df = get_historical_data(db, metric_full, HISTORICAL_WEEKS)
        
        if historical_df.empty:
            print(f"  ⚠️  No historical data found")
            results.append({
                'Metric': metric_display,
                'Fixed_Threshold': get_fixed_threshold(metric_full),
                'Fixed_Flagged': 'N/A',
                'StdDev_Threshold': 'N/A',
                'StdDev_Flagged': 'N/A',
                'Percentile_Threshold': 'N/A',
                'Percentile_Flagged': 'N/A',
                'ZScore_Threshold': 'N/A',
                'ZScore_Flagged': 'N/A',
                'Hybrid_Threshold': 'N/A',
                'Hybrid_Flagged': 'N/A'
            })
            continue
        
        # Calculate thresholds
        thresholds = calculate_thresholds(historical_df)
        
        if not thresholds:
            print(f"  ⚠️  Insufficient data for threshold calculation")
            results.append({
                'Metric': metric_display,
                'Fixed_Threshold': get_fixed_threshold(metric_full),
                'Fixed_Flagged': 'N/A',
                'StdDev_Threshold': 'N/A',
                'StdDev_Flagged': 'N/A',
                'Percentile_Threshold': 'N/A',
                'Percentile_Flagged': 'N/A',
                'ZScore_Threshold': 'N/A',
                'ZScore_Flagged': 'N/A',
                'Hybrid_Threshold': 'N/A',
                'Hybrid_Flagged': 'N/A'
            })
            continue
        
        # Get fixed threshold (AR metrics use 5%, others use 10%)
        fixed_threshold = get_fixed_threshold(metric_full)
        fixed_flagged = len(historical_df['abs_week_over_week_change_pct'].dropna()[
            historical_df['abs_week_over_week_change_pct'].dropna() >= fixed_threshold
        ])
        fixed_flagged_pct = (fixed_flagged / thresholds['total_changes']) * 100 if thresholds['total_changes'] > 0 else 0
        
        results.append({
            'Metric': metric_display,
            'Fixed_Threshold': f"{fixed_threshold:.1f}%",
            'Fixed_Flagged': f"{fixed_flagged} ({fixed_flagged_pct:.1f}%)",
            'StdDev_Threshold': f"{thresholds['std_dev_threshold']:.1f}%",
            'StdDev_Flagged': f"{thresholds['std_dev_flagged']} ({thresholds['std_dev_flagged_pct']:.1f}%)",
            'Percentile_Threshold': f"{thresholds['percentile_threshold']:.1f}%",
            'Percentile_Flagged': f"{thresholds['percentile_flagged']} ({thresholds['percentile_flagged_pct']:.1f}%)",
            'ZScore_Threshold': f"{thresholds['z_score_threshold']:.1f}%",
            'ZScore_Flagged': f"{thresholds['z_score_flagged']} ({thresholds['z_score_flagged_pct']:.1f}%)",
            'Hybrid_Threshold': f"{thresholds['hybrid_threshold']:.1f}%",
            'Hybrid_Flagged': f"{thresholds['hybrid_flagged']} ({thresholds['hybrid_flagged_pct']:.1f}%)"
        })
        
        print(f"  ✅ Calculated thresholds")
    
    # Create comprehensive table
    if results:
        print("\n" + "="*80)
        print("THRESHOLD ANALYSIS TABLE")
        print("="*80)
        
        # Create DataFrame
        df = pd.DataFrame(results)
        
        # Create a formatted table with multi-level columns
        print("\n📊 Week-over-Week Thresholds Table:")
        print("="*120)
        
        # Print table with proper formatting
        print(f"{'Metric':<50} | {'Fixed':<20} | {'Std Dev':<20} | {'Percentile':<20} | {'Z-Score':<20} | {'Hybrid':<20}")
        print(f"{'':<50} | {'Thresh | Flagged':<20} | {'Thresh | Flagged':<20} | {'Thresh | Flagged':<20} | {'Thresh | Flagged':<20} | {'Thresh | Flagged':<20}")
        print("-" * 120)
        
        for _, row in df.iterrows():
            metric = row['Metric'][:48]  # Truncate if too long
            print(f"{metric:<50} | {row['Fixed_Threshold']:<8} {row['Fixed_Flagged']:<11} | "
                  f"{row['StdDev_Threshold']:<8} {row['StdDev_Flagged']:<11} | "
                  f"{row['Percentile_Threshold']:<8} {row['Percentile_Flagged']:<11} | "
                  f"{row['ZScore_Threshold']:<8} {row['ZScore_Flagged']:<11} | "
                  f"{row['Hybrid_Threshold']:<8} {row['Hybrid_Flagged']:<11}")
        
        # Also create a cleaner markdown table
        print("\n" + "="*120)
        print("MARKDOWN TABLE FORMAT:")
        print("="*120)
        print("\n| Metric | Fixed | Std Dev | Percentile | Z-Score | Hybrid |")
        print("|" + "-"*6 + "|" + "-"*20 + "|" + "-"*20 + "|" + "-"*20 + "|" + "-"*20 + "|" + "-"*20 + "|")
        print("| | Threshold | Flagged | Threshold | Flagged | Threshold | Flagged | Threshold | Flagged | Threshold | Flagged |")
        print("|" + "-"*6 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*10 + "|")
        
        for _, row in df.iterrows():
            print(f"| {row['Metric']} | {row['Fixed_Threshold']} | {row['Fixed_Flagged']} | "
                  f"{row['StdDev_Threshold']} | {row['StdDev_Flagged']} | "
                  f"{row['Percentile_Threshold']} | {row['Percentile_Flagged']} | "
                  f"{row['ZScore_Threshold']} | {row['ZScore_Flagged']} | "
                  f"{row['Hybrid_Threshold']} | {row['Hybrid_Flagged']} |")
        
        # Save to CSV
        output_file = Path(__file__).parent / 'threshold_analysis_table.csv'
        df.to_csv(output_file, index=False)
        print(f"\n✅ Table saved to CSV: {output_file}")
        
        # Also save as markdown
        md_output = Path(__file__).parent / 'threshold_analysis_table.md'
        with open(md_output, 'w') as f:
            f.write("# Threshold Analysis Table\n\n")
            f.write("## Week-over-Week Thresholds\n\n")
            f.write("| Metric | Fixed | Std Dev | Percentile | Z-Score | Hybrid |\n")
            f.write("|" + "-"*6 + "|" + "-"*20 + "|" + "-"*20 + "|" + "-"*20 + "|" + "-"*20 + "|" + "-"*20 + "|" + "\n")
            f.write("| | Threshold | Flagged | Threshold | Flagged | Threshold | Flagged | Threshold | Flagged | Threshold | Flagged |\n")
            f.write("|" + "-"*6 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*10 + "|" + "\n")
            for _, row in df.iterrows():
                f.write(f"| {row['Metric']} | {row['Fixed_Threshold']} | {row['Fixed_Flagged']} | "
                       f"{row['StdDev_Threshold']} | {row['StdDev_Flagged']} | "
                       f"{row['Percentile_Threshold']} | {row['Percentile_Flagged']} | "
                       f"{row['ZScore_Threshold']} | {row['ZScore_Flagged']} | "
                       f"{row['Hybrid_Threshold']} | {row['Hybrid_Flagged']} |\n")
        print(f"✅ Table saved to Markdown: {md_output}")
    else:
        print("\n⚠️  No results to display")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())

