#!/usr/bin/env python3
"""
Databricks MCP Server

A Model Context Protocol server for Databricks operations.
Uses FastMCP for cleaner tool definitions.

Tools:
- execute_sql: Run any SQL query
- run_sql_file: Execute SQL from a local file
- create_notebook: Create notebooks in Databricks workspace
- run_notebook: Create and run notebooks as jobs
- get_job_status: Check job run status
- sync_to_workspace: Upload local files to Databricks
- sync_from_workspace: Download Databricks files locally

Configuration:
- Set environment variables or create a .env file in this directory:
  - DATABRICKS_HOST: Full workspace URL (e.g., https://xxx.cloud.databricks.com)
  - DATABRICKS_TOKEN: Personal access token
  - DATABRICKS_HTTP_PATH: SQL warehouse HTTP path
  - DATABRICKS_SERVER_HOSTNAME: Workspace hostname (without https://)
  - CLUSTER_ID: Cluster ID for notebook jobs

Usage:
    python server.py

Configure in ~/.cursor/mcp.json to use with Cursor.
"""

import os
import sys
import json
import time
from pathlib import Path
from typing import Optional, Any

# Add parent directories to path for imports
_REPO_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(_REPO_ROOT))

# Load .env from MCP directory if it exists
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).parent / '.env'
    if env_path.exists():
        load_dotenv(env_path)
except ImportError:
    pass

# =============================================================================
# IMPORTS FROM CORE MODULES
# =============================================================================

from core._config import get_config
from core.connection_pool import get_pool, ConnectionPool
from core.databricks_job_runner import DatabricksJobRunner
from core.workspace_sync import WorkspaceSync

# =============================================================================
# MCP SERVER SETUP (FastMCP pattern)
# =============================================================================

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print("MCP SDK not installed. Install with: pip install mcp", file=sys.stderr)
    sys.exit(1)

# Initialize FastMCP server
mcp = FastMCP("Databricks MCP")

# Initialize shared resources (lazy loading)
_config = get_config()
_pool: Optional[ConnectionPool] = None
_job_runner: Optional[DatabricksJobRunner] = None


def get_pool_instance() -> ConnectionPool:
    """Get or create the connection pool instance."""
    global _pool
    if _pool is None:
        _pool = get_pool()
        _pool.initialize()
    return _pool


def get_job_runner() -> DatabricksJobRunner:
    """Get or create the job runner instance."""
    global _job_runner
    if _job_runner is None:
        _job_runner = DatabricksJobRunner()
    return _job_runner


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def format_results_structured(
    results: list, 
    limit: int = 100, 
    execution_time_ms: float = None
) -> dict[str, Any]:
    """
    Format query results as structured JSON for AI agents.
    
    Returns a dictionary with:
    - success: bool
    - row_count: int
    - columns: list of column names
    - data: list of row dictionaries
    - truncated: bool (if results were limited)
    - execution_time_ms: float (optional)
    """
    if not results:
        return {
            "success": True,
            "row_count": 0,
            "columns": [],
            "data": [],
            "truncated": False,
            "message": "Query returned 0 rows",
            "execution_time_ms": execution_time_ms
        }
    
    # Extract column names
    columns = []
    first_row = results[0]
    if hasattr(first_row, '_fields'):
        columns = list(first_row._fields)
    elif hasattr(first_row, 'asDict'):
        columns = list(first_row.asDict().keys())
    
    # Convert rows to dictionaries
    data = []
    for row in results[:limit]:
        row_dict = {}
        
        if hasattr(row, 'asDict'):
            row_dict = row.asDict()
        elif hasattr(row, '_asdict'):
            row_dict = dict(row._asdict())
        elif hasattr(row, '_fields'):
            row_dict = {col: val for col, val in zip(row._fields, row)}
        else:
            row_dict = {"value": str(row)}
        
        # Convert non-serializable types to strings
        for k, v in row_dict.items():
            if v is not None and not isinstance(v, (str, int, float, bool, list, dict)):
                row_dict[k] = str(v)
        
        data.append(row_dict)
    
    return {
        "success": True,
        "row_count": len(results),
        "rows_returned": len(data),
        "columns": columns,
        "data": data,
        "truncated": len(results) > limit,
        "execution_time_ms": execution_time_ms
    }


def format_results_text(results: list, limit: int = 100) -> str:
    """Format query results as readable text (legacy format)."""
    if not results:
        return "Query returned 0 rows."
    
    lines = [f"Query returned {len(results)} rows:\n"]
    
    if hasattr(results[0], '_fields'):
        lines.append(" | ".join(str(h) for h in results[0]._fields))
        lines.append("-" * 80)
    
    for row in results[:limit]:
        if hasattr(row, '_fields'):
            lines.append(" | ".join(str(v) for v in row))
        else:
            lines.append(str(row))
    
    if len(results) > limit:
        lines.append(f"\n... and {len(results) - limit} more rows")
    
    return "\n".join(lines)


def add_limit_if_needed(query: str, limit: int) -> str:
    """Add LIMIT clause to SELECT queries if not present."""
    query_upper = query.strip().upper()
    if query_upper.startswith("SELECT") and "LIMIT" not in query_upper:
        return f"{query.rstrip(';')} LIMIT {limit}"
    return query


# =============================================================================
# MCP TOOLS
# =============================================================================

@mcp.tool()
def execute_sql(query: str, limit: int = 100) -> dict[str, Any]:
    """
    Execute any SQL query on Databricks. This is the primary tool for all data operations.

    Common patterns:
    - List tables: SHOW TABLES IN schema_name
    - Describe table: DESCRIBE table_name
    - Sample data: SELECT * FROM table LIMIT 10
    - Find duplicates: SELECT col, COUNT(*) FROM table GROUP BY col HAVING COUNT(*) > 1
    - Profile column: SELECT COUNT(*), COUNT(col), COUNT(DISTINCT col) FROM table
    - Create table: CREATE TABLE new_table AS SELECT ...

    Args:
        query: SQL query to execute
        limit: Max rows to return (default: 100)

    Returns:
        JSON with: success, row_count, columns, data[], execution_time_ms, truncated
    """
    try:
        pool = get_pool_instance()
        
        # Add LIMIT if SELECT without LIMIT
        original_query = query
        query = add_limit_if_needed(query, limit)
        
        # Execute with timing
        start_time = time.time()
        results = pool.execute(query)
        execution_time_ms = round((time.time() - start_time) * 1000, 2)
        
        # Return structured response
        response = format_results_structured(results, limit=limit, execution_time_ms=execution_time_ms)
        response["query"] = original_query[:200] + "..." if len(original_query) > 200 else original_query
        
        return response
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "query": query[:200] + "..." if len(query) > 200 else query
        }


@mcp.tool()
def run_sql_file(file_path: str, output_format: str = "json", limit: int = 100) -> dict[str, Any]:
    """
    Execute SQL from a local file. Useful for complex queries stored in .sql files.

    Args:
        file_path: Path to the SQL file
        output_format: Output format - 'json' (structured) or 'show' (text). Default: json
        limit: Maximum rows to return (default: 100)

    Returns:
        JSON with: success, row_count, columns, data[], file_path, execution_time_ms
    """
    try:
        # Read SQL file
        with open(file_path, 'r') as f:
            query = f.read()
        
        query = add_limit_if_needed(query, limit)
        
        pool = get_pool_instance()
        
        # Execute with timing
        start_time = time.time()
        results = pool.execute(query)
        execution_time_ms = round((time.time() - start_time) * 1000, 2)
        
        if output_format == 'show':
            # Legacy text format
            text_output = format_results_text(results, limit)
            return {
                "success": True,
                "file_path": file_path,
                "output_format": "text",
                "execution_time_ms": execution_time_ms,
                "output": text_output
            }
        else:
            # Structured JSON format (default)
            response = format_results_structured(results, limit=limit, execution_time_ms=execution_time_ms)
            response["file_path"] = file_path
            return response
            
    except FileNotFoundError:
        return {
            "success": False,
            "error": f"File not found: {file_path}",
            "file_path": file_path
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "file_path": file_path
        }


@mcp.tool()
def create_notebook(notebook_path: str, content: str, overwrite: bool = True) -> dict[str, Any]:
    """
    Create a Python notebook in Databricks workspace.

    Args:
        notebook_path: Path in Databricks workspace (e.g., /Workspace/Users/user@example.com/my_notebook)
        content: Python notebook content
        overwrite: If True, overwrite existing notebook (default: True)

    Returns:
        JSON with: success, notebook_path, action, overwrite
    """
    try:
        runner = get_job_runner()
        success = runner.create_notebook(notebook_path, content, overwrite)
        
        return {
            "success": success,
            "notebook_path": notebook_path,
            "action": "created" if success else "failed",
            "overwrite": overwrite,
            "error": None if success else "Failed to create notebook"
        }
        
    except Exception as e:
        return {
            "success": False,
            "notebook_path": notebook_path,
            "action": "failed",
            "error": str(e)
        }


@mcp.tool()
def run_notebook(
    notebook_path: str, 
    notebook_content: str, 
    job_name: str,
    timeout_seconds: int = 3600,
    poll_interval: int = 10
) -> dict[str, Any]:
    """
    Create and run a notebook as a Databricks job. Waits for completion and returns output.

    Args:
        notebook_path: Path in Databricks workspace
        notebook_content: Python notebook content
        job_name: Name for the Databricks job
        timeout_seconds: Job timeout in seconds (default: 3600)
        poll_interval: Seconds between status checks (default: 10)

    Returns:
        JSON with: success, notebook_path, job_name, job_id, run_id, state, result_state, outputs[]
    """
    runner = get_job_runner()
    
    result = {
        'success': False,
        'notebook_path': notebook_path,
        'job_name': job_name
    }
    
    try:
        # Step 1: Create notebook
        if not runner.create_notebook(notebook_path, notebook_content):
            result['error'] = 'Failed to create notebook'
            return result
        
        # Step 2: Create job
        job_id = runner.create_job(notebook_path, job_name, timeout_seconds)
        if not job_id:
            result['error'] = 'Failed to create job'
            return result
        result['job_id'] = job_id
        
        # Step 3: Run job
        run_id = runner.run_job(job_id)
        if not run_id:
            result['error'] = 'Failed to run job'
            return result
        result['run_id'] = run_id
        
        # Step 4: Monitor job
        start_time = time.time()
        max_wait = timeout_seconds
        
        while True:
            status = runner.get_run_status(run_id)
            if not status:
                result['error'] = 'Failed to get job status'
                return result
            
            state = status.get('state', {})
            life_cycle_state = state.get('life_cycle_state', 'UNKNOWN')
            result_state = state.get('result_state')
            
            # Job finished
            if life_cycle_state in ['TERMINATED', 'SKIPPED', 'INTERNAL_ERROR']:
                result['state'] = life_cycle_state
                result['result_state'] = result_state
                result['success'] = result_state == 'SUCCESS'
                
                # Collect output
                if 'tasks' in status:
                    outputs = []
                    for task in status.get('tasks', []):
                        task_run_id = task.get('run_id')
                        if task_run_id:
                            task_output = runner.get_task_output(task_run_id)
                            if task_output:
                                outputs.append(task_output)
                    result['outputs'] = outputs
                
                return result
            
            # Timeout check
            if time.time() - start_time > max_wait:
                result['error'] = 'Job timed out'
                result['state'] = 'TIMEOUT'
                return result
            
            time.sleep(poll_interval)
            
    except Exception as e:
        result['error'] = str(e)
        return result


@mcp.tool()
def get_job_status(run_id: int) -> dict[str, Any]:
    """
    Get the status of a Databricks job run.

    Args:
        run_id: Databricks job run ID

    Returns:
        JSON with: success, run_id, life_cycle_state, result_state, is_running, is_complete, is_success
    """
    try:
        runner = get_job_runner()
        status = runner.get_run_status(str(run_id))
        
        if status:
            state = status.get('state', {})
            return {
                "success": True,
                "run_id": run_id,
                "life_cycle_state": state.get('life_cycle_state'),
                "result_state": state.get('result_state'),
                "state_message": state.get('state_message'),
                "is_running": state.get('life_cycle_state') in ['PENDING', 'RUNNING', 'TERMINATING'],
                "is_complete": state.get('life_cycle_state') in ['TERMINATED', 'SKIPPED', 'INTERNAL_ERROR'],
                "is_success": state.get('result_state') == 'SUCCESS',
                "full_status": status
            }
        else:
            return {
                "success": False,
                "run_id": run_id,
                "error": f"Could not get status for run {run_id}"
            }
            
    except Exception as e:
        return {
            "success": False,
            "run_id": run_id,
            "error": str(e)
        }


@mcp.tool()
def sync_to_workspace(
    local_dir: str, 
    workspace_dir: str, 
    pattern: str = "**/*.py",
    dry_run: bool = False
) -> dict[str, Any]:
    """
    Sync local files to Databricks workspace.

    Args:
        local_dir: Local directory path
        workspace_dir: Databricks workspace directory
        pattern: File pattern to sync (default: **/*.py)
        dry_run: If True, preview without uploading (default: False)

    Returns:
        JSON with: success, action, local_dir, workspace_dir, files_synced, dry_run
    """
    try:
        sync = WorkspaceSync(local_dir=local_dir, workspace_dir=workspace_dir)
        result = sync.sync_to_workspace(pattern=pattern, dry_run=dry_run)
        
        # Ensure structured response
        if not isinstance(result, dict):
            result = {"result": result}
        
        result["success"] = result.get("success", True)
        result["action"] = "sync_to_workspace"
        result["local_dir"] = local_dir
        result["workspace_dir"] = workspace_dir
        result["dry_run"] = dry_run
        
        return result
        
    except Exception as e:
        return {
            "success": False,
            "action": "sync_to_workspace",
            "local_dir": local_dir,
            "workspace_dir": workspace_dir,
            "dry_run": dry_run,
            "error": str(e)
        }


@mcp.tool()
def sync_from_workspace(
    local_dir: str, 
    workspace_dir: str, 
    dry_run: bool = False
) -> dict[str, Any]:
    """
    Sync files from Databricks workspace to local directory.

    Args:
        local_dir: Local directory path
        workspace_dir: Databricks workspace directory
        dry_run: If True, preview without downloading (default: False)

    Returns:
        JSON with: success, action, local_dir, workspace_dir, files_synced, dry_run
    """
    try:
        sync = WorkspaceSync(local_dir=local_dir, workspace_dir=workspace_dir)
        result = sync.sync_from_workspace(dry_run=dry_run)
        
        # Ensure structured response
        if not isinstance(result, dict):
            result = {"result": result}
        
        result["success"] = result.get("success", True)
        result["action"] = "sync_from_workspace"
        result["local_dir"] = local_dir
        result["workspace_dir"] = workspace_dir
        result["dry_run"] = dry_run
        
        return result
        
    except Exception as e:
        return {
            "success": False,
            "action": "sync_from_workspace",
            "local_dir": local_dir,
            "workspace_dir": workspace_dir,
            "dry_run": dry_run,
            "error": str(e)
        }


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    mcp.run()
