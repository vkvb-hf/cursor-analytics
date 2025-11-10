#!/usr/bin/env python3
"""
Run the long term steering report notebook and retrieve output

This script:
1. Reads the long_term_steering_report.py notebook
2. Creates/updates it in Databricks workspace
3. Runs it as a job for each comparison type
4. Downloads and displays all output files

Generates three files:
- detailed_summary_week_vs_prev_week.txt (week_prev)
- detailed_summary_week_vs_prev_yr_week.txt (week_yoy)
- detailed_summary_quarter_vs_prev_quarter.txt (quarter_prev)
"""

import sys
import os
import time
import requests
import base64
from pathlib import Path

# Add cursor_databricks directory to path for imports
cursor_databricks_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_dir)
from core.databricks_job_runner import DatabricksJobRunner
from config import DATABRICKS_HOST, TOKEN, CLUSTER_ID

def run_comparison(comparison_type, job_runner, notebook_file, notebook_path):
    """Run a single comparison type and download the output"""
    
    print(f"\n{'='*80}")
    print(f"📊 Running comparison type: {comparison_type}")
    print(f"{'='*80}")
    
    # Read the notebook content
    print("📖 Reading notebook file...")
    with open(notebook_file, 'r') as f:
        notebook_content = f.read()
    
    # Update the COMPARISON_TYPE in the notebook content
    lines = notebook_content.split('\n')
    for i, line in enumerate(lines):
        if line.strip().startswith("COMPARISON_TYPE ="):
            lines[i] = f"COMPARISON_TYPE = '{comparison_type}'  # Options: 'week_prev', 'week_yoy', 'quarter_prev'"
            break
    notebook_content = '\n'.join(lines)
    
    print(f"✅ Read {len(notebook_content)} characters from notebook")
    print(f"   Set COMPARISON_TYPE to: {comparison_type}")
    
    # Create/update the notebook in Databricks
    print(f"\n📝 Creating notebook in Databricks: {notebook_path}")
    if not job_runner.create_notebook(notebook_path, notebook_content):
        print("❌ Failed to create notebook")
        return None
    
    # Create and run the notebook as a job
    print(f"\n🚀 Creating and running notebook as job...")
    job_name = f"Long Term Steering Report - {comparison_type}"
    
    # Use create_and_run method which handles everything
    result = job_runner.create_and_run(
        notebook_path=notebook_path,
        notebook_content=notebook_content,
        job_name=job_name,
        timeout_seconds=3600,  # 1 hour
        max_wait=3600
    )
    
    if not result or result.get('result_state') != 'SUCCESS':
        print("❌ Job failed or did not complete successfully")
        if result:
            print(f"   Result state: {result.get('result_state')}")
            print(f"   State message: {result.get('state_message', 'N/A')}")
        return None
    
    run_id = result.get('run_id')
    print(f"\n✅ Job completed successfully! (Run ID: {run_id})")
    
    # Determine expected filename based on comparison type
    filename_map = {
        'week_prev': 'detailed_summary_week_vs_prev_week.txt',
        'week_yoy': 'detailed_summary_week_vs_prev_yr_week.txt',
        'quarter_prev': 'detailed_summary_quarter_vs_prev_quarter.txt'
    }
    filename = filename_map.get(comparison_type)
    
    if not filename:
        print(f"⚠️  Unknown comparison type: {comparison_type}")
        return None
    
    # Try to download the output file from workspace
    print(f"\n📥 Attempting to download output file: {filename}")
    
    workspace_base = "/Workspace/Users/visal.kumar@hellofresh.com"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    export_url = f"{DATABRICKS_HOST}/api/2.0/workspace/export"
    
    try:
        # List workspace directory to find the output folder
        list_url = f"{DATABRICKS_HOST}/api/2.0/workspace/list"
        response = requests.get(list_url, headers=headers, params={"path": workspace_base})
        
        if response.status_code == 200:
            items = response.json().get('objects', [])
            # Look for long-term-steering folders (single folder for all comparison types)
            # Pattern: long-term-steering-YYYY-Www (no comparison type suffix)
            import re
            pattern = re.compile(r'long-term-steering-\d{4}-W\d{2}$')
            steering_folders = []
            for item in items:
                path = item.get('path', '')
                folder_name = path.replace(f"{workspace_base}/", "")
                if pattern.match(folder_name):
                    steering_folders.append(item)
            
            if steering_folders:
                # Sort by path and get the latest (all comparison types use the same folder)
                latest_folder = sorted(steering_folders, key=lambda x: x['path'], reverse=True)[0]
                folder_path = latest_folder['path']
                
                print(f"📁 Found output folder: {folder_path}")
                
                # Try to download the file
                file_path = f"{folder_path}/{filename}"
                
                export_response = requests.get(export_url, headers=headers, 
                                              params={"path": file_path, "format": "AUTO"})
                
                if export_response.status_code == 200:
                    data = export_response.json()
                    content_b64 = data.get('content', '')
                    content = base64.b64decode(content_b64).decode('utf-8')
                    
                    # Save to local file
                    output_file = Path(__file__).parent / filename
                    with open(output_file, 'w') as f:
                        f.write(content)
                    
                    print(f"✅ Successfully downloaded {filename}")
                    print(f"   Saved to: {output_file.absolute()}")
                    
                    return str(output_file)
                else:
                    print(f"   ⚠️  Could not download {filename} (status: {export_response.status_code})")
                    print(f"   File path attempted: {file_path}")
            else:
                print(f"⚠️  No long-term-steering folders found in workspace")
        else:
            print(f"⚠️  Could not list workspace (status: {response.status_code})")
    except Exception as e:
        print(f"⚠️  Error downloading file: {e}")
        import traceback
        traceback.print_exc()
    
    return None

def main():
    """Run all three comparison types"""
    
    # Get comparison types from command line or use all three
    if len(sys.argv) > 1:
        comparison_types = sys.argv[1:]
        # Validate
        valid_types = ['week_prev', 'week_yoy', 'quarter_prev']
        invalid = [ct for ct in comparison_types if ct not in valid_types]
        if invalid:
            print(f"❌ Invalid comparison type(s): {invalid}")
            print(f"   Valid options: {valid_types}")
            return 1
    else:
        # Run all three by default
        comparison_types = ['week_prev', 'week_yoy', 'quarter_prev']
    
    print(f"📊 Running long term steering reports for: {', '.join(comparison_types)}")
    print(f"   This will generate {len(comparison_types)} file(s)")
    
    # Initialize the job runner
    job_runner = DatabricksJobRunner(
        host=DATABRICKS_HOST,
        token=TOKEN,
        cluster_id=CLUSTER_ID
    )
    
    # Path to the notebook file
    notebook_file = Path(__file__).parent / "long_term_steering_report.py"
    notebook_path = f"/Workspace/Users/visal.kumar@hellofresh.com/long_term_steering_report"
    
    # Run each comparison type
    downloaded_files = []
    failed_types = []
    
    for comparison_type in comparison_types:
        output_file = run_comparison(comparison_type, job_runner, notebook_file, notebook_path)
        if output_file:
            downloaded_files.append(output_file)
        else:
            failed_types.append(comparison_type)
        
        # Add a small delay between runs to avoid overwhelming the system
        if comparison_type != comparison_types[-1]:
            print(f"\n⏳ Waiting 5 seconds before next run...")
            time.sleep(5)
    
    # Summary
    print(f"\n{'='*80}")
    print(f"📊 SUMMARY")
    print(f"{'='*80}")
    print(f"✅ Successfully generated {len(downloaded_files)} file(s):")
    for f in downloaded_files:
        print(f"   - {Path(f).name}")
    
    if failed_types:
        print(f"\n❌ Failed to generate {len(failed_types)} file(s):")
        for ct in failed_types:
            print(f"   - {ct}")
    
    print(f"\n📁 All files saved to: {Path(__file__).parent}")
    
    return 0 if len(downloaded_files) == len(comparison_types) else 1

if __name__ == "__main__":
    sys.exit(main())

