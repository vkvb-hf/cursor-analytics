import re

def extract_metric_data(text, metric_name):
    """Extract data for a specific metric from text"""
    pattern = f"={70,}\\n{re.escape(metric_name)}\\n={70,}\\n(.*?)(?=\\n={70,}|$)"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else ""

def parse_cluster_data(text):
    """Parse cluster-level data"""
    clusters = {}
    lines = text.split('\n')
    current_cluster = None
    
    for line in lines:
        if 'For Overall cluster' in line:
            current_cluster = 'Overall'
            clusters[current_cluster] = line
        elif 'For HF-NA cluster' in line:
            current_cluster = 'HF-NA'
            clusters[current_cluster] = line
        elif 'For HF-INTL cluster' in line:
            current_cluster = 'HF-INTL'
            clusters[current_cluster] = line
        elif 'For US-HF cluster' in line:
            current_cluster = 'US-HF'
            clusters[current_cluster] = line
        elif 'For RTE cluster' in line:
            current_cluster = 'RTE'
            clusters[current_cluster] = line
        elif 'For WL cluster' in line:
            current_cluster = 'WL'
            clusters[current_cluster] = line
            
    return clusters

def extract_overall_change(text):
    """Extract Overall cluster percentage change"""
    match = re.search(r'Overall cluster.*?from ([\d.]+)% to ([\d.]+)%.*?([\d.]+)% (increase|decrease)', text)
    if match:
        from_val = float(match.group(1))
        to_val = float(match.group(2))
        change_pct = float(match.group(3))
        direction = match.group(4)
        return from_val, to_val, change_pct, direction
    return None, None, None, None

# Read all files
files = {
    'week_vs_prev': 'outputs/detailed_summary_week_vs_prev_week.txt',
    'month_vs_prev': 'outputs/detailed_summary_month_vs_prev_month.txt',
    'quarter_vs_prev': 'outputs/detailed_summary_quarter_vs_prev_quarter.txt',
    'week_vs_prev_yr': 'outputs/detailed_summary_week_vs_prev_yr_week.txt',
    'month_vs_prev_yr': 'outputs/detailed_summary_month_vs_prev_yr_month.txt',
    'quarter_vs_prev_yr': 'outputs/detailed_summary_quarter_vs_prev_yr_quarter.txt'
}

data = {}
for key, path in files.items():
    with open(path, 'r') as f:
        data[key] = f.read()

# Define metrics
metrics = [
    "1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess",
    "1_Activation (Paid + Referrals) - 1_Checkout Funnel - 2_SelectToSuccess",
    "1_Activation (Paid + Referrals) - 1_Checkout Funnel (backend) - 1_PaymentPageVisitToSuccess",
    "1_Activation (Paid + Referrals) - 2_Voucher Fraud - 1_Total Duplicate Rate",
    "1_Activation (Paid + Referrals) - 2_Voucher Fraud - 2_Total Duplicate Block Rate",
    "1_Activation (Paid + Referrals) - 3_Payment Fraud - 1_Payment Fraud Block Rate",
    "2_Reactivations - 1_ReactivationFunnel - 1_ReactivationRate",
    "3_Active - 1_1_Overall Total Box Candidates - 2_PreDunningAR",
    "3_Active - 1_2_Loyalty: LL0 (Initial charges) - 2_PreDunningAR",
    "3_Active - 1_3_Loyalty: LL0 and LL1+ (Recurring charges) - 2_PreDunningAR",
    "3_Active - 2_1_Boxes Shipped - 0_ShipRate",
    "3_Active - 2_1_Boxes Shipped - 1_RecoveryW0",
    "3_Active - 2_2_Boxes Shipped - 12wk lag - 2_Recovery_12wkCohort",
    "3_Active - 2_2_Boxes Shipped - 12wk lag - 3_DunningAvgNetProfit_12wkCohort"
]

print(f"Processing {len(metrics)} metrics...")
print("Sample metric data extraction test:")

# Test extraction for first metric
test_metric = metrics[0]
week_data = extract_metric_data(data['week_vs_prev'], test_metric)
print(f"\nExtracted week data length for first metric: {len(week_data)} chars")

# Test Overall cluster extraction
from_val, to_val, change_pct, direction = extract_overall_change(week_data)
print(f"Overall: {from_val}% to {to_val}% ({change_pct}% {direction})")

