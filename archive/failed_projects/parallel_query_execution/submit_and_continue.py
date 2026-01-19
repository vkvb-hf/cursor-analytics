#!/usr/bin/env python3
"""
Submit Queries and Continue - Demonstrates true non-blocking execution

This script submits queries and returns immediately, allowing you to continue working.
Results can be checked later.
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parallel.background_executor import get_background_executor


def submit_queries():
    """Submit queries and return immediately"""
    
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
    
    # Get executor
    executor = get_background_executor(max_workers=2)
    
    # Submit queries (returns immediately!)
    query_ids = executor.submit_queries(
        queries=[query1, query2],
        query_ids=["checkout_analysis", "sample_data"]
    )
    
    print("="*100)
    print("QUERIES SUBMITTED - RETURNING IMMEDIATELY")
    print("="*100)
    print(f"\nQuery IDs: {', '.join(query_ids)}")
    print("\nQueries are running in the background.")
    print("You can continue working or check status later with:")
    print(f"  python parallel/run_background_queries.py --status")
    print(f"  python parallel/run_background_queries.py --results {' '.join(query_ids)}")
    print("="*100 + "\n")
    
    # Return immediately - don't wait!
    return query_ids


if __name__ == "__main__":
    submit_queries()
    # Script exits here - queries continue running in background!

