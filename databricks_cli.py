#!/usr/bin/env python3
"""
Unified Databricks CLI Tool

A single entry point for all Databricks operations:
- Run SQL queries
- Create and execute notebooks
- Inspect tables
- Explore data

Usage from Cursor:
    python databricks_cli.py sql "SELECT * FROM table LIMIT 10"
    python databricks_cli.py sql-file queries/my_query.sql --format csv
    python databricks_cli.py notebook create /Workspace/path/to/notebook --file my_notebook.py
    python databricks_cli.py notebook run /Workspace/path/to/notebook --job-name my_job
    python databricks_cli.py table inspect schema.table --stats --sample 20
    python databricks_cli.py interactive
"""
import sys
import os
import argparse
from pathlib import Path

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core import (
    DatabricksJobRunner,
    TableInspector,
    run_query,
    print_table,
    run_sql_file,
    interactive_sql_main
)
from core.query_util import run_query as run_query_with_display


def sql_command(args):
    """Execute a SQL query"""
    if args.query:
        query = " ".join(args.query)
        results = run_query_with_display(query, limit=args.limit, title=args.title)
        return 0 if results is not None else 1
    elif args.file:
        return run_sql_file(args.file, args.format, args.limit)
    else:
        print("Error: Either --query or --file must be specified")
        return 1


def notebook_command(args):
    """Handle notebook operations"""
    runner = DatabricksJobRunner()
    
    if args.action == 'create':
        if not args.file:
            print("Error: --file is required for 'create' action")
            return 1
        
        with open(args.file, 'r') as f:
            content = f.read()
        
        success = runner.create_notebook(
            notebook_path=args.path,
            content=content,
            overwrite=args.overwrite
        )
        
        if success:
            print(f"✓ Notebook created at {args.path}")
            return 0
        else:
            print(f"✗ Failed to create notebook")
            return 1
    
    elif args.action == 'run':
        if not args.file:
            # Try to get content from path
            print("Error: --file is required for 'run' action")
            return 1
        
        with open(args.file, 'r') as f:
            content = f.read()
        
        job_name = args.job_name or f"notebook_{Path(args.path).name}"
        
        result = runner.create_and_run(
            notebook_path=args.path,
            notebook_content=content,
            job_name=job_name
        )
        
        if result:
            print(f"✓ Job created: {result.get('job_id')}")
            print(f"✓ Run ID: {result.get('run_id')}")
            return 0
        else:
            print("✗ Failed to create/run job")
            return 1
    
    elif args.action == 'status':
        if not args.run_id:
            print("Error: --run-id is required for 'status' action")
            return 1
        
        status = runner.get_job_status(args.run_id)
        if status:
            print(f"Status: {status.get('state')}")
            print(f"Run ID: {status.get('run_id')}")
            return 0
        else:
            print("✗ Failed to get job status")
            return 1
    
    else:
        print(f"Error: Unknown action '{args.action}'")
        return 1


def table_command(args):
    """Handle table inspection operations"""
    inspector = TableInspector()
    
    if args.action == 'inspect':
        if args.schema or not (args.stats or args.sample):
            print(f"\n=== Schema for {args.table} ===\n")
            schema = inspector.get_table_schema(args.table)
            if schema:
                print(schema)
            else:
                print("Failed to get schema")
        
        if args.stats or not (args.schema or args.sample):
            print(f"\n=== Statistics for {args.table} ===\n")
            stats = inspector.get_table_stats(args.table)
            if stats:
                print(stats)
            else:
                print("Failed to get statistics")
        
        if args.sample:
            print(f"\n=== Sample rows (first {args.sample}) ===\n")
            sample = inspector.get_table_sample(args.table, limit=args.sample)
            if sample:
                print(sample)
            else:
                print("Failed to get sample")
        
        return 0
    
    elif args.action == 'duplicates':
        print(f"\n=== Checking for duplicates in {args.table} ===\n")
        duplicates = inspector.find_duplicates(args.table, args.key_column)
        if duplicates:
            print(f"Found {len(duplicates)} duplicate rows")
            print_table(duplicates, limit=args.limit)
        else:
            print("No duplicates found or error occurred")
        return 0
    
    else:
        print(f"Error: Unknown action '{args.action}'")
        return 1


def main():
    parser = argparse.ArgumentParser(
        description='Unified Databricks CLI Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run SQL query
  python databricks_cli.py sql --query "SELECT * FROM table LIMIT 10"
  
  # Run SQL from file
  python databricks_cli.py sql --file queries/my_query.sql --format csv
  
  # Create notebook
  python databricks_cli.py notebook create /Workspace/path/to/notebook --file my_notebook.py
  
  # Run notebook as job
  python databricks_cli.py notebook run /Workspace/path/to/notebook --file my_notebook.py --job-name my_job
  
  # Inspect table
  python databricks_cli.py table inspect schema.table --stats --schema --sample 20
  
  # Interactive SQL
  python databricks_cli.py interactive
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # SQL command
    sql_parser = subparsers.add_parser('sql', help='Execute SQL queries')
    sql_group = sql_parser.add_mutually_exclusive_group(required=True)
    sql_group.add_argument('--query', nargs='+', help='SQL query to execute')
    sql_group.add_argument('--file', type=str, help='SQL file to execute')
    sql_parser.add_argument('--limit', type=int, default=100, help='Limit number of rows (default: 100)')
    sql_parser.add_argument('--format', choices=['show', 'csv', 'json'], default='show', help='Output format')
    sql_parser.add_argument('--title', type=str, help='Title for results table')
    
    # Notebook command
    notebook_parser = subparsers.add_parser('notebook', help='Notebook operations')
    notebook_parser.add_argument('action', choices=['create', 'run', 'status'], help='Action to perform')
    notebook_parser.add_argument('path', help='Notebook path in Databricks workspace')
    notebook_parser.add_argument('--file', type=str, help='Local notebook file')
    notebook_parser.add_argument('--job-name', type=str, help='Job name (for run action)')
    notebook_parser.add_argument('--run-id', type=int, help='Run ID (for status action)')
    notebook_parser.add_argument('--overwrite', action='store_true', help='Overwrite existing notebook')
    
    # Table command
    table_parser = subparsers.add_parser('table', help='Table operations')
    table_parser.add_argument('action', choices=['inspect', 'duplicates'], help='Action to perform')
    table_parser.add_argument('table', help='Table name (schema.table)')
    table_parser.add_argument('--schema', action='store_true', help='Show table schema')
    table_parser.add_argument('--stats', action='store_true', help='Show table statistics')
    table_parser.add_argument('--sample', type=int, help='Number of sample rows to show')
    table_parser.add_argument('--key-column', type=str, help='Key column for duplicate detection')
    table_parser.add_argument('--limit', type=int, default=20, help='Limit for results')
    
    # Interactive command
    subparsers.add_parser('interactive', help='Start interactive SQL shell')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    try:
        if args.command == 'sql':
            return sql_command(args)
        elif args.command == 'notebook':
            return notebook_command(args)
        elif args.command == 'table':
            return table_command(args)
        elif args.command == 'interactive':
            interactive_sql_main()
            return 0
        else:
            parser.print_help()
            return 1
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        return 130
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())

