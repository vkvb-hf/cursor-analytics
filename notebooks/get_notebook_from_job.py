#!/usr/bin/env python3
"""
Get notebook content from a Databricks job or notebook ID.
"""

import requests
import base64
import sys
import json
from config import DATABRICKS_HOST, TOKEN

def get_job_details(job_id):
    """Get details of a Databricks job."""
    headers = {"Authorization": f"Bearer {TOKEN}"}
    url = f"{DATABRICKS_HOST}/api/2.1/jobs/get"
    params = {"job_id": job_id}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error getting job details: {e}")
        if hasattr(e, 'response') and hasattr(e.response, 'text'):
            print(f"Response: {e.response.text}")
        return None

def get_notebook(notebook_path):
    """Download notebook content from Databricks workspace."""
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    url = f"{DATABRICKS_HOST}/api/2.0/workspace/export"
    params = {"path": notebook_path, "format": "SOURCE"}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        content_b64 = data.get('content', '')
        content = base64.b64decode(content_b64).decode('utf-8')
        
        return content
    except Exception as e:
        print(f"Error getting notebook: {e}")
        if hasattr(e, 'response') and hasattr(e.response, 'text'):
            print(f"Response: {e.response.text}")
        return None

def get_notebook_by_id(notebook_id):
    """Try to get notebook by ID using the notebooks API."""
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    # Try the notebooks API endpoint
    url = f"{DATABRICKS_HOST}/api/2.0/workspace/export"
    # Unfortunately, the API doesn't support IDs directly, we need the path
    # So we'll need to search or use the job to find the path
    
    return None

if __name__ == "__main__":
    # Job ID from the URL
    job_id = "863174042909812"
    notebook_id = "3549820133656532"
    
    print("=" * 80)
    print("Fetching Databricks Notebook")
    print("=" * 80)
    print(f"Job ID: {job_id}")
    print(f"Notebook ID: {notebook_id}")
    print()
    
    # Step 1: Get job details to find the notebook path
    print("📋 Step 1: Getting job details...")
    job_details = get_job_details(job_id)
    
    if not job_details:
        print("❌ Could not get job details")
        sys.exit(1)
    
    print("✅ Job details retrieved")
    
    # Extract notebook path from job
    notebook_path = None
    
    # Check tasks for notebook paths
    if 'settings' in job_details and 'tasks' in job_details['settings']:
        tasks = job_details['settings']['tasks']
        for task in tasks:
            if 'notebook_task' in task:
                notebook_path = task['notebook_task'].get('notebook_path')
                print(f"   Found notebook path: {notebook_path}")
                break
    
    if not notebook_path:
        print("⚠️  Could not find notebook path in job details")
        print("   Job settings:")
        print(json.dumps(job_details.get('settings', {}), indent=2))
        
        # Try to search workspace for the notebook
        print("\n🔍 Searching workspace for notebooks...")
        workspace_path = "/Workspace/Users/visal.kumar@hellofresh.com"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        url = f"{DATABRICKS_HOST}/api/2.0/workspace/list"
        response = requests.get(url, headers=headers, params={"path": workspace_path})
        
        if response.status_code == 200:
            data = response.json()
            print(f"\nFiles in {workspace_path}:")
            notebooks_found = []
            for item in data.get('objects', []):
                if item.get('object_type') in ['NOTEBOOK', 'FILE']:
                    path = item.get('path', '')
                    notebooks_found.append(path)
                    print(f"  - {path}")
            
            # Try common paths that might contain steering metrics
            steering_paths = [
                p for p in notebooks_found 
                if 'steering' in p.lower() or 'output' in p.lower() or 'metrics' in p.lower()
            ]
            
            if steering_paths:
                print(f"\n📌 Found potential steering-related notebooks:")
                for path in steering_paths:
                    print(f"   - {path}")
                notebook_path = steering_paths[0]  # Try the first one
                print(f"\n   Trying: {notebook_path}")
        
        if not notebook_path:
            print("\n❌ Could not determine notebook path")
            sys.exit(1)
    
    # Step 2: Get notebook content
    print(f"\n📝 Step 2: Getting notebook content from: {notebook_path}")
    notebook_content = get_notebook(notebook_path)
    
    if not notebook_content:
        print("❌ Could not get notebook content")
        sys.exit(1)
    
    print(f"✅ Notebook content retrieved ({len(notebook_content)} characters)")
    
    # Step 3: Display the steering metrics generation part
    print("\n" + "=" * 80)
    print("NOTEBOOK CONTENT")
    print("=" * 80)
    print(notebook_content)
    
    # Save to file
    output_file = f"notebook_{notebook_id}.py"
    with open(output_file, 'w') as f:
        f.write(notebook_content)
    print(f"\n💾 Saved notebook to: {output_file}")
    
    # Search for steering metrics generation
    print("\n" + "=" * 80)
    print("STEERING METRICS GENERATION SECTION")
    print("=" * 80)
    
    lines = notebook_content.split('\n')
    steering_sections = []
    in_steering_section = False
    current_section = []
    
    keywords = ['steering', 'write_formatted_summaries', 'generate_overall_summary', 
                'STEERING_METRICS', 'significance', 'z_score']
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        if any(keyword.lower() in line_lower for keyword in keywords):
            in_steering_section = True
            current_section = [(i+1, line)]
        elif in_steering_section:
            current_section.append((i+1, line))
            # End section after a blank line or function definition
            if line.strip() == '' and len(current_section) > 10:
                steering_sections.append(current_section)
                current_section = []
                in_steering_section = False
    
    if current_section:
        steering_sections.append(current_section)
    
    if steering_sections:
        print(f"\nFound {len(steering_sections)} section(s) related to steering metrics:")
        for idx, section in enumerate(steering_sections, 1):
            print(f"\n--- Section {idx} (lines {section[0][0]}-{section[-1][0]}) ---")
            for line_num, line in section[:50]:  # Show first 50 lines
                print(f"{line_num:5d} | {line}")
            if len(section) > 50:
                print(f"... ({len(section) - 50} more lines)")
    else:
        print("\n⚠️  Could not automatically identify steering metrics sections")
        print("   Showing full notebook content above")

