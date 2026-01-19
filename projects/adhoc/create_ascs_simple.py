#!/usr/bin/env python3
"""
Create ASCS table with simplified query (base data only, no cohort metrics)
This will help us verify the table structure works, then we can add cohort metrics
"""
import sys
import os

cursor_databricks_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_root)

from databricks_api import DatabricksAPI

def main():
    db = DatabricksAPI()
    
    # Simplified query - just base data without complex cohort calculations
    simplified_query = """
    CREATE OR REPLACE TABLE payments_hf.ascs_customer_attributes AS
    WITH date_lkup AS (
      SELECT
        hellofresh_week,
        CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS hellofresh_year_month,
        CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS hellofresh_year_quarter
      FROM
        dimensions.date_dimension dd
      WHERE
        hellofresh_week >= '2023-W01'
      GROUP BY
        1, 2, 3
    ),
    date_lkup_row AS (
      SELECT
        *,
        ROW_NUMBER() OVER(ORDER BY hellofresh_week ASC) AS row_num
      FROM
        date_lkup
    ),
    final_date_lkup AS (
      SELECT
        a.hellofresh_week,
        b.hellofresh_week AS lead_hellofresh_week_5wks,
        c.hellofresh_week AS lead_hellofresh_week_10wks,
        d.hellofresh_week AS lead_hellofresh_week_13wks,
        e.hellofresh_week AS lead_hellofresh_week_26wks,
        f.hellofresh_week AS lead_hellofresh_week_52wks
      FROM
        date_lkup_row a
        LEFT JOIN date_lkup_row b ON a.row_num = b.row_num - 5
        LEFT JOIN date_lkup_row c ON a.row_num = c.row_num - 10
        LEFT JOIN date_lkup_row d ON a.row_num = d.row_num - 13
        LEFT JOIN date_lkup_row e ON a.row_num = e.row_num - 26
        LEFT JOIN date_lkup_row f ON a.row_num = f.row_num - 52
    ),
    ascs_experiment_base AS (
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
    ),
    ascs_cancellation_survey AS (
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
    ),
    ascs_cancellation_with_customer AS (
      SELECT
        acs.country,
        CAST(cd.customer_id AS BIGINT) AS customer_id,
        acs.customer_nk,
        acs.event_timestamp,
        acs.first_cancellation_timestamp,
        dd.date_string_backwards AS cancellation_date,
        dd.hellofresh_week AS cancellation_hf_week
      FROM
        ascs_cancellation_survey acs
        JOIN public_edw_base_grain_live.customer cd
          ON acs.customer_nk = cd.customer_uuid
          AND acs.country = cd.bob_entity_code
        JOIN dimensions.date_dimension dd
          ON DATE(acs.event_timestamp) = DATE(dd.date_string_backwards)
    ),
    ascs_cancellation_base AS (
      SELECT
        ac.country,
        ac.customer_id,
        COALESCE(scd.details.subscription_id, NULL) AS subscription_id,
        COALESCE(scd.details.customer_plan_id, NULL) AS customer_plan_id,
        COALESCE(scd.details.loyalty, 0) AS loyalty,
        NULL AS exp_name,
        ac.cancellation_date AS cancellation_time,
        ac.cancellation_hf_week,
        NULL AS variation_name,
        COALESCE(scd.details.subscription_canceled, FALSE) AS is_canceled,
        COALESCE(scd.details.is_test, FALSE) AS is_test,
        FALSE AS is_experiment,
        TRUE AS is_ascs_cancellation,
        CASE
          WHEN scd.details.subscription_canceled = TRUE THEN TRUE
          ELSE FALSE
        END AS flag_subscription_canceled_matches
      FROM
        ascs_cancellation_with_customer ac
        LEFT JOIN dimensions.date_dimension dd_cancel
          ON DATE(ac.cancellation_date) = DATE(dd_cancel.date_string_backwards)
        LEFT JOIN payments_hf.f_subscription_cancellation_data scd
          ON ac.country = scd.business_unit
          AND ac.customer_id = scd.details.customer_id
          AND scd.import_day = dd_cancel.sk_date
          AND (scd.details.experiment_exploration IS NULL OR scd.details.experiment_exploration = '')
    ),
    ascs_combined_base AS (
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
        is_canceled,
        is_test,
        is_experiment,
        is_ascs_cancellation,
        NULL AS flag_subscription_canceled_matches
      FROM
        ascs_experiment_base
      
      UNION ALL
      
      SELECT
        country,
        customer_id,
        subscription_id,
        customer_plan_id,
        loyalty,
        exp_name,
        cancellation_time AS event_date,
        cancellation_hf_week AS event_hf_week,
        variation_name,
        is_canceled,
        is_test,
        is_experiment,
        is_ascs_cancellation,
        flag_subscription_canceled_matches
      FROM
        ascs_cancellation_base
    ),
    ascs_unique_base AS (
      SELECT
        country,
        customer_id,
        subscription_id,
        customer_plan_id,
        loyalty,
        exp_name,
        event_date,
        event_hf_week,
        MAX(variation_name) AS variation_name,
        MAX(is_canceled) AS flag_is_canceled,
        MAX(is_test) AS flag_is_test,
        MAX(is_experiment) AS flag_is_experiment,
        MAX(is_ascs_cancellation) AS flag_is_ascs_cancellation,
        MAX(flag_subscription_canceled_matches) AS flag_subscription_canceled_matches,
        ROW_NUMBER() OVER(
          PARTITION BY country, customer_id, event_date
          ORDER BY event_date DESC
        ) AS rn
      FROM
        ascs_combined_base
      WHERE
        is_test = FALSE
      GROUP BY
        country, customer_id, subscription_id, customer_plan_id, loyalty, exp_name, event_date, event_hf_week
    ),
    ascs_base_with_cohorts AS (
      SELECT
        a.*,
        b.lead_hellofresh_week_5wks,
        b.lead_hellofresh_week_10wks,
        b.lead_hellofresh_week_13wks,
        b.lead_hellofresh_week_26wks,
        b.lead_hellofresh_week_52wks
      FROM
        ascs_unique_base a
        JOIN final_date_lkup b ON a.event_hf_week = b.hellofresh_week
      WHERE
        a.rn = 1
        AND DATE(a.event_date) = '2025-11-01'
    )
    SELECT
      country,
      customer_id,
      subscription_id,
      customer_plan_id,
      loyalty,
      exp_name,
      event_date,
      event_hf_week,
      variation_name,
      flag_is_canceled,
      flag_is_test,
      flag_is_experiment,
      flag_is_ascs_cancellation,
      flag_subscription_canceled_matches,
      -- Placeholder columns for cohort metrics (will be NULL for now)
      CAST(NULL AS DOUBLE) AS profit_check_till_date_eur,
      CAST(NULL AS DOUBLE) AS gross_revenue_till_date_eur,
      CAST(NULL AS DOUBLE) AS net_revenue_till_date_eur,
      CAST(NULL AS DOUBLE) AS discount_till_date_eur,
      CAST(NULL AS DOUBLE) AS profit_till_date_eur,
      CAST(NULL AS BIGINT) AS count_orders_till_date,
      CAST(NULL AS BIGINT) AS reactivations_till_date,
      -- Cohort metrics placeholders
      CAST(NULL AS DOUBLE) AS profit_check_5w_eur,
      CAST(NULL AS DOUBLE) AS gross_revenue_5w_eur,
      CAST(NULL AS DOUBLE) AS net_revenue_5w_eur,
      CAST(NULL AS DOUBLE) AS profit_check_10w_eur,
      CAST(NULL AS DOUBLE) AS gross_revenue_10w_eur,
      CAST(NULL AS DOUBLE) AS net_revenue_10w_eur,
      CAST(NULL AS DOUBLE) AS profit_check_13w_eur,
      CAST(NULL AS DOUBLE) AS gross_revenue_13w_eur,
      CAST(NULL AS DOUBLE) AS net_revenue_13w_eur,
      CAST(NULL AS DOUBLE) AS profit_check_26w_eur,
      CAST(NULL AS DOUBLE) AS gross_revenue_26w_eur,
      CAST(NULL AS DOUBLE) AS net_revenue_26w_eur,
      CAST(NULL AS DOUBLE) AS profit_check_52w_eur,
      CAST(NULL AS DOUBLE) AS gross_revenue_52w_eur,
      CAST(NULL AS DOUBLE) AS net_revenue_52w_eur,
      CAST(NULL AS BIGINT) AS count_orders_5w,
      CAST(NULL AS BIGINT) AS count_paid_orders_5w,
      CAST(NULL AS BIGINT) AS count_orders_10w,
      CAST(NULL AS BIGINT) AS count_paid_orders_10w,
      CAST(NULL AS BIGINT) AS count_orders_13w,
      CAST(NULL AS BIGINT) AS count_paid_orders_13w,
      CAST(NULL AS BIGINT) AS count_orders_26w,
      CAST(NULL AS BIGINT) AS count_paid_orders_26w,
      CAST(NULL AS BIGINT) AS count_orders_52w,
      CAST(NULL AS BIGINT) AS count_paid_orders_52w,
      CAST(NULL AS BIGINT) AS count_reactivations_5w,
      CAST(NULL AS BIGINT) AS count_reactivations_10w,
      CAST(NULL AS BIGINT) AS count_reactivations_13w,
      CAST(NULL AS BIGINT) AS count_reactivations_26w,
      CAST(NULL AS BIGINT) AS count_reactivations_52w,
      CURRENT_TIMESTAMP() AS last_modified_ts
    FROM
      ascs_base_with_cohorts
    """
    
    print("=" * 80)
    print("Creating ASCS Customer Attributes Table (Simplified - Base Data Only)")
    print("=" * 80)
    print("This creates the table structure with base data.")
    print("Cohort metrics are set to NULL for now - can be added later.")
    print("=" * 80)
    print()
    
    try:
        result = db.run_sql(simplified_query, display=False)
        print("✓ CREATE TABLE executed")
        
        # Check if table exists
        print("\nChecking if table exists...")
        count_result = db.run_sql("SELECT COUNT(*) as cnt FROM payments_hf.ascs_customer_attributes", display=True)
        if count_result:
            print(f"\n✓ SUCCESS: Table created with {count_result[0][0]} rows!")
            return 0
        else:
            print("\n✗ Table does not exist")
            return 1
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())






