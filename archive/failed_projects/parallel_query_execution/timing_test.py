#!/usr/bin/env python3
"""
Timing Test - Measure query submission speed

Tests how fast query submission is to verify it's truly non-blocking.
"""
import sys
import os
import time
from datetime import datetime

# Add path
sys.path.insert(0, '/Users/visal.kumar/Documents/databricks/cursor_databricks')

print("="*100)
print("TIMING TEST - Query Submission Speed")
print("="*100)

# Timestamp BEFORE submission
timestamp_before = time.time()
datetime_before = datetime.now()

print(f"\n⏰ TIMESTAMP BEFORE SUBMISSION:")
print(f"   Unix timestamp: {timestamp_before:.6f}")
print(f"   Human readable: {datetime_before.strftime('%Y-%m-%d %H:%M:%S.%f')}")
print(f"\n🔄 SUBMITTING QUERIES NOW...\n")

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
    
    # Timestamp AFTER submission
    timestamp_after = time.time()
    datetime_after = datetime.now()
    
    # Calculate elapsed time
    elapsed_time = timestamp_after - timestamp_before
    
    print("="*100)
    print("⏰ TIMESTAMP AFTER SUBMISSION:")
    print(f"   Unix timestamp: {timestamp_after:.6f}")
    print(f"   Human readable: {datetime_after.strftime('%Y-%m-%d %H:%M:%S.%f')}")
    print(f"\n📊 TIMING RESULTS:")
    print(f"   Elapsed time: {elapsed_time:.6f} seconds")
    print(f"   Elapsed time: {elapsed_time * 1000:.3f} milliseconds")
    print(f"\n✅ Queries submitted successfully!")
    print(f"   Query IDs: {', '.join(query_ids)}")
    
    # Get status
    api = get_api()
    status = api.get_status()
    print(f"   Status: {status['running']} running, {status['pending']} pending")
    
    print(f"\n{'='*100}")
    print("ANALYSIS:")
    print(f"{'='*100}")
    if elapsed_time < 0.1:
        print(f"✅ EXCELLENT: Submission took {elapsed_time*1000:.1f}ms (< 100ms)")
        print("   This is fast enough to feel instant!")
    elif elapsed_time < 0.5:
        print(f"✅ GOOD: Submission took {elapsed_time*1000:.1f}ms (< 500ms)")
        print("   This is acceptable for background submission")
    elif elapsed_time < 1.0:
        print(f"⚠️  SLOW: Submission took {elapsed_time*1000:.1f}ms (< 1s)")
        print("   This might feel slightly delayed")
    else:
        print(f"❌ TOO SLOW: Submission took {elapsed_time*1000:.1f}ms (> 1s)")
        print("   This is blocking the chat interface too long")
    
    print(f"\n💡 Note: Queries are now running in background threads.")
    print(f"   The chat interface was blocked only for {elapsed_time*1000:.1f}ms")
    print(f"   (not for the full query execution time)")
    print("="*100)
    
    # Exit immediately
    sys.exit(0)
    
except ImportError as e:
    print(f"\n❌ Import Error: {e}")
    timestamp_after = time.time()
    elapsed_time = timestamp_after - timestamp_before
    print(f"   (Even with error, elapsed: {elapsed_time:.6f}s)")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ Error: {e}")
    timestamp_after = time.time()
    elapsed_time = timestamp_after - timestamp_before
    print(f"   (Even with error, elapsed: {elapsed_time:.6f}s)")
    import traceback
    traceback.print_exc()
    sys.exit(1)

