#!/usr/bin/env python3
"""
Submit and Wait - Submit queries and poll for results

Submits queries to daemon, then checks for results every 5 seconds,
up to 100 retries (max 500 seconds = ~8 minutes).
"""
import sys
import os
import json
import time
from pathlib import Path
from datetime import datetime

sys.path.insert(0, '/Users/visal.kumar/Documents/databricks/cursor_databricks')

# Daemon directories
REQUEST_DIR = Path('/tmp/databricks_query_daemon/requests')
RESULT_DIR = Path('/tmp/databricks_query_daemon/results')
REQUEST_DIR.mkdir(parents=True, exist_ok=True)

def submit_query(query, query_id, metadata=None):
    """Submit query to daemon"""
    request_file = REQUEST_DIR / f"{query_id}_{int(time.time() * 1000000)}.json"
    
    request = {
        'query_id': query_id,
        'query': query,
        'metadata': metadata or {},
        'submitted_at': datetime.now().isoformat()
    }
    
    with open(request_file, 'w') as f:
        json.dump(request, f)
    
    return query_id

def check_result(query_id):
    """Check if result file exists and return it"""
    result_file = RESULT_DIR / f"{query_id}.json"
    
    if result_file.exists():
        with open(result_file, 'r') as f:
            return json.load(f)
    return None

def submit_and_wait(queries, query_ids, max_retries=100, wait_seconds=5):
    """Submit queries and wait for results"""
    
    print("="*100)
    print("SUBMITTING QUERIES TO DAEMON")
    print("="*100)
    
    # Submit all queries
    submitted_ids = []
    for query, query_id in zip(queries, query_ids):
        submit_query(query, query_id)
        submitted_ids.append(query_id)
        print(f"✅ Submitted: {query_id}")
    
    print(f"\n🔄 Waiting for results (checking every {wait_seconds}s, max {max_retries} retries)...")
    print("="*100)
    
    # Wait and check for results
    results = {}
    completed = set()
    
    for attempt in range(1, max_retries + 1):
        time.sleep(wait_seconds)
        
        print(f"\n[Attempt {attempt}/{max_retries}] Checking results...")
        
        for query_id in submitted_ids:
            if query_id in completed:
                continue
            
            result = check_result(query_id)
            
            if result:
                results[query_id] = result
                completed.add(query_id)
                
                if result.get('status') == 'completed':
                    rows = result.get('result_count', 0)
                    duration = result.get('duration_seconds', 0)
                    print(f"  ✅ {query_id}: Completed ({duration:.2f}s, {rows:,} rows)")
                elif result.get('status') == 'failed':
                    error = result.get('error', 'Unknown error')
                    print(f"  ❌ {query_id}: Failed - {error}")
        
        # Check if all done
        if len(completed) == len(submitted_ids):
            print(f"\n✅ All queries completed!")
            break
        
        # Show progress
        remaining = len(submitted_ids) - len(completed)
        print(f"  ⏳ Still waiting for {remaining} query/queries...")
    
    print("\n" + "="*100)
    print("FINAL RESULTS")
    print("="*100)
    
    if len(completed) == len(submitted_ids):
        print("✅ All queries completed successfully!")
    else:
        print(f"⚠️  {len(completed)}/{len(submitted_ids)} queries completed")
        print(f"   {len(submitted_ids) - len(completed)} query/queries may still be running")
    
    return results

if __name__ == "__main__":
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
    
    results = submit_and_wait(
        queries=[query1, query2],
        query_ids=["checkout_analysis", "sample_data"],
        max_retries=100,
        wait_seconds=5
    )
    
    # Print results
    print("\n" + "="*100)
    print("QUERY RESULTS")
    print("="*100)
    
    for query_id, result in results.items():
        print(f"\n[{query_id}]")
        print("-"*100)
        print(f"Status: {result.get('status')}")
        if result.get('status') == 'completed':
            print(f"Duration: {result.get('duration_seconds', 0):.2f}s")
            print(f"Rows: {result.get('result_count', 0):,}")
            
            # Show first few rows
            result_data = result.get('result', [])
            if result_data:
                print(f"\nFirst {min(5, len(result_data))} rows:")
                for i, row in enumerate(result_data[:5]):
                    print(f"  Row {i+1}: {row}")
                if len(result_data) > 5:
                    print(f"  ... ({len(result_data) - 5} more rows)")
        elif result.get('status') == 'failed':
            print(f"Error: {result.get('error')}")
    
    print("\n" + "="*100)

