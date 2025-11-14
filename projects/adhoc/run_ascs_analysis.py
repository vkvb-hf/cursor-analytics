#!/usr/bin/env python3
"""
Run the ASCS Cancellation Analysis notebook
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from databricks_api import DatabricksAPI

def main():
    # Read the notebook content
    notebook_path = os.path.join(os.path.dirname(__file__), "notebooks/ascs_cancellation_analysis.py")
    
    with open(notebook_path, 'r') as f:
        notebook_content = f.read()
    
    # Initialize Databricks API
    db = DatabricksAPI()
    
    # Create and run the notebook as a job
    notebook_workspace_path = "/Workspace/Users/visal.kumar@hellofresh.com/ascs_cancellation_analysis"
    job_name = "ASCS Cancellation Analysis"
    
    print("=" * 100)
    print("Running ASCS Cancellation Analysis")
    print("=" * 100)
    print(f"Notebook path: {notebook_workspace_path}")
    print(f"Job name: {job_name}")
    print("=" * 100)
    print()
    
    # Create notebook and run as job
    job = db.run_notebook_job(
        notebook_path=notebook_workspace_path,
        notebook_content=notebook_content,
        job_name=job_name
    )
    
    if job:
        print(f"\n✅ Job submitted successfully!")
        print(f"   Run ID: {job.get('run_id')}")
        print(f"\n📊 Monitoring job execution...")
        print("   (This may take several minutes)")
        print()
        
        # Monitor job
        run_id = job.get('run_id')
        if run_id:
            status = db.get_job_status(run_id=run_id)
            if status:
                print(f"\n✅ Job completed!")
                return 0
            else:
                print(f"\n⚠️  Could not get job status")
                return 1
    else:
        print("\n❌ Failed to create/run job")
        return 1

if __name__ == "__main__":
    sys.exit(main())

