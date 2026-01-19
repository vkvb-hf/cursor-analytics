#!/usr/bin/env python3
"""
Background Query Executor - Runs queries in background without blocking

This executor allows you to submit queries and continue working while they execute.
Results can be retrieved later via the tracker.
"""
import sys
import os
import threading
import time
from typing import List, Dict, Optional, Callable, Any
from databricks import sql
from concurrent.futures import ThreadPoolExecutor, Future

# Add parent directory to path for config import
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN
from parallel.query_tracker import QueryTracker, QueryStatus


class BackgroundQueryExecutor:
    """
    Executes queries in the background without blocking
    
    Queries are submitted and run asynchronously. You can check status
    and retrieve results at any time without waiting.
    """
    
    def __init__(self, max_workers: int = 5, timeout_seconds: int = 300):
        """
        Initialize background query executor
        
        Args:
            max_workers: Maximum number of concurrent queries (default: 5)
            timeout_seconds: Timeout for each query in seconds (default: 300)
        """
        self.max_workers = max_workers
        self.timeout_seconds = timeout_seconds
        self.tracker = QueryTracker()
        self._executor: Optional[ThreadPoolExecutor] = None
        self._lock = threading.Lock()
        self._futures: Dict[str, Future] = {}
        self._start_executor()
    
    def _start_executor(self):
        """Start the thread pool executor"""
        with self._lock:
            if self._executor is None or self._executor._shutdown:
                self._executor = ThreadPoolExecutor(
                    max_workers=self.max_workers,
                    thread_name_prefix="QueryExecutor"
                )
    
    def _execute_single_query(self, query: str, query_id: str, 
                              on_complete: Optional[Callable] = None,
                              on_error: Optional[Callable] = None) -> Any:
        """
        Execute a single query in a thread
        
        Args:
            query: SQL query string
            query_id: Query ID for tracking
            on_complete: Optional callback when query completes
            on_error: Optional callback when query fails
            
        Returns:
            Query results or None
        """
        thread_id = threading.get_ident()
        self.tracker.start_query(query_id, thread_id=thread_id)
        
        try:
            with sql.connect(
                server_hostname=SERVER_HOSTNAME,
                http_path=HTTP_PATH,
                access_token=TOKEN,
                timeout_seconds=self.timeout_seconds
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    result = cursor.fetchall()
                    
                    result_count = len(result) if result else 0
                    self.tracker.complete_query(query_id, result=result, result_count=result_count)
                    
                    if on_complete:
                        try:
                            on_complete(query_id, result, result_count)
                        except Exception as e:
                            print(f"Error in on_complete callback for {query_id}: {e}")
                    
                    return result
                    
        except Exception as e:
            error_msg = str(e)
            self.tracker.fail_query(query_id, error_msg)
            
            if on_error:
                try:
                    on_error(query_id, error_msg)
                except Exception as e:
                    print(f"Error in on_error callback for {query_id}: {e}")
            
            return None
    
    def submit_query(self, query: str, query_id: Optional[str] = None,
                    metadata: Optional[Dict[str, Any]] = None,
                    on_complete: Optional[Callable] = None,
                    on_error: Optional[Callable] = None) -> str:
        """
        Submit a single query to run in the background
        
        Args:
            query: SQL query string
            query_id: Optional query ID (auto-generated if not provided)
            metadata: Optional metadata dictionary
            on_complete: Optional callback function(query_id, result, result_count)
            on_error: Optional callback function(query_id, error_message)
            
        Returns:
            Query ID string
        """
        if query_id is None:
            query_id = self.tracker.register_query(query, metadata=metadata)
        else:
            self.tracker.register_query(query, query_id=query_id, metadata=metadata)
        
        # Ensure executor is running
        self._start_executor()
        
        # Submit query to executor
        future = self._executor.submit(
            self._execute_single_query,
            query,
            query_id,
            on_complete,
            on_error
        )
        
        with self._lock:
            self._futures[query_id] = future
        
        return query_id
    
    def submit_queries(self, queries: List[str],
                      query_ids: Optional[List[str]] = None,
                      metadata: Optional[List[Dict[str, Any]]] = None,
                      on_complete: Optional[Callable] = None,
                      on_error: Optional[Callable] = None) -> List[str]:
        """
        Submit multiple queries to run in the background
        
        Args:
            queries: List of SQL query strings
            query_ids: Optional list of query IDs
            metadata: Optional list of metadata dictionaries
            on_complete: Optional callback function(query_id, result, result_count)
            on_error: Optional callback function(query_id, error_message)
            
        Returns:
            List of query IDs
        """
        if query_ids is None:
            query_ids = []
            for query in queries:
                query_ids.append(self.tracker.register_query(query))
        else:
            for i, query in enumerate(queries):
                meta = metadata[i] if metadata and i < len(metadata) else None
                self.tracker.register_query(query, query_id=query_ids[i], metadata=meta)
        
        # Submit all queries
        for query, query_id in zip(queries, query_ids):
            self.submit_query(query, query_id, 
                            metadata=metadata[query_ids.index(query_id)] if metadata else None,
                            on_complete=on_complete,
                            on_error=on_error)
        
        return query_ids
    
    def submit_query_file(self, file_path: str,
                         query_id: Optional[str] = None,
                         on_complete: Optional[Callable] = None,
                         on_error: Optional[Callable] = None) -> str:
        """
        Submit a query from a SQL file to run in the background
        
        Args:
            file_path: Path to SQL file
            query_id: Optional query ID (uses filename if not provided)
            on_complete: Optional callback function
            on_error: Optional callback function
            
        Returns:
            Query ID string
        """
        try:
            with open(file_path, 'r') as f:
                query = f.read()
            
            if query_id is None:
                import os
                query_id = os.path.basename(file_path).replace('.sql', '')
            
            metadata = {"file_path": file_path, "filename": os.path.basename(file_path)}
            return self.submit_query(query, query_id, metadata, on_complete, on_error)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            raise
    
    def submit_query_files(self, file_paths: List[str],
                          query_ids: Optional[List[str]] = None,
                          on_complete: Optional[Callable] = None,
                          on_error: Optional[Callable] = None) -> List[str]:
        """
        Submit multiple queries from SQL files to run in the background
        
        Args:
            file_paths: List of paths to SQL files
            query_ids: Optional list of query IDs
            on_complete: Optional callback function
            on_error: Optional callback function
            
        Returns:
            List of query IDs
        """
        if query_ids is None:
            import os
            query_ids = [os.path.basename(fp).replace('.sql', '') for fp in file_paths]
        
        submitted_ids = []
        for file_path, query_id in zip(file_paths, query_ids):
            try:
                qid = self.submit_query_file(file_path, query_id, on_complete, on_error)
                submitted_ids.append(qid)
            except Exception as e:
                print(f"Failed to submit {file_path}: {e}")
        
        return submitted_ids
    
    def get_result(self, query_id: str, wait: bool = False, timeout: Optional[float] = None) -> Optional[Any]:
        """
        Get result for a specific query
        
        Args:
            query_id: Query ID
            wait: If True, wait for query to complete if still running
            timeout: Maximum time to wait in seconds (None = wait indefinitely)
            
        Returns:
            Query result or None if not available/failed
        """
        query_info = self.tracker.get_query(query_id)
        
        if query_info is None:
            return None
        
        if query_info.status == QueryStatus.COMPLETED:
            return query_info.result
        
        if query_info.status == QueryStatus.FAILED:
            return None
        
        if wait and query_info.status in [QueryStatus.PENDING, QueryStatus.RUNNING]:
            # Wait for completion
            future = self._futures.get(query_id)
            if future:
                try:
                    future.result(timeout=timeout)
                    query_info = self.tracker.get_query(query_id)
                    if query_info and query_info.status == QueryStatus.COMPLETED:
                        return query_info.result
                except Exception as e:
                    print(f"Error waiting for query {query_id}: {e}")
        
        return None
    
    def wait_for_query(self, query_id: str, timeout: Optional[float] = None) -> bool:
        """
        Wait for a specific query to complete
        
        Args:
            query_id: Query ID
            timeout: Maximum time to wait in seconds (None = wait indefinitely)
            
        Returns:
            True if completed successfully, False otherwise
        """
        future = self._futures.get(query_id)
        if future:
            try:
                future.result(timeout=timeout)
                query_info = self.tracker.get_query(query_id)
                return query_info and query_info.status == QueryStatus.COMPLETED
            except Exception as e:
                print(f"Error waiting for query {query_id}: {e}")
                return False
        return False
    
    def wait_for_all(self, timeout: Optional[float] = None):
        """
        Wait for all running queries to complete
        
        Args:
            timeout: Maximum time to wait in seconds (None = wait indefinitely)
        """
        start_time = time.time()
        
        while True:
            running = self.tracker.get_running_queries()
            pending = self.tracker.get_pending_queries()
            
            if not running and not pending:
                break
            
            if timeout and (time.time() - start_time) > timeout:
                print(f"Timeout waiting for queries to complete")
                break
            
            time.sleep(0.5)
    
    def get_tracker(self) -> QueryTracker:
        """Get the query tracker instance"""
        return self.tracker
    
    def print_status(self):
        """Print current status of all queries"""
        self.tracker.print_status()
    
    def shutdown(self, wait: bool = True):
        """
        Shutdown the executor
        
        Args:
            wait: If True, wait for running queries to complete
        """
        with self._lock:
            if self._executor and not self._executor._shutdown:
                if wait:
                    self.wait_for_all()
                self._executor.shutdown(wait=wait)
                self._executor = None


# Global background executor instance
_global_executor: Optional[BackgroundQueryExecutor] = None
_executor_lock = threading.Lock()


def get_background_executor(max_workers: int = 5, timeout_seconds: int = 300) -> BackgroundQueryExecutor:
    """
    Get or create a global background executor instance
    
    Args:
        max_workers: Maximum number of concurrent queries
        timeout_seconds: Timeout per query in seconds
        
    Returns:
        BackgroundQueryExecutor instance
    """
    global _global_executor
    
    with _executor_lock:
        if _global_executor is None or _global_executor._executor is None or _global_executor._executor._shutdown:
            _global_executor = BackgroundQueryExecutor(max_workers, timeout_seconds)
        return _global_executor

