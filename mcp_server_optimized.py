#!/usr/bin/env python3
"""
Databricks MCP Server (Optimized & Trimmed)

A lean Model Context Protocol server with only essential, non-redundant tools.
All SQL-based operations use execute_sql - no wrapper functions.

Tools:
- execute_sql: Run any SQL query (covers list_tables, describe, sample, profile, etc.)
- run_sql_file: Execute SQL from a local file
- create_notebook: Create notebooks in Databricks workspace
- run_notebook: Create and run notebooks as jobs
- get_job_status: Check job run status
- sync_to_workspace: Upload local files to Databricks
- sync_from_workspace: Download Databricks files locally

Usage:
    python mcp_server_optimized.py

Configure in ~/.cursor/mcp.json to use with Cursor.
"""

import sys
import os
import json
import asyncio
import atexit
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
except ImportError:
    print("MCP SDK not installed. Install with: pip install mcp", file=sys.stderr)
    sys.exit(1)

from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN, DATABRICKS_HOST, CLUSTER_ID

server = Server("databricks-mcp-optimized")


class ConnectionPool:
    """Persistent connection pool for Databricks SQL."""
    
    def __init__(self):
        self._connection = None
        self._initialized = False
    
    def _create_connection(self):
        from databricks import sql
        return sql.connect(
            server_hostname=SERVER_HOSTNAME,
            http_path=HTTP_PATH,
            access_token=TOKEN,
            timeout_seconds=300
        )
    
    def initialize(self):
        if not self._initialized:
            try:
                self._connection = self._create_connection()
                self._initialized = True
                print("Databricks connection initialized", file=sys.stderr)
            except Exception as e:
                print(f"Failed to initialize connection: {e}", file=sys.stderr)
    
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


class DatabricksAPI:
    """Lean Databricks API - only unique operations, no SQL wrappers."""
    
    def __init__(self):
        self._job_runner = None
    
    @property
    def job_runner(self):
        if self._job_runner is None:
            from core import DatabricksJobRunner
            self._job_runner = DatabricksJobRunner(
                host=DATABRICKS_HOST,
                token=TOKEN,
                cluster_id=CLUSTER_ID
            )
        return self._job_runner
    
    def run_sql(self, query: str) -> Optional[list]:
        try:
            return _pool.execute_query(query)
        except Exception as e:
            print(f"Error executing query: {e}", file=sys.stderr)
            return None
    
    def create_notebook(self, notebook_path: str, content: str, overwrite: bool = True) -> bool:
        return self.job_runner.create_notebook(notebook_path, content, overwrite)
    
    def run_notebook_job(self, notebook_path: str, notebook_content: str, job_name: str, **kwargs) -> Optional[dict]:
        return self.job_runner.create_and_run(
            notebook_path=notebook_path,
            notebook_content=notebook_content,
            job_name=job_name,
            **kwargs
        )
    
    def get_job_status(self, run_id: int) -> Optional[dict]:
        return self.job_runner.get_run_status(str(run_id))
    
    def sync_to_workspace(self, local_dir: str, workspace_dir: str, pattern: str = "**/*.py", dry_run: bool = False) -> dict:
        from core.workspace_sync import WorkspaceSync
        sync = WorkspaceSync(local_dir, workspace_dir)
        return sync.sync_to_workspace(pattern=pattern, dry_run=dry_run)
    
    def sync_from_workspace(self, local_dir: str, workspace_dir: str, dry_run: bool = False) -> dict:
        from core.workspace_sync import WorkspaceSync
        sync = WorkspaceSync(local_dir, workspace_dir)
        return sync.sync_from_workspace(dry_run=dry_run)


_api = DatabricksAPI()


@server.list_tools()
async def list_tools():
    """List available Databricks tools - optimized set only."""
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
                    "query": {
                        "type": "string",
                        "description": "SQL query to execute"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Max rows to return for SELECT queries (default: 100)",
                        "default": 100
                    }
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
                    "file_path": {
                        "type": "string",
                        "description": "Path to the SQL file"
                    },
                    "output_format": {
                        "type": "string",
                        "description": "Output format: 'show', 'csv', or 'json'",
                        "enum": ["show", "csv", "json"],
                        "default": "show"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum rows to return",
                        "default": 100
                    }
                },
                "required": ["file_path"]
            }
        ),
        Tool(
            name="create_notebook",
            description="Create a Python notebook in Databricks workspace. Content should be valid Databricks notebook format with # COMMAND ---------- separators.",
            inputSchema={
                "type": "object",
                "properties": {
                    "notebook_path": {
                        "type": "string",
                        "description": "Path in Databricks workspace (e.g., /Workspace/Users/user@example.com/my_notebook)"
                    },
                    "content": {
                        "type": "string",
                        "description": "Python notebook content"
                    },
                    "overwrite": {
                        "type": "boolean",
                        "description": "Overwrite if notebook exists",
                        "default": True
                    }
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
                    "notebook_path": {
                        "type": "string",
                        "description": "Path in Databricks workspace for the notebook"
                    },
                    "notebook_content": {
                        "type": "string",
                        "description": "Python notebook content to execute"
                    },
                    "job_name": {
                        "type": "string",
                        "description": "Name for the Databricks job"
                    }
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
                    "run_id": {
                        "type": "integer",
                        "description": "Databricks job run ID"
                    }
                },
                "required": ["run_id"]
            }
        ),
        Tool(
            name="sync_to_workspace",
            description="Sync local files to Databricks workspace. Useful for deploying notebooks and scripts.",
            inputSchema={
                "type": "object",
                "properties": {
                    "local_dir": {
                        "type": "string",
                        "description": "Local directory path"
                    },
                    "workspace_dir": {
                        "type": "string",
                        "description": "Databricks workspace directory path"
                    },
                    "pattern": {
                        "type": "string",
                        "description": "File pattern to sync (e.g., '**/*.py')",
                        "default": "**/*.py"
                    },
                    "dry_run": {
                        "type": "boolean",
                        "description": "Preview what would be synced without making changes",
                        "default": False
                    }
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
                    "local_dir": {
                        "type": "string",
                        "description": "Local directory path"
                    },
                    "workspace_dir": {
                        "type": "string",
                        "description": "Databricks workspace directory path"
                    },
                    "dry_run": {
                        "type": "boolean",
                        "description": "Preview what would be synced without making changes",
                        "default": False
                    }
                },
                "required": ["local_dir", "workspace_dir"]
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""
    try:
        if name == "execute_sql":
            query = arguments["query"]
            limit = arguments.get("limit", 100)
            
            # Add LIMIT if SELECT without LIMIT
            query_upper = query.strip().upper()
            if query_upper.startswith("SELECT") and "LIMIT" not in query_upper:
                query = f"{query.rstrip(';')} LIMIT {limit}"
            
            results = _api.run_sql(query)
            
            if results is None:
                return [TextContent(type="text", text="Query execution failed. Check the query syntax.")]
            
            if len(results) == 0:
                return [TextContent(type="text", text="Query returned 0 rows.")]
            
            # Format results
            output_lines = [f"Query returned {len(results)} rows:\n"]
            
            if hasattr(results[0], '_fields'):
                headers = results[0]._fields
                output_lines.append(" | ".join(str(h) for h in headers))
                output_lines.append("-" * 80)
            
            for row in results[:limit]:
                if hasattr(row, '_fields'):
                    output_lines.append(" | ".join(str(v) for v in row))
                else:
                    output_lines.append(str(row))
            
            return [TextContent(type="text", text="\n".join(output_lines))]
        
        elif name == "run_sql_file":
            file_path = arguments["file_path"]
            output_format = arguments.get("output_format", "show")
            limit = arguments.get("limit", 100)
            
            with open(file_path, 'r') as f:
                query = f.read()
            
            query_upper = query.strip().upper()
            if query_upper.startswith("SELECT") and "LIMIT" not in query_upper:
                query = f"{query.rstrip(';')} LIMIT {limit}"
            
            results = _api.run_sql(query)
            
            if results is None:
                return [TextContent(type="text", text="SQL file execution failed.")]
            
            if output_format == 'json':
                data = [dict(r._asdict()) if hasattr(r, '_asdict') else str(r) for r in results]
                return [TextContent(type="text", text=json.dumps(data, indent=2, default=str))]
            else:
                output_lines = [f"Query returned {len(results)} rows:\n"]
                if results and hasattr(results[0], '_fields'):
                    output_lines.append(" | ".join(results[0]._fields))
                    output_lines.append("-" * 80)
                for row in results:
                    if hasattr(row, '_fields'):
                        output_lines.append(" | ".join(str(v) for v in row))
                    else:
                        output_lines.append(str(row))
                return [TextContent(type="text", text="\n".join(output_lines))]
        
        elif name == "create_notebook":
            notebook_path = arguments["notebook_path"]
            content = arguments["content"]
            overwrite = arguments.get("overwrite", True)
            
            success = _api.create_notebook(notebook_path, content, overwrite)
            
            if success:
                return [TextContent(type="text", text=f"✅ Notebook created at {notebook_path}")]
            else:
                return [TextContent(type="text", text=f"❌ Failed to create notebook at {notebook_path}")]
        
        elif name == "run_notebook":
            result = _api.run_notebook_job(
                notebook_path=arguments["notebook_path"],
                notebook_content=arguments["notebook_content"],
                job_name=arguments["job_name"]
            )
            
            if result:
                return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]
            else:
                return [TextContent(type="text", text="Failed to run notebook job")]
        
        elif name == "get_job_status":
            status = _api.get_job_status(arguments["run_id"])
            
            if status:
                return [TextContent(type="text", text=json.dumps(status, indent=2, default=str))]
            else:
                return [TextContent(type="text", text=f"Could not get status for run {arguments['run_id']}")]
        
        elif name == "sync_to_workspace":
            result = _api.sync_to_workspace(
                arguments["local_dir"],
                arguments["workspace_dir"],
                arguments.get("pattern", "**/*.py"),
                arguments.get("dry_run", False)
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]
        
        elif name == "sync_from_workspace":
            result = _api.sync_from_workspace(
                arguments["local_dir"],
                arguments["workspace_dir"],
                arguments.get("dry_run", False)
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]
        
        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]
    
    except Exception as e:
        import traceback
        return [TextContent(type="text", text=f"Error executing {name}: {str(e)}\n{traceback.format_exc()}")]


async def main():
    _pool.initialize()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
