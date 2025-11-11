#!/usr/bin/env python3
"""
Verify business unit output by comparing with direct table queries
"""

import sys
import os
import re
from pathlib import Path
import pandas as pd

# Add cursor_databricks directory to path for imports
cursor_databricks_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_dir)

try:
    from databricks import sql
    from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN
except ImportError:
    print("⚠️  Could not import config. Using environment variables.")
    SERVER_HOSTNAME = os.getenv('DATABRICKS_SERVER_HOSTNAME')
    HTTP_PATH = os.getenv('DATABRICKS_HTTP_PATH')
    TOKEN = os.getenv('DATABRICKS_TOKEN')

def execute_query(query):
    """Execute SQL query and return results"""
    connection = sql.connect(
        server_hostname=SERVER_HOSTNAME,
        http_path=HTTP_PATH,
        access_token=TOKEN
    )
    
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return result

def parse_bu_from_file(filepath):
    """Parse business unit entries from the output file"""
    bu_entries = []
    
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    content = ''.join(lines)
    
    # Split by period sections (look for "13-Week Period" or "4-Week Period")
    period_sections = re.split(r'={80}\n(13-Week Period|4-Week Period)', content)
    
    for i in range(1, len(period_sections), 2):
        if i + 1 >= len(period_sections):
            break
        
        period_type = period_sections[i]
        period_content = period_sections[i + 1]
        
        # Find period info
        period_match = re.search(r'Current Period: (.*?)\nPrevious Period: (.*?)\n', period_content)
        if not period_match:
            continue
        
        current_period_str = period_match.group(1).strip()
        prev_period_str = period_match.group(2).strip()
        
        # Parse weeks
        current_weeks = [w.strip() for w in current_period_str.split(',')]
        prev_weeks = [w.strip() for w in prev_period_str.split(',')]
        
        # Find all metrics in this period section
        metric_pattern = r'={80}\n([^\n]+)\n={80}(.*?)(?=\n={80}\n[^\n]+\n={80}|$)'
        metric_matches = re.finditer(metric_pattern, period_content, re.DOTALL)
        
        for metric_match in metric_matches:
            metric_name = metric_match.group(1).strip()
            metric_content = metric_match.group(2)
            
            # Find business unit sections
            bu_pattern = r'All business units by change magnitude \(([^)]+)\):\n(.*?)(?=\n\n|All business units|For Overall|Top dimensions)'
            bu_matches = re.finditer(bu_pattern, metric_content, re.DOTALL)
            
            for bu_match in bu_matches:
                cluster = bu_match.group(1)
                entries_text = bu_match.group(2)
                
                # Parse individual entries: "- BU: prev% to current% (change% direction, volume impacted: X)"
                entry_pattern = r'- ([A-Z]{2}): ([\d.]+)% to ([\d.]+)% \(([\d.]+)% (increase|decrease), volume impacted: ([\d.]+[KM]?)\)'
                entry_matches = re.finditer(entry_pattern, entries_text)
                
                for entry_match in entry_matches:
                    bu = entry_match.group(1)
                    prev_pct = float(entry_match.group(2))
                    current_pct = float(entry_match.group(3))
                    change_pct = float(entry_match.group(4))
                    direction = entry_match.group(5)
                    volume = entry_match.group(6)
                    
                    bu_entries.append({
                        'metric_name': metric_name,
                        'cluster': cluster,
                        'business_unit': bu,
                        'prev_pct': prev_pct,
                        'current_pct': current_pct,
                        'change_pct': change_pct,
                        'direction': direction,
                        'volume_impacted': volume,
                        'current_weeks': current_weeks,
                        'prev_weeks': prev_weeks
                    })
    
    return bu_entries

def query_table_for_bu(metric_name, business_unit, weeks_list, prev_weeks_list):
    """Query the table for a specific business unit and metric"""
    
    # Parse metric name to get focus_group, metric_group, metric_name
    # Format: "1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess"
    parts = metric_name.split(' - ')
    if len(parts) != 3:
        print(f"⚠️  Could not parse metric name: {metric_name}")
        return None
    
    focus_group = parts[0].strip()
    metric_group = parts[1].strip()
    metric_name_part = parts[2].strip()
    
    # Build weeks filter
    weeks_str = ','.join([f"'{w}'" for w in weeks_list])
    prev_weeks_str = ','.join([f"'{w}'" for w in prev_weeks_list])
    
    # Query current period
    query_current = f"""
        SELECT
            SUM(current_metric_value_numerator) as current_numerator,
            SUM(current_metric_value_denominator) as current_denominator
        FROM payments_hf.payments_p0_metrics
        WHERE date_value IN ({weeks_str})
            AND date_granularity = 'WEEK'
            AND reporting_cluster = 'Overall'
            AND business_unit = '{business_unit}'
            AND dimension_name = '_Overall'
            AND focus_group = '{focus_group}'
            AND metric_group = '{metric_group}'
            AND metric_name = '{metric_name_part}'
            AND flag_is_p0 = 'TRUE'
            AND metric_type IN ('ratio', 'dollar-ratio')
    """
    
    # Query previous period
    query_prev = f"""
        SELECT
            SUM(current_metric_value_numerator) as prev_numerator,
            SUM(current_metric_value_denominator) as prev_denominator
        FROM payments_hf.payments_p0_metrics
        WHERE date_value IN ({prev_weeks_str})
            AND date_granularity = 'WEEK'
            AND reporting_cluster = 'Overall'
            AND business_unit = '{business_unit}'
            AND dimension_name = '_Overall'
            AND focus_group = '{focus_group}'
            AND metric_group = '{metric_group}'
            AND metric_name = '{metric_name_part}'
            AND flag_is_p0 = 'TRUE'
            AND metric_type IN ('ratio', 'dollar-ratio')
    """
    
    try:
        result_current = execute_query(query_current)
        result_prev = execute_query(query_prev)
        
        if result_current and result_prev:
            current_num = result_current[0][0] if result_current[0][0] else 0
            current_den = result_current[0][1] if result_current[0][1] else 0
            prev_num = result_prev[0][0] if result_prev[0][0] else 0
            prev_den = result_prev[0][1] if result_prev[0][1] else 0
            
            current_ratio = (current_num / current_den * 100) if current_den > 0 else 0
            prev_ratio = (prev_num / prev_den * 100) if prev_den > 0 else 0
            change_pct = ((current_ratio - prev_ratio) / prev_ratio * 100) if prev_ratio > 0 else 0
            
            return {
                'current_pct': current_ratio,
                'prev_pct': prev_ratio,
                'change_pct': change_pct,
                'current_numerator': current_num,
                'current_denominator': current_den,
                'prev_numerator': prev_num,
                'prev_denominator': prev_den
            }
    except Exception as e:
        print(f"Error querying table: {e}")
        import traceback
        traceback.print_exc()
        return None
    
    return None

def main():
    """Main verification function"""
    print("=" * 80)
    print("Verifying Business Unit Output")
    print("=" * 80)
    
    filepath = 'long_term.txt'
    
    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        return
    
    # Parse business unit entries
    bu_entries = parse_bu_from_file(filepath)
    print(f"\n📊 Found {len(bu_entries)} business unit entries in file")
    
    if not bu_entries:
        print("⚠️  No business unit entries found")
        return
    
    # Get sample entries to verify (first 5 unique business units)
    seen = set()
    sample_entries = []
    for entry in bu_entries:
        key = (entry['metric_name'], entry['business_unit'])
        if key not in seen:
            seen.add(key)
            sample_entries.append(entry)
            if len(sample_entries) >= 5:
                break
    
    print(f"\n🔍 Verifying {len(sample_entries)} sample entries...")
    print("=" * 80)
    
    results = []
    for i, entry in enumerate(sample_entries, 1):
        print(f"\n📋 Sample {i}: {entry['business_unit']} ({entry['cluster']} cluster)")
        print(f"   Metric: {entry['metric_name'][:70]}...")
        print(f"   From file: {entry['prev_pct']:.2f}% → {entry['current_pct']:.2f}% ({entry['change_pct']:.2f}% {entry['direction']})")
        print(f"   Period: {len(entry['current_weeks'])} weeks vs {len(entry['prev_weeks'])} weeks")
        
        # Query table
        table_result = query_table_for_bu(
            entry['metric_name'],
            entry['business_unit'],
            entry['current_weeks'],
            entry['prev_weeks']
        )
        
        if table_result:
            print(f"   From table: {table_result['prev_pct']:.2f}% → {table_result['current_pct']:.2f}% ({table_result['change_pct']:.2f}%)")
            
            # Compare
            prev_diff = abs(entry['prev_pct'] - table_result['prev_pct'])
            current_diff = abs(entry['current_pct'] - table_result['current_pct'])
            change_diff = abs(entry['change_pct'] - table_result['change_pct'])
            
            match = prev_diff < 0.1 and current_diff < 0.1 and change_diff < 1.0
            
            if match:
                print(f"   ✅ Match! (differences: prev={prev_diff:.4f}%, current={current_diff:.4f}%, change={change_diff:.4f}%)")
            else:
                print(f"   ⚠️  Mismatch! (differences: prev={prev_diff:.4f}%, current={current_diff:.4f}%, change={change_diff:.4f}%)")
                print(f"   Table details: num={table_result['current_numerator']}, den={table_result['current_denominator']}")
            
            results.append({
                'metric': entry['metric_name'][:50],
                'bu': entry['business_unit'],
                'cluster': entry['cluster'],
                'file_prev': entry['prev_pct'],
                'file_current': entry['current_pct'],
                'file_change': entry['change_pct'],
                'table_prev': table_result['prev_pct'],
                'table_current': table_result['current_pct'],
                'table_change': table_result['change_pct'],
                'prev_diff': prev_diff,
                'current_diff': current_diff,
                'change_diff': change_diff,
                'match': match
            })
        else:
            print(f"   ❌ Could not query table for this entry")
            results.append({
                'metric': entry['metric_name'][:50],
                'bu': entry['business_unit'],
                'cluster': entry['cluster'],
                'file_prev': entry['prev_pct'],
                'file_current': entry['current_pct'],
                'file_change': entry['change_pct'],
                'table_prev': None,
                'table_current': None,
                'table_change': None,
                'prev_diff': None,
                'current_diff': None,
                'change_diff': None,
                'match': False
            })
    
    # Summary
    print("\n" + "=" * 80)
    print("Summary")
    print("=" * 80)
    
    if results:
        df = pd.DataFrame(results)
        matches = df[df['match'] == True]
        mismatches = df[df['match'] == False]
        
        print(f"\n✅ Matches: {len(matches)}/{len(results)}")
        print(f"⚠️  Mismatches: {len(mismatches)}/{len(results)}")
        
        if len(mismatches) > 0:
            print("\nMismatches:")
            print(mismatches[['metric', 'bu', 'file_prev', 'table_prev', 'file_current', 'table_current', 'prev_diff', 'current_diff']].to_string())
        
        # Save results
        df.to_csv('bu_verification_results.csv', index=False)
        print(f"\n📄 Results saved to bu_verification_results.csv")
    
    print("\n" + "=" * 80)
    print("Verification complete")

if __name__ == "__main__":
    main()
