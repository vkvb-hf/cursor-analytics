#!/usr/bin/env python3
"""
Test script for parallel query execution
Tests two queries simultaneously and tracks output
"""
import sys
import os
import time
import threading

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parallel.parallel_query_api import ParallelQueryAPI
from core.query_util import print_table


def test_parallel_execution():
    """Test parallel execution with two queries"""
    
    # Define the two queries
    query1 = """
SELECT dd.iso_year_week, 
       COUNT(DISTINCT a.customer_id) as total_customers, 
       COUNT(DISTINCT CASE WHEN be.event_checkout_success > 0 THEN a.customer_id END) as successful_checkout, 
       ROUND(COUNT(DISTINCT CASE WHEN be.event_checkout_success > 0 THEN a.customer_id END) * 100.0 / COUNT(DISTINCT a.customer_id), 2) as checkout_success_rate 
FROM payments_hf.checkout_customer_actuals a 
JOIN dimensions.date_dimension dd ON DATE(a.checkout_date) = DATE(dd.date_string_backwards) 
LEFT JOIN payments_hf.checkout_funnel_backend be ON a.business_unit = be.country 
    AND a.customer_id = be.customer_id 
    AND DATE(a.checkout_date) = DATE(be.event_date) 
WHERE a.channel = '' 
    AND a.is_actual = true 
    AND a.is_in_morpheus = false 
    AND a.checkout_date >= '2025-01-01' 
GROUP BY dd.iso_year_week 
ORDER BY dd.iso_year_week
"""
    
    query2 = "SELECT * FROM payments_hf.checkout_funnel_backend LIMIT 5"
    
    print("="*100)
    print("TESTING PARALLEL QUERY EXECUTION")
    print("="*100)
    print("\nQuery 1: Complex checkout analysis query")
    print("Query 2: Simple LIMIT 5 query")
    print("\nStarting parallel execution...\n")
    
    # Create API instance
    api = ParallelQueryAPI(max_workers=2, timeout_seconds=300)
    
    # Track completion callbacks
    completed_queries = []
    completion_lock = threading.Lock()
    
    def on_query_complete(query_id, result, result_count):
        """Callback when a query completes"""
        with completion_lock:
            completed_queries.append(query_id)
            print(f"\n{'='*100}")
            print(f"✅ QUERY COMPLETED: {query_id}")
            print(f"   Rows returned: {result_count:,}")
            print(f"{'='*100}\n")
            
            # Process results immediately
            query_info = api.get_tracker().get_query(query_id)
            if query_info and query_info.result:
                print(f"Processing results for {query_id}...")
                
                if query_id == "query_1":
                    # Process the complex query results
                    print("\nCheckout Success Rate Analysis:")
                    print("-"*100)
                    if query_info.result:
                        # Get column names
                        column_names = None
                        if hasattr(query_info.result[0], '_fields'):
                            column_names = list(query_info.result[0]._fields)
                        elif hasattr(query_info.result[0], '__dict__'):
                            column_names = [k for k in query_info.result[0].__dict__.keys() if not k.startswith('_')]
                        
                        print_table(
                            query_info.result,
                            column_names=column_names,
                            limit=None,
                            title=f"Results from {query_id}"
                        )
                elif query_id == "query_2":
                    # Process the simple query results
                    print("\nSample Data from checkout_funnel_backend:")
                    print("-"*100)
                    if query_info.result:
                        column_names = None
                        if hasattr(query_info.result[0], '_fields'):
                            column_names = list(query_info.result[0]._fields)
                        elif hasattr(query_info.result[0], '__dict__'):
                            column_names = [k for k in query_info.result[0].__dict__.keys() if not k.startswith('_')]
                        
                        print_table(
                            query_info.result,
                            column_names=column_names,
                            limit=None,
                            title=f"Results from {query_id}"
                        )
                
                print(f"\n✓ Processed results for {query_id}\n")
    
    def on_query_error(query_id, error):
        """Callback when a query fails"""
        print(f"\n❌ QUERY FAILED: {query_id}")
        print(f"   Error: {error}\n")
    
    # Execute queries with custom IDs
    start_time = time.time()
    results = api.run_queries(
        queries=[query1, query2],
        query_ids=["query_1", "query_2"],
        wait=False  # Don't wait, we'll monitor manually
    )
    
    print("Queries submitted! Monitoring progress...\n")
    
    # Monitor status while queries run
    last_status_time = time.time()
    status_interval = 2.0  # Print status every 2 seconds
    
    while True:
        running = api.get_tracker().get_running_queries()
        pending = api.get_tracker().get_pending_queries()
        
        # Print status updates periodically
        current_time = time.time()
        if current_time - last_status_time >= status_interval:
            api.print_status()
            last_status_time = current_time
        
        # Check if all queries are done
        if not running and not pending:
            break
        
        time.sleep(0.5)  # Check every 500ms
    
    # Wait a bit more to ensure all callbacks are processed
    time.sleep(1)
    
    total_time = time.time() - start_time
    
    # Print final status
    print("\n" + "="*100)
    print("FINAL STATUS")
    print("="*100)
    api.print_status()
    
    # Print summary
    print("\n" + "="*100)
    print("EXECUTION SUMMARY")
    print("="*100)
    status = api.get_status()
    print(f"Total queries: {status['total']}")
    print(f"Completed: {status['completed']}")
    print(f"Failed: {status['failed']}")
    print(f"Total execution time: {total_time:.2f}s")
    
    # Show individual query timings
    all_queries = api.get_tracker().get_all_queries()
    print("\nQuery Timings:")
    for q in all_queries:
        if q.duration_seconds:
            print(f"  {q.query_id}: {q.duration_seconds:.2f}s")
    
    print("="*100 + "\n")
    
    # Return results
    return results


if __name__ == "__main__":
    try:
        results = test_parallel_execution()
        print("✅ Test completed successfully!")
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

