#!/usr/bin/env python3
"""Inspect the table structure and sample data."""

import sys
import os
from databricks import sql
# Add parent directory to path for config import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN

def inspect_table():
    """Inspect the table."""
    table_name = "payments_hf.adyen_ml_test_data"
    
    print("=" * 80)
    print("Table Inspection")
    print("=" * 80)
    print(f"Table: {table_name}\n")
    
    try:
        with sql.connect(
            server_hostname=SERVER_HOSTNAME,
            http_path=HTTP_PATH,
            access_token=TOKEN,
            timeout_seconds=300
        ) as connection:
            
            with connection.cursor() as cursor:
                # Get table schema
                print("📋 Table Schema:")
                print("-" * 80)
                cursor.execute(f"DESCRIBE {table_name}")
                for row in cursor.fetchall():
                    print(f"   {row[0]:<30} {row[1]:<20} {row[2]}")
                
                # Total count
                print(f"\n📊 Row Count:")
                print("-" * 80)
                cursor.execute(f"SELECT COUNT(*) as total_rows FROM {table_name}")
                total = cursor.fetchone()[0]
                print(f"   Total rows: {total:,}")
                
                # Check for source_filename column
                print(f"\n🔍 Checking source_filename column:")
                print("-" * 80)
                cursor.execute(f"SELECT COUNT(DISTINCT source_filename) as unique_files FROM {table_name}")
                unique_files = cursor.fetchone()[0]
                print(f"   Unique filenames: {unique_files}")
                
                # Sample of source_filename values
                cursor.execute(f"""
                    SELECT source_filename, COUNT(*) as row_count
                    FROM {table_name}
                    GROUP BY source_filename
                    ORDER BY row_count DESC
                    LIMIT 10
                """)
                
                print(f"\n📄 Sample source_filename distribution:")
                print("-" * 80)
                rows = cursor.fetchall()
                if rows:
                    for row in rows:
                        filename = row[0] if row[0] else "(NULL)"
                        count = row[1]
                        print(f"   {filename:<60} {count:,} rows")
                else:
                    print("   No data found")
                
                # Check NULL values in source_filename
                cursor.execute(f"SELECT COUNT(*) as null_count FROM {table_name} WHERE source_filename IS NULL")
                null_count = cursor.fetchone()[0]
                print(f"\n   NULL source_filename values: {null_count:,}")
                
                # Sample rows
                print(f"\n📄 Sample Rows (first 3):")
                print("-" * 80)
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 3")
                columns = [desc[0] for desc in cursor.description]
                
                # Print header
                print("   | " + " | ".join(col[:15] for col in columns[:8]) + " |")
                print("   " + "-" * 100)
                
                # Print rows
                for row in cursor.fetchall():
                    values = [str(val)[:15] if val else "NULL" for val in row[:8]]
                    print("   | " + " | ".join(values) + " |")
                
                # Check risk_profile column
                print(f"\n📊 Risk Profile Distribution:")
                print("-" * 80)
                cursor.execute(f"""
                    SELECT risk_profile, COUNT(*) as row_count
                    FROM {table_name}
                    GROUP BY risk_profile
                    ORDER BY row_count DESC
                """)
                for row in cursor.fetchall():
                    profile = row[0] if row[0] else "(NULL)"
                    count = row[1]
                    print(f"   {profile:<30} {count:,} rows")
                
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    inspect_table()


