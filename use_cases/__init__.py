"""
Use Cases - Composite scripts that combine core functions

These are higher-level scripts for specific workflows:
- csv_to_table: Upload CSVs and create Databricks tables
- create_table: Create tables from SQL
- interactive_sql: Interactive SQL REPL

These are NOT pure functions - they combine multiple core functions
for specific use cases.
"""

from .csv_to_table import create_table_from_csvs
from .create_table import create_table
from .interactive_sql import main as interactive_sql_main

__all__ = [
    'create_table_from_csvs',
    'create_table',
    'interactive_sql_main',
]
