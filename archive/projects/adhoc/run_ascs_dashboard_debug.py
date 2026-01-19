#!/usr/bin/env python3
"""
Run [PY-3350] ASCS Dashboard Debug notebook
"""
import sys
import os

cursor_databricks_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_root)

from databricks_api import DatabricksAPI

def main():
    # Read notebook content
    notebook_path_local = os.path.join(
        os.path.dirname(__file__),
        'notebooks/ascs_dashboard_debug.py'
    )
    
    with open(notebook_path_local, 'r') as f:
        notebook_content = f.read()
    
    db = DatabricksAPI()
    
    notebook_path = "/Workspace/Users/visal.kumar@hellofresh.com/[PY-3350] ASCS Dashboard"
    job_name = "[PY-3350] ASCS Dashboard - Debug"
    
    print("=" * 80)
    print("[PY-3350] ASCS Dashboard - Running Debug Notebook")
    print("=" * 80)
    print(f"Notebook: {notebook_path}")
    print(f"Job: {job_name}")
    print("=" * 80)
    print()
    
    result = db.run_notebook_job(
        notebook_path=notebook_path,
        notebook_content=notebook_content,
        job_name=job_name,
        auto_inject_output=True,
        auto_read_output=True
    )
    
    if result:
        print("\n" + "=" * 80)
        print("✓ Job completed!")
        print("=" * 80)
        if 'run_id' in result:
            print(f"Run ID: {result['run_id']}")
        return 0
    else:
        print("\n" + "=" * 80)
        print("✗ Job failed")
        print("=" * 80)
        return 1

if __name__ == "__main__":
    sys.exit(main())






