#!/usr/bin/env python3
"""
Remove duplicate records from payments_hf.adyen_ml_test_data table.
Ensures uniqueness at PSP_Reference level.
"""

import sys
from databricks import sql
from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN


def deduplicate_table(table_name: str = "payments_hf.adyen_ml_test_data", 
                      unique_column: str = "PSP_Reference",
                      dry_run: bool = False):
    """
    Remove duplicate records from a table, keeping only one row per unique_column.
    
    Args:
        table_name: Full table name (schema.table)
        unique_column: Column that should be unique
        dry_run: If True, only report what would be removed without making changes
    """
    print("=" * 80)
    print("Deduplicate Table")
    print("=" * 80)
    print(f"Table: {table_name}")
    print(f"Unique column: {unique_column}")
    if dry_run:
        print("🔍 DRY RUN MODE - No changes will be made")
    print("=" * 80)
    
    try:
        with sql.connect(
            server_hostname=SERVER_HOSTNAME,
            http_path=HTTP_PATH,
            access_token=TOKEN,
            timeout_seconds=600
        ) as connection:
            
            with connection.cursor() as cursor:
                # Step 1: Check current state
                print("\n📊 Step 1: Checking current table state...")
                print("-" * 80)
                
                cursor.execute(f"SELECT COUNT(*) as total_rows FROM {table_name}")
                total_rows_before = cursor.fetchone()[0]
                print(f"   Total rows: {total_rows_before:,}")
                
                cursor.execute(f"SELECT COUNT(DISTINCT {unique_column}) as unique_values FROM {table_name}")
                unique_values = cursor.fetchone()[0]
                print(f"   Unique {unique_column}s: {unique_values:,}")
                
                duplicates_count = total_rows_before - unique_values
                
                if duplicates_count == 0:
                    print(f"\n✅ No duplicates found. Table is already unique at {unique_column}.")
                    return True
                
                print(f"\n⚠️  Found {duplicates_count:,} duplicate rows")
                print(f"   ({duplicates_count / total_rows_before * 100:.2f}% duplicates)")
                
                # Step 2: Show sample duplicates
                print(f"\n🔍 Step 2: Sample duplicates by {unique_column}...")
                print("-" * 80)
                cursor.execute(f"""
                    SELECT 
                        {unique_column},
                        COUNT(*) as duplicate_count
                    FROM {table_name}
                    GROUP BY {unique_column}
                    HAVING COUNT(*) > 1
                    ORDER BY duplicate_count DESC
                    LIMIT 10
                """)
                
                sample_duplicates = cursor.fetchall()
                print(f"   Top 10 {unique_column}s with duplicates:")
                print(f"   {'Value':<30} {'Count':>10}")
                print("-" * 80)
                for row in sample_duplicates:
                    value = str(row[0] or 'NULL')[:28]
                    count = row[1]
                    print(f"   {value:<30} {count:>10,}")
                
                if dry_run:
                    print(f"\n🔍 DRY RUN: Would remove {duplicates_count:,} duplicate rows")
                    print(f"   Final row count would be: {unique_values:,}")
                    return True
                
                # Step 3: Get all column names for the deduplication query
                print(f"\n🔧 Step 3: Getting table schema...")
                print("-" * 80)
                
                # Use a SELECT LIMIT 0 to get column names from cursor description
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
                if cursor.description:
                    all_columns = [desc[0] for desc in cursor.description]
                else:
                    # Fallback: use DESCRIBE and filter properly
                    cursor.execute(f"DESCRIBE {table_name}")
                    columns_info = cursor.fetchall()
                    # DESCRIBE returns: col_name, data_type, comment
                    # Filter out metadata rows (those starting with # or empty)
                    all_columns = []
                    for col in columns_info:
                        col_name = col[0] if col and len(col) > 0 else None
                        data_type = col[1] if col and len(col) > 1 else None
                        # Valid column if it has a name, has a data type, and doesn't start with #
                        if (col_name and data_type and 
                            not col_name.strip().startswith('#') and 
                            col_name.strip()):
                            all_columns.append(col_name)
                
                print(f"   Found {len(all_columns)} columns")
                
                # Step 4: Create deduplicated table
                print(f"\n🔄 Step 4: Creating deduplicated table...")
                print("-" * 80)
                print("   Using ROW_NUMBER() to keep first occurrence of each duplicate")
                print("   This may take a few minutes for large tables...")
                
                # Create deduplication query using ROW_NUMBER
                # Keep the first row per unique_column (using stable ordering for deterministic results)
                # We'll order by unique_column itself plus a few key columns if available
                columns_list = ", ".join([f"`{col}`" for col in all_columns])
                
                # Try to find a timestamp/date column for better ordering
                # Otherwise, order by unique_column + first few columns for deterministic results
                timestamp_columns = [col for col in all_columns if any(term in col.lower() 
                                     for term in ['date', 'time', 'created', 'updated', 'timestamp'])]
                
                if timestamp_columns:
                    # Use the first timestamp column found for ordering
                    order_by_col = f"`{timestamp_columns[0]}` DESC"
                    print(f"   Using {timestamp_columns[0]} for deterministic ordering")
                else:
                    # Fallback: order by unique_column itself (keeps arbitrary but deterministic row)
                    order_by_col = f"`{unique_column}`"
                    print(f"   Using {unique_column} for deterministic ordering")
                
                deduplication_query = f"""
                    CREATE OR REPLACE TABLE {table_name} AS
                    SELECT 
                        {columns_list}
                    FROM (
                        SELECT 
                            {columns_list},
                            ROW_NUMBER() OVER (
                                PARTITION BY `{unique_column}` 
                                ORDER BY {order_by_col}
                            ) as row_num
                        FROM {table_name}
                    ) ranked
                    WHERE row_num = 1
                """
                
                print(f"\n   Executing deduplication query...")
                cursor.execute(deduplication_query)
                print(f"   ✅ Deduplication query executed")
                
                # Step 5: Verify results
                print(f"\n📊 Step 5: Verifying deduplication...")
                print("-" * 80)
                
                cursor.execute(f"SELECT COUNT(*) as total_rows FROM {table_name}")
                total_rows_after = cursor.fetchone()[0]
                
                cursor.execute(f"SELECT COUNT(DISTINCT {unique_column}) as unique_values FROM {table_name}")
                unique_values_after = cursor.fetchone()[0]
                
                print(f"   Rows before: {total_rows_before:,}")
                print(f"   Rows after:  {total_rows_after:,}")
                print(f"   Rows removed: {total_rows_before - total_rows_after:,}")
                print(f"   Unique {unique_column}s: {unique_values_after:,}")
                
                if unique_values_after == total_rows_after:
                    print(f"\n✅ Success! Table is now unique at {unique_column}.")
                    print(f"   Removed {duplicates_count:,} duplicate rows")
                    return True
                else:
                    print(f"\n⚠️  Warning: Table still has duplicates")
                    print(f"   This should not happen - please investigate")
                    return False
                
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main function with command-line interface."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Remove duplicate records from payments_hf.adyen_ml_test_data table',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Remove duplicates (default table and column)
  python deduplicate_table.py
  
  # Dry run to see what would be removed
  python deduplicate_table.py --dry-run
  
  # Custom table and column
  python deduplicate_table.py --table schema.table_name --column unique_col
        """
    )
    
    parser.add_argument(
        '--table',
        type=str,
        default='payments_hf.adyen_ml_test_data',
        help='Table name to deduplicate (default: payments_hf.adyen_ml_test_data)'
    )
    
    parser.add_argument(
        '--column',
        type=str,
        default='PSP_Reference',
        help='Column that should be unique (default: PSP_Reference)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Only show what would be removed, without making changes'
    )
    
    args = parser.parse_args()
    
    success = deduplicate_table(
        table_name=args.table,
        unique_column=args.column,
        dry_run=args.dry_run
    )
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

