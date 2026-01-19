#!/usr/bin/env python3
"""
Databricks Query Utility - Main query tool for exploring tables
Run SQL queries against Databricks with formatted output
"""
import sys
import os
import argparse
from decimal import Decimal
from typing import List, Any, Optional

# Import config - works both when installed as package and when run directly
try:
    from core._config import SERVER_HOSTNAME, HTTP_PATH, TOKEN
except ImportError:
    # Fallback for direct script execution
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN

def format_value(value: Any) -> str:
    """Format a value for display"""
    if value is None:
        return 'NULL'
    if isinstance(value, bool):
        return str(value)  # Check bool before int (since bool is subclass of int)
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, (int, float)):
        if isinstance(value, int):
            return f"{value:,}"
        return f"{value:.2f}"
    return str(value)

def print_table(results: List[Any], column_names: List[str] = None, limit: Optional[int] = None, title: Optional[str] = None):
    """
    Print query results in a formatted table
    
    Args:
        results: List of Row objects from query
        column_names: List of column names (optional, will try to infer if not provided)
        limit: Maximum number of rows to display (None = all)
        title: Optional title for the table
    """
    if not results:
        print("No results returned.")
        return
    
    # Determine rows to display
    display_results = results[:limit] if limit else results
    
    # Get column names if not provided
    if not column_names:
        first_row = results[0]
        
        # Try to access as databricks Row object (has .show() method and supports attribute access)
        try:
            # Databricks rows can be accessed by index or attribute
            # Try to get column names from the row structure
            if hasattr(first_row, '_fields'):
                column_names = list(first_row._fields)
            elif hasattr(first_row, '__dict__'):
                column_names = [k for k in first_row.__dict__.keys() if not k.startswith('_')]
            else:
                # Try accessing as tuple/list with cursor description
                # If we have a cursor, get description, otherwise infer from row length
                num_cols = len(first_row) if hasattr(first_row, '__len__') else 1
                column_names = [f"col_{i+1}" for i in range(num_cols)]
        except Exception as e:
            # Last resort: use row length
            try:
                num_cols = len(first_row)
                column_names = [f"col_{i+1}" for i in range(num_cols)]
            except:
                column_names = ["value"]
    
    # Calculate column widths
    col_widths = {}
    for i, col in enumerate(column_names):
        # Width based on column name
        width = len(str(col))
        # Check widths in data
        for row in display_results:
            try:
                # Try multiple ways to access the value
                val = None
                # First try attribute access (if column name is valid Python identifier)
                if col.replace('_', '').isalnum() and hasattr(row, col):
                    try:
                        val = getattr(row, col)
                    except:
                        pass
                
                # If attribute access failed, try index access
                if val is None:
                    if isinstance(row, (list, tuple)) and i < len(row):
                        val = row[i]
                    elif hasattr(row, '__getitem__'):
                        try:
                            val = row[i]
                        except:
                            try:
                                val = row[col]
                            except:
                                pass
                
                if val is not None:
                    formatted_val = format_value(val)
                    width = max(width, len(formatted_val))
            except:
                pass
        col_widths[col] = min(width, 50)  # Cap at 50 chars
    
    # Print title if provided
    if title:
        print("=" * 100)
        print(title)
        print("=" * 100)
    
    # Calculate total width for header
    total_width = sum(col_widths.values()) + (len(column_names) - 1) * 3  # 3 chars for " | "
    
    # Print header
    header = " | ".join(col.ljust(col_widths[col]) for col in column_names)
    print("=" * len(header))
    print(header)
    print("-" * len(header))
    
    # Print rows
    for row in display_results:
        values = []
        for i, col in enumerate(column_names):
            try:
                # Try multiple ways to access the value
                val = None
                # First try attribute access (if column name is valid Python identifier)
                if col.replace('_', '').isalnum() and hasattr(row, col):
                    try:
                        val = getattr(row, col)
                    except:
                        pass
                
                # If attribute access failed, try index access
                if val is None:
                    if isinstance(row, (list, tuple)) and i < len(row):
                        val = row[i]
                    elif hasattr(row, '__getitem__'):
                        try:
                            val = row[i]
                        except:
                            try:
                                val = row[col]
                            except:
                                pass
            except:
                val = None
            
            formatted = format_value(val)
            # Truncate long values
            if len(formatted) > col_widths[col]:
                formatted = formatted[:col_widths[col]-3] + "..."
            values.append(formatted.ljust(col_widths[col]))
        print(" | ".join(values))
    
    print("=" * len(header))
    
    # Print summary
    if limit and len(results) > limit:
        print(f"\nShowing {limit} of {len(results)} rows. Use --limit {len(results)} to see all.")
    else:
        print(f"\nTotal rows: {len(results)}")

def run_query(query: str, limit: Optional[int] = None, title: Optional[str] = None):
    """
    Execute a SQL query and display formatted results
    
    Args:
        query: SQL query to execute
        limit: Number of rows to display (None = all)
        title: Optional title for results table
    
    Returns:
        List of Row objects
    """
    # Lazy import to avoid ImportError when databricks-sql-connector not installed
    from databricks import sql
    
    print("="*100)
    print("Connecting to Databricks...")
    print("="*100)
    
    try:
        with sql.connect(
            server_hostname=SERVER_HOSTNAME,
            http_path=HTTP_PATH,
            access_token=TOKEN,
            timeout_seconds=30
        ) as connection:
            
            print("✓ Connected successfully!")
            
            with connection.cursor() as cursor:
                print(f"\nExecuting query:\n{query}\n")
                
                cursor.execute(query)
                result = cursor.fetchall()
                
                print(f"✓ Query completed! ({len(result)} rows returned)\n")
                
                # Get column names from cursor description
                column_names = None
                if cursor.description:
                    column_names = [desc[0] for desc in cursor.description]
                
                # Display formatted results
                print_table(result, column_names=column_names, limit=limit, title=title)
                
                return result
                
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    parser = argparse.ArgumentParser(
        description='Query Databricks and display formatted results',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Query with default limit (20 rows)
  python query_util.py "SELECT * FROM payments_hf.chargebacks_dashboard LIMIT 10"
  
  # Query with custom limit
  python query_util.py "SELECT * FROM table" --limit 50
  
  # Show all rows
  python query_util.py "SELECT * FROM table" --limit 0
  
  # With title
  python query_util.py "SELECT * FROM table" --title "My Results"
        """
    )
    
    parser.add_argument('query', nargs='+', help='SQL query to execute')
    parser.add_argument('--limit', type=int, default=20, 
                       help='Number of rows to display (0 = all, default: 20)')
    parser.add_argument('--title', type=str, default=None,
                       help='Title for the results table')
    
    args = parser.parse_args()
    
    # Join query parts
    query = " ".join(args.query)
    
    # Convert limit: 0 means no limit (None)
    display_limit = None if args.limit == 0 else args.limit
    
    run_query(query, limit=display_limit, title=args.title)

if __name__ == "__main__":
    main()

