#!/usr/bin/env python3
"""
Validate the generated steering report files against the payments_hf.payments_p0_metrics table.

This script:
1. Reads the generated report files
2. Queries the actual metrics table for the same periods
3. Compares values and reports discrepancies
"""

import sys
import os
import re
from pathlib import Path
from collections import defaultdict

# Add cursor_databricks directory to path for imports
cursor_databricks_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_dir)
from databricks_api import DatabricksAPI
from config import DATABRICKS_HOST, TOKEN

# Initialize API
db_api = DatabricksAPI()

def parse_report_file(file_path):
    """Parse a report file and extract metric values"""
    metrics_data = defaultdict(list)
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract current week/period from header
    current_match = re.search(r'Current (?:Week|Quarter).*?:\s*([\d\-,W\s]+)', content)
    prev_match = re.search(r'Previous (?:Week|Year Week|Quarter).*?:\s*([\d\-,W\s]+)', content)
    
    current_period = current_match.group(1).strip() if current_match else None
    prev_period = prev_match.group(1).strip() if prev_match else None
    
    # Extract metric summaries
    # Pattern: "For {cluster} cluster, the {metric} {direction} from {prev}% to {current}%"
    pattern = r'For (\w+(?:-\w+)?) cluster, the (.+?) (?:increased|decreased) from ([\d.]+)% to ([\d.]+)%'
    
    for match in re.finditer(pattern, content):
        cluster = match.group(1)
        metric_name = match.group(2)
        prev_value = float(match.group(3))
        current_value = float(match.group(4))
        
        metrics_data[metric_name].append({
            'cluster': cluster,
            'prev_value': prev_value,
            'current_value': current_value
        })
    
    return {
        'current_period': current_period,
        'prev_period': prev_period,
        'metrics': dict(metrics_data)
    }

def query_metrics_table(metric_name, cluster, date_values, comparison_type='prev_period', prev_date_values=None):
    """Query the metrics table for a specific metric
    
    Args:
        metric_name: Full metric name
        cluster: Reporting cluster
        date_values: List of date values (weeks) for current period
        comparison_type: 'prev_period' or 'prev_year'
        prev_date_values: List of date values for previous period (for quarter comparisons)
    """
    
    # Determine which columns to use based on comparison type
    if comparison_type == 'prev_period':
        prev_num_col = 'prev_metric_value_numerator'
        prev_den_col = 'prev_metric_value_denominator'
    elif comparison_type == 'prev_year':
        prev_num_col = 'prev_yr_metric_value_numerator'
        prev_den_col = 'prev_yr_metric_value_denominator'
    else:
        return None
    
    # Map cluster names
    cluster_map = {
        'Overall': 'Overall',
        'HF-NA': 'HF-NA',
        'HF-INTL': 'HF-INTL',
        'RTE': 'RTE',
        'WL': 'WL'
    }
    reporting_cluster = cluster_map.get(cluster, cluster)
    
    # Special metrics that use dimension_value='Good' instead of dimension_name='_Overall'
    SPECIAL_METRICS = ['0_ShipRate', '1_RecoveryW0', '2_Recovery_12wkCohort', '3_DunningAvgNetProfit_12wkCohort']
    
    # Extract metric name from full metric name
    metric_parts = metric_name.split(' - ')
    if len(metric_parts) > 0:
        actual_metric_name = metric_parts[-1]
    else:
        actual_metric_name = metric_name
    
    # Determine if this is a special metric
    is_special = any(sm in actual_metric_name for sm in SPECIAL_METRICS)
    
    # Build query with proper dimension handling
    if is_special:
        dimension_filter = "dimension_value = 'Good'"
    else:
        dimension_filter = "dimension_name = '_Overall'"
    
    # Handle date filter - single week or multiple weeks
    if len(date_values) == 1:
        date_filter = f"date_value = '{date_values[0]}'"
    else:
        # Multiple weeks - use IN clause
        date_list = ','.join([f"'{dv}'" for dv in date_values])
        date_filter = f"date_value IN ({date_list})"
    
    # For quarter comparisons with prev_period, we need to query prev_date_values separately
    if comparison_type == 'prev_period' and prev_date_values:
        # Query current period
        query_current = f"""
        SELECT 
            SUM(current_metric_value_numerator) as current_num,
            SUM(current_metric_value_denominator) as current_den
        FROM payments_hf.payments_p0_metrics
        WHERE reporting_cluster = '{reporting_cluster}'
          AND date_granularity = 'WEEK'
          AND {date_filter}
          AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '{metric_name}'
          AND {dimension_filter}
          AND flag_is_p0 = 'TRUE'
          AND metric_type IN ('ratio', 'dollar-ratio')
        GROUP BY reporting_cluster
        """
        
        # Query previous period
        if len(prev_date_values) == 1:
            prev_date_filter = f"date_value = '{prev_date_values[0]}'"
        else:
            prev_date_list = ','.join([f"'{dv}'" for dv in prev_date_values])
            prev_date_filter = f"date_value IN ({prev_date_list})"
        
        query_prev = f"""
        SELECT 
            SUM(current_metric_value_numerator) as prev_num,
            SUM(current_metric_value_denominator) as prev_den
        FROM payments_hf.payments_p0_metrics
        WHERE reporting_cluster = '{reporting_cluster}'
          AND date_granularity = 'WEEK'
          AND {prev_date_filter}
          AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '{metric_name}'
          AND {dimension_filter}
          AND flag_is_p0 = 'TRUE'
          AND metric_type IN ('ratio', 'dollar-ratio')
        GROUP BY reporting_cluster
        """
        
        try:
            results_current = db_api.run_sql(query_current, display=False)
            results_prev = db_api.run_sql(query_prev, display=False)
            
            if results_current and results_prev and len(results_current) > 0 and len(results_prev) > 0:
                curr_row = results_current[0]
                prev_row = results_prev[0]
                
                current_num = curr_row[0] or 0
                current_den = curr_row[1] or 0
                prev_num = prev_row[0] or 0
                prev_den = prev_row[1] or 0
                
                current_ratio = (current_num / current_den * 100) if current_den > 0 else 0
                prev_ratio = (prev_num / prev_den * 100) if prev_den > 0 else 0
                
                return {
                    'current_value': current_ratio,
                    'prev_value': prev_ratio,
                    'current_num': current_num,
                    'current_den': current_den,
                    'prev_num': prev_num,
                    'prev_den': prev_den
                }
        except Exception as e:
            print(f"   ⚠️  Error querying table: {e}")
            return None
        
        return None
    
    # Single week or year-over-year query
    query = f"""
    SELECT 
        SUM(current_metric_value_numerator) as current_num,
        SUM(current_metric_value_denominator) as current_den,
        SUM({prev_num_col}) as prev_num,
        SUM({prev_den_col}) as prev_den
    FROM payments_hf.payments_p0_metrics
    WHERE reporting_cluster = '{reporting_cluster}'
      AND date_granularity = 'WEEK'
      AND {date_filter}
      AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '{metric_name}'
      AND {dimension_filter}
      AND flag_is_p0 = 'TRUE'
      AND metric_type IN ('ratio', 'dollar-ratio')
    GROUP BY reporting_cluster
    """
    
    try:
        results = db_api.run_sql(query, display=False)
        if results and len(results) > 0:
            row = results[0]
            current_num = row[0] or 0
            current_den = row[1] or 0
            prev_num = row[2] or 0
            prev_den = row[3] or 0
            
            current_ratio = (current_num / current_den * 100) if current_den > 0 else 0
            prev_ratio = (prev_num / prev_den * 100) if prev_den > 0 else 0
            
            return {
                'current_value': current_ratio,
                'prev_value': prev_ratio,
                'current_num': current_num,
                'current_den': current_den,
                'prev_num': prev_num,
                'prev_den': prev_den
            }
    except Exception as e:
        print(f"   ⚠️  Error querying table: {e}")
        return None
    
    return None

def validate_file(file_path, comparison_type):
    """Validate a single report file"""
    print(f"\n{'='*80}")
    print(f"Validating: {Path(file_path).name}")
    print(f"{'='*80}")
    
    # Parse the file
    parsed = parse_report_file(file_path)
    
    if not parsed['current_period']:
        print("⚠️  Could not extract current period from file")
        return False
    
    print(f"Current Period: {parsed['current_period']}")
    print(f"Previous Period: {parsed['prev_period']}")
    
    # Extract date value(s) - handle both single week and multi-week periods
    date_values = []
    is_quarter = ',' in parsed['current_period'] or '13 weeks' in parsed['current_period'].lower()
    
    if is_quarter:
        # Extract all week strings from the period
        week_matches = re.findall(r'(\d{4}-W\d{2})', parsed['current_period'])
        if week_matches:
            date_values = week_matches
            print(f"Quarter comparison detected: {len(date_values)} weeks")
    else:
        # Single week
        week_match = re.search(r'(\d{4}-W\d{2})', parsed['current_period'])
        if week_match:
            date_values = [week_match.group(1)]
    
    if not date_values:
        print("⚠️  Could not extract date value(s) for validation")
        return False
    
    print(f"Using {len(date_values)} date value(s) for validation")
    
    # Extract previous period date values for quarter comparisons
    prev_date_values = None
    if is_quarter and parsed['prev_period']:
        prev_week_matches = re.findall(r'(\d{4}-W\d{2})', parsed['prev_period'])
        if prev_week_matches:
            prev_date_values = prev_week_matches
    
    # Validate each metric
    discrepancies = []
    validated_count = 0
    
    for metric_name, metric_entries in parsed['metrics'].items():
        for entry in metric_entries:
            cluster = entry['cluster']
            file_prev = entry['prev_value']
            file_current = entry['current_value']
            
            # Query the table
            table_data = query_metrics_table(metric_name, cluster, date_values, comparison_type, prev_date_values)
            
            if table_data:
                table_prev = table_data['prev_value']
                table_current = table_data['current_value']
                
                # Compare (allow small rounding differences)
                prev_diff = abs(file_prev - table_prev)
                current_diff = abs(file_current - table_current)
                
                if prev_diff > 0.1 or current_diff > 0.1:
                    discrepancies.append({
                        'metric': metric_name,
                        'cluster': cluster,
                        'file_prev': file_prev,
                        'table_prev': table_prev,
                        'prev_diff': prev_diff,
                        'file_current': file_current,
                        'table_current': table_current,
                        'current_diff': current_diff
                    })
                else:
                    validated_count += 1
            else:
                print(f"   ⚠️  Could not query table for: {metric_name} - {cluster}")
    
    # Report results
    print(f"\n✅ Validation Results:")
    print(f"   Validated: {validated_count} metric/cluster combinations")
    print(f"   Discrepancies: {len(discrepancies)}")
    
    if discrepancies:
        print(f"\n❌ Discrepancies found:")
        for disc in discrepancies[:10]:  # Show first 10
            print(f"   {disc['metric'][:50]}... - {disc['cluster']}")
            print(f"      Prev: File={disc['file_prev']:.2f}%, Table={disc['table_prev']:.2f}% (diff={disc['prev_diff']:.2f}%)")
            print(f"      Current: File={disc['file_current']:.2f}%, Table={disc['table_current']:.2f}% (diff={disc['current_diff']:.2f}%)")
        if len(discrepancies) > 10:
            print(f"   ... and {len(discrepancies) - 10} more")
        return False
    else:
        print(f"✅ All values match!")
        return True

def main():
    """Validate all generated report files"""
    
    script_dir = Path(__file__).parent
    
    # Find all report files
    report_files = {
        'week_prev': script_dir / 'detailed_summary_week_vs_prev_week.txt',
        'week_yoy': script_dir / 'detailed_summary_week_vs_prev_yr_week.txt',
        'quarter_prev': script_dir / 'detailed_summary_quarter_vs_prev_quarter.txt'
    }
    
    print("🔍 Validating Steering Report Files")
    print("=" * 80)
    
    results = {}
    for comp_type, file_path in report_files.items():
        if file_path.exists():
            comparison_type = 'prev_period' if comp_type in ['week_prev', 'quarter_prev'] else 'prev_year'
            results[comp_type] = validate_file(file_path, comparison_type)
        else:
            print(f"\n⚠️  File not found: {file_path.name}")
            results[comp_type] = False
    
    # Summary
    print(f"\n{'='*80}")
    print("VALIDATION SUMMARY")
    print(f"{'='*80}")
    
    all_valid = True
    for comp_type, is_valid in results.items():
        status = "✅ PASS" if is_valid else "❌ FAIL"
        print(f"{status}: {comp_type}")
        if not is_valid:
            all_valid = False
    
    return 0 if all_valid else 1

if __name__ == "__main__":
    sys.exit(main())

