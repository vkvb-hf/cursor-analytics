#!/usr/bin/env python3
"""
Verify table data by comparing CSV row counts with table row counts.
Uses direct SQL queries for faster verification.
"""

import sys
import os
import requests
import base64
from databricks import sql
from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN, DATABRICKS_HOST

def count_csv_rows():
    """Count rows in all CSV files."""
    workspace_path = "/Workspace/Users/visal.kumar@hellofresh.com/adyen-ml-test"
    
    print("=" * 80)
    print("Counting Rows in CSV Files")
    print("=" * 80)
    
    # Get token for Workspace API
    headers = {"Authorization": f"Bearer {TOKEN}"}
    workspace_host = DATABRICKS_HOST
    
    # List files
    list_url = f"{workspace_host}/api/2.0/workspace/list"
    list_response = requests.get(list_url, headers=headers, params={"path": workspace_path})
    
    if list_response.status_code != 200:
        print(f"❌ Failed to list files: {list_response.text}")
        return None
    
    files = list_response.json().get('objects', [])
    csv_files = [f for f in files if f.get('path', '').endswith('.csv')]
    
    print(f"📁 Found {len(csv_files)} CSV files")
    
    total_rows = 0
    file_counts = []
    
    for i, file_info in enumerate(csv_files, 1):
        file_path = file_info['path']
        file_name = os.path.basename(file_path)
        
        if i % 10 == 0 or i <= 5:
            print(f"   Processing [{i}/{len(csv_files)}]: {file_name}")
        
        try:
            # Download file
            export_url = f"{workspace_host}/api/2.0/workspace/export"
            export_response = requests.get(
                export_url, 
                headers=headers, 
                params={"path": file_path, "format": "SOURCE"}
            )
            
            if export_response.status_code == 200:
                data = export_response.json()
                content_b64 = data.get('content', '')
                content = base64.b64decode(content_b64).decode('utf-8')
                
                # Count rows (excluding header and comments)
                lines = content.split('\n')
                data_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
                row_count = len(data_lines) - 1 if len(data_lines) > 0 else 0
                
                file_counts.append({
                    'filename': file_name,
                    'rows': row_count
                })
                total_rows += row_count
            else:
                print(f"   ⚠️  Failed to download {file_name}")
                file_counts.append({
                    'filename': file_name,
                    'rows': 0,
                    'error': export_response.text
                })
        except Exception as e:
            print(f"   ⚠️  Error processing {file_name}: {e}")
            file_counts.append({
                'filename': file_name,
                'rows': 0,
                'error': str(e)
            })
    
    print(f"\n✅ Total rows in CSVs: {total_rows:,}")
    
    return {
        'total_rows': total_rows,
        'file_counts': file_counts,
        'total_files': len(csv_files)
    }


def get_table_counts():
    """Get row counts from the table."""
    table_name = "payments_hf.adyen_ml_test_data"
    
    print("\n" + "=" * 80)
    print("Counting Rows in Table")
    print("=" * 80)
    
    try:
        with sql.connect(
            server_hostname=SERVER_HOSTNAME,
            http_path=HTTP_PATH,
            access_token=TOKEN,
            timeout_seconds=300
        ) as connection:
            
            with connection.cursor() as cursor:
                # Total count
                cursor.execute(f"SELECT COUNT(*) as total_rows FROM {table_name}")
                total_result = cursor.fetchone()
                total_rows = total_result[0] if total_result else 0
                
                print(f"📊 Total rows in table: {total_rows:,}")
                
                # Count by source_filename
                cursor.execute(f"""
                    SELECT source_filename, COUNT(*) as row_count
                    FROM {table_name}
                    GROUP BY source_filename
                    ORDER BY row_count DESC
                """)
                
                filename_counts = []
                for row in cursor.fetchall():
                    filename_counts.append({
                        'filename': row[0],
                        'rows': row[1]
                    })
                
                print(f"📁 Files in table: {len(filename_counts)}")
                
                # Unique filenames
                cursor.execute(f"SELECT COUNT(DISTINCT source_filename) as unique_files FROM {table_name}")
                unique_result = cursor.fetchone()
                unique_files = unique_result[0] if unique_result else 0
                
                print(f"📁 Unique filenames: {unique_files}")
                
                return {
                    'total_rows': total_rows,
                    'filename_counts': filename_counts,
                    'unique_files': unique_files
                }
                
    except Exception as e:
        print(f"❌ Error querying table: {e}")
        import traceback
        traceback.print_exc()
        return None


def compare_counts(csv_counts, table_counts):
    """Compare CSV counts with table counts."""
    print("\n" + "=" * 80)
    print("COMPARISON RESULTS")
    print("=" * 80)
    
    csv_total = csv_counts['total_rows']
    table_total = table_counts['total_rows']
    difference = csv_total - table_total
    
    print(f"\n📊 CSV Files:")
    print(f"   Total files: {csv_counts['total_files']}")
    print(f"   Total rows: {csv_total:,}")
    
    print(f"\n📊 Table:")
    print(f"   Table name: payments_hf.adyen_ml_test_data")
    print(f"   Unique filenames: {table_counts['unique_files']}")
    print(f"   Total rows: {table_total:,}")
    
    print(f"\n🔍 Comparison:")
    print(f"   Difference: {difference:,} rows")
    
    if difference == 0:
        print(f"\n✅ PERFECT MATCH! All {csv_total:,} rows are in the table.")
    elif difference > 0:
        print(f"\n⚠️  Table has {difference:,} fewer rows than CSVs.")
        print(f"   This is expected if duplicates were removed.")
        
        # Check for duplicates
        if difference < csv_total * 0.1:  # Less than 10% difference
            print(f"   ✅ Difference is small ({difference/csv_total*100:.2f}%) - likely just duplicates.")
        else:
            print(f"   ⚠️  Difference is significant ({difference/csv_total*100:.2f}%) - please investigate.")
    else:
        print(f"\n⚠️  Table has {abs(difference):,} more rows than CSVs!")
        print(f"   This should not happen - please investigate!")
    
    # Sample file-by-file comparison
    print(f"\n📄 Sample File Comparison (first 10 files):")
    print("-" * 80)
    
    csv_file_dict = {f['filename']: f['rows'] for f in csv_counts['file_counts']}
    table_file_dict = {f['filename']: f['rows'] for f in table_counts['filename_counts']}
    
    sample_files = list(csv_file_dict.keys())[:10]
    
    for filename in sample_files:
        csv_rows = csv_file_dict.get(filename, 0)
        table_rows = table_file_dict.get(filename, 0)
        diff = csv_rows - table_rows
        
        status = "✅" if diff == 0 else "⚠️"
        print(f"   {status} {filename}")
        print(f"      CSV: {csv_rows:,} rows | Table: {table_rows:,} rows | Diff: {diff:,}")
    
    if len(csv_file_dict) > 10:
        print(f"   ... and {len(csv_file_dict) - 10} more files")


def main():
    """Main function."""
    # Step 1: Count CSV rows
    csv_counts = count_csv_rows()
    if not csv_counts:
        print("❌ Failed to count CSV rows")
        sys.exit(1)
    
    # Step 2: Count table rows
    table_counts = get_table_counts()
    if not table_counts:
        print("❌ Failed to count table rows")
        sys.exit(1)
    
    # Step 3: Compare
    compare_counts(csv_counts, table_counts)
    
    print("\n" + "=" * 80)
    print("✅ Verification complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()


