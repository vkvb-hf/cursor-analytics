#!/usr/bin/env python3
"""
Query Tracker - Tracks the status of SQL queries being executed
"""
import threading
import time
from datetime import datetime
from enum import Enum
from typing import Dict, Optional, Any, List
from dataclasses import dataclass, field


class QueryStatus(Enum):
    """Status of a query execution"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class QueryInfo:
    """Information about a query being tracked"""
    query_id: str
    query: str
    status: QueryStatus = QueryStatus.PENDING
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration_seconds: Optional[float] = None
    error: Optional[str] = None
    result_count: Optional[int] = None
    result: Optional[Any] = None
    thread_id: Optional[int] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


class QueryTracker:
    """
    Thread-safe tracker for monitoring SQL query execution
    """
    
    def __init__(self):
        self._queries: Dict[str, QueryInfo] = {}
        self._lock = threading.Lock()
        self._next_id = 1
    
    def register_query(self, query: str, query_id: Optional[str] = None, 
                      metadata: Optional[Dict[str, Any]] = None) -> str:
        """
        Register a new query to track
        
        Args:
            query: SQL query string
            query_id: Optional custom query ID (auto-generated if not provided)
            metadata: Optional metadata dictionary
            
        Returns:
            Query ID string
        """
        with self._lock:
            if query_id is None:
                query_id = f"query_{self._next_id}_{int(time.time())}"
                self._next_id += 1
            
            query_info = QueryInfo(
                query_id=query_id,
                query=query,
                status=QueryStatus.PENDING,
                metadata=metadata or {}
            )
            self._queries[query_id] = query_info
            return query_id
    
    def start_query(self, query_id: str, thread_id: Optional[int] = None):
        """Mark a query as started"""
        with self._lock:
            if query_id in self._queries:
                self._queries[query_id].status = QueryStatus.RUNNING
                self._queries[query_id].start_time = datetime.now()
                if thread_id is not None:
                    self._queries[query_id].thread_id = thread_id
    
    def complete_query(self, query_id: str, result: Optional[Any] = None, 
                      result_count: Optional[int] = None):
        """Mark a query as completed"""
        with self._lock:
            if query_id in self._queries:
                query_info = self._queries[query_id]
                query_info.status = QueryStatus.COMPLETED
                query_info.end_time = datetime.now()
                query_info.result = result
                query_info.result_count = result_count
                if query_info.start_time:
                    query_info.duration_seconds = (
                        query_info.end_time - query_info.start_time
                    ).total_seconds()
    
    def fail_query(self, query_id: str, error: str):
        """Mark a query as failed"""
        with self._lock:
            if query_id in self._queries:
                query_info = self._queries[query_id]
                query_info.status = QueryStatus.FAILED
                query_info.end_time = datetime.now()
                query_info.error = error
                if query_info.start_time:
                    query_info.duration_seconds = (
                        query_info.end_time - query_info.start_time
                    ).total_seconds()
    
    def cancel_query(self, query_id: str):
        """Mark a query as cancelled"""
        with self._lock:
            if query_id in self._queries:
                query_info = self._queries[query_id]
                query_info.status = QueryStatus.CANCELLED
                query_info.end_time = datetime.now()
                if query_info.start_time:
                    query_info.duration_seconds = (
                        query_info.end_time - query_info.start_time
                    ).total_seconds()
    
    def get_query(self, query_id: str) -> Optional[QueryInfo]:
        """Get query information by ID"""
        with self._lock:
            return self._queries.get(query_id)
    
    def get_all_queries(self) -> List[QueryInfo]:
        """Get all tracked queries"""
        with self._lock:
            return list(self._queries.values())
    
    def get_running_queries(self) -> List[QueryInfo]:
        """Get all currently running queries"""
        with self._lock:
            return [q for q in self._queries.values() 
                   if q.status == QueryStatus.RUNNING]
    
    def get_pending_queries(self) -> List[QueryInfo]:
        """Get all pending queries"""
        with self._lock:
            return [q for q in self._queries.values() 
                   if q.status == QueryStatus.PENDING]
    
    def get_completed_queries(self) -> List[QueryInfo]:
        """Get all completed queries"""
        with self._lock:
            return [q for q in self._queries.values() 
                   if q.status == QueryStatus.COMPLETED]
    
    def get_failed_queries(self) -> List[QueryInfo]:
        """Get all failed queries"""
        with self._lock:
            return [q for q in self._queries.values() 
                   if q.status == QueryStatus.FAILED]
    
    def get_status_summary(self) -> Dict[str, int]:
        """Get summary of query statuses"""
        with self._lock:
            summary = {
                "total": len(self._queries),
                "pending": 0,
                "running": 0,
                "completed": 0,
                "failed": 0,
                "cancelled": 0
            }
            for query in self._queries.values():
                summary[query.status.value] = summary.get(query.status.value, 0) + 1
            return summary
    
    def print_status(self):
        """Print current status of all queries"""
        with self._lock:
            summary = self.get_status_summary()
            print("\n" + "="*100)
            print("QUERY TRACKER STATUS")
            print("="*100)
            print(f"Total queries: {summary['total']}")
            print(f"  Pending:   {summary['pending']}")
            print(f"  Running:   {summary['running']}")
            print(f"  Completed: {summary['completed']}")
            print(f"  Failed:    {summary['failed']}")
            print(f"  Cancelled: {summary['cancelled']}")
            print("="*100)
            
            if self._queries:
                print("\nQuery Details:")
                print("-"*100)
                for query_id, query_info in sorted(self._queries.items()):
                    status_icon = {
                        QueryStatus.PENDING: "⏳",
                        QueryStatus.RUNNING: "🔄",
                        QueryStatus.COMPLETED: "✅",
                        QueryStatus.FAILED: "❌",
                        QueryStatus.CANCELLED: "🚫"
                    }.get(query_info.status, "❓")
                    
                    print(f"{status_icon} [{query_info.query_id}] {query_info.status.value.upper()}")
                    
                    # Truncate query for display
                    query_preview = query_info.query[:80] + "..." if len(query_info.query) > 80 else query_info.query
                    print(f"   Query: {query_preview}")
                    
                    if query_info.start_time:
                        print(f"   Started: {query_info.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
                    
                    if query_info.duration_seconds is not None:
                        print(f"   Duration: {query_info.duration_seconds:.2f}s")
                    
                    if query_info.result_count is not None:
                        print(f"   Rows: {query_info.result_count:,}")
                    
                    if query_info.error:
                        print(f"   Error: {query_info.error[:100]}")
                    
                    print()
            
            print("="*100 + "\n")
    
    def clear_completed(self):
        """Clear all completed queries from tracker"""
        with self._lock:
            self._queries = {
                qid: qinfo for qid, qinfo in self._queries.items()
                if qinfo.status != QueryStatus.COMPLETED
            }
    
    def clear_all(self):
        """Clear all queries from tracker"""
        with self._lock:
            self._queries.clear()

