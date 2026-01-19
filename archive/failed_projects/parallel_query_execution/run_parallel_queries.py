#!/usr/bin/env python3
"""
Run Multiple SQL Queries in Parallel

Usage:
    python run_parallel_queries.py --queries "SELECT 1" "SELECT 2" "SELECT 3"
    python run_parallel_queries.py --files query1.sql query2.sql query3.sql
    python run_parallel_queries.py --files query1.sql query2.sql --max-workers 10
"""
import sys
import os
import argparse
import time
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parallel.parallel_executor import ParallelQueryExecutor
from parallel.query_tracker import QueryStatus


def print_results_summary(executor: ParallelQueryExecutor):
    """Print summary of query results"""
    tracker = executor.get_tracker()
    all_queries = tracker.get_all_queries()
    
    print("\n" + "="*100)
    print("EXECUTION SUMMARY")
    print("="*100)
    
    completed = tracker.get_completed_queries()
    failed = tracker.get_failed_queries()
    running = tracker.get_running_queries()
    
    print(f"\n✅ Completed: {len(completed)}")
    print(f"❌ Failed: {len(failed)}")
    print(f"🔄 Running: {len(running)}")
    
    if completed:
        print("\n" + "-"*100)
        print("COMPLETED QUERIES:")
        print("-"*100)
        for query_info in completed:
            duration = query_info.duration_seconds or 0
            rows = query_info.result_count or 0
            print(f"  ✅ {query_info.query_id}")
            print(f"     Duration: {duration:.2f}s | Rows: {rows:,}")
            if query_info.metadata.get('filename'):
                print(f"     File: {query_info.metadata['filename']}")
    
    if failed:
        print("\n" + "-"*100)
        print("FAILED QUERIES:")
        print("-"*100)
        for query_info in failed:
            print(f"  ❌ {query_info.query_id}")
            print(f"     Error: {query_info.error}")
            if query_info.metadata.get('filename'):
                print(f"     File: {query_info.metadata['filename']}")
    
    print("\n" + "="*100 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description='Execute multiple SQL queries in parallel',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run multiple queries from command line
  python run_parallel_queries.py --queries "SELECT 1" "SELECT 2" "SELECT 3"
  
  # Run queries from SQL files
  python run_parallel_queries.py --files query1.sql query2.sql query3.sql
  
  # Run with custom max workers
  python run_parallel_queries.py --files *.sql --max-workers 10
  
  # Run queries and show status updates
  python run_parallel_queries.py --files *.sql --status-interval 2
        """
    )
    
    parser.add_argument('--queries', nargs='+', 
                       help='SQL queries to execute (as separate arguments)')
    parser.add_argument('--files', nargs='+',
                       help='SQL file paths to execute')
    parser.add_argument('--max-workers', type=int, default=5,
                       help='Maximum number of concurrent queries (default: 5)')
    parser.add_argument('--timeout', type=int, default=300,
                       help='Timeout per query in seconds (default: 300)')
    parser.add_argument('--status-interval', type=float, default=None,
                       help='Print status updates every N seconds (default: disabled)')
    parser.add_argument('--no-wait', action='store_true',
                       help='Do not wait for queries to complete (returns immediately)')
    parser.add_argument('--show-results', action='store_true',
                       help='Show query results (default: summary only)')
    
    args = parser.parse_args()
    
    if not args.queries and not args.files:
        parser.error("Must provide either --queries or --files")
    
    if args.queries and args.files:
        parser.error("Cannot provide both --queries and --files")
    
    # Create executor
    executor = ParallelQueryExecutor(
        max_workers=args.max_workers,
        timeout_seconds=args.timeout
    )
    
    print("="*100)
    print("PARALLEL QUERY EXECUTOR")
    print("="*100)
    print(f"Max workers: {args.max_workers}")
    print(f"Timeout: {args.timeout}s")
    print("="*100 + "\n")
    
    # Execute queries
    start_time = time.time()
    
    if args.queries:
        print(f"Executing {len(args.queries)} queries in parallel...\n")
        results = executor.execute_queries(
            queries=args.queries,
            wait_for_completion=not args.no_wait
        )
    else:
        # Validate files exist
        for file_path in args.files:
            if not os.path.exists(file_path):
                print(f"Error: File not found: {file_path}")
                sys.exit(1)
        
        print(f"Executing {len(args.files)} SQL files in parallel...\n")
        results = executor.execute_query_files(
            file_paths=args.files,
            wait_for_completion=not args.no_wait
        )
    
    # Monitor status if interval is set
    if args.status_interval and not args.no_wait:
        import threading
        
        def status_monitor():
            while True:
                running = executor.get_tracker().get_running_queries()
                if not running:
                    break
                executor.print_status()
                time.sleep(args.status_interval)
        
        monitor_thread = threading.Thread(target=status_monitor, daemon=True)
        monitor_thread.start()
    
    # Wait for completion if requested
    if not args.no_wait:
        executor.wait_for_all()
        total_time = time.time() - start_time
        print(f"\n✓ All queries completed in {total_time:.2f}s\n")
    
    # Print final status
    executor.print_status()
    
    # Print results summary
    print_results_summary(executor)
    
    # Show results if requested
    if args.show_results:
        tracker = executor.get_tracker()
        completed = tracker.get_completed_queries()
        
        if completed:
            print("="*100)
            print("QUERY RESULTS")
            print("="*100)
            
            for query_info in completed:
                print(f"\n[{query_info.query_id}]")
                print("-"*100)
                if query_info.result:
                    # Show first few rows
                    for i, row in enumerate(query_info.result[:10]):
                        print(f"Row {i+1}: {row}")
                    if len(query_info.result) > 10:
                        print(f"... ({len(query_info.result) - 10} more rows)")
                print()
            
            print("="*100 + "\n")
    
    # Exit with error code if any queries failed
    failed_count = len(executor.get_tracker().get_failed_queries())
    if failed_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()

