#!/usr/bin/env python3
"""
Test the Agent Background API - Demonstrates non-blocking behavior

This shows how agents can submit queries without blocking the chat interface.
"""
import sys
import os
import time

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parallel.agent_background_api import submit_and_continue, get_api


def test_non_blocking():
    """Test that queries can be submitted without blocking"""
    
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
    
    print("="*100)
    print("TESTING NON-BLOCKING QUERY SUBMISSION")
    print("="*100)
    
    # Submit queries - this should return in <0.1s
    start_time = time.time()
    query_ids = submit_and_continue(
        queries=[query1, query2],
        query_ids=["checkout_analysis", "sample_data"]
    )
    submit_time = time.time() - start_time
    
    print(f"\n✓ Queries submitted in {submit_time:.3f} seconds")
    print(f"  Query IDs: {', '.join(query_ids)}")
    print("\n" + "="*100)
    print("CONTROL RETURNED IMMEDIATELY - CHAT INTERFACE STAYS RESPONSIVE")
    print("="*100)
    print("\nQueries are running in background.")
    print("You can continue working or check status later.\n")
    
    # Show that we can check status immediately (non-blocking)
    api = get_api()
    status = api.get_status()
    print(f"Current status: {status['running']} running, {status['pending']} pending")
    
    return query_ids


if __name__ == "__main__":
    test_non_blocking()
    # Script exits here - queries continue in background
    # Chat interface is no longer locked!

