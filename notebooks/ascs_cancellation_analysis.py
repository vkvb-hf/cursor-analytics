# Databricks notebook source
# MAGIC %md
# MAGIC # ASCS Cancellation Analysis - CSC Pattern
# MAGIC 
# MAGIC This analysis focuses on customers who:
# MAGIC 1. Were cancelled by ASCS (c)
# MAGIC 2. Reactivated with at least one successful payment/order delivery (s)
# MAGIC 3. Were cancelled again by ASCS (c)
# MAGIC 
# MAGIC Pattern: **%csc%** (cancelled → successful → cancelled)
# MAGIC 
# MAGIC **Note**: This analysis specifically excludes:
# MAGIC - %cc%: Customers who reactivated but were cancelled before any successful payment
# MAGIC - %cfc%: Customers who reactivated, had failed payments, then were cancelled

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Create customer_sequences table

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create or replace table with customer event sequences
# MAGIC CREATE OR REPLACE TABLE payments_hf_staging.customer_sequences AS
# MAGIC WITH cancellations AS (
# MAGIC     SELECT
# MAGIC         'c' as event_type,
# MAGIC         cs.customer_nk,
# MAGIC         cs.submitted_datetime as event_timestamp,
# MAGIC         MIN(cs.submitted_datetime) OVER (PARTITION BY cs.customer_nk) as first_cancellation_timestamp
# MAGIC     FROM global_bi_business.plan_cancellation_survey_hist cs
# MAGIC     WHERE LOWER(cs.answer) IN ('cc-failed-payments', 'cc-payment-chargeback')
# MAGIC       AND cs.submitted_datetime >= '2024-01-01'
# MAGIC       AND cs.submitted_datetime < '2026-01-01'
# MAGIC ),
# MAGIC 
# MAGIC orders AS (
# MAGIC     SELECT
# MAGIC         CASE 
# MAGIC             WHEN o.bob_status = 'money_received' AND o.box_shipped = 1 THEN 's'  -- successful order
# MAGIC             ELSE 'f'  -- failed order
# MAGIC         END as event_type,
# MAGIC         cd.customer_uuid as customer_nk,
# MAGIC         o.order_created_at as event_timestamp
# MAGIC     FROM payments_hf.f_orders o
# MAGIC     JOIN global_bi_business.customer_dimension cd
# MAGIC         ON o.country = cd.bob_entity_code
# MAGIC         AND o.customer_id = cd.customer_id
# MAGIC     WHERE o.order_created_at >= '2024-01-01'
# MAGIC ),
# MAGIC 
# MAGIC all_events AS (
# MAGIC     SELECT
# MAGIC         event_type,
# MAGIC         customer_nk,
# MAGIC         event_timestamp,
# MAGIC         first_cancellation_timestamp,
# MAGIC         CASE WHEN event_type = 'c' THEN 0 ELSE 1 END as event_priority
# MAGIC     FROM cancellations
# MAGIC     
# MAGIC     UNION ALL
# MAGIC     
# MAGIC     SELECT
# MAGIC         o.event_type,
# MAGIC         o.customer_nk,
# MAGIC         o.event_timestamp,
# MAGIC         c.first_cancellation_timestamp,
# MAGIC         1 as event_priority
# MAGIC     FROM orders o
# MAGIC     INNER JOIN (
# MAGIC         SELECT DISTINCT customer_nk, first_cancellation_timestamp
# MAGIC         FROM cancellations
# MAGIC     ) c ON o.customer_nk = c.customer_nk
# MAGIC ),
# MAGIC 
# MAGIC filtered_events AS (
# MAGIC     SELECT
# MAGIC         event_type,
# MAGIC         customer_nk,
# MAGIC         event_timestamp,
# MAGIC         first_cancellation_timestamp,
# MAGIC         event_priority
# MAGIC     FROM all_events
# MAGIC     WHERE event_timestamp >= first_cancellation_timestamp
# MAGIC ),
# MAGIC 
# MAGIC events_array AS (
# MAGIC     SELECT
# MAGIC         customer_nk,
# MAGIC         COLLECT_LIST(STRUCT(event_timestamp, event_priority, event_type)) as events
# MAGIC     FROM filtered_events
# MAGIC     GROUP BY customer_nk
# MAGIC ),
# MAGIC 
# MAGIC sorted_events_array AS (
# MAGIC     SELECT
# MAGIC         customer_nk,
# MAGIC         ARRAY_SORT(events, (left, right) ->
# MAGIC             CASE
# MAGIC                 WHEN left.event_timestamp < right.event_timestamp THEN -1
# MAGIC                 WHEN left.event_timestamp > right.event_timestamp THEN 1
# MAGIC                 WHEN left.event_priority < right.event_priority THEN -1
# MAGIC                 WHEN left.event_priority > right.event_priority THEN 1
# MAGIC                 ELSE 0
# MAGIC             END
# MAGIC         ) as sorted_events
# MAGIC     FROM events_array
# MAGIC ),
# MAGIC 
# MAGIC customer_sequences_base AS (
# MAGIC     SELECT
# MAGIC         customer_nk,
# MAGIC         CONCAT_WS('', TRANSFORM(sorted_events, x -> x.event_type)) as event_sequence,
# MAGIC         TRANSFORM(sorted_events, x -> STRUCT(x.event_timestamp as event_timestamp, x.event_type as event_type)) as event_details,
# MAGIC         SIZE(sorted_events) as total_events
# MAGIC     FROM sorted_events_array
# MAGIC ),
# MAGIC 
# MAGIC -- Get first cancellation info for year grouping
# MAGIC first_cancellation_info AS (
# MAGIC     SELECT
# MAGIC         customer_nk,
# MAGIC         first_cancellation_timestamp,
# MAGIC         YEAR(DATE(first_cancellation_timestamp)) as first_cancellation_year
# MAGIC     FROM (
# MAGIC         SELECT DISTINCT customer_nk, first_cancellation_timestamp
# MAGIC         FROM cancellations
# MAGIC     )
# MAGIC )
# MAGIC 
# MAGIC SELECT
# MAGIC     cs.customer_nk,
# MAGIC     cd.bob_entity_code,
# MAGIC     cd.customer_id,
# MAGIC     cs.event_sequence,
# MAGIC     cs.event_details,
# MAGIC     cs.total_events,
# MAGIC     fci.first_cancellation_timestamp,
# MAGIC     fci.first_cancellation_year
# MAGIC FROM customer_sequences_base cs
# MAGIC JOIN global_bi_business.customer_dimension cd
# MAGIC     ON cs.customer_nk = cd.customer_uuid
# MAGIC JOIN first_cancellation_info fci
# MAGIC     ON cs.customer_nk = fci.customer_nk

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Query CSC Pattern from customer_sequences table

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Count CSC pattern customers by year
# MAGIC SELECT
# MAGIC     first_cancellation_year as cancellation_year,
# MAGIC     COUNT(DISTINCT customer_nk) as csc_customers_count
# MAGIC FROM payments_hf_staging.customer_sequences
# MAGIC WHERE event_sequence LIKE '%csc%'  -- Pattern: cancelled → successful → cancelled
# MAGIC GROUP BY first_cancellation_year
# MAGIC ORDER BY first_cancellation_year

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3: Total CSC Pattern Count

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Total count across both years
# MAGIC SELECT
# MAGIC     'Total (2024 + 2025)' as period,
# MAGIC     COUNT(DISTINCT customer_nk) as csc_customers_count
# MAGIC FROM payments_hf_staging.customer_sequences
# MAGIC WHERE event_sequence LIKE '%csc%'

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 4: Example Queries for Granular Analysis
# MAGIC 
# MAGIC Now that we have the `customer_sequences` table, you can query it for more granular information:

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Example: View sample CSC customers with their event sequences
# MAGIC SELECT
# MAGIC     customer_nk,
# MAGIC     bob_entity_code,
# MAGIC     customer_id,
# MAGIC     event_sequence,
# MAGIC     total_events,
# MAGIC     first_cancellation_year
# MAGIC FROM payments_hf_staging.customer_sequences
# MAGIC WHERE event_sequence LIKE '%csc%'
# MAGIC LIMIT 20

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Example: Count by different patterns
# MAGIC SELECT
# MAGIC     CASE
# MAGIC         WHEN event_sequence LIKE '%csc%' THEN 'CSC Pattern'
# MAGIC         WHEN event_sequence LIKE '%cc%' AND event_sequence NOT LIKE '%csc%' THEN 'CC Pattern (no success)'
# MAGIC         WHEN event_sequence LIKE '%cfc%' THEN 'CFC Pattern'
# MAGIC         ELSE 'Other'
# MAGIC     END as pattern_type,
# MAGIC     COUNT(DISTINCT customer_nk) as customer_count
# MAGIC FROM payments_hf_staging.customer_sequences
# MAGIC GROUP BY pattern_type
# MAGIC ORDER BY customer_count DESC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Table Schema
# MAGIC 
# MAGIC The `payments_hf_staging.customer_sequences` table contains:
# MAGIC - `customer_nk`: Customer UUID
# MAGIC - `bob_entity_code`: Business unit/country
# MAGIC - `customer_id`: Customer ID
# MAGIC - `event_sequence`: String pattern of events (e.g., 'csc', 'cc', 'cfc', etc.)
# MAGIC - `event_details`: Array of structs with event_timestamp and event_type
# MAGIC - `total_events`: Total number of events in the sequence
# MAGIC - `first_cancellation_timestamp`: Timestamp of first ASCS cancellation
# MAGIC - `first_cancellation_year`: Year of first ASCS cancellation
# MAGIC 
# MAGIC **Pattern Definitions:**
# MAGIC - **c** = ASCS cancellation (cc-failed-payments or cc-payment-chargeback)
# MAGIC - **s** = Successful order (bob_status = 'money_received' AND box_shipped = 1)
# MAGIC - **f** = Failed order (any other order status)
# MAGIC 
# MAGIC **CSC Pattern**: Customers who were cancelled, then had at least one successful order, then were cancelled again.
