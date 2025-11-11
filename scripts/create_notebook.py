#!/usr/bin/env python3
"""
CLI script to create and run Databricks notebooks
Usage: python scripts/create_notebook.py <notebook_path> <notebook_content_file> [job_name]
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.databricks_job_runner import DatabricksJobRunner

def main():
    if len(sys.argv) < 3:
        print("Usage: python scripts/create_notebook.py <notebook_path> <notebook_content_file> [job_name]")
        print("Example: python scripts/create_notebook.py /Workspace/notebooks/my_notebook.py my_notebook.py my_job")
        sys.exit(1)
    
    notebook_path = sys.argv[1]
    content_file = sys.argv[2]
    job_name = sys.argv[3] if len(sys.argv) > 3 else None
    
    # Read notebook content
    with open(content_file, 'r') as f:
        notebook_content = f.read()
    
    runner = DatabricksJobRunner()
    
    if job_name:
        print(f"Creating and running job: {job_name}")
        result = runner.create_and_run(
            notebook_path=notebook_path,
            notebook_content=notebook_content,
            job_name=job_name
        )
        print(f"Job created with ID: {result.get('job_id')}")
        print(f"Run ID: {result.get('run_id')}")
    else:
        print(f"Creating notebook at: {notebook_path}")
        # Just create the notebook without running as job
        # Implementation depends on databricks_workspace.py
        print("Notebook creation functionality to be implemented")

if __name__ == "__main__":
    main()


