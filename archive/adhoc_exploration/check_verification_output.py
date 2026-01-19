#!/usr/bin/env python3
"""Check the output of the verification job."""

import requests
import json
import sys
from config import DATABRICKS_HOST, TOKEN

def get_job_run(run_id):
    """Get job run details."""
    headers = {"Authorization": f"Bearer {TOKEN}"}
    url = f"{DATABRICKS_HOST}/api/2.1/jobs/runs/get?run_id={run_id}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def get_task_output(task_run_id):
    """Get output from a specific task run."""
    headers = {"Authorization": f"Bearer {TOKEN}"}
    url = f"{DATABRICKS_HOST}/api/2.1/jobs/runs/get-output?run_id={task_run_id}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    # Latest run ID from the verification
    run_id = "993626257199240"
    
    print("=" * 80)
    print("Fetching Verification Job Output")
    print("=" * 80)
    print(f"Run ID: {run_id}")
    
    # Get job run details to find task run IDs
    run_details = get_job_run(run_id)
    
    if not run_details:
        print("❌ Could not retrieve run details")
        sys.exit(1)
    
    # Get task run IDs
    tasks = run_details.get('tasks', [])
    if not tasks:
        print("❌ No tasks found in run")
        sys.exit(1)
    
    print(f"\nFound {len(tasks)} task(s)")
    
    # Get output from each task
    for task in tasks:
        task_key = task.get('task_key', 'unknown')
        task_run_id = task.get('run_id')
        
        print(f"\n📌 Task: {task_key} (Run ID: {task_run_id})")
        print("-" * 80)
        
        if task_run_id:
            output = get_task_output(task_run_id)
            
            if output and 'notebook_output' in output:
                notebook_output = output['notebook_output']
                if 'result' in notebook_output:
                    result = notebook_output['result']
                    if 'data' in result:
                        for item in result['data']:
                            if 'text/plain' in item:
                                print(item['text/plain'])
                    if 'errorSummary' in result:
                        print(f"\n❌ Error: {result['errorSummary']}")
                    if 'cause' in result:
                        print(f"   Cause: {result['cause']}")
            else:
                print("⚠️  No notebook output available")
        else:
            print("⚠️  No task run ID available")

