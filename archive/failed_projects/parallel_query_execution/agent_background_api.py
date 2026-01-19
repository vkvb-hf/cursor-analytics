#!/usr/bin/env python3
"""
Agent Background API - Direct Python API for agents to submit queries without blocking

This API allows agents to submit queries and immediately return control,
without waiting for queries to complete. The chat interface stays responsive.
"""
import sys
import os
import threading
from typing import List, Dict, Optional, Any

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parallel.background_executor import get_background_executor, BackgroundQueryExecutor


class AgentBackgroundAPI:
    """
    API for agents to submit queries in background without blocking chat interface
    
    Usage:
        api = AgentBackgroundAPI()
        query_ids = api.submit_queries([query1, query2])
        # Returns immediately - chat interface stays responsive
        # Later: results = api.get_results(query_ids)
    """
    
    def __init__(self, max_workers: int = 5, timeout_seconds: int = 300):
        """Initialize the API"""
        self.executor = get_background_executor(max_workers, timeout_seconds)
    
    def submit_queries(self, queries: List[str], 
                      query_ids: Optional[List[str]] = None,
                      metadata: Optional[List[Dict[str, Any]]] = None) -> List[str]:
        """
        Submit queries to run in background - RETURNS IMMEDIATELY
        
        This method does NOT block. The chat interface stays responsive.
        
        Args:
            queries: List of SQL query strings
            query_ids: Optional list of query IDs
            metadata: Optional metadata for each query
            
        Returns:
            List of query IDs
        """
        return self.executor.submit_queries(
            queries=queries,
            query_ids=query_ids,
            metadata=metadata
        )
    
    def submit_query_files(self, file_paths: List[str],
                          query_ids: Optional[List[str]] = None) -> List[str]:
        """
        Submit SQL files to run in background - RETURNS IMMEDIATELY
        
        Args:
            file_paths: List of SQL file paths
            query_ids: Optional list of query IDs
            
        Returns:
            List of query IDs
        """
        return self.executor.submit_query_files(
            file_paths=file_paths,
            query_ids=query_ids
        )
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get status of all queries - NON-BLOCKING
        
        Returns:
            Dictionary with status summary
        """
        return self.executor.get_tracker().get_status_summary()
    
    def get_results(self, query_ids: Optional[List[str]] = None,
                   wait: bool = False) -> Dict[str, Any]:
        """
        Get results for queries - Only blocks if wait=True
        
        Args:
            query_ids: List of query IDs (None = all completed)
            wait: If True, wait for queries to complete
            
        Returns:
            Dictionary mapping query_id to result
        """
        if query_ids is None:
            # Get all completed queries
            completed = self.executor.get_tracker().get_completed_queries()
            results = {}
            for q in completed:
                if q.result is not None:
                    results[q.query_id] = q.result
            return results
        else:
            results = {}
            for qid in query_ids:
                result = self.executor.get_result(qid, wait=wait)
                if result is not None:
                    results[qid] = result
            return results
    
    def check_completed(self, query_ids: List[str]) -> Dict[str, bool]:
        """
        Check which queries have completed - NON-BLOCKING
        
        Returns:
            Dictionary mapping query_id to completion status
        """
        status = {}
        for qid in query_ids:
            query_info = self.executor.get_tracker().get_query(qid)
            status[qid] = query_info is not None and query_info.status.value == 'completed'
        return status
    
    def print_status(self):
        """Print current status - NON-BLOCKING"""
        self.executor.print_status()


# Global instance for easy access
_global_api: Optional[AgentBackgroundAPI] = None
_api_lock = threading.Lock()


def get_api(max_workers: int = 5, timeout_seconds: int = 300) -> AgentBackgroundAPI:
    """
    Get or create global API instance
    
    Returns:
        AgentBackgroundAPI instance
    """
    global _global_api
    
    with _api_lock:
        if _global_api is None:
            _global_api = AgentBackgroundAPI(max_workers, timeout_seconds)
        return _global_api


# Convenience function for quick usage
def submit_and_continue(queries: List[str], 
                        query_ids: Optional[List[str]] = None) -> List[str]:
    """
    Submit queries and return immediately - chat interface stays responsive
    
    This is the main function agents should use. It:
    1. Submits queries to background
    2. Returns immediately (non-blocking)
    3. Chat interface stays responsive
    
    Args:
        queries: List of SQL query strings
        query_ids: Optional list of query IDs
        
    Returns:
        List of query IDs
        
    Example:
        # Submit queries - returns in <0.1s, chat stays responsive
        query_ids = submit_and_continue([
            "SELECT COUNT(*) FROM table1",
            "SELECT COUNT(*) FROM table2"
        ])
        
        # Later, check results (non-blocking)
        api = get_api()
        results = api.get_results(query_ids, wait=False)
    """
    api = get_api()
    return api.submit_queries(queries, query_ids=query_ids)

