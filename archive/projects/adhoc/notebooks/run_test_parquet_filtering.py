#!/usr/bin/env python3
"""
Run the Parquet filtering performance test
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
            print(f"   Response: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Error reading DBFS file: {e}")
        return None

def main():
    """Main function to run the performance test."""
    
    # Read the notebook content
    notebook_file = os.path.join(os.path.dirname(__file__), "test_parquet_filtering_performance.py")
    with open(notebook_file, 'r') as f:
        notebook_content = f.read()
    
    notebook_path = "/Workspace/Users/visal.kumar@hellofresh.com/test_parquet_filtering_performance"
    job_name = "test_parquet_filtering_performance"
    output_file = "/tmp/parquet_filtering_performance_test.txt"
    
    print("=" * 100)
    print("Parquet Filtering Performance Test")
    print("=" * 100)
    print(f"\n📝 Notebook: {notebook_path}")
    print(f"🚀 Job: {job_name}")
    print(f"📊 Output file: {output_file}")
    print("=" * 100)
    print("\n⏱️  This test will:")
    print("   - Compare old approach (DATE conversion) vs new approach (timestamp filtering)")
    print("   - Test 5 different date periods")
    print("   - Test both 7-day and 30-day windows")
    print("   - Measure execution time for each")
    print("=" * 100)
    
    # Initialize job runner
    runner = DatabricksJobRunner()
    
    # Create and run notebook
    print("\n📝 Creating notebook and running as job...")
    result = runner.create_and_run(
        notebook_path=notebook_path,
        notebook_content=notebook_content,
        job_name=job_name,
        timeout_seconds=3600,
        poll_interval=10,
        max_wait=3600,  # 1 hour max
        show_output=True
    )
    
    # Check if job succeeded
    if result.get('result_state') == 'SUCCESS':
        print("\n" + "=" * 100)
        print("✅ Job completed successfully!")
        print("=" * 100)
        
        # Read output from DBFS
        print(f"\n📖 Reading output from DBFS: {output_file}")
        output_content = read_dbfs_file(output_file)
        
        if output_content:
            print("\n" + "=" * 100)
            print("TEST RESULTS:")
            print("=" * 100)
            print(output_content)
            print("=" * 100)
        else:
            print("⚠️  Could not read output file from DBFS")
            print("   The file may not exist or the path is incorrect")
    else:
        print("\n" + "=" * 100)
        print(f"❌ Job finished with state: {result.get('result_state')}")
        print("=" * 100)
        
        # Try to read output anyway (might have partial results)
        output_content = read_dbfs_file(output_file)
        if output_content:
            print("\n📖 Partial output:")
            print("=" * 100)
            print(output_content)
            print("=" * 100)

if __name__ == "__main__":
    main()

