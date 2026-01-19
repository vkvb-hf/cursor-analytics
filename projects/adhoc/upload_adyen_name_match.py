#!/usr/bin/env python3
"""
Upload AdyenNameMatch.csv to Databricks and create table payments_hf.AdyenNameMatch

Usage:
    python upload_adyen_name_match.py
"""

import os
import sys
import base64
import requests

# Add parent directory to path for config import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import DATABRICKS_HOST, TOKEN
from core.databricks_workspace import create_workspace_directory
from core.csv_to_table import create_table_from_csvs


def upload_csv_to_workspace_auto(
    csv_file_path: str,
    csv_filename: str,
    databricks_path: str,
    workspace_host: str,
    token: str
) -> dict:
    """
    Upload a CSV file to Databricks workspace using AUTO format.
    
    Args:
        csv_file_path: Local path to CSV file
        csv_filename: Filename for the uploaded file
        databricks_path: Target workspace directory path
        workspace_host: Databricks workspace hostname
        token: Databricks personal access token
    
    Returns:
        Dictionary with 'success' (bool) and either 'workspace_path'/'size_mb' or 'error'
    """
    workspace_file_path = f"{databricks_path.rstrip('/')}/{csv_filename}"
    headers = {"Authorization": f"Bearer {token}"}
    
    # Read file content as text
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as f:
            file_content_text = f.read()
    except UnicodeDecodeError:
        try:
            with open(csv_file_path, 'r', encoding='latin-1') as f:
                file_content_text = f.read()
        except Exception as e:
            return {'success': False, 'error': f"Error reading file: {e}"}
    except Exception as e:
        return {'success': False, 'error': f"Error reading file: {e}"}
    
    # Delete existing file if it exists
    try:
        delete_url = f"{workspace_host}/api/2.0/workspace/delete"
        delete_payload = {"path": workspace_file_path}
        requests.post(delete_url, headers=headers, json=delete_payload)
    except:
        pass  # Non-critical if file doesn't exist
    
    # Upload using Workspace API with AUTO format for CSV files
    try:
        file_content_b64 = base64.b64encode(file_content_text.encode('utf-8')).decode('utf-8')
        
        import_url = f"{workspace_host}/api/2.0/workspace/import"
        import_payload = {
            "path": workspace_file_path,
            "content": file_content_b64,
            "format": "AUTO",  # Use AUTO for CSV files
            "overwrite": True
        }
        
        response = requests.post(import_url, headers=headers, json=import_payload)
        response.raise_for_status()
        
        return {
            'success': True,
            'workspace_path': workspace_file_path,
            'size_mb': len(file_content_text.encode('utf-8')) / (1024 * 1024)
        }
        
    except requests.exceptions.HTTPError as e:
        error_msg = str(e)
        try:
            error_detail = e.response.json()
            error_msg = f"{e}: {error_detail}"
        except:
            if hasattr(e, 'response') and hasattr(e.response, 'text'):
                error_msg = f"{e}: {e.response.text}"
        
        return {'success': False, 'error': error_msg}
    except Exception as e:
        return {'success': False, 'error': str(e)}


def main():
    """Main function."""
    print("=" * 80)
    print("Upload AdyenNameMatch.csv to Databricks")
    print("=" * 80)
    
    # Configuration
    local_csv_path = "/Users/visal.kumar/Documents/AdyenNameMatch.csv"
    csv_filename = "AdyenNameMatch.csv"
    workspace_dir = "/Workspace/Users/visal.kumar@hellofresh.com/adyen-name-match"
    table_name = "payments_hf.AdyenNameMatch"
    
    # Step 1: Verify local file exists
    print(f"\n📁 Step 1: Checking local file...")
    if not os.path.exists(local_csv_path):
        print(f"❌ Error: File not found: {local_csv_path}")
        sys.exit(1)
    
    file_size_mb = os.path.getsize(local_csv_path) / (1024 * 1024)
    print(f"✅ Found file: {csv_filename} ({file_size_mb:.2f} MB)")
    
    # Step 2: Create workspace directory
    print(f"\n📂 Step 2: Creating workspace directory...")
    try:
        # Create parent directories
        create_workspace_directory(workspace_dir, DATABRICKS_HOST, TOKEN)
        
        # Ensure the target directory itself exists
        headers = {"Authorization": f"Bearer {TOKEN}"}
        mkdir_url = f"{DATABRICKS_HOST}/api/2.0/workspace/mkdirs"
        mkdir_payload = {"path": workspace_dir}
        mkdir_response = requests.post(mkdir_url, headers=headers, json=mkdir_payload)
        if mkdir_response.status_code not in [200, 400]:
            mkdir_response.raise_for_status()
        
        print(f"✅ Directory ready: {workspace_dir}")
    except Exception as e:
        print(f"⚠️  Warning creating directory: {e}")
    
    # Step 3: Upload CSV to workspace
    print(f"\n📤 Step 3: Uploading CSV to workspace...")
    upload_result = upload_csv_to_workspace_auto(
        csv_file_path=local_csv_path,
        csv_filename=csv_filename,
        databricks_path=workspace_dir,
        workspace_host=DATABRICKS_HOST,
        token=TOKEN
    )
    
    if not upload_result.get('success'):
        print(f"❌ Upload failed: {upload_result.get('error')}")
        sys.exit(1)
    
    print(f"✅ Upload successful!")
    print(f"   Workspace path: {upload_result['workspace_path']}")
    print(f"   Size: {upload_result['size_mb']:.2f} MB")
    
    # Step 4: Create table from CSV
    print(f"\n📊 Step 4: Creating table from CSV...")
    print(f"   Table: {table_name}")
    print(f"   Source: {upload_result['workspace_path']}")
    
    success = create_table_from_csvs(
        workspace_path=workspace_dir,
        table_name=table_name,
        custom_columns=None,
        drop_if_exists=True,
        verify=True,
        test_mode=False
    )
    
    if success:
        print("\n" + "=" * 80)
        print("✅ SUCCESS: Table created successfully!")
        print("=" * 80)
        print(f"   Table: {table_name}")
        print(f"   Source: {upload_result['workspace_path']}")
        sys.exit(0)
    else:
        print("\n" + "=" * 80)
        print("❌ FAILED: Table creation failed")
        print("=" * 80)
        sys.exit(1)


if __name__ == "__main__":
    main()

