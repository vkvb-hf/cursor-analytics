#!/usr/bin/env python3
"""
Get Query Results - Retrieve results from daemon

This reads result files written by the daemon.
"""
import sys
import json
from pathlib import Path

RESULT_DIR = Path('/tmp/databricks_query_daemon/results')

query_id = sys.argv[1] if len(sys.argv) > 1 else None

if query_id:
    result_file = RESULT_DIR / f"{query_id}.json"
    if result_file.exists():
        with open(result_file, 'r') as f:
            result = json.load(f)
        print(json.dumps(result, indent=2))
    else:
        print(f'{"status": "not_ready", "query_id": "{query_id}"}')
else:
    # List all available results
    results = {}
    for result_file in RESULT_DIR.glob('*.json'):
        query_id = result_file.stem
        with open(result_file, 'r') as f:
            results[query_id] = json.load(f)
    print(json.dumps(results, indent=2))

