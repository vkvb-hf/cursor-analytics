#!/usr/bin/env python3
"""
Generic Databricks Notebook and Job Runner

This module provides utilities to:
1. Create Databricks notebooks
2. Submit them as jobs
3. Monitor job execution
4. Display output in real-time
"""

import requests
import json
import time
import sys
import os
import base64
from typing import Optional, Dict, List

# Import config - works both when installed as package and when run directly
try:
    from core._config import DATABRICKS_HOST, TOKEN, CLUSTER_ID
except ImportError:
    # Fallback for direct script execution
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from config import DATABRICKS_HOST, TOKEN, CLUSTER_ID


class DatabricksJobRunner:
    """Generic utility for creating notebooks and running them as jobs."""
    
    def __init__(self, host: str = None, token: str = None, cluster_id: str = None):
        self.host = host or DATABRICKS_HOST
        self.token = token or TOKEN
        self.cluster_id = cluster_id or CLUSTER_ID
        self.headers = {"Authorization": f"Bearer {self.token}"}
    
    def create_notebook(self, notebook_path: str, content: str, overwrite: bool = True) -> bool:
        """
        Create a notebook in Databricks workspace.
        
        Args:
            notebook_path: Full path to notebook (e.g., /Workspace/Users/user@example.com/my_notebook)
            content: Notebook content (Python source code)
            overwrite: If True, overwrite existing notebook
        
        Returns:
            True if successful, False otherwise
        """
        print(f"📝 Creating notebook: {notebook_path}")
        
        # Encode content as base64
        content_b64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
        
        url = f"{self.host}/api/2.0/workspace/import"
        payload = {
            "path": notebook_path,
            "content": content_b64,
            "format": "SOURCE",
            "language": "PYTHON",
            "overwrite": overwrite
        }
        
        try:
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            print(f"✅ Notebook created successfully!")
            return True
        except Exception as e:
            print(f"❌ Error creating notebook: {e}")
            if hasattr(e, 'response') and hasattr(e.response, 'text'):
                print(f"   Response: {e.response.text}")
            return False
    
    def create_job(
        self, 
        notebook_path: str, 
        job_name: str = None,
        timeout_seconds: int = 3600,
        max_retries: int = 0
    ) -> Optional[str]:
        """
        Create a Databricks job that runs a notebook.
        
        Args:
            notebook_path: Path to notebook to run
            job_name: Name for the job (defaults to notebook name)
            timeout_seconds: Job timeout in seconds
            max_retries: Maximum retry attempts
        
        Returns:
            Job ID if successful, None otherwise
        """
        if not job_name:
            job_name = f"Run {notebook_path.split('/')[-1]}"
        
        print(f"🚀 Creating Databricks job: {job_name}")
        
        url = f"{self.host}/api/2.1/jobs/create"
        payload = {
            "name": job_name,
            "tasks": [{
                "task_key": "run_notebook",
                "notebook_task": {
                    "notebook_path": notebook_path
                },
                "existing_cluster_id": self.cluster_id,
                "timeout_seconds": timeout_seconds,
                "max_retries": max_retries
            }],
            "timeout_seconds": timeout_seconds,
            "max_concurrent_runs": 1
        }
        
        try:
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            job_data = response.json()
            job_id = job_data['job_id']
            print(f"✅ Job created! Job ID: {job_id}")
            return job_id
        except Exception as e:
            print(f"❌ Error creating job: {e}")
            if hasattr(e, 'response') and hasattr(e.response, 'text'):
                print(f"   Response: {e.response.text}")
            return None
    
    def run_job(self, job_id: str) -> Optional[str]:
        """
        Run a Databricks job.
        
        Args:
            job_id: Job ID to run
        
        Returns:
            Run ID if successful, None otherwise
        """
        print(f"▶️  Starting job run...")
        
        url = f"{self.host}/api/2.1/jobs/run-now"
        payload = {"job_id": job_id}
        
        try:
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            run_data = response.json()
            run_id = run_data['run_id']
            print(f"✅ Job run started! Run ID: {run_id}")
            return run_id
        except Exception as e:
            print(f"❌ Error running job: {e}")
            if hasattr(e, 'response') and hasattr(e.response, 'text'):
                print(f"   Response: {e.response.text}")
            return None
    
    def get_run_status(self, run_id: str) -> Optional[Dict]:
        """Get the status of a job run."""
        url = f"{self.host}/api/2.1/jobs/runs/get?run_id={run_id}"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ Error getting run status: {e}")
            return None
    
    def get_task_output(self, task_run_id: str) -> Optional[Dict]:
        """Get output from a specific task run."""
        url = f"{self.host}/api/2.1/jobs/runs/get-output?run_id={task_run_id}"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            # Silently fail - task might not have output yet
            return None
    
    def monitor_job(
        self, 
        run_id: str, 
        poll_interval: int = 10,
        max_wait: int = 3600,
        show_output: bool = True
    ) -> Dict:
        """
        Monitor job execution and display output.
        
        Args:
            run_id: Run ID to monitor
            poll_interval: Seconds between status checks
            max_wait: Maximum seconds to wait
            show_output: If True, display job output
        
        Returns:
            Dictionary with final status and output
        """
        print(f"\n📊 Monitoring job run: {run_id}")
        print("=" * 80)
        
        states = {
            'PENDING': '⏳ Pending',
            'RUNNING': '⚡ Running',
            'TERMINATING': '🔄 Terminating',
            'TERMINATED': '✅ Terminated',
            'SKIPPED': '⏭️  Skipped',
            'INTERNAL_ERROR': '❌ Internal Error'
        }
        
        result_states = {
            'SUCCESS': '✅ Success',
            'FAILED': '❌ Failed',
            'TIMEDOUT': '⏱️  Timeout',
            'CANCELED': '🚫 Canceled'
        }
        
        last_state = None
        start_time = time.time()
        output_collected = []
        
        while True:
            status = self.get_run_status(run_id)
            if not status:
                break
            
            state = status['state'].get('life_cycle_state', 'UNKNOWN')
            result_state = status['state'].get('result_state')
            
            # Show state change
            if state != last_state:
                state_display = states.get(state, state)
                print(f"\n{state_display}: {state}")
                if result_state:
                    result_display = result_states.get(result_state, result_state)
                    print(f"   Result: {result_display}")
                last_state = state
                
                # If running, show elapsed time
                if state == 'RUNNING':
                    elapsed = int(time.time() - start_time)
                    print(f"   ⏱️  Elapsed: {elapsed}s")
            
            # If job is finished
            if state in ['TERMINATED', 'SKIPPED', 'INTERNAL_ERROR']:
                print("\n" + "=" * 80)
                
                # Collect output from all tasks
                if show_output:
                    output_collected = self._collect_outputs(status)
                
                # Final status
                if result_state == 'SUCCESS':
                    print("\n✅ Job completed successfully!")
                else:
                    print(f"\n⚠️  Job finished with state: {result_state}")
                
                return {
                    'run_id': run_id,
                    'state': state,
                    'result_state': result_state,
                    'output': output_collected
                }
            
            # Check timeout
            if time.time() - start_time > max_wait:
                print("\n⏱️  Timeout reached. Job may still be running.")
                print(f"   Check job status in Databricks UI")
                return {
                    'run_id': run_id,
                    'state': 'TIMEOUT',
                    'result_state': None,
                    'output': output_collected
                }
            
            time.sleep(poll_interval)
    
    def _collect_outputs(self, status: Dict) -> List[Dict]:
        """
        Collect and display outputs from all tasks in a job run.
        Uses Databricks native API to get notebook cell outputs - works universally for any notebook.
        """
        outputs = []
        
        # Try to get task outputs
        if 'tasks' in status:
            for task in status.get('tasks', []):
                task_run_id = task.get('run_id')
                task_key = task.get('task_key', 'unknown')
                
                if task_run_id:
                    task_output = self.get_task_output(task_run_id)
                    if task_output:
                        outputs.append({
                            'task_key': task_key,
                            'output': task_output
                        })
        
        # Display outputs in a readable format
        if outputs:
            print("\n" + "=" * 80)
            print("📋 NOTEBOOK OUTPUT (from Databricks API)")
            print("=" * 80)
            
            for output_info in outputs:
                task_key = output_info['task_key']
                output = output_info['output']
                
                print(f"\n📌 Task: {task_key}")
                print("-" * 80)
                
                # Extract notebook output - this is the universal way to get output
                if 'notebook_output' in output and 'result' in output['notebook_output']:
                    result = output['notebook_output']['result']
                    
                    # Print all text output (print statements, query results, etc.)
                    if result.get('data'):
                        for item in result.get('data', []):
                            # Handle text/plain output (most common - print statements, query results)
                            if 'text/plain' in item:
                                print(item['text/plain'])
                            # Handle text/html (DataFrame displays, etc.)
                            elif 'text/html' in item:
                                # For HTML, try to extract text content
                                # In most cases, HTML contains formatted tables that we can't easily parse
                                # But we can at least indicate it's there
                                html_content = item['text/html']
                                # Try to extract text from simple HTML
                                import re
                                # Remove HTML tags for basic text extraction
                                text = re.sub(r'<[^>]+>', '', html_content)
                                if text.strip():
                                    print(text.strip())
                            # Handle other output types
                            elif 'application/vnd.databricks.result-v1+json' in item:
                                # Structured data - try to format it
                                try:
                                    import json
                                    data = item['application/vnd.databricks.result-v1+json']
                                    if isinstance(data, str):
                                        data = json.loads(data)
                                    print(json.dumps(data, indent=2))
                                except:
                                    print(str(item))
                    
                    # Show errors if any
                    if result.get('errorSummary'):
                        print(f"\n❌ Error: {result['errorSummary']}")
                    if result.get('cause'):
                        print(f"   Cause: {result['cause']}")
                
                # Handle direct error in output
                elif 'error' in output:
                    print(f"❌ Error: {output['error']}")
                    if 'error_trace' in output:
                        print(f"   Trace: {output['error_trace']}")
                
                print("-" * 80)
        else:
            # No outputs found - might still be processing
            print("\n⚠️  No output available yet (job may still be processing)")
        
        return outputs
    
    def create_and_run(
        self,
        notebook_path: str,
        notebook_content: str,
        job_name: str = None,
        timeout_seconds: int = 3600,
        poll_interval: int = 10,
        max_wait: int = 3600,
        show_output: bool = True,
        auto_read_output: bool = True,
        output_path: str = None,
        auto_inject_output: bool = True
    ) -> Dict:
        """
        Complete workflow: create notebook, create job, run job, and monitor.
        
        Args:
            notebook_path: Path where notebook will be created
            notebook_content: Notebook content (Python source)
            job_name: Name for the job
            timeout_seconds: Job timeout
            poll_interval: Status check interval
            max_wait: Maximum wait time
            show_output: Show job output
            auto_read_output: Automatically read output from DBFS after job completes
            output_path: Specific output path to read (if None, auto-detect)
            auto_inject_output: Automatically inject NotebookOutput framework (default: True)
        
        Returns:
            Dictionary with job status and outputs
        """
        print("=" * 80)
        print("Databricks Notebook & Job Runner")
        print("=" * 80)
        
        # Step 0: Auto-inject DBFS output writing (WORKING approach)
        if auto_inject_output:
            try:
                from core.dbfs_output_injector import inject_dbfs_output
                notebook_content = inject_dbfs_output(
                    notebook_content,
                    job_name=job_name
                )
                print("✅ DBFS output writing auto-injected (output will be visible in terminal)")
            except Exception as e:
                print(f"⚠️  Warning: Could not inject DBFS output: {e}")
                print("   Continuing without auto-injection...")
        
        # Step 1: Create notebook
        if not self.create_notebook(notebook_path, notebook_content):
            return {'success': False, 'error': 'Failed to create notebook'}
        
        # Step 2: Create job
        job_id = self.create_job(notebook_path, job_name, timeout_seconds)
        if not job_id:
            return {'success': False, 'error': 'Failed to create job'}
        
        # Step 3: Run job
        run_id = self.run_job(job_id)
        if not run_id:
            return {'success': False, 'error': 'Failed to run job'}
        
        # Step 4: Monitor job
        result = self.monitor_job(run_id, poll_interval, max_wait, show_output)
        result['job_id'] = job_id
        result['notebook_path'] = notebook_path
        result['run_id'] = run_id
        result['success'] = result.get('result_state') == 'SUCCESS'
        
        # Step 5: Read output from DBFS if requested
        if auto_read_output and result.get('success'):
            # Try to read from standard output location first (used by DBFS injector)
            standard_output_path = f"/tmp/notebook_outputs/{job_name.replace(' ', '_')}_output.txt" if job_name else "/tmp/notebook_outputs/notebook_output.txt"
            
            try:
                from core.notebook_output_reader import NotebookOutputReader
                reader = NotebookOutputReader()
                content = reader.read_output(standard_output_path)
                if content:
                    print("\n" + "=" * 80)
                    print("📊 NOTEBOOK OUTPUT (from DBFS)")
                    print("=" * 80)
                    print(content)
                    print("=" * 80)
                    return result
            except Exception as e:
                # Fall back to regular output reading
                pass
            
            # Fall back to regular output reading
            self._read_notebook_output(job_name, run_id, output_path)
        
        return result
    
    def _read_notebook_output(self, job_name: str = None, run_id: str = None, output_path: str = None):
        """
        Read and display notebook output from DBFS.
        
        Args:
            job_name: Job name to find output file
            run_id: Run ID for output file
            output_path: Specific output path (if provided, use this)
        """
        try:
            from core.notebook_output_reader import NotebookOutputReader
            
            reader = NotebookOutputReader()
            
            if output_path:
                # Use specific path
                reader.display_output(output_path)
            else:
                # Try to find output file
                if job_name:
                    # Try to find by job name
                    latest = reader.get_latest_output(job_name=job_name)
                    if latest:
                        reader.display_output(latest)
                        return
                
                # Try to find latest output
                latest = reader.get_latest_output()
                if latest:
                    reader.display_output(latest)
                else:
                    print("\n⚠️  No output file found in /tmp/notebook_outputs/")
                    print("   Make sure your notebook uses NotebookOutput.write_to_dbfs()")
                    
        except ImportError:
            print("\n⚠️  Could not import NotebookOutputReader")
            print("   Output reading disabled")
        except Exception as e:
            print(f"\n⚠️  Error reading output: {e}")


def main():
    """Example usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Run Databricks notebook as job')
    parser.add_argument('--notebook-path', required=True, help='Notebook path')
    parser.add_argument('--notebook-file', required=True, help='Notebook content file')
    parser.add_argument('--job-name', help='Job name (optional)')
    parser.add_argument('--timeout', type=int, default=3600, help='Timeout in seconds')
    
    args = parser.parse_args()
    
    # Read notebook content
    with open(args.notebook_file, 'r') as f:
        content = f.read()
    
    # Create runner and execute
    runner = DatabricksJobRunner()
    result = runner.create_and_run(
        notebook_path=args.notebook_path,
        notebook_content=content,
        job_name=args.job_name,
        timeout_seconds=args.timeout
    )
    
    sys.exit(0 if result.get('success') else 1)


if __name__ == "__main__":
    main()

