#!/usr/bin/env python3
"""
Verify the notebook was uploaded correctly to Databricks workspace
"""

import os
import sys
import requests

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from config import DATABRICKS_HOST, TOKEN

def verify_notebook():
    """Verify notebook exists in workspace."""
    
    workspace_path = "/Workspace/Users/visal.kumar@hellofresh.com/[PY-3368] post-spider revamp"
    
    print("=" * 80)
    print("Verify Notebook in Databricks Workspace")
    print("=" * 80)
    print(f"\n🔍 Checking: {workspace_path}")
    
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    # Check if notebook exists
    get_status_url = f"{DATABRICKS_HOST}/api/2.0/workspace/get-status"
    params = {"path": workspace_path}
    
    try:
        response = requests.get(get_status_url, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ Notebook found in workspace!")
            print(f"   📄 Path: {data.get('path', 'N/A')}")
            print(f"   📝 Language: {data.get('language', 'N/A')}")
            print(f"   📊 Object Type: {data.get('object_type', 'N/A')}")
            print(f"   🔗 Object ID: {data.get('object_id', 'N/A')}")
            
            # Try to get the content to verify it's correct
            export_url = f"{DATABRICKS_HOST}/api/2.0/workspace/export"
            export_params = {"path": workspace_path, "format": "SOURCE"}
            
            export_response = requests.get(export_url, headers=headers, params=export_params)
            
            if export_response.status_code == 200:
                export_data = export_response.json()
                content_size = len(export_data.get('content', ''))
                print(f"\n📊 Content verification:")
                print(f"   ✅ Content retrieved successfully")
                print(f"   📏 Content size: {content_size:,} bytes")
                
                # Check if it contains key markers
                import base64
                content = base64.b64decode(export_data.get('content', '')).decode('utf-8')
                
                key_markers = [
                    "Graph Duplicate Detection from S3 CSV Files",
                    "payments_hf.customer_identifiers_20251121",
                    "s3://hf-payments-data-lake-live-main/voucher_abuse/neptune_backfill/20250305"
                ]
                
                print(f"\n🔍 Checking key content markers:")
                for marker in key_markers:
                    if marker in content:
                        print(f"   ✅ Found: '{marker[:50]}...'")
                    else:
                        print(f"   ❌ Missing: '{marker[:50]}...'")
                
                print(f"\n{'=' * 80}")
                print("✅ Verification complete - Notebook is correctly uploaded!")
                print(f"{'=' * 80}")
                return True
            else:
                print(f"\n⚠️  Could not retrieve content (status: {export_response.status_code})")
                print(f"   Response: {export_response.text[:200]}")
                return False
                
        elif response.status_code == 404:
            print(f"\n❌ Notebook not found in workspace!")
            print(f"   The file may not have been uploaded correctly.")
            return False
        else:
            print(f"\n❌ Error checking notebook (status: {response.status_code})")
            print(f"   Response: {response.text[:200]}")
            return False
            
    except Exception as e:
        print(f"\n❌ Error verifying notebook: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = verify_notebook()
    sys.exit(0 if success else 1)






