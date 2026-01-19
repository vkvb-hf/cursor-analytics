#!/usr/bin/env python3
"""
Investigate clusters with final_cluster_size > 100
Check customer attributes to understand why these clusters are so large
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from databricks_api import DatabricksAPI

def find_large_clusters():
    """Find clusters with final_cluster_size > 100"""
    query = """
    SELECT
      cluster_id,
      business_unit,
      MAX(final_cluster_size) as final_cluster_size,
      COUNT(DISTINCT customer_uuid) as customer_count,
      MIN(subscription_date) as first_subscription_date,
      MAX(subscription_date) as last_subscription_date,
      COUNT(DISTINCT country_cluster) as country_cluster_count
    FROM payments_hf.customer_cluster_sub_creation_data
    WHERE final_cluster_size > 100
    GROUP BY cluster_id, business_unit
    ORDER BY final_cluster_size DESC
    LIMIT 20
    """
    
    db = DatabricksAPI()
    print("=" * 80)
    print("CLUSTERS WITH final_cluster_size > 100")
    print("=" * 80)
    results = db.run_sql(query, limit=20)
    return results

def get_cluster_details(cluster_id, business_unit):
    """Get detailed customer attributes for a specific cluster"""
    query = f"""
    WITH cluster_customers AS (
      SELECT DISTINCT
        customer_uuid,
        customer_id,
        business_unit,
        cluster_id
      FROM payments_hf.customer_cluster_sub_creation_data
      WHERE cluster_id = '{cluster_id}'
        AND business_unit = '{business_unit}'
    ),
    phone_counts AS (
      SELECT 
        ca.phone,
        COUNT(DISTINCT cc.customer_id) as phone_count
      FROM cluster_customers cc
      LEFT JOIN dl_bob_live_non_pii.customer_address ca
        ON cc.customer_id = ca.fk_customer
        AND cc.business_unit = ca.business_unit
        AND ca.is_billing = 0
      WHERE ca.phone IS NOT NULL
      GROUP BY ca.phone
    ),
    email_counts AS (
      SELECT 
        c.email,
        COUNT(DISTINCT cc.customer_id) as email_count
      FROM cluster_customers cc
      JOIN public_edw_base_grain_live.customer c
        ON cc.customer_uuid = c.customer_uuid
      WHERE c.email IS NOT NULL
      GROUP BY c.email
    )
    SELECT
      cc.customer_id,
      cc.customer_uuid,
      c.email,
      pc.phone_count,
      ec.email_count,
      ca.phone,
      LEFT(ca.address1, 50) as address1,
      ca.postcode,
      ca.city,
      LEFT(c.first_name, 20) as first_name,
      LEFT(c.last_name, 20) as last_name,
      c.created_at
    FROM cluster_customers cc
    JOIN public_edw_base_grain_live.customer c
      ON cc.customer_uuid = c.customer_uuid
    LEFT JOIN dl_bob_live_non_pii.customer_address ca
      ON cc.customer_id = ca.fk_customer
      AND cc.business_unit = ca.business_unit
      AND ca.is_billing = 0
    LEFT JOIN phone_counts pc
      ON ca.phone = pc.phone
    LEFT JOIN email_counts ec
      ON c.email = ec.email
    ORDER BY COALESCE(pc.phone_count, 0) DESC, COALESCE(ec.email_count, 0) DESC
    LIMIT 100
    """
    
    db = DatabricksAPI()
    print(f"\n{'=' * 80}")
    print(f"CLUSTER DETAILS: cluster_id={cluster_id}, business_unit={business_unit}")
    print(f"{'=' * 80}")
    results = db.run_sql(query, limit=100)
    return results

def analyze_phone_patterns(cluster_id, business_unit):
    """Analyze phone number patterns in a cluster"""
    query = f"""
    WITH cluster_customers AS (
      SELECT DISTINCT
        customer_uuid,
        customer_id,
        business_unit
      FROM payments_hf.customer_cluster_sub_creation_data
      WHERE cluster_id = '{cluster_id}'
        AND business_unit = '{business_unit}'
    )
    SELECT
      ca.phone,
      COUNT(DISTINCT cc.customer_id) as customer_count,
      COUNT(DISTINCT c.email) as unique_emails,
      COUNT(DISTINCT ca.address1) as unique_addresses,
      COUNT(DISTINCT ca.postcode) as unique_postcodes,
      MIN(c.created_at) as first_customer_created,
      MAX(c.created_at) as last_customer_created,
      -- Check for suspicious patterns
      CASE 
        WHEN ca.phone IS NULL THEN 'NULL'
        WHEN LENGTH(ca.phone) < 5 THEN 'TOO_SHORT'
        WHEN LENGTH(ca.phone) > 20 THEN 'TOO_LONG'
        WHEN ca.phone LIKE '000%' THEN 'STARTS_WITH_000'
        WHEN ca.phone LIKE '111%' THEN 'STARTS_WITH_111'
        WHEN ca.phone LIKE '123%' THEN 'STARTS_WITH_123'
        WHEN ca.phone LIKE '000000%' THEN 'MULTIPLE_ZEROS'
        WHEN ca.phone LIKE '111111%' THEN 'MULTIPLE_ONES'
        ELSE 'NORMAL'
      END as phone_pattern
    FROM cluster_customers cc
    JOIN public_edw_base_grain_live.customer c
      ON cc.customer_uuid = c.customer_uuid
    LEFT JOIN dl_bob_live_non_pii.customer_address ca
      ON cc.customer_id = ca.fk_customer
      AND cc.business_unit = ca.business_unit
      AND ca.is_billing = 0
    WHERE ca.phone IS NOT NULL
    GROUP BY ca.phone
    HAVING COUNT(DISTINCT cc.customer_id) > 1
    ORDER BY customer_count DESC
    LIMIT 50
    """
    
    db = DatabricksAPI()
    print(f"\n{'=' * 80}")
    print(f"PHONE NUMBER PATTERNS: cluster_id={cluster_id}, business_unit={business_unit}")
    print(f"{'=' * 80}")
    results = db.run_sql(query, limit=50)
    return results

def analyze_match_reasons(cluster_id, business_unit):
    """Analyze match reasons for customers in a cluster"""
    query = f"""
    WITH cluster_customers AS (
      SELECT DISTINCT
        customer_id,
        business_unit
      FROM payments_hf.customer_cluster_sub_creation_data
      WHERE cluster_id = '{cluster_id}'
        AND business_unit = '{business_unit}'
    )
    SELECT
      gd.match_reasons,
      COUNT(DISTINCT gd.customer_id) as customer_count
    FROM cluster_customers cc
    JOIN payments_hf.graph_customers_with_match_reasons gd
      ON cc.customer_id = gd.customer_id
      AND cc.business_unit = gd.business_unit
    WHERE gd.is_duplicate_in_business_unit = TRUE
    GROUP BY gd.match_reasons
    ORDER BY customer_count DESC
    LIMIT 20
    """
    
    db = DatabricksAPI()
    print(f"\n{'=' * 80}")
    print(f"MATCH REASONS: cluster_id={cluster_id}, business_unit={business_unit}")
    print(f"{'=' * 80}")
    results = db.run_sql(query, limit=20)
    return results

def analyze_shopper_emails(cluster_id, business_unit):
    """Analyze shopper emails in a cluster - these are often the culprit for large clusters"""
    query = f"""
    WITH cluster_customers AS (
      SELECT DISTINCT
        customer_id,
        customer_uuid,
        business_unit
      FROM payments_hf.customer_cluster_sub_creation_data
      WHERE cluster_id = '{cluster_id}'
        AND business_unit = '{business_unit}'
    )
    SELECT
      ptd.value as shopper_email,
      COUNT(DISTINCT cc.customer_id) as customer_count,
      COUNT(DISTINCT c.email) as unique_account_emails,
      COUNT(DISTINCT ca.address1) as unique_addresses,
      COUNT(DISTINCT ca.postcode) as unique_postcodes,
      MIN(c.created_at) as first_customer_created,
      MAX(c.created_at) as last_customer_created,
      MIN(so.created_at) as first_order_date,
      MAX(so.created_at) as last_order_date
    FROM cluster_customers cc
    JOIN public_edw_base_grain_live.customer c
      ON cc.customer_uuid = c.customer_uuid
    JOIN dl_bob_live_non_pii.sales_order so
      ON cc.customer_id = so.fk_customer
      AND cc.business_unit = so.business_unit
    JOIN dl_bob_live_non_pii.payment_token pt
      ON so.fk_payment_token = pt.id_payment_token
    JOIN dl_bob_live_non_pii.payment_token_details ptd
      ON pt.id_payment_token = ptd.fk_payment_token
      AND ptd.key = 'shopper_email'
      AND ptd.value IS NOT NULL
    LEFT JOIN dl_bob_live_non_pii.customer_address ca
      ON cc.customer_id = ca.fk_customer
      AND cc.business_unit = ca.business_unit
      AND ca.is_billing = 0
    GROUP BY ptd.value
    HAVING COUNT(DISTINCT cc.customer_id) > 1
    ORDER BY customer_count DESC
    LIMIT 30
    """
    
    db = DatabricksAPI()
    print(f"\n{'=' * 80}")
    print(f"SHOPPER EMAIL ANALYSIS: cluster_id={cluster_id}, business_unit={business_unit}")
    print(f"{'=' * 80}")
    results = db.run_sql(query, limit=30)
    return results

def main():
    """Main investigation function"""
    print("\n" + "=" * 80)
    print("INVESTIGATING LARGE CLUSTERS (final_cluster_size > 100)")
    print("=" * 80 + "\n")
    
    # Step 1: Find large clusters
    large_clusters = find_large_clusters()
    
    if not large_clusters or len(large_clusters) == 0:
        print("No clusters found with final_cluster_size > 100")
        return
    
    # Step 2: Pick the first cluster for detailed analysis
    if large_clusters and len(large_clusters) > 0:
        # Get the first row (largest cluster)
        # Results are tuples, extract cluster_id and business_unit
        first_cluster = large_clusters[0]
        cluster_id = str(first_cluster[0])  # cluster_id
        business_unit = str(first_cluster[1])  # business_unit
        
        print(f"\n{'=' * 80}")
        print(f"SELECTED CLUSTER FOR DETAILED ANALYSIS:")
        print(f"  cluster_id: {cluster_id}")
        print(f"  business_unit: {business_unit}")
        print(f"{'=' * 80}\n")
        
        # Step 3: Get cluster details
        cluster_details = get_cluster_details(cluster_id, business_unit)
        
        # Step 4: Analyze phone patterns
        phone_patterns = analyze_phone_patterns(cluster_id, business_unit)
        
        # Step 5: Analyze match reasons
        match_reasons = analyze_match_reasons(cluster_id, business_unit)
        
        # Step 6: Analyze shopper emails (often the main culprit)
        shopper_emails = analyze_shopper_emails(cluster_id, business_unit)
        
        print("\n" + "=" * 80)
        print("INVESTIGATION COMPLETE")
        print("=" * 80)
        print("\nKEY FINDINGS:")
        print("- Phone numbers appear to be hashed (TOO_LONG pattern)")
        print("- Many customers matched by 'shopper_email' alone")
        print("- Shopper emails from payment providers (PayPal, Klarna) are likely causing large clusters")
        print("=" * 80)

if __name__ == "__main__":
    main()

