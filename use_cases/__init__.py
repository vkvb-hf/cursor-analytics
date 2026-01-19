"""
Use Cases - Composite scripts that combine core functions

These are higher-level scripts for specific workflows:
- csv_to_table: Upload CSVs and create Databricks tables
- create_table: Create tables from SQL
- interactive_sql: Interactive SQL REPL

These are NOT pure functions - they combine multiple core functions
for specific use cases.

Note: These modules require databricks-sql-connector to be installed.
Import them directly when needed rather than from this __init__.py
if you want to avoid import errors.
"""

# Lazy imports to avoid ImportError when databricks-sql-connector not installed
def __getattr__(name):
    if name == 'create_table_from_csvs':
        from .csv_to_table import create_table_from_csvs
        return create_table_from_csvs
    elif name == 'create_table':
        from .create_table import create_table
        return create_table
    elif name == 'interactive_sql_main':
        from .interactive_sql import main as interactive_sql_main
        return interactive_sql_main
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = [
    'create_table_from_csvs',
    'create_table',
    'interactive_sql_main',
]
