#!/usr/bin/env python3
"""
Run Queries in Background - Non-blocking query execution

This script allows you to submit queries and continue working while they execute.
You can check status and retrieve results later.

Usage:
    python run_background_queries.py --queries "SELECT 1" "SELECT 2"
    python run_background_queries.py --files query1.sql query2.sql
    python run_background_queries.py --status  # Check status of running queries
    python run_background_queries.py --results query_1 query_2  # Get results
"""
import sys
import os
import argparse
import time
from pathlib import Path
from typing import List, Optional

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parallel.background_executor import get_background_executor, BackgroundQueryExecutor
from parallel.query_tracker import QueryStatus
from core.query_util import print_table


def submit_queries(executor: BackgroundQueryExecutor, queries: List[str], 
                  query_ids: Optional[List[str]] = None):
    """Submit queries to run in background"""
    print("="*100)
    print("SUBMITTING QUERIES TO RUN IN BACKGROUND")
    print("="*100)
    
    submitted_ids = executor.submit_queries(queries, query_ids=query_ids)
    
    print(f"\n✓ Submitted {len(submitted_ids)} queries")
    print("\nQuery IDs:")
    for qid in submitted_ids:
        print(f"  - {qid}")
    
    print("\n" + "="*100)
    print("Queries are now running in the background!")
    print("You can continue working or check status with --status")
    print("="*100 + "\n")
    
    return submitted_ids


def submit_files(executor: BackgroundQueryExecutor, file_paths: List[str]):
    """Submit SQL files to run in background"""
    print("="*100)
    print("SUBMITTING SQL FILES TO RUN IN BACKGROUND")
    print("="*100)
    
    # Validate files exist
    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"Error: File not found: {file_path}")
            return []
    
    submitted_ids = executor.submit_query_files(file_paths)
    
    print(f"\n✓ Submitted {len(submitted_ids)} queries from files")
    print("\nQuery IDs:")
    for qid in submitted_ids:
        print(f"  - {qid}")
    
    print("\n" + "="*100)
    print("Queries are now running in the background!")
    print("You can continue working or check status with --status")
    print("="*100 + "\n")
    
    return submitted_ids


def show_status(executor: BackgroundQueryExecutor):
    """Show status of all queries"""
    executor.print_status()


def show_results(executor: BackgroundQueryExecutor, query_ids: List[str], 
                show_table: bool = True):
    """Show results for specific queries"""
    print("="*100)
    print("QUERY RESULTS")
    print("="*100)
    
    for query_id in query_ids:
        query_info = executor.get_tracker().get_query(query_id)
        
        if query_info is None:
            print(f"\n❌ Query {query_id} not found")
            continue
        
        print(f"\n[{query_id}]")
        print("-"*100)
        print(f"Status: {query_info.status.value}")
        
        if query_info.status == QueryStatus.RUNNING:
            if query_info.start_time:
                elapsed = (time.time() - query_info.start_time.timestamp())
                print(f"Running for: {elapsed:.1f}s")
            print("Query is still running. Use --wait to wait for completion.")
        
        elif query_info.status == QueryStatus.PENDING:
            print("Query is pending execution.")
        
        elif query_info.status == QueryStatus.COMPLETED:
            print(f"Duration: {query_info.duration_seconds:.2f}s")
            print(f"Rows returned: {query_info.result_count:,}")
            
            if show_table and query_info.result:
                # Get column names
                column_names = None
                if hasattr(query_info.result[0], '_fields'):
                    column_names = list(query_info.result[0]._fields)
                elif hasattr(query_info.result[0], '__dict__'):
                    column_names = [k for k in query_info.result[0].__dict__.keys() if not k.startswith('_')]
                
                print_table(
                    query_info.result,
                    column_names=column_names,
                    limit=50,
                    title=f"Results from {query_id}"
                )
        
        elif query_info.status == QueryStatus.FAILED:
            print(f"Error: {query_info.error}")
    
    print("="*100 + "\n")


def wait_for_queries(executor: BackgroundQueryExecutor, query_ids: Optional[List[str]] = None,
                    timeout: Optional[float] = None):
    """Wait for queries to complete"""
    if query_ids:
        print(f"Waiting for {len(query_ids)} queries to complete...")
        for qid in query_ids:
            executor.wait_for_query(qid, timeout=timeout)
    else:
        print("Waiting for all queries to complete...")
        executor.wait_for_all(timeout=timeout)
    
    print("✓ All requested queries completed\n")


def main():
    parser = argparse.ArgumentParser(
        description='Run queries in background (non-blocking)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Submit queries to run in background
  python run_background_queries.py --queries "SELECT 1" "SELECT 2"
  
  # Submit SQL files
  python run_background_queries.py --files query1.sql query2.sql
  
  # Check status of all queries
  python run_background_queries.py --status
  
  # Get results for specific queries
  python run_background_queries.py --results query_1 query_2
  
  # Wait for queries to complete
  python run_background_queries.py --wait query_1 query_2
        """
    )
    
    parser.add_argument('--queries', nargs='+',
                       help='SQL queries to submit (runs in background)')
    parser.add_argument('--files', nargs='+',
                       help='SQL file paths to submit (runs in background)')
    parser.add_argument('--status', action='store_true',
                       help='Show status of all queries')
    parser.add_argument('--results', nargs='+',
                       help='Show results for specific query IDs')
    parser.add_argument('--wait', nargs='*', metavar='QUERY_ID',
                       help='Wait for queries to complete (all if no IDs provided)')
    parser.add_argument('--timeout', type=float,
                       help='Timeout in seconds when waiting')
    parser.add_argument('--max-workers', type=int, default=5,
                       help='Maximum concurrent queries (default: 5)')
    
    args = parser.parse_args()
    
    # Get background executor
    executor = get_background_executor(max_workers=args.max_workers)
    
    # Handle different actions
    if args.queries:
        submit_queries(executor, args.queries)
    
    elif args.files:
        submit_files(executor, args.files)
    
    elif args.status:
        show_status(executor)
    
    elif args.results:
        show_results(executor, args.results)
    
    elif args.wait is not None:
        wait_for_queries(executor, args.wait if args.wait else None, args.timeout)
        show_status(executor)
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

