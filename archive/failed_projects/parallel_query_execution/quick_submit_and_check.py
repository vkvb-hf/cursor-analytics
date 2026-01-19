#!/usr/bin/env python3
"""
Quick Submit and Check - Submit queries, check once, return immediately

This submits queries and does ONE quick check. If results aren't ready,
it returns anyway (non-blocking). You can check again later.
"""
import sys
import os
import json
import time
from pathlib import Path
from datetime import datetime

sys.path.insert(0, '/Users/visal.kumar/Documents/databricks/cursor_databricks')

REQUEST_DIR = Path('/tmp/databricks_query_daemon/requests')
RESULT_DIR = Path('/tmp/databricks_query_daemon/results')
REQUEST_DIR.mkdir(parents=True, exist_ok=True)

def submit_query(query, query_id):
    """Submit query to daemon (fast, non-blocking)"""
    request_file = REQUEST_DIR / f"{query_id}_{int(time.time() * 1000000)}.json"
    request = {
        'query_id': query_id,
        'query': query,
        'metadata': {},
        'submitted_at': datetime.now().isoformat()
    }
    with open(request_file, 'w') as f:
        json.dump(request, f)
    return query_id

def quick_check(query_ids):
    """Quick check for results (non-blocking file read)"""
    results = {}
    for query_id in query_ids:
        result_file = RESULT_DIR / f"{query_id}.json"
        if result_file.exists():
            with open(result_file, 'r') as f:
                results[query_id] = json.load(f)
    return results

if __name__ == "__main__":
    query1 = """SELECT dd.iso_year_week, COUNT(DISTINCT a.customer_id) as total_customers, COUNT(DISTINCT CASE WHEN be.event_checkout_success > 0 THEN a.customer_id END) as successful_checkout, ROUND(COUNT(DISTINCT CASE WHEN be.event_checkout_success > 0 THEN a.customer_id END) * 100.0 / COUNT(DISTINCT a.customer_id), 2) as checkout_success_rate FROM payments_hf.checkout_customer_actuals a JOIN dimensions.date_dimension dd ON DATE(a.checkout_date) = DATE(dd.date_string_backwards) LEFT JOIN payments_hf.checkout_funnel_backend be ON a.business_unit = be.country AND a.customer_id = be.customer_id AND DATE(a.checkout_date) = DATE(be.event_date) WHERE a.channel = '' AND a.is_actual = true AND a.is_in_morpheus = false AND a.checkout_date >= '2025-01-01' GROUP BY dd.iso_year_week ORDER BY dd.iso_year_week"""
    query2 = "SELECT * FROM payments_hf.checkout_funnel_backend LIMIT 5"
    
    query_ids = ["checkout_analysis", "sample_data"]
    
    # Submit (fast)
    start = time.time()
    for query, qid in zip([query1, query2], query_ids):
        submit_query(query, qid)
    submit_time = time.time() - start
    
    print(f"Submitted in {submit_time*1000:.1f}ms")
    
    # Quick check after 5 seconds (non-blocking)
    time.sleep(5)
    results = quick_check(query_ids)
    
    if results:
        print("Some results ready!")
        for qid, result in results.items():
            print(f"  {qid}: {result.get('status')}")
    else:
        print("Results not ready yet (will check again later)")
    
    # Exit immediately - don't block!
    sys.exit(0)

