#!/usr/bin/env python3
"""
Example usage of parallel query execution

This script demonstrates how to use the parallel query execution system.
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parallel.parallel_query_api import ParallelQueryAPI, run_parallel


def example_simple():
    """Simple example using the convenience function"""
    print("="*80)
    print("Example 1: Simple Parallel Execution")
    print("="*80)
    
    queries = [
        "SELECT 1 as test1, 'Hello' as message1",
        "SELECT 2 as test2, 'World' as message2",
        "SELECT 3 as test3, 'Parallel' as message3"
    ]
    
    results = run_parallel(queries, max_workers=3)
    
    print("\nResults:")
    for query_id, result in results.items():
        print(f"  {query_id}: {result}")
    print()


def example_advanced():
    """Advanced example using the API class"""
    print("="*80)
    print("Example 2: Advanced Usage with Status Tracking")
    print("="*80)
    
    api = ParallelQueryAPI(max_workers=3, timeout_seconds=60)
    
    queries = [
        "SELECT 1 as num, 'First' as label",
        "SELECT 2 as num, 'Second' as label",
        "SELECT 3 as num, 'Third' as label",
        "SELECT 4 as num, 'Fourth' as label",
        "SELECT 5 as num, 'Fifth' as label"
    ]
    
    print("\nRunning queries...")
    results = api.run_queries(queries)
    
    print("\nStatus Summary:")
    status = api.get_status()
    print(f"  Total: {status['total']}")
    print(f"  Completed: {status['completed']}")
    print(f"  Failed: {status['failed']}")
    
    print("\nDetailed Status:")
    api.print_status()
    
    print("\nResults:")
    for query_id, result in results.items():
        if result:
            print(f"  {query_id}: {len(result)} rows")
        else:
            print(f"  {query_id}: No results")
    print()


def example_with_files():
    """Example of running SQL files in parallel"""
    print("="*80)
    print("Example 3: Running SQL Files in Parallel")
    print("="*80)
    
    # This would work if you have SQL files
    # api = ParallelQueryAPI(max_workers=5)
    # 
    # sql_files = [
    #     'query1.sql',
    #     'query2.sql',
    #     'query3.sql'
    # ]
    # 
    # results = api.run_files(sql_files)
    # api.print_status()
    
    print("Note: This example requires SQL files to exist.")
    print("Usage: api.run_files(['file1.sql', 'file2.sql'])")
    print()


if __name__ == "__main__":
    print("\n" + "="*80)
    print("PARALLEL QUERY EXECUTION EXAMPLES")
    print("="*80 + "\n")
    
    try:
        example_simple()
        example_advanced()
        example_with_files()
        
        print("="*80)
        print("Examples completed successfully!")
        print("="*80 + "\n")
        
    except Exception as e:
        print(f"\nError running examples: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

