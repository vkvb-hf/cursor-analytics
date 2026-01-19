#!/usr/bin/env python3
"""
Daemon-style query submission - Runs in background process

This script submits queries and then runs as a daemon, allowing the terminal
command to return while queries continue executing.
"""
import sys
import os
import time
import signal
import atexit
from pathlib import Path

# Add path
sys.path.insert(0, '/Users/visal.kumar/Documents/databricks/cursor_databricks')

def daemonize():
    """Fork to background"""
    try:
        pid = os.fork()
        if pid > 0:
            # Parent process - exit immediately
            sys.exit(0)
    except OSError as e:
        print(f"Fork failed: {e}")
        sys.exit(1)
    
    # Child process continues
    os.setsid()
    os.umask(0)
    
    # Second fork
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as e:
        print(f"Second fork failed: {e}")
        sys.exit(1)

def main():
    """Main function - runs queries in background"""
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
        
        print(f"✅ Queries submitted: {', '.join(query_ids)}")
        print("🔄 Queries running in background daemon process")
        
        # Wait for queries to complete
        api = get_api()
        while True:
            status = api.get_status()
            if status['running'] == 0 and status['pending'] == 0:
                break
            time.sleep(1)
        
        print("✅ All queries completed")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--daemon":
        daemonize()
    
    # Write PID file
    pid_file = Path("/tmp/query_daemon.pid")
    pid_file.write_text(str(os.getpid()))
    
    # Register cleanup
    def cleanup():
        if pid_file.exists():
            pid_file.unlink()
    atexit.register(cleanup)
    
    main()

