#!/usr/bin/env python3
"""
Databricks Python API

A clean Python API for easy integration with Cursor IDE.
This provides a simple interface for all Databricks operations.

Usage in Cursor:
    from databricks_api import DatabricksAPI
    
    db = DatabricksAPI()
    
    # Run SQL query
    results = db.run_sql("SELECT * FROM table LIMIT 10")
    
    # Inspect table
    schema = db.inspect_table("schema.table")
    
    # Create and run notebook
    job = db.create_notebook_job("/Workspace/path", notebook_content, "my_job")
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core import (
    DatabricksJobRunner,
    TableInspector,
    run_query as run_query_with_display,
    run_sql_file,
    print_table
)
from typing import List, Dict, Optional, Any


class DatabricksAPI:
    """
    Unified API for Databricks operations.
    
    This class provides a simple interface for all Databricks operations,
    making it easy to use from Cursor IDE or any Python script.
    """
    
    def __init__(self, server_hostname: Optional[str] = None, 
                 http_path: Optional[str] = None, 
                 token: Optional[str] = None,
                 databricks_host: Optional[str] = None,
                 cluster_id: Optional[str] = None):
        """
        Initialize the Databricks API.
        
        If parameters are not provided, they will be loaded from config.py
        """
        self.job_runner = DatabricksJobRunner(
            host=databricks_host,
            token=token,
            cluster_id=cluster_id
        )
        self.table_inspector = TableInspector(
            server_hostname=server_hostname,
            http_path=http_path,
            token=token
        )
    
    def run_sql(self, query: str, limit: Optional[int] = None, 
                display: bool = True) -> Optional[List[Any]]:
        """
        Execute a SQL query.
        
        Args:
            query: SQL query string
            limit: Maximum number of rows to return
            display: Whether to display results (default: True)
        
        Returns:
            List of result rows, or None on error
        """
        if display:
            return run_query_with_display(query, limit=limit)
        else:
            # Silent execution - just return results
            from databricks import sql
            from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN
            
            try:
                with sql.connect(
                    server_hostname=SERVER_HOSTNAME,
                    http_path=HTTP_PATH,
                    access_token=TOKEN,
                    timeout_seconds=30
                ) as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(query)
                        return cursor.fetchall()
            except Exception as e:
                print(f"Error executing query: {e}")
                return None
    
    def run_sql_file(self, file_path: str, output_format: str = 'show', 
                     limit: int = 100) -> int:
        """
        Execute SQL from a file.
        
        Args:
            file_path: Path to SQL file
            output_format: Output format ('show', 'csv', 'json')
            limit: Maximum number of rows
        
        Returns:
            0 on success, 1 on error
        """
        return run_sql_file(file_path, output_format, limit)
    
    def inspect_table(self, table_name: str, 
                     include_schema: bool = True,
                     include_stats: bool = True,
                     sample_rows: Optional[int] = None) -> Dict[str, Any]:
        """
        Inspect a table.
        
        Args:
            table_name: Table name in format schema.table
            include_schema: Whether to include schema information
            include_stats: Whether to include statistics
            sample_rows: Number of sample rows to include
        
        Returns:
            Dictionary with inspection results
        """
        result = {}
        
        if include_schema:
            result['schema'] = self.table_inspector.get_table_schema(table_name)
        
        if include_stats:
            result['stats'] = self.table_inspector.get_table_stats(table_name)
        
        if sample_rows:
            result['sample'] = self.table_inspector.get_table_sample(table_name, limit=sample_rows)
        
        return result
    
    def find_duplicates(self, table_name: str, key_column: str, 
                       limit: int = 20) -> Optional[List[Any]]:
        """
        Find duplicate rows in a table.
        
        Args:
            table_name: Table name in format schema.table
            key_column: Column to check for duplicates
            limit: Maximum number of duplicate rows to return
        
        Returns:
            List of duplicate rows, or None on error
        """
        return self.table_inspector.find_duplicates(table_name, key_column, limit)
    
    def create_notebook(self, notebook_path: str, content: str, 
                       overwrite: bool = True) -> bool:
        """
        Create a notebook in Databricks workspace.
        
        Args:
            notebook_path: Path in Databricks workspace
            content: Notebook content
            overwrite: Whether to overwrite if exists
        
        Returns:
            True on success, False on error
        """
        return self.job_runner.create_notebook(notebook_path, content, overwrite)
    
    def run_notebook_job(self, notebook_path: str, notebook_content: str, 
                        job_name: str) -> Optional[Dict[str, Any]]:
        """
        Create and run a notebook as a Databricks job.
        
        Args:
            notebook_path: Path in Databricks workspace
            notebook_content: Notebook content
            job_name: Name for the job
        
        Returns:
            Dictionary with job_id and run_id, or None on error
        """
        return self.job_runner.create_and_run(
            notebook_path=notebook_path,
            notebook_content=notebook_content,
            job_name=job_name
        )
    
    def get_job_status(self, run_id: int) -> Optional[Dict[str, Any]]:
        """
        Get the status of a job run.
        
        Args:
            run_id: Databricks run ID
        
        Returns:
            Dictionary with job status, or None on error
        """
        return self.job_runner.get_run_status(str(run_id))
    
    def get_job_output(self, run_id: int) -> Optional[str]:
        """
        Get the output of a completed job run.
        
        Args:
            run_id: Databricks run ID
        
        Returns:
            Job output as string, or None on error
        """
        return self.job_runner.get_job_output(run_id)


# Convenience functions for quick usage
def sql(query: str, limit: Optional[int] = None) -> Optional[List[Any]]:
    """Quick SQL execution"""
    api = DatabricksAPI()
    return api.run_sql(query, limit=limit, display=True)


def inspect(table_name: str, sample: int = 10) -> Dict[str, Any]:
    """Quick table inspection"""
    api = DatabricksAPI()
    return api.inspect_table(table_name, sample_rows=sample)


def notebook(path: str, content: str, job_name: str) -> Optional[Dict[str, Any]]:
    """Quick notebook job creation"""
    api = DatabricksAPI()
    return api.run_notebook_job(path, content, job_name)


if __name__ == "__main__":
    # Example usage
    db = DatabricksAPI()
    
    # Run a query
    results = db.run_sql("SELECT 1 as test")
    print(f"Query returned {len(results) if results else 0} rows")
    
    # Inspect a table (if you have one)
    # schema = db.inspect_table("schema.table", sample_rows=5)
    # print(schema)

