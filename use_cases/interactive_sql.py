#!/usr/bin/env python3
"""
Interactive SQL Shell for Databricks
"""
from databricks import sql
import sys
import os

# Import config - works both when installed as package and when run directly
try:
    from core._config import SERVER_HOSTNAME, HTTP_PATH, TOKEN
except ImportError:
    # Fallback for direct script execution
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN

from core.query_util import print_table

def main():
    print("="*80)
    print("Databricks Interactive SQL Shell")
    print("="*80)
    print("\nConnecting to Databricks...")
    
    try:
        connection = sql.connect(
            server_hostname=SERVER_HOSTNAME,
            http_path=HTTP_PATH,
            access_token=TOKEN,
            timeout_seconds=30
        )
        
        print("✓ Connected successfully!")
        
        print("\nEnter your SQL queries below. Type 'exit' or 'quit' to exit.")
        print("Type 'help' for available commands.")
        print("="*80)
        print()
        
        while True:
            try:
                query = input("SQL> ")
                
                if query.lower() in ['exit', 'quit', 'q']:
                    print("\nExiting...")
                    break
                
                if query.lower() == 'help':
                    print("\nAvailable commands:")
                    print("  exit/quit/q - Exit the program")
                    print("  help - Show this help message")
                    print("  table:<name> - Show table schema")
                    print("  tables - List available tables")
                    print("\nEnter SQL queries directly to execute them.")
                    continue
                
                if not query.strip():
                    continue
                
                with connection.cursor() as cursor:
                    print(f"\nExecuting query:\n{query}\n")
                    cursor.execute(query)
                    result = cursor.fetchall()
                    
                    print(f"✓ Query executed successfully ({len(result)} rows)")
                    
                    # Get column names from cursor description
                    column_names = None
                    if cursor.description:
                        column_names = [desc[0] for desc in cursor.description]
                    
                    # Use formatted table display (limit to 20 rows)
                    print_table(result, column_names=column_names, limit=20)
                    
                    print()
                    
            except KeyboardInterrupt:
                print("\n\nExiting...")
                break
            except Exception as e:
                print(f"\n✗ Error: {e}\n")
        
        connection.close()
        print("Connection closed.")
        
    except Exception as e:
        print(f"✗ Failed to connect: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()

