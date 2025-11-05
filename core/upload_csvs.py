#!/usr/bin/env python3
"""
Upload CSV files to Databricks workspace.

Usage:
    python upload_csvs.py [--extract-dir EXTRACT_DIR] [--test]
"""

import os
import sys
import argparse
import tempfile
from typing import Dict
# Add parent directory to path for config import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATABRICKS_HOST, TOKEN
from core.databricks_workspace import create_workspace_directory, upload_csv_to_workspace


def upload_csv_files(
    extract_dir: str,
    databricks_path: str,
    workspace_host: str,
    token: str,
    test_mode: bool = False
) -> Dict:
    """
    Upload all CSV files from extract directory to Databricks workspace.
    
    Args:
        extract_dir: Directory containing CSV files
        databricks_path: Target workspace path
        workspace_host: Databricks workspace hostname
        token: Databricks personal access token
        test_mode: If True, only upload the largest file
    
    Returns:
        Dictionary with upload results
    """
    results = {
        'success': [],
        'failed': [],
        'total': 0,
        'total_size_mb': 0
    }
    
    if not os.path.exists(extract_dir):
        print(f"❌ Error: Directory not found: {extract_dir}")
        return results
    
    csv_files = [f for f in os.listdir(extract_dir) if f.lower().endswith('.csv')]
    
    if not csv_files:
        print(f"⚠️  No CSV files found in: {extract_dir}")
        return results
    
    # In test mode, only upload the largest file
    if test_mode:
        csv_info = []
        for csv_file in csv_files:
            csv_path = os.path.join(extract_dir, csv_file)
            csv_info.append({
                'filename': csv_file,
                'path': csv_path,
                'size': os.path.getsize(csv_path)
            })
        csv_info.sort(key=lambda x: x['size'], reverse=True)
        csv_files = [csv_info[0]['filename']]
        print(f"🧪 TEST MODE: Uploading only largest file ({csv_files[0]})")
    
    results['total'] = len(csv_files)
    print(f"📦 Found {len(csv_files)} CSV file(s) to upload")
    print("=" * 80)
    
    # Create workspace directory structure
    create_workspace_directory(databricks_path, workspace_host, token)
    
    # Upload each CSV file
    for idx, csv_file in enumerate(csv_files, 1):
        csv_path = os.path.join(extract_dir, csv_file)
        file_size_mb = os.path.getsize(csv_path) / (1024 * 1024)
        
        print(f"\n[{idx}/{len(csv_files)}] 📤 Uploading: {csv_file}")
        print(f"   Size: {file_size_mb:.2f} MB")
        
        upload_result = upload_csv_to_workspace(
            csv_file_path=csv_path,
            csv_filename=csv_file,
            databricks_path=databricks_path,
            workspace_host=workspace_host,
            token=token
        )
        
        if upload_result['success']:
            print(f"   ✅ Success")
            results['success'].append({
                'filename': csv_file,
                'size_mb': upload_result['size_mb']
            })
            results['total_size_mb'] += upload_result['size_mb']
        else:
            print(f"   ❌ Failed: {upload_result['error']}")
            results['failed'].append({
                'filename': csv_file,
                'error': upload_result['error']
            })
    
    return results


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Upload CSV files to Databricks workspace')
    parser.add_argument(
        '--extract-dir',
        default=os.path.join(tempfile.gettempdir(), "databricks_csv_extract"),
        help='Directory containing extracted CSV files'
    )
    parser.add_argument(
        '--databricks-path',
        default="/Workspace/Users/visal.kumar@hellofresh.com/adyen-ml-test",
        help='Target Databricks workspace path'
    )
    parser.add_argument(
        '--test',
        action='store_true',
        help='Test mode: only upload the largest file'
    )
    
    args = parser.parse_args()
    
    print("=" * 80)
    print("Upload CSV Files to Databricks Workspace")
    print("=" * 80)
    print(f"\n📁 Extract directory: {args.extract_dir}")
    print(f"🎯 Target path: {args.databricks_path}")
    print("=" * 80)
    
    if not os.path.exists(args.extract_dir):
        print(f"\n❌ Error: Directory not found: {args.extract_dir}")
        print("Please run 'unzip_csvs.py' first to extract the CSV files.")
        sys.exit(1)
    
    results = upload_csv_files(
        extract_dir=args.extract_dir,
        databricks_path=args.databricks_path,
        workspace_host=DATABRICKS_HOST,
        token=TOKEN,
        test_mode=args.test
    )
    
    # Print summary
    print("\n" + "=" * 80)
    print("Upload Summary")
    print("=" * 80)
    print(f"✅ Successfully uploaded: {len(results['success'])}/{results['total']}")
    print(f"❌ Failed: {len(results['failed'])}/{results['total']}")
    print(f"📊 Total size uploaded: {results['total_size_mb']:.2f} MB")
    
    if results['failed']:
        print(f"\n❌ Failed files ({len(results['failed'])}):")
        for item in results['failed'][:10]:
            print(f"   - {item['filename']}: {item['error']}")
        if len(results['failed']) > 10:
            print(f"   ... and {len(results['failed']) - 10} more")
    
    print("=" * 80)
    print(f"\n🌐 View files in browser:")
    print(f"   {DATABRICKS_HOST}/#workspace{args.databricks_path}")
    print("=" * 80)
    
    sys.exit(0 if len(results['failed']) == 0 else 1)


if __name__ == "__main__":
    main()


