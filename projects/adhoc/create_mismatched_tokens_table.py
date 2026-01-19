#!/usr/bin/env python3
"""
Create Databricks table from local MISMATCHED_tokens CSV files.

This script:
1. Uploads local CSV files starting with "MISMATCHED_tokens" to Databricks workspace
2. Creates a table from those CSV files

Usage:
    python create_mismatched_tokens_table.py [--table-name SCHEMA.TABLE] [--drop-if-exists]
"""

import os
import sys
import glob
import argparse
import requests
from pathlib import Path

# Add parent directories to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import DATABRICKS_HOST, TOKEN
from core.databricks_workspace import create_workspace_directory, upload_csv_to_workspace
from core.csv_to_table import create_table_from_csvs


def find_local_csv_files(base_dir: str, pattern: str = "MISMATCHED_tokens*.csv") -> list:
    """
    Find local CSV files matching the pattern.
    
    Args:
        base_dir: Base directory to search
        pattern: Glob pattern to match CSV files
    
    Returns:
        List of CSV file paths
    """
    csv_files = glob.glob(os.path.join(base_dir, pattern))
    return sorted(csv_files)


def upload_local_csvs_to_workspace(
    local_csv_files: list,
    workspace_path: str,
    workspace_host: str,
    token: str
) -> dict:
    """
    Upload local CSV files to Databricks workspace.
    
    Args:
        local_csv_files: List of local CSV file paths
        workspace_path: Target workspace directory path
        workspace_host: Databricks workspace hostname
        token: Databricks personal access token
    
    Returns:
        Dictionary with upload results
    """
    print("=" * 80)
    print("Step 1: Uploading CSV files to Databricks workspace")
    print("=" * 80)
    
    results = {
        'success': [],
        'failed': [],
        'total': len(local_csv_files)
    }
    
    # Create workspace directory (including the target directory itself)
    print(f"\n📁 Creating workspace directory: {workspace_path}")
    create_workspace_directory(workspace_path, workspace_host, token)
    # Also create the target directory itself
    headers = {"Authorization": f"Bearer {token}"}
    try:
        mkdir_url = f"{workspace_host}/api/2.0/workspace/mkdirs"
        mkdir_payload = {"path": workspace_path}
        mkdir_response = requests.post(mkdir_url, headers=headers, json=mkdir_payload)
        if mkdir_response.status_code not in [200, 400]:
            mkdir_response.raise_for_status()
    except Exception as e:
        if "RESOURCE_ALREADY_EXISTS" not in str(e):
            print(f"⚠️  Warning creating directory {workspace_path}: {e}")
    print("✅ Directory ready")
    
    # Upload each CSV file
    for idx, csv_file in enumerate(local_csv_files, 1):
        filename = os.path.basename(csv_file)
        file_size_mb = os.path.getsize(csv_file) / (1024 * 1024)
        
        print(f"\n[{idx}/{len(local_csv_files)}] 📤 Uploading: {filename}")
        print(f"   Size: {file_size_mb:.2f} MB")
        
        upload_result = upload_csv_to_workspace(
            csv_file_path=csv_file,
            csv_filename=filename,
            databricks_path=workspace_path,
            workspace_host=workspace_host,
            token=token
        )
        
        if upload_result['success']:
            print(f"   ✅ Success: {upload_result['workspace_path']}")
            results['success'].append({
                'filename': filename,
                'workspace_path': upload_result['workspace_path'],
                'size_mb': upload_result['size_mb']
            })
        else:
            print(f"   ❌ Failed: {upload_result['error']}")
            results['failed'].append({
                'filename': filename,
                'error': upload_result['error']
            })
    
    # Print summary
    print("\n" + "=" * 80)
    print("Upload Summary")
    print("=" * 80)
    print(f"✅ Successfully uploaded: {len(results['success'])}/{results['total']}")
    print(f"❌ Failed: {len(results['failed'])}/{results['total']}")
    
    if results['failed']:
        print(f"\n❌ Failed files:")
        for item in results['failed']:
            print(f"   - {item['filename']}: {item['error']}")
    
    print("=" * 80)
    
    return results


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Create Databricks table from local MISMATCHED_tokens CSV files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage (default table: default.mismatched_tokens)
  python create_mismatched_tokens_table.py
  
  # Custom table name
  python create_mismatched_tokens_table.py --table-name analytics.mismatched_tokens
  
  # Drop existing table if it exists
  python create_mismatched_tokens_table.py --table-name analytics.mismatched_tokens --drop-if-exists
        """
    )
    
    parser.add_argument(
        '--csv-dir',
        default='/Users/visal.kumar/Documents',
        help='Directory containing CSV files (default: /Users/visal.kumar/Documents)'
    )
    parser.add_argument(
        '--workspace-path',
        default='/Workspace/Users/visal.kumar@hellofresh.com/mismatched_tokens',
        help='Target Databricks workspace path for CSV files'
    )
    parser.add_argument(
        '--table-name',
        default='default.mismatched_tokens',
        help='Target table name (format: schema.table_name, default: default.mismatched_tokens)'
    )
    parser.add_argument(
        '--drop-if-exists',
        action='store_true',
        help='Drop table if it exists before creating'
    )
    parser.add_argument(
        '--add-filename',
        action='store_true',
        help='Add source_filename column with CSV filename'
    )
    
    args = parser.parse_args()
    
    print("=" * 80)
    print("Create Table from MISMATCHED_tokens CSV Files")
    print("=" * 80)
    print(f"\n📁 CSV directory: {args.csv_dir}")
    print(f"🎯 Workspace path: {args.workspace_path}")
    print(f"📊 Table name: {args.table_name}")
    print("=" * 80)
    
    # Step 1: Find local CSV files
    print("\n📋 Finding local CSV files...")
    local_csv_files = find_local_csv_files(args.csv_dir, "MISMATCHED_tokens*.csv")
    
    if not local_csv_files:
        print(f"❌ No CSV files found matching pattern 'MISMATCHED_tokens*.csv' in {args.csv_dir}")
        sys.exit(1)
    
    print(f"✅ Found {len(local_csv_files)} CSV file(s):")
    for csv_file in local_csv_files:
        filename = os.path.basename(csv_file)
        file_size_mb = os.path.getsize(csv_file) / (1024 * 1024)
        print(f"   - {filename} ({file_size_mb:.2f} MB)")
    
    # Step 2: Upload CSV files to workspace
    upload_results = upload_local_csvs_to_workspace(
        local_csv_files=local_csv_files,
        workspace_path=args.workspace_path,
        workspace_host=DATABRICKS_HOST,
        token=TOKEN
    )
    
    if len(upload_results['success']) == 0:
        print("\n❌ No files were successfully uploaded. Cannot create table.")
        sys.exit(1)
    
    # Step 3: Create table from uploaded CSV files
    print("\n" + "=" * 80)
    print("Step 2: Creating table from CSV files")
    print("=" * 80)
    
    # Build custom columns if requested
    custom_columns = {}
    if args.add_filename:
        custom_columns['source_filename'] = lambda f: f
    
    success = create_table_from_csvs(
        workspace_path=args.workspace_path,
        table_name=args.table_name,
        custom_columns=custom_columns if custom_columns else None,
        drop_if_exists=args.drop_if_exists,
        verify=True
    )
    
    if success:
        print("\n" + "=" * 80)
        print("✅ SUCCESS: Table created successfully!")
        print("=" * 80)
        print(f"\n📊 Table: {args.table_name}")
        print(f"🌐 View in Databricks: {DATABRICKS_HOST}/#workspace{args.workspace_path}")
        print("=" * 80)
        sys.exit(0)
    else:
        print("\n" + "=" * 80)
        print("❌ FAILED: Table creation failed")
        print("=" * 80)
        sys.exit(1)


if __name__ == "__main__":
    main()

