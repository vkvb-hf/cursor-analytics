#!/usr/bin/env python3
"""
Example: Workspace Sync Workflow

This example demonstrates the complete workflow:
1. Create a notebook locally
2. Sync to Databricks workspace
3. Run as a job
4. View changes in workspace
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from databricks_api import DatabricksAPI
from core.workspace_sync import WorkspaceSync


def main():
    """Example workspace sync workflow."""
    
    # Configuration
    local_dir = Path.home() / "databricks_notebooks_example"
    workspace_dir = "/Workspace/Users/visal.kumar@hellofresh.com/notebooks_example"
    
    # Create local directory
    local_dir.mkdir(exist_ok=True)
    
    # Create a sample notebook
    notebook_content = """# Databricks notebook source
# MAGIC %md
# MAGIC # Example Analysis Notebook
# MAGIC 
# MAGIC This notebook was created locally and synced to Databricks!

# MAGIC %sql
# MAGIC -- Example query
# MAGIC SELECT 
# MAGIC     CURRENT_TIMESTAMP() as current_time,
# MAGIC     'Hello from synced notebook!' as message
"""
    
    notebook_file = local_dir / "example_analysis.py"
    with open(notebook_file, 'w') as f:
        f.write(notebook_content)
    
    print("=" * 80)
    print("Workspace Sync Example")
    print("=" * 80)
    print(f"\n1. Created local notebook: {notebook_file}")
    
    # Initialize API
    db = DatabricksAPI()
    
    # Sync to workspace
    print(f"\n2. Syncing to workspace: {workspace_dir}")
    result = db.sync_to_workspace(
        local_dir=str(local_dir),
        workspace_dir=workspace_dir,
        pattern="**/*.py"
    )
    
    if result['success']:
        print(f"   ✅ Synced {len(result['success'])} file(s)")
    else:
        print(f"   ❌ Failed to sync: {result.get('failed', [])}")
        return
    
    # Run as job
    notebook_path = f"{workspace_dir}/example_analysis"
    print(f"\n3. Running notebook as job: {notebook_path}")
    
    job_result = db.run_notebook_job(
        notebook_path=notebook_path,
        notebook_content=notebook_content,
        job_name="Example Sync Workflow"
    )
    
    if job_result and job_result.get('success'):
        print(f"   ✅ Job completed successfully!")
        print(f"   Job ID: {job_result.get('job_id')}")
        print(f"   Run ID: {job_result.get('run_id')}")
    else:
        print(f"   ❌ Job failed: {job_result}")
    
    print(f"\n4. View notebook in Databricks UI:")
    print(f"   {workspace_dir}/example_analysis")
    print("\n" + "=" * 80)
    print("Workflow complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()






