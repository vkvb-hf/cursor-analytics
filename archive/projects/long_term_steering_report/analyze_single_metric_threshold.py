#!/usr/bin/env python3
"""
Analyze threshold for a single metric with detailed plots and explanations.
This helps understand the data distribution and why we select specific thresholds.
"""
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Add cursor_databricks directory to path
cursor_databricks_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_dir)

from databricks_api import DatabricksAPI

# Configuration
SPECIAL_METRICS = ['0_ShipRate', '1_RecoveryW0', '2_Recovery_12wkCohort', '3_DunningAvgNetProfit_12wkCohort']

# Select a metric to analyze
METRIC_TO_ANALYZE = '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
METRIC_DISPLAY_NAME = 'Payment Page Visit to Success'

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
            print("No weeks found")
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
        import traceback
        traceback.print_exc()
        return pd.DataFrame()
    
    return pd.DataFrame()

def analyze_and_plot(historical_df, metric_name):
    """Analyze threshold and create visualizations."""
    if historical_df.empty:
        print("No data to analyze")
        return
    
    print(f"\n{'='*80}")
    print(f"DETAILED ANALYSIS: {metric_name}")
    print(f"{'='*80}")
    
    # Basic statistics
    print(f"\n📊 Data Overview:")
    print(f"   Total weeks analyzed: {len(historical_df)}")
    print(f"   Date range: {historical_df['date_value'].min()} to {historical_df['date_value'].max()}")
    print(f"   Unique dates: {historical_df['date_value'].nunique()}")
    print(f"   Metric value range: {historical_df['metric_value'].min():.4f} to {historical_df['metric_value'].max():.4f}")
    print(f"   Mean metric value: {historical_df['metric_value'].mean():.4f}")
    
    # Show sample data
    print(f"\n📋 Sample Data (first 10 rows):")
    print(historical_df[['date_value', 'metric_value', 'week_over_week_change_pct']].head(10).to_string(index=False))
    
    # Check data quality
    unique_dates = historical_df['date_value'].nunique()
    if unique_dates < len(historical_df):
        print(f"\n⚠️  Data Issue Detected:")
        print(f"   Only {unique_dates} unique dates found in {len(historical_df)} rows")
        print(f"   This suggests duplicate dates in the data")
        print(f"   Unique dates: {sorted(historical_df['date_value'].unique())[:10]}...")
    else:
        print(f"\n✅ Data Quality Check:")
        print(f"   {unique_dates} unique dates found in {len(historical_df)} rows - Perfect!")
        print(f"   Date range spans: {sorted(historical_df['date_value'].unique())[0]} to {sorted(historical_df['date_value'].unique())[-1]}")
    
    # Week-over-week changes
    changes = historical_df['abs_week_over_week_change_pct'].dropna()
    
    # Check for issues
    print(f"\n🔍 Data Quality Checks:")
    zero_changes = len(changes[changes == 0])
    print(f"   Weeks with 0% change: {zero_changes} ({zero_changes/len(changes)*100:.1f}%)")
    print(f"   Weeks with NaN change: {len(changes[changes.isna()])}")
    print(f"   Weeks with inf change: {len(changes[changes == np.inf])}")
    print(f"   Weeks with >100% change: {len(changes[changes > 100])}")
    
    # Filter out infinite and extremely large values
    changes_clean = changes[changes != np.inf]
    changes_clean = changes_clean[changes_clean < 10000]
    
    print(f"\n📈 Week-over-Week Change Statistics:")
    print(f"   Total changes: {len(changes_clean)}")
    print(f"   Changes with valid values: {len(changes_clean[changes_clean.notna()])}")
    print(f"   Changes with inf values: {len(changes[changes == np.inf])}")
    print(f"   Changes > 10000%: {len(changes[changes >= 10000])}")
    
    if len(changes_clean) < 10:
        print(f"\n⚠️  Insufficient valid data points ({len(changes_clean)} < 10)")
        return
    
    mean_change = changes_clean.mean()
    median_change = changes_clean.median()
    std_dev = changes_clean.std()
    p50 = changes_clean.quantile(0.50)
    p75 = changes_clean.quantile(0.75)
    p90 = changes_clean.quantile(0.90)
    p95 = changes_clean.quantile(0.95)
    p99 = changes_clean.quantile(0.99)
    
    print(f"\n   Mean absolute change: {mean_change:.2f}%")
    print(f"   Median absolute change: {median_change:.2f}%")
    print(f"   Standard deviation: {std_dev:.2f}%")
    print(f"   50th percentile: {p50:.2f}%")
    print(f"   75th percentile: {p75:.2f}%")
    print(f"   90th percentile: {p90:.2f}%")
    print(f"   95th percentile: {p95:.2f}%")
    print(f"   99th percentile: {p99:.2f}%")
    
    # Calculate thresholds
    std_dev_2sigma = mean_change + (2.0 * std_dev)
    z_score_99 = mean_change + (2.576 * std_dev) if std_dev > 0 else mean_change
    hybrid = (std_dev_2sigma + p95) / 2.0
    
    # Cap at reasonable maximum
    std_dev_2sigma = min(std_dev_2sigma, 1000)
    z_score_99 = min(z_score_99, 1000)
    hybrid = min(hybrid, 1000)
    
    print(f"\n📊 Calculated Thresholds:")
    print(f"   Fixed (current):       10.0%")
    print(f"   Std Dev (2σ):          {std_dev_2sigma:.1f}%")
    print(f"   Percentile (95th):     {p95:.1f}%")
    print(f"   Z-Score (99%):         {z_score_99:.1f}%")
    print(f"   Hybrid (avg):          {hybrid:.1f}%")
    
    # Explain the thresholds
    print(f"\n💡 Threshold Explanation:")
    print(f"   • Fixed (10%): Current hardcoded threshold")
    print(f"   • Std Dev (2σ): Mean + 2 standard deviations = {mean_change:.1f}% + 2×{std_dev:.1f}% = {std_dev_2sigma:.1f}%")
    print(f"     → Captures ~95% of normal variation (2-sigma rule)")
    print(f"   • Percentile (95th): {p95:.1f}% of historical changes were smaller than this")
    print(f"     → Only flag changes larger than 95% of historical changes")
    print(f"   • Z-Score (99%): Mean + 2.576×std_dev = {mean_change:.1f}% + 2.576×{std_dev:.1f}% = {z_score_99:.1f}%")
    print(f"     → Statistical significance at 99% confidence level")
    print(f"   • Hybrid: Average of Std Dev and Percentile = ({std_dev_2sigma:.1f}% + {p95:.1f}%) / 2 = {hybrid:.1f}%")
    print(f"     → Balanced approach combining both methods")
    
    # Show what percentage of changes would be flagged
    print(f"\n📊 Impact Analysis:")
    for threshold_name, threshold_value in [
        ('Fixed (10%)', 10.0),
        ('Std Dev (2σ)', std_dev_2sigma),
        ('Percentile (95th)', p95),
        ('Z-Score (99%)', z_score_99),
        ('Hybrid', hybrid)
    ]:
        flagged = len(changes_clean[changes_clean >= threshold_value])
        flagged_pct = (flagged / len(changes_clean)) * 100
        print(f"   {threshold_name:20s}: Would flag {flagged:3d} changes ({flagged_pct:5.1f}% of historical changes)")
    
    # Create plots
    output_dir = Path(__file__).parent
    output_dir.mkdir(exist_ok=True)
    
    # Plot 1: Time series of metric values
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle(f'Threshold Analysis: {metric_name}', fontsize=16, fontweight='bold')
    
    # Plot 1.1: Metric value over time
    ax1 = axes[0, 0]
    ax1.plot(historical_df['date_value'], historical_df['metric_value'], marker='o', linewidth=2, markersize=4)
    ax1.set_title('Metric Value Over Time', fontweight='bold')
    ax1.set_xlabel('Week')
    ax1.set_ylabel('Metric Value')
    ax1.grid(True, alpha=0.3)
    ax1.tick_params(axis='x', rotation=45)
    
    # Plot 1.2: Week-over-week changes over time
    ax2 = axes[0, 1]
    ax2.plot(historical_df['date_value'][1:], historical_df['week_over_week_change_pct'][1:], 
             marker='o', linewidth=2, markersize=4, color='orange')
    ax2.axhline(y=0, color='black', linestyle='--', linewidth=1)
    ax2.set_title('Week-over-Week Change Over Time', fontweight='bold')
    ax2.set_xlabel('Week')
    ax2.set_ylabel('Change (%)')
    ax2.grid(True, alpha=0.3)
    ax2.tick_params(axis='x', rotation=45)
    
    # Plot 1.3: Distribution of absolute changes
    ax3 = axes[1, 0]
    ax3.hist(changes_clean, bins=30, edgecolor='black', alpha=0.7)
    ax3.axvline(x=10, color='red', linestyle='--', linewidth=2, label='Fixed (10%)')
    ax3.axvline(x=std_dev_2sigma, color='blue', linestyle='--', linewidth=2, label=f'Std Dev (2σ) = {std_dev_2sigma:.1f}%')
    ax3.axvline(x=p95, color='green', linestyle='--', linewidth=2, label=f'Percentile (95th) = {p95:.1f}%')
    ax3.axvline(x=hybrid, color='purple', linestyle='--', linewidth=2, label=f'Hybrid = {hybrid:.1f}%')
    ax3.set_title('Distribution of Absolute Week-over-Week Changes', fontweight='bold')
    ax3.set_xlabel('Absolute Change (%)')
    ax3.set_ylabel('Frequency')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Plot 1.4: Box plot with thresholds
    ax4 = axes[1, 1]
    box_data = [changes_clean]
    bp = ax4.boxplot(box_data, vert=True, patch_artist=True)
    bp['boxes'][0].set_facecolor('lightblue')
    ax4.axhline(y=10, color='red', linestyle='--', linewidth=2, label='Fixed (10%)')
    ax4.axhline(y=std_dev_2sigma, color='blue', linestyle='--', linewidth=2, label=f'Std Dev (2σ) = {std_dev_2sigma:.1f}%')
    ax4.axhline(y=p95, color='green', linestyle='--', linewidth=2, label=f'Percentile (95th) = {p95:.1f}%')
    ax4.axhline(y=hybrid, color='purple', linestyle='--', linewidth=2, label=f'Hybrid = {hybrid:.1f}%')
    ax4.set_title('Box Plot: Absolute Changes with Thresholds', fontweight='bold')
    ax4.set_ylabel('Absolute Change (%)')
    ax4.set_xticklabels(['Week-over-Week\nChanges'])
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save plot
    plot_file = output_dir / f'threshold_analysis_{metric_name.replace(" ", "_").replace("/", "_")}.png'
    plt.savefig(plot_file, dpi=150, bbox_inches='tight')
    print(f"\n✅ Plot saved to: {plot_file}")
    
    # Create a detailed summary plot
    fig2, axes2 = plt.subplots(1, 1, figsize=(12, 8))
    
    # Cumulative distribution
    sorted_changes = np.sort(changes_clean)
    cumulative_pct = np.arange(1, len(sorted_changes) + 1) / len(sorted_changes) * 100
    
    axes2.plot(sorted_changes, cumulative_pct, linewidth=3, label='Cumulative Distribution')
    axes2.axvline(x=10, color='red', linestyle='--', linewidth=2, label='Fixed (10%)')
    axes2.axvline(x=std_dev_2sigma, color='blue', linestyle='--', linewidth=2, label=f'Std Dev (2σ) = {std_dev_2sigma:.1f}%')
    axes2.axvline(x=p95, color='green', linestyle='--', linewidth=2, label=f'Percentile (95th) = {p95:.1f}%')
    axes2.axvline(x=hybrid, color='purple', linestyle='--', linewidth=2, label=f'Hybrid = {hybrid:.1f}%')
    
    # Add annotations
    for threshold_name, threshold_value, color in [
        ('Fixed', 10.0, 'red'),
        ('Std Dev', std_dev_2sigma, 'blue'),
        ('Percentile', p95, 'green'),
        ('Hybrid', hybrid, 'purple')
    ]:
        pct_above = len(changes_clean[changes_clean >= threshold_value]) / len(changes_clean) * 100
        axes2.annotate(f'{threshold_name}\n({pct_above:.1f}% flagged)',
                      xy=(threshold_value, 100 - pct_above),
                      xytext=(10, 20),
                      textcoords='offset points',
                      bbox=dict(boxstyle='round,pad=0.5', facecolor=color, alpha=0.3),
                      arrowprops=dict(arrowstyle='->', color=color),
                      fontsize=9)
    
    axes2.set_title(f'Cumulative Distribution of Changes: {metric_name}', fontweight='bold', fontsize=14)
    axes2.set_xlabel('Absolute Week-over-Week Change (%)', fontsize=12)
    axes2.set_ylabel('Cumulative Percentage (%)', fontsize=12)
    axes2.legend(fontsize=10)
    axes2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    plot_file2 = output_dir / f'threshold_cumulative_{metric_name.replace(" ", "_").replace("/", "_")}.png'
    plt.savefig(plot_file2, dpi=150, bbox_inches='tight')
    print(f"✅ Cumulative distribution plot saved to: {plot_file2}")
    
    # Show the plots
    plt.show()

def main():
    print("="*80)
    print("SINGLE METRIC THRESHOLD ANALYSIS")
    print("="*80)
    print(f"\nAnalyzing: {METRIC_DISPLAY_NAME}")
    print(f"Metric: {METRIC_TO_ANALYZE}")
    print(f"Historical weeks: {HISTORICAL_WEEKS}")
    print("\nConnecting to Databricks...")
    
    db = DatabricksAPI()
    
    # Get historical data
    historical_df = get_historical_data(db, METRIC_TO_ANALYZE, HISTORICAL_WEEKS)
    
    if historical_df.empty:
        print("❌ No historical data found")
        return 1
    
    # Analyze and plot
    analyze_and_plot(historical_df, METRIC_DISPLAY_NAME)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())

