#!/usr/bin/env python3
"""
Databricks MCP Server - Standalone Edition

A completely self-contained Model Context Protocol server for Databricks.
NO external dependencies on local modules - everything is inlined.

Tools:
- execute_sql: Run any SQL query
- run_sql_file: Execute SQL from a local file
- create_notebook: Create notebooks in Databricks workspace
- run_notebook: Create and run notebooks as jobs
- get_job_status: Check job run status
- sync_to_workspace: Upload local files to Databricks
- sync_from_workspace: Download Databricks files locally

Configuration:
- Set environment variables or create a .env file:
  - DATABRICKS_HOST: Full workspace URL (e.g., https://xxx.cloud.databricks.com)
  - DATABRICKS_TOKEN: Personal access token
  - DATABRICKS_HTTP_PATH: SQL warehouse HTTP path
  - DATABRICKS_SERVER_HOSTNAME: Workspace hostname (without https://)
  - CLUSTER_ID: Cluster ID for notebook jobs

Usage:
    python mcp_server_standalone.py

Configure in ~/.cursor/mcp.json to use with Cursor.
"""

import os
import sys
import json
import asyncio
import atexit
import base64
import time
import re
from pathlib import Path
from typing import Optional, Dict, List, Any

# =============================================================================
# CONFIGURATION - Load from environment variables
# =============================================================================

def load_config():
    """Load configuration from environment variables or .env file."""
    # Try to load from .env file
    try:
        from dotenv import load_dotenv
        # Look for .env in same directory as this script
        env_path = Path(__file__).parent / '.env'
        if env_path.exists():
            load_dotenv(env_path)
    except ImportError:
        pass  # dotenv not installed, use system env vars
    
    config = {
        'DATABRICKS_HOST': os.getenv('DATABRICKS_HOST', ''),
        'TOKEN': os.getenv('DATABRICKS_TOKEN', ''),
        'HTTP_PATH': os.getenv('DATABRICKS_HTTP_PATH', ''),
        'SERVER_HOSTNAME': os.getenv('DATABRICKS_SERVER_HOSTNAME', ''),
        'CLUSTER_ID': os.getenv('CLUSTER_ID', ''),
    }
    
    # Derive SERVER_HOSTNAME from DATABRICKS_HOST if not set
    if not config['SERVER_HOSTNAME'] and config['DATABRICKS_HOST']:
        config['SERVER_HOSTNAME'] = config['DATABRICKS_HOST'].replace('https://', '').replace('http://', '')
    
    # Validate required config
    missing = [k for k in ['DATABRICKS_HOST', 'TOKEN', 'HTTP_PATH'] if not config.get(k)]
    if missing:
        print(f"⚠️  Missing required config: {', '.join(missing)}", file=sys.stderr)
        print("   Set environment variables or create .env file", file=sys.stderr)
    
    return config

CONFIG = load_config()

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

# =============================================================================
# CONNECTION POOL - Persistent SQL connections
# =============================================================================

class ConnectionPool:
    """Persistent connection pool for Databricks SQL."""
    
    def __init__(self):
        self._connection = None
        self._initialized = False
    
    def _create_connection(self):
        from databricks import sql
        return sql.connect(
            server_hostname=CONFIG['SERVER_HOSTNAME'],
            http_path=CONFIG['HTTP_PATH'],
            access_token=CONFIG['TOKEN'],
            timeout_seconds=300
        )
    
    def initialize(self):
        if not self._initialized and CONFIG['TOKEN']:
            try:
                self._connection = self._create_connection()
                self._initialized = True
                print("✅ Databricks SQL connection initialized", file=sys.stderr)
            except Exception as e:
                print(f"❌ Failed to initialize connection: {e}", file=sys.stderr)
    
    def get_connection(self):
        if self._connection is None:
            self._connection = self._create_connection()
            self._initialized = True
        return self._connection
    
    def execute_query(self, query: str) -> list:
        try:
            conn = self.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except Exception as e:
            print(f"Query failed, attempting reconnect: {e}", file=sys.stderr)
            self._connection = None
            conn = self.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
    
    def close(self):
        if self._connection:
            try:
                self._connection.close()
            except:
                pass
            self._connection = None
            self._initialized = False

_pool = ConnectionPool()
atexit.register(_pool.close)

# =============================================================================
# DATABRICKS REST API CLIENT - Inlined from core/databricks_job_runner.py
# =============================================================================

class DatabricksClient:
    """
    Databricks REST API client for notebook and job operations.
    Completely self-contained - no external dependencies.
    """
    
    def __init__(self):
        self.host = CONFIG['DATABRICKS_HOST']
        self.token = CONFIG['TOKEN']
        self.cluster_id = CONFIG['CLUSTER_ID']
        self.headers = {"Authorization": f"Bearer {self.token}"}
    
    def _request(self, method: str, endpoint: str, **kwargs) -> Optional[Dict]:
        """Make HTTP request to Databricks API."""
        import requests
        url = f"{self.host}{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
            response.raise_for_status()
            return response.json() if response.text else {}
        except Exception as e:
            print(f"❌ API error: {e}", file=sys.stderr)
            return None
    
    # -------------------------------------------------------------------------
    # Notebook Operations
    # -------------------------------------------------------------------------
    
    def create_notebook(self, notebook_path: str, content: str, overwrite: bool = True) -> bool:
        """Create a notebook in Databricks workspace."""
        content_b64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
        
        result = self._request('POST', '/api/2.0/workspace/import', json={
            "path": notebook_path,
            "content": content_b64,
            "format": "SOURCE",
            "language": "PYTHON",
            "overwrite": overwrite
        })
        return result is not None
    
    # -------------------------------------------------------------------------
    # Job Operations
    # -------------------------------------------------------------------------
    
    def create_job(self, notebook_path: str, job_name: str, timeout_seconds: int = 3600) -> Optional[str]:
        """Create a Databricks job that runs a notebook."""
        result = self._request('POST', '/api/2.1/jobs/create', json={
            "name": job_name,
            "tasks": [{
                "task_key": "run_notebook",
                "notebook_task": {"notebook_path": notebook_path},
                "existing_cluster_id": self.cluster_id,
                "timeout_seconds": timeout_seconds,
                "max_retries": 0
            }],
            "timeout_seconds": timeout_seconds,
            "max_concurrent_runs": 1
        })
        return result.get('job_id') if result else None
    
    def run_job(self, job_id: str) -> Optional[str]:
        """Start a job run."""
        result = self._request('POST', '/api/2.1/jobs/run-now', json={"job_id": job_id})
        return result.get('run_id') if result else None
    
    def get_run_status(self, run_id: str) -> Optional[Dict]:
        """Get job run status."""
        return self._request('GET', f'/api/2.1/jobs/runs/get?run_id={run_id}')
    
    def get_task_output(self, task_run_id: str) -> Optional[Dict]:
        """Get output from a task run."""
        return self._request('GET', f'/api/2.1/jobs/runs/get-output?run_id={task_run_id}')
    
    def create_and_run_notebook(self, notebook_path: str, notebook_content: str, 
                                 job_name: str, timeout_seconds: int = 3600,
                                 poll_interval: int = 10, max_wait: int = 3600) -> Dict:
        """
        Complete workflow: create notebook, create job, run job, and monitor.
        Returns dictionary with job status and outputs.
        """
        result = {
            'success': False,
            'notebook_path': notebook_path,
            'job_name': job_name
        }
        
        # Step 1: Create notebook
        if not self.create_notebook(notebook_path, notebook_content):
            result['error'] = 'Failed to create notebook'
            return result
        
        # Step 2: Create job
        job_id = self.create_job(notebook_path, job_name, timeout_seconds)
        if not job_id:
            result['error'] = 'Failed to create job'
            return result
        result['job_id'] = job_id
        
        # Step 3: Run job
        run_id = self.run_job(job_id)
        if not run_id:
            result['error'] = 'Failed to run job'
            return result
        result['run_id'] = run_id
        
        # Step 4: Monitor job
        start_time = time.time()
        while True:
            status = self.get_run_status(run_id)
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
                            task_output = self.get_task_output(task_run_id)
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
    
    # -------------------------------------------------------------------------
    # Workspace Sync Operations - Inlined from core/workspace_sync.py
    # -------------------------------------------------------------------------
    
    def _create_workspace_dirs(self, workspace_path: str):
        """Create directory structure in workspace."""
        import requests
        path_parts = workspace_path.strip('/').split('/')
        for i in range(1, len(path_parts)):
            parent_path = '/' + '/'.join(path_parts[:i])
            try:
                requests.post(
                    f"{self.host}/api/2.0/workspace/mkdirs",
                    headers=self.headers,
                    json={"path": parent_path}
                )
            except:
                pass
    
    def upload_file(self, local_path: Path, workspace_path: str, overwrite: bool = True) -> Dict:
        """Upload a single file to Databricks workspace."""
        import requests
        
        if not local_path.exists():
            return {'success': False, 'error': f'File not found: {local_path}'}
        
        try:
            with open(local_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return {'success': False, 'error': f'Error reading file: {e}'}
        
        # Create directory structure
        workspace_dir = '/'.join(workspace_path.split('/')[:-1])
        self._create_workspace_dirs(workspace_dir)
        
        # Determine language from extension
        ext = local_path.suffix.lower()
        language = {'py': 'PYTHON', '.sql': 'SQL', '.scala': 'SCALA', '.r': 'R'}.get(ext, 'PYTHON')
        
        # Upload
        content_b64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
        try:
            response = requests.post(
                f"{self.host}/api/2.0/workspace/import",
                headers=self.headers,
                json={
                    "path": workspace_path,
                    "content": content_b64,
                    "format": "SOURCE",
                    "language": language,
                    "overwrite": overwrite
                }
            )
            response.raise_for_status()
            return {'success': True, 'local_path': str(local_path), 'workspace_path': workspace_path}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def download_file(self, workspace_path: str, local_path: Path, overwrite: bool = True) -> Dict:
        """Download a file from Databricks workspace."""
        import requests
        
        if local_path.exists() and not overwrite:
            return {'success': False, 'error': f'File exists: {local_path}'}
        
        local_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            response = requests.get(
                f"{self.host}/api/2.0/workspace/export",
                headers=self.headers,
                params={"path": workspace_path, "format": "SOURCE"}
            )
            response.raise_for_status()
            
            content_b64 = response.json().get('content', '')
            content = base64.b64decode(content_b64).decode('utf-8')
            
            with open(local_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return {'success': True, 'workspace_path': workspace_path, 'local_path': str(local_path)}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def list_workspace_files(self, workspace_dir: str, recursive: bool = True) -> List[str]:
        """List all files in workspace directory."""
        import requests
        files = []
        
        try:
            response = requests.get(
                f"{self.host}/api/2.0/workspace/list",
                headers=self.headers,
                params={"path": workspace_dir}
            )
            response.raise_for_status()
            
            for item in response.json().get('objects', []):
                path = item['path']
                obj_type = item.get('object_type', '')
                
                if obj_type in ['NOTEBOOK', 'FILE']:
                    files.append(path)
                elif obj_type == 'DIRECTORY' and recursive:
                    files.extend(self.list_workspace_files(path, recursive=True))
        except Exception as e:
            print(f"⚠️  Error listing workspace: {e}", file=sys.stderr)
        
        return files
    
    def sync_to_workspace(self, local_dir: str, workspace_dir: str, 
                          pattern: str = "**/*.py", dry_run: bool = False) -> Dict:
        """Sync local files to Databricks workspace."""
        local_path = Path(local_dir).expanduser().resolve()
        files = list(local_path.glob(pattern))
        
        results = {'success': [], 'failed': [], 'total': len(files)}
        
        for file_path in files:
            if file_path.is_file():
                relative = file_path.relative_to(local_path)
                ws_path = f"{workspace_dir.rstrip('/')}/{relative.as_posix()}"
                
                if dry_run:
                    results['success'].append({'local': str(file_path), 'workspace': ws_path, 'dry_run': True})
                else:
                    result = self.upload_file(file_path, ws_path)
                    if result['success']:
                        results['success'].append(result)
                    else:
                        results['failed'].append(result)
        
        return results
    
    def sync_from_workspace(self, local_dir: str, workspace_dir: str, dry_run: bool = False) -> Dict:
        """Sync workspace files to local directory."""
        local_path = Path(local_dir).expanduser().resolve()
        local_path.mkdir(parents=True, exist_ok=True)
        
        workspace_files = self.list_workspace_files(workspace_dir)
        results = {'success': [], 'failed': [], 'total': len(workspace_files)}
        
        for ws_path in workspace_files:
            if ws_path.startswith(workspace_dir):
                relative = ws_path.replace(workspace_dir, '').lstrip('/')
                file_path = local_path / relative
                
                if dry_run:
                    results['success'].append({'workspace': ws_path, 'local': str(file_path), 'dry_run': True})
                else:
                    result = self.download_file(ws_path, file_path)
                    if result['success']:
                        results['success'].append(result)
                    else:
                        results['failed'].append(result)
        
        return results

# Global client instance
_client = DatabricksClient()

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

Returns formatted results with column headers.""",
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
            description="Execute SQL from a local file. Useful for complex queries stored in .sql files.",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_path": {"type": "string", "description": "Path to the SQL file"},
                    "output_format": {"type": "string", "enum": ["show", "csv", "json"], "default": "show"},
                    "limit": {"type": "integer", "description": "Maximum rows to return", "default": 100}
                },
                "required": ["file_path"]
            }
        ),
        Tool(
            name="create_notebook",
            description="Create a Python notebook in Databricks workspace.",
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
            description="Create and run a notebook as a Databricks job. Waits for completion and returns output.",
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
            description="Get the status of a Databricks job run.",
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
            description="Sync local files to Databricks workspace.",
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
            description="Sync files from Databricks workspace to local directory.",
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
    """Handle tool calls."""
    try:
        # ---------------------------------------------------------------------
        # SQL Operations
        # ---------------------------------------------------------------------
        if name == "execute_sql":
            query = arguments["query"]
            limit = arguments.get("limit", 100)
            
            # Add LIMIT if SELECT without LIMIT
            query_upper = query.strip().upper()
            if query_upper.startswith("SELECT") and "LIMIT" not in query_upper:
                query = f"{query.rstrip(';')} LIMIT {limit}"
            
            results = _pool.execute_query(query)
            
            if not results:
                return [TextContent(type="text", text="Query returned 0 rows.")]
            
            # Format results
            lines = [f"Query returned {len(results)} rows:\n"]
            if hasattr(results[0], '_fields'):
                lines.append(" | ".join(str(h) for h in results[0]._fields))
                lines.append("-" * 80)
            
            for row in results[:limit]:
                if hasattr(row, '_fields'):
                    lines.append(" | ".join(str(v) for v in row))
                else:
                    lines.append(str(row))
            
            return [TextContent(type="text", text="\n".join(lines))]
        
        # ---------------------------------------------------------------------
        elif name == "run_sql_file":
            file_path = arguments["file_path"]
            output_format = arguments.get("output_format", "show")
            limit = arguments.get("limit", 100)
            
            with open(file_path, 'r') as f:
                query = f.read()
            
            query_upper = query.strip().upper()
            if query_upper.startswith("SELECT") and "LIMIT" not in query_upper:
                query = f"{query.rstrip(';')} LIMIT {limit}"
            
            results = _pool.execute_query(query)
            
            if not results:
                return [TextContent(type="text", text="Query returned 0 rows.")]
            
            if output_format == 'json':
                data = [dict(r._asdict()) if hasattr(r, '_asdict') else str(r) for r in results]
                return [TextContent(type="text", text=json.dumps(data, indent=2, default=str))]
            else:
                lines = [f"Query returned {len(results)} rows:\n"]
                if results and hasattr(results[0], '_fields'):
                    lines.append(" | ".join(results[0]._fields))
                    lines.append("-" * 80)
                for row in results:
                    lines.append(" | ".join(str(v) for v in row) if hasattr(row, '_fields') else str(row))
                return [TextContent(type="text", text="\n".join(lines))]
        
        # ---------------------------------------------------------------------
        # Notebook Operations
        # ---------------------------------------------------------------------
        elif name == "create_notebook":
            success = _client.create_notebook(
                arguments["notebook_path"],
                arguments["content"],
                arguments.get("overwrite", True)
            )
            if success:
                return [TextContent(type="text", text=f"✅ Notebook created at {arguments['notebook_path']}")]
            else:
                return [TextContent(type="text", text=f"❌ Failed to create notebook")]
        
        # ---------------------------------------------------------------------
        elif name == "run_notebook":
            result = _client.create_and_run_notebook(
                arguments["notebook_path"],
                arguments["notebook_content"],
                arguments["job_name"]
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]
        
        # ---------------------------------------------------------------------
        elif name == "get_job_status":
            status = _client.get_run_status(str(arguments["run_id"]))
            if status:
                return [TextContent(type="text", text=json.dumps(status, indent=2, default=str))]
            else:
                return [TextContent(type="text", text=f"Could not get status for run {arguments['run_id']}")]
        
        # ---------------------------------------------------------------------
        # Workspace Sync Operations
        # ---------------------------------------------------------------------
        elif name == "sync_to_workspace":
            result = _client.sync_to_workspace(
                arguments["local_dir"],
                arguments["workspace_dir"],
                arguments.get("pattern", "**/*.py"),
                arguments.get("dry_run", False)
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]
        
        # ---------------------------------------------------------------------
        elif name == "sync_from_workspace":
            result = _client.sync_from_workspace(
                arguments["local_dir"],
                arguments["workspace_dir"],
                arguments.get("dry_run", False)
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]
        
        # ---------------------------------------------------------------------
        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]
    
    except Exception as e:
        import traceback
        return [TextContent(type="text", text=f"Error: {str(e)}\n{traceback.format_exc()}")]

# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

async def main():
    """Run the MCP server."""
    _pool.initialize()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
