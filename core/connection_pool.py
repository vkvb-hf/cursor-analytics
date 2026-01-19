#!/usr/bin/env python3
"""
Databricks SQL Connection Pool

Provides a persistent, reusable connection pool for Databricks SQL queries.
Used by both MCP servers and CLI tools to avoid connection overhead.

Usage:
    from core.connection_pool import get_pool, execute_query
    
    # Simple query execution
    results = execute_query("SELECT * FROM table LIMIT 10")
    
    # Or use the pool directly
    pool = get_pool()
    results = pool.execute("SELECT COUNT(*) FROM table")
"""

import atexit
import sys
from typing import List, Any, Optional, Dict

from core._config import get_config


class ConnectionPool:
    """
    Persistent connection pool for Databricks SQL.
    
    Maintains a single connection that is reused across queries.
    Automatically reconnects if the connection is lost.
    """
    
    _instance: Optional['ConnectionPool'] = None
    
    def __init__(self):
        self._connection = None
        self._initialized = False
        self._config = get_config()
    
    @classmethod
    def get_instance(cls) -> 'ConnectionPool':
        """Get singleton instance of connection pool."""
        if cls._instance is None:
            cls._instance = ConnectionPool()
        return cls._instance
    
    def _create_connection(self):
        """Create a new Databricks SQL connection."""
        from databricks import sql
        return sql.connect(
            server_hostname=self._config.SERVER_HOSTNAME,
            http_path=self._config.HTTP_PATH,
            access_token=self._config.TOKEN,
            timeout_seconds=300
        )
    
    def initialize(self) -> bool:
        """
        Initialize the connection pool.
        
        Returns:
            True if initialization successful, False otherwise
        """
        if self._initialized:
            return True
            
        if not self._config.TOKEN:
            print("⚠️  Cannot initialize connection: DATABRICKS_TOKEN not set", file=sys.stderr)
            return False
        
        try:
            self._connection = self._create_connection()
            self._initialized = True
            print("✅ Databricks SQL connection initialized", file=sys.stderr)
            return True
        except Exception as e:
            print(f"❌ Failed to initialize connection: {e}", file=sys.stderr)
            return False
    
    def get_connection(self):
        """
        Get the current connection, creating one if needed.
        
        Returns:
            Active Databricks SQL connection
        """
        if self._connection is None:
            self._connection = self._create_connection()
            self._initialized = True
        return self._connection
    
    def execute(self, query: str, fetch: bool = True) -> List[Any]:
        """
        Execute a SQL query using the pooled connection.
        
        Args:
            query: SQL query to execute
            fetch: Whether to fetch results (default True)
        
        Returns:
            List of result rows, or empty list for non-SELECT queries
        """
        try:
            conn = self.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(query)
                if fetch:
                    return cursor.fetchall()
                return []
        except Exception as e:
            # Connection might be stale, try reconnecting once
            print(f"Query failed, attempting reconnect: {e}", file=sys.stderr)
            self._connection = None
            conn = self.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(query)
                if fetch:
                    return cursor.fetchall()
                return []
    
    def execute_with_columns(self, query: str) -> tuple[List[Any], List[str]]:
        """
        Execute a SQL query and return results with column names.
        
        Args:
            query: SQL query to execute
        
        Returns:
            Tuple of (results, column_names)
        """
        try:
            conn = self.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description] if cursor.description else []
                return results, columns
        except Exception as e:
            print(f"Query failed, attempting reconnect: {e}", file=sys.stderr)
            self._connection = None
            conn = self.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description] if cursor.description else []
                return results, columns
    
    def close(self):
        """Close the connection pool."""
        if self._connection:
            try:
                self._connection.close()
            except Exception:
                pass
            self._connection = None
            self._initialized = False


# Module-level convenience functions

def get_pool() -> ConnectionPool:
    """Get the singleton connection pool instance."""
    return ConnectionPool.get_instance()


def execute_query(query: str) -> List[Any]:
    """
    Execute a SQL query using the shared connection pool.
    
    Args:
        query: SQL query to execute
    
    Returns:
        List of result rows
    """
    return get_pool().execute(query)


def execute_query_with_columns(query: str) -> tuple[List[Any], List[str]]:
    """
    Execute a SQL query and return results with column names.
    
    Args:
        query: SQL query to execute
    
    Returns:
        Tuple of (results, column_names)
    """
    return get_pool().execute_with_columns(query)


# Register cleanup on exit
def _cleanup():
    if ConnectionPool._instance:
        ConnectionPool._instance.close()

atexit.register(_cleanup)
