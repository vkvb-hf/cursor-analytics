#!/usr/bin/env python3
"""
CLI script to run SQL queries against Databricks
Usage: python scripts/run_sql.py <sql_file> [output_format] [limit]
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.run_sql_file import run_sql_file

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/run_sql.py <sql_file> [output_format] [limit]")
        print("Example: python scripts/run_sql.py queries/my_query.sql csv 1000")
        sys.exit(1)
    
    sql_file = sys.argv[1]
    output_format = sys.argv[2] if len(sys.argv) > 2 else "show"
    limit = int(sys.argv[3]) if len(sys.argv) > 3 else 100
    
    run_sql_file(sql_file, output_format, limit)


