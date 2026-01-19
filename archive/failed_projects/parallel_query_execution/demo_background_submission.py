#!/usr/bin/env python3
"""
Demo: Submit queries in background with clear communication
"""
import sys
import os

# Add path
sys.path.insert(0, '/Users/visal.kumar/Documents/databricks/cursor_databricks')

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
    
    print("="*100)
    print("SUBMITTING QUERIES TO RUN IN BACKGROUND")
    print("="*100)
    
    # Submit queries - returns immediately!
    query_ids = submit_and_continue(
        queries=[query1, query2],
        query_ids=["checkout_analysis", "sample_data"]
    )
    
    print(f"\n✅ Queries submitted successfully!")
    print(f"   Query IDs: {', '.join(query_ids)}")
    print(f"\n🔄 QUERIES ARE NOW RUNNING IN THE BACKGROUND")
    print(f"   - They will execute concurrently")
    print(f"   - Chat interface stays responsive")
    print(f"   - You can continue working immediately")
    print(f"\n📊 Current Status:")
    
    # Check initial status
    api = get_api()
    status = api.get_status()
    print(f"   Running: {status['running']}")
    print(f"   Pending: {status['pending']}")
    print(f"   Completed: {status['completed']}")
    
    print("\n" + "="*100)
    print("You can check status later or retrieve results when ready.")
    print("="*100)
    
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure you're in the correct directory with the virtual environment activated")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

