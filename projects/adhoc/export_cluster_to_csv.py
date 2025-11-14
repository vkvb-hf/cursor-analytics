#!/usr/bin/env python3
"""
Export all customer attributes from a cluster to CSV
"""

import sys
import os
import csv
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from databricks_api import DatabricksAPI

def export_cluster_to_csv(cluster_id, business_unit, output_file=None):
    """Export all customer attributes from a cluster to CSV"""
    
    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"cluster_{cluster_id}_{business_unit}_{timestamp}.csv"
    
    query = f"""
    WITH cluster_customers AS (
      SELECT DISTINCT
        customer_uuid,
        customer_id
      FROM payments_hf.customer_cluster_sub_creation_data
      WHERE cluster_id = '{cluster_id}'
        AND business_unit = '{business_unit}'
    )
    SELECT
      cc.customer_id,
      bob.customer_uuid,
      bob.subscribed_at_local,
      bob.first_name,
      bob.last_name,
      bob.phone,
      bob.postcode,
      bob.address,
      bob.account_email,
      bob.card_first_6,
      bob.card_last_2,
      bob.shopper_email,
      bob.ip,
      bob.sales_order_id,
      bob.payment_token_id,
      bob.subscription_id,
      bob.customer_address_id,
      -- Get match reasons from graph table
      gd.match_reasons,
      gd.is_duplicate_in_business_unit,
      gd.business_unit_cluster_size as final_cluster_size
    FROM cluster_customers cc
    LEFT JOIN payments_hf.checkout_customer_details_bob bob
      ON cc.customer_uuid = bob.customer_uuid
      AND cc.customer_id = bob.customer_id
    LEFT JOIN payments_hf.graph_customers_with_match_reasons gd
      ON cc.customer_id = gd.customer_id
      AND '{business_unit}' = gd.business_unit
    ORDER BY bob.subscribed_at_local DESC NULLS LAST, cc.customer_id
    """
    
    db = DatabricksAPI()
    print(f"\n{'=' * 80}")
    print(f"EXPORTING CLUSTER TO CSV: {cluster_id} ({business_unit})")
    print(f"Output file: {output_file}")
    print(f"{'=' * 80}")
    
    # Run query and get results
    results = db.run_sql(query, limit=None, display=False)
    
    if not results:
        print("No results found!")
        return None
    
    # Write to CSV
    print(f"\nWriting {len(results)} rows to CSV...")
    
    # Get column names from first result (assuming it's a tuple with column info)
    # Or we can define them explicitly
    columns = [
        'customer_id',
        'customer_uuid',
        'subscribed_at_local',
        'first_name',
        'last_name',
        'phone',
        'postcode',
        'address',
        'account_email',
        'card_first_6',
        'card_last_2',
        'shopper_email',
        'ip',
        'sales_order_id',
        'payment_token_id',
        'subscription_id',
        'customer_address_id',
        'match_reasons',
        'is_duplicate_in_business_unit',
        'final_cluster_size'
    ]
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header
        writer.writerow(columns)
        
        # Write data rows
        for row in results:
            # Convert row to list, handling None values and arrays
            row_list = []
            for i, val in enumerate(row):
                if val is None:
                    row_list.append('')
                elif isinstance(val, (list, tuple)):
                    # Convert array to string representation
                    row_list.append(str(val))
                else:
                    row_list.append(str(val))
            writer.writerow(row_list)
    
    print(f"✓ Successfully exported {len(results)} rows to {output_file}")
    print(f"  Full path: {os.path.abspath(output_file)}")
    
    return output_file

def main():
    """Main function"""
    cluster_id = "US_548"
    business_unit = "US"
    
    print("\n" + "=" * 80)
    print("EXPORTING CLUSTER CUSTOMER ATTRIBUTES TO CSV")
    print("=" * 80)
    print(f"\nCluster ID: {cluster_id}")
    print(f"Business Unit: {business_unit}")
    print(f"Expected customers: ~67,077")
    print("\nThis may take a few minutes...")
    
    output_file = export_cluster_to_csv(cluster_id, business_unit)
    
    if output_file:
        print("\n" + "=" * 80)
        print("EXPORT COMPLETE")
        print("=" * 80)
        print(f"\nCSV file created: {output_file}")
        print(f"Location: {os.path.abspath(output_file)}")
        print("=" * 80)

if __name__ == "__main__":
    main()

