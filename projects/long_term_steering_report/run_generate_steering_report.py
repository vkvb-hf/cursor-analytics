#!/usr/bin/env python3
"""
Run the generate_steering_report.py notebook on Databricks and download the output
"""
import sys
import os
import time
import base64
import requests
from pathlib import Path

# Add cursor_databricks directory to path
cursor_databricks_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_dir)

from core.databricks_job_runner import DatabricksJobRunner
from config import DATABRICKS_HOST, TOKEN, CLUSTER_ID

def main():
    """Run the steering report generation notebook"""
    
    print("📊 Running Steering Report Generation...")
    print(f"   This will generate a comprehensive steering report from source data")
    
    # Initialize the job runner
    job_runner = DatabricksJobRunner(
        host=DATABRICKS_HOST,
        token=TOKEN,
        cluster_id=CLUSTER_ID
    )
    
    # Path to the notebook file
    notebook_file = Path(__file__).parent / "generate_steering_report.py"
    notebook_path = f"/Workspace/Users/visal.kumar@hellofresh.com/generate_steering_report"
    
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
    job_name = "Generate Steering Report from Source"
    
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
        return 1
    
    run_id = result.get('run_id')
    print(f"\n✅ Job completed successfully! (Run ID: {run_id})")
    
    # Try to download the output file from workspace
    print(f"\n📥 Attempting to download output file...")
    
    workspace_base = "/Workspace/Users/visal.kumar@hellofresh.com"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    export_url = f"{DATABRICKS_HOST}/api/2.0/workspace/export"
    
    try:
        # List workspace directory to find the output folder
        list_url = f"{DATABRICKS_HOST}/api/2.0/workspace/list"
        response = requests.get(list_url, headers=headers, params={"path": workspace_base})
        
        if response.status_code == 200:
            items = response.json().get('objects', [])
            # Look for long-term-steering folders
            steering_folders = [item for item in items 
                              if item.get('path', '').startswith(f"{workspace_base}/long-term-steering-")]
            
            if steering_folders:
                # Sort by path and get the latest
                latest_folder = sorted(steering_folders, key=lambda x: x['path'], reverse=True)[0]
                folder_path = latest_folder['path']
                
                print(f"📁 Found output folder: {folder_path}")
                
                # Try to download the steering report file
                filename = "W*_steering_report.md"
                file_path = f"{folder_path}/{filename}"
                
                # List files in the folder to find the exact filename
                folder_list_url = f"{DATABRICKS_HOST}/api/2.0/workspace/list"
                folder_response = requests.get(folder_list_url, headers=headers, params={"path": folder_path})
                
                if folder_response.status_code == 200:
                    folder_items = folder_response.json().get('objects', [])
                    steering_files = [item for item in folder_items 
                                    if item.get('path', '').endswith('_steering_report.md')]
                    
                    if steering_files:
                        # Get the latest steering report file
                        latest_file = sorted(steering_files, key=lambda x: x['path'], reverse=True)[0]
                        file_path = latest_file['path']
                        
                        print(f"📄 Found steering report: {file_path}")
                        
                        export_response = requests.get(export_url, headers=headers, 
                                                     params={"path": file_path, "format": "AUTO"})
                        
                        if export_response.status_code == 200:
                            data = export_response.json()
                            content_b64 = data.get('content', '')
                            content = base64.b64decode(content_b64).decode('utf-8')
                            
                            # Save to local file
                            output_file = Path(__file__).parent / Path(file_path).name
                            with open(output_file, 'w') as f:
                                f.write(content)
                            
                            print(f"✅ Successfully downloaded steering report")
                            print(f"   Saved to: {output_file.absolute()}")
                            
                            # Show a preview of the output
                            print(f"\n{'='*80}")
                            print(f"📄 STEERING REPORT PREVIEW")
                            print(f"{'='*80}")
                            lines = content.split('\n')
                            preview_lines = lines[:50]  # First 50 lines
                            print('\n'.join(preview_lines))
                            if len(lines) > 50:
                                print(f"\n... ({len(lines) - 50} more lines)")
                            
                            return 0
                        else:
                            print(f"   ⚠️  Could not download file (status: {export_response.status_code})")
                    else:
                        # Try searching all steering folders for the file
                        print(f"⚠️  No steering report files found in {folder_path}, searching all steering folders...")
                        all_steering_files = []
                        for folder_item in steering_folders:
                            folder_path_to_search = folder_item['path']
                            folder_resp = requests.get(folder_list_url, headers=headers, params={"path": folder_path_to_search})
                            if folder_resp.status_code == 200:
                                folder_items = folder_resp.json().get('objects', [])
                                steering_files = [item for item in folder_items 
                                                if item.get('path', '').endswith('_steering_report.md')]
                                all_steering_files.extend(steering_files)
                        
                        if all_steering_files:
                            latest_file = sorted(all_steering_files, key=lambda x: x['path'], reverse=True)[0]
                            file_path = latest_file['path']
                            print(f"📄 Found steering report in another folder: {file_path}")
                            
                            export_response = requests.get(export_url, headers=headers, 
                                                         params={"path": file_path, "format": "AUTO"})
                            
                            if export_response.status_code == 200:
                                data = export_response.json()
                                content_b64 = data.get('content', '')
                                content = base64.b64decode(content_b64).decode('utf-8')
                                
                                output_file = Path(__file__).parent / Path(file_path).name
                                with open(output_file, 'w') as f:
                                    f.write(content)
                                
                                print(f"✅ Successfully downloaded steering report")
                                print(f"   Saved to: {output_file.absolute()}")
                                
                                # Show a preview
                                print(f"\n{'='*80}")
                                print(f"📄 STEERING REPORT PREVIEW")
                                print(f"{'='*80}")
                                lines = content.split('\n')
                                preview_lines = lines[:50]
                                print('\n'.join(preview_lines))
                                if len(lines) > 50:
                                    print(f"\n... ({len(lines) - 50} more lines)")
                                
                                return 0
                        else:
                            print(f"⚠️  No steering report files found in any steering folder")
                else:
                    print(f"⚠️  Could not list folder contents (status: {folder_response.status_code})")
            else:
                print(f"⚠️  No long-term-steering folders found in workspace")
        else:
            print(f"⚠️  Could not list workspace (status: {response.status_code})")
    except Exception as e:
        print(f"⚠️  Error downloading file: {e}")
        import traceback
        traceback.print_exc()
    
    print(f"\n📁 Check the Databricks workspace for the output file:")
    print(f"   {workspace_base}/long-term-steering-*/W*_steering_report.md")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())

