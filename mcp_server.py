#!/usr/bin/env python3
"""
Databricks MCP Server (Optimized)

A Model Context Protocol server that exposes Databricks functionality to AI assistants.
This wraps the existing cursor_databricks toolkit with connection pooling for speed.

Optimizations:
- Persistent SQL connection (reused across queries)
- Eager initialization on startup
- Connection health checks with auto-reconnect

Usage:
    python mcp_server.py

Configure in ~/.cursor/mcp.json to use with Cursor.
"""

import sys
import os
import json
import asyncio
import atexit
from typing import Any, Optional
from contextlib import contextmanager

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
except ImportError:
    print("MCP SDK not installed. Install with: pip install mcp", file=sys.stderr)
    sys.exit(1)

# Import config
from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN, DATABRICKS_HOST, CLUSTER_ID

# Initialize MCP server
server = Server("databricks-mcp")


class ConnectionPool:
    """
    Persistent connection pool for Databricks SQL.
    Maintains a single connection that's reused across queries.
    """
    
    def __init__(self):
        self._connection = None
        self._cursor = None
        self._initialized = False
    
    def _create_connection(self):
        """Create a new Databricks SQL connection"""
        from databricks import sql
        return sql.connect(
            server_hostname=SERVER_HOSTNAME,
            http_path=HTTP_PATH,
            access_token=TOKEN,
            timeout_seconds=300  # 5 minute timeout for long queries
        )
    
    def initialize(self):
        """Initialize the connection pool (call once at startup)"""
        if not self._initialized:
            try:
                self._connection = self._create_connection()
                self._initialized = True
                print("Databricks connection initialized", file=sys.stderr)
            except Exception as e:
                print(f"Failed to initialize connection: {e}", file=sys.stderr)
    
    def get_connection(self):
        """Get a connection, creating one if needed"""
        if self._connection is None:
            self._connection = self._create_connection()
            self._initialized = True
        return self._connection
    
    def execute_query(self, query: str) -> list:
        """Execute a query using the pooled connection"""
        try:
            conn = self.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except Exception as e:
            # Connection might be stale, try to reconnect once
            print(f"Query failed, attempting reconnect: {e}", file=sys.stderr)
            self._connection = None
            conn = self.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
    
    def close(self):
        """Close the connection"""
        if self._connection:
            try:
                self._connection.close()
            except:
                pass
            self._connection = None
            self._initialized = False


# Global connection pool - initialized once, reused forever
_pool = ConnectionPool()

# Register cleanup on exit
atexit.register(_pool.close)


class OptimizedDatabricksAPI:
    """
    Optimized Databricks API using connection pooling.
    Much faster than creating new connections for each query.
    """
    
    def __init__(self):
        # Import heavy modules once
        self._job_runner = None
    
    @property
    def job_runner(self):
        """Lazy load job runner"""
        if self._job_runner is None:
            from core import DatabricksJobRunner
            self._job_runner = DatabricksJobRunner(
                host=DATABRICKS_HOST,
                token=TOKEN,
                cluster_id=CLUSTER_ID
            )
        return self._job_runner
    
    def run_sql(self, query: str, display: bool = False) -> Optional[list]:
        """Execute SQL using the connection pool (fast!)"""
        try:
            return _pool.execute_query(query)
        except Exception as e:
            print(f"Error executing query: {e}", file=sys.stderr)
            return None
    
    def run_sql_file(self, file_path: str, output_format: str = 'show', limit: int = 100) -> int:
        """Execute SQL from a file"""
        try:
            with open(file_path, 'r') as f:
                query = f.read()
            
            # Add limit if SELECT and no limit
            query_upper = query.strip().upper()
            if query_upper.startswith("SELECT") and "LIMIT" not in query_upper:
                query = f"{query.rstrip(';')} LIMIT {limit}"
            
            results = self.run_sql(query)
            
            if results is None:
                return 1
            
            if output_format == 'json':
                print(json.dumps([dict(r._asdict()) if hasattr(r, '_asdict') else str(r) for r in results], indent=2, default=str))
            elif output_format == 'csv':
                if results and hasattr(results[0], '_fields'):
                    print(','.join(results[0]._fields))
                for row in results:
                    if hasattr(row, '_fields'):
                        print(','.join(str(v) for v in row))
                    else:
                        print(str(row))
            else:
                for row in results:
                    print(row)
            
            return 0
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
    
    def create_notebook(self, notebook_path: str, content: str, overwrite: bool = True) -> bool:
        """Create a notebook in workspace"""
        return self.job_runner.create_notebook(notebook_path, content, overwrite)
    
    def run_notebook_job(self, notebook_path: str, notebook_content: str, 
                        job_name: str, **kwargs) -> Optional[dict]:
        """Create and run a notebook job"""
        return self.job_runner.create_and_run(
            notebook_path=notebook_path,
            notebook_content=notebook_content,
            job_name=job_name,
            **kwargs
        )
    
    def get_job_status(self, run_id: int) -> Optional[dict]:
        """Get job status"""
        return self.job_runner.get_run_status(str(run_id))
    
    def sync_to_workspace(self, local_dir: str, workspace_dir: str,
                         pattern: str = "**/*.py", dry_run: bool = False) -> dict:
        """Sync local files to workspace"""
        from core.workspace_sync import WorkspaceSync
        sync = WorkspaceSync(local_dir, workspace_dir)
        return sync.sync_to_workspace(pattern=pattern, dry_run=dry_run)
    
    def sync_from_workspace(self, local_dir: str, workspace_dir: str,
                           dry_run: bool = False) -> dict:
        """Sync workspace files to local"""
        from core.workspace_sync import WorkspaceSync
        sync = WorkspaceSync(local_dir, workspace_dir)
        return sync.sync_from_workspace(dry_run=dry_run)
    
    def find_duplicates(self, table_name: str, key_column: str, limit: int = 20) -> Optional[list]:
        """Find duplicate rows"""
        query = f"""
            SELECT {key_column}, COUNT(*) as cnt
            FROM {table_name}
            GROUP BY {key_column}
            HAVING COUNT(*) > 1
            ORDER BY cnt DESC
            LIMIT {limit}
        """
        return self.run_sql(query)
    
    def describe_table(self, table_name: str) -> Optional[list]:
        """Get table schema with column names, types, and comments"""
        return self.run_sql(f"DESCRIBE {table_name}")
    
    def sample_table(self, table_name: str, limit: int = 10, where_clause: str = None) -> Optional[list]:
        """Get sample rows from a table with optional filter"""
        query = f"SELECT * FROM {table_name}"
        if where_clause:
            query += f" WHERE {where_clause}"
        query += f" LIMIT {limit}"
        return self.run_sql(query)
    
    def profile_column(self, table_name: str, column_name: str) -> dict:
        """Get statistics for a specific column"""
        # Get basic stats
        stats_query = f"""
            SELECT 
                COUNT(*) as total_rows,
                COUNT({column_name}) as non_null_count,
                COUNT(*) - COUNT({column_name}) as null_count,
                COUNT(DISTINCT {column_name}) as distinct_count
            FROM {table_name}
        """
        stats = self.run_sql(stats_query)
        
        # Get value distribution (top 10)
        dist_query = f"""
            SELECT {column_name}, COUNT(*) as cnt
            FROM {table_name}
            GROUP BY {column_name}
            ORDER BY cnt DESC
            LIMIT 10
        """
        distribution = self.run_sql(dist_query)
        
        return {
            'stats': stats[0] if stats else None,
            'top_values': distribution
        }
    
    def create_table_as_select(self, new_table_name: str, select_query: str, 
                               replace: bool = False) -> bool:
        """Create a new table from a SELECT query (for dashboard data sources)"""
        try:
            if replace:
                self.run_sql(f"DROP TABLE IF EXISTS {new_table_name}")
            
            create_query = f"CREATE TABLE {new_table_name} AS {select_query}"
            self.run_sql(create_query)
            return True
        except Exception as e:
            print(f"Error creating table: {e}", file=sys.stderr)
            return False
    
    def generate_exploratory_notebook(self, table_name: str, analysis_goal: str = None) -> str:
        """Generate a Databricks notebook for exploratory data analysis"""
        notebook = f'''# Databricks notebook source
# MAGIC %md
# MAGIC # Exploratory Data Analysis: {table_name}
# MAGIC 
# MAGIC **Generated:** {{datetime.now().strftime('%Y-%m-%d %H:%M')}}
# MAGIC 
# MAGIC **Goal:** {analysis_goal or 'Explore and understand the data'}

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Data Overview

# COMMAND ----------

# Load the data
df = spark.table("{table_name}")
print(f"Total rows: {{df.count():,}}")
print(f"Total columns: {{len(df.columns)}}")

# COMMAND ----------

# Schema
df.printSchema()

# COMMAND ----------

# Sample data
display(df.limit(20))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Column Statistics

# COMMAND ----------

# Summary statistics for numeric columns
display(df.describe())

# COMMAND ----------

# Null counts per column
from pyspark.sql.functions import col, sum as spark_sum, when, count

null_counts = df.select([
    spark_sum(when(col(c).isNull(), 1).otherwise(0)).alias(c) 
    for c in df.columns
])
display(null_counts)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Value Distributions

# COMMAND ----------

# Get categorical columns (string type)
string_cols = [f.name for f in df.schema.fields if str(f.dataType) == 'StringType()']

for col_name in string_cols[:5]:  # First 5 string columns
    print(f"\\n=== {{col_name}} ===")
    display(df.groupBy(col_name).count().orderBy("count", ascending=False).limit(10))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Date/Time Analysis (if applicable)

# COMMAND ----------

# Find date columns
date_cols = [f.name for f in df.schema.fields if 'Date' in str(f.dataType) or 'Timestamp' in str(f.dataType)]

for col_name in date_cols[:3]:
    print(f"\\n=== {{col_name}} range ===")
    display(df.select(
        min(col_name).alias("min_date"),
        max(col_name).alias("max_date")
    ))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Key Insights
# MAGIC 
# MAGIC _Add your observations here after running the analysis_

# COMMAND ----------

# Custom analysis - add your queries here
# Example: 
# display(df.filter(col("status") == "active").groupBy("country").count())
'''
        return notebook
    
    def generate_pipeline_notebook(self, source_tables: list, target_table: str, 
                                   transformation_description: str = None) -> str:
        """Generate a Databricks notebook for data pipeline/ETL"""
        sources_list = ", ".join(source_tables)
        notebook = f'''# Databricks notebook source
# MAGIC %md
# MAGIC # Data Pipeline: {target_table}
# MAGIC 
# MAGIC **Source Tables:** {sources_list}
# MAGIC **Target Table:** {target_table}
# MAGIC 
# MAGIC **Description:** {transformation_description or 'Data transformation pipeline'}
# MAGIC 
# MAGIC **Generated:** {{datetime.now().strftime('%Y-%m-%d %H:%M')}}

# COMMAND ----------

# MAGIC %md
# MAGIC ## Configuration

# COMMAND ----------

# Pipeline configuration
TARGET_TABLE = "{target_table}"
WRITE_MODE = "overwrite"  # or "append"

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Load Source Data

# COMMAND ----------

'''
        # Add source table loading
        for i, table in enumerate(source_tables):
            table_alias = table.split('.')[-1]
            notebook += f'''# Load {table}
df_{table_alias} = spark.table("{table}")
print(f"{table}: {{df_{table_alias}.count():,}} rows")

# COMMAND ----------

'''
        
        notebook += f'''# MAGIC %md
# MAGIC ## 2. Data Transformations

# COMMAND ----------

from pyspark.sql.functions import *

# TODO: Add your transformations here
# Example joins, filters, aggregations

# Starting with first source table
df_result = df_{source_tables[0].split('.')[-1]}

# Example transformation:
# df_result = df_result.filter(col("status") == "active")
# df_result = df_result.withColumn("processed_date", current_date())

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Data Quality Checks

# COMMAND ----------

# Row count check
print(f"Output rows: {{df_result.count():,}}")

# Null check on key columns
# df_result.select([count(when(col(c).isNull(), c)).alias(c) for c in df_result.columns]).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Write Output

# COMMAND ----------

# Write to target table
df_result.write.mode(WRITE_MODE).saveAsTable(TARGET_TABLE)
print(f"✅ Data written to {{TARGET_TABLE}}")

# COMMAND ----------

# Verify output
spark.table(TARGET_TABLE).limit(5).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Pipeline Summary

# COMMAND ----------

# Final stats
final_count = spark.table(TARGET_TABLE).count()
print(f"Pipeline completed successfully!")
print(f"Target table: {{TARGET_TABLE}}")
print(f"Total rows: {{final_count:,}}")

dbutils.notebook.exit(f"SUCCESS: {{final_count}} rows")
'''
        return notebook


# Global optimized API instance
_api = OptimizedDatabricksAPI()


@server.list_tools()
async def list_tools():
    """List available Databricks tools"""
    return [
        Tool(
            name="execute_sql",
            description="Execute a SQL query on Databricks and return results. Use for SELECT queries, data exploration, and analysis.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "SQL query to execute"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of rows to return (default: 100)",
                        "default": 100
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="run_sql_file",
            description="Execute SQL from a local file on Databricks",
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
                        "description": "Maximum number of rows",
                        "default": 100
                    }
                },
                "required": ["file_path"]
            }
        ),
        Tool(
            name="list_tables",
            description="List tables in a Databricks schema/database",
            inputSchema={
                "type": "object",
                "properties": {
                    "schema_name": {
                        "type": "string",
                        "description": "Schema/database name to list tables from"
                    },
                    "catalog": {
                        "type": "string",
                        "description": "Catalog name (optional, defaults to current catalog)"
                    }
                },
                "required": ["schema_name"]
            }
        ),
        Tool(
            name="create_notebook",
            description="Create a Python notebook in Databricks workspace",
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
            description="Create and run a notebook as a Databricks job. Returns job output when complete.",
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
            description="Get the status of a Databricks job run",
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
            description="Sync local files to Databricks workspace",
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
                        "description": "If true, only show what would be synced",
                        "default": False
                    }
                },
                "required": ["local_dir", "workspace_dir"]
            }
        ),
        Tool(
            name="sync_from_workspace",
            description="Sync files from Databricks workspace to local directory",
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
                        "description": "If true, only show what would be synced",
                        "default": False
                    }
                },
                "required": ["local_dir", "workspace_dir"]
            }
        ),
        Tool(
            name="find_duplicates",
            description="Find duplicate rows in a table based on a key column",
            inputSchema={
                "type": "object",
                "properties": {
                    "table_name": {
                        "type": "string",
                        "description": "Table name in format 'schema.table'"
                    },
                    "key_column": {
                        "type": "string",
                        "description": "Column to check for duplicates"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of duplicate rows to return",
                        "default": 20
                    }
                },
                "required": ["table_name", "key_column"]
            }
        ),
        Tool(
            name="describe_table",
            description="Get table schema with column names, data types, and comments. Use this to understand table structure before querying.",
            inputSchema={
                "type": "object",
                "properties": {
                    "table_name": {
                        "type": "string",
                        "description": "Full table name (e.g., 'hive_metastore.payments_hf.f_orders')"
                    }
                },
                "required": ["table_name"]
            }
        ),
        Tool(
            name="sample_table",
            description="Get sample rows from a table. Quick way to see what data looks like.",
            inputSchema={
                "type": "object",
                "properties": {
                    "table_name": {
                        "type": "string",
                        "description": "Full table name"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Number of rows to return",
                        "default": 10
                    },
                    "where_clause": {
                        "type": "string",
                        "description": "Optional WHERE clause filter (without 'WHERE' keyword)"
                    }
                },
                "required": ["table_name"]
            }
        ),
        Tool(
            name="profile_column",
            description="Get statistics and value distribution for a specific column. Useful for data exploration.",
            inputSchema={
                "type": "object",
                "properties": {
                    "table_name": {
                        "type": "string",
                        "description": "Full table name"
                    },
                    "column_name": {
                        "type": "string",
                        "description": "Column to profile"
                    }
                },
                "required": ["table_name", "column_name"]
            }
        ),
        Tool(
            name="create_dashboard_table",
            description="Create a new table from a SELECT query. Use for creating dashboard data sources or materialized views.",
            inputSchema={
                "type": "object",
                "properties": {
                    "new_table_name": {
                        "type": "string",
                        "description": "Name for the new table (e.g., 'hive_metastore.payments_hf.my_dashboard_data')"
                    },
                    "select_query": {
                        "type": "string",
                        "description": "SELECT query that defines the table data"
                    },
                    "replace_if_exists": {
                        "type": "boolean",
                        "description": "If true, drop and recreate the table if it exists",
                        "default": False
                    }
                },
                "required": ["new_table_name", "select_query"]
            }
        ),
        Tool(
            name="create_exploratory_notebook",
            description="Generate a Databricks notebook template for exploratory data analysis on a table. Creates a complete EDA workflow.",
            inputSchema={
                "type": "object",
                "properties": {
                    "table_name": {
                        "type": "string",
                        "description": "Table to analyze"
                    },
                    "notebook_path": {
                        "type": "string",
                        "description": "Path in Databricks workspace to save the notebook"
                    },
                    "analysis_goal": {
                        "type": "string",
                        "description": "Description of what you want to learn from the data"
                    }
                },
                "required": ["table_name", "notebook_path"]
            }
        ),
        Tool(
            name="create_pipeline_notebook",
            description="Generate a Databricks notebook template for data pipeline/ETL. Creates a structured pipeline with source loading, transformations, quality checks, and output.",
            inputSchema={
                "type": "object",
                "properties": {
                    "source_tables": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of source table names"
                    },
                    "target_table": {
                        "type": "string",
                        "description": "Name of the output table"
                    },
                    "notebook_path": {
                        "type": "string",
                        "description": "Path in Databricks workspace to save the notebook"
                    },
                    "description": {
                        "type": "string",
                        "description": "Description of what the pipeline does"
                    }
                },
                "required": ["source_tables", "target_table", "notebook_path"]
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls"""
    try:
        if name == "execute_sql":
            query = arguments["query"]
            limit = arguments.get("limit", 100)
            
            # Add LIMIT if not present and it's a SELECT query
            query_upper = query.strip().upper()
            if query_upper.startswith("SELECT") and "LIMIT" not in query_upper:
                query = f"{query.rstrip(';')} LIMIT {limit}"
            
            results = _api.run_sql(query)
            
            if results is None:
                return [TextContent(type="text", text="Query execution failed. Check the query syntax.")]
            
            if len(results) == 0:
                return [TextContent(type="text", text="Query returned 0 rows.")]
            
            # Format results as a table
            output_lines = []
            output_lines.append(f"Query returned {len(results)} rows:\n")
            
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
            
            # Read and execute the file
            with open(file_path, 'r') as f:
                query = f.read()
            
            query_upper = query.strip().upper()
            if query_upper.startswith("SELECT") and "LIMIT" not in query_upper:
                query = f"{query.rstrip(';')} LIMIT {limit}"
            
            results = _api.run_sql(query)
            
            if results is None:
                return [TextContent(type="text", text="SQL file execution failed.")]
            
            # Format based on output_format
            if output_format == 'json':
                data = []
                for r in results:
                    if hasattr(r, '_asdict'):
                        data.append(dict(r._asdict()))
                    else:
                        data.append(str(r))
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
        
        elif name == "list_tables":
            schema_name = arguments["schema_name"]
            catalog = arguments.get("catalog", "")
            
            if catalog:
                query = f"SHOW TABLES IN {catalog}.{schema_name}"
            else:
                query = f"SHOW TABLES IN {schema_name}"
            
            results = _api.run_sql(query)
            
            if results:
                tables = [str(row) for row in results]
                return [TextContent(type="text", text=f"Tables in {schema_name}:\n" + "\n".join(tables))]
            else:
                return [TextContent(type="text", text=f"No tables found in {schema_name}")]
        
        elif name == "create_notebook":
            notebook_path = arguments["notebook_path"]
            content = arguments["content"]
            overwrite = arguments.get("overwrite", True)
            
            success = _api.create_notebook(notebook_path, content, overwrite)
            
            if success:
                return [TextContent(type="text", text=f"Notebook created successfully at {notebook_path}")]
            else:
                return [TextContent(type="text", text=f"Failed to create notebook at {notebook_path}")]
        
        elif name == "run_notebook":
            notebook_path = arguments["notebook_path"]
            notebook_content = arguments["notebook_content"]
            job_name = arguments["job_name"]
            
            result = _api.run_notebook_job(
                notebook_path=notebook_path,
                notebook_content=notebook_content,
                job_name=job_name
            )
            
            if result:
                return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]
            else:
                return [TextContent(type="text", text="Failed to run notebook job")]
        
        elif name == "get_job_status":
            run_id = arguments["run_id"]
            
            status = _api.get_job_status(run_id)
            
            if status:
                return [TextContent(type="text", text=json.dumps(status, indent=2, default=str))]
            else:
                return [TextContent(type="text", text=f"Could not get status for run {run_id}")]
        
        elif name == "sync_to_workspace":
            local_dir = arguments["local_dir"]
            workspace_dir = arguments["workspace_dir"]
            pattern = arguments.get("pattern", "**/*.py")
            dry_run = arguments.get("dry_run", False)
            
            result = _api.sync_to_workspace(local_dir, workspace_dir, pattern, dry_run)
            return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]
        
        elif name == "sync_from_workspace":
            local_dir = arguments["local_dir"]
            workspace_dir = arguments["workspace_dir"]
            dry_run = arguments.get("dry_run", False)
            
            result = _api.sync_from_workspace(local_dir, workspace_dir, dry_run)
            return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]
        
        elif name == "find_duplicates":
            table_name = arguments["table_name"]
            key_column = arguments["key_column"]
            limit = arguments.get("limit", 20)
            
            results = _api.find_duplicates(table_name, key_column, limit)
            
            if results:
                output_lines = [f"Duplicates found ({len(results)} groups):\n"]
                if hasattr(results[0], '_fields'):
                    output_lines.append(" | ".join(str(h) for h in results[0]._fields))
                    output_lines.append("-" * 40)
                for row in results:
                    if hasattr(row, '_fields'):
                        output_lines.append(" | ".join(str(v) for v in row))
                    else:
                        output_lines.append(str(row))
                return [TextContent(type="text", text="\n".join(output_lines))]
            else:
                return [TextContent(type="text", text=f"No duplicates found for {key_column} in {table_name}")]
        
        elif name == "describe_table":
            table_name = arguments["table_name"]
            results = _api.describe_table(table_name)
            
            if results:
                output = f"Schema for {table_name}:\n\n"
                output += f"{'Column':<40} {'Type':<30} {'Comment'}\n"
                output += "-" * 100 + "\n"
                for row in results:
                    col_name = str(row[0]) if row[0] else ""
                    col_type = str(row[1]) if len(row) > 1 and row[1] else ""
                    comment = str(row[2]) if len(row) > 2 and row[2] else ""
                    output += f"{col_name:<40} {col_type:<30} {comment}\n"
                return [TextContent(type="text", text=output)]
            else:
                return [TextContent(type="text", text=f"Could not describe table {table_name}")]
        
        elif name == "sample_table":
            table_name = arguments["table_name"]
            limit = arguments.get("limit", 10)
            where_clause = arguments.get("where_clause")
            
            results = _api.sample_table(table_name, limit, where_clause)
            
            if results:
                output_lines = [f"Sample from {table_name} ({len(results)} rows):\n"]
                if hasattr(results[0], '_fields'):
                    output_lines.append(" | ".join(str(h) for h in results[0]._fields))
                    output_lines.append("-" * 100)
                for row in results:
                    if hasattr(row, '_fields'):
                        output_lines.append(" | ".join(str(v)[:50] for v in row))
                    else:
                        output_lines.append(str(row))
                return [TextContent(type="text", text="\n".join(output_lines))]
            else:
                return [TextContent(type="text", text=f"No data found in {table_name}")]
        
        elif name == "profile_column":
            table_name = arguments["table_name"]
            column_name = arguments["column_name"]
            
            profile = _api.profile_column(table_name, column_name)
            
            output = f"Profile for {table_name}.{column_name}:\n\n"
            
            if profile['stats']:
                stats = profile['stats']
                output += "=== Statistics ===\n"
                output += f"Total Rows:     {stats[0]:,}\n"
                output += f"Non-Null:       {stats[1]:,}\n"
                output += f"Null Count:     {stats[2]:,}\n"
                output += f"Distinct Count: {stats[3]:,}\n"
                if stats[0] > 0:
                    output += f"Null %:         {(stats[2]/stats[0])*100:.2f}%\n"
                    output += f"Cardinality:    {(stats[3]/stats[0])*100:.2f}%\n"
            
            if profile['top_values']:
                output += "\n=== Top 10 Values ===\n"
                for row in profile['top_values']:
                    output += f"{str(row[0])[:50]:<50} {row[1]:>10,}\n"
            
            return [TextContent(type="text", text=output)]
        
        elif name == "create_dashboard_table":
            new_table_name = arguments["new_table_name"]
            select_query = arguments["select_query"]
            replace = arguments.get("replace_if_exists", False)
            
            success = _api.create_table_as_select(new_table_name, select_query, replace)
            
            if success:
                # Get row count
                count_result = _api.run_sql(f"SELECT COUNT(*) FROM {new_table_name}")
                row_count = count_result[0][0] if count_result else "unknown"
                return [TextContent(type="text", text=f"✅ Table {new_table_name} created successfully!\nRows: {row_count:,}")]
            else:
                return [TextContent(type="text", text=f"❌ Failed to create table {new_table_name}")]
        
        elif name == "create_exploratory_notebook":
            table_name = arguments["table_name"]
            notebook_path = arguments["notebook_path"]
            analysis_goal = arguments.get("analysis_goal")
            
            # Generate notebook content
            content = _api.generate_exploratory_notebook(table_name, analysis_goal)
            
            # Create the notebook
            success = _api.create_notebook(notebook_path, content)
            
            if success:
                return [TextContent(type="text", text=f"✅ Exploratory notebook created at {notebook_path}\n\nThe notebook includes:\n- Data overview (row count, columns)\n- Schema inspection\n- Sample data preview\n- Column statistics\n- Null analysis\n- Value distributions\n- Date range analysis\n\nOpen it in Databricks to run the analysis!")]
            else:
                return [TextContent(type="text", text=f"❌ Failed to create notebook at {notebook_path}")]
        
        elif name == "create_pipeline_notebook":
            source_tables = arguments["source_tables"]
            target_table = arguments["target_table"]
            notebook_path = arguments["notebook_path"]
            description = arguments.get("description")
            
            # Generate notebook content
            content = _api.generate_pipeline_notebook(source_tables, target_table, description)
            
            # Create the notebook
            success = _api.create_notebook(notebook_path, content)
            
            if success:
                sources_str = ", ".join(source_tables)
                return [TextContent(type="text", text=f"✅ Pipeline notebook created at {notebook_path}\n\nPipeline:\n- Sources: {sources_str}\n- Target: {target_table}\n\nThe notebook includes:\n- Source data loading\n- Transformation template\n- Data quality checks\n- Output writing\n- Pipeline summary\n\nOpen it in Databricks to customize and run!")]
            else:
                return [TextContent(type="text", text=f"❌ Failed to create notebook at {notebook_path}")]
        
        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]
    
    except Exception as e:
        import traceback
        return [TextContent(type="text", text=f"Error executing {name}: {str(e)}\n{traceback.format_exc()}")]


async def main():
    """Run the MCP server"""
    # Initialize connection pool eagerly on startup
    _pool.initialize()
    
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
