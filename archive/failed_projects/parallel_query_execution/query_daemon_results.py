#!/usr/bin/env python3
"""
Query Daemon Results - Get results from daemon's executor

This connects to the daemon's executor to get query results.
"""
import sys
import os
import json
from pathlib import Path

sys.path.insert(0, '/Users/visal.kumar/Documents/databricks/cursor_databricks')

# The daemon uses a global executor, but we need to access it
# Since daemon is in separate process, we'll use the status file
# and try to get results from the executor if possible

from parallel.agent_background_api import get_api

api = get_api()
executor = api.executor
tracker = executor.get_tracker()

# Get all queries
all_queries = tracker.get_all_queries()

if not all_queries:
    print("No queries found in current executor instance.")
    print("Note: Daemon runs in separate process with its own executor.")
    print("Results should be written to /tmp/databricks_query_daemon/results/")
    sys.exit(0)

print(f"Found {len(all_queries)} queries in executor:\n")

for q in all_queries:
    print(f"[{q.query_id}]")
    print(f"  Status: {q.status.value}")
    if q.duration_seconds:
        print(f"  Duration: {q.duration_seconds:.2f}s")
    if q.result_count is not None:
        print(f"  Rows: {q.result_count:,}")
    if q.error:
        print(f"  Error: {q.error}")
    
    if q.result and len(q.result) > 0:
        print(f"  Results ({len(q.result)} rows):")
        # Show first few rows
        for i, row in enumerate(q.result[:5]):
            if hasattr(row, '_fields'):
                # Databricks Row object
                row_dict = {col: getattr(row, col) for col in row._fields}
                print(f"    Row {i+1}: {row_dict}")
            elif isinstance(row, (list, tuple)):
                print(f"    Row {i+1}: {list(row)}")
            else:
                print(f"    Row {i+1}: {row}")
        if len(q.result) > 5:
            print(f"    ... ({len(q.result) - 5} more rows)")
    print()

