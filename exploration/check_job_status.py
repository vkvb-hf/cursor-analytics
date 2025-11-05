#!/usr/bin/env python3
"""Check the status and output of a Databricks job run."""

import requests
import sys
from config import DATABRICKS_HOST, TOKEN

def check_job_run(run_id):
    """Check job run status and get output."""
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    # Get run status
    status_url = f"{DATABRICKS_HOST}/api/2.1/jobs/runs/get?run_id={run_id}"
    status_response = requests.get(status_url, headers=headers)
    status_response.raise_for_status()
    status = status_response.json()
    
    print("=" * 80)
    print("Job Run Status")
    print("=" * 80)
    print(f"Run ID: {run_id}")
    print(f"State: {status['state'].get('life_cycle_state')}")
    print(f"Result: {status['state'].get('result_state')}")
    
    # Get output
    output_url = f"{DATABRICKS_HOST}/api/2.1/jobs/runs/get-output?run_id={run_id}"
    output_response = requests.get(output_url, headers=headers)
    
    if output_response.status_code == 200:
        output = output_response.json()
        print("\n" + "=" * 80)
        print("Job Output")
        print("=" * 80)
        print(json.dumps(output, indent=2))
    else:
        print(f"\n⚠️  Could not get output (status: {output_response.status_code})")
        print(f"   Response: {output_response.text}")

if __name__ == "__main__":
    import json
    run_id = sys.argv[1] if len(sys.argv) > 1 else "282827169992437"
    check_job_run(run_id)

