# Databricks notebook source
# MAGIC %md
# MAGIC # [PY-3350] ASCS Dashboard - Debug Query
# MAGIC 
# MAGIC This notebook debugs the ASCS customer attributes query by creating temporary tables for each CTE.
# MAGIC We'll create intermediate tables to identify where the issue is.
# MAGIC 
# MAGIC **Date Filter:** 2025-11-01

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Date Lookup Tables

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.temp_20251201_date_lkup;
# MAGIC 
# MAGIC CREATE TABLE payments_hf.temp_20251201_date_lkup AS
# MAGIC SELECT
# MAGIC   hellofresh_week,
# MAGIC   CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS hellofresh_year_month,
# MAGIC   CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS hellofresh_year_quarter
# MAGIC FROM
# MAGIC   dimensions.date_dimension dd
# MAGIC WHERE
# MAGIC   hellofresh_week >= '2023-W01'
# MAGIC GROUP BY
# MAGIC   1, 2, 3;
# MAGIC 
# MAGIC SELECT COUNT(*) as row_count FROM payments_hf.temp_20251201_date_lkup;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.temp_20251201_date_lkup_row;
# MAGIC 
# MAGIC CREATE TABLE payments_hf.temp_20251201_date_lkup_row AS
# MAGIC SELECT
# MAGIC   *,
# MAGIC   ROW_NUMBER() OVER(ORDER BY hellofresh_week ASC) AS row_num
# MAGIC FROM
# MAGIC   payments_hf.temp_20251201_date_lkup;
# MAGIC 
# MAGIC SELECT COUNT(*) as row_count FROM payments_hf.temp_20251201_date_lkup_row;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.temp_20251201_final_date_lkup;
# MAGIC 
# MAGIC CREATE TABLE payments_hf.temp_20251201_final_date_lkup AS
# MAGIC SELECT
# MAGIC   a.hellofresh_week,
# MAGIC   b.hellofresh_week AS lead_hellofresh_week_5wks,
# MAGIC   c.hellofresh_week AS lead_hellofresh_week_10wks,
# MAGIC   d.hellofresh_week AS lead_hellofresh_week_13wks,
# MAGIC   e.hellofresh_week AS lead_hellofresh_week_26wks,
# MAGIC   f.hellofresh_week AS lead_hellofresh_week_52wks
# MAGIC FROM
# MAGIC   payments_hf.temp_20251201_date_lkup_row a
# MAGIC   LEFT JOIN payments_hf.temp_20251201_date_lkup_row b ON a.row_num = b.row_num - 5
# MAGIC   LEFT JOIN payments_hf.temp_20251201_date_lkup_row c ON a.row_num = c.row_num - 10
# MAGIC   LEFT JOIN payments_hf.temp_20251201_date_lkup_row d ON a.row_num = d.row_num - 13
# MAGIC   LEFT JOIN payments_hf.temp_20251201_date_lkup_row e ON a.row_num = e.row_num - 26
# MAGIC   LEFT JOIN payments_hf.temp_20251201_date_lkup_row f ON a.row_num = f.row_num - 52;
# MAGIC 
# MAGIC SELECT COUNT(*) as row_count FROM payments_hf.temp_20251201_final_date_lkup;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: ASCS Experiment Base

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.temp_20251201_ascs_experiment_base;
# MAGIC 
# MAGIC CREATE TABLE payments_hf.temp_20251201_ascs_experiment_base AS
# MAGIC SELECT
# MAGIC   business_unit AS country,
# MAGIC   details.customer_id,
# MAGIC   details.subscription_id,
# MAGIC   details.customer_plan_id,
# MAGIC   details.loyalty,
# MAGIC   'ASCS (PAYS-3159)' AS exp_name,
# MAGIC   dd.date_string_backwards AS allocation_time,
# MAGIC   dd.hellofresh_week AS allocation_hf_week,
# MAGIC   details.experiment_exploration AS variation_name,
# MAGIC   details.subscription_canceled AS is_canceled,
# MAGIC   details.is_test,
# MAGIC   TRUE AS is_experiment,
# MAGIC   details.subscription_canceled AS is_ascs_cancellation
# MAGIC FROM
# MAGIC   payments_hf.f_subscription_cancellation_data scd
# MAGIC   JOIN dimensions.date_dimension dd ON scd.import_day = dd.sk_date
# MAGIC WHERE
# MAGIC   1 = 1
# MAGIC   AND details.experiment_exploration IS NOT NULL
# MAGIC   AND import_day >= 20231110
# MAGIC   AND DATE(dd.date_string_backwards) = '2025-11-01';
# MAGIC 
# MAGIC SELECT COUNT(*) as row_count FROM payments_hf.temp_20251201_ascs_experiment_base;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3: ASCS Cancellation Survey

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.temp_20251201_ascs_cancellation_survey;
# MAGIC 
# MAGIC CREATE TABLE payments_hf.temp_20251201_ascs_cancellation_survey AS
# MAGIC SELECT
# MAGIC   'c' AS event_type,
# MAGIC   cs.customer_nk,
# MAGIC   cs.submitted_datetime AS event_timestamp,
# MAGIC   cs.country,
# MAGIC   MIN(cs.submitted_datetime) OVER (PARTITION BY cs.customer_nk) AS first_cancellation_timestamp
# MAGIC FROM
# MAGIC   global_bi_business.plan_cancellation_survey_hist cs
# MAGIC WHERE
# MAGIC   LOWER(cs.answer) IN ('cc-failed-payments', 'cc-payment-chargeback')
# MAGIC   AND cs.submitted_datetime >= '2025-01-01'
# MAGIC   AND DATE(cs.submitted_datetime) = '2025-11-01'
# MAGIC LIMIT 100;
# MAGIC 
# MAGIC SELECT COUNT(*) as row_count FROM payments_hf.temp_20251201_ascs_cancellation_survey;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 4: ASCS Cancellation with Customer

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.temp_20251201_ascs_cancellation_with_customer;
# MAGIC 
# MAGIC CREATE TABLE payments_hf.temp_20251201_ascs_cancellation_with_customer AS
# MAGIC SELECT
# MAGIC   acs.country,
# MAGIC   CAST(cd.customer_id AS BIGINT) AS customer_id,
# MAGIC   acs.customer_nk,
# MAGIC   acs.event_timestamp,
# MAGIC   acs.first_cancellation_timestamp,
# MAGIC   dd.date_string_backwards AS cancellation_date,
# MAGIC   dd.hellofresh_week AS cancellation_hf_week
# MAGIC FROM
# MAGIC   payments_hf.temp_20251201_ascs_cancellation_survey acs
# MAGIC   JOIN public_edw_base_grain_live.customer cd
# MAGIC     ON acs.customer_nk = cd.customer_uuid
# MAGIC     AND acs.country = cd.bob_entity_code
# MAGIC   JOIN dimensions.date_dimension dd
# MAGIC     ON DATE(acs.event_timestamp) = DATE(dd.date_string_backwards);
# MAGIC 
# MAGIC SELECT COUNT(*) as row_count FROM payments_hf.temp_20251201_ascs_cancellation_with_customer;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 5: ASCS Cancellation Base

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.temp_20251201_ascs_cancellation_base;
# MAGIC 
# MAGIC CREATE TABLE payments_hf.temp_20251201_ascs_cancellation_base AS
# MAGIC SELECT
# MAGIC   ac.country,
# MAGIC   ac.customer_id,
# MAGIC   COALESCE(scd.details.subscription_id, NULL) AS subscription_id,
# MAGIC   COALESCE(scd.details.customer_plan_id, NULL) AS customer_plan_id,
# MAGIC   COALESCE(scd.details.loyalty, 0) AS loyalty,
# MAGIC   NULL AS exp_name,
# MAGIC   ac.cancellation_date AS cancellation_time,
# MAGIC   ac.cancellation_hf_week,
# MAGIC   NULL AS variation_name,
# MAGIC   COALESCE(scd.details.subscription_canceled, FALSE) AS is_canceled,
# MAGIC   COALESCE(scd.details.is_test, FALSE) AS is_test,
# MAGIC   FALSE AS is_experiment,
# MAGIC   TRUE AS is_ascs_cancellation,
# MAGIC   CASE
# MAGIC     WHEN scd.details.subscription_canceled = TRUE THEN TRUE
# MAGIC     ELSE FALSE
# MAGIC   END AS flag_subscription_canceled_matches
# MAGIC FROM
# MAGIC   payments_hf.temp_20251201_ascs_cancellation_with_customer ac
# MAGIC   LEFT JOIN dimensions.date_dimension dd_cancel
# MAGIC     ON DATE(ac.cancellation_date) = DATE(dd_cancel.date_string_backwards)
# MAGIC   LEFT JOIN payments_hf.f_subscription_cancellation_data scd
# MAGIC     ON ac.country = scd.business_unit
# MAGIC     AND ac.customer_id = scd.details.customer_id
# MAGIC     AND scd.import_day = dd_cancel.sk_date
# MAGIC     AND (scd.details.experiment_exploration IS NULL OR scd.details.experiment_exploration = '');
# MAGIC 
# MAGIC SELECT COUNT(*) as row_count FROM payments_hf.temp_20251201_ascs_cancellation_base;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 6: ASCS Combined Base

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.temp_20251201_ascs_combined_base;
# MAGIC 
# MAGIC CREATE TABLE payments_hf.temp_20251201_ascs_combined_base AS
# MAGIC SELECT
# MAGIC   country,
# MAGIC   customer_id,
# MAGIC   subscription_id,
# MAGIC   customer_plan_id,
# MAGIC   loyalty,
# MAGIC   exp_name,
# MAGIC   allocation_time AS event_date,
# MAGIC   allocation_hf_week AS event_hf_week,
# MAGIC   variation_name,
# MAGIC   is_canceled,
# MAGIC   is_test,
# MAGIC   is_experiment,
# MAGIC   is_ascs_cancellation,
# MAGIC   NULL AS flag_subscription_canceled_matches
# MAGIC FROM
# MAGIC   payments_hf.temp_20251201_ascs_experiment_base
# MAGIC 
# MAGIC UNION ALL
# MAGIC 
# MAGIC SELECT
# MAGIC   country,
# MAGIC   customer_id,
# MAGIC   subscription_id,
# MAGIC   customer_plan_id,
# MAGIC   loyalty,
# MAGIC   exp_name,
# MAGIC   cancellation_time AS event_date,
# MAGIC   cancellation_hf_week AS event_hf_week,
# MAGIC   variation_name,
# MAGIC   is_canceled,
# MAGIC   is_test,
# MAGIC   is_experiment,
# MAGIC   is_ascs_cancellation,
# MAGIC   flag_subscription_canceled_matches
# MAGIC FROM
# MAGIC   payments_hf.temp_20251201_ascs_cancellation_base;
# MAGIC 
# MAGIC SELECT COUNT(*) as row_count FROM payments_hf.temp_20251201_ascs_combined_base;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 7: ASCS Unique Base

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.temp_20251201_ascs_unique_base;
# MAGIC 
# MAGIC CREATE TABLE payments_hf.temp_20251201_ascs_unique_base AS
# MAGIC SELECT
# MAGIC   country,
# MAGIC   customer_id,
# MAGIC   subscription_id,
# MAGIC   customer_plan_id,
# MAGIC   loyalty,
# MAGIC   exp_name,
# MAGIC   event_date,
# MAGIC   event_hf_week,
# MAGIC   MAX(variation_name) AS variation_name,
# MAGIC   MAX(is_canceled) AS flag_is_canceled,
# MAGIC   MAX(is_test) AS flag_is_test,
# MAGIC   MAX(is_experiment) AS flag_is_experiment,
# MAGIC   MAX(is_ascs_cancellation) AS flag_is_ascs_cancellation,
# MAGIC   MAX(flag_subscription_canceled_matches) AS flag_subscription_canceled_matches,
# MAGIC   ROW_NUMBER() OVER(
# MAGIC     PARTITION BY country, customer_id, event_date
# MAGIC     ORDER BY event_date DESC
# MAGIC   ) AS rn
# MAGIC FROM
# MAGIC   payments_hf.temp_20251201_ascs_combined_base
# MAGIC WHERE
# MAGIC   is_test = FALSE
# MAGIC GROUP BY
# MAGIC   country, customer_id, subscription_id, customer_plan_id, loyalty, exp_name, event_date, event_hf_week;
# MAGIC 
# MAGIC SELECT COUNT(*) as row_count, COUNT(*) FILTER (WHERE rn = 1) as unique_count 
# MAGIC FROM payments_hf.temp_20251201_ascs_unique_base;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 8: ASCS Base with Cohorts

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.temp_20251201_ascs_base_with_cohorts;
# MAGIC 
# MAGIC CREATE TABLE payments_hf.temp_20251201_ascs_base_with_cohorts AS
# MAGIC SELECT
# MAGIC   a.*,
# MAGIC   b.lead_hellofresh_week_5wks,
# MAGIC   b.lead_hellofresh_week_10wks,
# MAGIC   b.lead_hellofresh_week_13wks,
# MAGIC   b.lead_hellofresh_week_26wks,
# MAGIC   b.lead_hellofresh_week_52wks
# MAGIC FROM
# MAGIC   payments_hf.temp_20251201_ascs_unique_base a
# MAGIC   JOIN payments_hf.temp_20251201_final_date_lkup b ON a.event_hf_week = b.hellofresh_week
# MAGIC WHERE
# MAGIC   a.rn = 1
# MAGIC   AND DATE(a.event_date) = '2025-11-01';
# MAGIC 
# MAGIC SELECT COUNT(*) as row_count FROM payments_hf.temp_20251201_ascs_base_with_cohorts;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 9: Financial Till Date

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.temp_20251201_financial_till_date;
# MAGIC 
# MAGIC CREATE TABLE payments_hf.temp_20251201_financial_till_date AS
# MAGIC SELECT
# MAGIC   a.country,
# MAGIC   a.customer_id,
# MAGIC   a.event_date,
# MAGIC   a.event_hf_week,
# MAGIC   MAX(c.profit_check_cumulative_eur) AS profit_check_till_date_eur,
# MAGIC   MAX(c.gross_revenue_cumulative_eur) AS gross_revenue_till_date_eur,
# MAGIC   MAX(c.net_revenue_cumulative_eur) AS net_revenue_till_date_eur,
# MAGIC   MAX(c.discount_cumulative_eur) AS discount_till_date_eur,
# MAGIC   MAX(c.profit_cumulative_eur) AS profit_till_date_eur,
# MAGIC   MAX(c.count_orders_cumulative) AS count_orders_till_date,
# MAGIC   MAX(c.reactivations_to_date) AS reactivations_till_date
# MAGIC FROM
# MAGIC   payments_hf.temp_20251201_ascs_base_with_cohorts a
# MAGIC   LEFT JOIN payments_hf.customer_cohort_roi c
# MAGIC     ON a.country = c.country
# MAGIC     AND a.customer_id = c.customer_id
# MAGIC     AND c.hf_delivery_week <= a.event_hf_week
# MAGIC GROUP BY
# MAGIC   a.country, a.customer_id, a.event_date, a.event_hf_week;
# MAGIC 
# MAGIC SELECT COUNT(*) as row_count FROM payments_hf.temp_20251201_financial_till_date;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 10: Summary - Check Why No Records
# MAGIC 
# MAGIC Let's analyze each step to see where records are lost

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC   'date_lkup' as step,
# MAGIC   COUNT(*) as row_count
# MAGIC FROM payments_hf.temp_20251201_date_lkup
# MAGIC 
# MAGIC UNION ALL
# MAGIC 
# MAGIC SELECT 
# MAGIC   'experiment_base' as step,
# MAGIC   COUNT(*) as row_count
# MAGIC FROM payments_hf.temp_20251201_ascs_experiment_base
# MAGIC 
# MAGIC UNION ALL
# MAGIC 
# MAGIC SELECT 
# MAGIC   'cancellation_survey' as step,
# MAGIC   COUNT(*) as row_count
# MAGIC FROM payments_hf.temp_20251201_ascs_cancellation_survey
# MAGIC 
# MAGIC UNION ALL
# MAGIC 
# MAGIC SELECT 
# MAGIC   'cancellation_with_customer' as step,
# MAGIC   COUNT(*) as row_count
# MAGIC FROM payments_hf.temp_20251201_ascs_cancellation_with_customer
# MAGIC 
# MAGIC UNION ALL
# MAGIC 
# MAGIC SELECT 
# MAGIC   'cancellation_base' as step,
# MAGIC   COUNT(*) as row_count
# MAGIC FROM payments_hf.temp_20251201_ascs_cancellation_base
# MAGIC 
# MAGIC UNION ALL
# MAGIC 
# MAGIC SELECT 
# MAGIC   'combined_base' as step,
# MAGIC   COUNT(*) as row_count
# MAGIC FROM payments_hf.temp_20251201_ascs_combined_base
# MAGIC 
# MAGIC UNION ALL
# MAGIC 
# MAGIC SELECT 
# MAGIC   'unique_base' as step,
# MAGIC   COUNT(*) as row_count
# MAGIC FROM payments_hf.temp_20251201_ascs_unique_base
# MAGIC 
# MAGIC UNION ALL
# MAGIC 
# MAGIC SELECT 
# MAGIC   'base_with_cohorts' as step,
# MAGIC   COUNT(*) as row_count
# MAGIC FROM payments_hf.temp_20251201_ascs_base_with_cohorts
# MAGIC 
# MAGIC UNION ALL
# MAGIC 
# MAGIC SELECT 
# MAGIC   'financial_till_date' as step,
# MAGIC   COUNT(*) as row_count
# MAGIC FROM payments_hf.temp_20251201_financial_till_date
# MAGIC 
# MAGIC ORDER BY step;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 11: Check Sample Data

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM payments_hf.temp_20251201_ascs_experiment_base LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM payments_hf.temp_20251201_ascs_cancellation_survey LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM payments_hf.temp_20251201_ascs_base_with_cohorts LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 12: Analyze Date Filtering
# MAGIC 
# MAGIC Check if the date filter is causing issues

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Check what dates are actually in the experiment base
# MAGIC SELECT 
# MAGIC   DATE(allocation_time) as allocation_date,
# MAGIC   COUNT(*) as cnt
# MAGIC FROM payments_hf.temp_20251201_ascs_experiment_base
# MAGIC GROUP BY 1
# MAGIC ORDER BY 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Check unique base after date filter
# MAGIC SELECT 
# MAGIC   DATE(event_date) as event_date,
# MAGIC   COUNT(*) as cnt,
# MAGIC   COUNT(DISTINCT customer_id) as distinct_customers
# MAGIC FROM payments_hf.temp_20251201_ascs_unique_base
# MAGIC WHERE rn = 1
# MAGIC   AND DATE(event_date) = '2025-11-01'
# MAGIC GROUP BY 1;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Debug Complete
# MAGIC 
# MAGIC Review the record counts at each step to identify where data is lost.






