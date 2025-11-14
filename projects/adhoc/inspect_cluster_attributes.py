#!/usr/bin/env python3
"""
Inspect actual attribute values for customers in a large cluster
Get customer information from payments_hf.graph_customers_with_match_reasons
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from databricks_api import DatabricksAPI

def get_cluster_sample(cluster_id, business_unit, limit=50):
    """Get sample customers from a cluster with all their attributes"""
    query = f"""
    SELECT
      gd.customer_id,
      gd.business_unit,
      gd.root_in_business_unit as cluster_id,
      gd.business_unit_cluster_size as final_cluster_size,
      gd.is_duplicate_in_business_unit,
      gd.match_reasons,
      gd.subscribed_at_local,
      -- Get customer details
      c.email as account_email,
      c.first_name,
      c.last_name,
      c.created_at as customer_created_at,
      -- Get address details
      ca.phone,
      ca.address1,
      ca.address2,
      ca.postcode,
      ca.city,
      -- Get payment token details (shopper_email, card, etc.)
      ptd_shopper.value as shopper_email,
      ptd_card.value as card_number,
      ptd_payer.value as payer_email,
      pt.type as payment_token_type,
      -- Get order details
      so.order_nr,
      so.created_at as order_created_at,
      so.grand_total
    FROM payments_hf.graph_customers_with_match_reasons gd
    JOIN public_edw_base_grain_live.customer c
      ON gd.customer_id = c.customer_id
      AND gd.business_unit = c.bob_entity_code
    LEFT JOIN dl_bob_live_non_pii.customer_address ca
      ON gd.customer_id = ca.fk_customer
      AND gd.business_unit = ca.business_unit
      AND ca.is_billing = 0
    LEFT JOIN dl_bob_live_non_pii.sales_order so
      ON gd.customer_id = so.fk_customer
      AND gd.business_unit = so.business_unit
      AND DATE(gd.subscribed_at_local) = DATE(so.created_at)
    LEFT JOIN dl_bob_live_non_pii.payment_token pt
      ON so.fk_payment_token = pt.id_payment_token
    LEFT JOIN dl_bob_live_non_pii.payment_token_details ptd_shopper
      ON pt.id_payment_token = ptd_shopper.fk_payment_token
      AND ptd_shopper.key = 'shopper_email'
    LEFT JOIN dl_bob_live_non_pii.payment_token_details ptd_card
      ON pt.id_payment_token = ptd_card.fk_payment_token
      AND ptd_card.key = 'number'
    LEFT JOIN dl_bob_live_non_pii.payment_token_details ptd_payer
      ON pt.id_payment_token = ptd_payer.fk_payment_token
      AND ptd_payer.key = 'payer_email'
    WHERE gd.root_in_business_unit = '{cluster_id}'
      AND gd.business_unit = '{business_unit}'
    ORDER BY gd.subscribed_at_local DESC
    LIMIT {limit}
    """
    
    db = DatabricksAPI()
    print(f"\n{'=' * 80}")
    print(f"SAMPLE CUSTOMERS FROM CLUSTER: {cluster_id} ({business_unit})")
    print(f"{'=' * 80}")
    results = db.run_sql(query, limit=limit)
    return results

def analyze_attribute_values(cluster_id, business_unit):
    """Analyze the actual values of matching attributes"""
    query = f"""
    WITH cluster_customers AS (
      SELECT DISTINCT
        customer_id,
        business_unit
      FROM payments_hf.graph_customers_with_match_reasons
      WHERE root_in_business_unit = '{cluster_id}'
        AND business_unit = '{business_unit}'
      LIMIT 100
    )
    SELECT
      -- Phone analysis
      ca.phone,
      COUNT(DISTINCT cc.customer_id) as phone_usage_count,
      COUNT(DISTINCT c.email) as unique_emails_with_phone,
      COUNT(DISTINCT ca.address1) as unique_addresses_with_phone,
      -- Show sample values (first 3)
      SLICE(COLLECT_LIST(DISTINCT LEFT(c.email, 30)), 1, 3) as sample_emails,
      SLICE(COLLECT_LIST(DISTINCT LEFT(ca.address1, 30)), 1, 3) as sample_addresses,
      -- Phone pattern
      CASE 
        WHEN ca.phone IS NULL THEN 'NULL'
        WHEN LENGTH(ca.phone) < 5 THEN 'TOO_SHORT'
        WHEN LENGTH(ca.phone) > 20 THEN 'TOO_LONG'
        WHEN ca.phone LIKE '000%' THEN 'STARTS_WITH_000'
        WHEN ca.phone LIKE '111%' THEN 'STARTS_WITH_111'
        WHEN ca.phone LIKE '123%' THEN 'STARTS_WITH_123'
        WHEN ca.phone RLIKE '^[0-9]+$' = FALSE THEN 'HAS_NON_DIGITS'
        ELSE 'NORMAL'
      END as phone_pattern,
      LENGTH(ca.phone) as phone_length
    FROM cluster_customers cc
    JOIN public_edw_base_grain_live.customer c
      ON cc.customer_id = c.customer_id
      AND cc.business_unit = c.bob_entity_code
    LEFT JOIN dl_bob_live_non_pii.customer_address ca
      ON cc.customer_id = ca.fk_customer
      AND cc.business_unit = ca.business_unit
      AND ca.is_billing = 0
    WHERE ca.phone IS NOT NULL
    GROUP BY ca.phone
    HAVING COUNT(DISTINCT cc.customer_id) > 1
    ORDER BY phone_usage_count DESC
    LIMIT 20
    """
    
    db = DatabricksAPI()
    print(f"\n{'=' * 80}")
    print(f"PHONE NUMBER VALUE ANALYSIS: {cluster_id} ({business_unit})")
    print(f"{'=' * 80}")
    results = db.run_sql(query, limit=20)
    return results

def analyze_shopper_emails_values(cluster_id, business_unit):
    """Analyze actual shopper email values"""
    query = f"""
    WITH cluster_customers AS (
      SELECT DISTINCT
        customer_id,
        business_unit
      FROM payments_hf.graph_customers_with_match_reasons
      WHERE root_in_business_unit = '{cluster_id}'
        AND business_unit = '{business_unit}'
      LIMIT 100
    )
    SELECT
      ptd.value as shopper_email,
      COUNT(DISTINCT cc.customer_id) as customer_count,
      COUNT(DISTINCT c.email) as unique_account_emails,
      -- Show sample account emails (first 5)
      SLICE(COLLECT_LIST(DISTINCT LEFT(c.email, 30)), 1, 5) as sample_account_emails,
      -- Check if it's a hash
      CASE 
        WHEN LENGTH(ptd.value) = 64 AND ptd.value RLIKE '^[a-f0-9]+$' THEN 'SHA256_HASH'
        WHEN ptd.value LIKE '%@%' THEN 'EMAIL_FORMAT'
        ELSE 'OTHER'
      END as email_type,
      LENGTH(ptd.value) as email_length
    FROM cluster_customers cc
    JOIN public_edw_base_grain_live.customer c
      ON cc.customer_id = c.customer_id
      AND cc.business_unit = c.bob_entity_code
    JOIN dl_bob_live_non_pii.sales_order so
      ON cc.customer_id = so.fk_customer
      AND cc.business_unit = so.business_unit
    JOIN dl_bob_live_non_pii.payment_token pt
      ON so.fk_payment_token = pt.id_payment_token
    JOIN dl_bob_live_non_pii.payment_token_details ptd
      ON pt.id_payment_token = ptd.fk_payment_token
      AND ptd.key = 'shopper_email'
      AND ptd.value IS NOT NULL
    GROUP BY ptd.value
    HAVING COUNT(DISTINCT cc.customer_id) > 1
    ORDER BY customer_count DESC
    LIMIT 20
    """
    
    db = DatabricksAPI()
    print(f"\n{'=' * 80}")
    print(f"SHOPPER EMAIL VALUE ANALYSIS: {cluster_id} ({business_unit})")
    print(f"{'=' * 80}")
    results = db.run_sql(query, limit=20)
    return results

def get_match_reasons_details(cluster_id, business_unit):
    """Get detailed match reasons with actual attribute values"""
    query = f"""
    SELECT
      gd.customer_id,
      gd.match_reasons,
      gd.is_duplicate_in_business_unit,
      -- Show actual values that matched
      c.email as account_email,
      ca.phone,
      LEFT(ca.address1, 50) as address1,
      ca.postcode,
      LEFT(c.first_name, 20) as first_name,
      LEFT(c.last_name, 20) as last_name,
      -- Payment token details
      ptd_shopper.value as shopper_email,
      ptd_card.value as card_last4,
      pt.type as payment_type
    FROM payments_hf.graph_customers_with_match_reasons gd
    JOIN public_edw_base_grain_live.customer c
      ON gd.customer_id = c.customer_id
      AND gd.business_unit = c.bob_entity_code
    LEFT JOIN dl_bob_live_non_pii.customer_address ca
      ON gd.customer_id = ca.fk_customer
      AND gd.business_unit = ca.business_unit
      AND ca.is_billing = 0
    LEFT JOIN dl_bob_live_non_pii.sales_order so
      ON gd.customer_id = so.fk_customer
      AND gd.business_unit = so.business_unit
      AND DATE(gd.subscribed_at_local) = DATE(so.created_at)
    LEFT JOIN dl_bob_live_non_pii.payment_token pt
      ON so.fk_payment_token = pt.id_payment_token
    LEFT JOIN dl_bob_live_non_pii.payment_token_details ptd_shopper
      ON pt.id_payment_token = ptd_shopper.fk_payment_token
      AND ptd_shopper.key = 'shopper_email'
    LEFT JOIN dl_bob_live_non_pii.payment_token_details ptd_card
      ON pt.id_payment_token = ptd_card.fk_payment_token
      AND ptd_card.key = 'number'
    WHERE gd.root_in_business_unit = '{cluster_id}'
      AND gd.business_unit = '{business_unit}'
      AND gd.is_duplicate_in_business_unit = TRUE
    ORDER BY 
      CASE 
        WHEN array_contains(gd.match_reasons, 'shopper_email') THEN 1
        WHEN array_contains(gd.match_reasons, 'phone') THEN 2
        ELSE 3
      END,
      gd.subscribed_at_local DESC
    LIMIT 50
    """
    
    db = DatabricksAPI()
    print(f"\n{'=' * 80}")
    print(f"MATCH REASONS WITH ACTUAL VALUES: {cluster_id} ({business_unit})")
    print(f"{'=' * 80}")
    results = db.run_sql(query, limit=50)
    return results

def main():
    """Main investigation function"""
    print("\n" + "=" * 80)
    print("INSPECTING CLUSTER ATTRIBUTE VALUES")
    print("=" * 80)
    
    # Use the largest cluster we found earlier
    cluster_id = "US_548"
    business_unit = "US"
    
    print(f"\nAnalyzing cluster: {cluster_id} ({business_unit})")
    print("This cluster has 67,077 customers")
    
    # Step 1: Get sample customers with all attributes
    sample_customers = get_cluster_sample(cluster_id, business_unit, limit=30)
    
    # Step 2: Analyze phone number values
    phone_analysis = analyze_attribute_values(cluster_id, business_unit)
    
    # Step 3: Analyze shopper email values
    shopper_email_analysis = analyze_shopper_emails_values(cluster_id, business_unit)
    
    # Step 4: Get match reasons with actual values
    match_reasons_details = get_match_reasons_details(cluster_id, business_unit)
    
    print("\n" + "=" * 80)
    print("INVESTIGATION COMPLETE")
    print("=" * 80)
    print("\nThis analysis shows the actual attribute values that are causing")
    print("customers to be clustered together.")
    print("=" * 80)

if __name__ == "__main__":
    main()

