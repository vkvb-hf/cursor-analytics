#!/usr/bin/env python3
"""
Inspect CSV files for a single customer to see what data is available.

This script reads the Neptune CSV files and shows all data for one customer.
"""

import sys
import os

# Add cursor_databricks directory to path
script_dir = os.path.dirname(os.path.abspath(__file__))
cursor_databricks_dir = os.path.dirname(os.path.dirname(script_dir))
sys.path.insert(0, cursor_databricks_dir)

from databricks_api import DatabricksAPI

def inspect_csv_customer(customer_node_id: str = None):
    """
    Inspect CSV files for a single customer.
    
    Args:
        customer_node_id: Customer node ID (e.g., "US_12345"). If None, picks first customer.
    """
    db = DatabricksAPI()
    
    save_path = "s3://hf-payments-data-lake-live-main/voucher_abuse/neptune_backfill/20250305"
    
    print("=" * 100)
    print("INSPECT CSV FILES FOR ONE CUSTOMER")
    print("=" * 100)
    print(f"\n📥 Reading CSV files from: {save_path}")
    
    # Read vertices CSV using Spark SQL
    vertices_query = f"""
    SELECT *
    FROM read_files(
      '{save_path}/vertices',
      format => 'csv',
      header => true,
      inferSchema => false
    )
    """
    
    # Read edges CSV using Spark SQL
    edges_query = f"""
    SELECT *
    FROM read_files(
      '{save_path}/edges',
      format => 'csv',
      header => true,
      inferSchema => false
    )
    """
    
    print("\n📊 Reading vertices CSV...")
    vertices_result = db.run_sql(vertices_query, limit=1000, display=False)
    vertices_df = vertices_result if vertices_result else []
    print(f"   Read {len(vertices_df)} vertices")
    
    print("\n📊 Reading edges CSV...")
    edges_result = db.run_sql(edges_query, limit=1000, display=False)
    edges_df = edges_result if edges_result else []
    print(f"   Read {len(edges_df)} edges")
    
    # If no customer specified, pick first one from edges
    if customer_node_id is None:
        if edges_df and len(edges_df) > 0:
            # Get first customer from edges
            customer_node_id = edges_df[0].get('~from')
            if customer_node_id:
                print(f"\n✅ Using first customer found: {customer_node_id}")
            else:
                print("❌ No customer node found in first edge")
                return
        else:
            print("❌ No edges found in CSV")
            return
    
    print(f"\n🔍 Filtering CSV data for customer: {customer_node_id}")
    print("=" * 100)
    
    # Filter customer vertex from vertices_df
    print(f"\n📋 Vertex record (customer node):")
    print("-" * 100)
    customer_vertex = [
        row for row in vertices_df 
        if row.get('~id') == customer_node_id and row.get('~label') == 'customer'
    ]
    
    if customer_vertex:
        for row in customer_vertex:
            print(f"  ~id: {row.get('~id', 'N/A')}")
            print(f"  ~label: {row.get('~label', 'N/A')}")
            print(f"  created_at: {row.get('created_at', 'N/A')}")
            print(f"  checkout_success: {row.get('checkout_success', 'N/A')}")
    else:
        print("  ⚠️  No vertex found for this customer")
    
    # Filter edges for this customer
    print(f"\n📋 All edges (identifiers) for this customer:")
    print("-" * 100)
    customer_edges = [
        row for row in edges_df 
        if row.get('~from') == customer_node_id
    ]
    
    # Sort by label and to
    customer_edges.sort(key=lambda x: (x.get('~label', ''), x.get('~to', '')))
    
    if customer_edges:
        print(f"  Total identifiers: {len(customer_edges)}")
        print("\n  Edge details:")
        for i, row in enumerate(customer_edges[:20], 1):  # Show first 20
            print(f"    {i}. {row.get('~label', 'N/A')}: {row.get('~to', 'N/A')}")
        
        if len(customer_edges) > 20:
            print(f"    ... and {len(customer_edges) - 20} more")
        
        # Group by identifier type
        identifier_types = {}
        for row in customer_edges:
            label = row.get('~label', 'unknown')
            if label not in identifier_types:
                identifier_types[label] = []
            identifier_types[label].append(row.get('~to', 'N/A'))
        
        print(f"\n  Identifier types breakdown:")
        for label, identifiers in sorted(identifier_types.items()):
            print(f"    {label}: {len(identifiers)} identifiers")
            # Show first 3 examples
            for identifier in identifiers[:3]:
                print(f"      - {identifier}")
            if len(identifiers) > 3:
                print(f"      ... and {len(identifiers) - 3} more")
    else:
        print("  ⚠️  No edges found for this customer")
    
    # Get identifier vertices
    if customer_edges:
        identifier_ids = [row.get('~to') for row in customer_edges if row.get('~to')]
        if identifier_ids:
            # Filter identifier vertices
            identifier_vertices = [
                row for row in vertices_df
                if row.get('~id') in identifier_ids and row.get('~label') == 'identifier'
            ]
            
            print(f"\n📋 Sample identifier vertices (what {customer_node_id} is connected to):")
            print("-" * 100)
            
            if identifier_vertices:
                print(f"  Showing {len(identifier_vertices)} of {len(identifier_ids)} identifier vertices:")
                for i, row in enumerate(identifier_vertices[:10], 1):
                    print(f"    {i}. {row.get('~id', 'N/A')} (label: {row.get('~label', 'N/A')})")
                if len(identifier_vertices) > 10:
                    print(f"    ... and {len(identifier_vertices) - 10} more")
    
    # Summary
    print("\n" + "=" * 100)
    print("SUMMARY:")
    print("=" * 100)
    print(f"  Customer Node: {customer_node_id}")
    
    if customer_vertex:
        created_at = customer_vertex[0].get('created_at', 'N/A')
        print(f"  Created At: {created_at}")
    
    if customer_edges:
        print(f"  Number of Identifiers: {len(customer_edges)}")
        print(f"  Identifier Types: {', '.join(sorted(identifier_types.keys()))}")
    
    print("\n  ✅ What's AVAILABLE in CSV:")
    print("    - Customer node ID (business_unit_customer_id)")
    print("    - created_at timestamp")
    print("    - All identifiers (processed/cleaned values)")
    print("      Examples: 'email:johndoe@gmail.com', 'phone:1234567890', 'card_address:...'")
    
    print("\n  ❌ What's MISSING from CSV:")
    print("    - first_name, last_name")
    print("    - phone (raw), postcode, address")
    print("    - account_email (raw), shopper_email (raw)")
    print("    - card_first_6, card_last_2")
    print("    - ip")
    print("    - customer_uuid")
    print("\n  Note: These raw attributes were used to GENERATE the identifiers,")
    print("  but only the processed identifiers are stored in CSV files.")
    print("=" * 100)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Inspect CSV files for a single customer")
    parser.add_argument(
        "--customer",
        type=str,
        default=None,
        help="Customer node ID (e.g., 'US_12345'). If not provided, uses first customer found."
    )
    
    args = parser.parse_args()
    
    inspect_csv_customer(args.customer)

