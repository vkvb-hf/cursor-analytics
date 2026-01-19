#!/usr/bin/env python3
"""
Generic table inspection utilities for Databricks.

This module provides reusable functions for inspecting table structure,
checking for duplicates, verifying data quality, and analyzing conflicts.
"""

import sys
import os
from typing import Dict, List, Optional, Tuple
from databricks import sql

# Import config - works both when installed as package and when run directly
try:
    from core._config import SERVER_HOSTNAME, HTTP_PATH, TOKEN
except ImportError:
    # Fallback for direct script execution
    try:
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN
    except ImportError:
        # Last resort fallback
        SERVER_HOSTNAME = None
        HTTP_PATH = None
        TOKEN = None


class TableInspector:
    """Generic table inspector for Databricks tables."""
    
    def __init__(self, server_hostname: str = None, http_path: str = None, token: str = None):
        """Initialize TableInspector with connection parameters."""
        self.server_hostname = server_hostname or SERVER_HOSTNAME
        self.http_path = http_path or HTTP_PATH
        self.token = token or TOKEN
    
    def get_connection(self):
        """Get a database connection."""
        return sql.connect(
            server_hostname=self.server_hostname,
            http_path=self.http_path,
            access_token=self.token,
            timeout_seconds=600
        )
    
    def get_table_schema(self, table_name: str) -> List[Dict]:
        """Get table schema information."""
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"DESCRIBE {table_name}")
                schema = []
                for row in cursor.fetchall():
                    schema.append({
                        'column': row[0],
                        'data_type': row[1],
                        'comment': row[2] if len(row) > 2 else None
                    })
                return schema
    
    def get_table_stats(self, table_name: str) -> Dict:
        """Get basic table statistics."""
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                total_rows = cursor.fetchone()[0]
                
                # Get column count
                schema = self.get_table_schema(table_name)
                
                return {
                    'table_name': table_name,
                    'total_rows': total_rows,
                    'column_count': len(schema),
                    'columns': [col['column'] for col in schema]
                }
    
    def check_duplicates_by_column(self, table_name: str, column_name: str, limit: int = 20) -> List[Dict]:
        """Check for duplicate values in a specific column."""
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""
                    SELECT 
                        {column_name},
                        COUNT(*) as duplicate_count
                    FROM {table_name}
                    GROUP BY {column_name}
                    HAVING COUNT(*) > 1
                    ORDER BY duplicate_count DESC
                    LIMIT {limit}
                """)
                
                duplicates = []
                for row in cursor.fetchall():
                    duplicates.append({
                        'value': row[0],
                        'count': row[1]
                    })
                return duplicates
    
    def check_cross_column_conflicts(
        self, 
        table_name: str,
        identifier_column: str,
        check_columns: List[str],
        limit: int = 20
    ) -> Dict[str, List[Dict]]:
        """
        Check if identifier column values have multiple values in check_columns.
        
        Args:
            table_name: Table to check
            identifier_column: Column to group by (e.g., 'PSP_Reference')
            check_columns: Columns to check for conflicts (e.g., ['Status', 'risk_profile'])
            limit: Maximum results per check
            
        Returns:
            Dictionary with check_column as key and list of conflicts as value
        """
        results = {}
        
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                for check_col in check_columns:
                    cursor.execute(f"""
                        SELECT 
                            {identifier_column},
                            COUNT(DISTINCT {check_col}) as unique_values,
                            COUNT(*) as total_rows
                        FROM {table_name}
                        WHERE {check_col} IS NOT NULL
                        GROUP BY {identifier_column}
                        HAVING COUNT(DISTINCT {check_col}) > 1
                        ORDER BY unique_values DESC, total_rows DESC
                        LIMIT {limit}
                    """)
                    
                    conflicts = []
                    for row in cursor.fetchall():
                        conflicts.append({
                            'identifier': row[0],
                            'unique_values': row[1],
                            'total_rows': row[2]
                        })
                    
                    results[check_col] = conflicts
        
        return results
    
    def compare_csv_to_table(
        self,
        table_name: str,
        csv_row_counts: List[Dict[str, int]],
        identifier_column: str = 'source_filename'
    ) -> Dict:
        """
        Compare CSV row counts with table row counts.
        
        Args:
            table_name: Table to compare against
            csv_row_counts: List of dicts with 'filename' and 'rows' keys
            identifier_column: Column in table that matches CSV filename
            
        Returns:
            Comparison results dictionary
        """
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                # Get table counts by identifier
                cursor.execute(f"""
                    SELECT 
                        {identifier_column},
                        COUNT(*) as row_count
                    FROM {table_name}
                    WHERE {identifier_column} IS NOT NULL
                    GROUP BY {identifier_column}
                """)
                
                table_counts = {row[0]: row[1] for row in cursor.fetchall()}
                
                # Compare
                total_csv_rows = sum(csv['rows'] for csv in csv_row_counts)
                total_table_rows = sum(table_counts.values())
                
                csv_file_dict = {csv['filename']: csv['rows'] for csv in csv_row_counts}
                
                matches = []
                mismatches = []
                
                for csv_file in csv_row_counts:
                    filename = csv_file['filename']
                    csv_rows = csv_file['rows']
                    table_rows = table_counts.get(filename, 0)
                    
                    if csv_rows == table_rows:
                        matches.append({'filename': filename, 'csv_rows': csv_rows, 'table_rows': table_rows})
                    else:
                        mismatches.append({
                            'filename': filename,
                            'csv_rows': csv_rows,
                            'table_rows': table_rows,
                            'difference': csv_rows - table_rows
                        })
                
                return {
                    'total_csv_rows': total_csv_rows,
                    'total_table_rows': total_table_rows,
                    'difference': total_csv_rows - total_table_rows,
                    'matches': matches,
                    'mismatches': mismatches,
                    'match_count': len(matches),
                    'mismatch_count': len(mismatches)
                }
    
    def inspect_table(self, table_name: str, sample_rows: int = 3) -> Dict:
        """Comprehensive table inspection."""
        stats = self.get_table_stats(table_name)
        schema = self.get_table_schema(table_name)
        
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                # Get sample rows
                cursor.execute(f"SELECT * FROM {table_name} LIMIT {sample_rows}")
                columns = [desc[0] for desc in cursor.description]
                sample_data = []
                for row in cursor.fetchall():
                    sample_data.append(dict(zip(columns, row)))
                
                return {
                    'stats': stats,
                    'schema': schema,
                    'sample_data': sample_data
                }


def main():
    """Example usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Inspect Databricks table')
    parser.add_argument('table_name', help='Table name to inspect')
    parser.add_argument('--check-duplicates', help='Column to check for duplicates')
    parser.add_argument('--check-conflicts', help='Identifier column to check for conflicts')
    parser.add_argument('--conflict-columns', nargs='+', help='Columns to check for conflicts')
    
    args = parser.parse_args()
    
    inspector = TableInspector()
    
    print("=" * 80)
    print(f"Inspecting table: {args.table_name}")
    print("=" * 80)
    
    # Get basic stats
    stats = inspector.get_table_stats(args.table_name)
    print(f"\n📊 Total rows: {stats['total_rows']:,}")
    print(f"📊 Columns: {stats['column_count']}")
    
    # Check duplicates if requested
    if args.check_duplicates:
        print(f"\n🔍 Checking duplicates in column: {args.check_duplicates}")
        duplicates = inspector.check_duplicates_by_column(args.table_name, args.check_duplicates)
        if duplicates:
            print(f"⚠️  Found {len(duplicates)} duplicate values")
            for dup in duplicates[:10]:
                print(f"   {dup['value']}: {dup['count']} occurrences")
        else:
            print("✅ No duplicates found")
    
    # Check conflicts if requested
    if args.check_conflicts and args.conflict_columns:
        print(f"\n🔍 Checking conflicts for identifier: {args.check_conflicts}")
        conflicts = inspector.check_cross_column_conflicts(
            args.table_name,
            args.check_conflicts,
            args.conflict_columns
        )
        
        for col, conflicts_list in conflicts.items():
            if conflicts_list:
                print(f"⚠️  {col}: Found {len(conflicts_list)} conflicts")
            else:
                print(f"✅ {col}: No conflicts")


if __name__ == "__main__":
    main()

