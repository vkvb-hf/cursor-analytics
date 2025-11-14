#!/usr/bin/env python3
"""
Run the threshold analysis notebook on Databricks and display the output
"""
import sys
import os
import time
from pathlib import Path

# Add cursor_databricks directory to path
cursor_databricks_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_dir)

from core.databricks_job_runner import DatabricksJobRunner
from config import DATABRICKS_HOST, TOKEN, CLUSTER_ID

def main():
    """Run the threshold analysis notebook"""
    
    print("📊 Running Threshold Analysis for All Metrics...")
    print(f"   This will analyze historical trends and calculate data-driven thresholds")
    
    # Initialize the job runner
    job_runner = DatabricksJobRunner(
        host=DATABRICKS_HOST,
        token=TOKEN,
        cluster_id=CLUSTER_ID
    )
    
    # Path to the notebook file
    notebook_file = Path(__file__).parent / "analyze_all_thresholds.py"
    notebook_path = f"/Workspace/Users/visal.kumar@hellofresh.com/analyze_all_thresholds"
    
    # Read the notebook content
    print("📖 Reading notebook file...")
    with open(notebook_file, 'r') as f:
        notebook_content = f.read()
    
    print(f"✅ Read {len(notebook_content)} characters from notebook")
    
    # Create/update the notebook in Databricks
    print(f"\n📝 Creating notebook in Databricks: {notebook_path}")
    if not job_runner.create_notebook(notebook_path, notebook_content):
        print("❌ Failed to create notebook")
        return 1
    
    # Create and run the notebook as a job
    print(f"\n🚀 Creating and running notebook as job...")
    job_name = "Analyze Thresholds for All Metrics"
    
    result = job_runner.create_and_run(
        notebook_path=notebook_path,
        notebook_content=notebook_content,
        job_name=job_name,
        timeout_seconds=1800,  # 30 minutes
        max_wait=1800
    )
    
    if not result or result.get('result_state') != 'SUCCESS':
        print("❌ Job failed or did not complete successfully")
        if result:
            print(f"   Result state: {result.get('result_state')}")
            print(f"   State message: {result.get('state_message', 'N/A')}")
        return 1
    
    run_id = result.get('run_id')
    print(f"\n✅ Job completed successfully! (Run ID: {run_id})")
    
    # Try to download the output files
    print(f"\n📥 Attempting to download output files...")
    
    try:
        import requests
        import base64
        
        headers = {"Authorization": f"Bearer {TOKEN}"}
        
        # Try to download report from workspace first (more reliable)
        workspace_files = [
            '/Workspace/Users/visal.kumar@hellofresh.com/threshold_analysis_report.txt'
        ]
        
        for workspace_path in workspace_files:
            export_url = f"{DATABRICKS_HOST}/api/2.0/workspace/export"
            response = requests.get(
                export_url,
                headers=headers,
                params={"path": workspace_path, "format": "AUTO"}
            )
            
            if response.status_code == 200:
                data = response.json()
                content_b64 = data.get('content', '')
                content = base64.b64decode(content_b64).decode('utf-8')
                
                local_file = Path(__file__).parent / Path(workspace_path).name
                with open(local_file, 'w') as f:
                    f.write(content)
                
                print(f"✅ Downloaded from workspace: {local_file.name}")
                print(f"   Saved to: {local_file.absolute()}")
                
                # Show full report
                print(f"\n{'='*80}")
                print(f"📋 FULL THRESHOLD ANALYSIS REPORT")
                print(f"{'='*80}")
                print(content)
                print(f"{'='*80}")
                break
        
        # Also try to download from DBFS
        dbfs_files = [
            '/tmp/threshold_analysis_report.txt',
            '/tmp/threshold_analysis_summary.csv',
            '/tmp/threshold_analysis_detailed.csv'
        ]
        
        for dbfs_path in dbfs_files:
            # Use DBFS API to read the file (POST with JSON body)
            dbfs_read_url = f"{DATABRICKS_HOST}/api/2.0/dbfs/read"
            response = requests.post(
                dbfs_read_url,
                headers=headers,
                json={"path": dbfs_path}
            )
            
            if response.status_code == 200:
                data = response.json()
                # DBFS API returns 'data' field with base64 encoded content
                content_b64 = data.get('data', '')
                if not content_b64:
                    # Try alternative field name
                    content_b64 = data.get('bytes_read', '')
                content = base64.b64decode(content_b64).decode('utf-8')
                
                # Save locally
                local_file = Path(__file__).parent / Path(dbfs_path).name
                with open(local_file, 'w') as f:
                    f.write(content)
                
                print(f"✅ Downloaded: {local_file.name}")
                print(f"   Saved to: {local_file.absolute()}")
                
                # Show full report if it's the text report
                if 'report.txt' in dbfs_path:
                    print(f"\n{'='*80}")
                    print(f"📋 FULL THRESHOLD ANALYSIS REPORT")
                    print(f"{'='*80}")
                    print(content)
                    print(f"{'='*80}")
            else:
                print(f"⚠️  Could not download {dbfs_path} (status: {response.status_code})")
                if response.status_code == 404:
                    print(f"   File may not exist yet. Check job logs for output.")
    
    except Exception as e:
        print(f"⚠️  Error downloading files: {e}")
        import traceback
        traceback.print_exc()
    
    print(f"\n📁 Check the Databricks workspace for the notebook output:")
    print(f"   {notebook_path}")
    print(f"\n📁 Check DBFS for output files:")
    print(f"   /tmp/threshold_analysis_report.txt")
    print(f"   /tmp/threshold_analysis_summary.csv")
    print(f"   /tmp/threshold_analysis_detailed.csv")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())

