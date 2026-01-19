#!/usr/bin/env python3
"""
Persistent Submit - Uses file-based state to persist queries across processes

This allows queries to be submitted and tracked even when the process exits.
"""
import sys
import os
import json
import time
from pathlib import Path
from datetime import datetime

sys.path.insert(0, '/Users/visal.kumar/Documents/databricks/cursor_databricks')

# State file location
STATE_DIR = Path('/tmp/databricks_queries')
STATE_DIR.mkdir(exist_ok=True)
QUERIES_FILE = STATE_DIR / 'active_queries.json'

def load_queries():
    """Load active queries from file"""
    if QUERIES_FILE.exists():
        with open(QUERIES_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_queries(queries):
    """Save active queries to file"""
    with open(QUERIES_FILE, 'w') as f:
        json.dump(queries, f, indent=2)

def submit_query(query, query_id, metadata=None):
    """Submit a query and save to persistent state"""
    queries = load_queries()
    
    queries[query_id] = {
        'query': query,
        'status': 'pending',
        'submitted_at': datetime.now().isoformat(),
        'metadata': metadata or {}
    }
    
    save_queries(queries)
    
    # Now actually submit to background executor
    from parallel.agent_background_api import submit_and_continue
    submit_and_continue([query], [query_id])
    
    return query_id

if __name__ == "__main__":
    query1 = """SELECT dd.iso_year_week, COUNT(DISTINCT a.customer_id) as total_customers, COUNT(DISTINCT CASE WHEN be.event_checkout_success > 0 THEN a.customer_id END) as successful_checkout, ROUND(COUNT(DISTINCT CASE WHEN be.event_checkout_success > 0 THEN a.customer_id END) * 100.0 / COUNT(DISTINCT a.customer_id), 2) as checkout_success_rate FROM payments_hf.checkout_customer_actuals a JOIN dimensions.date_dimension dd ON DATE(a.checkout_date) = DATE(dd.date_string_backwards) LEFT JOIN payments_hf.checkout_funnel_backend be ON a.business_unit = be.country AND a.customer_id = be.customer_id AND DATE(a.checkout_date) = DATE(be.event_date) WHERE a.channel = '' AND a.is_actual = true AND a.is_in_morpheus = false AND a.checkout_date >= '2025-01-01' GROUP BY dd.iso_year_week ORDER BY dd.iso_year_week"""
    query2 = "SELECT * FROM payments_hf.checkout_funnel_backend LIMIT 5"
    
    start = time.time()
    submit_query(query1, "checkout_analysis")
    submit_query(query2, "sample_data")
    elapsed = time.time() - start
    
    print(f"Submitted in {elapsed*1000:.1f}ms")
    sys.exit(0)

