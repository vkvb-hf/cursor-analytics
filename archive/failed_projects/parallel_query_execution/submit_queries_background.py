#!/usr/bin/env python3
"""
Submit Queries to Background - Exits immediately after submission

This script submits queries and exits immediately, so terminal commands don't block.
The queries continue running in background threads.
"""
import sys
import os
import time
import atexit

# Add path
sys.path.insert(0, '/Users/visal.kumar/Documents/databricks/cursor_databricks')

print("="*100)
print("🔄 SUBMITTING QUERIES TO RUN IN BACKGROUND")
print("="*100)

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
    
    # Submit queries
    query_ids = submit_and_continue(
        queries=[query1, query2],
        query_ids=["checkout_analysis", "sample_data"]
    )
    
    submit_time = time.time() - start_time
    
    # Get initial status
    api = get_api()
    status = api.get_status()
    
    print(f"\n✅ Queries submitted in {submit_time:.3f}s")
    print(f"📋 Query IDs: {', '.join(query_ids)}")
    print(f"📊 Status: {status['running']} running, {status['pending']} pending")
    print(f"\n🔄 QUERIES ARE NOW RUNNING IN THE BACKGROUND")
    print(f"   The script will exit now, but queries continue executing.")
    print(f"\n💡 To check results later:")
    print(f"   python parallel/run_background_queries.py --results {' '.join(query_ids)}")
    print("="*100)
    
    # CRITICAL: Don't wait, exit immediately!
    # The background executor threads will continue running
    # They are not daemon threads, so they'll complete even after script exits
    sys.exit(0)
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

