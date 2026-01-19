#!/usr/bin/env python3
"""
Run Multiple SQL Files in Parallel

A convenient wrapper for running SQL files in parallel with better file handling.

Usage:
    python run_parallel_sql_files.py query1.sql query2.sql query3.sql
    python run_parallel_sql_files.py *.sql --max-workers 10
    python run_parallel_sql_files.py queries/*.sql --output-dir results/
"""
import sys
import os
import argparse
import time
from pathlib import Path
import json

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parallel.parallel_executor import ParallelQueryExecutor
from core.query_util import print_table


def save_results_to_file(query_id: str, result: Any, output_dir: str, format: str = 'json'):
    """Save query results to file"""
    output_dir_path = Path(output_dir)
    output_dir_path.mkdir(parents=True, exist_ok=True)
    
    if format == 'json':
        output_path = output_dir_path / f"{query_id}_results.json"
        import pandas as pd
        df = pd.DataFrame(result)
        df.to_json(output_path, orient='records', indent=2)
    elif format == 'csv':
        output_path = output_dir_path / f"{query_id}_results.csv"
        import pandas as pd
        df = pd.DataFrame(result)
        df.to_csv(output_path, index=False)
    else:
        return None
    
    return str(output_path)


def main():
    parser = argparse.ArgumentParser(
        description='Execute multiple SQL files in parallel',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run multiple SQL files
  python run_parallel_sql_files.py query1.sql query2.sql query3.sql
  
  # Run all SQL files in current directory
  python run_parallel_sql_files.py *.sql
  
  # Run with custom settings
  python run_parallel_sql_files.py *.sql --max-workers 10 --timeout 600
  
  # Save results to files
  python run_parallel_sql_files.py *.sql --output-dir results/ --output-format csv
        """
    )
    
    parser.add_argument('files', nargs='+',
                       help='SQL file paths (supports glob patterns)')
    parser.add_argument('--max-workers', type=int, default=5,
                       help='Maximum number of concurrent queries (default: 5)')
    parser.add_argument('--timeout', type=int, default=300,
                       help='Timeout per query in seconds (default: 300)')
    parser.add_argument('--status-interval', type=float, default=5.0,
                       help='Print status updates every N seconds (default: 5.0)')
    parser.add_argument('--output-dir', type=str, default=None,
                       help='Directory to save query results (default: disabled)')
    parser.add_argument('--output-format', choices=['json', 'csv'], default='json',
                       help='Output format for saved results (default: json)')
    parser.add_argument('--show-results', action='store_true',
                       help='Display query results in terminal')
    parser.add_argument('--show-limit', type=int, default=20,
                       help='Limit rows shown per query (default: 20)')
    
    args = parser.parse_args()
    
    # Expand glob patterns
    import glob
    all_files = []
    for pattern in args.files:
        matched = glob.glob(pattern)
        if matched:
            all_files.extend(matched)
        else:
            # If no match, treat as literal file path
            if os.path.exists(pattern):
                all_files.append(pattern)
            else:
                print(f"Warning: File/pattern not found: {pattern}")
    
    if not all_files:
        print("Error: No SQL files found")
        sys.exit(1)
    
    # Filter to only SQL files
    sql_files = [f for f in all_files if f.endswith('.sql')]
    
    if not sql_files:
        print("Error: No .sql files found")
        sys.exit(1)
    
    print("="*100)
    print("PARALLEL SQL FILE EXECUTOR")
    print("="*100)
    print(f"Files to execute: {len(sql_files)}")
    print(f"Max workers: {args.max_workers}")
    print(f"Timeout: {args.timeout}s")
    if args.output_dir:
        print(f"Output directory: {args.output_dir}")
    print("="*100 + "\n")
    
    # Create executor
    executor = ParallelQueryExecutor(
        max_workers=args.max_workers,
        timeout_seconds=args.timeout
    )
    
    # Execute queries
    start_time = time.time()
    
    print(f"Executing {len(sql_files)} SQL files in parallel...\n")
    results = executor.execute_query_files(
        file_paths=sql_files,
        wait_for_completion=True
    )
    
    # Monitor status
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
    
    # Wait for completion
    executor.wait_for_all()
    total_time = time.time() - start_time
    
    print(f"\n✓ All queries completed in {total_time:.2f}s\n")
    
    # Print final status
    executor.print_status()
    
    # Process results
    tracker = executor.get_tracker()
    completed = tracker.get_completed_queries()
    failed = tracker.get_failed_queries()
    
    # Save results if requested
    if args.output_dir and completed:
        print(f"\nSaving results to {args.output_dir}...")
        saved_files = []
        for query_info in completed:
            if query_info.result:
                saved_path = save_results_to_file(
                    query_info.query_id,
                    query_info.result,
                    args.output_dir,
                    format=args.output_format
                )
                if saved_path:
                    saved_files.append(saved_path)
        
        print(f"✓ Saved {len(saved_files)} result files")
        for path in saved_files:
            print(f"  - {path}")
    
    # Show results if requested
    if args.show_results and completed:
        print("\n" + "="*100)
        print("QUERY RESULTS")
        print("="*100)
        
        for query_info in completed:
            filename = query_info.metadata.get('filename', query_info.query_id)
            print(f"\n[{filename}]")
            print("-"*100)
            
            if query_info.result:
                # Get column names from result structure
                column_names = None
                if query_info.result and len(query_info.result) > 0:
                    first_row = query_info.result[0]
                    if hasattr(first_row, '_fields'):
                        column_names = list(first_row._fields)
                    elif hasattr(first_row, '__dict__'):
                        column_names = [k for k in first_row.__dict__.keys() if not k.startswith('_')]
                
                print_table(
                    query_info.result,
                    column_names=column_names,
                    limit=args.show_limit,
                    title=f"Results from {filename}"
                )
            else:
                print("No results returned")
            
            print()
        
        print("="*100 + "\n")
    
    # Print summary
    print("\n" + "="*100)
    print("EXECUTION SUMMARY")
    print("="*100)
    print(f"✅ Completed: {len(completed)}")
    print(f"❌ Failed: {len(failed)}")
    
    if completed:
        total_duration = sum(q.duration_seconds or 0 for q in completed)
        avg_duration = total_duration / len(completed) if completed else 0
        total_rows = sum(q.result_count or 0 for q in completed)
        print(f"\nTotal execution time: {total_time:.2f}s")
        print(f"Average query duration: {avg_duration:.2f}s")
        print(f"Total rows returned: {total_rows:,}")
    
    if failed:
        print("\nFailed queries:")
        for query_info in failed:
            filename = query_info.metadata.get('filename', query_info.query_id)
            print(f"  ❌ {filename}: {query_info.error}")
    
    print("="*100 + "\n")
    
    # Exit with error code if any queries failed
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()

