#!/usr/bin/env python3
"""
Test SQL query with EXPLAIN FORMATTED to check for syntax errors
"""
from databricks import sql
from pathlib import Path
import sys

# Try to import config, fall back to example if not available
try:
    from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN
except ImportError:
    print("⚠️  config.py not found. Please create it from config.py.example")
    print("   See SETUP.md for instructions")
    sys.exit(1)

def test_explain_formatted(sql_file_path):
    """
    Run EXPLAIN FORMATTED on a SQL file to check for syntax errors
    """
    print("="*80)
    print(f"Testing SQL file: {sql_file_path}")
    print("="*80)
    
    # Read SQL file
    try:
        with open(sql_file_path, 'r') as f:
            sql_query = f.read()
    except FileNotFoundError:
        print(f"✗ Error: SQL file not found: {sql_file_path}")
        sys.exit(1)
    
    # Prepend EXPLAIN FORMATTED
    explain_query = f"EXPLAIN FORMATTED\n{sql_query}"
    
    print("\n" + "="*80)
    print("Connecting to Databricks...")
    print("="*80)
    
    try:
        with sql.connect(
            server_hostname=SERVER_HOSTNAME,
            http_path=HTTP_PATH,
            access_token=TOKEN,
            timeout_seconds=120  # Longer timeout for EXPLAIN
        ) as connection:
            
            print("✓ Connected successfully!")
            
            with connection.cursor() as cursor:
                print("\n" + "="*80)
                print("Executing EXPLAIN FORMATTED...")
                print("="*80)
                
                try:
                    cursor.execute(explain_query)
                    result = cursor.fetchall()
                    
                    print("\n✓ EXPLAIN FORMATTED executed successfully!")
                    print("\n" + "="*80)
                    print("Query Plan:")
                    print("="*80)
                    
                    # Print the explain plan
                    for row in result:
                        # Databricks returns explain plan as rows
                        # Each row is typically a string representation
                        print(row)
                    
                    print("\n" + "="*80)
                    print("✓ No syntax errors found!")
                    print("="*80)
                    return True
                    
                except Exception as query_error:
                    print("\n" + "="*80)
                    print("✗ SQL Error Detected:")
                    print("="*80)
                    print(f"Error: {query_error}")
                    print("\nFull error details:")
                    import traceback
                    traceback.print_exc()
                    return False
                
    except Exception as e:
        print(f"\n✗ Connection Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    # Default path to payment_fraud_dashboard.sql
    default_sql_path = Path(__file__).parent.parent.parent / "GitHub" / "ddi-pays-pipelines" / "ddi_pays_pipelines" / "analytics_etl" / "queries" / "payment_fraud_dashboard.sql"
    
    if len(sys.argv) > 1:
        sql_path = Path(sys.argv[1])
    else:
        sql_path = default_sql_path
    
    if not sql_path.exists():
        print(f"✗ Error: SQL file not found: {sql_path}")
        print(f"\nUsage: python {sys.argv[0]} [path/to/query.sql]")
        sys.exit(1)
    
    success = test_explain_formatted(sql_path)
    sys.exit(0 if success else 1)

