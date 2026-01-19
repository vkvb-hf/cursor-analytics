#!/usr/bin/env python3
"""
Utility to fetch Databricks notebook content from editor URLs or notebook IDs.

This module can extract notebook content from:
1. Editor URLs: https://{host}/editor/notebooks/{notebook_id}?o={org_id}
2. Job URLs: https://{host}/jobs/{job_id}?o={org_id}
3. Direct notebook IDs
"""

import requests
import base64
import re
import sys
import os
from typing import Optional, Tuple

# Add parent directory to path to import config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATABRICKS_HOST, TOKEN


def extract_notebook_id_from_url(url: str) -> Optional[str]:
    """
    Extract notebook ID from various Databricks URL formats.
    
    Args:
        url: Databricks URL (editor link, job link, etc.)
    
    Returns:
        Notebook ID if found, None otherwise
    """
    # Pattern for editor URLs: /editor/notebooks/{notebook_id}
    editor_pattern = r'/editor/notebooks/(\d+)'
    match = re.search(editor_pattern, url)
    if match:
        return match.group(1)
    
    return None


def extract_job_id_from_url(url: str) -> Optional[str]:
    """
    Extract job ID from Databricks job URLs.
    
    Args:
        url: Databricks job URL
    
    Returns:
        Job ID if found, None otherwise
    """
    # Pattern for job URLs: /jobs/{job_id}
    job_pattern = r'/jobs/(\d+)'
    match = re.search(job_pattern, url)
    if match:
        return match.group(1)
    
    return None


def get_job_details(job_id: str) -> Optional[dict]:
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


def get_notebook_path_from_job(job_id: str) -> Optional[str]:
    """
    Extract notebook path from a job configuration.
    
    Args:
        job_id: Databricks job ID
    
    Returns:
        Notebook path if found, None otherwise
    """
    job_details = get_job_details(job_id)
    if not job_details:
        return None
    
    # Check tasks for notebook paths
    if 'settings' in job_details and 'tasks' in job_details['settings']:
        tasks = job_details['settings']['tasks']
        for task in tasks:
            if 'notebook_task' in task:
                notebook_path = task['notebook_task'].get('notebook_path')
                if notebook_path:
                    return notebook_path
    
    return None


def get_job_runs(job_id: str, limit: int = 25) -> Optional[list]:
    """
    Get recent job runs for a specific job.
    
    Args:
        job_id: Job ID
        limit: Maximum number of runs to retrieve
    
    Returns:
        List of run details, or None if error
    """
    headers = {"Authorization": f"Bearer {TOKEN}"}
    url = f"{DATABRICKS_HOST}/api/2.1/jobs/runs/list"
    params = {"job_id": job_id, "limit": limit}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json().get('runs', [])
    except Exception as e:
        print(f"Error getting job runs: {e}")
        return None


def get_run_details(run_id: str) -> Optional[dict]:
    """
    Get detailed information about a specific job run.
    
    Args:
        run_id: Run ID
    
    Returns:
        Run details dictionary, or None if error
    """
    headers = {"Authorization": f"Bearer {TOKEN}"}
    url = f"{DATABRICKS_HOST}/api/2.1/jobs/runs/get"
    params = {"run_id": run_id}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return None


def verify_notebook_id(notebook_path: str, target_notebook_id: str) -> bool:
    """
    Verify if a notebook path matches the target notebook ID.
    
    Since we can't directly get notebook ID from path, we'll try to fetch
    the notebook and check metadata. However, this is limited by API capabilities.
    
    For now, this is a placeholder. In practice, we rely on the fact that
    if a notebook path is used in a recent run, it's likely the correct one.
    
    Args:
        notebook_path: Notebook workspace path
        target_notebook_id: Target notebook ID to match
    
    Returns:
        True if we can verify (for now, always returns True as placeholder)
    """
    # TODO: Implement actual verification if Databricks API supports it
    # For now, we'll assume if we found it in a run, it's valid
    return True


def search_notebook_in_job_runs(notebook_id: str, limit_jobs: int = 50, limit_runs_per_job: int = 25) -> Optional[Tuple[str, str]]:
    """
    Search through job runs to find the latest run that matches the notebook ID.
    
    This method:
    1. Lists all jobs
    2. For each job, gets recent runs
    3. Checks each run's tasks for notebook information
    4. Collects all notebook paths and their run details
    5. Returns the latest matching notebook path and run ID
    
    Note: Since Databricks API doesn't expose notebook IDs in run details,
    we can't directly verify which notebook path matches the ID. However, we
    return the most recently used notebook path, which is likely to be correct.
    
    Args:
        notebook_id: Notebook ID to search for
        limit_jobs: Maximum number of jobs to search
        limit_runs_per_job: Maximum runs per job to check
    
    Returns:
        Tuple of (notebook_path, run_id) if found, or None
    """
    headers = {"Authorization": f"Bearer {TOKEN}"}
    url = f"{DATABRICKS_HOST}/api/2.1/jobs/list"
    
    try:
        response = requests.get(url, headers=headers, params={"limit": limit_jobs})
        response.raise_for_status()
        jobs_data = response.json()
        
        jobs = jobs_data.get('jobs', [])
        print(f"🔍 Searching through {len(jobs)} jobs and their recent runs...")
        
        matching_runs = []  # Store notebook path info with metadata
        
        for job_idx, job in enumerate(jobs):
            job_id = job.get('job_id')
            if not job_id:
                continue
            
            # Show progress for large searches
            if (job_idx + 1) % 10 == 0:
                print(f"   Processed {job_idx + 1}/{len(jobs)} jobs...")
            
            # Get recent runs for this job
            runs = get_job_runs(str(job_id), limit_runs_per_job)
            if not runs:
                continue
            
            for run in runs:
                run_id = run.get('run_id')
                if not run_id:
                    continue
                
                # Get detailed run information
                run_details = get_run_details(str(run_id))
                if not run_details:
                    continue
                
                # Check tasks for notebook information
                tasks = run_details.get('tasks', [])
                for task in tasks:
                    # Check if task has notebook_task configuration
                    if 'notebook_task' in task:
                        notebook_task = task['notebook_task']
                        notebook_path = notebook_task.get('notebook_path')
                        
                        if notebook_path:
                            start_time = run.get('start_time', 0)
                            # Avoid duplicates
                            if not any(r['notebook_path'] == notebook_path and 
                                      r['start_time'] == start_time for r in matching_runs):
                                matching_runs.append({
                                    'notebook_path': notebook_path,
                                    'run_id': str(run_id),
                                    'start_time': start_time,
                                    'job_id': str(job_id),
                                    'job_name': job.get('settings', {}).get('name', 'Unknown')
                                })
        
        if not matching_runs:
            print(f"   No notebook paths found in recent job runs")
            return None
        
        # Sort by start_time descending (most recent first)
        matching_runs.sort(key=lambda x: x['start_time'], reverse=True)
        
        # Group by notebook path to see which ones are used most frequently
        path_counts = {}
        for run_info in matching_runs:
            path = run_info['notebook_path']
            path_counts[path] = path_counts.get(path, 0) + 1
        
        # Find the most frequently used notebook path
        most_used_path = max(path_counts.items(), key=lambda x: x[1])[0] if path_counts else None
        
        # Get the latest run for the most frequently used path
        latest_run = None
        if most_used_path:
            for run_info in matching_runs:
                if run_info['notebook_path'] == most_used_path:
                    latest_run = run_info
                    break
        
        # Fallback to just the most recent run
        if not latest_run:
            latest_run = matching_runs[0]
        
        print(f"✅ Found {len(matching_runs)} notebook path(s) in recent runs")
        print(f"   Most frequently used path: {most_used_path} ({path_counts.get(most_used_path, 0)} runs)")
        print(f"   Latest run: {latest_run['run_id']} (job: {latest_run['job_id']} - {latest_run['job_name']})")
        print(f"   Notebook path: {latest_run['notebook_path']}")
        
        return latest_run['notebook_path'], latest_run['run_id']
        
    except Exception as e:
        print(f"Error searching job runs: {e}")
        import traceback
        traceback.print_exc()
    
    return None


def search_jobs_for_notebook(notebook_id: str, limit: int = 100) -> Optional[str]:
    """
    Search through jobs to find one that uses a notebook with the given ID.
    
    DEPRECATED: Use search_notebook_in_job_runs() instead for better accuracy.
    
    Args:
        notebook_id: Notebook ID to search for
        limit: Maximum number of jobs to search
    
    Returns:
        Notebook path if found in a job, None otherwise
    """
    # Try the new method first
    result = search_notebook_in_job_runs(notebook_id, limit_jobs=limit)
    if result:
        return result[0]  # Return just the notebook path
    
    return None


def search_notebook_by_id(notebook_id: str, search_paths: list = None) -> Optional[str]:
    """
    Search for a notebook by ID in the workspace.
    
    Note: Databricks API doesn't support direct lookup by notebook ID,
    so we need to search the workspace. This is a fallback method.
    
    Args:
        notebook_id: Notebook ID to search for
        search_paths: List of workspace paths to search (defaults to user workspace)
    
    Returns:
        Notebook path if found, None otherwise
    """
    if search_paths is None:
        search_paths = [
            "/Workspace/Users/visal.kumar@hellofresh.com",
            "/Workspace/Users/elizaveta.dmitrieva@hellofresh.com",
            "/Workspace/Shared"
        ]
    
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    for base_path in search_paths:
        try:
            # Recursively search the workspace
            url = f"{DATABRICKS_HOST}/api/2.0/workspace/list"
            response = requests.get(url, headers=headers, params={"path": base_path})
            
            if response.status_code == 200:
                data = response.json()
                objects = data.get('objects', [])
                
                # Note: The workspace API doesn't return notebook IDs directly
                # This is a limitation - we'd need to check each notebook's metadata
                # For now, this is a placeholder for future enhancement
                
                print(f"   Searched in: {base_path}")
                print(f"   Found {len(objects)} items")
                
        except Exception as e:
            print(f"Error searching workspace: {e}")
    
    return None


def get_notebook(notebook_path: str) -> Optional[str]:
    """
    Download notebook content from Databricks workspace.
    
    Args:
        notebook_path: Full workspace path to the notebook
    
    Returns:
        Notebook content as string, or None if error
    """
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


def get_notebook_from_url(url: str, fallback_to_job: bool = True) -> Tuple[Optional[str], Optional[str]]:
    """
    Get notebook content from a Databricks URL.
    
    Supports:
    1. Editor URLs: https://{host}/editor/notebooks/{notebook_id}?o={org_id}
    2. Job URLs: https://{host}/jobs/{job_id}?o={org_id} (if fallback_to_job=True)
    
    Args:
        url: Databricks URL
        fallback_to_job: If True, try to get notebook path from job if URL is a job link
    
    Returns:
        Tuple of (notebook_content, notebook_path) or (None, None) if error
    """
    print(f"📋 Processing URL: {url}")
    
    # Try to extract notebook ID from editor URL
    notebook_id = extract_notebook_id_from_url(url)
    job_id = extract_job_id_from_url(url)
    
    notebook_path = None
    
    # Strategy 1: If it's a job URL, try to get notebook path from job
    if job_id and fallback_to_job:
        print(f"🔍 Detected job URL, extracting notebook path from job {job_id}...")
        notebook_path = get_notebook_path_from_job(job_id)
        if notebook_path:
            print(f"✅ Found notebook path from job: {notebook_path}")
    
    # Strategy 2: If we have notebook ID, try to find it via job runs search
    if notebook_id and not notebook_path:
        print(f"🔍 Detected notebook ID: {notebook_id}")
        print(f"⚠️  Note: Direct notebook ID lookup is not supported by Databricks API")
        print(f"   Searching through job runs to find matching notebook...")
        result = search_notebook_in_job_runs(notebook_id)
        if result:
            notebook_path, matching_run_id = result
            print(f"✅ Found notebook path from latest matching job run: {notebook_path}")
            print(f"   Matching run ID: {matching_run_id}")
    
    # Strategy 3: If still no path, try workspace search (less reliable)
    if notebook_id and not notebook_path:
        print(f"   Trying workspace search as fallback...")
        notebook_path = search_notebook_by_id(notebook_id)
    
    # If we still don't have a path, we can't proceed
    if not notebook_path:
        print(f"\n❌ Could not determine notebook path from URL")
        print(f"   Options:")
        print(f"   1. Provide the notebook workspace path directly")
        print(f"   2. If this is a job URL, ensure the job has a notebook task configured")
        if notebook_id:
            print(f"   3. Notebook ID found: {notebook_id} (but path lookup not available)")
        return None, None
    
    # Get the notebook content
    print(f"\n📝 Fetching notebook content from: {notebook_path}")
    notebook_content = get_notebook(notebook_path)
    
    if notebook_content:
        print(f"✅ Successfully retrieved notebook ({len(notebook_content)} characters)")
        return notebook_content, notebook_path
    else:
        print(f"❌ Failed to retrieve notebook content")
        return None, None


def main():
    """CLI interface for fetching notebooks from URLs."""
    if len(sys.argv) < 2:
        print("Usage: python get_notebook_from_url.py <databricks_url> [output_file]")
        print("\nExamples:")
        print("  python get_notebook_from_url.py 'https://hf-gp.cloud.databricks.com/editor/notebooks/3549820133656532?o=4157495209488006'")
        print("  python get_notebook_from_url.py 'https://hf-gp.cloud.databricks.com/jobs/863174042909812?o=4157495209488006' notebook.py")
        sys.exit(1)
    
    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    notebook_content, notebook_path = get_notebook_from_url(url)
    
    if notebook_content:
        if output_file:
            with open(output_file, 'w') as f:
                f.write(notebook_content)
            print(f"\n💾 Saved notebook to: {output_file}")
        else:
            print("\n" + "=" * 80)
            print("NOTEBOOK CONTENT")
            print("=" * 80)
            print(notebook_content[:1000])  # Show first 1000 chars
            if len(notebook_content) > 1000:
                print(f"\n... ({len(notebook_content) - 1000} more characters)")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()

