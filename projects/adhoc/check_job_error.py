#!/usr/bin/env python3
"""Check job error details"""
import sys
import os

cursor_databricks_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_root)

from databricks_api import DatabricksAPI

db = DatabricksAPI()
run_id = 491787225905714

print("Checking job run details...")
status = db.get_job_status(run_id=run_id)
print(f"\nStatus: {status}")






