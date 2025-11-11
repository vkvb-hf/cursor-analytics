#!/usr/bin/env python3
"""
Run the steering output generation notebook and retrieve detailed_summary.txt

This script:
1. Reads the steering_output_generation.py notebook
2. Creates/updates it in Databricks workspace
3. Runs it as a job
4. Downloads the detailed_summary.txt file
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

def main():
    """Run the steering output generation notebook"""
    
    # Initialize the job runner
    job_runner = DatabricksJobRunner(
        host=DATABRICKS_HOST,
        token=TOKEN,
        cluster_id=CLUSTER_ID
    )
    
    # Path to the notebook file
    # Use parametrized version by default
    notebook_file = Path(__file__).parent / "steering_output_generation_parametrized.py"
    notebook_path = "/Workspace/Users/visal.kumar@hellofresh.com/steering_output_generation_parametrized"
    
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
    job_name = "Steering Output Generation"
    
    # Use create_and_run method which handles everything
    result = job_runner.create_and_run(
        notebook_path=notebook_path,
        notebook_content=notebook_content,
        job_name=job_name,
        timeout_seconds=7200,  # 2 hours for large queries
        max_wait=7200
    )
    
    if not result or result.get('result_state') != 'SUCCESS':
        print("❌ Job failed or did not complete successfully")
        return 1
    
    run_id = result.get('run_id')
    
    # Result already contains the final status from create_and_run
    final_status = result
    
    if final_status.get('result_state') == 'SUCCESS':
        print(f"\n✅ Job completed successfully!")
        
        # Try to download the detailed_summary files from workspace
        print(f"\n📥 Attempting to download detailed_summary files...")
        
        # The notebook writes to OUTPUT_FOLDER/steering-{latest_date_str}/detailed_summary_*.txt
        # We need to find the latest steering folder
        workspace_base = "/Workspace/Users/visal.kumar@hellofresh.com"
        
        # Try to find the latest steering folder and download all 3 files
        headers = {"Authorization": f"Bearer {TOKEN}"}
        list_url = f"{DATABRICKS_HOST}/api/2.0/workspace/list"

        # List of files to download (3 main files)
        files_to_download = [
            'detailed_summary.txt',
            'long_term.txt',
            'comparison_prev_yr.txt'
        ]

        try:
            # List workspace directory to find steering folders
            response = requests.get(list_url, headers=headers, params={"path": workspace_base})
            if response.status_code == 200:
                items = response.json().get('objects', [])
                # Look for both parametrized and regular steering folders
                steering_folders = [item for item in items if item.get('path', '').startswith(f"{workspace_base}/steering-")]

                if steering_folders:
                    # Sort by path (which includes date) and get the latest
                    latest_folder = sorted(steering_folders, key=lambda x: x['path'], reverse=True)[0]
                    steering_path = latest_folder['path']
                    
                    print(f"📁 Found steering folder: {steering_path}")
                    
                    # Download each file
                    export_url = f"{DATABRICKS_HOST}/api/2.0/workspace/export"
                    downloaded_count = 0
                    
                    for filename in files_to_download:
                        file_path = f"{steering_path}/{filename}"
                        print(f"📄 Attempting to download: {filename}")
                        
                        export_response = requests.get(export_url, headers=headers, params={"path": file_path, "format": "AUTO"})
                        
                        if export_response.status_code == 200:
                            data = export_response.json()
                            content_b64 = data.get('content', '')
                            content = base64.b64decode(content_b64).decode('utf-8')
                            
                            # Save to local file
                            output_file = Path(__file__).parent / filename
                            with open(output_file, 'w') as f:
                                f.write(content)
                            
                            print(f"   ✅ Successfully downloaded {filename}")
                            print(f"      Saved to: {output_file.absolute()}")
                            downloaded_count += 1
                        else:
                            print(f"   ⚠️  Could not download {filename} (status: {export_response.status_code})")
                    
                    if downloaded_count > 0:
                        print(f"\n✅ Successfully downloaded {downloaded_count} out of {len(files_to_download)} files")
                        return 0
                    else:
                        print(f"\n⚠️  Could not download any files")
                else:
                    print(f"⚠️  No steering folders found in workspace")
            else:
                print(f"⚠️  Could not list workspace (status: {response.status_code})")
        except Exception as e:
            print(f"⚠️  Error downloading files: {e}")
            import traceback
            traceback.print_exc()
        
        # Fallback: print instructions
        print(f"\n💡 Manual download instructions:")
        print(f"   1. Go to Databricks workspace: {DATABRICKS_HOST}")
        print(f"   2. Navigate to: {workspace_base}")
        print(f"   3. Look for folder: steering-parametrized-YYYY-Www")
        print(f"   4. Download all 6 detailed_summary_*.txt files from that folder")
        
        return 0
    else:
        print(f"\n❌ Job failed with status: {final_status.get('result_state')}")
        if 'state_message' in final_status:
            print(f"   Error: {final_status['state_message']}")
        return 1

if __name__ == "__main__":
    sys.exit(main())

