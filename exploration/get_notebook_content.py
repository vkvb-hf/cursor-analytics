#!/usr/bin/env python3
"""Get notebook content from Databricks."""

import requests
import base64
import sys
from config import DATABRICKS_HOST, TOKEN

def get_notebook(notebook_path):
    """Download notebook content."""
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    url = f"{DATABRICKS_HOST}/api/2.0/workspace/export"
    params = {"path": notebook_path, "format": "SOURCE"}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        content_b64 = data.get('content', '')
        content = base64.b64decode(content_b64).decode('utf-8')
        
        return content
    except Exception as e:
        print(f"Error: {e}")
        if hasattr(e, 'response'):
            print(f"Response: {e.response.text}")
        return None

if __name__ == "__main__":
    # Try to get notebook - we need the path
    # Based on the URL, it might be in the user's workspace
    # Let's try to find it or ask for the path
    
    # The notebook ID is 3346424239730025
    # We need the workspace path, not the ID
    
    # Let's check common locations
    possible_paths = [
        "/Workspace/Users/visal.kumar@hellofresh.com/simple_uploader",
        "/Workspace/Users/visal.kumar@hellofresh.com/uploader",
        "/Workspace/Users/visal.kumar@hellofresh.com/upload_csvs",
    ]
    
    print("Trying to find notebook...")
    for path in possible_paths:
        print(f"  Trying: {path}")
        content = get_notebook(path)
        if content:
            print(f"\n✅ Found notebook at: {path}")
            print("=" * 80)
            print(content)
            print("=" * 80)
            sys.exit(0)
    
    print("\n❌ Could not find notebook automatically.")
    print("Please provide the notebook path, or I can list your workspace files.")
    
    # List workspace to help find it
    workspace_path = "/Workspace/Users/visal.kumar@hellofresh.com"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    url = f"{DATABRICKS_HOST}/api/2.0/workspace/list"
    response = requests.get(url, headers=headers, params={"path": workspace_path})
    
    if response.status_code == 200:
        data = response.json()
        print(f"\nFiles in {workspace_path}:")
        for item in data.get('objects', []):
            if item.get('object_type') in ['NOTEBOOK', 'FILE']:
                print(f"  - {item.get('path')} ({item.get('object_type')})")

