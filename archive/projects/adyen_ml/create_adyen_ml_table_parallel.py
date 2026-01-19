#!/usr/bin/env python3
"""
Create payments_hf.adyen_ml_test_info table with parallel processing.

This script processes CSV files in parallel using threading for faster upload.
The table is partitioned by source_filename for better performance.
"""

import sys
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from csv_to_table import (
    get_csv_files_from_workspace, 
    download_csv_from_workspace,
    sanitize_column_name,
    create_column_mapping,
    DATABRICKS_HOST,
    TOKEN,
    SERVER_HOSTNAME,
    HTTP_PATH
)
from config import TOKEN as CONFIG_TOKEN
import databricks.sql as sql
import csv
import io

# Risk profile mapping
RISK_PROFILE_MAPPING = {
    'THLH73H2VSWDN842': 'Jade1314 CANADA ML',
    'QNN7MK9V6T5T87F3': 'Very_High_ecomm',
    'TBDLJCJZX8LLWWF3': 'Medium_ecomm',
    'J2M3VKGZMHZNZ4Q9': 'Medium',
    'DXPLDK9V6T5T87F3': 'High_ecomm',
    'QLKKNG4S2Q9428Q9': 'Very_High',
    'ZDGX3H4S2Q9428Q9': 'High'
}


def extract_profile_reference(filename: str) -> str:
    """Extract profile reference from filename."""
    parts = filename.split('_')
    if len(parts) >= 2:
        return parts[1]
    return 'Unknown'


def get_risk_profile(filename: str) -> str:
    """Get risk profile from filename."""
    profile_ref = extract_profile_reference(filename)
    return RISK_PROFILE_MAPPING.get(profile_ref, 'Unknown')


# Global lock for printing
print_lock = Lock()


def safe_print(*args, **kwargs):
    """Thread-safe print function."""
    with print_lock:
        print(*args, **kwargs)
        sys.stdout.flush()


def process_single_file(file_info):
    """Process a single CSV file and insert into table."""
    idx, csv_file, table_name, workspace_host, token, column_mapping, custom_columns = file_info
    
    filename = os.path.basename(csv_file)
    
    try:
        safe_print(f"\n{'='*80}")
        safe_print(f"[{idx[0]}/{idx[1]}] 🚀 STARTING: {filename}")
        safe_print(f"{'='*80}")
        
        # Download CSV content
        csv_content = download_csv_from_workspace(csv_file, workspace_host, token)
        if not csv_content:
            safe_print(f"   ⚠️  [{idx[0]}/{idx[1]}] Skipping {filename} (download failed)")
            return {'success': False, 'filename': filename, 'error': 'Download failed', 'rows': 0}
        
        # Remove comment lines
        lines = csv_content.split('\n')
        cleaned_lines = [line for line in lines if not line.strip().startswith('#')]
        cleaned_content = '\n'.join(cleaned_lines)
        
        # Parse CSV
        reader = csv.DictReader(io.StringIO(cleaned_content))
        column_names = reader.fieldnames or []
        
        # Use column mapping
        sanitized_cols = [column_mapping.get(col, sanitize_column_name(col)) for col in column_names]
        
        # Build INSERT statement
        base_cols = ", ".join([f"`{col}`" for col in sanitized_cols])
        
        # Add custom columns
        custom_col_names = []
        custom_col_values = []
        if custom_columns:
            for col_name, col_func in custom_columns.items():
                custom_col_names.append(f"`{col_name}`")
                custom_value = col_func(filename)
                escaped_value = custom_value.replace("'", "''")
                custom_col_values.append(f"'{escaped_value}'")
        
        if custom_col_names:
            all_cols = f"{base_cols}, {', '.join(custom_col_names)}"
        else:
            all_cols = base_cols
        
        # Create connection for this thread
        connection = sql.connect(
            server_hostname=SERVER_HOSTNAME,
            http_path=HTTP_PATH,
            access_token=token,
            timeout_seconds=600
        )
        
        cursor = connection.cursor()
        
        # Prepare VALUES clause
        rows_to_insert = []
        row_count = 0
        
        for row in reader:
            values = []
            for orig_col, sanitized_col in zip(column_names, sanitized_cols):
                value = row.get(orig_col, '')
                if value == '' or value is None:
                    values.append('NULL')
                else:
                    escaped = str(value).replace("'", "''")
                    values.append(f"'{escaped}'")
            
            if custom_col_values:
                values.extend(custom_col_values)
            
            rows_to_insert.append(f"({', '.join(values)})")
            row_count += 1
            
            # Insert in batches of 1000 rows
            if len(rows_to_insert) >= 1000:
                insert_sql = f"""
INSERT INTO {table_name} ({all_cols})
VALUES {', '.join(rows_to_insert)}
                """.strip()
                cursor.execute(insert_sql)
                rows_to_insert = []
                safe_print(f"   📦 [{idx[0]}/{idx[1]}] {filename}: Inserted batch of 1000 rows...")
        
        # Insert remaining rows
        if rows_to_insert:
            insert_sql = f"""
INSERT INTO {table_name} ({all_cols})
VALUES {', '.join(rows_to_insert)}
            """.strip()
            cursor.execute(insert_sql)
        
        cursor.close()
        connection.close()
        
        safe_print(f"\n{'='*80}")
        safe_print(f"✅ [{idx[0]}/{idx[1]}] COMPLETED: {filename}")
        safe_print(f"   📊 Rows inserted: {row_count:,}")
        safe_print(f"{'='*80}")
        
        return {'success': True, 'filename': filename, 'rows': row_count, 'file_number': idx[0]}
        
    except Exception as e:
        safe_print(f"\n{'='*80}")
        safe_print(f"❌ [{idx[0]}/{idx[1]}] FAILED: {filename}")
        safe_print(f"   Error: {e}")
        safe_print(f"{'='*80}")
        return {'success': False, 'filename': filename, 'error': str(e), 'rows': 0, 'file_number': idx[0]}


def create_partitioned_table_from_csvs(
    workspace_path: str,
    table_name: str,
    custom_columns: dict = None,
    drop_if_exists: bool = False,
    max_workers: int = 5
) -> bool:
    """
    Create partitioned Databricks table from CSV files using parallel processing.
    """
    print("=" * 80)
    print("Create Partitioned Table from CSV Files (Parallel Processing)")
    print("=" * 80)
    print(f"\n📁 Workspace path: {workspace_path}")
    print(f"🎯 Table name: {table_name}")
    print(f"⚡ Parallel workers: {max_workers}")
    print("=" * 80)
    
    # Step 1: Get list of CSV files
    print("\n📋 Step 1: Getting list of CSV files...")
    csv_files = get_csv_files_from_workspace(workspace_path, DATABRICKS_HOST, TOKEN)
    
    if not csv_files:
        print("❌ No CSV files found!")
        return False
    
    print(f"✅ Found {len(csv_files)} CSV file(s)")
    
    # Show all files
    print(f"\n{'='*80}")
    print(f"📋 Files to be processed ({len(csv_files)} total):")
    print(f"{'='*80}")
    for i, csv_file in enumerate(csv_files, 1):
        filename = os.path.basename(csv_file)
        print(f"   [{i:3d}/{len(csv_files)}] {filename}")
    print(f"{'='*80}\n")
    sys.stdout.flush()
    
    # Step 2: Download first CSV to infer schema
    print("\n📝 Step 2: Inferring schema from first CSV file...")
    first_csv_content = download_csv_from_workspace(csv_files[0], DATABRICKS_HOST, TOKEN)
    
    if not first_csv_content:
        print("❌ Could not download first CSV file!")
        return False
    
    # Parse first CSV to get schema
    lines = first_csv_content.split('\n')
    cleaned_lines = [line for line in lines if not line.strip().startswith('#')]
    cleaned_content = '\n'.join(cleaned_lines)
    reader = csv.DictReader(io.StringIO(cleaned_content))
    column_names = list(reader.fieldnames or [])
    
    # Create column mapping
    column_mapping = create_column_mapping(column_names)
    sanitized_column_names = [column_mapping[col] for col in column_names]
    
    # Determine column types (simplified - all STRING for now)
    column_types = {}
    for col in column_names:
        column_types[col] = 'STRING'
    
    sanitized_column_types = {}
    for orig_col, sanitized_col in column_mapping.items():
        sanitized_column_types[sanitized_col] = 'STRING'
    
    # Add custom columns
    additional_col_types = {}
    if custom_columns:
        for col_name in custom_columns.keys():
            additional_col_types[col_name] = 'STRING'
    
    # Step 3: Create partitioned table
    print("\n🏗️  Step 3: Creating partitioned table with schema...")
    
    # Build column definitions
    col_defs = []
    for col in sanitized_column_names:
        col_defs.append(f"    `{col}` STRING")
    
    # Add custom columns
    if additional_col_types:
        for col_name in additional_col_types.keys():
            col_defs.append(f"    `{col_name}` STRING")
    
    schema, table = table_name.split('.') if '.' in table_name else ('default', table_name)
    table_location = f"s3://hf-payments-data-lake-live-main/{schema}/{table}_v2"
    
    create_sql = f"""CREATE OR REPLACE TABLE {table_name} (
{',\n'.join(col_defs)}
)
USING DELTA
PARTITIONED BY (source_filename)
LOCATION '{table_location}'
    """
    
    try:
        with sql.connect(
            server_hostname=SERVER_HOSTNAME,
            http_path=HTTP_PATH,
            access_token=TOKEN,
            timeout_seconds=600
        ) as connection:
            
            with connection.cursor() as cursor:
                if drop_if_exists:
                    print("   Dropping existing table if it exists...")
                    try:
                        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
                        print("   ✅ Table dropped successfully")
                    except Exception as drop_error:
                        print(f"   ⚠️  Warning: Could not drop table: {drop_error}")
                
                print("   Creating partitioned table...")
                cursor.execute(create_sql)
                print("✅ Partitioned table created successfully!")
                print("   📊 Table is partitioned by: source_filename")
                
                # Step 4: Process files in parallel
                print(f"\n{'='*80}")
                print(f"⚡ Step 4: Processing {len(csv_files)} files in parallel ({max_workers} workers)...")
                print(f"{'='*80}\n")
                sys.stdout.flush()
                
                # Prepare file info for parallel processing
                file_info_list = [
                    ((idx, len(csv_files)), csv_file, table_name, DATABRICKS_HOST, TOKEN, column_mapping, custom_columns)
                    for idx, csv_file in enumerate(csv_files, 1)
                ]
                
                results = {'success': [], 'failed': [], 'total_rows': 0}
                
                # Process files in parallel
                with ThreadPoolExecutor(max_workers=max_workers) as executor:
                    future_to_file = {
                        executor.submit(process_single_file, file_info): file_info[0][0]
                        for file_info in file_info_list
                    }
                    
                    for future in as_completed(future_to_file):
                        result = future.result()
                        if result['success']:
                            results['success'].append(result)
                            results['total_rows'] += result['rows']
                        else:
                            results['failed'].append(result)
                
                # Final summary
                print(f"\n{'='*80}")
                print("📊 Final Summary")
                print(f"{'='*80}")
                print(f"✅ Files successfully processed: {len(results['success'])}/{len(csv_files)}")
                print(f"❌ Files failed: {len(results['failed'])}/{len(csv_files)}")
                print(f"📊 Total rows inserted: {results['total_rows']:,}")
                
                # Show some successful files
                if results['success']:
                    print(f"\n✅ Sample successfully processed files:")
                    for item in sorted(results['success'], key=lambda x: x['file_number'])[:10]:
                        print(f"   [{item['file_number']}] {item['filename']} ({item['rows']:,} rows)")
                    if len(results['success']) > 10:
                        print(f"   ... and {len(results['success']) - 10} more files")
                
                # Show failed files
                if results['failed']:
                    print(f"\n❌ Failed files:")
                    for item in results['failed']:
                        print(f"   [{item.get('file_number', '?')}] {item['filename']}: {item['error']}")
                
                # Verify table
                verify_query = f"SELECT COUNT(*) as row_count FROM {table_name}"
                cursor.execute(verify_query)
                result = cursor.fetchall()
                row_count = result[0][0] if result else 0
                print(f"\n📊 Total rows in table: {row_count:,}")
                
                print("\n" + "=" * 80)
                print("✅ Table creation and data loading completed!")
                print("=" * 80)
                
                return True
                
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Create Adyen ML Test Info table with parallel processing')
    parser.add_argument('--drop-if-exists', action='store_true', help='Drop table if it exists')
    parser.add_argument('--workers', type=int, default=5, help='Number of parallel workers (default: 5)')
    
    args = parser.parse_args()
    
    workspace_path = "/Workspace/Users/visal.kumar@hellofresh.com/adyen-ml-test"
    table_name = "payments_hf.adyen_ml_test_info"
    
    custom_columns = {
        'source_filename': lambda f: f,
        'profile_reference': extract_profile_reference,
        'risk_profile': get_risk_profile
    }
    
    success = create_partitioned_table_from_csvs(
        workspace_path=workspace_path,
        table_name=table_name,
        custom_columns=custom_columns,
        drop_if_exists=args.drop_if_exists,
        max_workers=args.workers
    )
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
