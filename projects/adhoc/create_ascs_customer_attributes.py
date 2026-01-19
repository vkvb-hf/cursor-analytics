#!/usr/bin/env python3
"""
Create payments_hf.ascs_customer_attributes table from SQL file
This script runs the SQL query for 2025-11-01 and creates the table
"""
import sys
import os

# Add cursor_databricks root to path
cursor_databricks_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_root)

from core.create_table import create_table

def main():
    # Path to SQL file
    sql_file_path = "/Users/visal.kumar/Documents/GitHub/ddi-pays-pipelines/ddi_pays_pipelines/analytics_etl/queries/ascs_customer_attributes.sql"
    
    # Table name
    table_name = "payments_hf.ascs_customer_attributes"
    
    print("=" * 80)
    print("Creating ASCS Customer Attributes Table")
    print("=" * 80)
    print(f"SQL File: {sql_file_path}")
    print(f"Table: {table_name}")
    print(f"Date Filter: 2025-11-01")
    print("=" * 80)
    print()
    
    # Create table (will drop if exists)
    success = create_table(
        sql_file_path=sql_file_path,
        table_name=table_name,
        drop_if_exists=True
    )
    
    if success:
        print("\n" + "=" * 80)
        print("✓ SUCCESS: Table created successfully!")
        print("=" * 80)
        return 0
    else:
        print("\n" + "=" * 80)
        print("✗ FAILED: Table creation failed")
        print("=" * 80)
        return 1

if __name__ == "__main__":
    sys.exit(main())

