#!/usr/bin/env python3
"""
Submit Query to Daemon - Fast file-based submission

This script writes a request file to the daemon. It's fast because it's just file I/O,
no Python imports, no database connections - just writing a JSON file!
"""
import sys
import os
import json
import time
from pathlib import Path
from datetime import datetime

# Daemon directories
DAEMON_DIR = Path('/tmp/databricks_query_daemon')
REQUEST_DIR = DAEMON_DIR / 'requests'
REQUEST_DIR.mkdir(parents=True, exist_ok=True)

def submit_to_daemon(query, query_id, metadata=None):
    """Submit query to daemon via file (fast, non-blocking!)"""
    request_file = REQUEST_DIR / f"{query_id}_{int(time.time() * 1000000)}.json"
    
    request = {
        'query_id': query_id,
        'query': query,
        'metadata': metadata or {},
        'submitted_at': datetime.now().isoformat()
    }
    
    with open(request_file, 'w') as f:
        json.dump(request, f)
    
    return str(request_file)

if __name__ == "__main__":
    # Your queries
    query1 = """SELECT dd.iso_year_week, COUNT(DISTINCT a.customer_id) as total_customers, COUNT(DISTINCT CASE WHEN be.event_checkout_success > 0 THEN a.customer_id END) as successful_checkout, ROUND(COUNT(DISTINCT CASE WHEN be.event_checkout_success > 0 THEN a.customer_id END) * 100.0 / COUNT(DISTINCT a.customer_id), 2) as checkout_success_rate FROM payments_hf.checkout_customer_actuals a JOIN dimensions.date_dimension dd ON DATE(a.checkout_date) = DATE(dd.date_string_backwards) LEFT JOIN payments_hf.checkout_funnel_backend be ON a.business_unit = be.country AND a.customer_id = be.customer_id AND DATE(a.checkout_date) = DATE(be.event_date) WHERE a.channel = '' AND a.is_actual = true AND a.is_in_morpheus = false AND a.checkout_date >= '2025-01-01' GROUP BY dd.iso_year_week ORDER BY dd.iso_year_week"""
    query2 = "SELECT * FROM payments_hf.checkout_funnel_backend LIMIT 5"
    
    start = time.time()
    submit_to_daemon(query1, "checkout_analysis")
    submit_to_daemon(query2, "sample_data")
    elapsed = time.time() - start
    
    print(f"Submitted to daemon in {elapsed*1000:.3f}ms")
    sys.exit(0)

