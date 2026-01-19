#!/usr/bin/env python3
"""
Run test script for gc_checkout_success_20251121 as a Databricks notebook job.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from databricks_api import DatabricksAPI
from core.notebook_output_reader import NotebookOutputReader

def main():
    """Run the test notebook as a job."""
    
    # Read notebook content
    notebook_path = Path(__file__).parent / "test_gc_checkout_success.py"
    
    if not notebook_path.exists():
        print(f"❌ Error: Notebook not found: {notebook_path}")
        return 1
    
    with open(notebook_path, 'r') as f:
        notebook_content = f.read()
    
    # Initialize API
    db = DatabricksAPI()
    
    # Job configuration
    workspace_notebook_path = "/Workspace/Users/visal.kumar@hellofresh.com/test_gc_checkout_success"
    job_name = "Test GC Checkout Success 20251121"
    
    print("=" * 80)
    print("Test: Create Graph Customers with Successful Conversions Only")
    print("=" * 80)
    print(f"\n📓 Notebook: {workspace_notebook_path}")
    print(f"📋 Job Name: {job_name}")
    print(f"📁 Local file: {notebook_path}")
    print("\n🚀 Creating and running job...")
    print("=" * 80)
    
    # Run notebook as job with output capture
    result = db.run_notebook_job(
        notebook_path=workspace_notebook_path,
        notebook_content=notebook_content,
        job_name=job_name,
        auto_inject_output=True,  # Automatically inject output capture
        auto_read_output=True      # Automatically read output after completion
    )
    
    if result:
        print("\n" + "=" * 80)
        print("✅ Job completed successfully!")
        print("=" * 80)
        print(f"📊 Job ID: {result.get('job_id', 'N/A')}")
        print(f"📊 Run ID: {result.get('run_id', 'N/A')}")
        
        # Try to read output from DBFS
        print("\n📥 Reading output from DBFS...")
        reader = NotebookOutputReader()
        
        # Try to find output files
        output_files = reader.list_output_files("/tmp/notebook_outputs")
        gc_checkout_files = [f for f in output_files if "gc_checkout_success" in f]
        
        if gc_checkout_files:
            print(f"\n✅ Found {len(gc_checkout_files)} output file(s):")
            for output_file in sorted(gc_checkout_files, reverse=True)[:2]:  # Show latest 2
                print(f"\n📄 Reading: {output_file}")
                reader.display_output(output_file, show_header=True)
        else:
            print("⚠️  No output files found in /tmp/notebook_outputs")
            print("   The notebook may not have written output files yet.")
        
        return 0
    else:
        print("\n❌ Job failed or did not complete successfully")
        return 1

if __name__ == "__main__":
    sys.exit(main())

