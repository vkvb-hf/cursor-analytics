#!/usr/bin/env python3
"""
Test Background Execution - Submit queries and return immediately
"""
import sys
import os
import time

# Add path
sys.path.insert(0, '/Users/visal.kumar/Documents/databricks/cursor_databricks')

print("="*100)
print("TESTING BACKGROUND QUERY EXECUTION")
print("="*100)
print("\n🔄 SUBMITTING QUERIES TO RUN IN BACKGROUND...")
print("   (This should return immediately, chat interface stays responsive)\n")

start_time = time.time()

try:
    from parallel.agent_background_api import submit_and_continue, get_api
    
    # Your queries
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
    
    # Submit queries - should return immediately!
    query_ids = submit_and_continue(
        queries=[query1, query2],
        query_ids=["checkout_analysis", "sample_data"]
    )
    
    submit_time = time.time() - start_time
    
    print("="*100)
    print("✅ QUERIES SUBMITTED TO BACKGROUND")
    print("="*100)
    print(f"\n⏱️  Submission time: {submit_time:.3f} seconds (should be <0.1s)")
    print(f"📋 Query IDs: {', '.join(query_ids)}")
    print(f"\n🔄 QUERIES ARE NOW RUNNING IN THE BACKGROUND")
    print(f"   - Executing concurrently in background threads")
    print(f"   - Chat interface stays responsive")
    print(f"   - You can continue working immediately")
    
    # Check initial status
    api = get_api()
    status = api.get_status()
    print(f"\n📊 Current Status:")
    print(f"   Total: {status['total']}")
    print(f"   Running: {status['running']}")
    print(f"   Pending: {status['pending']}")
    print(f"   Completed: {status['completed']}")
    
    print("\n" + "="*100)
    print("✅ TEST SUCCESSFUL - Queries submitted to background!")
    print("   Chat interface is responsive - you can continue working.")
    print("="*100)
    print("\n💡 To check results later, use:")
    print(f"   python parallel/run_background_queries.py --results {' '.join(query_ids)}")
    print("="*100 + "\n")
    
except ImportError as e:
    print(f"\n❌ Import Error: {e}")
    print("Make sure virtual environment is activated and dependencies are installed")
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()

