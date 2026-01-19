#!/usr/bin/env python3
"""
Retrieve cluster logs from DBFS for job execution output.
"""
import requests
import sys
import os

# Import config - works both when installed as package and when run directly
try:
    from core._config import DATABRICKS_HOST, TOKEN
except ImportError:
    # Fallback for direct script execution
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from config import DATABRICKS_HOST, TOKEN


def get_cluster_logs(cluster_id: str, run_id: str = None):
    """
    Get cluster logs from DBFS.
    
    Args:
        cluster_id: Cluster ID
        run_id: Optional run ID to filter logs
    
    Returns:
        Log content or None
    """
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    # Try to list files in cluster logs directory
    log_path = f"/cluster-logs/{cluster_id}/driver"
    
    # List files in the log directory
    list_url = f"{DATABRICKS_HOST}/api/2.0/dbfs/list"
    list_payload = {"path": log_path}
    
    try:
        list_response = requests.get(list_url, headers=headers, json=list_payload)
        if list_response.status_code == 200:
            files = list_response.json().get('files', [])
            
            # Look for stdout/stderr files
            stdout_files = [f for f in files if 'stdout' in f.get('path', '').lower()]
            stderr_files = [f for f in files if 'stderr' in f.get('path', '').lower()]
            
            logs = {}
            
            # Read stdout files
            for file_info in stdout_files[:5]:  # Limit to first 5 files
                file_path = file_info['path']
                read_url = f"{DATABRICKS_HOST}/api/2.0/dbfs/read"
                read_payload = {"path": file_path}
                read_response = requests.get(read_url, headers=headers, json=read_payload)
                if read_response.status_code == 200:
                    content = read_response.json().get('data', '')
                    # Decode base64 if needed
                    if content:
                        import base64
                        try:
                            decoded = base64.b64decode(content).decode('utf-8')
                            logs[file_path] = decoded
                        except:
                            logs[file_path] = content
            
            # Read stderr files
            for file_info in stderr_files[:5]:  # Limit to first 5 files
                file_path = file_info['path']
                read_url = f"{DATABRICKS_HOST}/api/2.0/dbfs/read"
                read_payload = {"path": file_path}
                read_response = requests.get(read_url, headers=headers, json=read_payload)
                if read_response.status_code == 200:
                    content = read_response.json().get('data', '')
                    # Decode base64 if needed
                    if content:
                        import base64
                        try:
                            decoded = base64.b64decode(content).decode('utf-8')
                            logs[file_path] = decoded
                        except:
                            logs[file_path] = content
            
            return logs
        else:
            print(f"⚠️  Could not list log files: {list_response.status_code}")
            return None
    except Exception as e:
        print(f"⚠️  Error accessing cluster logs: {e}")
        return None


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python get_cluster_logs.py <cluster_id> [run_id]")
        sys.exit(1)
    
    cluster_id = sys.argv[1]
    run_id = sys.argv[2] if len(sys.argv) > 2 else None
    
    logs = get_cluster_logs(cluster_id, run_id)
    if logs:
        for path, content in logs.items():
            print(f"\n{'=' * 80}")
            print(f"Log: {path}")
            print(f"{'=' * 80}")
            print(content[-5000:])  # Show last 5000 chars
    else:
        print("No logs found or error accessing logs")


