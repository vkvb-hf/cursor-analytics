#!/usr/bin/env python3
"""
Generic utility to create Databricks tables from CSV files in workspace.

This module downloads CSV files from workspace, infers schema, creates table,
and loads data using COPY INTO or INSERT statements.

Usage:
    python csv_to_table.py --workspace-path PATH --table-name SCHEMA.TABLE [options]
"""

import os
import sys
import csv
import io
import argparse
import requests
import tempfile
from typing import List, Dict, Callable, Optional, Tuple
from databricks import sql

# Import config - works both when installed as package and when run directly
try:
    from core._config import SERVER_HOSTNAME, HTTP_PATH, TOKEN, DATABRICKS_HOST
except ImportError:
    # Fallback for direct script execution
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN, DATABRICKS_HOST


def get_csv_files_from_workspace(workspace_path: str, workspace_host: str, token: str) -> List[str]:
    """
    Get list of CSV files from Databricks workspace.
    
    Args:
        workspace_path: Workspace directory path
        workspace_host: Databricks workspace hostname
        token: Databricks personal access token
    
    Returns:
        List of CSV file paths
    """
    headers = {'Authorization': f'Bearer {token}'}
    
    try:
        resp = requests.get(
            f'{workspace_host}/api/2.0/workspace/list',
            headers=headers,
            json={'path': workspace_path}
        )
        resp.raise_for_status()
        
        files = [
            f['path'] for f in resp.json().get('objects', [])
            if f.get('path', '').endswith('.csv')
        ]
        return sorted(files)
    except Exception as e:
        print(f"❌ Error listing files: {e}")
        return []


def download_csv_from_workspace(file_path: str, workspace_host: str, token: str) -> Optional[str]:
    """
    Download CSV file content from workspace.
    
    Args:
        file_path: Workspace file path
        workspace_host: Databricks workspace hostname
        token: Databricks personal access token
    
    Returns:
        CSV content as string, or None if error
    """
    headers = {'Authorization': f'Bearer {token}'}
    
    try:
        # Export file from workspace
        export_url = f'{workspace_host}/api/2.0/workspace/export'
        resp = requests.get(
            export_url,
            headers=headers,
            params={'path': file_path, 'format': 'SOURCE'}
        )
        resp.raise_for_status()
        
        # Decode base64 content
        import base64
        content_b64 = resp.json().get('content', '')
        content = base64.b64decode(content_b64).decode('utf-8')
        
        return content
    except Exception as e:
        print(f"⚠️  Error downloading {file_path}: {e}")
        return None


def infer_csv_schema(csv_content: str, sample_rows: int = 100) -> Tuple[List[str], Dict[str, str]]:
    """
    Infer schema from CSV content.
    
    Args:
        csv_content: CSV file content as string
        sample_rows: Number of rows to sample for type inference
    
    Returns:
        Tuple of (column_names, column_types_dict)
    """
    # Remove comment lines (lines starting with #)
    lines = csv_content.split('\n')
    cleaned_lines = [line for line in lines if not line.strip().startswith('#')]
    cleaned_content = '\n'.join(cleaned_lines)
    
    reader = csv.DictReader(io.StringIO(cleaned_content))
    
    # Get column names from header
    column_names = reader.fieldnames or []
    
    # Sample rows for type inference
    sample = []
    for i, row in enumerate(reader):
        if i >= sample_rows:
            break
        sample.append(row)
    
    # Infer types (simple inference)
    column_types = {}
    for col in column_names:
        types_found = set()
        for row in sample:
            value = row.get(col, '').strip()
            if value:
                # Simple type detection
                if value.replace('.', '', 1).replace('-', '', 1).isdigit():
                    if '.' in value or 'E' in value.upper() or 'e' in value:
                        types_found.add('DOUBLE')
                    else:
                        types_found.add('BIGINT')
                elif value.lower() in ('true', 'false'):
                    types_found.add('BOOLEAN')
                elif value.startswith('20') and len(value) >= 10:  # Date-like
                    types_found.add('STRING')  # Keep as string for dates
                else:
                    types_found.add('STRING')
        
        # Default to STRING if ambiguous or empty
        if len(types_found) == 1:
            column_types[col] = list(types_found)[0]
        else:
            column_types[col] = 'STRING'
    
    return column_names, column_types


def sanitize_column_name(col_name: str) -> str:
    """
    Sanitize column name for SQL.
    Replaces spaces and special chars, keeps only alphanumeric and underscores.
    """
    # Replace spaces and special characters with underscores
    sanitized = ''.join(c if c.isalnum() or c == '_' else '_' for c in col_name)
    # Remove consecutive underscores
    while '__' in sanitized:
        sanitized = sanitized.replace('__', '_')
    # Remove leading/trailing underscores
    sanitized = sanitized.strip('_')
    # Ensure it doesn't start with a number
    if sanitized and sanitized[0].isdigit():
        sanitized = '_' + sanitized
    # Fallback if empty
    if not sanitized:
        sanitized = 'col_' + str(hash(col_name))[-8:]
    return sanitized


def create_column_mapping(original_columns: List[str]) -> Dict[str, str]:
    """
    Create mapping from original column names to sanitized names.
    
    Returns:
        Dict mapping original_name -> sanitized_name
    """
    mapping = {}
    seen = set()
    
    for col in original_columns:
        sanitized = sanitize_column_name(col)
        # Handle duplicates
        counter = 1
        original_sanitized = sanitized
        while sanitized in seen:
            sanitized = f"{original_sanitized}_{counter}"
            counter += 1
        seen.add(sanitized)
        mapping[col] = sanitized
    
    return mapping


def create_table_schema_sql(
    table_name: str,
    columns: List[str],
    column_types: Dict[str, str],
    additional_columns: Optional[Dict[str, str]] = None,
    column_mapping: Optional[Dict[str, str]] = None,
    table_location: Optional[str] = None
) -> str:
    """
    Generate CREATE TABLE SQL with schema.
    
    Args:
        table_name: Table name (schema.table)
        columns: List of column names from CSV
        column_types: Dict of column name -> type
        additional_columns: Dict of additional column_name -> type
        column_mapping: Optional mapping from original to sanitized column names
        table_location: Optional custom location for the table
    
    Returns:
        CREATE TABLE SQL statement
    """
    col_defs = []
    
    # Add CSV columns
    for col in columns:
        col_type = column_types.get(col, 'STRING')
        # Use mapped name if provided, otherwise sanitize
        if column_mapping:
            safe_col = column_mapping[col]
        else:
            safe_col = sanitize_column_name(col)
        col_defs.append(f"    `{safe_col}` {col_type}")
    
    # Add additional columns
    if additional_columns:
        for col_name, col_type in additional_columns.items():
            safe_col = f"`{col_name.replace('`', '``')}`"
            col_defs.append(f"    {safe_col} {col_type}")
    
    location_clause = f"\nLOCATION '{table_location}'" if table_location else ""
    
    col_defs_str = ',\n'.join(col_defs)
    sql = f"""CREATE OR REPLACE TABLE {table_name} (
{col_defs_str}
)
USING DELTA{location_clause}
    """
    
    return sql.strip()


def load_csv_data_to_table(
    csv_files: List[str],
    workspace_path: str,
    table_name: str,
    workspace_host: str,
    token: str,
    custom_columns: Optional[Dict[str, Callable[[str], str]]] = None,
    column_mapping: Optional[Dict[str, str]] = None
) -> Dict:
    """
    Load CSV data into table using INSERT statements.
    
    Args:
        csv_files: List of CSV file paths
        table_name: Target table name
        workspace_path: Base workspace path
        workspace_host: Databricks workspace hostname
        token: Databricks personal access token
        custom_columns: Optional dict of column_name -> function(filename)
        column_mapping: Optional mapping from original to sanitized column names
    
    Returns:
        Dictionary with success/failed lists and statistics
    """
    print(f"\n📥 Loading data from {len(csv_files)} CSV file(s)...")
    
    results = {
        'success': [],
        'failed': [],
        'total_files': len(csv_files),
        'total_rows': 0
    }
    
    try:
        with sql.connect(
            server_hostname=SERVER_HOSTNAME,
            http_path=HTTP_PATH,
            access_token=TOKEN,
            timeout_seconds=600
        ) as connection:
            
            with connection.cursor() as cursor:
                for idx, csv_file in enumerate(csv_files, 1):
                    filename = os.path.basename(csv_file)
                    print(f"\n{'='*80}")
                    print(f"[{idx}/{len(csv_files)}] Processing: {filename}")
                    print(f"{'='*80}")
                    import sys
                    sys.stdout.flush()  # Ensure output is visible immediately
                    
                    try:
                        # Download CSV content
                        csv_content = download_csv_from_workspace(csv_file, workspace_host, token)
                        if not csv_content:
                            print(f"   ⚠️  Skipping {filename} (download failed)")
                            results['failed'].append({
                                'filename': filename,
                                'error': 'Download failed',
                                'file_number': idx
                            })
                            continue
                        
                        # Remove comment lines (lines starting with #)
                        lines = csv_content.split('\n')
                        cleaned_lines = [line for line in lines if not line.strip().startswith('#')]
                        cleaned_content = '\n'.join(cleaned_lines)
                        
                        # Parse CSV
                        reader = csv.DictReader(io.StringIO(cleaned_content))
                        column_names = reader.fieldnames or []
                        
                        # Use column mapping if provided, otherwise create new mapping
                        if column_mapping:
                            sanitized_cols = [column_mapping.get(col, sanitize_column_name(col)) for col in column_names]
                        else:
                            sanitized_cols = [sanitize_column_name(col) for col in column_names]
                        
                        # Build INSERT statement with sanitized column names
                        base_cols = ", ".join([f"`{col}`" for col in sanitized_cols])
                        
                        # Add custom columns
                        custom_col_names = []
                        custom_col_values = []
                        if custom_columns:
                            for col_name, col_func in custom_columns.items():
                                custom_col_names.append(f"`{col_name}`")
                                custom_value = col_func(filename)
                                # Escape single quotes
                                escaped_value = custom_value.replace("'", "''")
                                custom_col_values.append(f"'{escaped_value}'")
                        
                        if custom_col_names:
                            all_cols = f"{base_cols}, {', '.join(custom_col_names)}"
                        else:
                            all_cols = base_cols
                        
                        # Prepare VALUES clause
                        rows_to_insert = []
                        row_count = 0
                        
                        for row in reader:
                            values = []
                            for orig_col, sanitized_col in zip(column_names, sanitized_cols):
                                value = row.get(orig_col, '')
                                # Escape single quotes and NULL handling
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
                                print(f"   📦 Inserted batch of 1000 rows...")
                                import sys
                                sys.stdout.flush()  # Ensure output is visible immediately
                        
                        # Insert remaining rows
                        if rows_to_insert:
                            insert_sql = f"""
INSERT INTO {table_name} ({all_cols})
VALUES {', '.join(rows_to_insert)}
                            """.strip()
                            cursor.execute(insert_sql)
                        
                        print(f"\n{'='*80}")
                        print(f"✅ SUCCESSFULLY PROCESSED: {filename}")
                        print(f"   Rows inserted: {row_count:,}")
                        print(f"   File: [{idx}/{len(csv_files)}]")
                        print(f"{'='*80}")
                        import sys
                        sys.stdout.flush()  # Ensure output is visible immediately
                        
                        results['success'].append({
                            'filename': filename,
                            'rows': row_count,
                            'file_number': idx
                        })
                        results['total_rows'] += row_count
                        
                    except Exception as file_error:
                        print(f"\n{'='*80}")
                        print(f"❌ FAILED: {filename}")
                        print(f"   Error: {file_error}")
                        print(f"{'='*80}")
                        import sys
                        sys.stdout.flush()  # Ensure output is visible immediately
                        results['failed'].append({
                            'filename': filename,
                            'error': str(file_error),
                            'file_number': idx
                        })
                        # Continue with next file
                        continue
                
                return results
                
    except Exception as e:
        print(f"\n❌ Error loading data: {e}")
        import traceback
        traceback.print_exc()
        results['failed'].append({'filename': 'ALL', 'error': str(e)})
        return results


def create_table_from_csvs(
    workspace_path: str,
    table_name: str,
    custom_columns: Optional[Dict[str, Callable[[str], str]]] = None,
    drop_if_exists: bool = False,
    verify: bool = True,
    test_mode: bool = False
) -> bool:
    """
    Create Databricks table from CSV files in workspace.
    
    Args:
        workspace_path: Workspace directory containing CSV files
        table_name: Target table name (format: schema.table_name)
        custom_columns: Optional dict of column_name -> function(filename) for custom columns
        drop_if_exists: If True, drop table before creating
        verify: If True, verify table creation and show stats
    
    Returns:
        True if successful, False otherwise
    """
    print("=" * 80)
    print("Create Table from CSV Files")
    print("=" * 80)
    print(f"\n📁 Workspace path: {workspace_path}")
    print(f"🎯 Table name: {table_name}")
    print("=" * 80)
    
    # Step 1: Get list of CSV files
    print("\n📋 Step 1: Getting list of CSV files...")
    csv_files = get_csv_files_from_workspace(workspace_path, DATABRICKS_HOST, TOKEN)
    
    if not csv_files:
        print("❌ No CSV files found!")
        return False
    
    print(f"✅ Found {len(csv_files)} CSV file(s)")
    
    # In test mode, only use first file
    if test_mode:
        csv_files = csv_files[:1]
        print(f"🧪 TEST MODE: Using only first CSV file")
        print(f"   File: {os.path.basename(csv_files[0])}")
    
    # Step 2: Download first CSV to infer schema
    print("\n📝 Step 2: Inferring schema from first CSV file...")
    first_csv_content = download_csv_from_workspace(csv_files[0], DATABRICKS_HOST, TOKEN)
    
    if not first_csv_content:
        print("❌ Could not download first CSV file!")
        return False
    
    column_names, column_types = infer_csv_schema(first_csv_content)
    print(f"✅ Inferred {len(column_names)} columns")
    print(f"   Sample columns: {', '.join(column_names[:5])}...")
    
    # Step 3: Create table with schema
    print("\n🏗️  Step 3: Creating table with schema...")
    
    # Create column mapping (original -> sanitized)
    column_mapping = create_column_mapping(column_names)
    sanitized_column_names = [column_mapping[col] for col in column_names]
    
    # Determine additional column types
    additional_col_types = {}
    if custom_columns:
        for col_name in custom_columns.keys():
            additional_col_types[col_name] = 'STRING'  # Default to STRING for custom columns
    
    # Create type mapping for sanitized columns
    sanitized_column_types = {}
    for orig_col, sanitized_col in column_mapping.items():
        sanitized_column_types[sanitized_col] = column_types.get(orig_col, 'STRING')
    
    # Generate custom location to avoid Delta log conflicts
    # Extract schema and table name
    schema, table = table_name.split('.') if '.' in table_name else ('default', table_name)
    # Use a unique location with timestamp to avoid conflicts
    table_location = f"s3://hf-payments-data-lake-live-main/{schema}/{table}_v2"
    
    create_sql = create_table_schema_sql(
        table_name=table_name,
        columns=sanitized_column_names,
        column_types=sanitized_column_types,
        additional_columns=additional_col_types if additional_col_types else None,
        column_mapping=None,  # Already using sanitized names
        table_location=table_location
    )
    
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
                        print("   Will attempt to create/recreate...")
                
                print("   Creating table...")
                try:
                    cursor.execute(create_sql)
                except Exception as create_error:
                    if "already exists" in str(create_error).lower() or "TABLE_OR_VIEW_ALREADY_EXISTS" in str(create_error):
                        print(f"   ℹ️  Table already exists, skipping creation")
                        print("   Will insert data into existing table...")
                    else:
                        raise
                print("✅ Table created successfully!")
                
                # Show list of files to be processed
                print(f"\n{'='*80}")
                print(f"📋 Files to be processed ({len(csv_files)} total):")
                print(f"{'='*80}")
                for i, csv_file in enumerate(csv_files, 1):
                    filename = os.path.basename(csv_file)
                    print(f"   [{i:3d}/{len(csv_files)}] {filename}")
                print(f"{'='*80}\n")
                import sys
                sys.stdout.flush()
                
                # Step 4: Load data
                load_results = load_csv_data_to_table(
                    csv_files=csv_files,
                    workspace_path=workspace_path,
                    table_name=table_name,
                    workspace_host=DATABRICKS_HOST,
                    token=TOKEN,
                    custom_columns=custom_columns,
                    column_mapping=column_mapping
                )
                
                if not isinstance(load_results, dict) or len(load_results.get('success', [])) == 0:
                    if isinstance(load_results, dict) and load_results.get('failed'):
                        print(f"\n❌ No files were successfully processed")
                        return False
                    return False
                
                if verify:
                    # Verify table
                    print("\n" + "=" * 80)
                    print("📊 Step 5: Verification Summary")
                    print("=" * 80)
                    
                    verify_query = f"SELECT COUNT(*) as row_count FROM {table_name}"
                    cursor.execute(verify_query)
                    result = cursor.fetchall()
                    row_count = result[0][0] if result else 0
                    
                    print(f"\n✅ Files successfully processed: {len(load_results.get('success', []))}/{load_results.get('total_files', 0)}")
                    print(f"❌ Files failed: {len(load_results.get('failed', []))}/{load_results.get('total_files', 0)}")
                    print(f"📊 Total rows in table: {row_count:,}")
                    print(f"📊 Rows inserted by script: {load_results.get('total_rows', 0):,}")
                    
                    # Show sample
                    sample_query = f"SELECT * FROM {table_name} LIMIT 3"
                    cursor.execute(sample_query)
                    columns = [desc[0] for desc in cursor.description]
                    print(f"\n📋 Table has {len(columns)} columns")
                    print(f"   Columns: {', '.join(columns[:10])}...")
                    
                    if custom_columns:
                        print("\n📊 Custom columns summary:")
                        for col_name in custom_columns.keys():
                            distinct_query = f"SELECT COUNT(DISTINCT `{col_name}`) as distinct_count FROM {table_name}"
                            cursor.execute(distinct_query)
                            distinct_result = cursor.fetchall()
                            print(f"   {col_name}: {distinct_result[0][0]} distinct values")
                    
                    # Show successfully processed files
                    if load_results.get('success'):
                        print(f"\n✅ Successfully processed files ({len(load_results['success'])}):")
                        for item in load_results['success'][:10]:
                            print(f"   [{item['file_number']}] {item['filename']} ({item['rows']:,} rows)")
                        if len(load_results['success']) > 10:
                            print(f"   ... and {len(load_results['success']) - 10} more files")
                    
                    # Show failed files
                    if load_results.get('failed'):
                        print(f"\n❌ Failed files ({len(load_results['failed'])}):")
                        for item in load_results['failed'][:10]:
                            print(f"   [{item.get('file_number', '?')}] {item['filename']}: {item['error']}")
                        if len(load_results['failed']) > 10:
                            print(f"   ... and {len(load_results['failed']) - 10} more failures")
                    
                    print("\n" + "=" * 80)
                    print("✅ Table creation and data loading completed!")
                    print("=" * 80)
                
                return True
                
    except Exception as e:
        print(f"\n❌ Error creating table: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(
        description='Create Databricks table from CSV files in workspace',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage
  python csv_to_table.py \\
      --workspace-path "/Workspace/Users/user@example.com/my-data" \\
      --table-name "my_schema.my_table"
  
  # With filename column
  python csv_to_table.py \\
      --workspace-path "/Workspace/Users/user@example.com/my-data" \\
      --table-name "my_schema.my_table" \\
      --add-filename \\
      --drop-if-exists
        """
    )
    
    parser.add_argument(
        '--workspace-path',
        required=True,
        help='Workspace directory path containing CSV files'
    )
    parser.add_argument(
        '--table-name',
        required=True,
        help='Target table name (format: schema.table_name)'
    )
    parser.add_argument(
        '--add-filename',
        action='store_true',
        help='Add source_filename column with CSV filename'
    )
    parser.add_argument(
        '--drop-if-exists',
        action='store_true',
        help='Drop table if it exists before creating'
    )
    parser.add_argument(
        '--no-verify',
        action='store_true',
        help='Skip table verification'
    )
    
    args = parser.parse_args()
    
    # Build custom columns if requested
    custom_columns = {}
    if args.add_filename:
        custom_columns['source_filename'] = lambda f: f
    
    success = create_table_from_csvs(
        workspace_path=args.workspace_path,
        table_name=args.table_name,
        custom_columns=custom_columns if custom_columns else None,
        drop_if_exists=args.drop_if_exists,
        verify=not args.no_verify
    )
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
