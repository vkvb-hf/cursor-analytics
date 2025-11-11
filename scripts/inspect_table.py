#!/usr/bin/env python3
"""
CLI script to inspect Databricks tables
Usage: python scripts/inspect_table.py <schema.table> [options]
"""
import sys
import os
import argparse
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.table_inspector import TableInspector

def main():
    parser = argparse.ArgumentParser(description='Inspect a Databricks table')
    parser.add_argument('table', help='Table name in format schema.table')
    parser.add_argument('--stats', action='store_true', help='Show table statistics')
    parser.add_argument('--schema', action='store_true', help='Show table schema')
    parser.add_argument('--sample', type=int, default=10, help='Number of sample rows to show')
    
    args = parser.parse_args()
    
    inspector = TableInspector()
    
    if args.schema or not (args.stats or args.schema):
        print(f"\n=== Schema for {args.table} ===\n")
        schema = inspector.get_table_schema(args.table)
        # Print schema details
    
    if args.stats or not (args.stats or args.schema):
        print(f"\n=== Statistics for {args.table} ===\n")
        stats = inspector.get_table_stats(args.table)
        print(stats)
    
    print(f"\n=== Sample rows (first {args.sample}) ===\n")
    sample = inspector.get_table_sample(args.table, limit=args.sample)
    print(sample)

if __name__ == "__main__":
    main()


