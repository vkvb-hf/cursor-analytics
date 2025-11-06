#!/usr/bin/env python3
"""
Generate steering report from detailed_summary_combined.txt
Focuses on week-over-week with month-over-month trend commentary and year-over-year context
"""
import re
from pathlib import Path
from collections import defaultdict

def parse_summary_file(file_path):
    """Parse the detailed summary file and extract key metrics"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract week number
    week_match = re.search(r'2025-W(\d+)', content)
    week_num = week_match.group(1) if week_match else 'XX'
    
    metrics_data = {}
    current_metric = None
    current_comparison = None
    current_section = None
    
    lines = content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Detect metric header (starts with number_)
        if re.match(r'^\d+_.*', line):
            metric_name = line
            if metric_name not in metrics_data:
                metrics_data[metric_name] = {
                    'week_prev': {},
                    'week_yoy': {},
                    'month_prev': {},
                    'month_yoy': {}
                }
            current_metric = metric_name
            i += 1
            continue
        
        # Detect comparison section
        if '--- vs Previous Period' in line and current_metric:
            current_comparison = 'week_prev'
            current_section = None
            i += 1
            continue
        
        if '--- vs Previous Year' in line and current_metric:
            current_comparison = 'week_yoy'
            current_section = None
            i += 1
            continue
        
        if '--- 4-Week Period vs Previous 4-Week Period' in line and current_metric:
            current_comparison = 'month_prev'
            current_section = None
            i += 1
            continue
        
        if '--- 4-Week Period vs Previous Year 4-Week Period' in line and current_metric:
            current_comparison = 'month_yoy'
            current_section = None
            i += 1
            continue
        
        # Parse cluster line
        if current_metric and current_comparison:
            cluster_match = re.search(r'^For (\w+(?:-\w+)?) cluster, the', line)
            if cluster_match:
                cluster = cluster_match.group(1)
                # Extract: "increased/decreased from X% to Y%" or "from €X to €Y"
                # Try percentage format first
                pct_match = re.search(r'from ([\d.]+)% to ([\d.]+)%', line)
                if not pct_match:
                    # Try Euro format
                    pct_match = re.search(r'from €([\d.]+) to €([\d.]+)', line)
                
                rel_match = re.search(r'a (slight|notable|substantial) ([\d.]+)% (increase|decrease)', line)
                vol_match = re.search(r'volume impacted: ([\d.K]+)', line)
                sig_match = 'not statistically significant' not in line
                impact_match = re.search(r'(positive|negative) business impact', line)
                
                if pct_match and rel_match:
                    prev_val = float(pct_match.group(1))
                    curr_val = float(pct_match.group(2))
                    rel_change = float(rel_match.group(2))
                    direction = rel_match.group(3)
                    volume = vol_match.group(1) if vol_match else '0'
                    impact = impact_match.group(1) if impact_match else 'neutral'
                    is_euro = '€' in line
                    
                    if cluster not in metrics_data[current_metric][current_comparison]:
                        metrics_data[current_metric][current_comparison][cluster] = {
                            'prev': prev_val,
                            'curr': curr_val,
                            'rel_change': rel_change,
                            'direction': direction,
                            'volume': volume,
                            'significant': sig_match,
                            'impact': impact,
                            'is_euro': is_euro,
                            'business_units': [],
                            'dimensions': []
                        }
        
        # Track if we're in business units or dimensions section
        if 'All business units by change magnitude:' in line:
            current_section = 'business_units'
            i += 1
            continue
        
        if 'Top dimensions by change magnitude:' in line:
            current_section = 'dimensions'
            i += 1
            continue
        
        # Parse business unit lines (2-3 letter codes like US, CA, FR, DE, FJ, etc.)
        # Also handle Euro amounts for Dunning Profit
        if current_metric and current_comparison and current_section == 'business_units':
            # Try percentage format first
            bu_match = re.search(r'^- ([A-Z]{2,3}): ([\d.]+)% to ([\d.]+)% \(([\d.]+)% (increase|decrease)', line)
            if not bu_match:
                # Try Euro format
                bu_match = re.search(r'^- ([A-Z]{2,3}): €([\d.]+) to €([\d.]+) \(([\d.]+)% (increase|decrease)', line)
            if bu_match:
                bu = bu_match.group(1)
                prev_pct = float(bu_match.group(2))
                curr_pct = float(bu_match.group(3))
                rel_change = float(bu_match.group(4))
                direction = bu_match.group(5)
                vol_match = re.search(r'volume impacted: ([\d.K]+)', line)
                volume = vol_match.group(1) if vol_match else '0'
                
                # Find the most recent cluster context (find the last cluster mentioned)
                # We need to track which cluster we're currently in
                # For now, store in the last cluster we saw
                last_cluster = None
                for cluster in reversed(['Overall', 'HF-NA', 'HF-INTL', 'US-HF', 'RTE', 'WL']):
                    if cluster in metrics_data[current_metric][current_comparison]:
                        last_cluster = cluster
                        break
                
                if last_cluster:
                    if 'business_units' not in metrics_data[current_metric][current_comparison][last_cluster]:
                        metrics_data[current_metric][current_comparison][last_cluster]['business_units'] = []
                    # Check if this is Euro format
                    is_euro = '€' in line
                    metrics_data[current_metric][current_comparison][last_cluster]['business_units'].append({
                        'name': bu,
                        'prev': prev_pct,
                        'curr': curr_pct,
                        'rel_change': rel_change,
                        'direction': direction,
                        'volume': volume,
                        'is_euro': is_euro
                    })
        
        # Parse dimension lines (longer names like "PaymentMethod Apple Pay", "ChannelCategory Paid")
        if current_metric and current_comparison and current_section == 'dimensions' and re.match(r'^- \w+.*:', line):
            dim_match = re.search(r'^- ([\w\s]+): ([\d.]+)% to ([\d.]+)% \(([\d.]+)% (increase|decrease)', line)
            if dim_match and len(dim_match.group(1)) > 3:  # Filter out 2-letter codes
                dim_name = dim_match.group(1).strip()
                prev_pct = float(dim_match.group(2))
                curr_pct = float(dim_match.group(3))
                rel_change = float(dim_match.group(4))
                direction = dim_match.group(5)
                vol_match = re.search(r'volume impacted: ([\d.K]+)', line)
                volume = vol_match.group(1) if vol_match else '0'
                
                # Find the most recent cluster context
                for cluster in ['Overall', 'HF-NA', 'HF-INTL', 'US-HF', 'RTE', 'WL']:
                    if cluster in metrics_data[current_metric][current_comparison]:
                        if 'dimensions' not in metrics_data[current_metric][current_comparison][cluster]:
                            metrics_data[current_metric][current_comparison][cluster]['dimensions'] = []
                        metrics_data[current_metric][current_comparison][cluster]['dimensions'].append({
                            'name': dim_name,
                            'prev': prev_pct,
                            'curr': curr_pct,
                            'rel_change': rel_change,
                            'direction': direction,
                            'volume': volume
                        })
                        break
        
        i += 1
    
    return metrics_data, week_num

def generate_steering_report(metrics_data, week_num):
    """Generate the steering report markdown"""
    
    # Metric order from REPORT_PROMPT.md
    metric_order = [
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
    
    # Extract metric short names for table
    metric_short_names = {
        '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess': 'Payment Page Visit to Success',
        '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 2_SelectToSuccess': 'Select to Success',
        '1_Activation (Paid + Referrals) - 1_Checkout Funnel (backend) - 1_PaymentPageVisitToSuccess': 'Payment Page Visit to Success (backend)',
        '1_Activation (Paid + Referrals) - 2_Voucher Fraud - 1_Total Duplicate Rate': 'Duplicate Rate',
        '1_Activation (Paid + Referrals) - 2_Voucher Fraud - 2_Total Duplicate Block Rate': 'Duplicate Block Rate',
        '1_Activation (Paid + Referrals) - 3_Payment Fraud - 1_Payment Fraud Block Rate': 'Payment Fraud Block Rate',
        '2_Reactivations - 1_ReactivationFunnel - 1_ReactivationRate': 'Reactivation Rate',
        '3_Active - 1_1_Overall Total Box Candidates - 2_PreDunningAR': 'AR Pre Dunning',
        '3_Active - 1_2_Loyalty: LL0 (Initial charges) - 2_PreDunningAR': 'Acceptance LL0',
        '3_Active - 1_3_Loyalty: LL0 and LL1+ (Recurring charges) - 2_PreDunningAR': 'Acceptance LL0 and LL1+',
        '3_Active - 2_1_Boxes Shipped - 0_ShipRate': 'Ship Rate',
        '3_Active - 2_1_Boxes Shipped - 1_RecoveryW0': 'Recovery W0',
        '3_Active - 2_2_Boxes Shipped - 12wk lag - 2_Recovery_12wkCohort': 'Recovery W12 - DW21',
        '3_Active - 2_2_Boxes Shipped - 12wk lag - 3_DunningAvgNetProfit_12wkCohort': 'Dunning Profit'
    }
    
    # Generate key insights
    insights = generate_key_insights(metrics_data)
    
    # Start building the report
    report = f"""# 2025-W{week_num} Weekly Payments Metrics Steering

## Key Insights
{insights}

| Metrics | Anomaly/Callout | Notes |
| :--- | :--- | :--- |
"""
    
    # Generate table rows for each metric
    for metric_full in metric_order:
        if metric_full not in metrics_data:
            continue
        
        metric_short = metric_short_names.get(metric_full, metric_full.split(' - ')[-1])
        data = metrics_data[metric_full]
        
        # Build callout focusing on week-over-week with month trend and year context
        callout = build_callout(data, metric_full)
        
        report += f"| **{metric_short}** | {callout} | |\n"
    
    return report

def generate_key_insights(metrics_data):
    """Generate key insights section"""
    critical_issues = []
    positive_trends = []
    risk_shifts = []
    emerging_concerns = []
    
    # Analyze metrics for insights
    for metric_name, data in metrics_data.items():
        week_prev = data.get('week_prev', {})
        month_yoy = data.get('month_yoy', {})
        metric_short = metric_name.split(' - ')[-1]
        
        # Critical issues: significant negative week-over-week changes
        if 'Overall' in week_prev:
            overall = week_prev['Overall']
            if overall['significant'] and overall['impact'] == 'negative' and overall['rel_change'] > 5:
                critical_issues.append(f"{metric_short}: {overall['rel_change']:.1f}% {overall['direction']} WoW")
        
        # Positive trends: significant positive week-over-week
        if 'Overall' in week_prev:
            overall = week_prev['Overall']
            if overall['significant'] and overall['impact'] == 'positive' and overall['rel_change'] > 3:
                positive_trends.append(f"{metric_short}: {overall['rel_change']:.1f}% {overall['direction']} WoW")
        
        # Risk shifts: year-over-year 4-week declines
        if 'Overall' in month_yoy:
            overall_mth = month_yoy['Overall']
            if overall_mth['rel_change'] > 10 and overall_mth['direction'] == 'decrease':
                risk_shifts.append(f"{metric_short}: {overall_mth['rel_change']:.1f}% below year-ago baseline (4-wk)")
    
    # Format insights (limit to 1000 chars total)
    result = []
    if critical_issues:
        result.append(f"- **Critical Issues:** {', '.join(critical_issues[:2])}")
    if positive_trends:
        result.append(f"- **Positive Trends:** {', '.join(positive_trends[:2])}")
    if risk_shifts:
        result.append(f"- **Risk Shifts:** {', '.join(risk_shifts[:2])}")
    if not result:
        result.append("- **Overall:** Mixed performance across clusters with week-over-week improvements in checkout metrics")
    
    return '\n'.join(result)

def build_callout(data, metric_name):
    """Build the callout text for a metric focusing on week-over-week with month trend commentary"""
    week_prev = data.get('week_prev', {})
    month_prev = data.get('month_prev', {})
    month_yoy = data.get('month_yoy', {})
    
    clusters = ['Overall', 'HF-NA', 'HF-INTL', 'US-HF', 'RTE', 'WL']
    callout_parts = []
    
    # Week-over-week for each cluster (primary focus)
    is_euro_metric = False
    for cluster in clusters:
        if cluster in week_prev:
            info = week_prev[cluster]
            arrow = "↑" if info['direction'] == 'increase' else "↓"
            sig = "significant" if info['significant'] else "not significant"
            if info.get('is_euro', False):
                is_euro_metric = True
                callout_parts.append(f"- **{cluster}**: €{info['curr']:.2f} vs €{info['prev']:.2f} ({arrow}{info['rel_change']:.2f}%, {sig}, volume: {info['volume']})")
            else:
                callout_parts.append(f"- **{cluster}**: {info['curr']:.2f}% vs {info['prev']:.2f}% ({arrow}{info['rel_change']:.2f}%, {sig}, volume: {info['volume']})")
    
    # Add month-over-month trend commentary
    # Use month_prev if available (when prev != 0.00%), otherwise use month_yoy for context
    if 'Overall' in month_prev:
        mth_info = month_prev['Overall']
        prev_mth_pct = mth_info.get('prev', 0)
        current_mth_pct = mth_info.get('curr', 0)
        # Only show if we have valid previous period data (not 0.00%)
        if prev_mth_pct > 0.01 and current_mth_pct > 0:
            trend_arrow = "↑" if mth_info['direction'] == 'increase' else "↓"
            if is_euro_metric:
                callout_parts.append(f"<br><br>**4-Week Trend:** Current 4-week €{current_mth_pct:.2f} vs previous 4-week €{prev_mth_pct:.2f} ({trend_arrow}{mth_info['rel_change']:.1f}%)")
            else:
                callout_parts.append(f"<br><br>**4-Week Trend:** Current 4-week {current_mth_pct:.2f}% vs previous 4-week {prev_mth_pct:.2f}% ({trend_arrow}{mth_info['rel_change']:.1f}%)")
    
    # Add year-over-year context as expected baseline
    if 'Overall' in month_yoy:
        yoy_info = month_yoy['Overall']
        expected_pct = yoy_info.get('prev', 0)  # Previous year value as expected baseline
        current_mth = yoy_info.get('curr', 0)  # Current 4-week period
        if expected_pct > 0 and current_mth > 0:
            trend_arrow = "↑" if yoy_info['direction'] == 'increase' else "↓"
            if is_euro_metric:
                callout_parts.append(f" vs year-ago baseline €{expected_pct:.2f} ({trend_arrow}{yoy_info['rel_change']:.1f}%)")
            else:
                callout_parts.append(f" vs year-ago baseline {expected_pct:.2f}% ({trend_arrow}{yoy_info['rel_change']:.1f}%)")
    
    # Add business unit breakdowns for significant changes (top 3)
    # Check HF-NA and HF-INTL first as they typically have business units
    for cluster in ['HF-NA', 'HF-INTL', 'Overall']:
        if cluster in week_prev and week_prev[cluster].get('business_units'):
            bus = week_prev[cluster]['business_units']
            if bus:
                top_bus = sorted(bus, key=lambda x: abs(x['rel_change']), reverse=True)[:3]
                if top_bus and any(abs(b['rel_change']) > 5 for b in top_bus):
                    bu_parts = []
                    for bu in top_bus:
                        arrow = "↑" if bu['direction'] == 'increase' else "↓"
                        if bu.get('is_euro', False):
                            bu_parts.append(f"{bu['name']}: €{bu['curr']:.2f} to €{bu['prev']:.2f} ({arrow}{bu['rel_change']:.2f}%, volume impacted: {bu['volume']})")
                        else:
                            bu_parts.append(f"{bu['name']}: {bu['curr']:.2f}% to {bu['prev']:.2f}% ({arrow}{bu['rel_change']:.2f}%, volume impacted: {bu['volume']})")
                    if bu_parts:
                        callout_parts.append(f"<br><br>**Top Business Units ({cluster}):** {', '.join(bu_parts)}")
                    break
    
    # Add dimension breakdowns for significant changes (top 2)
    if 'Overall' in week_prev and week_prev['Overall']['significant']:
        if 'Overall' in week_prev and week_prev['Overall'].get('dimensions'):
            dims = week_prev['Overall']['dimensions']
            if dims:
                top_dims = sorted(dims, key=lambda x: abs(x['rel_change']), reverse=True)[:2]
                if top_dims and any(abs(d['rel_change']) > 10 for d in top_dims):
                    dim_parts = []
                    for dim in top_dims:
                        arrow = "↑" if dim['direction'] == 'increase' else "↓"
                        dim_parts.append(f"{dim['name']}: {dim['curr']:.2f}% to {dim['prev']:.2f}% ({arrow}{dim['rel_change']:.2f}%, volume impacted: {dim['volume']})")
                    if dim_parts:
                        callout_parts.append(f"<br><br>**Key Dimensions:** {', '.join(dim_parts)}")
    
    # Limit total length to ~1000 characters
    callout_text = '<br>'.join(callout_parts)
    if len(callout_text) > 1000:
        # Truncate to keep essential info
        parts = callout_text.split('<br>')
        truncated = []
        char_count = 0
        for part in parts:
            if char_count + len(part) > 1000:
                break
            truncated.append(part)
            char_count += len(part) + 4  # +4 for <br>
        callout_text = '<br>'.join(truncated)
    
    return callout_text if callout_parts else "No significant changes detected"

if __name__ == '__main__':
    summary_file = Path(__file__).parent / 'detailed_summary_combined.txt'
    metrics_data, week_num = parse_summary_file(summary_file)
    report = generate_steering_report(metrics_data, week_num)
    
    output_file = Path(__file__).parent / f'W{week_num}_steering.md'
    with open(output_file, 'w') as f:
        f.write(report)
    
    print(f"Generated steering report: {output_file}")
    print(f"Week: 2025-W{week_num}")
    print(f"Metrics processed: {len(metrics_data)}")
