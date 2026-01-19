"""
Databricks Core Utilities Package

Pure functions for working with Databricks.
These are the essential building blocks used by MCP servers and CLI tools.

Modules:
- connection_pool: Shared SQL connection pool (singleton)
- databricks_job_runner: Create and run Databricks jobs
- table_inspector: Inspect table schemas and data
- query_util: Execute SQL queries with formatting
- workspace_sync: Sync files with Databricks workspace
- run_sql_file: Execute SQL from files
- _config: Configuration loading

For use cases (composite scripts), see the use_cases/ folder.
"""

from .connection_pool import (
    ConnectionPool,
    get_pool,
    execute_query as pool_execute_query,
    execute_query_with_columns,
)
from .databricks_job_runner import DatabricksJobRunner
from .table_inspector import TableInspector
from .query_util import print_table, run_query
from .run_sql_file import run_sql_file
from .workspace_sync import WorkspaceSync
from ._config import get_config, DatabricksConfig

__all__ = [
    # Connection Pool
    'ConnectionPool',
    'get_pool',
    'pool_execute_query',
    'execute_query_with_columns',
    # Job Runner
    'DatabricksJobRunner',
    # Table Inspector
    'TableInspector',
    # Query Utilities
    'print_table',
    'run_query',
    # SQL File Runner
    'run_sql_file',
    # Workspace Sync
    'WorkspaceSync',
    # Config
    'get_config',
    'DatabricksConfig',
]
