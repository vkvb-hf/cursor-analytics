#!/usr/bin/env python3
"""
Parallel Query API - Programmatic interface for parallel query execution

This module provides a simple API for running queries in parallel from Python scripts.
"""
import sys
import os
from typing import List, Dict, Optional, Callable, Any

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parallel.parallel_executor import ParallelQueryExecutor
from parallel.query_tracker import QueryTracker, QueryStatus


class ParallelQueryAPI:
    """
    Simple API for parallel query execution
    """
    
    def __init__(self, max_workers: int = 5, timeout_seconds: int = 300):
        """
        Initialize the API
        
        Args:
            max_workers: Maximum number of concurrent queries
            timeout_seconds: Timeout per query in seconds
        """
        self.executor = ParallelQueryExecutor(
            max_workers=max_workers,
            timeout_seconds=timeout_seconds
        )
    
    def run_queries(self, queries: List[str], 
                   query_ids: Optional[List[str]] = None,
                   wait: bool = True) -> Dict[str, Any]:
        """
        Run multiple queries in parallel
        
        Args:
            queries: List of SQL query strings
            query_ids: Optional list of query IDs
            wait: If True, wait for all queries to complete
            
        Returns:
            Dictionary mapping query_id to result
        """
        return self.executor.execute_queries(
            queries=queries,
            query_ids=query_ids,
            wait_for_completion=wait
        )
    
    def run_files(self, file_paths: List[str],
                 wait: bool = True) -> Dict[str, Any]:
        """
        Run queries from SQL files in parallel
        
        Args:
            file_paths: List of paths to SQL files
            wait: If True, wait for all queries to complete
            
        Returns:
            Dictionary mapping query_id to result
        """
        return self.executor.execute_query_files(
            file_paths=file_paths,
            wait_for_completion=wait
        )
    
    def get_status(self) -> Dict[str, int]:
        """Get summary of query statuses"""
        return self.executor.get_tracker().get_status_summary()
    
    def get_results(self) -> Dict[str, Any]:
        """
        Get results from all completed queries
        
        Returns:
            Dictionary mapping query_id to result
        """
        completed = self.executor.get_tracker().get_completed_queries()
        return {q.query_id: q.result for q in completed if q.result is not None}
    
    def get_failed_queries(self) -> List[Dict[str, Any]]:
        """
        Get information about failed queries
        
        Returns:
            List of dictionaries with query_id, query, and error
        """
        failed = self.executor.get_tracker().get_failed_queries()
        return [
            {
                'query_id': q.query_id,
                'query': q.query,
                'error': q.error,
                'metadata': q.metadata
            }
            for q in failed
        ]
    
    def wait_for_completion(self, timeout: Optional[float] = None):
        """Wait for all running queries to complete"""
        self.executor.wait_for_all(timeout=timeout)
    
    def print_status(self):
        """Print current status"""
        self.executor.print_status()
    
    def get_tracker(self) -> QueryTracker:
        """Get the query tracker instance"""
        return self.executor.get_tracker()


# Convenience function for quick usage
def run_parallel(queries: List[str], max_workers: int = 5, 
                wait: bool = True) -> Dict[str, Any]:
    """
    Quick function to run queries in parallel
    
    Args:
        queries: List of SQL query strings
        max_workers: Maximum number of concurrent queries
        wait: If True, wait for all queries to complete
        
    Returns:
        Dictionary mapping query_id to result
        
    Example:
        results = run_parallel([
            "SELECT COUNT(*) FROM table1",
            "SELECT COUNT(*) FROM table2",
            "SELECT COUNT(*) FROM table3"
        ])
    """
    api = ParallelQueryAPI(max_workers=max_workers)
    return api.run_queries(queries, wait=wait)


if __name__ == "__main__":
    # Example usage
    api = ParallelQueryAPI(max_workers=3)
    
    queries = [
        "SELECT 1 as test1",
        "SELECT 2 as test2",
        "SELECT 3 as test3"
    ]
    
    print("Running queries in parallel...")
    results = api.run_queries(queries)
    
    print("\nStatus:")
    api.print_status()
    
    print("\nResults:")
    for query_id, result in results.items():
        print(f"{query_id}: {result}")

