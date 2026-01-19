#!/usr/bin/env python3
"""
Compare metrics from payments_hf.payments_p0_metrics table with detailed_summary files.

This script:
1. Queries the table directly for metric values
2. Parses the detailed_summary files to extract metric values
3. Creates a comparison table showing differences
"""

import sys
import os
import re
from pathlib import Path
import pandas as pd

# Add cursor_databricks directory to path for imports
cursor_databricks_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_dir)
from databricks import sql
from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN

# List of metrics to check
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

def parse_summary_file(file_path):
    """Parse a detailed_summary file and extract metric values for Overall cluster."""
    if not os.path.exists(file_path):
        return {}
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract period information from header
    current_period_match = re.search(r'Current Period:\s*(.+)', content)
    prev_period_match = re.search(r'Previous Period:\s*(.+)', content)
    
    current_period = current_period_match.group(1).strip() if current_period_match else None
    prev_period = prev_period_match.group(1).strip() if prev_period_match else None
    
    metrics_data = {}
    
    # Split by metric sections
    metric_sections = re.split(r'={80}\n([^\n]+)\n={80}', content)
    
    for i in range(1, len(metric_sections), 2):
        if i + 1 >= len(metric_sections):
            break
        
        metric_name = metric_sections[i].strip()
        metric_content = metric_sections[i + 1] if i + 1 < len(metric_sections) else ""
        
        # Find Overall cluster summary
        # Pattern: "For Overall cluster, the [long metric name] increased/decreased from X% to Y%"
        # OR: "from €X.XX to €Y.YY" for Euro-based metrics
        # The metric name can be very long, so we need a flexible pattern
        
        # Try percentage pattern first
        overall_match = re.search(
            r'For Overall cluster[^,]+,\s+[^,]+?\s+(?:increased|decreased)\s+from\s+([\d.]+)%?\s+to\s+([\d.]+)%?',
            metric_content,
            re.IGNORECASE | re.DOTALL
        )
        
        # Alternative simpler percentage pattern
        if not overall_match:
            overall_match = re.search(
                r'For Overall cluster.*?from\s+([\d.]+)%?\s+to\s+([\d.]+)%?',
                metric_content,
                re.IGNORECASE | re.DOTALL
            )
        
        # Try Euro pattern (€X.XX to €Y.YY)
        if not overall_match:
            overall_match = re.search(
                r'For Overall cluster.*?from\s+€([\d.]+)\s+to\s+€([\d.]+)',
                metric_content,
                re.IGNORECASE | re.DOTALL
            )
        
        if overall_match:
            prev_value = float(overall_match.group(1))
            current_value = float(overall_match.group(2))
            
            metrics_data[metric_name] = {
                'current': current_value,
                'prev': prev_value,
                'current_period': current_period,
                'prev_period': prev_period
            }
    
    return metrics_data

def execute_query(query_str):
    """Execute a SQL query and return results as a list of dictionaries."""
    with sql.connect(
        server_hostname=SERVER_HOSTNAME,
        http_path=HTTP_PATH,
        access_token=TOKEN
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query_str)
            result = cursor.fetchall()
            
            # Convert to list of dictionaries
            if result:
                columns = [desc[0] for desc in cursor.description]
                return [dict(zip(columns, row)) for row in result]
            return []

def query_table_metrics(date_value, date_granularity, comparison_type, weeks_list=None, prev_weeks_list=None):
    """Query payments_hf.payments_p0_metrics table for metric values."""
    metrics_dict = {}
    
    try:
        # Query current period
        if weeks_list:
            weeks_list_str = ','.join([f"'{w}'" for w in weeks_list])
            date_filter = f"date_value IN ({weeks_list_str})"
        else:
            date_filter = f"date_value = '{date_value}'"
        
        # Query current period values
        query_current = f"""
            SELECT
                CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
                SUM(current_metric_value_numerator) as current_numerator,
                SUM(current_metric_value_denominator) as current_denominator
            FROM payments_hf.payments_p0_metrics
            WHERE {date_filter}
                AND date_granularity = 'WEEK'
                AND reporting_cluster = 'Overall'
                AND dimension_name = '_Overall'
                AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) IN ({','.join([f"'{m}'" for m in STEERING_METRICS])})
            GROUP BY CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name)
        """
        
        result_current = execute_query(query_current)
        df_current = pd.DataFrame(result_current)
        
        # Query previous period values
        prev_ratio = None
        if comparison_type == 'prev_period' and prev_weeks_list:
            prev_weeks_list_str = ','.join([f"'{w}'" for w in prev_weeks_list])
            query_prev = f"""
                SELECT
                    CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
                    SUM(current_metric_value_numerator) as prev_numerator,
                    SUM(current_metric_value_denominator) as prev_denominator
                FROM payments_hf.payments_p0_metrics
                WHERE date_value IN ({prev_weeks_list_str})
                    AND date_granularity = 'WEEK'
                    AND reporting_cluster = 'Overall'
                    AND dimension_name = '_Overall'
                    AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) IN ({','.join([f"'{m}'" for m in STEERING_METRICS])})
                GROUP BY CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name)
            """
            result_prev = execute_query(query_prev)
            df_prev = pd.DataFrame(result_prev)
        elif comparison_type == 'prev_year':
            # For YoY, use prev_yr columns from current period
            query_prev = f"""
                SELECT
                    CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
                    SUM(prev_yr_metric_value_numerator) as prev_numerator,
                    SUM(prev_yr_metric_value_denominator) as prev_denominator
                FROM payments_hf.payments_p0_metrics
                WHERE {date_filter}
                    AND date_granularity = 'WEEK'
                    AND reporting_cluster = 'Overall'
                    AND dimension_name = '_Overall'
                    AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) IN ({','.join([f"'{m}'" for m in STEERING_METRICS])})
                GROUP BY CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name)
            """
            result_prev = execute_query(query_prev)
            df_prev = pd.DataFrame(result_prev)
        else:
            df_prev = pd.DataFrame()
        
        # Merge current and previous
        if not df_prev.empty:
            df_merged = df_current.merge(df_prev, on='metric_final_name', how='left')
        else:
            df_merged = df_current.copy()
            df_merged['prev_numerator'] = None
            df_merged['prev_denominator'] = None
        
        # Calculate ratios
        for _, row in df_merged.iterrows():
            metric_name = row['metric_final_name']
            current_ratio = (row['current_numerator'] / row['current_denominator'] * 100) if row['current_denominator'] > 0 else 0
            
            if pd.notna(row.get('prev_denominator')) and row.get('prev_denominator', 0) > 0:
                prev_ratio = (row['prev_numerator'] / row['prev_denominator'] * 100)
            else:
                prev_ratio = None
            
            metrics_dict[metric_name] = {
                'current': current_ratio,
                'prev': prev_ratio
            }
        
        return metrics_dict
    except Exception as e:
        print(f"Error querying table: {e}")
        import traceback
        traceback.print_exc()
        return {}

def main():
    """Main comparison function."""
    script_dir = Path(__file__).parent
    
    # Define comparison configurations
    comparisons = [
        {
            'name': 'week_prev',
            'file': 'detailed_summary_week_vs_prev_week.txt',
            'date_value': '2025-W44',
            'date_granularity': 'WEEK',
            'comparison_type': 'prev_period',
            'weeks_list': ['2025-W44'],
            'prev_weeks_list': ['2025-W43']
        },
        {
            'name': 'week_yoy',
            'file': 'detailed_summary_week_vs_prev_yr_week.txt',
            'date_value': '2025-W44',
            'date_granularity': 'WEEK',
            'comparison_type': 'prev_year',
            'weeks_list': ['2025-W44'],
            'prev_weeks_list': None
        },
        {
            'name': 'month_prev',
            'file': 'detailed_summary_month_vs_prev_month.txt',
            'date_value': '2025-W41-2025-W44',
            'date_granularity': '4WEEKS',
            'comparison_type': 'prev_period',
            'weeks_list': ['2025-W41', '2025-W42', '2025-W43', '2025-W44'],
            'prev_weeks_list': ['2025-W37', '2025-W38', '2025-W39', '2025-W40']
        },
        {
            'name': 'month_yoy',
            'file': 'detailed_summary_month_vs_prev_yr_month.txt',
            'date_value': '2025-W41-2025-W44',
            'date_granularity': '4WEEKS',
            'comparison_type': 'prev_year',
            'weeks_list': ['2025-W41', '2025-W42', '2025-W43', '2025-W44']
        },
        {
            'name': 'quarter_prev',
            'file': 'detailed_summary_quarter_vs_prev_quarter.txt',
            'date_value': '2025-W32-2025-W44',
            'date_granularity': '13WEEKS',
            'comparison_type': 'prev_period',
            'weeks_list': ['2025-W32', '2025-W33', '2025-W34', '2025-W35', '2025-W36', '2025-W37', 
                          '2025-W38', '2025-W39', '2025-W40', '2025-W41', '2025-W42', '2025-W43', '2025-W44'],
            'prev_weeks_list': ['2025-W19', '2025-W20', '2025-W21', '2025-W22', '2025-W23', '2025-W24', 
                               '2025-W25', '2025-W26', '2025-W27', '2025-W28', '2025-W29', '2025-W30', '2025-W31']
        },
        {
            'name': 'quarter_yoy',
            'file': 'detailed_summary_quarter_vs_prev_yr_quarter.txt',
            'date_value': '2025-W32-2025-W44',
            'date_granularity': '13WEEKS',
            'comparison_type': 'prev_year',
            'weeks_list': ['2025-W32', '2025-W33', '2025-W34', '2025-W35', '2025-W36', '2025-W37',
                          '2025-W38', '2025-W39', '2025-W40', '2025-W41', '2025-W42', '2025-W43', '2025-W44']
        }
    ]
    
    # Collect all data
    all_data = {}
    
    for comp in comparisons:
        print(f"\n{'='*80}")
        print(f"Processing: {comp['name']}")
        print(f"{'='*80}")
        
        # Parse file
        file_path = script_dir / comp['file']
        file_data = parse_summary_file(file_path)
        print(f"  Parsed {len(file_data)} metrics from file")
        
        # Query table
        table_data = query_table_metrics(
            comp['date_value'],
            comp['date_granularity'],
            comp['comparison_type'],
            comp.get('weeks_list'),
            comp.get('prev_weeks_list')
        )
        print(f"  Queried {len(table_data)} metrics from table")
        
        # Store for comparison
        all_data[comp['name']] = {
            'file': file_data,
            'table': table_data
        }
    
    # Build comparison table
    print(f"\n{'='*80}")
    print("Building Comparison Table")
    print(f"{'='*80}")
    
    comparison_rows = []
    
    for metric in STEERING_METRICS:
        row = {'Metric': metric}
        
        for comp_name in ['week_prev', 'week_yoy', 'month_prev', 'month_yoy', 'quarter_prev', 'quarter_yoy']:
            comp_data = all_data[comp_name]
            
            # Get values from file and table
            file_metric = comp_data['file'].get(metric, {})
            table_metric = comp_data['table'].get(metric, {})
            
            file_current = file_metric.get('current', None)
            file_prev = file_metric.get('prev', None)
            table_current = table_metric.get('current', None)
            table_prev = table_metric.get('prev', None)
            
            # Format values
            row[f'{comp_name}_file_current'] = f"{file_current:.2f}%" if file_current is not None else "N/A"
            row[f'{comp_name}_file_prev'] = f"{file_prev:.2f}%" if file_prev is not None else "N/A"
            row[f'{comp_name}_table_current'] = f"{table_current:.2f}%" if table_current is not None else "N/A"
            row[f'{comp_name}_table_prev'] = f"{table_prev:.2f}%" if table_prev is not None else "N/A"
            
            # Calculate differences
            if file_current is not None and table_current is not None:
                diff_current = abs(file_current - table_current)
                row[f'{comp_name}_diff_current'] = f"{diff_current:.4f}%"
            else:
                row[f'{comp_name}_diff_current'] = "N/A"
            
            if file_prev is not None and table_prev is not None:
                diff_prev = abs(file_prev - table_prev)
                row[f'{comp_name}_diff_prev'] = f"{diff_prev:.4f}%"
            else:
                row[f'{comp_name}_diff_prev'] = "N/A"
        
        comparison_rows.append(row)
    
    # Create DataFrame
    df_comparison = pd.DataFrame(comparison_rows)
    
    # Save to CSV
    output_file = script_dir / 'metrics_comparison_table.csv'
    df_comparison.to_csv(output_file, index=False)
    print(f"\n✅ Comparison table saved to: {output_file}")
    
    # Print summary
    print(f"\n{'='*80}")
    print("Summary Statistics")
    print(f"{'='*80}")
    
    for comp_name in ['week_prev', 'week_yoy', 'month_prev', 'month_yoy', 'quarter_prev', 'quarter_yoy']:
        diff_col = f'{comp_name}_diff_current'
        diffs = []
        for val in df_comparison[diff_col]:
            if val != "N/A":
                diffs.append(float(val.replace('%', '')))
        
        if diffs:
            avg_diff = sum(diffs) / len(diffs)
            max_diff = max(diffs)
            print(f"{comp_name}:")
            print(f"  Average difference: {avg_diff:.4f}%")
            print(f"  Maximum difference: {max_diff:.4f}%")
            print(f"  Metrics compared: {len(diffs)}")
    
    # Display first few rows
    print(f"\n{'='*80}")
    print("Sample Comparison (first 3 metrics)")
    print(f"{'='*80}")
    print(df_comparison[['Metric', 'week_prev_file_current', 'week_prev_table_current', 
                         'week_prev_diff_current']].head(3).to_string(index=False))
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

