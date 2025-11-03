#!/usr/bin/env python3
"""
Check cluster status and start if needed
"""
import requests
from config import DATABRICKS_HOST, TOKEN as DATABRICKS_TOKEN, CLUSTER_ID

def check_and_start_cluster():
    """Check cluster status and start if terminated"""
    url = f"{DATABRICKS_HOST}/api/2.0/clusters/get"
    headers = {
        "Authorization": f"Bearer {DATABRICKS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    params = {"cluster_id": CLUSTER_ID}
    
    response = requests.get(url, headers=headers, params=params)
    result = response.json()
    
    print(f"Cluster ID: {result['cluster_id']}")
    print(f"Cluster Name: {result['cluster_name']}")
    print(f"State: {result['state']}")
    
    if result['state'] == 'TERMINATED':
        print("\n⚠️  Cluster is TERMINATED. Starting now...")
        start_url = f"{DATABRICKS_HOST}/api/2.0/clusters/start"
        start_response = requests.post(start_url, headers=headers, json={"cluster_id": CLUSTER_ID})
        print("✓ Cluster start requested. Waiting for it to become RUNNING...")
        print("   (This may take 5-10 minutes)")
    elif result['state'] == 'RUNNING':
        print("\n✓ Cluster is RUNNING. Ready to use!")
    elif result['state'] in ['PENDING', 'RESTARTING']:
        print(f"\n⏳ Cluster is {result['state']}. Please wait...")
    else:
        print(f"\nℹ️  Cluster state: {result['state']}")

if __name__ == "__main__":
    try:
        check_and_start_cluster()
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()

