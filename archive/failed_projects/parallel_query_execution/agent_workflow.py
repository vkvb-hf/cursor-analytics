#!/usr/bin/env python3
"""
Agent Workflow - Submit queries and check status (non-blocking)

Usage:
    # Submit queries
    python agent_workflow.py submit
    
    # Check status (non-blocking, can run multiple times)
    python agent_workflow.py check
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
STATUS_FILE = Path('/tmp/databricks_query_daemon/status.json')
REQUEST_DIR.mkdir(parents=True, exist_ok=True)

def submit_queries(queries, query_ids):
    """Submit queries to daemon (fast, non-blocking)"""
    start = time.time()
    
    for query, query_id in zip(queries, query_ids):
        request_file = REQUEST_DIR / f"{query_id}_{int(time.time() * 1000000)}.json"
        request = {
            'query_id': query_id,
            'query': query,
            'metadata': {},
            'submitted_at': datetime.now().isoformat()
        }
        with open(request_file, 'w') as f:
            json.dump(request, f)
    
    elapsed = time.time() - start
    return query_ids, elapsed

def check_status():
    """Check status and results (non-blocking file reads)"""
    # Check daemon status
    daemon_status = {}
    if STATUS_FILE.exists():
        with open(STATUS_FILE, 'r') as f:
            daemon_status = json.load(f)
    
    # Check for result files
    results = {}
    if RESULT_DIR.exists():
        for result_file in RESULT_DIR.glob('*.json'):
            query_id = result_file.stem
            with open(result_file, 'r') as f:
                results[query_id] = json.load(f)
    
    return daemon_status, results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python agent_workflow.py [submit|check]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "submit":
        query1 = """SELECT dd.iso_year_week, COUNT(DISTINCT a.customer_id) as total_customers, COUNT(DISTINCT CASE WHEN be.event_checkout_success > 0 THEN a.customer_id END) as successful_checkout, ROUND(COUNT(DISTINCT CASE WHEN be.event_checkout_success > 0 THEN a.customer_id END) * 100.0 / COUNT(DISTINCT a.customer_id), 2) as checkout_success_rate FROM payments_hf.checkout_customer_actuals a JOIN dimensions.date_dimension dd ON DATE(a.checkout_date) = DATE(dd.date_string_backwards) LEFT JOIN payments_hf.checkout_funnel_backend be ON a.business_unit = be.country AND a.customer_id = be.customer_id AND DATE(a.checkout_date) = DATE(be.event_date) WHERE a.channel = '' AND a.is_actual = true AND a.is_in_morpheus = false AND a.checkout_date >= '2025-01-01' GROUP BY dd.iso_year_week ORDER BY dd.iso_year_week"""
        query2 = "SELECT * FROM payments_hf.checkout_funnel_backend LIMIT 5"
        
        query_ids, elapsed = submit_queries([query1, query2], ["checkout_analysis", "sample_data"])
        
        print(json.dumps({
            'action': 'submitted',
            'query_ids': query_ids,
            'elapsed_ms': elapsed * 1000,
            'message': 'Queries submitted to daemon'
        }, indent=2))
    
    elif command == "check":
        daemon_status, results = check_status()
        
        output = {
            'daemon_status': daemon_status.get('status', 'unknown'),
            'queries': daemon_status.get('queries', {}),
            'results_ready': list(results.keys()),
            'results': results
        }
        
        print(json.dumps(output, indent=2, default=str))
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

