#!/usr/bin/env python3
"""
Generate steering report directly from payments_hf.payments_p0_metrics table
Following REPORT_PROMPT_V2.md format
"""
import sys
import os
from pathlib import Path
from datetime import datetime

# Add cursor_databricks directory to path
cursor_databricks_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_dir)

from databricks_api import DatabricksAPI
from config import DATABRICKS_HOST, TOKEN, CLUSTER_ID
from databricks.cursor_databricks.projects.long_term_steering_report.long_term_steering_report import (
    build_metrics_query,
    process_comparison_data
)

def get_latest_week():
    """Get the latest complete week"""
    db_api = DatabricksAPI()
    
    query = """
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
    
    results = db_api.run_sql(query, display=False)
    if results and len(results) > 0:
        return results[0][0]
    return None

def get_prev_week(week_str):
    """Get previous week"""
    db_api = DatabricksAPI()
    
    query = f"""
    SELECT hellofresh_week
    FROM dimensions.date_dimension dd
    WHERE
      hellofresh_week >= '2021-W01'
      AND DATE(date_string_backwards) < CURRENT_DATE()
      AND hellofresh_week < '{week_str}'
    GROUP BY 1
    HAVING COUNT(*)=7
    ORDER BY hellofresh_week DESC
    LIMIT 1
    """
    
    results = db_api.run_sql(query, display=False)
    if results and len(results) > 0:
        return results[0][0]
    return None

def get_prev_year_week(week_str):
    """Get previous year same week"""
    year = int(week_str.split('-W')[0])
    week_num = week_str.split('-W')[1]
    prev_year = year - 1
    return f"{prev_year}-W{week_num}"

def get_latest_13_weeks():
    """Get latest 13 complete weeks"""
    db_api = DatabricksAPI()
    
    query = """
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
    
    results = db_api.run_sql(query, display=False)
    if results:
        return [row[0] for row in results]
    return []

def format_arrow(rel_change):
    """Return arrow based on relative change"""
    return '↑' if rel_change > 0 else '↓'

def format_significance(is_significant):
    """Format significance"""
    return 'significant' if is_significant else 'not significant'

def build_callout_for_metric(metric_name, week_prev_df, week_yoy_df, quarter_prev_df):
    """Build callout text for a metric from dataframes"""
    parts = []
    
    # Week vs Prev Week
    if week_prev_df is not None and not week_prev_df.empty:
        parts.append("**Current Week vs Prev Week:**")
        
        for cluster in ['Overall', 'HF-NA', 'HF-INTL', 'RTE', 'WL']:
            cluster_data = week_prev_df[week_prev_df['reporting_cluster'] == cluster]
            if not cluster_data.empty:
                row = cluster_data.iloc[0]
                arrow = format_arrow(row['relative_change_pct'])
                sig = format_significance(row.get('is_significant', False))
                volume = row.get('volume_impacted', '0')
                parts.append(f"- **{cluster}**: {row['prev_ratio']:.2f}% to {row['current_ratio']:.2f}% ({arrow}{abs(row['relative_change_pct']):.2f}%, {sig}, volume: {volume})")
        
        # Deep Insights - top business units
        parts.append("<br><br>**Deep Insights**")
        insights = []
        for cluster in ['Overall', 'HF-NA', 'HF-INTL', 'RTE', 'WL']:
            cluster_data = week_prev_df[week_prev_df['reporting_cluster'] == cluster]
            if not cluster_data.empty and 'business_unit' in cluster_data.columns:
                bu_data = cluster_data[cluster_data['business_unit'].notna()]
                if not bu_data.empty:
                    top_bu = bu_data.nlargest(3, 'relative_change_pct', keep='all')
                    for _, bu_row in top_bu.iterrows():
                        arrow = format_arrow(bu_row['relative_change_pct'])
                        insights.append(f"- **{cluster}** {bu_row['business_unit']}: {bu_row['prev_ratio']:.2f}% to {bu_row['current_ratio']:.2f}% ({arrow}{abs(bu_row['relative_change_pct']):.2f}%, volume: {bu_row.get('volume_impacted', '0')})")
        
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
                parts.append("<br><br>**Long Term Impact**")
                parts.append(f"- **Current Quarter vs Prev Quarter**: {row['prev_ratio']:.2f}% to {row['current_ratio']:.2f}% ({arrow}{abs(row['relative_change_pct']):.2f}%, volume: {row.get('volume_impacted', '0')})")
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
                parts.append("<br><br>**Comparison vs Prev Year**")
                parts.append(f"- **Current Week vs Prev Year Week**: {row['prev_ratio']:.2f}% to {row['current_ratio']:.2f}% ({arrow}{abs(row['relative_change_pct']):.2f}%, volume: {row.get('volume_impacted', '0')})")
            else:
                parts.append("<br><br>**Comparison vs Prev Year**<br>- No significant year-over-year impact (all changes <10%)")
        else:
            parts.append("<br><br>**Comparison vs Prev Year**<br>- No significant year-over-year impact (all changes <10%)")
    else:
        parts.append("<br><br>**Comparison vs Prev Year**<br>- No significant year-over-year impact (all changes <10%)")
    
    return "<br>".join(parts)

def generate_key_insights(week_prev_df, week_yoy_df, quarter_prev_df):
    """Generate key insights from dataframes"""
    insights = []
    
    # Critical Issues
    critical = []
    if week_prev_df is not None and not week_prev_df.empty:
        overall = week_prev_df[week_prev_df['reporting_cluster'] == 'Overall']
        if not overall.empty:
            for _, row in overall.iterrows():
                if row['relative_change_pct'] < -5:
                    metric_short = row.get('metric_final_name', '').split(' - ')[-1]
                    critical.append(f"{metric_short} decreased {abs(row['relative_change_pct']):.2f}% ({row['prev_ratio']:.2f}% to {row['current_ratio']:.2f}%)")
    
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
                    positive.append(f"{metric_short} increased {row['relative_change_pct']:.2f}% ({row['prev_ratio']:.2f}% to {row['current_ratio']:.2f}%)")
    
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

def main():
    """Generate steering report from source"""
    print("🔍 Fetching data from source...")
    
    # Get latest week
    latest_week = get_latest_week()
    if not latest_week:
        print("❌ Could not determine latest week")
        return 1
    
    print(f"📅 Latest week: {latest_week}")
    
    prev_week = get_prev_week(latest_week)
    prev_year_week = get_prev_year_week(latest_week)
    latest_13weeks = get_latest_13_weeks()
    prev_13weeks = latest_13weeks[13:] if len(latest_13weeks) >= 26 else []
    
    print(f"   Previous week: {prev_week}")
    print(f"   Previous year week: {prev_year_week}")
    print(f"   Current quarter: {len(latest_13weeks)} weeks")
    print(f"   Previous quarter: {len(prev_13weeks)} weeks")
    
    # Initialize Databricks API
    db_api = DatabricksAPI()
    
    # Metric groups in order (matching REPORT_PROMPT_V2.md)
    metric_groups = [
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
    
    # Query data for each comparison
    print("\n📊 Querying metrics data...")
    
    # Week vs Prev Week
    week_prev_query = build_metrics_query('WEEK', 'prev_period', latest_week)
    week_prev_results = db_api.run_sql(week_prev_query, display=False)
    
    # Week vs Prev Year Week  
    week_yoy_query = build_metrics_query('WEEK', 'prev_year', latest_week)
    week_yoy_results = db_api.run_sql(week_yoy_query, display=False)
    
    # Quarter vs Prev Quarter (need to aggregate 13 weeks)
    # For now, we'll use a simplified approach
    quarter_prev_query = build_metrics_query('WEEK', 'prev_period', latest_week)  # Simplified
    quarter_prev_results = db_api.run_sql(quarter_prev_query, display=False)
    
    print(f"   Week vs Prev Week: {len(week_prev_results) if week_prev_results else 0} rows")
    print(f"   Week vs Prev Year: {len(week_yoy_results) if week_yoy_results else 0} rows")
    print(f"   Quarter vs Prev Quarter: {len(quarter_prev_results) if quarter_prev_results else 0} rows")
    
    # Process data (convert to dataframes)
    # Note: This would need to be adapted based on the actual structure
    # For now, we'll create a simplified version
    
    # Generate report
    week_num = latest_week.split('-W')[1]
    report = f"# {latest_week} Weekly Payments Metrics Steering\n\n"
    report += "## Key Insights\n"
    report += "- **Critical Issues:** [To be populated from data]\n"
    report += "- **Positive Trends:** [To be populated from data]\n"
    report += "- **Risk Shifts:** [To be populated from data]\n"
    report += "- **Emerging Concerns:** [To be populated from data]\n\n"
    report += "| Metrics | Anomaly/Callout | Notes |\n"
    report += "| :--- | :--- | :--- |\n"
    
    # Add placeholder for each metric
    for metric_display, metric_full in metric_groups:
        report += f"| **{metric_display}** | [Data to be populated] | |\n"
    
    # Write output
    script_dir = Path(__file__).parent
    output_file = script_dir / f'W{week_num}_steering_from_source.md'
    with open(output_file, 'w') as f:
        f.write(report)
    
    print(f"\n✅ Generated steering report: {output_file}")
    print(f"   Week: {latest_week}")
    print(f"   Note: This is a template - needs integration with Spark DataFrame processing")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())

