#!/usr/bin/env python3
"""
Parallel Query Executor - Executes multiple SQL queries concurrently
"""
import sys
import os
import threading
from typing import List, Dict, Optional, Callable, Any
from databricks import sql
from concurrent.futures import ThreadPoolExecutor, as_completed

# Add parent directory to path for config import
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN
from parallel.query_tracker import QueryTracker, QueryStatus


class ParallelQueryExecutor:
    """
    Executes multiple SQL queries in parallel using threading
    """
    
    def __init__(self, max_workers: int = 5, timeout_seconds: int = 300):
        """
        Initialize parallel query executor
        
        Args:
            max_workers: Maximum number of concurrent queries (default: 5)
            timeout_seconds: Timeout for each query in seconds (default: 300)
        """
        self.max_workers = max_workers
        self.timeout_seconds = timeout_seconds
        self.tracker = QueryTracker()
        self._executor: Optional[ThreadPoolExecutor] = None
    
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
                        on_complete(query_id, result, result_count)
                    
                    return result
                    
        except Exception as e:
            error_msg = str(e)
            self.tracker.fail_query(query_id, error_msg)
            
            if on_error:
                on_error(query_id, error_msg)
            
            return None
    
    def execute_queries(self, queries: List[str], 
                       query_ids: Optional[List[str]] = None,
                       metadata: Optional[List[Dict[str, Any]]] = None,
                       on_complete: Optional[Callable] = None,
                       on_error: Optional[Callable] = None,
                       wait_for_completion: bool = True) -> Dict[str, Any]:
        """
        Execute multiple queries in parallel
        
        Args:
            queries: List of SQL query strings
            query_ids: Optional list of query IDs (auto-generated if not provided)
            metadata: Optional list of metadata dictionaries for each query
            on_complete: Optional callback function(query_id, result, result_count)
            on_error: Optional callback function(query_id, error_message)
            wait_for_completion: If True, wait for all queries to complete (default: True)
            
        Returns:
            Dictionary mapping query_id to result
        """
        if query_ids is None:
            query_ids = [self.tracker.register_query(q) for q in queries]
        else:
            # Register queries with provided IDs
            for i, query in enumerate(queries):
                meta = metadata[i] if metadata and i < len(metadata) else None
                self.tracker.register_query(query, query_id=query_ids[i], metadata=meta)
        
        results = {}
        
        # Create thread pool executor
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all queries
            future_to_query_id = {
                executor.submit(
                    self._execute_single_query,
                    query,
                    query_id,
                    on_complete,
                    on_error
                ): query_id
                for query, query_id in zip(queries, query_ids)
            }
            
            if wait_for_completion:
                # Wait for all queries to complete
                for future in as_completed(future_to_query_id):
                    query_id = future_to_query_id[future]
                    try:
                        result = future.result()
                        results[query_id] = result
                    except Exception as e:
                        results[query_id] = None
                        print(f"Error executing query {query_id}: {e}")
            else:
                # Return immediately, results will be available via tracker
                pass
        
        return results
    
    def execute_query_files(self, file_paths: List[str],
                           query_ids: Optional[List[str]] = None,
                           wait_for_completion: bool = True) -> Dict[str, Any]:
        """
        Execute queries from SQL files in parallel
        
        Args:
            file_paths: List of paths to SQL files
            query_ids: Optional list of query IDs (uses filename if not provided)
            wait_for_completion: If True, wait for all queries to complete
            
        Returns:
            Dictionary mapping query_id to result
        """
        queries = []
        metadata_list = []
        
        for file_path in file_paths:
            try:
                with open(file_path, 'r') as f:
                    query = f.read()
                queries.append(query)
                
                # Use filename as metadata
                import os
                filename = os.path.basename(file_path)
                metadata_list.append({"file_path": file_path, "filename": filename})
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
                queries.append("")  # Placeholder
                metadata_list.append({"file_path": file_path, "error": str(e)})
        
        if query_ids is None:
            query_ids = [os.path.basename(fp).replace('.sql', '') for fp in file_paths]
        
        return self.execute_queries(
            queries,
            query_ids=query_ids,
            metadata=metadata_list,
            wait_for_completion=wait_for_completion
        )
    
    def get_tracker(self) -> QueryTracker:
        """Get the query tracker instance"""
        return self.tracker
    
    def wait_for_all(self, timeout: Optional[float] = None):
        """
        Wait for all running queries to complete
        
        Args:
            timeout: Maximum time to wait in seconds (None = wait indefinitely)
        """
        import time
        start_time = time.time()
        
        while True:
            running = self.tracker.get_running_queries()
            if not running:
                break
            
            if timeout and (time.time() - start_time) > timeout:
                print(f"Timeout waiting for queries to complete")
                break
            
            time.sleep(0.5)  # Check every 500ms
    
    def print_status(self):
        """Print current status of all queries"""
        self.tracker.print_status()

