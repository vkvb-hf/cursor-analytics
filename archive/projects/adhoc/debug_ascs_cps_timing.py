"""
Debug ASCS vs CPS Timing
Compare when ASCS marked subscriptions as cancelled vs when CPS executed them
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from core.query_util import run_query

def main():
    print("=" * 80)
    print("ASCS vs CPS Timing Analysis")
    print("=" * 80)
    
    # Query 1: Check if we have access to ASCS subscription_to_cancel table
    query1 = """
    -- Check for ASCS internal tables
    SHOW TABLES IN payments_hf LIKE '*subscription*cancel*'
    """
    
    print("\n" + "=" * 80)
    print("Query 1: Find ASCS subscription_to_cancel table")
    print("=" * 80)
    
    run_query(query1, title="Available Tables")
    
    # Query 2: Compare simulation event time vs actual cancellation time
    # Using plan_cancellation_survey_hist which captures when CPS executed
    query2 = """
    WITH simulation AS (
      SELECT 
        customer_id,
        subscription_id,
        country,
        experiment_exploration,
        DATE(event_timestamp) AS simulation_date,
        event_timestamp AS simulation_timestamp,
        next_delivery_date,
        days_before_delivery,
        import_day
      FROM payments_hf.ascs_decision_service_simulation
      WHERE experiment_exploration = 'assess'
        AND import_day IN (20251020, 20251120)
    ),
    
    actual_cancellations AS (
      SELECT 
        CAST(cd.customer_id AS BIGINT) AS customer_id,
        cs.country,
        from_unixtime(cs.utc_timestamp) AS cps_execution_timestamp,
        DATE(from_unixtime(cs.utc_timestamp)) AS cps_execution_date,
        cs.answer AS cancellation_reason
      FROM global_bi_business.plan_cancellation_survey_hist cs
      JOIN public_edw_base_grain_live.customer cd
        ON cs.customer_nk = cd.customer_uuid
        AND cs.country = cd.bob_entity_code
      WHERE LOWER(cs.answer) IN ('cc-failed-payments', 'cc-payment-chargeback')
        AND cs.submitted_datetime >= '2025-10-01'
    )
    
    SELECT 
      s.import_day,
      s.simulation_date,
      s.next_delivery_date,
      a.cps_execution_date,
      DATEDIFF(a.cps_execution_date, s.simulation_date) AS days_from_simulation_to_cps,
      DATEDIFF(a.cps_execution_date, s.next_delivery_date) AS days_from_delivery_to_cps,
      COUNT(DISTINCT s.customer_id) AS customer_count
    FROM simulation s
    JOIN actual_cancellations a
      ON s.customer_id = a.customer_id
      AND s.country = a.country
    GROUP BY 1,2,3,4,5,6
    ORDER BY s.import_day, s.simulation_date, s.next_delivery_date, a.cps_execution_date
    """
    
    print("\n" + "=" * 80)
    print("Query 2: Simulation Date vs CPS Execution Date")
    print("=" * 80)
    print("\nThis shows the gap between when ASCS decided to cancel vs when CPS executed\n")
    
    run_query(query2, title="Simulation vs CPS Execution Timing")
    
    # Query 3: Summary by import_day
    query3 = """
    WITH simulation AS (
      SELECT 
        customer_id,
        subscription_id,
        country,
        experiment_exploration,
        DATE(event_timestamp) AS simulation_date,
        next_delivery_date,
        import_day
      FROM payments_hf.ascs_decision_service_simulation
      WHERE experiment_exploration = 'assess'
        AND import_day IN (20251020, 20251120)
    ),
    
    actual_cancellations AS (
      SELECT 
        CAST(cd.customer_id AS BIGINT) AS customer_id,
        cs.country,
        DATE(from_unixtime(cs.utc_timestamp)) AS cps_execution_date
      FROM global_bi_business.plan_cancellation_survey_hist cs
      JOIN public_edw_base_grain_live.customer cd
        ON cs.customer_nk = cd.customer_uuid
        AND cs.country = cd.bob_entity_code
      WHERE LOWER(cs.answer) IN ('cc-failed-payments', 'cc-payment-chargeback')
        AND cs.submitted_datetime >= '2025-10-01'
    )
    
    SELECT 
      s.import_day,
      COUNT(DISTINCT s.customer_id) AS total_customers,
      COUNT(DISTINCT CASE WHEN a.cps_execution_date = s.simulation_date THEN s.customer_id END) AS cancelled_same_day_as_simulation,
      COUNT(DISTINCT CASE WHEN a.cps_execution_date = s.next_delivery_date THEN s.customer_id END) AS cancelled_on_delivery_date,
      COUNT(DISTINCT CASE WHEN a.cps_execution_date > s.simulation_date THEN s.customer_id END) AS cancelled_after_simulation,
      ROUND(AVG(DATEDIFF(a.cps_execution_date, s.simulation_date)), 2) AS avg_days_from_simulation_to_cps
    FROM simulation s
    JOIN actual_cancellations a
      ON s.customer_id = a.customer_id
      AND s.country = a.country
    GROUP BY s.import_day
    ORDER BY s.import_day
    """
    
    print("\n" + "=" * 80)
    print("Query 3: Summary - When did CPS execute vs Simulation?")
    print("=" * 80)
    
    run_query(query3, title="CPS Execution Timing Summary")
    
    # Query 4: Check if CPS execution aligns with delivery date in November
    query4 = """
    WITH simulation AS (
      SELECT 
        customer_id,
        country,
        DATE(event_timestamp) AS simulation_date,
        next_delivery_date,
        import_day
      FROM payments_hf.ascs_decision_service_simulation
      WHERE experiment_exploration = 'assess'
        AND import_day = 20251120
        AND next_delivery_date IS NOT NULL
    ),
    
    actual_cancellations AS (
      SELECT 
        CAST(cd.customer_id AS BIGINT) AS customer_id,
        cs.country,
        DATE(from_unixtime(cs.utc_timestamp)) AS cps_execution_date
      FROM global_bi_business.plan_cancellation_survey_hist cs
      JOIN public_edw_base_grain_live.customer cd
        ON cs.customer_nk = cd.customer_uuid
        AND cs.country = cd.bob_entity_code
      WHERE LOWER(cs.answer) IN ('cc-failed-payments', 'cc-payment-chargeback')
        AND cs.submitted_datetime >= '2025-11-01'
    )
    
    SELECT 
      'November 2025' AS period,
      CASE 
        WHEN a.cps_execution_date = s.next_delivery_date THEN 'CPS executed ON delivery date'
        WHEN a.cps_execution_date < s.next_delivery_date THEN 'CPS executed BEFORE delivery date'
        WHEN a.cps_execution_date > s.next_delivery_date THEN 'CPS executed AFTER delivery date'
        ELSE 'Unknown'
      END AS timing_pattern,
      COUNT(DISTINCT s.customer_id) AS customer_count,
      ROUND(100.0 * COUNT(DISTINCT s.customer_id) / SUM(COUNT(DISTINCT s.customer_id)) OVER(), 2) AS percentage
    FROM simulation s
    JOIN actual_cancellations a
      ON s.customer_id = a.customer_id
      AND s.country = a.country
    GROUP BY 1, 2
    ORDER BY customer_count DESC
    """
    
    print("\n" + "=" * 80)
    print("Query 4: November - Does CPS Execution Align with Delivery Date?")
    print("=" * 80)
    
    run_query(query4, title="November CPS vs Delivery Date Alignment")
    
    print("\n" + "=" * 80)
    print("Analysis Complete")
    print("=" * 80)
    print("\n💡 Key Insights to Look For:")
    print("1. October: CPS execution should be SAME DAY as simulation (immediate)")
    print("2. November: CPS execution should ALIGN with delivery dates (scheduled)")
    print("3. If true, this confirms CPS changed to delivery-date-based execution")
    print("=" * 80)

if __name__ == "__main__":
    main()






