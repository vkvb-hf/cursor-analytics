#!/usr/bin/env python3
"""
Databricks MCP Server

A Model Context Protocol server for Databricks operations.
Imports functionality from core/ modules to avoid code duplication.

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
import asyncio
from pathlib import Path
from typing import Optional

# Add parent directories to path for imports
# This allows the MCP server to import from core/ when run directly
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
# IMPORTS FROM CORE MODULES (No duplication!)
# =============================================================================

from core._config import get_config
from core.connection_pool import get_pool, ConnectionPool
from core.databricks_job_runner import DatabricksJobRunner
from core.workspace_sync import WorkspaceSync
from core.run_sql_file import run_sql_file as core_run_sql_file

# =============================================================================
# MCP SERVER SETUP
# =============================================================================

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
except ImportError:
    print("MCP SDK not installed. Install with: pip install mcp", file=sys.stderr)
    sys.exit(1)

server = Server("databricks-mcp")

# Initialize shared resources
_config = get_config()
_pool = get_pool()
_job_runner: Optional[DatabricksJobRunner] = None


def get_job_runner() -> DatabricksJobRunner:
    """Get or create the job runner instance."""
    global _job_runner
    if _job_runner is None:
        _job_runner = DatabricksJobRunner()
    return _job_runner


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

import time as _time

def format_results_structured(results: list, limit: int = 100, 
                               execution_time_ms: float = None,
                               query: str = None) -> dict:
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
    
    # Extract column names - handle both namedtuple and Databricks Row
    columns = []
    first_row = results[0]
    if hasattr(first_row, '_fields'):
        columns = list(first_row._fields)
    elif hasattr(first_row, 'asDict'):
        # Databricks Row object
        columns = list(first_row.asDict().keys())
    
    # Convert rows to dictionaries
    data = []
    for row in results[:limit]:
        row_dict = {}
        
        # Handle Databricks Row (has asDict method)
        if hasattr(row, 'asDict'):
            row_dict = row.asDict()
        # Handle namedtuple (has _asdict method)
        elif hasattr(row, '_asdict'):
            row_dict = dict(row._asdict())
        # Handle namedtuple with _fields
        elif hasattr(row, '_fields'):
            row_dict = {col: val for col, val in zip(row._fields, row)}
        # Fallback
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
    
    # Get column names from first row
    if hasattr(results[0], '_fields'):
        lines.append(" | ".join(str(h) for h in results[0]._fields))
        lines.append("-" * 80)
    
    # Format rows
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


def make_response(success: bool, data: dict = None, error: str = None) -> dict:
    """Create a standardized response structure."""
    response = {"success": success}
    if data:
        response.update(data)
    if error:
        response["error"] = error
    return response


# =============================================================================
# MCP TOOL DEFINITIONS
# =============================================================================

@server.list_tools()
async def list_tools():
    """List available Databricks tools."""
    return [
        Tool(
            name="execute_sql",
            description="""Execute any SQL query on Databricks. This is the primary tool for all data operations.

Common patterns:
- List tables: SHOW TABLES IN schema_name
- Describe table: DESCRIBE table_name
- Sample data: SELECT * FROM table LIMIT 10
- Find duplicates: SELECT col, COUNT(*) FROM table GROUP BY col HAVING COUNT(*) > 1
- Profile column: SELECT COUNT(*), COUNT(col), COUNT(DISTINCT col) FROM table
- Create table: CREATE TABLE new_table AS SELECT ...

Returns JSON with: success, row_count, columns, data[], execution_time_ms, truncated.""",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "SQL query to execute"},
                    "limit": {"type": "integer", "description": "Max rows to return (default: 100)", "default": 100}
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="run_sql_file",
            description="""Execute SQL from a local file. Useful for complex queries stored in .sql files.

Returns JSON with: success, row_count, columns, data[], file_path, execution_time_ms.
Use output_format='show' for legacy text output.""",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_path": {"type": "string", "description": "Path to the SQL file"},
                    "output_format": {"type": "string", "enum": ["json", "show"], "default": "json", "description": "Output format: json (structured) or show (text)"},
                    "limit": {"type": "integer", "description": "Maximum rows to return", "default": 100}
                },
                "required": ["file_path"]
            }
        ),
        Tool(
            name="create_notebook",
            description="""Create a Python notebook in Databricks workspace.

Returns JSON with: success, notebook_path, action, overwrite.""",
            inputSchema={
                "type": "object",
                "properties": {
                    "notebook_path": {"type": "string", "description": "Path in Databricks workspace"},
                    "content": {"type": "string", "description": "Python notebook content"},
                    "overwrite": {"type": "boolean", "default": True}
                },
                "required": ["notebook_path", "content"]
            }
        ),
        Tool(
            name="run_notebook",
            description="""Create and run a notebook as a Databricks job. Waits for completion and returns output.

Returns JSON with: success, notebook_path, job_name, job_id, run_id, state, result_state, outputs[].""",
            inputSchema={
                "type": "object",
                "properties": {
                    "notebook_path": {"type": "string", "description": "Path in Databricks workspace"},
                    "notebook_content": {"type": "string", "description": "Python notebook content"},
                    "job_name": {"type": "string", "description": "Name for the Databricks job"}
                },
                "required": ["notebook_path", "notebook_content", "job_name"]
            }
        ),
        Tool(
            name="get_job_status",
            description="""Get the status of a Databricks job run.

Returns JSON with: success, run_id, life_cycle_state, result_state, is_running, is_complete, is_success.""",
            inputSchema={
                "type": "object",
                "properties": {
                    "run_id": {"type": "integer", "description": "Databricks job run ID"}
                },
                "required": ["run_id"]
            }
        ),
        Tool(
            name="sync_to_workspace",
            description="""Sync local files to Databricks workspace.

Returns JSON with: success, action, local_dir, workspace_dir, files_synced, dry_run.""",
            inputSchema={
                "type": "object",
                "properties": {
                    "local_dir": {"type": "string", "description": "Local directory path"},
                    "workspace_dir": {"type": "string", "description": "Databricks workspace directory"},
                    "pattern": {"type": "string", "default": "**/*.py"},
                    "dry_run": {"type": "boolean", "default": False}
                },
                "required": ["local_dir", "workspace_dir"]
            }
        ),
        Tool(
            name="sync_from_workspace",
            description="""Sync files from Databricks workspace to local directory.

Returns JSON with: success, action, local_dir, workspace_dir, files_synced, dry_run.""",
            inputSchema={
                "type": "object",
                "properties": {
                    "local_dir": {"type": "string", "description": "Local directory path"},
                    "workspace_dir": {"type": "string", "description": "Databricks workspace directory"},
                    "dry_run": {"type": "boolean", "default": False}
                },
                "required": ["local_dir", "workspace_dir"]
            }
        )
    ]


# =============================================================================
# MCP TOOL HANDLERS
# =============================================================================

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls with structured JSON responses."""
    try:
        # -----------------------------------------------------------------
        # SQL Operations (using core.connection_pool)
        # -----------------------------------------------------------------
        if name == "execute_sql":
            query = arguments["query"]
            limit = arguments.get("limit", 100)
            
            # Add LIMIT if SELECT without LIMIT
            original_query = query
            query = add_limit_if_needed(query, limit)
            
            # Execute with timing
            start_time = _time.time()
            results = _pool.execute(query)
            execution_time_ms = round((_time.time() - start_time) * 1000, 2)
            
            # Return structured response
            response = format_results_structured(
                results, 
                limit=limit,
                execution_time_ms=execution_time_ms
            )
            response["query"] = original_query[:200] + "..." if len(original_query) > 200 else original_query
            
            return [TextContent(type="text", text=json.dumps(response, indent=2, default=str))]
        
        # -----------------------------------------------------------------
        elif name == "run_sql_file":
            file_path = arguments["file_path"]
            output_format = arguments.get("output_format", "json")  # Default to JSON now
            limit = arguments.get("limit", 100)
            
            # Read SQL file
            with open(file_path, 'r') as f:
                query = f.read()
            
            query = add_limit_if_needed(query, limit)
            
            # Execute with timing
            start_time = _time.time()
            results = _pool.execute(query)
            execution_time_ms = round((_time.time() - start_time) * 1000, 2)
            
            if output_format == 'show':
                # Legacy text format
                text_output = format_results_text(results, limit)
                response = make_response(True, {
                    "file_path": file_path,
                    "output_format": "text",
                    "execution_time_ms": execution_time_ms,
                    "output": text_output
                })
            else:
                # Structured JSON format (default)
                response = format_results_structured(
                    results,
                    limit=limit,
                    execution_time_ms=execution_time_ms
                )
                response["file_path"] = file_path
            
            return [TextContent(type="text", text=json.dumps(response, indent=2, default=str))]
        
        # -----------------------------------------------------------------
        # Notebook Operations (using core.databricks_job_runner)
        # -----------------------------------------------------------------
        elif name == "create_notebook":
            runner = get_job_runner()
            notebook_path = arguments["notebook_path"]
            
            success = runner.create_notebook(
                notebook_path,
                arguments["content"],
                arguments.get("overwrite", True)
            )
            
            response = make_response(
                success=success,
                data={
                    "notebook_path": notebook_path,
                    "action": "created" if success else "failed",
                    "overwrite": arguments.get("overwrite", True)
                },
                error=None if success else "Failed to create notebook"
            )
            return [TextContent(type="text", text=json.dumps(response, indent=2, default=str))]
        
        # -----------------------------------------------------------------
        elif name == "run_notebook":
            runner = get_job_runner()
            
            result = _run_notebook_simple(
                runner,
                arguments["notebook_path"],
                arguments["notebook_content"],
                arguments["job_name"]
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]
        
        # -----------------------------------------------------------------
        elif name == "get_job_status":
            runner = get_job_runner()
            run_id = arguments["run_id"]
            status = runner.get_run_status(str(run_id))
            
            if status:
                # Extract key info for easier parsing
                state = status.get('state', {})
                response = make_response(True, {
                    "run_id": run_id,
                    "life_cycle_state": state.get('life_cycle_state'),
                    "result_state": state.get('result_state'),
                    "state_message": state.get('state_message'),
                    "is_running": state.get('life_cycle_state') in ['PENDING', 'RUNNING', 'TERMINATING'],
                    "is_complete": state.get('life_cycle_state') in ['TERMINATED', 'SKIPPED', 'INTERNAL_ERROR'],
                    "is_success": state.get('result_state') == 'SUCCESS',
                    "full_status": status
                })
            else:
                response = make_response(False, {"run_id": run_id}, f"Could not get status for run {run_id}")
            
            return [TextContent(type="text", text=json.dumps(response, indent=2, default=str))]
        
        # -----------------------------------------------------------------
        # Workspace Sync Operations (using core.workspace_sync)
        # -----------------------------------------------------------------
        elif name == "sync_to_workspace":
            sync = WorkspaceSync(
                local_dir=arguments["local_dir"],
                workspace_dir=arguments["workspace_dir"]
            )
            result = sync.sync_to_workspace(
                pattern=arguments.get("pattern", "**/*.py"),
                dry_run=arguments.get("dry_run", False)
            )
            
            # Ensure structured response
            if not isinstance(result, dict):
                result = {"result": result}
            result["success"] = result.get("success", True)
            result["action"] = "sync_to_workspace"
            result["local_dir"] = arguments["local_dir"]
            result["workspace_dir"] = arguments["workspace_dir"]
            result["dry_run"] = arguments.get("dry_run", False)
            
            return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]
        
        # -----------------------------------------------------------------
        elif name == "sync_from_workspace":
            sync = WorkspaceSync(
                local_dir=arguments["local_dir"],
                workspace_dir=arguments["workspace_dir"]
            )
            result = sync.sync_from_workspace(
                dry_run=arguments.get("dry_run", False)
            )
            
            # Ensure structured response
            if not isinstance(result, dict):
                result = {"result": result}
            result["success"] = result.get("success", True)
            result["action"] = "sync_from_workspace"
            result["local_dir"] = arguments["local_dir"]
            result["workspace_dir"] = arguments["workspace_dir"]
            result["dry_run"] = arguments.get("dry_run", False)
            
            return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]
        
        # -----------------------------------------------------------------
        else:
            response = make_response(False, {"tool": name}, f"Unknown tool: {name}")
            return [TextContent(type="text", text=json.dumps(response, indent=2))]
    
    except Exception as e:
        import traceback
        response = make_response(False, {
            "tool": name,
            "arguments": arguments,
            "traceback": traceback.format_exc()
        }, str(e))
        return [TextContent(type="text", text=json.dumps(response, indent=2, default=str))]


def _run_notebook_simple(runner: DatabricksJobRunner, notebook_path: str, 
                         notebook_content: str, job_name: str,
                         timeout_seconds: int = 3600, poll_interval: int = 10,
                         max_wait: int = 3600) -> dict:
    """
    Simplified notebook run for MCP (no stdout printing).
    
    This is a streamlined version of DatabricksJobRunner.create_and_run()
    that returns structured data instead of printing to stdout.
    """
    import time
    
    result = {
        'success': False,
        'notebook_path': notebook_path,
        'job_name': job_name
    }
    
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


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

async def main():
    """Run the MCP server."""
    # Initialize connection pool
    _pool.initialize()
    
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
