#!/usr/bin/env python3
"""
Quick Submit - Minimal overhead query submission

This script minimizes overhead by:
- Using minimal imports
- Exiting immediately after submission
- No status checks or printing
"""
import sys
import os

# Minimal path setup
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import only what's needed
from parallel.agent_background_api import submit_and_continue

# Queries
query1 = """SELECT dd.iso_year_week, COUNT(DISTINCT a.customer_id) as total_customers, COUNT(DISTINCT CASE WHEN be.event_checkout_success > 0 THEN a.customer_id END) as successful_checkout, ROUND(COUNT(DISTINCT CASE WHEN be.event_checkout_success > 0 THEN a.customer_id END) * 100.0 / COUNT(DISTINCT a.customer_id), 2) as checkout_success_rate FROM payments_hf.checkout_customer_actuals a JOIN dimensions.date_dimension dd ON DATE(a.checkout_date) = DATE(dd.date_string_backwards) LEFT JOIN payments_hf.checkout_funnel_backend be ON a.business_unit = be.country AND a.customer_id = be.customer_id AND DATE(a.checkout_date) = DATE(be.event_date) WHERE a.channel = '' AND a.is_actual = true AND a.is_in_morpheus = false AND a.checkout_date >= '2025-01-01' GROUP BY dd.iso_year_week ORDER BY dd.iso_year_week"""
query2 = "SELECT * FROM payments_hf.checkout_funnel_backend LIMIT 5"

# Submit and exit immediately
submit_and_continue([query1, query2], ["checkout_analysis", "sample_data"])
sys.exit(0)

