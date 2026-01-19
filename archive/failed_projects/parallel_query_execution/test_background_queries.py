#!/usr/bin/env python3
"""
Test Background Query Execution

Tests the background query executor with the user's queries.
Queries run in background, allowing the agent to continue working.
"""
import sys
import os
import time
from typing import List

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parallel.background_executor import get_background_executor
from parallel.query_tracker import QueryStatus
from core.query_util import print_table


def test_background_execution():
    """Test background execution with user's queries"""
    
    # User's queries
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
    print("TESTING BACKGROUND QUERY EXECUTION")
    print("="*100)
    print("\nQuery 1: Complex checkout analysis query")
    print("Query 2: Simple LIMIT 5 query")
    print("\nSubmitting queries to run in background...\n")
    
    # Get background executor
    executor = get_background_executor(max_workers=2, timeout_seconds=300)
    
    # Track completion
    completed_queries = []
    
    def on_complete(query_id, result, result_count):
        """Callback when query completes"""
        completed_queries.append(query_id)
        print(f"\n{'='*100}")
        print(f"✅ QUERY COMPLETED IN BACKGROUND: {query_id}")
        print(f"   Rows returned: {result_count:,}")
        print(f"{'='*100}\n")
    
    def on_error(query_id, error):
        """Callback when query fails"""
        print(f"\n❌ QUERY FAILED: {query_id}")
        print(f"   Error: {error}\n")
    
    # Submit queries (non-blocking)
    start_time = time.time()
    query_ids = executor.submit_queries(
        queries=[query1, query2],
        query_ids=["checkout_analysis", "sample_data"],
        on_complete=on_complete,
        on_error=on_error
    )
    
    submit_time = time.time() - start_time
    print(f"✓ Queries submitted in {submit_time:.3f}s")
    print(f"  Query IDs: {', '.join(query_ids)}")
    print("\n" + "="*100)
    print("QUERIES ARE NOW RUNNING IN BACKGROUND")
    print("You can continue working while they execute!")
    print("="*100 + "\n")
    
    # Show initial status
    print("Initial Status:")
    executor.print_status()
    
    # Simulate doing other work
    print("\n" + "-"*100)
    print("Simulating other work while queries run...")
    print("-"*100)
    
    # Monitor progress
    check_interval = 2.0
    last_check = time.time()
    
    while True:
        running = executor.get_tracker().get_running_queries()
        pending = executor.get_tracker().get_pending_queries()
        
        # Check status periodically
        current_time = time.time()
        if current_time - last_check >= check_interval:
            print(f"\n[{time.strftime('%H:%M:%S')}] Checking query status...")
            status = executor.get_tracker().get_status_summary()
            print(f"  Running: {status['running']}, Completed: {status['completed']}, Failed: {status['failed']}")
            last_check = current_time
        
        # Check if all done
        if not running and not pending:
            break
        
        time.sleep(0.5)
    
    total_time = time.time() - start_time
    
    # Show final status
    print("\n" + "="*100)
    print("FINAL STATUS")
    print("="*100)
    executor.print_status()
    
    # Show results
    print("\n" + "="*100)
    print("QUERY RESULTS")
    print("="*100)
    
    for query_id in query_ids:
        query_info = executor.get_tracker().get_query(query_id)
        
        if query_info and query_info.status == QueryStatus.COMPLETED:
            print(f"\n[{query_id}]")
            print("-"*100)
            print(f"Duration: {query_info.duration_seconds:.2f}s")
            print(f"Rows: {query_info.result_count:,}")
            
            if query_info.result:
                # Get column names
                column_names = None
                if len(query_info.result) > 0:
                    first_row = query_info.result[0]
                    if hasattr(first_row, '_fields'):
                        column_names = list(first_row._fields)
                    elif hasattr(first_row, '__dict__'):
                        column_names = [k for k in first_row.__dict__.keys() if not k.startswith('_')]
                
                # Show results
                if query_id == "checkout_analysis":
                    print("\nCheckout Success Rate Analysis:")
                    print_table(
                        query_info.result,
                        column_names=column_names,
                        limit=None,
                        title="Checkout Analysis Results"
                    )
                elif query_id == "sample_data":
                    print("\nSample Data from checkout_funnel_backend:")
                    print_table(
                        query_info.result,
                        column_names=column_names,
                        limit=None,
                        title="Sample Data"
                    )
        
        elif query_info and query_info.status == QueryStatus.FAILED:
            print(f"\n[{query_id}]")
            print("-"*100)
            print(f"❌ FAILED: {query_info.error}")
    
    print("\n" + "="*100)
    print("EXECUTION SUMMARY")
    print("="*100)
    print(f"Total time: {total_time:.2f}s")
    print(f"Submit time: {submit_time:.3f}s")
    print(f"Execution time: {total_time - submit_time:.2f}s")
    
    status = executor.get_tracker().get_status_summary()
    print(f"\nCompleted: {status['completed']}")
    print(f"Failed: {status['failed']}")
    
    # Show individual timings
    all_queries = executor.get_tracker().get_all_queries()
    print("\nQuery Timings:")
    for q in all_queries:
        if q.duration_seconds:
            print(f"  {q.query_id}: {q.duration_seconds:.2f}s")
    
    print("="*100 + "\n")
    
    return query_ids


if __name__ == "__main__":
    try:
        print("\nStarting background query execution test...\n")
        query_ids = test_background_execution()
        print("✅ Test completed successfully!")
        print(f"\nYou can check results later using:")
        print(f"  python parallel/run_background_queries.py --results {' '.join(query_ids)}")
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

