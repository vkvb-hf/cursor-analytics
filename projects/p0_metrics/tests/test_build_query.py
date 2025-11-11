#!/usr/bin/env python3
"""
Test what build_metrics_query returns for comparison_type='current'.

This will help us understand if the query structure is correct.
"""

# Simulate the query building logic
SPECIAL_METRICS = ['0_ShipRate', '1_RecoveryW0', '2_Recovery_12wkCohort', '3_DunningAvgNetProfit_12wkCohort']
EXCLUDED_METRICS = [
    '5_DunningBadDebtRate_12wkCohort',
    '6_TotalBadDebtRate_12wkCohort',
    '3_PaymentProcessingFees%',
    '1_ChargeBackRate', 
    '3_PostDunningAR'
]
EXCLUDED_DIMENSIONS = ['LoyaltySegment', 'PaymentMethod_OrderType']

def build_metrics_query_test(date_granularity, comparison_type, date_value_str, weeks_list=None):
    """Test version of build_metrics_query to see what it generates."""
    
    if comparison_type == 'current':
        prev_num_col = 'current_metric_value_numerator'
        prev_den_col = 'current_metric_value_denominator'
        comparison_label = 'Current'
    else:
        raise ValueError(f"Testing only 'current' type")
    
    if date_granularity in ['4WEEKS', '13WEEKS'] and weeks_list:
        weeks_list_str = ','.join([f"'{w}'" for w in weeks_list])
        date_filter = f"date_value IN ({weeks_list_str})"
        date_value_display = date_value_str
    else:
        date_filter = f"date_value = '{date_value_str}'"
        date_value_display = date_value_str
    
    # For 'current' comparison type, we only need current columns (no prev columns)
    if comparison_type == 'current':
        prev_cols_select = ""
    else:
        prev_cols_select = f"""
    SUM(a.{prev_num_col}) AS prev_metric_value_numerator,
    SUM(a.{prev_den_col}) AS prev_metric_value_denominator"""
    
    if date_granularity in ['4WEEKS', '13WEEKS'] and weeks_list:
        group_by_clause = """
      GROUP BY a.reporting_cluster,
        CASE WHEN a.reporting_cluster = 'Overall' THEN "Null" ELSE a.business_unit END,
        CONCAT(a.focus_group, ' - ', a.metric_group, ' - ',a.metric_name),
        CASE 
          WHEN a.metric_name IN ({special_metrics}) THEN '_Overall' 
          ELSE dimension_name 
        END,
        a.dimension_value,
        a.flag_more_is_good,
        a.flag_is_p0,
        a.metric_type
        """.replace('{special_metrics}', ','.join([f"'{m}'" for m in SPECIAL_METRICS]))
    else:
        group_by_clause = "GROUP BY ALL"
    
    metrics_query = f"""
    -- Query for {date_granularity} granularity, {comparison_label}
    SELECT 
    '{date_value_display}' as date_value,
    '{date_granularity}' as date_granularity,
    '{comparison_type}' as comparison_type,
    '{comparison_label}' as comparison_label,
    a.reporting_cluster,
    CASE WHEN a.reporting_cluster = 'Overall' THEN "Null" ELSE a.business_unit END AS business_unit,
    CONCAT(a.focus_group, ' - ', a.metric_group, ' - ',a.metric_name) as metric_final_name,
    CASE 
      WHEN a.metric_name IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])}) THEN '_Overall' 
      ELSE dimension_name 
    END AS dimension_name,
    a.dimension_value,
    a.flag_more_is_good,
    a.flag_is_p0,
    a.metric_type,
    SUM(a.current_metric_value_numerator) AS current_metric_value_numerator,
    SUM(a.current_metric_value_denominator) AS current_metric_value_denominator{prev_cols_select}
    FROM payments_hf.payments_p0_metrics a
    WHERE 1=1
      AND metric_type IN ('ratio', 'dollar-ratio')
      AND metric_name not in ({','.join([f"'{m}'" for m in EXCLUDED_METRICS])})
      AND flag_is_p0 = 'TRUE'
      AND date_granularity = 'WEEK'
      AND dimension_name NOT LIKE '%DeclineReason%'
      AND dimension_name not in ({','.join([f"'{d}'" for d in EXCLUDED_DIMENSIONS])})
      AND (
        (a.metric_name not IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])})) 
        OR (a.metric_name IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])}) AND dimension_value in ('Good'))
        )
      AND {date_filter}
      {group_by_clause}
    UNION ALL
    SELECT 
    '{date_value_display}' as date_value,
    '{date_granularity}' as date_granularity,
    '{comparison_type}' as comparison_type,
    '{comparison_label}' as comparison_label,
    'bu_level' AS reporting_cluster,
    a.business_unit,
    CONCAT(a.focus_group, ' - ', a.metric_group, ' - ',a.metric_name) as metric_final_name,
    a.dimension_name,
    a.dimension_value,
    a.flag_more_is_good,
    a.flag_is_p0,
    a.metric_type,
    SUM(a.current_metric_value_numerator) AS current_metric_value_numerator,
    SUM(a.current_metric_value_denominator) AS current_metric_value_denominator{prev_cols_select}
    FROM payments_hf.payments_p0_metrics a
    WHERE 1=1
      AND metric_type IN ('ratio', 'dollar-ratio')
      AND metric_name not in ({','.join([f"'{m}'" for m in EXCLUDED_METRICS])})
      AND flag_is_p0 = 'TRUE'
      AND date_granularity = 'WEEK'
      AND (
        (a.dimension_name = '_Overall' AND a.metric_name not IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])})) 
        OR (a.metric_name IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])}) AND dimension_value in ('Good'))
        )
      AND reporting_cluster = 'Overall'
      AND {date_filter}
      {group_by_clause.replace('GROUP BY a.reporting_cluster,\n        CASE WHEN a.reporting_cluster = \'Overall\' THEN "Null" ELSE a.business_unit END,', 'GROUP BY a.business_unit,') if 'GROUP BY' in group_by_clause else group_by_clause}
    """
    
    return metrics_query

# Test the query generation
print("="*80)
print("Testing build_metrics_query for comparison_type='current'")
print("="*80)

weeks_list = ['2025-W41', '2025-W42', '2025-W43', '2025-W44']
query = build_metrics_query_test('4WEEKS', 'current', '2025-W41-2025-W44', weeks_list)

print("\nGenerated Query (first 50 lines):")
print("="*80)
lines = query.split('\n')
for i, line in enumerate(lines[:50], 1):
    print(f"{i:3}: {line}")

print("\n" + "="*80)
print("Key observations:")
print("="*80)
print(f"1. prev_cols_select is empty: '{prev_cols_select}'")
print(f"2. Query selects current_metric_value_numerator and current_metric_value_denominator")
print(f"3. No prev_metric_value columns are selected when comparison_type='current'")
print(f"4. This is correct - we'll rename them after the query")

