#!/usr/bin/env python3
"""
Create or replace a table in Databricks using a SQL file
Usage: python create_table.py <sql_file> <schema.table_name> [--drop-if-exists]
"""
from databricks import sql
from pathlib import Path
import sys
import os
import argparse
# Add parent directory to path for config import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN

def create_table(sql_file_path, table_name, drop_if_exists=False):
    """
    Create or replace a table in Databricks using SQL from a file
    
    Args:
        sql_file_path: Path to SQL file with SELECT statement
        table_name: Target table name in format schema.table_name
        drop_if_exists: If True, drop table first before creating
    """
    print("="*80)
    print(f"Reading SQL file: {sql_file_path}")
    print("="*80)
    
    try:
        with open(sql_file_path, 'r') as f:
            sql_query = f.read()
        
        print(f"\nSQL Query preview (first 200 chars):\n{sql_query[:200]}...\n")
        
    except FileNotFoundError:
        print(f"✗ Error: SQL file not found: {sql_file_path}")
        sys.exit(1)
    
    # Parse schema and table
    if '.' not in table_name:
        print(f"✗ Error: Table name must be in format 'schema.table_name'")
        sys.exit(1)
    
    schema, table = table_name.split('.', 1)
    
    print("="*80)
    print(f"Creating table: {table_name}")
    print("="*80)
    
    try:
        with sql.connect(
            server_hostname=SERVER_HOSTNAME,
            http_path=HTTP_PATH,
            access_token=TOKEN,
            timeout_seconds=120
        ) as connection:
            
            print("✓ Connected successfully!")
            
            with connection.cursor() as cursor:
                # Drop table if requested
                if drop_if_exists:
                    drop_sql = f"DROP TABLE IF EXISTS {schema}.{table}"
                    print(f"\nDropping existing table...")
                    cursor.execute(drop_sql)
                    print("✓ Table dropped (if it existed)")
                
                # Create or replace table
                create_sql = f"CREATE OR REPLACE TABLE {table_name} AS\n{sql_query}"
                
                print(f"\nCreating table...")
                print(f"This may take a moment...")
                cursor.execute(create_sql)
                
                print("✓ Table created successfully!")
                
                # Get table info
                print("\n" + "="*80)
                print("Verifying table creation...")
                print("="*80)
                
                verify_query = f"SELECT COUNT(*) as row_count FROM {table_name}"
                cursor.execute(verify_query)
                result = cursor.fetchall()
                row_count = result[0][0] if result else 0
                
                print(f"✓ Table {table_name} created with {row_count} rows")
                
                # Show sample data
                sample_query = f"SELECT * FROM {table_name} LIMIT 5"
                cursor.execute(sample_query)
                sample_result = cursor.fetchall()
                
                print("\n" + "="*80)
                print("Sample data (first 5 rows):")
                print("="*80)
                for i, row in enumerate(sample_result, 1):
                    print(f"Row {i}: {row}")
                
                return True
                
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Create a table in Databricks from a SQL file'
    )
    parser.add_argument('sql_file', help='Path to SQL file with SELECT statement')
    parser.add_argument('table_name', help='Target table name (schema.table_name)')
    parser.add_argument('--drop-if-exists', action='store_true',
                       help='Drop table if it exists before creating')
    
    args = parser.parse_args()
    
    success = create_table(args.sql_file, args.table_name, args.drop_if_exists)
    sys.exit(0 if success else 1)

