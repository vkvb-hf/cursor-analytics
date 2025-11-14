#!/usr/bin/env python3
"""Get detailed output from a job run."""

import sys
import requests
import json
from config import DATABRICKS_HOST, TOKEN

def get_job_output(run_id):
    """Get full output from job run."""
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    # Get run status
    status_url = f"{DATABRICKS_HOST}/api/2.1/jobs/runs/get?run_id={run_id}"
    status_response = requests.get(status_url, headers=headers)
    status_response.raise_for_status()
    status = status_response.json()
    
    print("=" * 80)
    print("Job Run Details")
    print("=" * 80)
    print(f"Run ID: {run_id}")
    print(f"State: {status['state'].get('life_cycle_state')}")
    print(f"Result: {status['state'].get('result_state')}")
    
    # Get task outputs
    if 'tasks' in status:
        for task in status.get('tasks', []):
            task_run_id = task.get('run_id')
            task_key = task.get('task_key')
            
            if task_run_id:
                print(f"\n{'=' * 80}")
                print(f"Task: {task_key}")
                print(f"Task Run ID: {task_run_id}")
                print(f"{'=' * 80}")
                
                output_url = f"{DATABRICKS_HOST}/api/2.1/jobs/runs/get-output?run_id={task_run_id}"
                output_response = requests.get(output_url, headers=headers)
                
                if output_response.status_code == 200:
                    output = output_response.json()
                    print(json.dumps(output, indent=2))
                else:
                    print(f"Status: {output_response.status_code}")
                    print(f"Response: {output_response.text}")

if __name__ == "__main__":
    run_id = sys.argv[1] if len(sys.argv) > 1 else "586070144964867"
    get_job_output(run_id)
