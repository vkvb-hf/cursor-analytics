#!/usr/bin/env python3
"""
Run the find affected dates analysis
"""

import sys
import os
import requests
import base64

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.databricks_job_runner import DatabricksJobRunner
from config import DATABRICKS_HOST, TOKEN

def read_dbfs_file(file_path: str) -> str:
    """Read a file from DBFS and return its content."""
    headers = {"Authorization": f"Bearer {TOKEN}"}
    read_url = f"{DATABRICKS_HOST}/api/2.0/dbfs/read"
    
    try:
        response = requests.get(
            read_url,
            headers=headers,
            json={"path": file_path}
        )
        
        if response.status_code == 200:
            file_data = response.json()
            if 'data' in file_data:
                return base64.b64decode(file_data['data']).decode('utf-8')
            else:
                return None
        else:
            print(f"⚠️  Could not read file (status: {response.status_code})")
            return None
    except Exception as e:
        print(f"❌ Error reading DBFS file: {e}")
        return None

def main():
    """Main function."""
    
    notebook_file = os.path.join(os.path.dirname(__file__), "find_affected_dates.py")
    with open(notebook_file, 'r') as f:
        notebook_content = f.read()
    
    notebook_path = "/Workspace/Users/visal.kumar@hellofresh.com/find_affected_dates"
    job_name = "find_affected_dates"
    output_file = "/tmp/find_affected_dates_results.txt"
    
    print("=" * 100)
    print("Find Dates Affected Like Nov 3")
    print("=" * 100)
    
    runner = DatabricksJobRunner()
    
    print("\n📝 Creating notebook and running as job...")
    result = runner.create_and_run(
        notebook_path=notebook_path,
        notebook_content=notebook_content,
        job_name=job_name,
        timeout_seconds=600,
        poll_interval=10,
        max_wait=600,
        show_output=True
    )
    
    if result.get('result_state') == 'SUCCESS':
        print("\n" + "=" * 100)
        print("✅ Job completed successfully!")
        print("=" * 100)
        
        output_content = read_dbfs_file(output_file)
        if output_content:
            print("\n" + "=" * 100)
            print("RESULTS:")
            print("=" * 100)
            print(output_content)
            print("=" * 100)
    else:
        print(f"\n❌ Job finished with state: {result.get('result_state')}")

if __name__ == "__main__":
    main()

