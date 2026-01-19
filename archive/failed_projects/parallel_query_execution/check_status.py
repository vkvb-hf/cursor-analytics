#!/usr/bin/env python3
"""
Check Query Status - Non-blocking status check

This script reads the daemon status file - it's just reading a file, very fast!
"""
import sys
import json
from pathlib import Path

STATUS_FILE = Path('/tmp/databricks_query_daemon/status.json')

if STATUS_FILE.exists():
    with open(STATUS_FILE, 'r') as f:
        status = json.load(f)
    print(json.dumps(status, indent=2))
else:
    print('{"status": "daemon_not_running"}')

