#!/usr/bin/env python3
"""
Test ASCS query step by step using temporary tables
"""
import sys
import os

cursor_databricks_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_root)

from databricks_api import DatabricksAPI

def main():
    db = DatabricksAPI()
    
    print("=" * 80)
    print("Testing ASCS Query Step by Step")
    print("=" * 80)
    
    # Step 1: Test cancellation survey CTE
    print("\nStep 1: Testing ascs_cancellation_survey CTE...")
    step1_query = """
    CREATE OR REPLACE TEMPORARY VIEW test_ascs_cancellation_survey AS
    SELECT
      'c' AS event_type,
      cs.customer_nk,
      cs.submitted_datetime AS event_timestamp,
      cs.country,
      MIN(cs.submitted_datetime) OVER (PARTITION BY cs.customer_nk) AS first_cancellation_timestamp
    FROM
      global_bi_business.plan_cancellation_survey_hist cs
    WHERE
      LOWER(cs.answer) IN ('cc-failed-payments', 'cc-payment-chargeback')
      AND cs.submitted_datetime >= '2025-01-01'
      AND DATE(cs.submitted_datetime) = '2025-11-01'
    LIMIT 100
    """
    
    try:
        result = db.run_sql(step1_query, display=False)
        print("✓ Step 1 passed: Created temporary view")
        
        # Check row count
        count_result = db.run_sql("SELECT COUNT(*) as cnt FROM test_ascs_cancellation_survey", display=True)
        if count_result:
            print(f"  Row count: {count_result[0][0]}")
    except Exception as e:
        print(f"✗ Step 1 failed: {e}")
        return 1
    
    # Step 2: Test experiment base CTE
    print("\nStep 2: Testing ascs_experiment_base CTE...")
    step2_query = """
    CREATE OR REPLACE TEMPORARY VIEW test_ascs_experiment_base AS
    SELECT
      business_unit AS country,
      details.customer_id,
      details.subscription_id,
      details.customer_plan_id,
      details.loyalty,
      'ASCS (PAYS-3159)' AS exp_name,
      dd.date_string_backwards AS allocation_time,
      dd.hellofresh_week AS allocation_hf_week,
      details.experiment_exploration AS variation_name,
      details.subscription_canceled AS is_canceled,
      details.is_test,
      TRUE AS is_experiment,
      details.subscription_canceled AS is_ascs_cancellation
    FROM
      payments_hf.f_subscription_cancellation_data scd
      JOIN dimensions.date_dimension dd ON scd.import_day = dd.sk_date
    WHERE
      1 = 1
      AND details.experiment_exploration IS NOT NULL
      AND import_day >= 20231110
      AND DATE(dd.date_string_backwards) = '2025-11-01'
    """
    
    try:
        result = db.run_sql(step2_query, display=False)
        print("✓ Step 2 passed: Created temporary view")
        
        count_result = db.run_sql("SELECT COUNT(*) as cnt FROM test_ascs_experiment_base", display=True)
        if count_result:
            print(f"  Row count: {count_result[0][0]}")
    except Exception as e:
        print(f"✗ Step 2 failed: {e}")
        return 1
    
    # Step 3: Try creating the final table with a simplified query
    print("\nStep 3: Testing simplified final query...")
    step3_query = """
    CREATE OR REPLACE TABLE payments_hf.ascs_customer_attributes_test AS
    WITH ascs_experiment_base AS (
      SELECT
        business_unit AS country,
        details.customer_id,
        details.subscription_id,
        details.customer_plan_id,
        details.loyalty,
        'ASCS (PAYS-3159)' AS exp_name,
        dd.date_string_backwards AS allocation_time,
        dd.hellofresh_week AS allocation_hf_week,
        details.experiment_exploration AS variation_name,
        details.subscription_canceled AS is_canceled,
        details.is_test,
        TRUE AS is_experiment,
        details.subscription_canceled AS is_ascs_cancellation
      FROM
        payments_hf.f_subscription_cancellation_data scd
        JOIN dimensions.date_dimension dd ON scd.import_day = dd.sk_date
      WHERE
        details.experiment_exploration IS NOT NULL
        AND import_day >= 20231110
        AND DATE(dd.date_string_backwards) = '2025-11-01'
    )
    SELECT
      country,
      customer_id,
      subscription_id,
      customer_plan_id,
      loyalty,
      exp_name,
      allocation_time AS event_date,
      allocation_hf_week AS event_hf_week,
      variation_name,
      is_canceled AS flag_is_canceled,
      is_test AS flag_is_test,
      is_experiment AS flag_is_experiment,
      is_ascs_cancellation AS flag_is_ascs_cancellation,
      NULL AS flag_subscription_canceled_matches,
      CURRENT_TIMESTAMP() AS last_modified_ts
    FROM ascs_experiment_base
    LIMIT 1000
    """
    
    try:
        result = db.run_sql(step3_query, display=False)
        print("✓ Step 3 passed: Created test table")
        
        count_result = db.run_sql("SELECT COUNT(*) as cnt FROM payments_hf.ascs_customer_attributes_test", display=True)
        if count_result:
            print(f"  Row count: {count_result[0][0]}")
    except Exception as e:
        print(f"✗ Step 3 failed: {e}")
        return 1
    
    print("\n" + "=" * 80)
    print("✓ All steps passed! The query structure works.")
    print("=" * 80)
    return 0

if __name__ == "__main__":
    sys.exit(main())






