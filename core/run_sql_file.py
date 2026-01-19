#!/usr/bin/env python3
"""
Execute SQL from files
Usage: python run_sql_file.py <sql_file> [output_format] [limit]
"""
from pathlib import Path
import sys
import os

# Import config - works both when installed as package and when run directly
try:
    from core._config import SERVER_HOSTNAME, HTTP_PATH, TOKEN
except ImportError:
    # Fallback for direct script execution
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN

from core.query_util import print_table

def run_sql_file(sql_file_path, output_format='show', limit=100):
    """
    Run a SQL file against Databricks
    """
    # Lazy import to avoid ImportError when databricks-sql-connector not installed
    from databricks import sql
    
    print("="*80)
    print(f"Reading SQL file: {sql_file_path}")
    print("="*80)
    
    try:
        with open(sql_file_path, 'r') as f:
            sql_query = f.read()
        
        print(f"\nSQL Query:\n{sql_query}\n")
        
    except FileNotFoundError:
        print(f"✗ Error: SQL file not found: {sql_file_path}")
        sys.exit(1)
    
    print("="*80)
    print("Executing query...")
    print("="*80)
    
    try:
        with sql.connect(
            server_hostname=SERVER_HOSTNAME,
            http_path=HTTP_PATH,
            access_token=TOKEN,
            timeout_seconds=60
        ) as connection:
            
            print("✓ Connected successfully!")
            
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                result = cursor.fetchall()
                
                print(f"✓ Query executed successfully")
                print(f"✓ Total rows returned: {len(result)}")
                
                # Output results
                print("\n" + "="*80)
                print(f"Outputting results (format: {output_format})...")
                print("="*80)
                
                if output_format == "show":
                    # Get column names from cursor description
                    column_names = None
                    if cursor.description:
                        column_names = [desc[0] for desc in cursor.description]
                    
                    # Use formatted table display
                    print_table(result, column_names=column_names, limit=limit, 
                               title=f"Results from {Path(sql_file_path).name}")
                
                elif output_format == "csv":
                    import pandas as pd
                    df = pd.DataFrame(result)
                    output_path = f"{Path(sql_file_path).stem}_output.csv"
                    df.to_csv(output_path, index=False)
                    print(f"\n✓ Results saved to: {output_path}")
                
                elif output_format == "json":
                    import pandas as pd
                    df = pd.DataFrame(result)
                    output_path = f"{Path(sql_file_path).stem}_output.json"
                    df.to_json(output_path, orient='records', indent=2)
                    print(f"\n✓ Results saved to: {output_path}")
                
                else:
                    print(f"✗ Unknown output format: {output_format}")
                    print("Supported formats: show, csv, json")
                
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_sql_file.py <sql_file> [output_format] [limit]")
        print("Example: python run_sql_file.py query.sql csv 1000")
        sys.exit(1)
    
    sql_file = sys.argv[1]
    output_format = sys.argv[2] if len(sys.argv) > 2 else "show"
    limit = int(sys.argv[3]) if len(sys.argv) > 3 else 100
    
    run_sql_file(sql_file, output_format, limit)

