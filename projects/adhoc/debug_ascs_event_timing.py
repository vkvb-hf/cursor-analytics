"""
Debug ASCS Event Timing Analysis
Investigates why "assess" group cancellations changed from same-day to staggered timing.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from core.query_util import run_query

def main():
    print("=" * 80)
    print("ASCS Event Timing Debug Analysis")
    print("=" * 80)
    
    # Query 1: Check for multiple event timestamps per import_day
    query1 = """
    SELECT 
      import_day,
      DATE(event_timestamp) as event_date,
      COUNT(DISTINCT event_timestamp) as unique_event_times,
      MIN(event_timestamp) as first_event,
      MAX(event_timestamp) as last_event,
      DATEDIFF(HOUR, MIN(event_timestamp), MAX(event_timestamp)) as hours_spread,
      COUNT(DISTINCT customer_id) as customer_count
    FROM payments_hf.ascs_decision_service_simulation  
    WHERE experiment_exploration = 'assess'
      AND import_day IN (20251020, 20251120, 20251121)
    GROUP BY import_day, DATE(event_timestamp)
    ORDER BY import_day, event_date
    """
    
    print("\n" + "=" * 80)
    print("Query 1: Event Timestamp Distribution per Import Day")
    print("=" * 80)
    print("\nThis shows if events are generated in batches vs single run\n")
    
    run_query(query1, title="Event Timestamp Distribution")
    
    # Query 2: Detailed event timestamp distribution
    query2 = """
    SELECT 
      import_day,
      event_timestamp,
      COUNT(DISTINCT customer_id) as customers_in_batch,
      COUNT(DISTINCT subscription_id) as subscriptions_in_batch,
      MIN(days_before_delivery) as min_days_before,
      MAX(days_before_delivery) as max_days_before,
      MIN(next_delivery_date) as earliest_delivery,
      MAX(next_delivery_date) as latest_delivery
    FROM payments_hf.ascs_decision_service_simulation
    WHERE experiment_exploration = 'assess'
      AND import_day IN (20251020, 20251120, 20251121)
    GROUP BY import_day, event_timestamp
    ORDER BY import_day, event_timestamp
    LIMIT 50
    """
    
    print("\n" + "=" * 80)
    print("Query 2: Event Batch Details")
    print("=" * 80)
    print("\nThis shows characteristics of each event batch\n")
    
    run_query(query2, title="Event Batch Details")
    
    # Query 3: Check if subscription_cancellation_data job run times changed
    query3 = """
    SELECT 
      import_day,
      COUNT(DISTINCT DATE(event_timestamp)) as unique_event_dates,
      COUNT(DISTINCT HOUR(event_timestamp)) as unique_event_hours,
      MIN(DATE(event_timestamp)) as first_event_date,
      MAX(DATE(event_timestamp)) as last_event_date,
      MIN(HOUR(event_timestamp)) as earliest_hour,
      MAX(HOUR(event_timestamp)) as latest_hour,
      COUNT(DISTINCT customer_id) as total_customers
    FROM payments_hf.f_subscription_cancellation_data
    WHERE business_unit = 'DE'
      AND import_day IN (20251020, 20251120, 20251121)
    GROUP BY import_day
    ORDER BY import_day
    """
    
    print("\n" + "=" * 80)
    print("Query 3: Source Data Event Generation Times")
    print("=" * 80)
    print("\nThis checks the raw Kafka events from f_subscription_cancellation_data\n")
    
    run_query(query3, title="Source Data Event Generation Times")
    
    # Query 4: Sample actual event timestamps
    query4 = """
    SELECT 
      import_day,
      event_timestamp,
      customer_id,
      subscription_id,
      days_before_delivery,
      next_delivery_date,
      experiment_exploration
    FROM payments_hf.ascs_decision_service_simulation
    WHERE experiment_exploration = 'assess'
      AND import_day IN (20251020, 20251120)
      AND customer_id IN (
        SELECT customer_id 
        FROM payments_hf.ascs_decision_service_simulation 
        WHERE experiment_exploration = 'assess' 
          AND import_day = 20251120 
        LIMIT 5
      )
    ORDER BY import_day, customer_id, event_timestamp
    """
    
    print("\n" + "=" * 80)
    print("Query 4: Sample Customer Event Timestamps")
    print("=" * 80)
    print("\nThis shows specific examples of event timing for same customers\n")
    
    run_query(query4, title="Sample Customer Event Timestamps")
    
    print("\n" + "=" * 80)
    print("Analysis Complete")
    print("=" * 80)
    print("\n📊 Key Things to Look For:")
    print("1. Query 1: Multiple event timestamps per import_day = batched processing")
    print("2. Query 2: Different event_timestamps = events generated at different times")
    print("3. Query 3: Source data timing - when Kafka events were actually created")
    print("4. Query 4: Specific examples showing event timing patterns")
    print("\n💡 Expected Finding:")
    print("November should show MULTIPLE event timestamps per import_day,")
    print("while October should show a SINGLE event timestamp.")
    print("=" * 80)

if __name__ == "__main__":
    main()

