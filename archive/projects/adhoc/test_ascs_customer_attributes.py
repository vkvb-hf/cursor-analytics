#!/usr/bin/env python3
"""
Test ascs_customer_attributes.sql with EXPLAIN FORMATTED to check for errors
"""
import sys
from pathlib import Path

# Add parent directory to path
script_dir = Path(__file__).parent
parent_dir = script_dir.parent.parent
sys.path.insert(0, str(parent_dir))

from core.query_util import run_query

def test_explain_formatted():
    """Run EXPLAIN FORMATTED on the SQL query"""
    # Use absolute path from Documents directory
    sql_file = Path("/Users/visal.kumar/Documents/GitHub/ddi-pays-pipelines/ddi_pays_pipelines/analytics_etl/queries/ascs_customer_attributes.sql")
    
    print("="*80)
    print(f"Testing SQL file: {sql_file}")
    print("="*80)
    
    # Read SQL file
    try:
        with open(sql_file, 'r') as f:
            sql_query = f.read()
    except FileNotFoundError:
        print(f"✗ Error: SQL file not found: {sql_file}")
        return False
    
    # Prepend EXPLAIN FORMATTED
    explain_query = f"EXPLAIN FORMATTED\n{sql_query}"
    
    print("\n" + "="*80)
    print("Executing EXPLAIN FORMATTED...")
    print("="*80 + "\n")
    
    try:
        run_query(explain_query, title="Query Plan")
        print("\n" + "="*80)
        print("✓ EXPLAIN FORMATTED executed successfully - no syntax errors!")
        print("="*80)
        return True
    except Exception as e:
        print("\n" + "="*80)
        print("✗ SQL Error Detected:")
        print("="*80)
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_explain_formatted()
    sys.exit(0 if success else 1)

