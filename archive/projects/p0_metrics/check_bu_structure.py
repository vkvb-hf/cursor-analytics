#!/usr/bin/env python3
"""
Check how business units are stored in the payments_p0_metrics table
"""

import sys
import os
from pathlib import Path

# Add cursor_databricks directory to path for imports
cursor_databricks_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_dir)
from databricks import sql
from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN
import pandas as pd

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
                return pd.DataFrame([dict(zip(columns, row)) for row in result])
            return pd.DataFrame()

print("="*80)
print("Checking Business Unit Data Structure")
print("="*80)

# Check what reporting_cluster values exist for business units
check_structure_query = """
    SELECT DISTINCT
        reporting_cluster,
        business_unit,
        COUNT(*) as row_count
    FROM payments_hf.payments_p0_metrics
    WHERE date_value IN ('2025-W41', '2025-W42', '2025-W43', '2025-W44')
      AND date_granularity = 'WEEK'
      AND business_unit IS NOT NULL
      AND business_unit != 'Null'
    GROUP BY reporting_cluster, business_unit
    ORDER BY reporting_cluster, business_unit
    LIMIT 50
"""

print("\n📊 Checking reporting_cluster values for business units...")
structure_df = execute_query(check_structure_query)
print(f"   Found {len(structure_df)} unique combinations")
if not structure_df.empty:
    print(f"\n   Sample data:")
    print(structure_df.head(20).to_string())
    print(f"\n   Reporting clusters: {structure_df['reporting_cluster'].unique().tolist()}")

# Check for a specific business unit
test_bu_query = """
    SELECT 
        reporting_cluster,
        business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
        dimension_name,
        SUM(current_metric_value_numerator) AS current_numerator,
        SUM(current_metric_value_denominator) AS current_denominator
    FROM payments_hf.payments_p0_metrics
    WHERE date_value IN ('2025-W41', '2025-W42', '2025-W43', '2025-W44')
      AND date_granularity = 'WEEK'
      AND business_unit = 'US'
      AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
      AND dimension_name = '_Overall'
    GROUP BY reporting_cluster, business_unit, 
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name),
        dimension_name
"""

print(f"\n📊 Checking specific business unit (US)...")
test_bu_df = execute_query(test_bu_query)
if not test_bu_df.empty:
    print(f"   Found {len(test_bu_df)} rows for US business unit")
    print(test_bu_df.to_string())
else:
    print(f"   ⚠️  No data found for US business unit")

# Check what the actual query in the notebook would return
print(f"\n📊 Checking what the notebook query would return...")
notebook_query = f"""
    SELECT 
        reporting_cluster,
        CASE WHEN reporting_cluster = 'Overall' THEN "Null" ELSE business_unit END AS business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
        dimension_name,
        SUM(current_metric_value_numerator) AS current_numerator,
        SUM(current_metric_value_denominator) AS current_denominator
    FROM payments_hf.payments_p0_metrics
    WHERE date_value IN ('2025-W41', '2025-W42', '2025-W43', '2025-W44')
      AND date_granularity = 'WEEK'
      AND reporting_cluster = 'bu_level'
      AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
      AND dimension_name = '_Overall'
    GROUP BY reporting_cluster,
        CASE WHEN reporting_cluster = 'Overall' THEN "Null" ELSE business_unit END,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name),
        dimension_name
"""

notebook_df = execute_query(notebook_query)
if not notebook_df.empty:
    print(f"   Found {len(notebook_df)} rows with reporting_cluster = 'bu_level'")
    print(notebook_df.head(10).to_string())
else:
    print(f"   ⚠️  No data found with reporting_cluster = 'bu_level'")
    
    # Check if bu_level exists at all
    check_bu_level = """
        SELECT DISTINCT reporting_cluster
        FROM payments_hf.payments_p0_metrics
        WHERE date_value IN ('2025-W41', '2025-W42', '2025-W43', '2025-W44')
          AND date_granularity = 'WEEK'
        LIMIT 20
    """
    bu_level_df = execute_query(check_bu_level)
    print(f"\n   Available reporting_cluster values:")
    print(bu_level_df.to_string())


