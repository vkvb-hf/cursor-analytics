#!/usr/bin/env python3
"""
Databricks SQL Connection Pool

Provides a persistent, reusable connection pool for Databricks SQL queries.
Used by both MCP servers and CLI tools to avoid connection overhead.

Features:
- Automatic reconnection on stale connections
- Background keep-alive to prevent idle disconnects
- Health checks before query execution
- Thread-safe connection management
- Cluster-first with SQL Warehouse failover

Failover Strategy:
- Primary: Interactive cluster (faster for heavy workloads)
- Fallback: SQL Warehouse (always available, auto-scales)
- Auto-recovery: Switches back to cluster when available

Usage:
    from core.connection_pool import get_pool, execute_query
    
    # Simple query execution
    results = execute_query("SELECT * FROM table LIMIT 10")
    
    # Or use the pool directly
    pool = get_pool()
    results = pool.execute("SELECT COUNT(*) FROM table")
    
    # Check current connection type
    print(pool.get_connection_info())
"""

import atexit
import sys
import threading
import time
import requests
from typing import List, Any, Optional, Dict

from core._config import get_config


class ConnectionPool:
    """
    Persistent connection pool for Databricks SQL.
    
    Maintains a single connection that is reused across queries.
    Automatically reconnects if the connection is lost.
    Includes background keep-alive to prevent idle disconnects.
    Supports cluster-first with SQL Warehouse failover.
    """
    
    _instance: Optional['ConnectionPool'] = None
    _lock = threading.Lock()
    
    CONNECTION_TIMEOUT = 30
    QUERY_TIMEOUT = 300
    KEEPALIVE_INTERVAL = 120  # Ping every 2 minutes to keep connection alive
    HEALTH_CHECK_QUERY = "SELECT 1"
    CLUSTER_CHECK_INTERVAL = 300  # Check if cluster is back every 5 minutes
    
    # Connection types
    CONN_TYPE_CLUSTER = "cluster"
    CONN_TYPE_WAREHOUSE = "warehouse"
    CONN_TYPE_DEFAULT = "default"
    
    def __init__(self):
        self._connection = None
        self._initialized = False
        self._config = get_config()
        self._conn_lock = threading.Lock()
        self._keepalive_thread: Optional[threading.Thread] = None
        self._keepalive_stop = threading.Event()
        self._last_activity = time.time()
        
        # Failover state
        self._current_conn_type = self.CONN_TYPE_DEFAULT
        self._current_http_path = self._config.HTTP_PATH
        self._using_fallback = False
        self._last_cluster_check = 0
        self._cluster_start_requested = False
    
    @classmethod
    def get_instance(cls) -> 'ConnectionPool':
        """Get singleton instance of connection pool."""
        with cls._lock:
            if cls._instance is None:
                cls._instance = ConnectionPool()
            return cls._instance
    
    def _get_cluster_state(self) -> Optional[str]:
        """
        Get the current state of the interactive cluster.
        
        Returns:
            Cluster state: RUNNING, PENDING, TERMINATED, etc. or None if error
        """
        if not self._config.CLUSTER_ID or not self._config.DATABRICKS_HOST:
            return None
        
        try:
            url = f"{self._config.DATABRICKS_HOST}/api/2.0/clusters/get"
            headers = {"Authorization": f"Bearer {self._config.TOKEN}"}
            response = requests.get(url, headers=headers, params={"cluster_id": self._config.CLUSTER_ID}, timeout=10)
            
            if response.status_code == 200:
                return response.json().get("state")
            return None
        except Exception:
            return None
    
    def _start_cluster(self) -> bool:
        """
        Start the interactive cluster if it's not running.
        
        Returns:
            True if start request was successful or cluster already running
        """
        if not self._config.CLUSTER_ID or not self._config.DATABRICKS_HOST:
            return False
        
        try:
            state = self._get_cluster_state()
            
            if state == "RUNNING":
                return True
            
            if state in ["PENDING", "RESTARTING", "RESIZING"]:
                print(f"⏳ Cluster is {state}, waiting...", file=sys.stderr)
                return False
            
            # Cluster is TERMINATED or TERMINATING - start it
            url = f"{self._config.DATABRICKS_HOST}/api/2.0/clusters/start"
            headers = {"Authorization": f"Bearer {self._config.TOKEN}"}
            response = requests.post(url, headers=headers, json={"cluster_id": self._config.CLUSTER_ID}, timeout=10)
            
            if response.status_code == 200:
                print(f"🚀 Started cluster {self._config.CLUSTER_ID}", file=sys.stderr)
                self._cluster_start_requested = True
                return False  # Not ready yet, but starting
            else:
                print(f"⚠️  Failed to start cluster: {response.text}", file=sys.stderr)
                return False
        except Exception as e:
            print(f"⚠️  Error starting cluster: {e}", file=sys.stderr)
            return False
    
    def _is_cluster_available(self) -> bool:
        """Check if the cluster is running and available."""
        state = self._get_cluster_state()
        return state == "RUNNING"
    
    def _create_connection(self, http_path: Optional[str] = None):
        """Create a new Databricks SQL connection with timeouts."""
        from databricks import sql
        
        path = http_path or self._current_http_path
        
        return sql.connect(
            server_hostname=self._config.SERVER_HOSTNAME,
            http_path=path,
            access_token=self._config.TOKEN,
            _socket_timeout=self.CONNECTION_TIMEOUT,
            timeout_seconds=self.QUERY_TIMEOUT,
        )
    
    def _try_connect_to_cluster(self) -> bool:
        """
        Try to connect to the interactive cluster.
        
        Returns:
            True if connection successful, False otherwise
        """
        if not self._config.CLUSTER_HTTP_PATH:
            return False
        
        try:
            # Check if cluster is running
            if not self._is_cluster_available():
                # Try to start it
                self._start_cluster()
                return False
            
            # Try to connect
            conn = self._create_connection(self._config.CLUSTER_HTTP_PATH)
            
            # Test the connection
            with conn.cursor() as cursor:
                cursor.execute(self.HEALTH_CHECK_QUERY)
                cursor.fetchall()
            
            # Success - use this connection
            self._safe_close_connection()
            self._connection = conn
            self._current_http_path = self._config.CLUSTER_HTTP_PATH
            self._current_conn_type = self.CONN_TYPE_CLUSTER
            self._using_fallback = False
            print("✅ Connected to interactive cluster", file=sys.stderr)
            return True
            
        except Exception as e:
            print(f"⚠️  Cluster connection failed: {e}", file=sys.stderr)
            return False
    
    def _try_connect_to_warehouse(self) -> bool:
        """
        Try to connect to the SQL Warehouse.
        
        Returns:
            True if connection successful, False otherwise
        """
        warehouse_path = self._config.WAREHOUSE_HTTP_PATH or self._config.HTTP_PATH
        
        if not warehouse_path:
            return False
        
        try:
            conn = self._create_connection(warehouse_path)
            
            # Test the connection
            with conn.cursor() as cursor:
                cursor.execute(self.HEALTH_CHECK_QUERY)
                cursor.fetchall()
            
            # Success - use this connection
            self._safe_close_connection()
            self._connection = conn
            self._current_http_path = warehouse_path
            self._current_conn_type = self.CONN_TYPE_WAREHOUSE
            self._using_fallback = True
            print("✅ Connected to SQL Warehouse (fallback)", file=sys.stderr)
            return True
            
        except Exception as e:
            print(f"❌ Warehouse connection failed: {e}", file=sys.stderr)
            return False
    
    def _connect_with_failover(self) -> bool:
        """
        Connect using failover strategy: cluster first, then warehouse.
        
        Returns:
            True if any connection successful, False otherwise
        """
        if not self._config.ENABLE_FAILOVER:
            # No failover - use default HTTP_PATH
            try:
                self._connection = self._create_connection()
                self._current_conn_type = self.CONN_TYPE_DEFAULT
                return True
            except Exception as e:
                print(f"❌ Connection failed: {e}", file=sys.stderr)
                return False
        
        # Failover enabled - try cluster first
        if self._try_connect_to_cluster():
            return True
        
        # Cluster not available - fall back to warehouse
        print("🔄 Falling back to SQL Warehouse...", file=sys.stderr)
        return self._try_connect_to_warehouse()
    
    def _maybe_switch_to_cluster(self):
        """
        Check if we should switch back to cluster from warehouse.
        Called periodically when using fallback.
        """
        if not self._using_fallback or not self._config.ENABLE_FAILOVER:
            return
        
        # Don't check too frequently
        now = time.time()
        if now - self._last_cluster_check < self.CLUSTER_CHECK_INTERVAL:
            return
        
        self._last_cluster_check = now
        
        # Check if cluster is now available
        if self._is_cluster_available():
            print("🔄 Cluster is now available, switching back...", file=sys.stderr)
            if self._try_connect_to_cluster():
                print("✅ Switched back to cluster", file=sys.stderr)
    
    def _safe_close_connection(self):
        """Safely close the current connection, ignoring errors."""
        if self._connection:
            try:
                self._connection.close()
            except Exception:
                pass
            self._connection = None
    
    def _is_connection_healthy(self) -> bool:
        """
        Check if the current connection is healthy.
        
        Returns:
            True if connection is usable, False otherwise
        """
        if self._connection is None:
            return False
        
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(self.HEALTH_CHECK_QUERY)
                cursor.fetchall()
            return True
        except Exception:
            return False
    
    def _ensure_healthy_connection(self):
        """
        Ensure we have a healthy connection, reconnecting if necessary.
        Uses failover strategy if enabled.
        
        Returns:
            Active, healthy Databricks SQL connection
        """
        with self._conn_lock:
            # Check if we should switch back to cluster
            self._maybe_switch_to_cluster()
            
            if not self._is_connection_healthy():
                print("🔄 Connection unhealthy, reconnecting...", file=sys.stderr)
                self._safe_close_connection()
                
                if not self._connect_with_failover():
                    raise ConnectionError("Failed to connect to Databricks")
                
                print(f"✅ Reconnected to Databricks ({self._current_conn_type})", file=sys.stderr)
            
            self._last_activity = time.time()
            return self._connection
    
    def get_connection_info(self) -> Dict[str, Any]:
        """
        Get information about the current connection.
        
        Returns:
            Dict with connection type, http_path, using_fallback, cluster_state
        """
        return {
            "connection_type": self._current_conn_type,
            "http_path": self._current_http_path,
            "using_fallback": self._using_fallback,
            "failover_enabled": self._config.ENABLE_FAILOVER,
            "cluster_state": self._get_cluster_state() if self._config.ENABLE_FAILOVER else None,
            "cluster_id": self._config.CLUSTER_ID,
        }
    
    def _keepalive_worker(self):
        """Background worker that pings the connection to keep it alive."""
        while not self._keepalive_stop.wait(timeout=self.KEEPALIVE_INTERVAL):
            # Only ping if there's been no recent activity
            if time.time() - self._last_activity > self.KEEPALIVE_INTERVAL:
                try:
                    with self._conn_lock:
                        if self._connection is not None:
                            with self._connection.cursor() as cursor:
                                cursor.execute(self.HEALTH_CHECK_QUERY)
                                cursor.fetchall()
                            self._last_activity = time.time()
                except Exception as e:
                    print(f"⚠️  Keep-alive ping failed: {e}", file=sys.stderr)
                    # Don't reconnect here - let the next query trigger reconnection
    
    def _start_keepalive(self):
        """Start the background keep-alive thread."""
        if self._keepalive_thread is None or not self._keepalive_thread.is_alive():
            self._keepalive_stop.clear()
            self._keepalive_thread = threading.Thread(
                target=self._keepalive_worker,
                daemon=True,
                name="databricks-keepalive"
            )
            self._keepalive_thread.start()
    
    def _stop_keepalive(self):
        """Stop the background keep-alive thread."""
        self._keepalive_stop.set()
        if self._keepalive_thread and self._keepalive_thread.is_alive():
            self._keepalive_thread.join(timeout=5)
    
    def initialize(self) -> bool:
        """
        Initialize the connection pool with failover support.
        
        Returns:
            True if initialization successful, False otherwise
        """
        if self._initialized:
            return True
            
        if not self._config.TOKEN:
            print("⚠️  Cannot initialize connection: DATABRICKS_TOKEN not set", file=sys.stderr)
            return False
        
        try:
            with self._conn_lock:
                if self._config.ENABLE_FAILOVER:
                    print("🔄 Failover enabled: cluster → warehouse", file=sys.stderr)
                    if not self._connect_with_failover():
                        return False
                else:
                    self._connection = self._create_connection()
                    self._current_conn_type = self.CONN_TYPE_DEFAULT
                
                self._initialized = True
                self._last_activity = time.time()
            
            # Start keep-alive thread
            self._start_keepalive()
            
            conn_info = f"({self._current_conn_type})"
            if self._using_fallback:
                conn_info += " [fallback]"
            print(f"✅ Databricks SQL connection initialized {conn_info} (with keep-alive)", file=sys.stderr)
            return True
        except Exception as e:
            print(f"❌ Failed to initialize connection: {e}", file=sys.stderr)
            return False
    
    def get_connection(self):
        """
        Get a healthy connection, creating or reconnecting if needed.
        
        Returns:
            Active Databricks SQL connection
        """
        return self._ensure_healthy_connection()
    
    def execute(self, query: str, fetch: bool = True) -> List[Any]:
        """
        Execute a SQL query using the pooled connection.
        
        Args:
            query: SQL query to execute
            fetch: Whether to fetch results (default True)
        
        Returns:
            List of result rows, or empty list for non-SELECT queries
        """
        max_retries = 2
        last_error = None
        
        for attempt in range(max_retries):
            try:
                conn = self._ensure_healthy_connection()
                with conn.cursor() as cursor:
                    cursor.execute(query)
                    if fetch:
                        return cursor.fetchall()
                    return []
            except Exception as e:
                last_error = e
                error_str = str(e).lower()
                
                # Check for recoverable connection errors
                is_connection_error = any(msg in error_str for msg in [
                    "i/o operation on closed file",
                    "connection",
                    "session",
                    "closed",
                    "invalid sessionhandle",
                    "thrift",
                    "transport",
                    "socket",
                ])
                
                if is_connection_error and attempt < max_retries - 1:
                    print(f"⚠️  Query failed (attempt {attempt + 1}), reconnecting: {e}", file=sys.stderr)
                    with self._conn_lock:
                        self._safe_close_connection()
                    continue
                else:
                    raise
        
        raise last_error
    
    def execute_with_columns(self, query: str) -> tuple[List[Any], List[str]]:
        """
        Execute a SQL query and return results with column names.
        
        Args:
            query: SQL query to execute
        
        Returns:
            Tuple of (results, column_names)
        """
        max_retries = 2
        last_error = None
        
        for attempt in range(max_retries):
            try:
                conn = self._ensure_healthy_connection()
                with conn.cursor() as cursor:
                    cursor.execute(query)
                    results = cursor.fetchall()
                    columns = [desc[0] for desc in cursor.description] if cursor.description else []
                    return results, columns
            except Exception as e:
                last_error = e
                error_str = str(e).lower()
                
                is_connection_error = any(msg in error_str for msg in [
                    "i/o operation on closed file",
                    "connection",
                    "session",
                    "closed",
                    "invalid sessionhandle",
                    "thrift",
                    "transport",
                    "socket",
                ])
                
                if is_connection_error and attempt < max_retries - 1:
                    print(f"⚠️  Query failed (attempt {attempt + 1}), reconnecting: {e}", file=sys.stderr)
                    with self._conn_lock:
                        self._safe_close_connection()
                    continue
                else:
                    raise
        
        raise last_error
    
    def close(self):
        """Close the connection pool and stop keep-alive."""
        self._stop_keepalive()
        with self._conn_lock:
            self._safe_close_connection()
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
