#!/usr/bin/env python3
"""
Inspect actual (unhashed) customer information from checkout_customer_details_bob and spider tables
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from databricks_api import DatabricksAPI

def get_bob_customer_details(cluster_id, business_unit, limit=30):
    """Get actual customer details from checkout_customer_details_bob (unhashed PII)"""
    query = f"""
    WITH cluster_customers AS (
      SELECT DISTINCT
        customer_uuid,
        customer_id
      FROM payments_hf.customer_cluster_sub_creation_data
      WHERE cluster_id = '{cluster_id}'
        AND business_unit = '{business_unit}'
      LIMIT 100
    )
    SELECT
      cc.customer_id,
      bob.customer_uuid,
      bob.subscribed_at_local,
      bob.first_name,
      bob.last_name,
      bob.phone,
      bob.postcode,
      LEFT(bob.address, 50) as address,
      bob.account_email,
      bob.card_first_6,
      bob.card_last_2,
      bob.shopper_email,
      bob.ip,
      bob.sales_order_id,
      bob.payment_token_id
    FROM cluster_customers cc
    JOIN payments_hf.checkout_customer_details_bob bob
      ON cc.customer_uuid = bob.customer_uuid
      AND cc.customer_id = bob.customer_id
    ORDER BY bob.subscribed_at_local DESC
    LIMIT {limit}
    """
    
    db = DatabricksAPI()
    print(f"\n{'=' * 80}")
    print(f"ACTUAL CUSTOMER DETAILS FROM BOB (Unhashed PII): {cluster_id} ({business_unit})")
    print(f"{'=' * 80}")
    results = db.run_sql(query, limit=limit)
    return results

def get_spider_customer_details(cluster_id, business_unit, limit=30):
    """Get actual customer details from checkout_customer_details_spider"""
    query = f"""
    WITH cluster_customers AS (
      SELECT DISTINCT
        customer_uuid,
        customer_id
      FROM payments_hf.customer_cluster_sub_creation_data
      WHERE cluster_id = '{cluster_id}'
        AND business_unit = '{business_unit}'
      LIMIT 100
    )
    SELECT
      cc.customer_id,
      spider.customer_uuid,
      spider.subscribed_at_local,
      spider.first_name,
      spider.last_name,
      spider.phone,
      spider.postcode,
      LEFT(spider.address, 50) as address,
      spider.account_email,
      spider.card_first_6,
      spider.card_last_2,
      spider.shopper_email,
      spider.ip
    FROM cluster_customers cc
    JOIN payments_hf.checkout_customer_details_spider spider
      ON cc.customer_uuid = spider.customer_uuid
      AND cc.customer_id = spider.customer_id
    ORDER BY spider.subscribed_at_local DESC
    LIMIT {limit}
    """
    
    db = DatabricksAPI()
    print(f"\n{'=' * 80}")
    print(f"ACTUAL CUSTOMER DETAILS FROM SPIDER: {cluster_id} ({business_unit})")
    print(f"{'=' * 80}")
    results = db.run_sql(query, limit=limit)
    return results

def analyze_shared_attributes_bob(cluster_id, business_unit):
    """Analyze which actual attributes are shared across customers in the cluster"""
    query = f"""
    WITH cluster_customers AS (
      SELECT DISTINCT
        customer_uuid,
        customer_id
      FROM payments_hf.customer_cluster_sub_creation_data
      WHERE cluster_id = '{cluster_id}'
        AND business_unit = '{business_unit}'
      LIMIT 200
    )
    SELECT
      bob.phone,
      COUNT(DISTINCT cc.customer_id) as customer_count,
      COUNT(DISTINCT bob.account_email) as unique_account_emails,
      COUNT(DISTINCT bob.shopper_email) as unique_shopper_emails,
      COUNT(DISTINCT bob.address) as unique_addresses,
      COUNT(DISTINCT bob.postcode) as unique_postcodes,
      COUNT(DISTINCT bob.card_first_6) as unique_card_first_6,
      -- Show sample values (first 3)
      SLICE(COLLECT_LIST(DISTINCT LEFT(bob.account_email, 40)), 1, 3) as sample_account_emails,
      SLICE(COLLECT_LIST(DISTINCT LEFT(bob.shopper_email, 40)), 1, 3) as sample_shopper_emails,
      SLICE(COLLECT_LIST(DISTINCT LEFT(bob.address, 30)), 1, 3) as sample_addresses
    FROM cluster_customers cc
    JOIN payments_hf.checkout_customer_details_bob bob
      ON cc.customer_uuid = bob.customer_uuid
      AND cc.customer_id = bob.customer_id
    WHERE bob.phone IS NOT NULL
    GROUP BY bob.phone
    HAVING COUNT(DISTINCT cc.customer_id) > 1
    ORDER BY customer_count DESC
    LIMIT 20
    """
    
    db = DatabricksAPI()
    print(f"\n{'=' * 80}")
    print(f"SHARED PHONE NUMBERS ANALYSIS (BOB): {cluster_id} ({business_unit})")
    print(f"{'=' * 80}")
    results = db.run_sql(query, limit=20)
    return results

def analyze_shared_shopper_emails_bob(cluster_id, business_unit):
    """Analyze shared shopper emails"""
    query = f"""
    WITH cluster_customers AS (
      SELECT DISTINCT
        customer_uuid,
        customer_id
      FROM payments_hf.customer_cluster_sub_creation_data
      WHERE cluster_id = '{cluster_id}'
        AND business_unit = '{business_unit}'
      LIMIT 200
    )
    SELECT
      bob.shopper_email,
      COUNT(DISTINCT cc.customer_id) as customer_count,
      COUNT(DISTINCT bob.account_email) as unique_account_emails,
      COUNT(DISTINCT bob.phone) as unique_phones,
      COUNT(DISTINCT bob.address) as unique_addresses,
      COUNT(DISTINCT bob.postcode) as unique_postcodes,
      -- Show sample values (first 5)
      SLICE(COLLECT_LIST(DISTINCT LEFT(bob.account_email, 40)), 1, 5) as sample_account_emails,
      SLICE(COLLECT_LIST(DISTINCT LEFT(bob.phone, 20)), 1, 5) as sample_phones
    FROM cluster_customers cc
    JOIN payments_hf.checkout_customer_details_bob bob
      ON cc.customer_uuid = bob.customer_uuid
      AND cc.customer_id = bob.customer_id
    WHERE bob.shopper_email IS NOT NULL
    GROUP BY bob.shopper_email
    HAVING COUNT(DISTINCT cc.customer_id) > 1
    ORDER BY customer_count DESC
    LIMIT 20
    """
    
    db = DatabricksAPI()
    print(f"\n{'=' * 80}")
    print(f"SHARED SHOPPER EMAILS ANALYSIS (BOB): {cluster_id} ({business_unit})")
    print(f"{'=' * 80}")
    results = db.run_sql(query, limit=20)
    return results

def main():
    """Main investigation function"""
    print("\n" + "=" * 80)
    print("INSPECTING ACTUAL (UNHASHED) CUSTOMER INFORMATION")
    print("=" * 80)
    
    # Use the largest cluster we found earlier
    cluster_id = "US_548"
    business_unit = "US"
    
    print(f"\nAnalyzing cluster: {cluster_id} ({business_unit})")
    print("This cluster has 67,077 customers")
    print("\nQuerying checkout_customer_details_bob and spider tables for actual PII data...")
    
    # Step 1: Get actual customer details from BOB
    bob_details = get_bob_customer_details(cluster_id, business_unit, limit=30)
    
    # Step 2: Get actual customer details from Spider
    spider_details = get_spider_customer_details(cluster_id, business_unit, limit=30)
    
    # Step 3: Analyze shared phone numbers
    shared_phones = analyze_shared_attributes_bob(cluster_id, business_unit)
    
    # Step 4: Analyze shared shopper emails
    shared_shopper_emails = analyze_shared_shopper_emails_bob(cluster_id, business_unit)
    
    print("\n" + "=" * 80)
    print("INVESTIGATION COMPLETE")
    print("=" * 80)
    print("\nThis analysis shows the actual (unhashed) customer information")
    print("from checkout_customer_details_bob and spider tables.")
    print("=" * 80)

if __name__ == "__main__":
    main()

