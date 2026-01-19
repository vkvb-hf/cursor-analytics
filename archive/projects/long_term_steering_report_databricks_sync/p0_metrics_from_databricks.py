# Databricks notebook source
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.payments_p0_metrics_checkout_funnel;
# MAGIC
# MAGIC REFRESH TABLE payments_hf.fact_payment_conversion_rate;
# MAGIC REFRESH TABLE dimensions.date_dimension;
# MAGIC REFRESH TABLE payments_hf.checkout_customer_actuals;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE payments_hf.payments_p0_metrics_checkout_funnel AS WITH union_all_base AS (
# MAGIC SELECT
# MAGIC   a.country,
# MAGIC   a.customer_id,
# MAGIC   DATE(a.date_string_backwards) AS date_string_backwards,
# MAGIC   a.channel,
# MAGIC   CASE
# MAGIC     WHEN a.channel IN (
# MAGIC       'Freebies',
# MAGIC       'Freebies Offline',
# MAGIC       'Freebies Online',
# MAGIC       'HelloShare',
# MAGIC       'HelloShare Online',
# MAGIC       'Organic Referral',
# MAGIC       'Referral (Organic Non-Social)'
# MAGIC     ) THEN 'Referral'
# MAGIC     ELSE 'Paid'
# MAGIC   END AS category,
# MAGIC   a.asset,
# MAGIC   a.device,
# MAGIC   a.browser,
# MAGIC   a.payment_method,
# MAGIC   CASE 
# MAGIC     WHEN a.payment_method LIKE '%ApplePay' THEN 'Apple Pay'
# MAGIC     WHEN a.payment_method LIKE '%Paypal' THEN 'Paypal'
# MAGIC     WHEN a.payment_method LIKE '%CreditCard' THEN 'Credit Card'
# MAGIC     WHEN a.payment_method IN ('No payment method', 'undefined') THEN 'Unknown'
# MAGIC     WHEN a.payment_method IS NULL THEN 'Unknown'
# MAGIC     ELSE 'Others' 
# MAGIC   END AS payment_method_reporting,  
# MAGIC   a.is_pay_visit,
# MAGIC   a.is_select,
# MAGIC   a.is_click,
# MAGIC   a.is_fs_check,
# MAGIC   NULL AS is_voucher_fraud_block,
# MAGIC   NULL AS is_payment_fraud_block,
# MAGIC   a.is_success,
# MAGIC   a.is_pvs,
# MAGIC   a.is_different_checkout,
# MAGIC   NULL as is_duplicate_at_pre_checkout,
# MAGIC   NULL as is_duplicate_at_post_checkout,
# MAGIC   NULL as is_post_checkout_block
# MAGIC FROM
# MAGIC   payments_hf.fact_payment_conversion_rate AS a
# MAGIC
# MAGIC UNION ALL
# MAGIC
# MAGIC SELECT
# MAGIC   a.business_unit AS country,
# MAGIC   a.customer_id,
# MAGIC   DATE(a.checkout_date) AS date_string_backwards,
# MAGIC   NULL AS channel,
# MAGIC   a.category AS category,
# MAGIC   NULL AS asset,
# MAGIC   NULL AS device,
# MAGIC   NULL AS browser,
# MAGIC   NULL AS payment_method,
# MAGIC   NULL AS payment_method_reporting,  
# MAGIC   NULL AS is_pay_visit,
# MAGIC   NULL AS is_select,
# MAGIC   NULL AS is_click,
# MAGIC   1 AS is_fs_check,
# MAGIC   is_fs_blocked AS is_voucher_fraud_block,
# MAGIC   CASE 
# MAGIC     WHEN (COALESCE(a.is_checkout_blocked, FALSE) AND COALESCE(a.is_payment_fraud, FALSE)) THEN 1 
# MAGIC     ELSE 0 
# MAGIC   END AS is_payment_fraud_block,
# MAGIC   NULL AS is_success,
# MAGIC   NULL AS is_pvs,
# MAGIC   0 AS is_different_checkout,
# MAGIC   coalesce(a.is_checkout_duplicate, false) as is_duplicate_at_pre_checkout, -- spider rollout Edit: May 28, 2025
# MAGIC   coalesce(a.is_vaq_v1_duplicate, false) as is_duplicate_at_post_checkout,
# MAGIC   coalesce(a.is_vaq_blocked, false) as is_post_checkout_block
# MAGIC FROM
# MAGIC   payments_hf.checkout_customer_actuals AS a
# MAGIC WHERE is_actual
# MAGIC )
# MAGIC , base AS (
# MAGIC   SELECT
# MAGIC   country,
# MAGIC   customer_id,
# MAGIC   date_string_backwards,
# MAGIC   MAX(channel) AS channel,
# MAGIC   MAX(category) AS category,
# MAGIC   MAX(asset) AS asset,
# MAGIC   MAX(device) AS device,
# MAGIC   MAX(browser) AS browser,
# MAGIC   MAX(payment_method) AS payment_method,
# MAGIC   COALESCE(MAX(payment_method_reporting), 'Unknown') AS payment_method_reporting,  
# MAGIC   MAX(is_pay_visit) AS is_pay_visit,
# MAGIC   MAX(is_select) AS is_select,
# MAGIC   MAX(is_click) AS is_click,
# MAGIC   MAX(is_fs_check) AS is_fs_check,
# MAGIC   MAX(is_voucher_fraud_block) AS is_voucher_fraud_block,
# MAGIC   MAX(is_payment_fraud_block) AS is_payment_fraud_block,
# MAGIC   MAX(is_success) AS is_success,
# MAGIC   MAX(is_pvs) AS is_pvs,
# MAGIC   MAX(is_different_checkout) AS is_different_checkout,
# MAGIC   MAX(is_duplicate_at_pre_checkout) as is_duplicate_at_pre_checkout,
# MAGIC   MAX(is_duplicate_at_post_checkout) as is_duplicate_at_post_checkout,
# MAGIC   MAX(is_post_checkout_block) as is_post_checkout_block
# MAGIC
# MAGIC   FROM union_all_base
# MAGIC
# MAGIC   GROUP BY
# MAGIC   All
# MAGIC
# MAGIC )
# MAGIC SELECT
# MAGIC   -- a.*,
# MAGIC   dd.iso_year_week AS hellofresh_week,
# MAGIC   CONCAT(dd.year, '-', dd.month) AS hellofresh_year_month,
# MAGIC   CONCAT(dd.year, '-', dd.quarter) AS hellofresh_year_quarter,
# MAGIC   country,
# MAGIC   customer_id,
# MAGIC   a.date_string_backwards,
# MAGIC   channel,
# MAGIC   category,
# MAGIC   asset,
# MAGIC   device,
# MAGIC   browser,
# MAGIC   payment_method,
# MAGIC   payment_method_reporting,  
# MAGIC   is_pay_visit,
# MAGIC   is_select,
# MAGIC   is_click,
# MAGIC   is_fs_check,
# MAGIC   is_voucher_fraud_block,
# MAGIC   is_payment_fraud_block,
# MAGIC   is_success,
# MAGIC   is_pvs,
# MAGIC   is_different_checkout,
# MAGIC   is_duplicate_at_pre_checkout, -- spider rollout Edit: May 28, 2025
# MAGIC   is_duplicate_at_post_checkout,
# MAGIC   is_post_checkout_block,
# MAGIC   SUM(1) AS customer_count
# MAGIC FROM
# MAGIC   base AS a
# MAGIC   INNER JOIN dimensions.date_dimension dd ON DATE(a.date_string_backwards) = DATE(dd.date_string_backwards)
# MAGIC   GROUP BY ALL
# MAGIC ;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.payments_p0_metrics_checkout_funnel_backend;
# MAGIC
# MAGIC REFRESH TABLE payments_hf.checkout_funnel_backend;
# MAGIC REFRESH TABLE dimensions.date_dimension;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE payments_hf.payments_p0_metrics_checkout_funnel_backend AS
# MAGIC SELECT
# MAGIC   -- a.*,
# MAGIC   country,
# MAGIC   event_payment_method_listed,
# MAGIC   event_attempted_fraud_check,
# MAGIC   event_payment_verification_attempt AS event_attempted_payment_verification,
# MAGIC   event_payment_verification_success,
# MAGIC   event_successful_conversion,
# MAGIC   CASE 
# MAGIC     WHEN lower(a.payment_method) LIKE '%applepay' THEN 'Apple Pay'
# MAGIC     WHEN lower(a.payment_method) LIKE '%paypal' THEN 'Paypal'
# MAGIC     WHEN lower(a.payment_method) LIKE '%creditcard' THEN 'Credit Card'
# MAGIC     WHEN lower(a.payment_method) IN ('no payment method', 'undefined') THEN 'Unknown'
# MAGIC     WHEN lower(a.payment_method) IS NULL THEN 'Unknown'
# MAGIC     ELSE 'Others' 
# MAGIC   END AS payment_method_reporting,
# MAGIC   dd.iso_year_week AS hellofresh_week,
# MAGIC   CONCAT(dd.year, '-', dd.month) AS hellofresh_year_month,
# MAGIC   CONCAT(dd.year, '-', dd.quarter) AS hellofresh_year_quarter,
# MAGIC   SUM(1) AS customer_count
# MAGIC
# MAGIC FROM
# MAGIC   payments_hf.checkout_funnel_backend AS a
# MAGIC   INNER JOIN dimensions.date_dimension dd ON DATE(a.event_date) = DATE(dd.date_string_backwards)
# MAGIC   GROUP BY ALL
# MAGIC ;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DROP TABLE IF EXISTS payments_hf.payments_p0_metrics_empty_conversions;
# MAGIC
# MAGIC REFRESH TABLE payments_hf.empty_conversion_customer_level;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE payments_hf.payments_p0_metrics_empty_conversions AS WITH date_lkup AS (
# MAGIC   SELECT
# MAGIC     hellofresh_week,
# MAGIC     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS hellofresh_year_month,
# MAGIC     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS hellofresh_year_quarter
# MAGIC   FROM
# MAGIC     dimensions.date_dimension dd
# MAGIC   WHERE
# MAGIC     hellofresh_week >= '2022-W01'
# MAGIC   GROUP BY
# MAGIC     1,
# MAGIC     2,
# MAGIC     3
# MAGIC ),
# MAGIC date_lkup_row AS (
# MAGIC   SELECT
# MAGIC     *,
# MAGIC     ROW_NUMBER() OVER(ORDER BY hellofresh_week ASC) AS row_num
# MAGIC   FROM
# MAGIC     date_lkup
# MAGIC ),
# MAGIC final_date_lkup AS (
# MAGIC   SELECT
# MAGIC     a.hellofresh_week,
# MAGIC     a.hellofresh_year_month,
# MAGIC     a.hellofresh_year_quarter, 
# MAGIC     b.hellofresh_week AS lead_hellofresh_week,
# MAGIC     b.hellofresh_year_month AS lead_hellofresh_year_month,
# MAGIC     b.hellofresh_year_quarter AS lead_hellofresh_year_quarter
# MAGIC   FROM
# MAGIC     date_lkup_row a
# MAGIC     JOIN date_lkup_row b ON a.row_num = b.row_num - 3
# MAGIC )
# MAGIC SELECT
# MAGIC   -- a.*,
# MAGIC   a.country,
# MAGIC   a.net_activations_3wk,
# MAGIC   a.net_reactivations_3wk,
# MAGIC   a.empty_conversion_reason_group,
# MAGIC   a.Category,
# MAGIC   dd.hellofresh_week,
# MAGIC   CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS hellofresh_year_month,
# MAGIC   CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS hellofresh_year_quarter,
# MAGIC   dd_l.lead_hellofresh_week,
# MAGIC   dd_l.lead_hellofresh_year_month,
# MAGIC   dd_l.lead_hellofresh_year_quarter,
# MAGIC   SUM(1) AS customer_count
# MAGIC FROM
# MAGIC   payments_hf.empty_conversion_customer_level AS a
# MAGIC   INNER JOIN dimensions.date_dimension dd ON a.conversion_date = dd.sk_date
# MAGIC   JOIN final_date_lkup AS dd_l ON dd.hellofresh_week = dd_l.hellofresh_week 
# MAGIC   GROUP BY ALL
# MAGIC ;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.payments_p0_metrics_box_candidates;
# MAGIC
# MAGIC REFRESH TABLE payments_hf.f_orders;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE payments_hf.payments_p0_metrics_box_candidates AS
# MAGIC WITH date_lkup AS (
# MAGIC   SELECT
# MAGIC     hellofresh_week,
# MAGIC     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS hellofresh_year_month,
# MAGIC     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS hellofresh_year_quarter
# MAGIC   FROM
# MAGIC     dimensions.date_dimension dd
# MAGIC   WHERE
# MAGIC     hellofresh_week >= '2022-W01'
# MAGIC   GROUP BY
# MAGIC     1,
# MAGIC     2,
# MAGIC     3
# MAGIC ),
# MAGIC date_lkup_row AS (
# MAGIC   SELECT
# MAGIC     *,
# MAGIC     ROW_NUMBER() OVER (ORDER BY hellofresh_week ASC) AS row_num
# MAGIC   FROM
# MAGIC     date_lkup
# MAGIC ),
# MAGIC final_date_lkup AS (
# MAGIC   SELECT
# MAGIC     a.hellofresh_week,
# MAGIC     a.hellofresh_year_month,
# MAGIC     a.hellofresh_year_quarter,
# MAGIC     b.hellofresh_week AS lead_hellofresh_week,
# MAGIC     b.hellofresh_year_month AS lead_hellofresh_year_month,
# MAGIC     b.hellofresh_year_quarter AS lead_hellofresh_year_quarter
# MAGIC   FROM
# MAGIC     date_lkup_row a
# MAGIC       JOIN date_lkup_row b
# MAGIC         ON a.row_num = b.row_num - 12
# MAGIC ),
# MAGIC enrich_data AS (
# MAGIC   SELECT
# MAGIC     a.*,
# MAGIC     CASE
# MAGIC       WHEN first_token = 'apple_pay' THEN 'Apple Pay'
# MAGIC       WHEN first_token = 'paypal' THEN 'Paypal'
# MAGIC       WHEN first_token = 'credit_card' THEN 'Credit Card' -- temporary fix
# MAGIC       WHEN
# MAGIC         first_token ilike '%visa%'
# MAGIC         OR first_token ilike 'mc%'
# MAGIC       THEN
# MAGIC         'Credit Card'
# MAGIC       WHEN first_token ilike '%apple%' THEN 'Apple Pay'
# MAGIC       WHEN first_token ilike '%paypal%' THEN 'Paypal' -- end temporary fix
# MAGIC       -- WHEN first_token IS NULL THEN 'Unknown'
# MAGIC       ELSE
# MAGIC         'Others'
# MAGIC     END AS payment_method_reporting,
# MAGIC     COALESCE(first_provider, "Unknown") AS first_provider_reporting,
# MAGIC     CASE
# MAGIC       WHEN NOT ((RIGHT(COALESCE(last_10_order_statuses, ''), 2) = 'ff')) THEN 'Good'
# MAGIC       ELSE 'Bad'
# MAGIC     END AS customer_quality,
# MAGIC     CASE
# MAGIC       WHEN type_order = 'initial' THEN 'Initial'
# MAGIC       ELSE 'Recurring'
# MAGIC     END AS order_type_reporting,
# MAGIC     CONCAT(
# MAGIC       CASE
# MAGIC         WHEN first_token = 'apple_pay' THEN 'Apple Pay'
# MAGIC         WHEN first_token = 'paypal' THEN 'Paypal'
# MAGIC         WHEN first_token = 'credit_card' THEN 'Credit Card' -- temporary fix
# MAGIC         WHEN
# MAGIC           first_token ilike '%visa%'
# MAGIC           OR first_token ilike 'mc%'
# MAGIC         THEN
# MAGIC           'Credit Card'
# MAGIC         WHEN first_token ilike '%apple%' THEN 'Apple Pay'
# MAGIC         WHEN first_token ilike '%paypal%' THEN 'Paypal' -- end temporary fix
# MAGIC         -- WHEN first_token IS NULL THEN 'Unknown'
# MAGIC         ELSE
# MAGIC           'Others'
# MAGIC       END,
# MAGIC       ' - ',
# MAGIC       CASE
# MAGIC         WHEN type_order = 'initial' THEN 'Initial'
# MAGIC         ELSE 'Recurring'
# MAGIC       END
# MAGIC     ) AS payment_method_order_type_reporting,
# MAGIC     CASE
# MAGIC       WHEN
# MAGIC         (
# MAGIC           (
# MAGIC             latest_status IN ('money_received', 'shipped', 'refunded', 'chargeback')
# MAGIC             AND latest_workflow IN (
# MAGIC               'batch', 'batch-rerun', 'manual', 'performPayment', 'perform', 'CAMS', 'initial', 'evangelist'
# MAGIC             )
# MAGIC             AND bob_status = 'money_received'
# MAGIC           )
# MAGIC         )
# MAGIC       THEN
# MAGIC         1
# MAGIC       ELSE 0
# MAGIC     END AS 1_FirstRunAR,
# MAGIC     CASE
# MAGIC       WHEN
# MAGIC         (
# MAGIC           (
# MAGIC             latest_status NOT IN ('canceled', 'clarify_payment_error')
# MAGIC             AND bob_status <> 'money_received'
# MAGIC             AND latest_status_dt < logistics_cutoff
# MAGIC             AND (
# MAGIC               (lower(latest_workflow) LIKE '%cipr%')
# MAGIC               OR (lower(latest_workflow) LIKE '%retry%')
# MAGIC             )
# MAGIC           )
# MAGIC           OR (
# MAGIC             latest_status NOT IN ('canceled', 'clarify_payment_error')
# MAGIC             AND bob_status <> 'money_received'
# MAGIC             AND latest_status_dt < logistics_cutoff
# MAGIC             AND latest_workflow IN (
# MAGIC               'batch', 'batch-rerun', 'manual', 'performPayment', 'perform', 'CAMS', 'initial', 'evangelist'
# MAGIC             )
# MAGIC           )
# MAGIC           OR (
# MAGIC             latest_status IN ('money_received', 'shipped', 'refunded', 'chargeback')
# MAGIC             AND latest_workflow IN (
# MAGIC               'batch', 'batch-rerun', 'manual', 'performPayment', 'perform', 'CAMS', 'initial', 'evangelist'
# MAGIC             )
# MAGIC             AND bob_status = 'money_received'
# MAGIC           )
# MAGIC         )
# MAGIC       THEN
# MAGIC         1
# MAGIC       ELSE 0
# MAGIC     END AS 2_PreDunningAR,
# MAGIC     CASE
# MAGIC       WHEN
# MAGIC         (
# MAGIC           (
# MAGIC             latest_status NOT IN ('canceled', 'clarify_payment_error')
# MAGIC             AND bob_status <> 'money_received'
# MAGIC           )
# MAGIC           OR (
# MAGIC             latest_status IN ('money_received', 'shipped', 'refunded', 'chargeback')
# MAGIC             AND latest_workflow IN (
# MAGIC               'batch', 'batch-rerun', 'manual', 'performPayment', 'perform', 'CAMS', 'initial', 'evangelist'
# MAGIC             )
# MAGIC             AND bob_status = 'money_received'
# MAGIC           )
# MAGIC         )
# MAGIC       THEN
# MAGIC         1
# MAGIC       ELSE 0
# MAGIC     END AS 3_PostDunningAR,
# MAGIC     -- Payment Approval Rate flag (added for P0 metrics)
# MAGIC     -- is_payment_approved: Orders not canceled (numerator for Payment Approval Rate)
# MAGIC     CASE
# MAGIC       WHEN latest_status != 'canceled' THEN 1
# MAGIC       ELSE 0
# MAGIC     END AS is_payment_approved,
# MAGIC     (
# MAGIC       SELECT
# MAGIC         TRANSFORM(FILTER(statuses, x -> x.status = 'clarify_payment_error'), x -> x.note)[0]
# MAGIC       FROM
# MAGIC         (
# MAGIC           SELECT
# MAGIC             ARRAY_SORT(
# MAGIC               FILTER(statuses, x -> x.status = 'clarify_payment_error'),
# MAGIC               (x, y) -> CASE
# MAGIC                 WHEN x.created_at.utc > y.created_at.utc THEN -1
# MAGIC                 WHEN x.created_at.utc < y.created_at.utc THEN 1
# MAGIC                 ELSE 0
# MAGIC               END
# MAGIC             ) AS sorted_errors
# MAGIC         )
# MAGIC     ) AS decline_note,
# MAGIC     dd.hellofresh_week,
# MAGIC     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS hellofresh_year_month,
# MAGIC     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS hellofresh_year_quarter,
# MAGIC     dd1.lead_hellofresh_week,
# MAGIC     dd1.lead_hellofresh_year_month,
# MAGIC     dd1.lead_hellofresh_year_quarter
# MAGIC   FROM
# MAGIC     payments_hf.f_orders AS a
# MAGIC       INNER JOIN dimensions.date_dimension dd
# MAGIC         ON DATE(a.delivery_date) = DATE(dd.date_string_backwards)
# MAGIC       JOIN final_date_lkup AS dd1
# MAGIC         ON dd.hellofresh_week = dd1.hellofresh_week
# MAGIC   WHERE
# MAGIC     DATE(a.delivery_date) >= '2022-12-31' -- FROM 2023-W01 HF-week
# MAGIC ),
# MAGIC enrich_data_v2 AS (
# MAGIC   SELECT
# MAGIC     dp.*,
# MAGIC     case
# MAGIC       when
# MAGIC         dp.decline_note like 'PROVIDER_ERROR: failure executing charge with provider%'
# MAGIC       then
# MAGIC         'PROVIDER_ERROR: failure executing charge with provider'
# MAGIC       when
# MAGIC         dp.decline_note ilike SOME ('%insufficient funds%', '%not enough balance%')
# MAGIC       then
# MAGIC         'Insufficient Funds'
# MAGIC       when dp.decline_note like 'INTERNAL_ERROR(Post)%' then 'Internal error (Post Adyenpayments)'
# MAGIC       when
# MAGIC         dp.decline_note like 'PROVIDER_ERROR(Payment method token is invalid%'
# MAGIC       then
# MAGIC         'PROVIDER_ERROR(Payment method token is invalid)'
# MAGIC       -- when
# MAGIC       --   dp.decline_note like '%Could not find an acquirer account for the provided txvariant%'
# MAGIC       -- then
# MAGIC       --   'Could not find an acquirer account for the provided txvariant'
# MAGIC       -- when
# MAGIC       --   dp.decline_note like '%Could not find an acquirer account for the provided currency%'
# MAGIC       -- then
# MAGIC       --   'Could not find an acquirer account for the provided currency'
# MAGIC       when dp.decline_note like '%NO CARDHOLDER AUTHORIZATION%' then 'No cardholder authorization'
# MAGIC       when
# MAGIC         dp.decline_note like 'PROVIDER_ERROR(Post%'
# MAGIC       then
# MAGIC         'PROVIDER_ERROR(Post API Braintreegateway)'
# MAGIC       when
# MAGIC         dp.decline_note like '%CARDHOLDER DID NOT AUTHORIZE-CARD NOT PRESENT%'
# MAGIC       then
# MAGIC         'CARDHOLDER DID NOT AUTHORIZE-CARD NOT PRESENT'
# MAGIC       when
# MAGIC         dp.decline_note like
# MAGIC           'PROVIDER_ERROR: failure executing charge with provider: Post "https://api.braintreegateway%'
# MAGIC       then
# MAGIC         'PROVIDER_ERROR: failure executing charge with provider: Post api.braintreegateway.com'
# MAGIC       when
# MAGIC         dp.decline_note like 'PROVIDER_ERROR: failure executing charge with provider%'
# MAGIC       then
# MAGIC         'PROVIDER_ERROR: failure executing charge with provider'
# MAGIC       when dp.decline_note like '%Post "Post%context canceled%' then 'Post: Context canceled'
# MAGIC       when
# MAGIC         dp.decline_note like '%Post%request canceled%'
# MAGIC       then
# MAGIC         'Post: Request canceled. Timeout exceeded'
# MAGIC       when
# MAGIC         dp.decline_note like 'PROVIDER_ERROR(Internal Error in authorise%'
# MAGIC       then
# MAGIC         'PROVIDER_ERROR(Internal Error in authorise)'
# MAGIC       when dp.decline_note like 'CaseId%' then 'Case ID'
# MAGIC       when dp.decline_note like 'v2%failed%' then 'V2 failed'
# MAGIC       when dp.decline_note like '%STATE_FAILED' then 'State_failed'
# MAGIC       when dp.decline_note like '%-%-%-%-%' then 'Unknown' --              when try_cast(split(cdp.note, ',')[0] AS integer) IS NOT NULL then 'Unknown'
# MAGIC       WHEN dp.decline_note like "Refused%" then "Refused - eg: Declined, Closed Card, Do Not Honor, etc."
# MAGIC       -- WHEN dp.decline_note like "Refused(Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank Or It Can't Be Used For This Payment)%" then "Refused(Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank Or It Can't Be Used For This Payment)"
# MAGIC       -- WHEN dp.decline_note like "Refused(Declined)%" then "Refused(Declined)"
# MAGIC       -- WHEN dp.decline_note like "Refused(Closed Card)%" then "Refused(Closed Card)"
# MAGIC       -- WHEN dp.decline_note like "Refused(Do Not Honor)%" then "Refused(Do Not Honor)"
# MAGIC       -- WHEN dp.decline_note like "Refused(PayPal Buyer Revoked Pre-Approved Payment Authorization)%" then "Refused(PayPal Buyer Revoked Pre-Approved Payment Authorization)"
# MAGIC       -- WHEN dp.decline_note like "Refused(No Account)%" then "Refused(No Account)"
# MAGIC       -- WHEN dp.decline_note like "Refused(Cannot Authorize at this time%" then "Refused(Cannot Authorize)"
# MAGIC       -- WHEN dp.decline_note like "Refused%" then "Refused - other reasons"
# MAGIC       else "Other reasons"
# MAGIC     end as decline_reason
# MAGIC   FROM
# MAGIC     enrich_data dp
# MAGIC )
# MAGIC SELECT
# MAGIC   hellofresh_week,
# MAGIC   hellofresh_year_month,
# MAGIC   hellofresh_year_quarter,
# MAGIC   lead_hellofresh_week,
# MAGIC   lead_hellofresh_year_month,
# MAGIC   lead_hellofresh_year_quarter,
# MAGIC   country,
# MAGIC   dunning_execution,
# MAGIC   product_type,
# MAGIC   segment,
# MAGIC   customer_loyalty,
# MAGIC   box_shipped,
# MAGIC   recovered_in_days,
# MAGIC   payment_method_reporting,
# MAGIC   first_provider_reporting,
# MAGIC   customer_quality,
# MAGIC   type_order,
# MAGIC   order_type_reporting,
# MAGIC   payment_method_order_type_reporting,
# MAGIC   case
# MAGIC     WHEN 1_FirstRunAR = 1 THEN '1. SUCCESSFULL'
# MAGIC     else decline_reason
# MAGIC   end as decline_reason_first_run_reporting,
# MAGIC   CASE
# MAGIC     WHEN 2_PreDunningAR = 1 THEN '1. SUCCESSFULL'
# MAGIC     else decline_reason
# MAGIC   end as decline_reason_pre_dunning_reporting,
# MAGIC   CASE
# MAGIC     WHEN 3_PostDunningAR = 1 THEN '1. SUCCESSFULL'
# MAGIC     else decline_reason
# MAGIC   end as decline_reason_post_dunning_reporting,
# MAGIC   SUM(1_FirstRunAR) AS 1_FirstRunAR,
# MAGIC   SUM(2_PreDunningAR) AS 2_PreDunningAR,
# MAGIC   SUM(3_PostDunningAR) AS 3_PostDunningAR,
# MAGIC   SUM(is_payment_approved) AS is_payment_approved,
# MAGIC   SUM(grand_total_eur) AS grand_total_eur,
# MAGIC   SUM(1) AS order_count
# MAGIC
# MAGIC FROM
# MAGIC   enrich_data_v2
# MAGIC GROUP BY ALL
# MAGIC ;

# COMMAND ----------

# %sql

# DROP TABLE IF EXISTS payments_hf.payments_p0_metrics_top_up_financials;

# REFRESH TABLE payments_hf.currency_dimension_daily;
# REFRESH TABLE payments_hf.top_up_service_top_ups;
# REFRESH TABLE payments_hf.top_up_service_top_up_options;
# REFRESH TABLE payments_hf.balance_service_transactions;
# REFRESH TABLE dl_bob_live_non_pii.customer;
# REFRESH TABLE dimensions.date_dimension;
# REFRESH TABLE payments_hf.customer_cohort_roi;
# REFRESH TABLE payments_hf.f_customer_loyalty;
# REFRESH TABLE payments_hf.customer_actuals;

# CREATE TABLE payments_hf.payments_p0_metrics_top_up_financials AS with top_ups as (
#   select
#     tu.id as topup_id,
#     -- tu.customer_id as fk_customer_uuid,
#     concat(
#       string(top.system_country),
#       ': ',
#       string(top.offer_price),
#       '+',
#       string(top.bonus),
#       ' ',
#       string(top.currency_code)
#     ) AS option_name,
#     CASE
#       WHEN top.bonus < 15
#       or (
#         top.system_country = 'SE'
#         and top.bonus = 50
#       ) THEN 'Starting Pack'
#       WHEN top.system_country in ('US', 'AU', 'CA')
#       and top.bonus <= 20 THEN 'Top Seller'
#       WHEN top.bonus >= 15 THEN 'Best Value'
#       ELSE NULL
#     END AS package_name
#   from
#     payments_hf.top_up_service_top_ups tu
#     left join payments_hf.top_up_service_top_up_options top on tu.option_id = top.id
#   WHERE
#     tu.created_at >= timestamp('2024-07-01')
#     AND tu.status != 'FAILED'
# ),
# topup_transactions AS (
#   select
#     bst.id as bs_transaction_id,
#     bst.type,
#     CASE
#       WHEN contains(bst.reference_id, 'order_nr') THEN null
#       ELSE bst.reference_id
#     END AS topup_id,
#     bst.customer_uuid as fk_customer_uuid,
#     b.id_customer as customer_id,
#     b.business_unit as country,
#     bst.cash / 100 as cash_local_cur,
#     bst.bonus / 100 as bonus_local_cur,
#     bst.currency_code,
#     cast(
#       bst.cash / 100 * cdd.to_euro_conversion as decimal(32, 2)
#     ) as cash_eur,
#     cast(
#       bst.bonus / 100 * cdd.to_euro_conversion as decimal(32, 2)
#     ) as bonus_eur,
#     date(bst.created_at) as created_date,
#     dd.hellofresh_week,
#     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS hellofresh_year_month,
#     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS hellofresh_year_quarter
#   from
#     payments_hf.balance_service_transactions bst
#     JOIN dl_bob_live_non_pii.customer b ON bst.customer_uuid = b.uuid
#     inner join dimensions.date_dimension dd on cast(date(bst.created_at) as string) = dd.date_string_backwards
#     left join (
#       select
#         currency_name,
#         to_euro_conversion
#       from
#         payments_hf.currency_dimension_daily
#       where
#         cast(conversion_date as date) = current_date()
#     ) cdd on bst.currency_code = cdd.currency_name
#   where
#     bst.created_at >= timestamp('2024-07-01')
#     AND bst.type IN ('CREDIT', 'DEBIT')
# ),
# topup_filtered AS (
#   SELECT
#     tu.option_name,
#     tu.package_name,
#     tt.*
#   FROM
#     topup_transactions tt
#     LEFT JOIN top_ups tu ON tt.topup_id = tu.topup_id
#   where
#     tt.fk_customer_uuid not in -- overrides id
#     (
#       'a7adc394-8514-4de9-b786-1fb6297955dc',
#       '5c0148b9-a831-4c7d-84c3-b3d7e0a8e107',
#       '004811a2-9174-4d43-9dc7-12f61feffa3d',
#       'a1005090-453f-4ae4-b9eb-1e6721506265',
#       'f4fa98ab-a424-49e3-bcd4-64d1a3fffd8c',
#       '9b166114-b190-4b20-9d5d-e08eee6f2eb7',
#       'd4bf1360-d5dc-41e0-a7d8-9eb9471c187b',
#       '4e94d769-48f7-4b8f-bab2-91cc92b26f5f',
#       'aec279bf-9a25-49a0-8206-0b5dcfdc5c84',
#       '1d59094c-045c-4cc1-af20-47d4f2f6a614',
#       '2cf6ac6a-7d35-4da8-951e-5b045f011dfa',
#       'f6ac1bcf-5498-4d03-9234-abae2a0cf03a',
#       'd2bb02ea-6d9c-4d56-8c97-8c794878d52f',
#       '53f88786-1d10-4ee4-a3cc-b5800996ee3e',
#       '0dee076a-806a-47af-a831-65bd6df7a837',
#       '482379a0-c990-4707-81f5-da2cf3ed91c6',
#       '7cef0a14-5070-40f1-a165-ce3b61df01ce',
#       'b2a6ce35-e6ba-4a21-a70f-d51b7cb72613',
#       'ce5250a2-3682-4ad7-912a-5b8a73c927c7',
#       'bc791d9d-abac-4bbc-b386-6bef93a69a73',
#       'f87ea4ff-feb3-4610-9bb4-5c492e259b6f',
#       'ecd094ee-cbd4-4a0b-b7fc-1bb63d07a4bd',
#       '984d5e00-cdf7-405f-8326-bbf5deef668b',
#       'a8f0da06-0067-4ca8-a042-ba92e2cb19a1',
#       'eebd0b88-3ede-47f1-957d-37b719e91f16',
#       '56d709ea-df3f-4756-98ab-5b5f712fb564',
#       '5b1ab1de-3f68-4a3c-b54d-efcffe8bea14',
#       '066332d7-7c36-4c0c-8cff-68c01fb2edb4',
#       '542234ce-d371-48db-89ca-9ae374749270',
#       '30252846-af30-4443-b0ec-2c134fcbbd2d',
#       'fb8d7a45-b13e-4bc8-9820-b9139ee50047',
#       '4b32359b-5f8c-40b3-8d82-70a7effa21d1',
#       '83932022-d0ef-46b4-b9a5-77b9b0af9aa8',
#       '62195b37-4d49-4d6f-b6d4-5434208d37b4',
#       '5f51478b-768e-4099-80b7-10a80ba9adfd',
#       '6e5e6f13-59a4-4267-bbc4-5bf4d7b99910',
#       '330f7f7f-2350-44a4-af7b-bdfd6bcd453c',
#       '845de4e6-0c42-40ac-a403-67c5ed6726b6',
#       'fd146c50-e8f7-4e47-9fa3-0e3bcd96976e',
#       'fd851b6d-e10b-4066-8cc2-8e8ff610bab0',
#       '96a43699-c6af-4e28-87f6-1a0dbaa6abaa',
#       'cbdfc150-bd25-47e0-aafe-e9fb85e6037a',
#       'd5be09a4-68f7-406a-8abc-bfb1da75f927',
#       'ab9c69a8-a5c1-466c-a1f1-c29decf06850',
#       'ecebacc8-d371-4541-b8b2-890dfd9e8a61',
#       '1caae824-92c0-47e8-998d-c16c4a6749d0',
#       'b9b5b489-21ef-4bde-8e9d-b0f688ee017b',
#       'a9cc11bf-3c4d-421a-a988-2b4dda759595',
#       '15884b1f-af5d-40c7-9223-07746264f168',
#       '74f40475-eeeb-4924-bdb1-ff5e520917b7',
#       '58b23a26-0cf7-487c-a423-b51e32583b5d',
#       'b47f68b9-0622-45ca-b2ca-b646e77f8b27',
#       '9bd01d94-ee06-4415-9054-56b0a3308e0c',
#       '8e15b801-6959-4ab9-ae00-63faf51141c6',
#       '27ec70c8-ccd4-4773-a637-964ed9ca0860',
#       'bab84fdf-da0e-473a-88f0-da9235d238e7',
#       '7da3f37e-692c-4bb8-bc1c-41a86f4f6481',
#       '3eba7e59-1843-441f-8cb2-8c2bff0dad34',
#       '506d355b-24bf-4de0-a627-b5adeceb62e1',
#       '9573d98e-9f79-4548-9292-11f9b42bba23',
#       '0ADDCAE3-530D-4D09-A94C-B930980670D7',
#       '96bb05f8-7312-4058-bb9c-f4e948ca7a16',
#       '8233d47b-031a-4100-9f39-f74ce8dfca6c',
#       'ab93795e-e5f9-4b6c-95e5-00353c85b6af',
#       '8c42ea21-ab98-49d7-8e5b-c284ff1d180c',
#       '219cddcd-b71d-4b1f-a4b5-bf739521d21c',
#       '0dd66a1c-2d6f-4b27-a996-561743cc9a25',
#       '28448ff2-ff18-44ab-b000-f2f5f2ec0378',
#       '17949de1-698b-4a15-a3c3-f8a02fec9fdd',
#       '4937ef3e-92e9-443e-9f49-042d1bbc09d8',
#       '7c40b9a4-6be2-489f-87c3-7b16383df0b2',
#       'd152cf57-a184-47f4-a2ae-4a966aff7946',
#       '0b24c2fc-5cf8-4bfc-93ea-370b86ca3a48',
#       '7cca0069-e27c-42ea-b241-fa896bf478df',
#       '64e097a5-7103-4b5a-b91b-9bedf6f1aa79',
#       '47b776cd-784a-453e-9507-59892c1f7ec5',
#       '00ae56fb-4f75-4c82-a02a-6ca19ce8ed13',
#       'd7e91ed2-88ac-4ef2-9a40-578df6a04e94',
#       '2d3ce8dd-291d-44a4-9b3f-13534b5953ee',
#       '98aef740-1558-40a2-a1c4-47f40881842a',
#       '1afabff4-2910-42c2-b309-ca78a0e20e05',
#       '1a39bfdc-b034-4631-bf8b-e4dcc575e871',
#       '1f3144e5-06f9-4abe-b701-34a23caf9d7e',
#       'dcbd2c89-a7da-436d-8a11-d93fd7514d73',
#       '01051782-201e-4f3f-91ca-a2c6a7ffbcd3',
#       'b3c11916-a3bc-403e-8271-0d0ca36d1b89',
#       '895b8d1b-da8f-4d3b-9a67-bed8ce94db66',
#       '138ae4ef-636d-4b06-a8c6-effe7306370d',
#       '9d641591-ae44-4b67-91cb-e4751912e7ea',
#       'a0767c6d-a5d0-4248-8831-ccaff3cfc6a9',
#       'c3418a6b-67bb-4b62-9f7e-4e0853ee701f',
#       '158c8545-cc7a-459f-8da0-f4c8a3f32e9d',
#       'e04216bd-c88c-4043-be37-921a3219ae42',
#       'c7f53930-9269-4b91-a65c-6516ab5e0443',
#       '4d2cecf5-b5b4-40e6-bf81-d989a4cec607',
#       '1f96f99f-f24c-4364-aa78-3da750e001ce',
#       'e888d5ef-ff23-4df4-aa45-8de9dc547348',
#       '19a447c5-e949-4501-9f9e-e960868edab3'
#     )
# ),
# topup_channel as (
#   SELECT
#     t.*,
#     case
#       when roi.reactivation_date is not null then 'Reactivation'
#       when rc.channel is not null then 'Referral'
#       else 'Paid'
#     end as category,
#     case
#       when roi.reactivation_date is not null then case
#         when roi.reactivation_channel in (
#           'Amazon Employee Benefits',
#           'App Organic',
#           'App Paid Acquisition',
#           'B2B',
#           'B2B Conversion',
#           'B2B Revenue',
#           'Barter',
#           'Box Inserts',
#           'Brand Influencer',
#           'Customer Care Sorry Vouchers',
#           'Customer Care Sorry Vouchers New',
#           'Null',
#           'Sustainability',
#           'EveryShare Offline',
#           'Brand Partnership',
#           'Call Center',
#           'Channel Innovation',
#           'Checkout Alternate',
#           'CRM Paid App Acquisition',
#           'Cross Brand',
#           'Customer Care Sorry Vouchers',
#           'Customer Care Sorry Vouchers HelloShare New',
#           'Direct Mail CRM',
#           'Email Partnerships',
#           'Employee Discounts',
#           'EveryShare Online',
#           'Freebies',
#           'Gift boxes',
#           'HelloShare',
#           'HelloShare Offline',
#           'Influencer Boxes',
#           'Influencer Brand',
#           'Leads Generation',
#           'Organic',
#           'Organic Reactivation',
#           'Out of Home',
#           'PR',
#           'PR Boxen Influencer 2022',
#           'Print',
#           'Product Marketing',
#           'QA / Warehouse / Office boxes',
#           'QA Auto Test',
#           'Radio',
#           'Research',
#           'Revenue Partnerships',
#           'Security',
#           'SEA Reactivation',
#           'SEO Non-Brand',
#           'Social Media',
#           'TV Digital',
#           'TV Linear',
#           'Video Brand',
#           'Video Performance',
#           'WhatsApp',
#           'X-Channel'
#         ) then 'Other'
#         else roi.reactivation_channel
#       end
#       else case
#         when roi.activation_channel in (
#           'Amazon Employee Benefits',
#           'App Organic',
#           'App Paid Acquisition',
#           'B2B',
#           'B2B Conversion',
#           'B2B Revenue',
#           'Barter',
#           'Box Inserts',
#           'Brand Influencer',
#           'Customer Care Sorry Vouchers',
#           'Customer Care Sorry Vouchers New',
#           'Null',
#           'Sustainability',
#           'EveryShare Offline',
#           'Brand Partnership',
#           'Call Center',
#           'Channel Innovation',
#           'Checkout Alternate',
#           'CRM Paid App Acquisition',
#           'Cross Brand',
#           'Customer Care Sorry Vouchers',
#           'Customer Care Sorry Vouchers HelloShare New',
#           'Direct Mail CRM',
#           'Email Partnerships',
#           'Employee Discounts',
#           'EveryShare Online',
#           'Freebies',
#           'Gift boxes',
#           'HelloShare',
#           'HelloShare Offline',
#           'Influencer Boxes',
#           'Influencer Brand',
#           'Leads Generation',
#           'Organic',
#           'Organic Reactivation',
#           'Out of Home',
#           'PR',
#           'PR Boxen Influencer 2022',
#           'Print',
#           'Product Marketing',
#           'QA / Warehouse / Office boxes',
#           'QA Auto Test',
#           'Radio',
#           'Research',
#           'Revenue Partnerships',
#           'Security',
#           'SEA Reactivation',
#           'SEO Non-Brand',
#           'Social Media',
#           'TV Digital',
#           'TV Linear',
#           'Video Brand',
#           'Video Performance',
#           'WhatsApp',
#           'X-Channel'
#         ) then 'Other'
#         else roi.activation_channel
#       end
#     end as channel,
#     case
#       when coalesce(cl.loyalty, 0) <= 5 then coalesce(cl.loyalty, 0)
#       when cl.loyalty <= 10 then '6-10'
#       when cl.loyalty <= 19 then '11-19'
#       when cl.loyalty <= 29 then '20-29'
#       when cl.loyalty <= 39 then '30-39'
#       when cl.loyalty <= 49 then '40-49'
#       else '50+'
#     end as loyalty_level
#   FROM
#     topup_filtered t
#     LEFT JOIN (
#       SELECT
#         country,
#         customer_id,
#         hf_delivery_week,
#         activation_channel,
#         reactivation_date,
#         reactivation_channel
#       FROM
#         payments_hf.customer_cohort_roi
#       WHERE
#         hf_delivery_week >= '2024-W27'
#         AND country IN ('US', 'AU', 'DE', 'FR', 'BE', 'GB', 'IT', 'NL')
#     ) as roi ON roi.country = t.country
#     AND roi.customer_id = t.customer_id
#     AND roi.hf_delivery_week = t.hellofresh_week
#     LEFT JOIN payments_hf.referral_channels rc ON lower(rc.channel) = lower(roi.activation_channel)
#     LEFT JOIN (
#       SELECT
#         country,
#         customer_id,
#         hf_delivery_week,
#         loyalty
#       FROM
#         payments_hf.f_customer_loyalty
#       WHERE
#         hf_delivery_week >= '2024-W27'
#         AND country IN ('US', 'AU', 'DE', 'FR', 'BE', 'GB', 'IT', 'NL')
#     ) as cl on t.country = cl.country
#     and t.customer_id = cl.customer_id
#     and t.hellofresh_week = cl.hf_delivery_week
# ),
# topup_cash AS (
#   SELECT
#     t.option_name,
#     t.package_name,
#     t.category,
#     t.channel,
#     t.loyalty_level,
#     t.created_date,
#     t.hellofresh_week,
#     t.hellofresh_year_month,
#     t.hellofresh_year_quarter,
#     t.type,
#     'cash' AS credit_type,
#     t.country,
#     t.currency_code,
#     count_if(t.cash_local_cur > 0) as topup_count,
#     count(distinct t.customer_id) FILTER(
#       WHERE
#         t.cash_local_cur > 0
#     ) AS topup_users,
#     sum(t.cash_local_cur) as credit_sum_local_cur,
#     sum(t.cash_eur) as credit_sum_eur,
#     NULL AS gross_revenue_eur,
#     NULL AS profit_eur
#   FROM
#     topup_channel t
#   GROUP BY
#     ALL
# ),
# topup_bonus AS (
#   SELECT
#     t.option_name,
#     t.package_name,
#     t.category,
#     t.channel,
#     t.loyalty_level,
#     t.created_date,
#     t.hellofresh_week,
#     t.hellofresh_year_month,
#     t.hellofresh_year_quarter,
#     t.type,
#     'bonus' AS credit_type,
#     t.country,
#     t.currency_code,
#     count_if(t.bonus_local_cur > 0) as topup_count,
#     count(distinct t.customer_id) FILTER(
#       WHERE
#         t.bonus_local_cur > 0
#     ) AS topup_users,
#     sum(t.bonus_local_cur) as credit_sum_local_cur,
#     sum(t.bonus_eur) as credit_sum_eur,
#     NULL AS gross_revenue_eur,
#     NULL AS profit_eur
#   FROM
#     topup_channel t
#   GROUP BY
#     ALL
# ),
# topup_revenue AS (
#   SELECT
#     NULL AS option_name,
#     NULL AS package_name,
#     t.category,
#     t.channel,
#     t.loyalty_level,
#     NULL AS created_date,
#     ca.hf_delivery_week,
#     ca.hellofresh_year_month,
#     ca.hellofresh_year_quarter,
#     'CCR' AS type,
#     NULL AS credit_type,
#     t.country,
#     'EUR' AS currency_code,
#     NULL as topup_count,
#     NULL AS topup_users,
#     NULL as credit_sum_local_cur,
#     NULL as credit_sum_eur,
#     SUM(ca.gross_revenue_week_eur) AS gross_revenue_eur,
#     SUM(ca.profit_week_eur) AS profit_eur
#   FROM
#     (
#     SELECT
#       concat(fk_customer_uuid, '_', hellofresh_week) as customer_week,
#       country,
#       category,
#       channel,
#       min(loyalty_level) as loyalty_level
#     FROM topup_channel
#     WHERE type = 'DEBIT'
#     GROUP BY ALL 
#     ) t
#     JOIN (
#       SELECT
#         concat(customer_uuid, '_', hf_delivery_week) as customer_week,
#         hf_delivery_week,
#         dd.hellofresh_year_month,
#         dd.hellofresh_year_quarter,
#         net_ccv_mpc2_at_prediction_eur as profit_week_eur,
#         gross_revenue_at_prediction_eur as gross_revenue_week_eur
#       FROM
#         payments_hf.customer_actuals AS a
#         JOIN (
#           SELECT
#             hellofresh_week,
#             CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS hellofresh_year_month,
#             CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS hellofresh_year_quarter
#           FROM
#             dimensions.date_dimension dd
#           WHERE
#             hellofresh_week >= '2023-W01'
#           GROUP BY
#             1,
#             2,
#             3
#         ) AS dd ON a.hf_delivery_week = dd.hellofresh_week
#       where
#         hf_delivery_week >= '2024-W27'
#         AND country IN ('US','AU','DE','FR','BE','GB','IT','NL','CA','DK','ES','NO','SE')
#     ) ca ON ca.customer_week = t.customer_week
#   GROUP BY
#     ALL
# )
# SELECT
#   tc.*
# FROM
#   topup_cash tc
# UNION
# SELECT
#   tb.*
# FROM
#   topup_bonus tb
# UNION
# SELECT
#   tr.*
# FROM
#   topup_revenue tr;

# COMMAND ----------

# %sql

# DROP TABLE IF EXISTS payments_hf.payments_p0_metrics_top_up_orders;

# REFRESH TABLE materialized_views.pa_statsig_exposures_deduplicated;
# REFRESH TABLE dl_bob_live_non_pii.customer;
# REFRESH TABLE payments_hf.f_orders;
# REFRESH TABLE dimensions.date_dimension;
# REFRESH TABLE payments_hf.customer_cohort_roi;
# REFRESH TABLE payments_hf.f_customer_loyalty;
# REFRESH TABLE payments_hf.customer_actuals;
# REFRESH TABLE payments_hf.balance_service_transactions;

# CREATE TABLE payments_hf.payments_p0_metrics_top_up_orders AS 
# WITH eligible_users AS (
#   select
#       b.business_unit as country,
#       b.id_customer as customer_id,
#       e.user_id as customer_uuid,
#       min(e.timestamp) as event_datetime
#   from materialized_views.pa_statsig_exposures_deduplicated e
#   JOIN dl_bob_live_non_pii.customer b
#   ON e.user_id = b.uuid
#   where e.timestamp >= timestamp('2024-07-01')
#   AND ((e.experiment_id = 'top_up'
#     AND e.group_id = '12LxbQfeOf9QO0rTozDU88')
#     OR (e.experiment_id = 'top_up_multivariant'
#     AND e.group_id = 'cNKcsMfjJlm8xUfrMVrvq'))
#   and e.user_id IS NOT NULL
#   and e.user_id not in -- overrides id
#   ('a7adc394-8514-4de9-b786-1fb6297955dc','5c0148b9-a831-4c7d-84c3-b3d7e0a8e107','004811a2-9174-4d43-9dc7-12f61feffa3d','a1005090-453f-4ae4-b9eb-1e6721506265','f4fa98ab-a424-49e3-bcd4-64d1a3fffd8c','9b166114-b190-4b20-9d5d-e08eee6f2eb7','d4bf1360-d5dc-41e0-a7d8-9eb9471c187b','4e94d769-48f7-4b8f-bab2-91cc92b26f5f','aec279bf-9a25-49a0-8206-0b5dcfdc5c84','1d59094c-045c-4cc1-af20-47d4f2f6a614','2cf6ac6a-7d35-4da8-951e-5b045f011dfa','f6ac1bcf-5498-4d03-9234-abae2a0cf03a','d2bb02ea-6d9c-4d56-8c97-8c794878d52f','53f88786-1d10-4ee4-a3cc-b5800996ee3e','0dee076a-806a-47af-a831-65bd6df7a837','482379a0-c990-4707-81f5-da2cf3ed91c6','7cef0a14-5070-40f1-a165-ce3b61df01ce','b2a6ce35-e6ba-4a21-a70f-d51b7cb72613','ce5250a2-3682-4ad7-912a-5b8a73c927c7','bc791d9d-abac-4bbc-b386-6bef93a69a73','f87ea4ff-feb3-4610-9bb4-5c492e259b6f','ecd094ee-cbd4-4a0b-b7fc-1bb63d07a4bd','984d5e00-cdf7-405f-8326-bbf5deef668b','a8f0da06-0067-4ca8-a042-ba92e2cb19a1','eebd0b88-3ede-47f1-957d-37b719e91f16','56d709ea-df3f-4756-98ab-5b5f712fb564','5b1ab1de-3f68-4a3c-b54d-efcffe8bea14','066332d7-7c36-4c0c-8cff-68c01fb2edb4','542234ce-d371-48db-89ca-9ae374749270','30252846-af30-4443-b0ec-2c134fcbbd2d','fb8d7a45-b13e-4bc8-9820-b9139ee50047','4b32359b-5f8c-40b3-8d82-70a7effa21d1','83932022-d0ef-46b4-b9a5-77b9b0af9aa8','62195b37-4d49-4d6f-b6d4-5434208d37b4','5f51478b-768e-4099-80b7-10a80ba9adfd','6e5e6f13-59a4-4267-bbc4-5bf4d7b99910','330f7f7f-2350-44a4-af7b-bdfd6bcd453c','845de4e6-0c42-40ac-a403-67c5ed6726b6','fd146c50-e8f7-4e47-9fa3-0e3bcd96976e','fd851b6d-e10b-4066-8cc2-8e8ff610bab0','96a43699-c6af-4e28-87f6-1a0dbaa6abaa','cbdfc150-bd25-47e0-aafe-e9fb85e6037a','d5be09a4-68f7-406a-8abc-bfb1da75f927','ab9c69a8-a5c1-466c-a1f1-c29decf06850','ecebacc8-d371-4541-b8b2-890dfd9e8a61','1caae824-92c0-47e8-998d-c16c4a6749d0','b9b5b489-21ef-4bde-8e9d-b0f688ee017b','a9cc11bf-3c4d-421a-a988-2b4dda759595','15884b1f-af5d-40c7-9223-07746264f168','74f40475-eeeb-4924-bdb1-ff5e520917b7','58b23a26-0cf7-487c-a423-b51e32583b5d','b47f68b9-0622-45ca-b2ca-b646e77f8b27','9bd01d94-ee06-4415-9054-56b0a3308e0c','8e15b801-6959-4ab9-ae00-63faf51141c6','27ec70c8-ccd4-4773-a637-964ed9ca0860','bab84fdf-da0e-473a-88f0-da9235d238e7','7da3f37e-692c-4bb8-bc1c-41a86f4f6481','3eba7e59-1843-441f-8cb2-8c2bff0dad34','506d355b-24bf-4de0-a627-b5adeceb62e1','9573d98e-9f79-4548-9292-11f9b42bba23','0ADDCAE3-530D-4D09-A94C-B930980670D7','96bb05f8-7312-4058-bb9c-f4e948ca7a16','8233d47b-031a-4100-9f39-f74ce8dfca6c','ab93795e-e5f9-4b6c-95e5-00353c85b6af','8c42ea21-ab98-49d7-8e5b-c284ff1d180c','219cddcd-b71d-4b1f-a4b5-bf739521d21c','0dd66a1c-2d6f-4b27-a996-561743cc9a25','28448ff2-ff18-44ab-b000-f2f5f2ec0378','17949de1-698b-4a15-a3c3-f8a02fec9fdd','4937ef3e-92e9-443e-9f49-042d1bbc09d8','7c40b9a4-6be2-489f-87c3-7b16383df0b2','d152cf57-a184-47f4-a2ae-4a966aff7946','0b24c2fc-5cf8-4bfc-93ea-370b86ca3a48','7cca0069-e27c-42ea-b241-fa896bf478df','64e097a5-7103-4b5a-b91b-9bedf6f1aa79','47b776cd-784a-453e-9507-59892c1f7ec5','00ae56fb-4f75-4c82-a02a-6ca19ce8ed13','d7e91ed2-88ac-4ef2-9a40-578df6a04e94','2d3ce8dd-291d-44a4-9b3f-13534b5953ee','98aef740-1558-40a2-a1c4-47f40881842a','1afabff4-2910-42c2-b309-ca78a0e20e05','1a39bfdc-b034-4631-bf8b-e4dcc575e871','1f3144e5-06f9-4abe-b701-34a23caf9d7e','dcbd2c89-a7da-436d-8a11-d93fd7514d73','01051782-201e-4f3f-91ca-a2c6a7ffbcd3','b3c11916-a3bc-403e-8271-0d0ca36d1b89','895b8d1b-da8f-4d3b-9a67-bed8ce94db66','138ae4ef-636d-4b06-a8c6-effe7306370d','9d641591-ae44-4b67-91cb-e4751912e7ea','a0767c6d-a5d0-4248-8831-ccaff3cfc6a9','c3418a6b-67bb-4b62-9f7e-4e0853ee701f','158c8545-cc7a-459f-8da0-f4c8a3f32e9d','e04216bd-c88c-4043-be37-921a3219ae42','c7f53930-9269-4b91-a65c-6516ab5e0443','4d2cecf5-b5b4-40e6-bf81-d989a4cec607','1f96f99f-f24c-4364-aa78-3da750e001ce',
#   'e888d5ef-ff23-4df4-aa45-8de9dc547348', '19a447c5-e949-4501-9f9e-e960868edab3')
#   GROUP BY ALL
# ),
# total_orders AS (
#   SELECT
#     o.country,
#     o.customer_id,
#     o.order_nr,
#     o.grand_total_eur,
#     o.grand_total_local_currency,
#     o.hellofresh_delivery_week as hf_delivery_week,
#     date(o.order_created_at) as order_created_date
#   FROM payments_hf.f_orders o
#   JOIN eligible_users e
#   ON o.customer_id = e.customer_id AND o.country = e.country
#   WHERE o.order_created_at >= timestamp('2024-07-01')
#   AND o.order_created_at >= e.event_datetime
# ),
# channel_loyalty as (
#   SELECT t.*,
#   case
#     when roi.reactivation_date is not null then 'Reactivation'
#     when rc.channel is not null then 'Referral'
#     else 'Paid'
#   end as category,
#   case
#     when roi.reactivation_date is not null then case
#       when roi.reactivation_channel in ('Amazon Employee Benefits','App Organic','App Paid Acquisition','B2B','B2B Conversion','B2B Revenue','Barter','Box Inserts','Brand Influencer','Customer Care Sorry Vouchers','Customer Care Sorry Vouchers New','Null','Sustainability','EveryShare Offline','Brand Partnership','Call Center','Channel Innovation','Checkout Alternate','CRM Paid App Acquisition','Cross Brand','Customer Care Sorry Vouchers','Customer Care Sorry Vouchers HelloShare New','Direct Mail CRM','Email Partnerships','Employee Discounts','EveryShare Online','Freebies','Gift boxes','HelloShare','HelloShare Offline','Influencer Boxes','Influencer Brand','Leads Generation','Organic','Organic Reactivation','Out of Home','PR','PR Boxen Influencer 2022','Print','Product Marketing','QA / Warehouse / Office boxes','QA Auto Test','Radio','Research','Revenue Partnerships','Security','SEA Reactivation','SEO Non-Brand','Social Media','TV Digital','TV Linear','Video Brand','Video Performance','WhatsApp','X-Channel'
#       ) then 'Other'
#       else roi.reactivation_channel
#     end
#     else case
#       when roi.activation_channel in ('Amazon Employee Benefits','App Organic','App Paid Acquisition','B2B','B2B Conversion','B2B Revenue','Barter','Box Inserts','Brand Influencer','Customer Care Sorry Vouchers','Customer Care Sorry Vouchers New','Null','Sustainability','EveryShare Offline','Brand Partnership','Call Center','Channel Innovation','Checkout Alternate','CRM Paid App Acquisition','Cross Brand','Customer Care Sorry Vouchers','Customer Care Sorry Vouchers HelloShare New','Direct Mail CRM','Email Partnerships','Employee Discounts','EveryShare Online','Freebies','Gift boxes','HelloShare','HelloShare Offline','Influencer Boxes','Influencer Brand','Leads Generation','Organic','Organic Reactivation','Out of Home','PR','PR Boxen Influencer 2022','Print','Product Marketing','QA / Warehouse / Office boxes','QA Auto Test','Radio','Research','Revenue Partnerships','Security','SEA Reactivation','SEO Non-Brand','Social Media','TV Digital','TV Linear','Video Brand','Video Performance','WhatsApp','X-Channel'
#       ) then 'Other'
#       else roi.activation_channel
#     end
#   end as channel,
#   case
#       when coalesce(cl.loyalty, 0) <= 5 then coalesce(cl.loyalty, 0)
#       when cl.loyalty <= 10 then '6-10'
#       when cl.loyalty <= 19 then '11-19'
#       when cl.loyalty <= 29 then '20-29'
#       when cl.loyalty <= 39 then '30-39'
#       when cl.loyalty <= 49 then '40-49'
#       else '50+'
#     end as loyalty_level
#   FROM total_orders t
#   LEFT JOIN (
#     SELECT country, customer_id, hf_delivery_week, activation_channel, reactivation_date, reactivation_channel
#     FROM payments_hf.customer_cohort_roi
#     WHERE hf_delivery_week >= '2024-W27' AND country IN ('US','AU','DE','FR','BE','GB','IT','NL')
#   ) as roi
#   ON roi.country = t.country AND roi.customer_id = t.customer_id AND roi.hf_delivery_week = t.hf_delivery_week
#   LEFT JOIN payments_hf.referral_channels rc
#   ON lower(rc.channel) = lower(roi.activation_channel)
#   LEFT JOIN (
#     SELECT country, customer_id, hf_delivery_week, loyalty
#     FROM payments_hf.f_customer_loyalty
#     WHERE hf_delivery_week >= '2024-W27' AND country IN ('US','AU','DE','FR','BE','GB','IT','NL')
#   ) as cl
#   on t.country = cl.country and t.customer_id = cl.customer_id and t.hf_delivery_week = cl.hf_delivery_week
# ),
# top_up_debits AS (
#     select
#         CASE WHEN contains(bst.reference_id, 'order_nr') THEN replace(bst.reference_id,'order_nr:','')
#           ELSE null
#           END AS order_nr,
#         bst.customer_uuid as fk_customer_uuid,
#         b.id_customer as customer_id,
#         bst.cash as cash_local_cur,
#         bst.bonus as bonus_local_cur,
#         bst.currency_code,
#         cast(
#           bst.cash * cdd.to_euro_conversion
#           as decimal(32,2)
#         ) as cash_eur,
#         cast(
#           bst.bonus * cdd.to_euro_conversion
#           as decimal(32,2)
#         ) as bonus_eur,
#         bst.created_at
#     from payments_hf.balance_service_transactions bst
#     JOIN dl_bob_live_non_pii.customer b
#     ON bst.customer_uuid = b.uuid
#     left join (
#       select currency_name, to_euro_conversion
#       from payments_hf.currency_dimension_daily
#       where date(conversion_date) = current_date() ) as cdd
#     on bst.currency_code = cdd.currency_name
#     where bst.created_at >= timestamp('2024-07-01')
#     and bst.type = 'DEBIT'
# )
# SELECT 
#     o.country,
#     o.loyalty_level,
#     o.category,
#     o.channel,
#     o.order_created_date,
#     dd.hellofresh_week,
#     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS hellofresh_year_month,
#     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS hellofresh_year_quarter,    
#     count(o.order_nr) as order_count,
#     count(distinct o.customer_id) as user_count,
#     sum(o.grand_total_eur) as order_sum_eur,
#     sum(o.grand_total_local_currency) as order_sum_local_cur,
#     count(t.order_nr) AS topup_order_count,
#     count(distinct t.customer_id) as topup_user_count,
#     sum(t.cash_eur)/100 as sum_topup_cash_eur,
#     sum(t.bonus_eur)/100 as sum_topup_bonus_eur,
#     sum(t.cash_local_cur)/100 as sum_topup_cash_local_cur,
#     sum(t.bonus_local_cur)/100 as sum_topup_bonus_local_cur
# FROM channel_loyalty o
# LEFT JOIN top_up_debits t
# ON o.order_nr = t.order_nr AND o.customer_id = t.customer_id
# INNER JOIN dimensions.date_dimension dd ON DATE(o.order_created_date) = DATE(dd.date_string_backwards)
# GROUP BY ALL

# COMMAND ----------

# %sql

# DROP TABLE IF EXISTS payments_hf.payments_p0_metrics_top_up_funnel;

# REFRESH TABLE payments_hf.topup_events_funnel; 

# CREATE TABLE payments_hf.payments_p0_metrics_top_up_funnel AS
# select a.*, 
#   dd.hellofresh_week,
#   CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS hellofresh_year_month,
#   CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS hellofresh_year_quarter
# from payments_hf.topup_events_funnel a
#   INNER JOIN dimensions.date_dimension dd ON DATE(a.event_date) = DATE(dd.date_string_backwards)
# WHERE level = 'day';


# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DROP TABLE IF EXISTS payments_hf.payments_p0_metrics_dunning;
# MAGIC
# MAGIC REFRESH TABLE payments_hf.dunning_dashboard;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE payments_hf.payments_p0_metrics_dunning AS WITH date_lkup AS (
# MAGIC   SELECT
# MAGIC     hellofresh_week,
# MAGIC     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS hellofresh_year_month,
# MAGIC     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS hellofresh_year_quarter
# MAGIC   FROM
# MAGIC     dimensions.date_dimension dd
# MAGIC   WHERE
# MAGIC     hellofresh_week >= '2022-W01'
# MAGIC   GROUP BY
# MAGIC     1,
# MAGIC     2,
# MAGIC     3
# MAGIC ),
# MAGIC date_lkup_row AS (
# MAGIC   SELECT
# MAGIC     *,
# MAGIC     ROW_NUMBER() OVER(ORDER BY hellofresh_week ASC) AS row_num
# MAGIC   FROM
# MAGIC     date_lkup
# MAGIC ),
# MAGIC final_date_lkup AS (
# MAGIC   SELECT
# MAGIC     a.hellofresh_week,
# MAGIC     a.hellofresh_year_month,
# MAGIC     a.hellofresh_year_quarter, 
# MAGIC     b.hellofresh_week AS lead_hellofresh_week,
# MAGIC     b.hellofresh_year_month AS lead_hellofresh_year_month,
# MAGIC     b.hellofresh_year_quarter AS lead_hellofresh_year_quarter
# MAGIC   FROM
# MAGIC     date_lkup_row a
# MAGIC     JOIN date_lkup_row b ON a.row_num = b.row_num - 12
# MAGIC )
# MAGIC SELECT
# MAGIC   dd.hellofresh_week,
# MAGIC   dd.hellofresh_year_month,
# MAGIC   dd.hellofresh_year_quarter,
# MAGIC   dd.lead_hellofresh_week,
# MAGIC   dd.lead_hellofresh_year_month,
# MAGIC   dd.lead_hellofresh_year_quarter, 
# MAGIC   country,
# MAGIC   CASE
# MAGIC       WHEN loyalty_level = '0' THEN '0'
# MAGIC       WHEN loyalty_level IN ('1', '2', '3', '4', '5') THEN '1-5'
# MAGIC       ELSE '6+'
# MAGIC     END AS loyalty_segment,
# MAGIC   CASE
# MAGIC       WHEN NOT (
# MAGIC         (
# MAGIC           RIGHT(COALESCE(last_10_order_statuses, ''), 2) = 'ff'
# MAGIC         )
# MAGIC       ) THEN 'Good'
# MAGIC       ELSE 'Bad'
# MAGIC     END AS customer_quality,  
# MAGIC   dunning_execution,
# MAGIC   SUM(
# MAGIC     CASE
# MAGIC       WHEN recovery_date <= delivery_date THEN order_nr
# MAGIC       ELSE 0
# MAGIC     END
# MAGIC   ) AS recovery_w0,
# MAGIC   SUM(
# MAGIC     CASE
# MAGIC       WHEN recovered_in_days <= 84 THEN order_nr
# MAGIC       ELSE 0
# MAGIC     END
# MAGIC   ) AS recovery_w12,
# MAGIC   SUM(order_nr) AS order_count,
# MAGIC   SUM(profit_check_week_eur) - SUM(
# MAGIC     CASE
# MAGIC       WHEN dunning_execution = 'shipped' AND (recovered_in_days > 84 OR recovered_in_days IS NULL) THEN grand_total_eur
# MAGIC       ELSE 0
# MAGIC     END    
# MAGIC   ) AS net_profit, -- cohorted 12weeks 
# MAGIC   SUM(
# MAGIC     CASE
# MAGIC       WHEN dunning_execution = 'shipped' AND (recovered_in_days > 84 OR recovered_in_days IS NULL) THEN grand_total_eur
# MAGIC       ELSE 0
# MAGIC     END    
# MAGIC   ) AS open_debt, -- cohorted 12weeks 
# MAGIC   SUM(grand_total_eur) AS grand_total_eur,
# MAGIC   SUM(profit_check_week_eur) FILTER(WHERE dunning_decision_reason = 'prediction')
# MAGIC   - SUM(
# MAGIC     CASE
# MAGIC       WHEN
# MAGIC         dunning_decision_reason = 'prediction'
# MAGIC         AND (
# MAGIC           recovered_in_days > 84
# MAGIC           OR recovered_in_days IS NULL
# MAGIC         )
# MAGIC       THEN
# MAGIC         grand_total_eur
# MAGIC       ELSE 0
# MAGIC     END
# MAGIC   ) AS prediction_net_profit, 
# MAGIC   SUM(order_nr)
# MAGIC     FILTER (
# MAGIC       WHERE dunning_decision_reason = 'prediction'
# MAGIC     ) AS prediction_order_count,
# MAGIC   SUM(exploration_weighted_count)
# MAGIC     FILTER (
# MAGIC       WHERE dunning_execution = 'shipped'
# MAGIC       AND dunning_decision_reason = 'exploration_ship'
# MAGIC     ) AS exploration_order_count,
# MAGIC   SUM(
# MAGIC     CASE
# MAGIC       WHEN
# MAGIC         dunning_execution = 'shipped'
# MAGIC         AND dunning_decision_reason = 'exploration_ship'
# MAGIC         AND profit_check_week_eur > 0
# MAGIC         AND recovered_in_days <= 84
# MAGIC       THEN
# MAGIC         profit_check_week_eur * exploration_weighted_count
# MAGIC       ELSE 0
# MAGIC     END
# MAGIC   ) AS exploration_net_profit -- cohorted 12weeks
# MAGIC FROM
# MAGIC   payments_hf.dunning_dashboard a
# MAGIC   JOIN final_date_lkup AS dd ON a.hellofresh_delivery_week = dd.hellofresh_week
# MAGIC WHERE
# MAGIC   hellofresh_delivery_week >= '2022-W01'
# MAGIC   AND product_type = 'mealbox'
# MAGIC
# MAGIC GROUP BY
# MAGIC   ALL;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DROP TABLE IF EXISTS payments_hf.payments_p0_metrics_reactivation_funnel;
# MAGIC
# MAGIC REFRESH TABLE payments_hf.f_pvs_replica;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE payments_hf.payments_p0_metrics_reactivation_funnel AS with pvs_base as (
# MAGIC   select
# MAGIC     pvs.*,
# MAGIC     dd.quarter,
# MAGIC     dd.iso_year_week AS hellofresh_week,
# MAGIC     CONCAT(dd.year, '-', dd.month) AS hellofresh_year_month,
# MAGIC     CONCAT(dd.year, '-', dd.quarter) AS hellofresh_year_quarter,
# MAGIC     1 AS attempt,
# MAGIC     case
# MAGIC       when pvs.verification_result = 'verified' then 1
# MAGIC       else 0
# MAGIC     end AS verified,
# MAGIC     row_number() over (
# MAGIC       partition by pvs.customer_uuid,
# MAGIC       pvs.`date`
# MAGIC       order by
# MAGIC         case
# MAGIC           when pvs.verification_result = 'verified' then 1
# MAGIC           else 0
# MAGIC         end DESC,
# MAGIC         pvs.created_at DESC
# MAGIC     ) as rn_final,
# MAGIC     row_number() over (
# MAGIC       partition by pvs.customer_uuid,
# MAGIC       pvs.`date`
# MAGIC       order by
# MAGIC         pvs.created_at
# MAGIC     ) as rn_first
# MAGIC   from
# MAGIC     payments_hf.f_pvs_replica pvs
# MAGIC     inner join dimensions.date_dimension dd on pvs.date = dd.date_string_backwards
# MAGIC   where
# MAGIC     created_at >= '2022-12-31'
# MAGIC     and workflow = 'reactivation'
# MAGIC )
# MAGIC select
# MAGIC   customer_uuid,
# MAGIC   country,
# MAGIC   `date`,
# MAGIC   customer_id,
# MAGIC   quarter,
# MAGIC   hellofresh_week,
# MAGIC   hellofresh_year_month,
# MAGIC   hellofresh_year_quarter,
# MAGIC   attempt,
# MAGIC   max(
# MAGIC     CASE
# MAGIC       WHEN rn_first = 1 THEN new_payment_method
# MAGIC     END
# MAGIC   ) as new_payment_method_first,
# MAGIC   max(
# MAGIC     CASE
# MAGIC       WHEN rn_first = 1 THEN case
# MAGIC         when coalesce(diff_with_max_reactivation, 0) in (0, '0-9', '10-19', '20-29') then 'less than 29w'
# MAGIC         else 'more than 29w'
# MAGIC       end
# MAGIC     END
# MAGIC   ) as diff_with_max_reactivation_first,
# MAGIC   max(
# MAGIC     CASE
# MAGIC       WHEN rn_first = 1 THEN CASE
# MAGIC         WHEN payment_method LIKE '%ApplePay' THEN 'Apple Pay'
# MAGIC         WHEN payment_method LIKE '%Paypal' THEN 'Paypal'
# MAGIC         WHEN payment_method LIKE '%CreditCard' THEN 'Credit Card'
# MAGIC         WHEN payment_method IS NULL THEN 'Unknown'
# MAGIC         ELSE 'Others'
# MAGIC       END
# MAGIC     END
# MAGIC   ) as payment_method_first,
# MAGIC   max(
# MAGIC     CASE
# MAGIC       WHEN rn_first = 1 THEN verified
# MAGIC     END
# MAGIC   ) as verified_first,
# MAGIC   max(
# MAGIC     CASE
# MAGIC       WHEN rn_final = 1 THEN new_payment_method
# MAGIC     END
# MAGIC   ) as new_payment_method_final,
# MAGIC   max(
# MAGIC     CASE
# MAGIC       WHEN rn_final = 1 THEN CASE
# MAGIC         WHEN payment_method LIKE '%ApplePay' THEN 'Apple Pay'
# MAGIC         WHEN payment_method LIKE '%Paypal' THEN 'Paypal'
# MAGIC         WHEN payment_method LIKE '%CreditCard' THEN 'Credit Card'
# MAGIC         WHEN payment_method IS NULL THEN 'Unknown'
# MAGIC         ELSE 'Others'
# MAGIC       END
# MAGIC     END
# MAGIC   ) as payment_method_final,
# MAGIC   max(
# MAGIC     CASE
# MAGIC       WHEN rn_final = 1 THEN verified
# MAGIC     END
# MAGIC   ) as verified_final
# MAGIC from
# MAGIC   pvs_base
# MAGIC group by
# MAGIC   all

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DROP TABLE IF EXISTS payments_hf.payments_p0_metrics_psp_performance;
# MAGIC
# MAGIC REFRESH TABLE payments_hf.f_pvs_replica;
# MAGIC REFRESH TABLE payments_hf.f_pps_charges;
# MAGIC REFRESH TABLE payments_hf.refunds_service_refunds;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE payments_hf.payments_p0_metrics_psp_performance AS
# MAGIC SELECT
# MAGIC   'TokenisationOrVerification' AS request_type,
# MAGIC   pvs.country,
# MAGIC   dd.iso_year_week AS hellofresh_week,
# MAGIC   CONCAT(dd.year, '-', dd.month) AS hellofresh_year_month,
# MAGIC   CONCAT(dd.year, '-', dd.quarter) AS hellofresh_year_quarter,
# MAGIC   pvs.provider,
# MAGIC   NULL AS is_refund,
# MAGIC   SUM(1) AS count_attempt,
# MAGIC   SUM(
# MAGIC     CASE
# MAGIC       WHEN pvs.verification_result = 'verified' THEN 1
# MAGIC     END
# MAGIC   ) AS count_success,
# MAGIC   SUM(
# MAGIC     CASE
# MAGIC       WHEN pvs.verification_result <> 'verified' THEN 1
# MAGIC     END
# MAGIC   ) AS count_failure
# MAGIC FROM
# MAGIC   payments_hf.f_pvs_replica pvs
# MAGIC   INNER JOIN dimensions.date_dimension dd ON pvs.date = dd.date_string_backwards
# MAGIC WHERE
# MAGIC   created_at >= '2022-12-31'
# MAGIC GROUP BY
# MAGIC   ALL
# MAGIC UNION ALL
# MAGIC SELECT
# MAGIC   'Charge' AS request_type,
# MAGIC   pps.business_unit AS country,
# MAGIC   dd.iso_year_week AS hellofresh_week,
# MAGIC   CONCAT(dd.year, '-', dd.month) AS hellofresh_year_month,
# MAGIC   CONCAT(dd.year, '-', dd.quarter) AS hellofresh_year_quarter,
# MAGIC   pps.provider,
# MAGIC   CASE WHEN r.transaction_id IS NOT NULL THEN 1 ELSE 0 END AS is_refund,
# MAGIC   SUM(1) AS count_attempt,
# MAGIC   SUM(
# MAGIC     CASE
# MAGIC       WHEN pps.status IN ('authorised', 'authorized') THEN 1
# MAGIC     END
# MAGIC   ) AS count_success,
# MAGIC   SUM(
# MAGIC     CASE
# MAGIC       WHEN NOT(pps.status IN ('authorised', 'authorized')) THEN 1
# MAGIC     END
# MAGIC   ) AS count_failure
# MAGIC FROM
# MAGIC   payments_hf.f_pps_charges pps
# MAGIC LEFT JOIN payments_hf.refunds_service_refunds r
# MAGIC ON r.transaction_id = pps.fk_transaction  
# MAGIC   INNER JOIN dimensions.date_dimension dd ON DATE(pps.created_at) = DATE(dd.date_string_backwards)
# MAGIC WHERE
# MAGIC   pps.created_at >= '2022-12-31'
# MAGIC GROUP BY
# MAGIC   ALL;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.payments_p0_metrics_chargeback;
# MAGIC
# MAGIC REFRESH TABLE payments_hf.chargebacks_dashboard;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE payments_hf.payments_p0_metrics_chargeback AS WITH date_lkup AS (
# MAGIC   SELECT
# MAGIC     hellofresh_week,
# MAGIC     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS hellofresh_year_month,
# MAGIC     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS hellofresh_year_quarter
# MAGIC   FROM
# MAGIC     dimensions.date_dimension dd
# MAGIC   WHERE
# MAGIC     hellofresh_week >= '2022-W01'
# MAGIC   GROUP BY
# MAGIC     1,
# MAGIC     2,
# MAGIC     3
# MAGIC ),
# MAGIC date_lkup_row AS (
# MAGIC   SELECT
# MAGIC     *,
# MAGIC     ROW_NUMBER() OVER(
# MAGIC       ORDER BY
# MAGIC         hellofresh_week ASC
# MAGIC     ) AS row_num
# MAGIC   FROM
# MAGIC     date_lkup
# MAGIC ),
# MAGIC final_date_lkup AS (
# MAGIC   SELECT
# MAGIC     a.hellofresh_week,
# MAGIC     a.hellofresh_year_month,
# MAGIC     a.hellofresh_year_quarter,
# MAGIC     b.hellofresh_week AS lead_hellofresh_week,
# MAGIC     b.hellofresh_year_month AS lead_hellofresh_year_month,
# MAGIC     b.hellofresh_year_quarter AS lead_hellofresh_year_quarter
# MAGIC   FROM
# MAGIC     date_lkup_row a
# MAGIC     JOIN date_lkup_row b ON a.row_num = b.row_num - 13
# MAGIC )
# MAGIC SELECT
# MAGIC   dd.lead_hellofresh_week,
# MAGIC   dd.lead_hellofresh_year_month,
# MAGIC   dd.lead_hellofresh_year_quarter,
# MAGIC   a.*,
# MAGIC   CASE
# MAGIC     WHEN a.token = 'apple_pay' THEN 'Apple Pay'
# MAGIC     WHEN a.token = 'paypal' THEN 'Paypal'
# MAGIC     WHEN a.token = 'credit_card' THEN 'Credit Card'
# MAGIC     WHEN a.token = 'sepadirectdebit' THEN 'SEPA'
# MAGIC     -- WHEN a.latest_token IS NULL THEN 'Unknown' -- very low percentage
# MAGIC     ELSE 'Others'
# MAGIC   END AS payment_method_reporting
# MAGIC from
# MAGIC   payments_hf.chargebacks_dashboard AS a
# MAGIC   JOIN final_date_lkup AS dd ON a.iso_year_week = dd.hellofresh_week
# MAGIC where a.date_type = 'Delivery Date'
# MAGIC ;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.payments_p0_metrics_payment_cost;
# MAGIC
# MAGIC REFRESH TABLE dimensions.date_dimension;
# MAGIC REFRESH TABLE public_edw_business_mart_live.order_line_items_eur;
# MAGIC REFRESH TABLE public_ffdp_finance_pc2_live.box_level_profit_contribution_enriched;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE payments_hf.payments_p0_metrics_payment_cost AS WITH date_lkup AS (
# MAGIC   SELECT
# MAGIC     hellofresh_week,
# MAGIC     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS hellofresh_year_month,
# MAGIC     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS hellofresh_year_quarter
# MAGIC   FROM
# MAGIC     dimensions.date_dimension dd
# MAGIC   WHERE
# MAGIC     hellofresh_week >= '2023-W01'
# MAGIC   GROUP BY
# MAGIC     1,
# MAGIC     2,
# MAGIC     3
# MAGIC ),
# MAGIC revenue AS (
# MAGIC   SELECT
# MAGIC   oli.bob_entity_code
# MAGIC   , oli.hellofresh_delivery_week AS hellofresh_week
# MAGIC   , SUM(COALESCE(oli.order_item_revenue_excl_sales_tax, 0) 
# MAGIC     + COALESCE(oli.shipping_revenue_excl_sales_tax, 0)) AS gross_revenue_euro
# MAGIC   , COUNT(DISTINCT oli.composite_order_id) AS delivered_orders
# MAGIC
# MAGIC   FROM public_edw_business_mart_live.order_line_items_eur oli
# MAGIC   WHERE oli.hellofresh_delivery_week >= '2023-W01'
# MAGIC   AND oli.is_delivered
# MAGIC   GROUP BY ALL
# MAGIC ),
# MAGIC payment_cost AS (
# MAGIC   SELECT
# MAGIC   pc.country
# MAGIC   , pc.hellofresh_week
# MAGIC   , SUM(pc.ppf_total_cost_eur) AS payment_cost_euro
# MAGIC
# MAGIC   FROM public_ffdp_finance_pc2_live.box_level_profit_contribution_enriched pc -- Change: Dec 16th
# MAGIC   WHERE pc.hellofresh_week >= '2023-W01'
# MAGIC   GROUP BY ALL
# MAGIC )
# MAGIC , union_all AS (
# MAGIC   SELECT
# MAGIC   bob_entity_code AS country
# MAGIC   , hellofresh_week
# MAGIC   , gross_revenue_euro
# MAGIC   , delivered_orders
# MAGIC   , NULL AS payment_cost_euro
# MAGIC
# MAGIC   FROM revenue
# MAGIC
# MAGIC   UNION ALL
# MAGIC   
# MAGIC   SELECT
# MAGIC   country
# MAGIC   , hellofresh_week
# MAGIC   , NULL AS gross_revenue_euro
# MAGIC   , NULL AS delivered_orders
# MAGIC   , payment_cost_euro
# MAGIC
# MAGIC   FROM payment_cost
# MAGIC )
# MAGIC SELECT
# MAGIC   a.country
# MAGIC   , a.hellofresh_week
# MAGIC   , b.hellofresh_year_month
# MAGIC   , b.hellofresh_year_quarter
# MAGIC   , SUM(a.gross_revenue_euro) AS gross_revenue_euro
# MAGIC   , SUM(a.payment_cost_euro) AS payment_cost_euro
# MAGIC   , SUM(a.delivered_orders) AS delivered_orders
# MAGIC
# MAGIC FROM union_all AS a
# MAGIC JOIN date_lkup AS b
# MAGIC ON a.hellofresh_week = b.hellofresh_week
# MAGIC GROUP BY ALL
# MAGIC ;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DROP TABLE IF EXISTS payments_hf.payments_p0_metrics_cash_credits;
# MAGIC
# MAGIC REFRESH TABLE payments_hf.currency_dimension_daily;
# MAGIC REFRESH TABLE payments_hf.business_units;
# MAGIC REFRESH TABLE dimensions.date_dimension;
# MAGIC REFRESH TABLE public_edw_base_grain_live.issued_credits;
# MAGIC REFRESH TABLE public_edw_base_grain_live.redeemed_credits;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE payments_hf.payments_p0_metrics_cash_credits AS WITH base AS (
# MAGIC   SELECT
# MAGIC     DATE(ic.transaction_time_utc) AS transaction_date,
# MAGIC     ic.country,
# MAGIC     'CashCreditAdded' AS CashCreditType,
# MAGIC     SUM(ic.credits_amount) AS ValueLocal,
# MAGIC     SUM(ic.credits_amount * cdd.to_euro_conversion) AS ValueEuro
# MAGIC   FROM
# MAGIC     public_edw_base_grain_live.issued_credits AS ic
# MAGIC     JOIN payments_hf.business_units AS bu ON ic.country = bu.business_unit
# MAGIC     JOIN payments_hf.currency_dimension_daily AS cdd ON bu.currency = cdd.currency_name
# MAGIC     AND DATE(ic.transaction_time_utc) = DATE(cdd.conversion_date)
# MAGIC   GROUP BY
# MAGIC     1,
# MAGIC     2
# MAGIC   UNION
# MAGIC   SELECT
# MAGIC     DATE(rc.transaction_time_utc) AS transaction_date,
# MAGIC     rc.country,
# MAGIC     'CashCreditSpent' AS CashCreditType,
# MAGIC     SUM(rc.credits_amount) AS ValueLocal,
# MAGIC     SUM(rc.credits_amount * cdd.to_euro_conversion) AS ValueEuro
# MAGIC   FROM
# MAGIC     public_edw_base_grain_live.redeemed_credits AS rc
# MAGIC     JOIN payments_hf.business_units AS bu ON rc.country = bu.business_unit
# MAGIC     JOIN payments_hf.currency_dimension_daily AS cdd ON bu.currency = cdd.currency_name
# MAGIC     AND DATE(rc.transaction_time_utc) = DATE(cdd.conversion_date)
# MAGIC   GROUP BY
# MAGIC     1,
# MAGIC     2
# MAGIC )
# MAGIC SELECT
# MAGIC   transaction_date,
# MAGIC   country,
# MAGIC   CashCreditType,
# MAGIC   ValueLocal,
# MAGIC   ValueEuro,
# MAGIC   dd.hellofresh_week,
# MAGIC   CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS hellofresh_year_month,
# MAGIC   CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS hellofresh_year_quarter
# MAGIC FROM
# MAGIC   base AS b
# MAGIC   INNER JOIN dimensions.date_dimension dd ON DATE(b.transaction_date) = DATE(dd.date_string_backwards);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DROP TABLE IF EXISTS payments_hf.payments_p0_metrics_top_up_actives;
# MAGIC
# MAGIC REFRESH TABLE payments_hf.ek_metrics_topup_adoption;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE payments_hf.payments_p0_metrics_top_up_actives AS WITH date_lkup AS (
# MAGIC   SELECT
# MAGIC     hellofresh_week,
# MAGIC     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS hellofresh_year_month,
# MAGIC     CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS hellofresh_year_quarter
# MAGIC   FROM
# MAGIC     dimensions.date_dimension dd
# MAGIC   WHERE
# MAGIC     hellofresh_week >= '2023-W01'
# MAGIC   GROUP BY
# MAGIC     1,
# MAGIC     2,
# MAGIC     3
# MAGIC )
# MAGIC SELECT 
# MAGIC a.customer_uuid,
# MAGIC a.country,
# MAGIC a.hellofresh_week,
# MAGIC b.hellofresh_year_month,
# MAGIC b.hellofresh_year_quarter
# MAGIC FROM payments_hf.ek_metrics_topup_adoption AS a
# MAGIC JOIN date_lkup AS b
# MAGIC ON a.hellofresh_week = b.hellofresh_week
# MAGIC GROUP BY ALL
# MAGIC ;

# COMMAND ----------

metric_schema = {
    "Checkout Funnel": {
        "focus_group": "1_Activation (Paid + Referrals)",
        "metric_group": "1_Checkout Funnel",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_checkout_funnel",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "0_PaymentPageVisit": {
                "numerator": "SUM(CASE WHEN is_pay_visit = 1 THEN customer_count ELSE 0 END)",
                "denominator": "AVG(1)",
                "metric_type": "number",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },
            "1_PaymentPageVisitToSuccess": {
                "numerator": "SUM(CASE WHEN is_pay_visit = 1 AND is_success = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_pay_visit = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Payment Offering Squad",
            },            
            "2_SelectToSuccess": {
                "numerator": "SUM(CASE WHEN is_select = 1 AND is_success = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_select = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Payment Offering Squad",
            },  
            "3_Drop from Select to Click": {
                "numerator": "SUM(CASE WHEN is_select = 1 AND is_click = 0 AND is_success = 0 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_select = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },  
            "4_Drop from Click to FS": {
                "numerator": "SUM(CASE WHEN is_select = 1 AND is_click = 1 AND is_success = 0 AND is_pvs = 0 AND (NOT (COALESCE(is_voucher_fraud_block, false) = 1 OR COALESCE(is_payment_fraud_block, 0) = 1)) THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_select = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },                          
            "5_Drop in FS (Blocked)": {
                "numerator": "SUM(CASE WHEN is_select = 1 AND is_click = 1 AND is_pvs = 0 AND (COALESCE(is_voucher_fraud_block, false) = 1 OR COALESCE(is_payment_fraud_block, 0) = 1) THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_select = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },              
            "6_Drop in Payment Service": {
                "numerator": "SUM(CASE WHEN is_select = 1 AND is_click = 1 AND is_pvs = 1 AND is_success = 0 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_select = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },  
            "7_Duplicates Identified Pre-Checkout": {
                "numerator": "SUM(CASE WHEN is_fs_check = 1 AND is_duplicate_at_pre_checkout = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
            "8_Blocked Duplicates Pre-Checkout": {
                "numerator": "SUM(CASE WHEN is_fs_check = 1 AND is_voucher_fraud_block = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
            "9_Blocked Payment Fraud": {
                "numerator": "SUM(CASE WHEN is_fs_check = 1 AND is_payment_fraud_block = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
            "10_Duplicates Identified Post-CheckoutRate": {
                "numerator": "SUM(CASE WHEN is_duplicate_at_post_checkout = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
            "11_FraudApprovalRate": {
                "numerator": "SUM(CASE WHEN is_fs_check = 1 AND COALESCE(CAST(is_voucher_fraud_block AS INT), 0) = 0 AND COALESCE(CAST(is_payment_fraud_block AS INT), 0) = 0 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Risk & Fraud Management Squad",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "ChannelCategory": "category",
            "PaymentMethod": "payment_method_reporting",
        },
        "dimension_mapping": {
            "_Overall": [
                "0_PaymentPageVisit",
                "1_PaymentPageVisitToSuccess",
                "2_SelectToSuccess",
                "3_Drop from Select to Click",
                "4_Drop from Click to FS",
                "5_Drop in FS (Blocked)",
                "6_Drop in Payment Service",
                "7_Duplicates Identified Pre-Checkout",
                "8_Blocked Duplicates Pre-Checkout",
                "9_Blocked Payment Fraud",
                "10_Duplicates Identified Post-CheckoutRate",
                "11_FraudApprovalRate",
            ],
            "ChannelCategory": [
                "7_Duplicates Identified Pre-Checkout",
                "8_Blocked Duplicates Pre-Checkout",
                "9_Blocked Payment Fraud",
                "10_Duplicates Identified Post-CheckoutRate",
                "11_FraudApprovalRate",
            ],
            "PaymentMethod": [
                "2_SelectToSuccess",
                "3_Drop from Select to Click",
                "4_Drop from Click to FS",
                "5_Drop in FS (Blocked)",
                "6_Drop in Payment Service",
                "11_FraudApprovalRate",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
  AND is_different_checkout = FALSE
    """,
    },
    "Checkout Funnel Backend": {
        "focus_group": "1_Activation (Paid + Referrals)",
        "metric_group": "1_Checkout Funnel (backend)",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_checkout_funnel_backend",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "0_PaymentPageVisit": {
                "numerator": "SUM(CASE WHEN event_payment_method_listed = 1 THEN customer_count ELSE 0 END)",
                "denominator": "AVG(1)",
                "metric_type": "number",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },            
            "1_PaymentPageVisitToSuccess": {
                "numerator": "SUM(CASE WHEN event_payment_method_listed = 1 AND (event_attempted_fraud_check = 1 OR event_attempted_payment_verification = 1) AND event_successful_conversion = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN event_payment_method_listed = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Payment Offering Squad",
            },            
            "2_PaymentPageVisitToFS": {
                "numerator": "SUM(CASE WHEN event_payment_method_listed = 1 AND event_attempted_fraud_check = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN event_payment_method_listed = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },  
            "3_FSToPVS": {
                "numerator": "SUM(CASE WHEN event_payment_method_listed = 1 AND event_attempted_fraud_check = 1 AND event_attempted_payment_verification = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN event_payment_method_listed = 1 AND event_attempted_fraud_check = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },  
            "4_PVSToSuccess": {
               "numerator": "SUM(CASE WHEN event_payment_method_listed = 1 AND (event_attempted_fraud_check = 1 OR event_attempted_payment_verification = 1) AND event_successful_conversion = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN event_payment_method_listed = 1 AND (event_attempted_fraud_check = 1 OR event_attempted_payment_verification = 1) AND event_attempted_payment_verification = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },
            "5_PaymentCheckoutApprovalRate": {
                "numerator": "SUM(CASE WHEN event_payment_verification_success = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN event_attempted_payment_verification = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Payment Offering Squad",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "PaymentMethod": "payment_method_reporting",
        },
        "dimension_mapping": {
            "_Overall": [
                "0_PaymentPageVisit",
                "1_PaymentPageVisitToSuccess",
                "2_PaymentPageVisitToFS",
                "3_FSToPVS",
                "4_PVSToSuccess",
                "5_PaymentCheckoutApprovalRate",
            ],
            "PaymentMethod": [
                "4_PVSToSuccess",
                "5_PaymentCheckoutApprovalRate",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
    """,
    },
    "VoucherFraud": {
        "focus_group": "1_Activation (Paid + Referrals)",
        "metric_group": "2_Voucher Fraud",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_checkout_funnel",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "1_Total Duplicate Rate": {
                "numerator": "SUM(CASE WHEN (is_duplicate_at_post_checkout = 1) OR (is_fs_check = 1 AND is_duplicate_at_pre_checkout = 1) THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "TRUE",
                "team_ownership": "Risk & Fraud Management Squad",
            },
            "2_Total Duplicate Block Rate": {
                "numerator": "SUM(CASE WHEN (is_post_checkout_block = 1) OR (is_fs_check = 1 AND is_voucher_fraud_block = 1) THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "TRUE",
                "team_ownership": "Risk & Fraud Management Squad",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "ChannelCategory": "category",
        },
        "dimension_mapping": {
            "_Overall": [
                "1_Total Duplicate Rate",
                "2_Total Duplicate Block Rate",
            ],
            "ChannelCategory": [
                "1_Total Duplicate Rate",
                "2_Total Duplicate Block Rate",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
  AND is_different_checkout = FALSE
  AND is_post_checkout_block IS NOT NULL
    """,
    },
    "PaymentFraudActivation": {
        "focus_group": "1_Activation (Paid + Referrals)",
        "metric_group": "3_Payment Fraud",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_checkout_funnel",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "1_Payment Fraud Block Rate": {
                "numerator": "SUM(CASE WHEN is_fs_check = 1 AND is_payment_fraud_block = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "TRUE",
                "team_ownership": "Risk & Fraud Management Squad",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "ChannelCategory": "category",
        },
        "dimension_mapping": {
            "_Overall": [
                "1_Payment Fraud Block Rate",
            ],
            "ChannelCategory": [
                "1_Payment Fraud Block Rate",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
  AND is_different_checkout = FALSE
  AND is_post_checkout_block IS NOT NULL
    """,
    },    
    "Empty Activations": {
        "focus_group": "1_Activation (Paid + Referrals)",
        "metric_group": "4_Empty Activations (3wk lag)",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_empty_conversions",
        "date_granularity_mapping": {
            "WEEK": "lead_hellofresh_week",
            "MONTH": "lead_hellofresh_year_month",
            "QUARTER": "lead_hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "1_EmptyActivations3wk": {
                "numerator": "SUM(CASE WHEN net_activations_3wk = 0 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(customer_count)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
            "2_EA AOCS": {
                "numerator": "SUM(CASE WHEN net_activations_3wk = 0 AND empty_conversion_reason_group = 'AOCS' THEN customer_count ELSE 0 END)",
                "denominator": "SUM(customer_count)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
            "3_EA PaymentFail": {
                "numerator": "SUM(CASE WHEN net_activations_3wk = 0 AND empty_conversion_reason_group IN ('Dunning', 'ASCS') THEN customer_count ELSE 0 END)",
                "denominator": "SUM(customer_count)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
            "4_EA CustomerInitiatedCancellation": {
                "numerator": "SUM(CASE WHEN net_activations_3wk = 0 AND empty_conversion_reason_group IN ('Customer Cancellation', 'CC Cancellation') THEN customer_count ELSE 0 END)",
                "denominator": "SUM(customer_count)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
            "5_EA VoucherFraud": {
                "numerator": "SUM(CASE WHEN net_activations_3wk = 0 AND empty_conversion_reason_group IN ('Voucher Fraud') THEN customer_count ELSE 0 END)",
                "denominator": "SUM(customer_count)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
            "6_EA Others": {
                "numerator": "SUM(CASE WHEN net_activations_3wk = 0 AND empty_conversion_reason_group NOT IN ('Customer Cancellation', 'Dunning', 'ASCS', 'AOCS', 'CC Cancellation', 'Voucher Fraud') THEN customer_count ELSE 0 END)",
                "denominator": "SUM(customer_count)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "ChannelCategory": "Category",
        },
        "dimension_mapping": {
            "_Overall": [
                "1_EmptyActivations3wk",
                "2_EA AOCS",
                "3_EA PaymentFail",
                "4_EA CustomerInitiatedCancellation",
                "5_EA VoucherFraud",
                "6_EA Others",
            ],
            "ChannelCategory": [
                "1_EmptyActivations3wk",
                "2_EA AOCS",
                "3_EA PaymentFail",
                "4_EA CustomerInitiatedCancellation",
                "5_EA VoucherFraud",
                "6_EA Others",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
  AND Category IN ('Paid', 'Referrals')
    """,
    },
    "Empty Activations PaymentFail": {
        "focus_group": "1_Activation (Paid + Referrals)",
        "metric_group": "4_Empty Activations (3wk lag)",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_empty_conversions",
        "date_granularity_mapping": {
            "WEEK": "lead_hellofresh_week",
            "MONTH": "lead_hellofresh_year_month",
            "QUARTER": "lead_hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "3_EA PaymentFail": {
                "numerator": "SUM(CASE WHEN net_activations_3wk = 0 AND empty_conversion_reason_group IN ('Dunning', 'ASCS') THEN customer_count ELSE 0 END)",
                "denominator": "AVG(1)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
        },
        "dimension_value_mapping": {
            "DetailedReason": "empty_conversion_reason_group",
        },
        "dimension_mapping": {
            "DetailedReason": [
                "3_EA PaymentFail",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
  AND Category IN ('Paid', 'Referrals')
  AND net_activations_3wk = 0
  AND empty_conversion_reason_group IN ('Dunning', 'ASCS')
    """,
    },    
    "ReactivationFunnel": {
        "focus_group": "2_Reactivations",
        "metric_group": "1_ReactivationFunnel",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_reactivation_funnel",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            # "1_FirstReactivationDrop": {
            #     "numerator": """(SUM(attempt) - SUM(verified_first))""",
            #     "denominator": "SUM(attempt)",
            #     "metric_type": "ratio",
            #     "more_is_good": "FALSE",
            # },
            # "2_FRDExistingToken": {
            #     "numerator": """
            #     (SUM(CASE WHEN new_payment_method_first = false THEN attempt END) - SUM(CASE WHEN new_payment_method_first = false THEN verified_first END))
            #     """,
            #     "denominator": "SUM(CASE WHEN new_payment_method_first = false THEN attempt END)",
            #     "metric_type": "ratio",
            #     "more_is_good": "FALSE",
            # },
            # "3_FRDExistingTokenRecovered": {
            #     "numerator": """(SUM(CASE WHEN new_payment_method_first = false THEN verified_final END))""",
            #     "denominator": "SUM(CASE WHEN new_payment_method_first = false THEN attempt END)",
            #     "metric_type": "ratio",
            #     "more_is_good": "TRUE",
            # },
            # "4_FRDNewToken": {
            #     "numerator": """
            #     (SUM(CASE WHEN new_payment_method_first = true THEN attempt END) - SUM(CASE WHEN new_payment_method_first = true THEN verified_first END))
            #     """,
            #     "denominator": "SUM(CASE WHEN new_payment_method_first = true THEN attempt END)",
            #     "metric_type": "ratio",
            #     "more_is_good": "FALSE",
            # },
            # "5_FRDNewTokenRecovered": {
            #     "numerator": """(SUM(CASE WHEN new_payment_method_first = true THEN verified_final END))""",
            #     "denominator": "SUM(CASE WHEN new_payment_method_first = true THEN attempt END)",
            #     "metric_type": "ratio",
            #     "more_is_good": "TRUE",
            # },
            "1_ReactivationRate": {
                "numerator": """(SUM(verified_final))""",
                "denominator": "SUM(attempt)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Payment Offering Squad",
            },
            "2_Drop in Existing Token": {
                "numerator": """(SUM(CASE WHEN new_payment_method_final = false THEN attempt END) - SUM(CASE WHEN new_payment_method_final = false THEN verified_final END))""",
                "denominator": "SUM(attempt)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            }, 
            "3_Drop in New Token": {
                "numerator": """(SUM(CASE WHEN new_payment_method_final = true THEN attempt END) - SUM(CASE WHEN new_payment_method_final = true THEN verified_final END))""",
                "denominator": "SUM(attempt)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },                        
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "LastReactivationWeek": "diff_with_max_reactivation_first",
            # "PaymentMethodFirst": "payment_method_first",
            "PaymentMethod": "payment_method_final",
            # "FinalTokenType": "new_payment_method_final",
        },
        "dimension_mapping": {
            "_Overall": [
                "1_ReactivationRate",
                "2_Drop in Existing Token",
                "3_Drop in New Token",
                # "4_FRDNewToken",
                # "5_FRDNewTokenRecovered",
                # "6_FinalReactivationRate",
            ],
            "LastReactivationWeek": [
                "2_Drop in Existing Token",
            ],
            "PaymentMethod": [
                "1_ReactivationRate",
                "2_Drop in Existing Token",
                "3_Drop in New Token",
            ],
            # "PaymentMethodLast": [
            #     "3_FRDExistingTokenRecovered",
            #     "5_FRDNewTokenRecovered",
            #     "6_FinalReactivationRate",
            # ],
            # "FinalTokenType": [
            #     "6_FinalReactivationRate",
            # ],
        },
        "where_filter": """
  WHERE
  1 = 1
    """,
    },
    "Empty Reactivations": {
        "focus_group": "2_Reactivations",
        "metric_group": "2_Empty Reactivations (3wk lag)",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_empty_conversions",
        "date_granularity_mapping": {
            "WEEK": "lead_hellofresh_week",
            "MONTH": "lead_hellofresh_year_month",
            "QUARTER": "lead_hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "1_EmptyReactivation3wk": {
                "numerator": "SUM(CASE WHEN net_reactivations_3wk = 0 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(customer_count)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
            "2_ER PaymentFail": {
                "numerator": "SUM(CASE WHEN net_reactivations_3wk = 0 AND empty_conversion_reason_group IN ('Dunning', 'ASCS') THEN customer_count ELSE 0 END)",
                "denominator": "SUM(customer_count)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
            "3_ER CustomerInitiatedCancellation": {
                "numerator": "SUM(CASE WHEN net_reactivations_3wk = 0 AND empty_conversion_reason_group IN ('Customer Cancellation', 'CC Cancellation') THEN customer_count ELSE 0 END)",
                "denominator": "SUM(customer_count)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
            "4_ER Paused": {
                "numerator": "SUM(CASE WHEN net_reactivations_3wk = 0 AND empty_conversion_reason_group IN ('Paused') THEN customer_count ELSE 0 END)",
                "denominator": "SUM(customer_count)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },                        
            "5_ER Others": {
                "numerator": "SUM(CASE WHEN net_reactivations_3wk = 0 AND empty_conversion_reason_group NOT IN ('Dunning', 'ASCS', 'Customer Cancellation', 'CC Cancellation', 'Paused') THEN customer_count ELSE 0 END)",
                "denominator": "SUM(customer_count)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",      
        },
        "dimension_mapping": {
            "_Overall": [
                "1_EmptyReactivation3wk",
                "2_ER PaymentFail",
                "3_ER CustomerInitiatedCancellation",
                "4_ER Paused",
                "5_ER Others",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
  AND Category IN ('Reactivation')
    """,
    },
    "Empty Reactivations PaymentFail": {
        "focus_group": "2_Reactivations",
        "metric_group": "2_Empty Reactivations (3wk lag)",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_empty_conversions",
        "date_granularity_mapping": {
            "WEEK": "lead_hellofresh_week",
            "MONTH": "lead_hellofresh_year_month",
            "QUARTER": "lead_hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "2_ER PaymentFail": {
                "numerator": "SUM(CASE WHEN net_reactivations_3wk = 0 AND empty_conversion_reason_group IN ('Dunning', 'ASCS') THEN customer_count ELSE 0 END)",
                "denominator": "AVG(1)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
        },
        "dimension_value_mapping": {
            "DetailedReason": "empty_conversion_reason_group",
        },
        "dimension_mapping": {
            "DetailedReason": [
                "2_ER PaymentFail",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
  AND Category IN ('Reactivation')
  AND net_reactivations_3wk = 0
  AND empty_conversion_reason_group IN ('Dunning', 'ASCS')
    """,
    },    
    "AR": {
        "focus_group": "3_Active",
        "metric_group": "1_1_Overall Total Box Candidates",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_box_candidates",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "1_FirstRunAR": {
                "numerator": "SUM(1_FirstRunAR)",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
                "team_ownership": "Payment Platform Squad",
            },
            "2_PreDunningAR": {
                "numerator": "SUM(2_PreDunningAR)",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Payment Platform Squad",
            },
            "3_PostDunningAR": {
                "numerator": "SUM(3_PostDunningAR)",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Payment Platform Squad",
            },
            "4_DunningCancellations": {
                "numerator": """SUM(CASE WHEN dunning_execution = 'cancelled' THEN order_count ELSE 0 END)""",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
                "team_ownership": "Payment Platform Squad",
            }, 
            "5_RevenueDunningCancellations": {
                "numerator": """SUM(CASE WHEN dunning_execution = 'cancelled' THEN grand_total_eur ELSE 0 END)""",
                "denominator": "SUM(grand_total_eur)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
                "team_ownership": "Payment Platform Squad",
            },
            "6_PaymentApprovalRate": {
                "numerator": "SUM(is_payment_approved)",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Payment Platform Squad",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "PaymentMethod": "payment_method_reporting",
            "PaymentProvider": "first_provider_reporting",
            "CustomerQuality": "customer_quality",
            "OrderType": "order_type_reporting",
            "PaymentMethod_OrderType": "payment_method_order_type_reporting",
            # "DeclineReason_FirstRun": "decline_reason_first_run_reporting",
            "DeclineReason_PreDunning": "decline_reason_pre_dunning_reporting",
            "DeclineReason_PostDunning": "decline_reason_post_dunning_reporting",        
        },
        "dimension_mapping": {
            "_Overall": [
                "1_FirstRunAR",
                "2_PreDunningAR",
                "3_PostDunningAR", 
                "4_DunningCancellations",
                "5_RevenueDunningCancellations",
                "6_PaymentApprovalRate",
            ],
            "PaymentMethod": [
                "2_PreDunningAR",
                "3_PostDunningAR",
                "6_PaymentApprovalRate",
            ],
            "PaymentProvider": [
                "2_PreDunningAR",
                "3_PostDunningAR",
                "6_PaymentApprovalRate",
            ],
            "CustomerQuality": [
                "2_PreDunningAR",
                "3_PostDunningAR",
                "6_PaymentApprovalRate",
            ],            
            "OrderType": [
                "2_PreDunningAR",
                "3_PostDunningAR",
                "6_PaymentApprovalRate",
            ],            
            "PaymentMethod_OrderType": [
                "2_PreDunningAR",
                "3_PostDunningAR",
                "6_PaymentApprovalRate",
            ],      
            "DeclineReason_PreDunning": [
                "2_PreDunningAR",
            ],  
            "DeclineReason_PostDunning": [
                "3_PostDunningAR",              
            ],                                    
        },
        "where_filter": """
  WHERE
  1 = 1
  AND product_type = 'mealbox'
  AND segment IS NOT NULL
  AND customer_loyalty IS NOT NULL
    """,
    },
    "Loyalty-zero-initial-AR": {
        "focus_group": "3_Active",
        "metric_group": "1_2_Loyalty: LL0 (Initial charges)",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_box_candidates",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "1_FirstRunAR": {
                "numerator": "SUM(1_FirstRunAR)",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
                "team_ownership": "Payment Platform Squad",
            },
            "2_PreDunningAR": {
                "numerator": "SUM(2_PreDunningAR)",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Payment Platform Squad",
            },
            "3_PostDunningAR": {
                "numerator": "SUM(3_PostDunningAR)",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Payment Platform Squad",
            },
            "4_DunningCancellations": {
                "numerator": """SUM( CASE WHEN dunning_execution = 'cancelled' THEN order_count ELSE 0 END)""",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
                "team_ownership": "Payment Platform Squad",
            }, 
            "5_RevenueDunningCancellations": {
                "numerator": """SUM( CASE WHEN dunning_execution = 'cancelled' THEN grand_total_eur ELSE 0 END)""",
                "denominator": "SUM(grand_total_eur)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
                "team_ownership": "Payment Platform Squad",
            },
            "6_PaymentApprovalRate": {
                "numerator": "SUM(is_payment_approved)",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Payment Platform Squad",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "PaymentMethod": "payment_method_reporting",
            "PaymentProvider": "first_provider_reporting",
            "CustomerQuality": "customer_quality",
        },
        "dimension_mapping": {
            "_Overall": [
                "1_FirstRunAR",
                "2_PreDunningAR",
                "3_PostDunningAR", 
                "4_DunningCancellations",
                "5_RevenueDunningCancellations",
                "6_PaymentApprovalRate",
            ],
            "PaymentMethod": [
                "2_PreDunningAR",
                "3_PostDunningAR",
                "6_PaymentApprovalRate",
            ],
            "PaymentProvider": [
                "2_PreDunningAR",
                "3_PostDunningAR",
                "6_PaymentApprovalRate",
            ],
            "CustomerQuality": [
                "2_PreDunningAR",
                "3_PostDunningAR",
                "6_PaymentApprovalRate",
            ],            
        },
        "where_filter": """
  WHERE
  1 = 1
  AND product_type = 'mealbox'
  AND segment IS NOT NULL
  AND customer_loyalty IS NOT NULL
  AND customer_loyalty = 0
  AND type_order = 'initial'
    """,
    },    
    "Loyalty-recurring-AR": {
        "focus_group": "3_Active",
        "metric_group": "1_3_Loyalty: LL0 and LL1+ (Recurring charges)",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_box_candidates",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "1_FirstRunAR": {
                "numerator": "SUM(1_FirstRunAR)",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
                "team_ownership": "Payment Platform Squad",
            },
            "2_PreDunningAR": {
                "numerator": "SUM(2_PreDunningAR)",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Payment Platform Squad",
            },
            "3_PostDunningAR": {
                "numerator": "SUM(3_PostDunningAR)",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Payment Platform Squad",
            },
            "4_DunningCancellations": {
                "numerator": """SUM( CASE WHEN dunning_execution = 'cancelled' THEN order_count ELSE 0 END)""",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
                "team_ownership": "Payment Platform Squad",
            }, 
            "5_RevenueDunningCancellations": {
                "numerator": """SUM( CASE WHEN dunning_execution = 'cancelled' THEN grand_total_eur ELSE 0 END)""",
                "denominator": "SUM(grand_total_eur)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
                "team_ownership": "Payment Platform Squad",
            },
            "6_PaymentApprovalRate": {
                "numerator": "SUM(is_payment_approved)",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Payment Platform Squad",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "PaymentMethod": "payment_method_reporting",
            "PaymentProvider": "first_provider_reporting",
            "CustomerQuality": "customer_quality",
        },
        "dimension_mapping": {
            "_Overall": [
                "1_FirstRunAR",
                "2_PreDunningAR",
                "3_PostDunningAR", 
                "4_DunningCancellations",
                "5_RevenueDunningCancellations",
                "6_PaymentApprovalRate",
            ],
            "PaymentMethod": [
                "2_PreDunningAR",
                "3_PostDunningAR",
                "6_PaymentApprovalRate",
            ],
            "PaymentProvider": [
                "2_PreDunningAR",
                "3_PostDunningAR",
                "6_PaymentApprovalRate",
            ],
            "CustomerQuality": [
                "2_PreDunningAR",
                "3_PostDunningAR",
                "6_PaymentApprovalRate",
            ],            
        },
        "where_filter": """
  WHERE
  1 = 1
  AND product_type = 'mealbox'
  AND segment IS NOT NULL
  AND customer_loyalty IS NOT NULL
  AND customer_loyalty >= 0
  AND type_order <> 'initial'
    """,
    },    
    "SameWeekDunningMetrics": {
        "focus_group": "3_Active",
        "metric_group": "2_1_Boxes Shipped",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_dunning",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "0_ShipRate": {
                "numerator": """SUM(CASE WHEN dunning_execution = 'shipped' THEN order_count ELSE 0 END)""",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Payment Platform Squad",
            },            
            "1_RecoveryW0": {
                "numerator": """SUM(CASE WHEN dunning_execution = 'shipped' THEN recovery_w0 ELSE 0 END)""",
                "denominator": "SUM(CASE WHEN dunning_execution = 'shipped' THEN order_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
                "team_ownership": "Payment Platform Squad",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "LoyaltySegment": "loyalty_segment",
            "CustomerQuality": "customer_quality",
        },
        "dimension_mapping": {
            "_Overall": [
                "0_ShipRate",
                "1_RecoveryW0",
            ],
            "LoyaltySegment": [
                "0_ShipRate",
                "1_RecoveryW0",
            ],
            "CustomerQuality": [
                "0_ShipRate",
                "1_RecoveryW0",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
    """,
    },
    "Lag12wkDunningMetrics": {
        "focus_group": "3_Active",
        "metric_group": "2_2_Boxes Shipped - 12wk lag",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_dunning",
        "date_granularity_mapping": {
            "WEEK": "lead_hellofresh_week",
            "MONTH": "lead_hellofresh_year_month",
            "QUARTER": "lead_hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "2_Recovery_12wkCohort": {
                "numerator": """SUM(CASE WHEN dunning_execution = 'shipped' THEN recovery_w12 ELSE 0 END)""",
                "denominator": "SUM(CASE WHEN dunning_execution = 'shipped' THEN order_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
            },
            "3_DunningAvgNetProfit_12wkCohort": {
                "numerator": """SUM(prediction_net_profit)""",
                "denominator": "SUM(prediction_order_count)",
                "metric_type": "dollar-ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
            }, 
            "4_DunningProfitCoverageRate_12wkCohort": {
                "numerator": """SUM(prediction_net_profit)""",
                "denominator": "SUM(prediction_order_count)",
                "numerator_2": """SUM(exploration_net_profit)""",
                "denominator_2": "SUM(exploration_order_count)",
                "metric_type": "ratio-ratio",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
            }, 
            "5_DunningBadDebtRate_12wkCohort": {
                "numerator": """SUM(CASE WHEN dunning_execution = 'shipped' THEN open_debt ELSE 0 END)""",
                "denominator": "SUM(CASE WHEN dunning_execution = 'shipped' THEN grand_total_eur ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "TRUE",
            },  
            "6_DunningNetProfit_12wkCohort": {
                "numerator": """SUM(CASE WHEN dunning_execution = 'shipped' THEN net_profit ELSE 0 END)""",
                "denominator": "AVG(1)",
                "metric_type": "dollar",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            }, 
            "7_DunningBadDebt_12wkCohort": {
                "numerator": """SUM(CASE WHEN dunning_execution = 'shipped' THEN open_debt ELSE 0 END)""",
                "denominator": "AVG(1)",
                "metric_type": "dollar",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },                        
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "LoyaltySegment": "loyalty_segment",
            "CustomerQuality": "customer_quality",
        },
        "dimension_mapping": {
            "_Overall": [
                "2_Recovery_12wkCohort",
                "3_DunningAvgNetProfit_12wkCohort",
                "4_DunningProfitCoverageRate_12wkCohort",
                "5_DunningBadDebtRate_12wkCohort",
                "6_DunningNetProfit_12wkCohort",
                "7_DunningBadDebt_12wkCohort",
            ],
            "LoyaltySegment": [
                "2_Recovery_12wkCohort",
                "3_DunningAvgNetProfit_12wkCohort",
                "4_DunningProfitCoverageRate_12wkCohort",
                "5_DunningBadDebtRate_12wkCohort",
                "6_DunningNetProfit_12wkCohort",
                "7_DunningBadDebt_12wkCohort",
            ],
            "CustomerQuality": [
                "2_Recovery_12wkCohort",
                "3_DunningAvgNetProfit_12wkCohort",
                "4_DunningProfitCoverageRate_12wkCohort",
                "5_DunningBadDebtRate_12wkCohort",
                "6_DunningNetProfit_12wkCohort",
                "7_DunningBadDebt_12wkCohort",
            ],

        },
        "where_filter": """
  WHERE
  1 = 1
    """,
    },
    "Lag12wkDunningMetricsv2": {
        "focus_group": "3_Active",
        "metric_group": "2_2_Boxes Shipped - 12wk lag",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_box_candidates",
        "date_granularity_mapping": {
            "WEEK": "lead_hellofresh_week",
            "MONTH": "lead_hellofresh_year_month",
            "QUARTER": "lead_hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "6_TotalBadDebtRate_12wkCohort": {
                "numerator": """
                SUM(
                    CASE
                        WHEN (dunning_execution = 'shipped' AND box_shipped = 1) AND (recovered_in_days > 84 OR recovered_in_days IS NULL) THEN grand_total_eur
                        ELSE 0
                    END 
                )
                """,
                "denominator": "SUM(CASE WHEN box_shipped = 1 THEN grand_total_eur ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "TRUE",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "CustomerQuality": "customer_quality",
        },
        "dimension_mapping": {
            "_Overall": [
                "6_TotalBadDebtRate_12wkCohort",
            ],
            "CustomerQuality": [
                "6_TotalBadDebtRate_12wkCohort",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
    """,
    },        
    "TokenisationOrVerification": {
        "focus_group": "4_PSPPerformance",
        "metric_group": "1_Tokenisation Or Verification",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_psp_performance",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "1_TotalTransactions": {
                "numerator": """SUM(CASE WHEN request_type = 'TokenisationOrVerification' THEN count_attempt ELSE 0 END)""",
                "denominator": "AVG(1)",
                "metric_type": "number",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },
            "2_TransactionSuccessRate": {
                "numerator": """SUM(CASE WHEN request_type = 'TokenisationOrVerification' THEN count_success ELSE 0 END)""",
                "denominator": "SUM(CASE WHEN request_type = 'TokenisationOrVerification' THEN count_attempt ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "PaymentProvider": "provider",
        },
        "dimension_mapping": {
            "_Overall": [
                "1_TotalTransactions",
                "2_TransactionSuccessRate",
            ],
            "PaymentProvider": [
                "1_TotalTransactions",
                "2_TransactionSuccessRate",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
  AND provider IS NOT NULL
  AND provider <> ''
    """,
    },
    "Charge": {
        "focus_group": "4_PSPPerformance",
        "metric_group": "2_Charge",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_psp_performance",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "1_TotalTransactions": {
                "numerator": """SUM(CASE WHEN request_type = 'Charge' THEN count_attempt ELSE 0 END)""",
                "denominator": "AVG(1)",
                "metric_type": "number",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },
            "2_TransactionSuccessRate": {
                "numerator": """SUM(CASE WHEN request_type = 'Charge' THEN count_success ELSE 0 END)""",
                "denominator": "SUM(CASE WHEN request_type = 'Charge' THEN count_attempt ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },
            "3_TransactionRefunds": {
                "numerator": """SUM(CASE WHEN request_type = 'Charge' AND is_refund = 1 THEN count_attempt ELSE 0 END)""",
                "denominator": "SUM(CASE WHEN request_type = 'Charge' THEN count_success ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "PaymentProvider": "provider",
        },
        "dimension_mapping": {
            "_Overall": [
                "1_TotalTransactions",
                "2_TransactionSuccessRate",
                "3_TransactionRefunds",
            ],
            "PaymentProvider": [
                "1_TotalTransactions",
                "2_TransactionSuccessRate",
                "3_TransactionRefunds",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
  AND provider IS NOT NULL
  AND provider <> ''
    """,
    },
    "Lag26wkChargeBackMetrics": {
        "focus_group": "5_Payment Fraud",
        "metric_group": "2_Chargeback (13wks Lag)",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_chargeback",
        "date_granularity_mapping": {
            "WEEK": "lead_hellofresh_week",
            "MONTH": "lead_hellofresh_year_month",
            "QUARTER": "lead_hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "1_ChargeBackRate": {
                "numerator": """SUM(CASE WHEN is_fraud IS NOT NULL THEN count_orders ELSE 0 END)""",
                "denominator": "SUM(count_orders)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "TRUE",
                "team_ownership": "Risk & Fraud Management Squad",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "PaymentMethod": "payment_method_reporting",
        },
        "dimension_mapping": {
            "_Overall": [
                "1_ChargeBackRate",
            ],
            "PaymentMethod": [
                "1_ChargeBackRate",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
    """,
    },        
    "CashCredits": {
        "focus_group": "6_Cash Credits",
        "metric_group": "1_Total Amount of Cash Credits",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_cash_credits",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "1_CashCreditAddedEuro": {
                "numerator": """SUM(CASE WHEN CashCreditType = 'CashCreditAdded' THEN ValueEuro ELSE 0 END)""",
                "denominator": "AVG(1)",
                "metric_type": "dollar",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },
            "2_CashCreditSpentEuro": {
                "numerator": """SUM(CASE WHEN CashCreditType = 'CashCreditSpent' THEN ValueEuro ELSE 0 END)""",
                "denominator": "AVG(1)",
                "metric_type": "dollar",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },

        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
        },
        "dimension_mapping": {
            "_Overall": [
                "1_CashCreditAddedEuro",
                "2_CashCreditSpentEuro",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
    """,
    },            
    "TopUpFinance": {
        "focus_group": "6_Cash Credits",
        "metric_group": "2_Top-Ups",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_top_up_financials",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "1_CashCreditsAddedThroughTopUps": {
                "numerator": """SUM(CASE WHEN type = 'CREDIT' THEN credit_sum_eur ELSE 0 END)""",
                "denominator": "AVG(1)",
                "metric_type": "dollar",
                "more_is_good": "TRUE",
                "is_p0": "TRUE",
            },
            "2_TopUpsDiscount": {
                "numerator": """SUM(CASE WHEN type = 'CREDIT' AND credit_type = 'bonus' THEN credit_sum_eur ELSE 0 END)""",
                "denominator": "AVG(1)",
                "metric_type": "dollar",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },
            "5_TopUpsDiscountROI(Profit)": {
                "numerator": """(SUM(profit_eur) 
                - SUM(CASE WHEN type = 'DEBIT' AND credit_type = 'bonus' THEN credit_sum_eur ELSE 0 END))""",
                "denominator": "SUM(CASE WHEN type = 'DEBIT' AND credit_type = 'bonus' THEN credit_sum_eur ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },            
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "LoyaltyLevel": "loyalty_level",
        },
        "dimension_mapping": {
            "_Overall": [
                "1_CashCreditsAddedThroughTopUps",
                "2_TopUpsDiscount",
                "5_TopUpsDiscountROI(Profit)",
            ],
            "LoyaltyLevel": [
                "1_CashCreditsAddedThroughTopUps",
                "2_TopUpsDiscount",
                "5_TopUpsDiscountROI(Profit)",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
    """,
    },
    "TopUpActives": {
        "focus_group": "6_Cash Credits",
        "metric_group": "2_Top-Ups",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_top_up_actives",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "3_TopUpsActiveCustomers": {
                "numerator": """COUNT(DISTINCT customer_uuid)""",
                "denominator": "AVG(1)",
                "metric_type": "number",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
        },
        "dimension_mapping": {
            "_Overall": [
                "3_TopUpsActiveCustomers",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
    """,
    },
    "TopUpFunnel": {
        "focus_group": "6_Cash Credits",
        "metric_group": "2_Top-Ups",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_top_up_funnel",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "4_ConversionRate": {
                "numerator": """SUM(CASE WHEN event_type = 'success' THEN user_count ELSE 0 END)""",
                "denominator": "SUM(CASE WHEN event_type = 'banner_display' THEN user_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "LoyaltyLevel": "loyalty_level",
        },
        "dimension_mapping": {
            "_Overall": [
                "4_ConversionRate",
            ],
            "LoyaltyLevel": [
                "4_ConversionRate",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
  AND experiment_version = 'V2'
    """,
    },
    "TopUpRetention": {
        "focus_group": "6_Cash Credits",
        "metric_group": "2_Top-Ups",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_top_up_orders",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "6_TopUpOrderTakeRate": {
                "numerator": """SUM(topup_order_count)""",
                "denominator": "SUM(order_count)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "LoyaltyLevel": "loyalty_level",
        },
        "dimension_mapping": {
            "_Overall": [
                "6_TopUpOrderTakeRate",
            ],
            "LoyaltyLevel": [
                "6_TopUpOrderTakeRate",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
    """,
    },
    "PaymentCosts": {
        "focus_group": "7_Payment Costs",
        "metric_group": "1_PC2",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_payment_cost",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "1_GrossRevenue": {
                "numerator": """SUM(gross_revenue_euro)""",
                "denominator": "AVG(1)",
                "metric_type": "dollar",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },
            "2_PaymentProcessingFees": {
                "numerator": """SUM(payment_cost_euro)""",
                "denominator": "AVG(1)",
                "metric_type": "dollar",
                "more_is_good": "FALSE",
                "is_p0": "FALSE",
            },
            "3_PaymentProcessingFees%": {
                "numerator": """SUM(payment_cost_euro)""",
                "denominator": "SUM(gross_revenue_euro)",
                "metric_type": "ratio",
                "more_is_good": "FALSE",
                "is_p0": "TRUE",
            },
            "4_CostPerOrder": {
                "numerator": """SUM(payment_cost_euro)""",
                "denominator": "SUM(delivered_orders)",
                "metric_type": "small-dollar",
                "more_is_good": "FALSE",
                "is_p0": "TRUE",
            },

        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
        },
        "dimension_mapping": {
            "_Overall": [
                "1_GrossRevenue",
                "2_PaymentProcessingFees",
                "3_PaymentProcessingFees%",
                "4_CostPerOrder",
            ],
        },
        "where_filter": """
  WHERE
  1 = 1
    """,
    },                           
    "Checkout Funnel Simplified": {
        "focus_group": "8_Appendix",
        "metric_group": "1_Checkout Funnel Simplified",
        "database_name": "payments_hf",
        "table_name": "payments_p0_metrics_checkout_funnel",
        "date_granularity_mapping": {
            "WEEK": "hellofresh_week",
            "MONTH": "hellofresh_year_month",
            "QUARTER": "hellofresh_year_quarter",
        },
        "country": "country",
        "metric_list": {
            "1_PaymentPageVisit": {
                "numerator": "SUM(CASE WHEN is_pay_visit = 1 THEN customer_count ELSE 0 END)",
                "denominator": "AVG(1)",
                "metric_type": "number",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },
            "2_1_PaymentSelected": {
                "numerator": "SUM(CASE WHEN is_select = 1 THEN customer_count ELSE 0 END)",
                "denominator": "AVG(1)",
                "metric_type": "number",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },  
            "2_2_PaymentVistToSelect": {
                "numerator": "SUM(CASE WHEN is_select = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_pay_visit = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },              
            "3_1_PaymentClicked": {
                "numerator": "SUM(CASE WHEN is_click = 1 THEN customer_count ELSE 0 END)",
                "denominator": "AVG(1)",
                "metric_type": "number",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },     
            "3_2_PaymentSelectToClick": {
                "numerator": "SUM(CASE WHEN is_click = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_select = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },              
            "4_1_PaymentFSCheckSubmitted": {
                "numerator": "SUM(CASE WHEN is_click = 1 AND is_fs_check = 1 THEN customer_count ELSE 0 END)",
                "denominator": "AVG(1)",
                "metric_type": "number",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            }, 
            "4_2_PaymentClickToFS": {
                "numerator": "SUM(CASE WHEN is_click = 1 AND is_fs_check = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_click = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },             
            "4_3_PaymentFSCheckSubmitted(NoGAFilter)": {
                "numerator": "SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END)",
                "denominator": "AVG(1)",
                "metric_type": "number",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },                           
            "5_1_PaymentVerified": {
                "numerator": "SUM(CASE WHEN is_click = 1 AND is_fs_check = 1 AND is_pvs = 1 THEN customer_count ELSE 0 END)",
                "denominator": "AVG(1)",
                "metric_type": "number",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },  
            "5_2_PaymentFSToVerified": {
                "numerator": "SUM(CASE WHEN is_click = 1 AND is_fs_check = 1 AND is_pvs = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_click = 1 AND is_fs_check = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },      
            "5_3_PaymentVerified(NoGAFilter)": {
                "numerator": "SUM(CASE WHEN is_pvs = 1 THEN customer_count ELSE 0 END)",
                "denominator": "AVG(1)",
                "metric_type": "number",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },                                
            "6_1_PaymentSuccess": {
                "numerator": "SUM(CASE WHEN is_success = 1 THEN customer_count ELSE 0 END)",
                "denominator": "AVG(1)",
                "metric_type": "number",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            }, 
            "6_2_PaymentVerifiedToSuccess": {
                "numerator": "SUM(CASE WHEN is_success = 1 THEN customer_count ELSE 0 END)",
                "denominator": "SUM(CASE WHEN is_click = 1 AND is_fs_check = 1 AND is_pvs = 1 THEN customer_count ELSE 0 END)",
                "metric_type": "ratio",
                "more_is_good": "TRUE",
                "is_p0": "FALSE",
            },               
        },
        "dimension_value_mapping": {
            "_Overall": "NULL",
            "PaymentMethod": "payment_method_reporting",
        },
        "dimension_mapping": {
            "_Overall": [
                "1_PaymentPageVisit",
                "2_1_PaymentSelected",
                "2_2_PaymentVistToSelect",
                "3_1_PaymentClicked",
                "3_2_PaymentSelectToClick",
                "4_1_PaymentFSCheckSubmitted",
                "4_2_PaymentClickToFS",
                "4_3_PaymentFSCheckSubmitted(NoGAFilter)",
                "5_1_PaymentVerified",
                "5_2_PaymentFSToVerified",
                "5_3_PaymentVerified(NoGAFilter)",
                "6_1_PaymentSuccess",
                "6_2_PaymentVerifiedToSuccess",                
            ],
            "PaymentMethod": [
                "2_1_PaymentSelected",
                "3_1_PaymentClicked",
                "3_2_PaymentSelectToClick",
                "4_1_PaymentFSCheckSubmitted",
                "4_2_PaymentClickToFS",
                "4_3_PaymentFSCheckSubmitted(NoGAFilter)",
                "5_1_PaymentVerified",
                "5_2_PaymentFSToVerified",
                "5_3_PaymentVerified(NoGAFilter)",
                "6_1_PaymentSuccess",
                "6_2_PaymentVerifiedToSuccess",            ],
        },
        "where_filter": """
  WHERE
  1 = 1
  AND is_different_checkout = FALSE
    """,
    },
}

# COMMAND ----------

template = """
SELECT
'{}' AS focus_group
, '{}' AS metric_group
, '{}' AS date_granularity
, {} AS date_value
, b.reporting_cluster
, CASE WHEN b.reporting_cluster = 'Overall' THEN b.business_unit ELSE 'Null' END AS business_unit
, b.country_cluster
, '{}' AS metric_name
, '{}' AS dimension_name
, STRING({}) AS dimension_value
, '{}' AS metric_type
, '{}' AS flag_more_is_good
, '{}' AS flag_is_p0
, '{}' AS team_ownership
, {} AS metric_value_numerator
, {} AS metric_value_denominator
, {} AS metric_value_numerator_2
, {} AS metric_value_denominator_2
FROM {}.{} AS a
JOIN (
  SELECT
  business_unit
  , explode(reporting_cluster_array) AS reporting_cluster
  , 'Null' AS country_cluster

  FROM payments_hf.business_units

  UNION ALL

  SELECT
  business_unit
  , 'Overall' AS reporting_cluster
  , CASE 
    WHEN brand_code IN ('F75', 'YF') THEN 'RTE'
    WHEN brand NOT IN ('hellofresh') THEN 'WL'
    WHEN business_unit IN ('AU', 'NZ') THEN 'AUNZ'
    WHEN business_unit IN ('BE', 'NL', 'LU', 'FR') THEN 'BENELUXFR'
    WHEN business_unit IN ('DE', 'AT', 'CH') THEN 'DACH'
    WHEN business_unit IN ('NO', 'SE', 'DK') THEN 'NORDICS'
    WHEN business_unit IN ('ES', 'IT') THEN 'SOUTH EU'
    ELSE business_unit
    END AS country_cluster

  FROM payments_hf.business_units
  ) AS b
ON a.{} = b.business_unit
{}
GROUP BY ALL

"""

count_ = 1
final_sql_script = ""

for x in metric_schema.values():
  if x['focus_group'] in ["1_Activation (Paid + Referrals)", "2_Reactivations"]:
    for date_granularity, date_granularity_value in x['date_granularity_mapping'].items():
      for dimension_name, dimension_value in x['dimension_value_mapping'].items():
        for metric_name, metric_script in x['metric_list'].items():
          if metric_name in x['dimension_mapping'][dimension_name]:
            if metric_script['metric_type'] == 'ratio-ratio':
              sql_script = template.format(x['focus_group'],
                                        x['metric_group'],
                                        date_granularity,
                                        date_granularity_value,
                                        metric_name,
                                        dimension_name,
                                        dimension_value,
                                        metric_script['metric_type'],
                                        metric_script['more_is_good'],
                                        metric_script['is_p0'],
                                        metric_script.get('team_ownership', 'NULL'),
                                        metric_script['numerator'],
                                        metric_script['denominator'],
                                        metric_script['numerator_2'],
                                        metric_script['denominator_2'],
                                        x['database_name'],
                                        x['table_name'],
                                        x['country'],
                                        x['where_filter'])
            else:
                sql_script = template.format(x['focus_group'],
                                            x['metric_group'],
                                            date_granularity,
                                            date_granularity_value,
                                            metric_name,
                                            dimension_name,
                                            dimension_value,
                                            metric_script['metric_type'],
                                            metric_script['more_is_good'],
                                            metric_script['is_p0'],
                                            metric_script.get('team_ownership', 'NULL'),
                                            metric_script['numerator'],
                                            metric_script['denominator'],
                                            'NULL',
                                            'NULL',
                                            x['database_name'],
                                            x['table_name'],
                                            x['country'],
                                            x['where_filter'])
            if count_ == 1:
              final_sql_script = sql_script
              count_ += 1
            else:
              final_sql_script = final_sql_script + "UNION ALL" + sql_script

# print(final_sql_script)

final_sql_script_with_flags = """
WITH date_lkup AS (
  SELECT
  'WEEK' AS date_granularity
    , hellofresh_week AS date_value
    , dd.hellofresh_year AS date_year
    , INT(SPLIT(dd.hellofresh_week, '-W')[1]) AS date_granularity_num
  FROM dimensions.date_dimension dd
  WHERE
    hellofresh_week >= '2021-W01'
    AND DATE(date_string_backwards) < CURRENT_DATE()
  GROUP BY ALL

  UNION ALL

  SELECT
  'MONTH' AS date_granularity
    , CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS date_value
    , dd.hellofresh_year AS date_year
    , INT(dd.hellofresh_month) AS date_granularity_num
  FROM dimensions.date_dimension dd
  WHERE
    hellofresh_week >= '2021-W01'
    AND DATE(date_string_backwards) < CURRENT_DATE()    
  GROUP BY ALL

  UNION ALL

  SELECT
  'QUARTER' AS date_granularity
    , CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS date_value
    , dd.hellofresh_year AS date_year
    , INT(SPLIT(dd.hellofresh_quarter, 'Q')[1]) AS date_granularity_num
  FROM dimensions.date_dimension dd
  WHERE
    hellofresh_week >= '2021-W01'
    AND DATE(date_string_backwards) < CURRENT_DATE()    
  GROUP BY ALL
  )
   , date_lkup_row AS (
  SELECT
  date_granularity
    , date_value
    , date_year
    , date_granularity_num
    , ROW_NUMBER() OVER (PARTITION BY date_granularity ORDER BY date_year, date_granularity_num ) AS date_value_row_num

  FROM date_lkup
  )
   , final_date_lkup AS (
  -- ignoring the W53 performance
  SELECT
  a.date_granularity
    , a.date_value
    , a.date_year
    , a.date_granularity_num
    , a.date_value_row_num
    , pdl.date_value AS prev_date_value
    , CASE 
        WHEN a.date_granularity IN ('MONTH', 'QUARTER') THEN pdl.date_value
        WHEN a.date_granularity IN ('WEEK') THEN pdl2.date_value
      END AS prev_date_value_v2
    , pydl.date_value AS prev_year_date_value
  FROM date_lkup_row AS a
  LEFT JOIN date_lkup_row AS pdl
       ON a.date_granularity = pdl.date_granularity
       AND a.date_value_row_num = pdl.date_value_row_num + 1

  LEFT JOIN date_lkup_row AS pdl2
       ON a.date_granularity = pdl2.date_granularity
       AND a.date_value_row_num = pdl2.date_value_row_num + 4

  JOIN date_lkup_row AS pydl
       ON a.date_granularity = pydl.date_granularity
       AND a.date_granularity_num = pydl.date_granularity_num
       AND a.date_year = pydl.date_year + 1
  )
  , union_all_statement AS (
  {}
)
, union_all_data AS (
SELECT
a.focus_group
, a.metric_group
, a.date_granularity
, b.date_year
, a.date_value
, b.date_value_row_num
, a.reporting_cluster
, a.business_unit
, a.country_cluster
, a.metric_name
, a.dimension_name
, a.dimension_value
, a.metric_type
, a.flag_more_is_good
, a.flag_is_p0
, a.team_ownership
, a.metric_value_numerator
, a.metric_value_denominator
, a.metric_value_numerator_2
, a.metric_value_denominator_2
, 'Current' AS data_selection
FROM union_all_statement AS a
JOIN final_date_lkup AS b
ON a.date_granularity = b.date_granularity
AND a.date_value = b.date_value

UNION ALL

SELECT
a.focus_group
, a.metric_group
, a.date_granularity
, b.date_year
, b.date_value
, b.date_value_row_num
, a.reporting_cluster
, a.business_unit
, a.country_cluster
, a.metric_name
, a.dimension_name
, a.dimension_value
, a.metric_type
, a.flag_more_is_good
, a.flag_is_p0
, a.team_ownership
, a.metric_value_numerator
, a.metric_value_denominator
, a.metric_value_numerator_2
, a.metric_value_denominator_2
, 'PrevDateValue' AS data_selection
FROM union_all_statement AS a
JOIN final_date_lkup AS b
ON a.date_granularity = b.date_granularity
AND a.date_value = b.prev_date_value

UNION ALL

SELECT
a.focus_group
, a.metric_group
, a.date_granularity
, b.date_year
, b.date_value
, b.date_value_row_num
, a.reporting_cluster
, a.business_unit
, a.country_cluster
, a.metric_name
, a.dimension_name
, a.dimension_value
, a.metric_type
, a.flag_more_is_good
, a.flag_is_p0
, a.team_ownership
, a.metric_value_numerator
, a.metric_value_denominator
, a.metric_value_numerator_2
, a.metric_value_denominator_2
, 'PrevDateValueV2' AS data_selection
FROM union_all_statement AS a
JOIN final_date_lkup AS b
ON a.date_granularity = b.date_granularity
AND a.date_value = b.prev_date_value_v2

UNION ALL

SELECT
a.focus_group
, a.metric_group
, a.date_granularity
, b.date_year
, b.date_value
, b.date_value_row_num
, a.reporting_cluster
, a.business_unit
, a.country_cluster
, a.metric_name
, a.dimension_name
, a.dimension_value
, a.metric_type
, a.flag_more_is_good
, a.flag_is_p0
, a.team_ownership
, a.metric_value_numerator
, a.metric_value_denominator
, a.metric_value_numerator_2
, a.metric_value_denominator_2
, 'PrevYearDateValue' AS data_selection
FROM union_all_statement AS a
JOIN final_date_lkup AS b
ON a.date_granularity = b.date_granularity
AND a.date_value = b.prev_year_date_value
)
SELECT
date_granularity
, date_year
, date_value
, date_value_row_num AS date_value_order
, reporting_cluster
, business_unit
, country_cluster
, focus_group
, metric_group
, metric_name
, INT(SPLIT(metric_name, '_')[0]) AS metric_name_order
, dimension_name
, dimension_value
, metric_type
, flag_more_is_good
, flag_is_p0
, team_ownership
, SUM(CASE WHEN data_selection = 'Current' THEN metric_value_numerator ELSE 0 END) AS current_metric_value_numerator
, SUM(CASE WHEN data_selection = 'Current' THEN metric_value_denominator ELSE 0 END) AS current_metric_value_denominator
, SUM(CASE WHEN data_selection = 'Current' THEN metric_value_numerator_2 ELSE 0 END) AS current_metric_value_numerator_2
, SUM(CASE WHEN data_selection = 'Current' THEN metric_value_denominator_2 ELSE 0 END) AS current_metric_value_denominator_2
, SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_numerator ELSE 0 END) AS prev_metric_value_numerator
, SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_denominator ELSE 0 END) AS prev_metric_value_denominator
, SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_numerator_2 ELSE 0 END) AS prev_metric_value_numerator_2
, SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_denominator_2 ELSE 0 END) AS prev_metric_value_denominator_2
, SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_numerator ELSE 0 END) AS prev_yr_metric_value_numerator
, SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_denominator ELSE 0 END) AS prev_yr_metric_value_denominator
, SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_numerator_2 ELSE 0 END) AS prev_yr_metric_value_numerator_2
, SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_denominator_2 ELSE 0 END) AS prev_yr_metric_value_denominator_2
, SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_numerator ELSE 0 END) AS prev_v2_metric_value_numerator
, SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_denominator ELSE 0 END) AS prev_v2_metric_value_denominator
, SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_numerator_2 ELSE 0 END) AS prev_v2_metric_value_numerator_2
, SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_denominator_2 ELSE 0 END) AS prev_v2_metric_value_denominator_2
, CURRENT_TIMESTAMP AS last_update_ts
FROM union_all_data
WHERE date_year >= (EXTRACT(YEAR FROM CURRENT_DATE()) - 1)
GROUP BY ALL

"""

refresh_table_template = "REFRESH TABLE {}.{};"

for x in metric_schema.values():
  spark.sql(refresh_table_template.format(x['database_name'], x['table_name']))

spark.sql("REFRESH TABLE payments_hf.business_units;")

df = spark.sql(final_sql_script_with_flags.format(final_sql_script))

save_path = (f's3://hf-payments-data-lake-live-main/payments_hf/payments_p0_metrics_part_1')

database = "payments_hf"
table_name = "payments_p0_metrics_part_1"
# write table
(
    df.write.format("delta")
    .mode("overwrite")
    .option("path", save_path)
    .option("overwriteSchema", "true")
    .option("spark.databricks.delta.autoCompact.enabled", "true")
    .option("spark.databricks.delta.optimizeWrite.enabled", "true")
    .option("spark.databricks.delta.vacuum.parallelDelete.enabled", "true")
    .saveAsTable(f"{database}.{table_name}")
)

# COMMAND ----------

template = """
SELECT
'{}' AS focus_group
, '{}' AS metric_group
, '{}' AS date_granularity
, {} AS date_value
, b.reporting_cluster
, CASE WHEN b.reporting_cluster = 'Overall' THEN b.business_unit ELSE 'Null' END AS business_unit
, b.country_cluster
, '{}' AS metric_name
, '{}' AS dimension_name
, STRING({}) AS dimension_value
, '{}' AS metric_type
, '{}' AS flag_more_is_good
, '{}' AS flag_is_p0
, '{}' AS team_ownership
, {} AS metric_value_numerator
, {} AS metric_value_denominator
, {} AS metric_value_numerator_2
, {} AS metric_value_denominator_2
FROM {}.{} AS a
JOIN (
  SELECT
  business_unit
  , explode(reporting_cluster_array) AS reporting_cluster
  , 'Null' AS country_cluster

  FROM payments_hf.business_units

  UNION ALL

  SELECT
  business_unit
  , 'Overall' AS reporting_cluster
  , CASE 
    WHEN brand_code IN ('F75', 'YF') THEN 'RTE'
    WHEN brand NOT IN ('hellofresh') THEN 'WL'
    WHEN business_unit IN ('AU', 'NZ') THEN 'AUNZ'
    WHEN business_unit IN ('BE', 'NL', 'LU', 'FR') THEN 'BENELUXFR'
    WHEN business_unit IN ('DE', 'AT', 'CH') THEN 'DACH'
    WHEN business_unit IN ('NO', 'SE', 'DK') THEN 'NORDICS'
    WHEN business_unit IN ('ES', 'IT') THEN 'SOUTH EU'
    ELSE business_unit
    END AS country_cluster

  FROM payments_hf.business_units
  ) AS b
ON a.{} = b.business_unit
{}
GROUP BY ALL

"""

count_ = 1
final_sql_script = ""

for x in metric_schema.values():
  if x['focus_group'] == "3_Active":
    for date_granularity, date_granularity_value in x['date_granularity_mapping'].items():
      for dimension_name, dimension_value in x['dimension_value_mapping'].items():
        for metric_name, metric_script in x['metric_list'].items():
          if metric_name in x['dimension_mapping'][dimension_name]:
            if metric_script['metric_type'] == 'ratio-ratio':
              sql_script = template.format(x['focus_group'],
                                        x['metric_group'],
                                        date_granularity,
                                        date_granularity_value,
                                        metric_name,
                                        dimension_name,
                                        dimension_value,
                                        metric_script['metric_type'],
                                        metric_script['more_is_good'],
                                        metric_script['is_p0'],
                                        metric_script.get('team_ownership', 'NULL'),
                                        metric_script['numerator'],
                                        metric_script['denominator'],
                                        metric_script['numerator_2'],
                                        metric_script['denominator_2'],
                                        x['database_name'],
                                        x['table_name'],
                                        x['country'],
                                        x['where_filter'])
            else:
                sql_script = template.format(x['focus_group'],
                                            x['metric_group'],
                                            date_granularity,
                                            date_granularity_value,
                                            metric_name,
                                            dimension_name,
                                            dimension_value,
                                            metric_script['metric_type'],
                                            metric_script['more_is_good'],
                                            metric_script['is_p0'],
                                            metric_script.get('team_ownership', 'NULL'),
                                            metric_script['numerator'],
                                            metric_script['denominator'],
                                            'NULL',
                                            'NULL',
                                            x['database_name'],
                                            x['table_name'],
                                            x['country'],
                                            x['where_filter'])
            if count_ == 1:
              final_sql_script = sql_script
              count_ += 1
            else:
              final_sql_script = final_sql_script + "UNION ALL" + sql_script

# print(final_sql_script)

final_sql_script_with_flags = """
WITH date_lkup AS (
  SELECT
  'WEEK' AS date_granularity
    , hellofresh_week AS date_value
    , dd.hellofresh_year AS date_year
    , INT(SPLIT(dd.hellofresh_week, '-W')[1]) AS date_granularity_num
  FROM dimensions.date_dimension dd
  WHERE
    hellofresh_week >= '2021-W01'
    AND DATE(date_string_backwards) < CURRENT_DATE()
  GROUP BY ALL

  UNION ALL

  SELECT
  'MONTH' AS date_granularity
    , CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS date_value
    , dd.hellofresh_year AS date_year
    , INT(dd.hellofresh_month) AS date_granularity_num
  FROM dimensions.date_dimension dd
  WHERE
    hellofresh_week >= '2021-W01'
    AND DATE(date_string_backwards) < CURRENT_DATE()    
  GROUP BY ALL

  UNION ALL

  SELECT
  'QUARTER' AS date_granularity
    , CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS date_value
    , dd.hellofresh_year AS date_year
    , INT(SPLIT(dd.hellofresh_quarter, 'Q')[1]) AS date_granularity_num
  FROM dimensions.date_dimension dd
  WHERE
    hellofresh_week >= '2021-W01'
    AND DATE(date_string_backwards) < CURRENT_DATE()    
  GROUP BY ALL
  )
   , date_lkup_row AS (
  SELECT
  date_granularity
    , date_value
    , date_year
    , date_granularity_num
    , ROW_NUMBER() OVER (PARTITION BY date_granularity ORDER BY date_year, date_granularity_num ) AS date_value_row_num

  FROM date_lkup
  )
   , final_date_lkup AS (
  -- ignoring the W53 performance
  SELECT
  a.date_granularity
    , a.date_value
    , a.date_year
    , a.date_granularity_num
    , a.date_value_row_num
    , pdl.date_value AS prev_date_value
    , CASE 
        WHEN a.date_granularity IN ('MONTH', 'QUARTER') THEN pdl.date_value
        WHEN a.date_granularity IN ('WEEK') THEN pdl2.date_value
      END AS prev_date_value_v2
    , pydl.date_value AS prev_year_date_value
  FROM date_lkup_row AS a
  LEFT JOIN date_lkup_row AS pdl
       ON a.date_granularity = pdl.date_granularity
       AND a.date_value_row_num = pdl.date_value_row_num + 1

  LEFT JOIN date_lkup_row AS pdl2
       ON a.date_granularity = pdl2.date_granularity
       AND a.date_value_row_num = pdl2.date_value_row_num + 4

  JOIN date_lkup_row AS pydl
       ON a.date_granularity = pydl.date_granularity
       AND a.date_granularity_num = pydl.date_granularity_num
       AND a.date_year = pydl.date_year + 1
  )
  , union_all_statement AS (
  {}
)
, union_all_data AS (
SELECT
a.focus_group
, a.metric_group
, a.date_granularity
, b.date_year
, a.date_value
, b.date_value_row_num
, a.reporting_cluster
, a.business_unit
, a.country_cluster
, a.metric_name
, a.dimension_name
, a.dimension_value
, a.metric_type
, a.flag_more_is_good
, a.flag_is_p0
, a.team_ownership
, a.metric_value_numerator
, a.metric_value_denominator
, a.metric_value_numerator_2
, a.metric_value_denominator_2
, 'Current' AS data_selection
FROM union_all_statement AS a
JOIN final_date_lkup AS b
ON a.date_granularity = b.date_granularity
AND a.date_value = b.date_value

UNION ALL

SELECT
a.focus_group
, a.metric_group
, a.date_granularity
, b.date_year
, b.date_value
, b.date_value_row_num
, a.reporting_cluster
, a.business_unit
, a.country_cluster
, a.metric_name
, a.dimension_name
, a.dimension_value
, a.metric_type
, a.flag_more_is_good
, a.flag_is_p0
, a.team_ownership
, a.metric_value_numerator
, a.metric_value_denominator
, a.metric_value_numerator_2
, a.metric_value_denominator_2
, 'PrevDateValue' AS data_selection
FROM union_all_statement AS a
JOIN final_date_lkup AS b
ON a.date_granularity = b.date_granularity
AND a.date_value = b.prev_date_value

UNION ALL

SELECT
a.focus_group
, a.metric_group
, a.date_granularity
, b.date_year
, b.date_value
, b.date_value_row_num
, a.reporting_cluster
, a.business_unit
, a.country_cluster
, a.metric_name
, a.dimension_name
, a.dimension_value
, a.metric_type
, a.flag_more_is_good
, a.flag_is_p0
, a.team_ownership
, a.metric_value_numerator
, a.metric_value_denominator
, a.metric_value_numerator_2
, a.metric_value_denominator_2
, 'PrevDateValueV2' AS data_selection
FROM union_all_statement AS a
JOIN final_date_lkup AS b
ON a.date_granularity = b.date_granularity
AND a.date_value = b.prev_date_value_v2

UNION ALL

SELECT
a.focus_group
, a.metric_group
, a.date_granularity
, b.date_year
, b.date_value
, b.date_value_row_num
, a.reporting_cluster
, a.business_unit
, a.country_cluster
, a.metric_name
, a.dimension_name
, a.dimension_value
, a.metric_type
, a.flag_more_is_good
, a.flag_is_p0
, a.team_ownership
, a.metric_value_numerator
, a.metric_value_denominator
, a.metric_value_numerator_2
, a.metric_value_denominator_2
, 'PrevYearDateValue' AS data_selection
FROM union_all_statement AS a
JOIN final_date_lkup AS b
ON a.date_granularity = b.date_granularity
AND a.date_value = b.prev_year_date_value
)
SELECT
date_granularity
, date_year
, date_value
, date_value_row_num AS date_value_order
, reporting_cluster
, business_unit
, country_cluster
, focus_group
, metric_group
, metric_name
, INT(SPLIT(metric_name, '_')[0]) AS metric_name_order
, dimension_name
, dimension_value
, metric_type
, flag_more_is_good
, flag_is_p0
, team_ownership
, SUM(CASE WHEN data_selection = 'Current' THEN metric_value_numerator ELSE 0 END) AS current_metric_value_numerator
, SUM(CASE WHEN data_selection = 'Current' THEN metric_value_denominator ELSE 0 END) AS current_metric_value_denominator
, SUM(CASE WHEN data_selection = 'Current' THEN metric_value_numerator_2 ELSE 0 END) AS current_metric_value_numerator_2
, SUM(CASE WHEN data_selection = 'Current' THEN metric_value_denominator_2 ELSE 0 END) AS current_metric_value_denominator_2
, SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_numerator ELSE 0 END) AS prev_metric_value_numerator
, SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_denominator ELSE 0 END) AS prev_metric_value_denominator
, SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_numerator_2 ELSE 0 END) AS prev_metric_value_numerator_2
, SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_denominator_2 ELSE 0 END) AS prev_metric_value_denominator_2
, SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_numerator ELSE 0 END) AS prev_yr_metric_value_numerator
, SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_denominator ELSE 0 END) AS prev_yr_metric_value_denominator
, SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_numerator_2 ELSE 0 END) AS prev_yr_metric_value_numerator_2
, SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_denominator_2 ELSE 0 END) AS prev_yr_metric_value_denominator_2
, SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_numerator ELSE 0 END) AS prev_v2_metric_value_numerator
, SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_denominator ELSE 0 END) AS prev_v2_metric_value_denominator
, SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_numerator_2 ELSE 0 END) AS prev_v2_metric_value_numerator_2
, SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_denominator_2 ELSE 0 END) AS prev_v2_metric_value_denominator_2
, CURRENT_TIMESTAMP AS last_update_ts
FROM union_all_data
WHERE date_year >= (EXTRACT(YEAR FROM CURRENT_DATE()) - 1)
GROUP BY ALL

"""

refresh_table_template = "REFRESH TABLE {}.{};"

for x in metric_schema.values():
  spark.sql(refresh_table_template.format(x['database_name'], x['table_name']))

spark.sql("REFRESH TABLE payments_hf.business_units;")

df = spark.sql(final_sql_script_with_flags.format(final_sql_script))

save_path = (f's3://hf-payments-data-lake-live-main/payments_hf/payments_p0_metrics_part_2')

database = "payments_hf"
table_name = "payments_p0_metrics_part_2"
# write table
(
    df.write.format("delta")
    .mode("overwrite")
    .option("path", save_path)
    .option("overwriteSchema", "true")
    .option("spark.databricks.delta.autoCompact.enabled", "true")
    .option("spark.databricks.delta.optimizeWrite.enabled", "true")
    .option("spark.databricks.delta.vacuum.parallelDelete.enabled", "true")
    .saveAsTable(f"{database}.{table_name}")
)

# COMMAND ----------

template = """
SELECT
'{}' AS focus_group
, '{}' AS metric_group
, '{}' AS date_granularity
, {} AS date_value
, b.reporting_cluster
, CASE WHEN b.reporting_cluster = 'Overall' THEN b.business_unit ELSE 'Null' END AS business_unit
, b.country_cluster
, '{}' AS metric_name
, '{}' AS dimension_name
, STRING({}) AS dimension_value
, '{}' AS metric_type
, '{}' AS flag_more_is_good
, '{}' AS flag_is_p0
, '{}' AS team_ownership
, {} AS metric_value_numerator
, {} AS metric_value_denominator
, {} AS metric_value_numerator_2
, {} AS metric_value_denominator_2
FROM {}.{} AS a
JOIN (
  SELECT
  business_unit
  , explode(reporting_cluster_array) AS reporting_cluster
  , 'Null' AS country_cluster

  FROM payments_hf.business_units

  UNION ALL

  SELECT
  business_unit
  , 'Overall' AS reporting_cluster
  , CASE 
    WHEN brand_code IN ('F75', 'YF') THEN 'RTE'
    WHEN brand NOT IN ('hellofresh') THEN 'WL'
    WHEN business_unit IN ('AU', 'NZ') THEN 'AUNZ'
    WHEN business_unit IN ('BE', 'NL', 'LU', 'FR') THEN 'BENELUXFR'
    WHEN business_unit IN ('DE', 'AT', 'CH') THEN 'DACH'
    WHEN business_unit IN ('NO', 'SE', 'DK') THEN 'NORDICS'
    WHEN business_unit IN ('ES', 'IT') THEN 'SOUTH EU'
    ELSE business_unit
    END AS country_cluster

  FROM payments_hf.business_units
  ) AS b
ON a.{} = b.business_unit
{}
GROUP BY ALL

"""

count_ = 1
final_sql_script = ""

for x in metric_schema.values():
  if x['focus_group'] in ["4_PSPPerformance", "5_Payment Fraud", "6_Cash Credits", "7_Payment Costs", "8_Appendix"]:
    for date_granularity, date_granularity_value in x['date_granularity_mapping'].items():
      for dimension_name, dimension_value in x['dimension_value_mapping'].items():
        for metric_name, metric_script in x['metric_list'].items():
          if metric_name in x['dimension_mapping'][dimension_name]:
            if metric_script['metric_type'] == 'ratio-ratio':
              sql_script = template.format(x['focus_group'],
                                        x['metric_group'],
                                        date_granularity,
                                        date_granularity_value,
                                        metric_name,
                                        dimension_name,
                                        dimension_value,
                                        metric_script['metric_type'],
                                        metric_script['more_is_good'],
                                        metric_script['is_p0'],
                                        metric_script.get('team_ownership', 'NULL'),
                                        metric_script['numerator'],
                                        metric_script['denominator'],
                                        metric_script['numerator_2'],
                                        metric_script['denominator_2'],
                                        x['database_name'],
                                        x['table_name'],
                                        x['country'],
                                        x['where_filter'])
            else:
                sql_script = template.format(x['focus_group'],
                                            x['metric_group'],
                                            date_granularity,
                                            date_granularity_value,
                                            metric_name,
                                            dimension_name,
                                            dimension_value,
                                            metric_script['metric_type'],
                                            metric_script['more_is_good'],
                                            metric_script['is_p0'],
                                            metric_script.get('team_ownership', 'NULL'),
                                            metric_script['numerator'],
                                            metric_script['denominator'],
                                            'NULL',
                                            'NULL',
                                            x['database_name'],
                                            x['table_name'],
                                            x['country'],
                                            x['where_filter'])
            if count_ == 1:
              final_sql_script = sql_script
              count_ += 1
            else:
              final_sql_script = final_sql_script + "UNION ALL" + sql_script

# print(final_sql_script)

final_sql_script_with_flags = """
WITH date_lkup AS (
  SELECT
  'WEEK' AS date_granularity
    , hellofresh_week AS date_value
    , dd.hellofresh_year AS date_year
    , INT(SPLIT(dd.hellofresh_week, '-W')[1]) AS date_granularity_num
  FROM dimensions.date_dimension dd
  WHERE
    hellofresh_week >= '2021-W01'
    AND DATE(date_string_backwards) < CURRENT_DATE()
  GROUP BY ALL

  UNION ALL

  SELECT
  'MONTH' AS date_granularity
    , CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS date_value
    , dd.hellofresh_year AS date_year
    , INT(dd.hellofresh_month) AS date_granularity_num
  FROM dimensions.date_dimension dd
  WHERE
    hellofresh_week >= '2021-W01'
    AND DATE(date_string_backwards) < CURRENT_DATE()    
  GROUP BY ALL

  UNION ALL

  SELECT
  'QUARTER' AS date_granularity
    , CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS date_value
    , dd.hellofresh_year AS date_year
    , INT(SPLIT(dd.hellofresh_quarter, 'Q')[1]) AS date_granularity_num
  FROM dimensions.date_dimension dd
  WHERE
    hellofresh_week >= '2021-W01'
    AND DATE(date_string_backwards) < CURRENT_DATE()    
  GROUP BY ALL
  )
   , date_lkup_row AS (
  SELECT
  date_granularity
    , date_value
    , date_year
    , date_granularity_num
    , ROW_NUMBER() OVER (PARTITION BY date_granularity ORDER BY date_year, date_granularity_num ) AS date_value_row_num

  FROM date_lkup
  )
   , final_date_lkup AS (
  -- ignoring the W53 performance
  SELECT
  a.date_granularity
    , a.date_value
    , a.date_year
    , a.date_granularity_num
    , a.date_value_row_num
    , pdl.date_value AS prev_date_value
    , CASE 
        WHEN a.date_granularity IN ('MONTH', 'QUARTER') THEN pdl.date_value
        WHEN a.date_granularity IN ('WEEK') THEN pdl2.date_value
      END AS prev_date_value_v2
    , pydl.date_value AS prev_year_date_value
  FROM date_lkup_row AS a
  LEFT JOIN date_lkup_row AS pdl
       ON a.date_granularity = pdl.date_granularity
       AND a.date_value_row_num = pdl.date_value_row_num + 1

  LEFT JOIN date_lkup_row AS pdl2
       ON a.date_granularity = pdl2.date_granularity
       AND a.date_value_row_num = pdl2.date_value_row_num + 4

  JOIN date_lkup_row AS pydl
       ON a.date_granularity = pydl.date_granularity
       AND a.date_granularity_num = pydl.date_granularity_num
       AND a.date_year = pydl.date_year + 1
  )
  , union_all_statement AS (
  {}
)
, union_all_data AS (
SELECT
a.focus_group
, a.metric_group
, a.date_granularity
, b.date_year
, a.date_value
, b.date_value_row_num
, a.reporting_cluster
, a.business_unit
, a.country_cluster
, a.metric_name
, a.dimension_name
, a.dimension_value
, a.metric_type
, a.flag_more_is_good
, a.flag_is_p0
, a.team_ownership
, a.metric_value_numerator
, a.metric_value_denominator
, a.metric_value_numerator_2
, a.metric_value_denominator_2
, 'Current' AS data_selection
FROM union_all_statement AS a
JOIN final_date_lkup AS b
ON a.date_granularity = b.date_granularity
AND a.date_value = b.date_value

UNION ALL

SELECT
a.focus_group
, a.metric_group
, a.date_granularity
, b.date_year
, b.date_value
, b.date_value_row_num
, a.reporting_cluster
, a.business_unit
, a.country_cluster
, a.metric_name
, a.dimension_name
, a.dimension_value
, a.metric_type
, a.flag_more_is_good
, a.flag_is_p0
, a.team_ownership
, a.metric_value_numerator
, a.metric_value_denominator
, a.metric_value_numerator_2
, a.metric_value_denominator_2
, 'PrevDateValue' AS data_selection
FROM union_all_statement AS a
JOIN final_date_lkup AS b
ON a.date_granularity = b.date_granularity
AND a.date_value = b.prev_date_value

UNION ALL

SELECT
a.focus_group
, a.metric_group
, a.date_granularity
, b.date_year
, b.date_value
, b.date_value_row_num
, a.reporting_cluster
, a.business_unit
, a.country_cluster
, a.metric_name
, a.dimension_name
, a.dimension_value
, a.metric_type
, a.flag_more_is_good
, a.flag_is_p0
, a.team_ownership
, a.metric_value_numerator
, a.metric_value_denominator
, a.metric_value_numerator_2
, a.metric_value_denominator_2
, 'PrevDateValueV2' AS data_selection
FROM union_all_statement AS a
JOIN final_date_lkup AS b
ON a.date_granularity = b.date_granularity
AND a.date_value = b.prev_date_value_v2

UNION ALL

SELECT
a.focus_group
, a.metric_group
, a.date_granularity
, b.date_year
, b.date_value
, b.date_value_row_num
, a.reporting_cluster
, a.business_unit
, a.country_cluster
, a.metric_name
, a.dimension_name
, a.dimension_value
, a.metric_type
, a.flag_more_is_good
, a.flag_is_p0
, a.team_ownership
, a.metric_value_numerator
, a.metric_value_denominator
, a.metric_value_numerator_2
, a.metric_value_denominator_2
, 'PrevYearDateValue' AS data_selection
FROM union_all_statement AS a
JOIN final_date_lkup AS b
ON a.date_granularity = b.date_granularity
AND a.date_value = b.prev_year_date_value
)
SELECT
date_granularity
, date_year
, date_value
, date_value_row_num AS date_value_order
, reporting_cluster
, business_unit
, country_cluster
, focus_group
, metric_group
, metric_name
, INT(SPLIT(metric_name, '_')[0]) AS metric_name_order
, dimension_name
, dimension_value
, metric_type
, flag_more_is_good
, flag_is_p0
, team_ownership
, SUM(CASE WHEN data_selection = 'Current' THEN metric_value_numerator ELSE 0 END) AS current_metric_value_numerator
, SUM(CASE WHEN data_selection = 'Current' THEN metric_value_denominator ELSE 0 END) AS current_metric_value_denominator
, SUM(CASE WHEN data_selection = 'Current' THEN metric_value_numerator_2 ELSE 0 END) AS current_metric_value_numerator_2
, SUM(CASE WHEN data_selection = 'Current' THEN metric_value_denominator_2 ELSE 0 END) AS current_metric_value_denominator_2
, SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_numerator ELSE 0 END) AS prev_metric_value_numerator
, SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_denominator ELSE 0 END) AS prev_metric_value_denominator
, SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_numerator_2 ELSE 0 END) AS prev_metric_value_numerator_2
, SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_denominator_2 ELSE 0 END) AS prev_metric_value_denominator_2
, SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_numerator ELSE 0 END) AS prev_yr_metric_value_numerator
, SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_denominator ELSE 0 END) AS prev_yr_metric_value_denominator
, SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_numerator_2 ELSE 0 END) AS prev_yr_metric_value_numerator_2
, SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_denominator_2 ELSE 0 END) AS prev_yr_metric_value_denominator_2
, SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_numerator ELSE 0 END) AS prev_v2_metric_value_numerator
, SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_denominator ELSE 0 END) AS prev_v2_metric_value_denominator
, SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_numerator_2 ELSE 0 END) AS prev_v2_metric_value_numerator_2
, SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_denominator_2 ELSE 0 END) AS prev_v2_metric_value_denominator_2
, CURRENT_TIMESTAMP AS last_update_ts
FROM union_all_data
WHERE date_year >= (EXTRACT(YEAR FROM CURRENT_DATE()) - 1)
GROUP BY ALL

"""

refresh_table_template = "REFRESH TABLE {}.{};"

for x in metric_schema.values():
  spark.sql(refresh_table_template.format(x['database_name'], x['table_name']))

spark.sql("REFRESH TABLE payments_hf.business_units;")

df = spark.sql(final_sql_script_with_flags.format(final_sql_script))

save_path = (f's3://hf-payments-data-lake-live-main/payments_hf/payments_p0_metrics_part_3')

database = "payments_hf"
table_name = "payments_p0_metrics_part_3"
# write table
(
    df.write.format("delta")
    .mode("overwrite")
    .option("path", save_path)
    .option("overwriteSchema", "true")
    .option("spark.databricks.delta.autoCompact.enabled", "true")
    .option("spark.databricks.delta.optimizeWrite.enabled", "true")
    .option("spark.databricks.delta.vacuum.parallelDelete.enabled", "true")
    .saveAsTable(f"{database}.{table_name}")
)

# COMMAND ----------

# MAGIC %sql
# MAGIC REFRESH TABLE payments_hf.payments_p0_metrics;
# MAGIC REFRESH TABLE payments_hf.payments_p0_metrics_part_1;
# MAGIC REFRESH TABLE payments_hf.payments_p0_metrics_part_2;
# MAGIC REFRESH TABLE payments_hf.payments_p0_metrics_part_3;
# MAGIC
# MAGIC DROP TABLE IF EXISTS payments_hf.payments_p0_metrics_backup;
# MAGIC
# MAGIC CREATE TABLE payments_hf.payments_p0_metrics_backup AS 
# MAGIC SELECT * FROM payments_hf.payments_p0_metrics;
# MAGIC
# MAGIC DROP TABLE IF EXISTS payments_hf.payments_p0_metrics;
# MAGIC
# MAGIC CREATE TABLE payments_hf.payments_p0_metrics AS 
# MAGIC SELECT * FROM payments_hf.payments_p0_metrics_part_1
# MAGIC UNION ALL
# MAGIC SELECT * FROM payments_hf.payments_p0_metrics_part_2
# MAGIC UNION ALL
# MAGIC SELECT * FROM payments_hf.payments_p0_metrics_part_3
# MAGIC ;

# COMMAND ----------

# template = """
# SELECT
# '{}' AS focus_group
# , '{}' AS metric_group
# , '{}' AS date_granularity
# , {} AS date_value
# , b.reporting_cluster
# , CASE WHEN b.reporting_cluster = 'Overall' THEN b.business_unit ELSE 'Null' END AS business_unit
# , b.country_cluster
# , '{}' AS metric_name
# , '{}' AS dimension_name
# , STRING({}) AS dimension_value
# , '{}' AS metric_type
# , '{}' AS flag_more_is_good
# , '{}' AS flag_is_p0
# , {} AS metric_value_numerator
# , {} AS metric_value_denominator
# , {} AS metric_value_numerator_2
# , {} AS metric_value_denominator_2
# FROM {}.{} AS a
# JOIN (
#   SELECT
#   business_unit
#   , explode(reporting_cluster_array) AS reporting_cluster
#   , 'Null' AS country_cluster

#   FROM payments_hf.business_units

#   UNION ALL

#   SELECT
#   business_unit
#   , 'Overall' AS reporting_cluster
#   , CASE 
#     WHEN brand_code IN ('F75', 'YF') THEN 'RTE'
#     WHEN brand NOT IN ('hellofresh') THEN 'WL'
#     WHEN business_unit IN ('AU', 'NZ') THEN 'AUNZ'
#     WHEN business_unit IN ('BE', 'NL', 'LU', 'FR') THEN 'BENELUXFR'
#     WHEN business_unit IN ('DE', 'AT', 'CH') THEN 'DACH'
#     WHEN business_unit IN ('NO', 'SE', 'DK') THEN 'NORDICS'
#     WHEN business_unit IN ('ES', 'IT') THEN 'SOUTH EU'
#     ELSE business_unit
#     END AS country_cluster

#   FROM payments_hf.business_units
#   ) AS b
# ON a.{} = b.business_unit
# {}
# GROUP BY ALL

# """

# count_ = 1
# final_sql_script = ""

# for x in metric_schema.values():
#   for date_granularity, date_granularity_value in x['date_granularity_mapping'].items():
#     for dimension_name, dimension_value in x['dimension_value_mapping'].items():
#       for metric_name, metric_script in x['metric_list'].items():
#         if metric_name in x['dimension_mapping'][dimension_name]:
#           if metric_script['metric_type'] == 'ratio-ratio':
#             sql_script = template.format(x['focus_group'],
#                                       x['metric_group'],
#                                       date_granularity,
#                                       date_granularity_value,
#                                       metric_name,
#                                       dimension_name,
#                                       dimension_value,
#                                       metric_script['metric_type'],
#                                       metric_script['more_is_good'],
#                                       metric_script['is_p0'],
#                                       metric_script['numerator'],
#                                       metric_script['denominator'],
#                                       metric_script['numerator_2'],
#                                       metric_script['denominator_2'],
#                                       x['database_name'],
#                                       x['table_name'],
#                                       x['country'],
#                                       x['where_filter'])
#           else:
#               sql_script = template.format(x['focus_group'],
#                                           x['metric_group'],
#                                           date_granularity,
#                                           date_granularity_value,
#                                           metric_name,
#                                           dimension_name,
#                                           dimension_value,
#                                           metric_script['metric_type'],
#                                           metric_script['more_is_good'],
#                                           metric_script['is_p0'],
#                                           metric_script['numerator'],
#                                           metric_script['denominator'],
#                                           'NULL',
#                                           'NULL',
#                                           x['database_name'],
#                                           x['table_name'],
#                                           x['country'],
#                                           x['where_filter'])
#           if count_ == 1:
#             final_sql_script = sql_script
#             count_ += 1
#           else:
#             final_sql_script = final_sql_script + "UNION ALL" + sql_script

# # print(final_sql_script)

# final_sql_script_with_flags = """
# WITH date_lkup AS (
#   SELECT
#   'WEEK' AS date_granularity
#     , hellofresh_week AS date_value
#     , dd.hellofresh_year AS date_year
#     , INT(SPLIT(dd.hellofresh_week, '-W')[1]) AS date_granularity_num
#   FROM dimensions.date_dimension dd
#   WHERE
#     hellofresh_week >= '2021-W01'
#     AND DATE(date_string_backwards) < CURRENT_DATE()
#   GROUP BY ALL

#   UNION ALL

#   SELECT
#   'MONTH' AS date_granularity
#     , CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS date_value
#     , dd.hellofresh_year AS date_year
#     , INT(dd.hellofresh_month) AS date_granularity_num
#   FROM dimensions.date_dimension dd
#   WHERE
#     hellofresh_week >= '2021-W01'
#     AND DATE(date_string_backwards) < CURRENT_DATE()    
#   GROUP BY ALL

#   UNION ALL

#   SELECT
#   'QUARTER' AS date_granularity
#     , CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS date_value
#     , dd.hellofresh_year AS date_year
#     , INT(SPLIT(dd.hellofresh_quarter, 'Q')[1]) AS date_granularity_num
#   FROM dimensions.date_dimension dd
#   WHERE
#     hellofresh_week >= '2021-W01'
#     AND DATE(date_string_backwards) < CURRENT_DATE()    
#   GROUP BY ALL
#   )
#    , date_lkup_row AS (
#   SELECT
#   date_granularity
#     , date_value
#     , date_year
#     , date_granularity_num
#     , ROW_NUMBER() OVER (PARTITION BY date_granularity ORDER BY date_year, date_granularity_num ) AS date_value_row_num

#   FROM date_lkup
#   )
#    , final_date_lkup AS (
#   -- ignoring the W53 performance
#   SELECT
#   a.date_granularity
#     , a.date_value
#     , a.date_year
#     , a.date_granularity_num
#     , a.date_value_row_num
#     , pdl.date_value AS prev_date_value
#     , CASE 
#         WHEN a.date_granularity IN ('MONTH', 'QUARTER') THEN pdl.date_value
#         WHEN a.date_granularity IN ('WEEK') THEN pdl2.date_value
#       END AS prev_date_value_v2
#     , pydl.date_value AS prev_year_date_value
#   FROM date_lkup_row AS a
#   LEFT JOIN date_lkup_row AS pdl
#        ON a.date_granularity = pdl.date_granularity
#        AND a.date_value_row_num = pdl.date_value_row_num + 1

#   LEFT JOIN date_lkup_row AS pdl2
#        ON a.date_granularity = pdl2.date_granularity
#        AND a.date_value_row_num = pdl2.date_value_row_num + 4

#   JOIN date_lkup_row AS pydl
#        ON a.date_granularity = pydl.date_granularity
#        AND a.date_granularity_num = pydl.date_granularity_num
#        AND a.date_year = pydl.date_year + 1
#   )
#   , union_all_statement AS (
#   {}
# )
# , union_all_data AS (
# SELECT
# a.focus_group
# , a.metric_group
# , a.date_granularity
# , b.date_year
# , a.date_value
# , b.date_value_row_num
# , a.reporting_cluster
# , a.business_unit
# , a.country_cluster
# , a.metric_name
# , a.dimension_name
# , a.dimension_value
# , a.metric_type
# , a.flag_more_is_good
# , a.flag_is_p0
# , a.metric_value_numerator
# , a.metric_value_denominator
# , a.metric_value_numerator_2
# , a.metric_value_denominator_2
# , 'Current' AS data_selection
# FROM union_all_statement AS a
# JOIN final_date_lkup AS b
# ON a.date_granularity = b.date_granularity
# AND a.date_value = b.date_value

# UNION ALL

# SELECT
# a.focus_group
# , a.metric_group
# , a.date_granularity
# , b.date_year
# , b.date_value
# , b.date_value_row_num
# , a.reporting_cluster
# , a.business_unit
# , a.country_cluster
# , a.metric_name
# , a.dimension_name
# , a.dimension_value
# , a.metric_type
# , a.flag_more_is_good
# , a.flag_is_p0
# , a.metric_value_numerator
# , a.metric_value_denominator
# , a.metric_value_numerator_2
# , a.metric_value_denominator_2
# , 'PrevDateValue' AS data_selection
# FROM union_all_statement AS a
# JOIN final_date_lkup AS b
# ON a.date_granularity = b.date_granularity
# AND a.date_value = b.prev_date_value

# UNION ALL

# SELECT
# a.focus_group
# , a.metric_group
# , a.date_granularity
# , b.date_year
# , b.date_value
# , b.date_value_row_num
# , a.reporting_cluster
# , a.business_unit
# , a.country_cluster
# , a.metric_name
# , a.dimension_name
# , a.dimension_value
# , a.metric_type
# , a.flag_more_is_good
# , a.flag_is_p0
# , a.metric_value_numerator
# , a.metric_value_denominator
# , a.metric_value_numerator_2
# , a.metric_value_denominator_2
# , 'PrevDateValueV2' AS data_selection
# FROM union_all_statement AS a
# JOIN final_date_lkup AS b
# ON a.date_granularity = b.date_granularity
# AND a.date_value = b.prev_date_value_v2

# UNION ALL

# SELECT
# a.focus_group
# , a.metric_group
# , a.date_granularity
# , b.date_year
# , b.date_value
# , b.date_value_row_num
# , a.reporting_cluster
# , a.business_unit
# , a.country_cluster
# , a.metric_name
# , a.dimension_name
# , a.dimension_value
# , a.metric_type
# , a.flag_more_is_good
# , a.flag_is_p0
# , a.metric_value_numerator
# , a.metric_value_denominator
# , a.metric_value_numerator_2
# , a.metric_value_denominator_2
# , 'PrevYearDateValue' AS data_selection
# FROM union_all_statement AS a
# JOIN final_date_lkup AS b
# ON a.date_granularity = b.date_granularity
# AND a.date_value = b.prev_year_date_value
# )
# SELECT
# date_granularity
# , date_year
# , date_value
# , date_value_row_num AS date_value_order
# , reporting_cluster
# , business_unit
# , country_cluster
# , focus_group
# , metric_group
# , metric_name
# , INT(SPLIT(metric_name, '_')[0]) AS metric_name_order
# , dimension_name
# , dimension_value
# , metric_type
# , flag_more_is_good
# , flag_is_p0
# , SUM(CASE WHEN data_selection = 'Current' THEN metric_value_numerator ELSE 0 END) AS current_metric_value_numerator
# , SUM(CASE WHEN data_selection = 'Current' THEN metric_value_denominator ELSE 0 END) AS current_metric_value_denominator
# , SUM(CASE WHEN data_selection = 'Current' THEN metric_value_numerator_2 ELSE 0 END) AS current_metric_value_numerator_2
# , SUM(CASE WHEN data_selection = 'Current' THEN metric_value_denominator_2 ELSE 0 END) AS current_metric_value_denominator_2
# , SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_numerator ELSE 0 END) AS prev_metric_value_numerator
# , SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_denominator ELSE 0 END) AS prev_metric_value_denominator
# , SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_numerator_2 ELSE 0 END) AS prev_metric_value_numerator_2
# , SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_denominator_2 ELSE 0 END) AS prev_metric_value_denominator_2
# , SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_numerator ELSE 0 END) AS prev_yr_metric_value_numerator
# , SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_denominator ELSE 0 END) AS prev_yr_metric_value_denominator
# , SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_numerator_2 ELSE 0 END) AS prev_yr_metric_value_numerator_2
# , SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_denominator_2 ELSE 0 END) AS prev_yr_metric_value_denominator_2
# , SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_numerator ELSE 0 END) AS prev_v2_metric_value_numerator
# , SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_denominator ELSE 0 END) AS prev_v2_metric_value_denominator
# , SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_numerator_2 ELSE 0 END) AS prev_v2_metric_value_numerator_2
# , SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_denominator_2 ELSE 0 END) AS prev_v2_metric_value_denominator_2
# , CURRENT_TIMESTAMP AS last_update_ts
# FROM union_all_data
# WHERE date_year >= (EXTRACT(YEAR FROM CURRENT_DATE()) - 1)
# GROUP BY ALL

# """

# refresh_table_template = "REFRESH TABLE {}.{};"

# for x in metric_schema.values():
#   spark.sql(refresh_table_template.format(x['database_name'], x['table_name']))

# spark.sql("REFRESH TABLE payments_hf.business_units;")

# df = spark.sql(final_sql_script_with_flags.format(final_sql_script))

# save_path = (f's3://hf-payments-data-lake-live-main/payments_hf/payments_p0_metrics')

# database = "payments_hf"
# table_name = "payments_p0_metrics"
# # write table
# (
#     df.write.format("delta")
#     .mode("overwrite")
#     .option("path", save_path)
#     .option("overwriteSchema", "true")
#     .option("spark.databricks.delta.autoCompact.enabled", "true")
#     .option("spark.databricks.delta.optimizeWrite.enabled", "true")
#     .option("spark.databricks.delta.vacuum.parallelDelete.enabled", "true")
#     .saveAsTable(f"{database}.{table_name}")
# )

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP VIEW payments_hf_staging.payments_p0_metrics_view;
# MAGIC
# MAGIC CREATE VIEW payments_hf_staging.payments_p0_metrics_view AS 
# MAGIC SELECT * FROM payments_hf.payments_p0_metrics;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DROP VIEW IF EXISTS payments_hf.payments_p0_metrics_growth_integration_view;
# MAGIC
# MAGIC CREATE VIEW payments_hf.payments_p0_metrics_growth_integration_view AS 
# MAGIC SELECT
# MAGIC   clusters.cluster_,
# MAGIC   a.business_unit AS bob_entity_code,
# MAGIC   a.date_value AS week,
# MAGIC   CONCAT(
# MAGIC     'Payments: ', trim(regexp_replace(replace(regexp_replace(regexp_replace(a.metric_group, '([0-9]_)','_$1'), '([A-Z])',' \$1'), '_', ''), ' \+', ' '))
# MAGIC   ) AS metric_group,
# MAGIC   trim(regexp_replace(replace(regexp_replace(regexp_replace(a.metric_name, '([0-9]_)','_$1'), '([A-Z])',' \$1'), '_', ''), ' \+', ' ')) AS metric_name,
# MAGIC   'Ratio' AS metric_type,
# MAGIC   a.dimension_value AS additional_split,
# MAGIC   SUM(a.current_metric_value_numerator) AS numerator,
# MAGIC   SUM(a.current_metric_value_denominator) AS denominator
# MAGIC FROM
# MAGIC   payments_hf.payments_p0_metrics a
# MAGIC     INNER JOIN materialized_views.pa_growth_cro_p0_clusters clusters
# MAGIC       ON a.business_unit = clusters.bob_entity_code
# MAGIC WHERE
# MAGIC   1 = 1
# MAGIC   AND a.date_granularity = 'WEEK'
# MAGIC   AND a.reporting_cluster = 'Overall'
# MAGIC   AND a.flag_is_p0 = 'TRUE'
# MAGIC   AND (
# MAGIC     (
# MAGIC       a.metric_name IN (
# MAGIC         '1_PaymentPageVisitToSuccess',
# MAGIC         '2_SelectToSuccess',
# MAGIC         '1_ReactivationRate',
# MAGIC         '1_Total Duplicate Rate',
# MAGIC         '2_Total Duplicate Block Rate',
# MAGIC         '1_Payment Fraud Block Rate'
# MAGIC       )
# MAGIC       AND a.metric_group IN (
# MAGIC         '1_Checkout Funnel', '1_ReactivationFunnel', '3_Payment Fraud', '2_Voucher Fraud'
# MAGIC       )
# MAGIC       AND a.dimension_name IN ('_Overall', 'PaymentMethod', 'ChannelCategory')
# MAGIC     )
# MAGIC     OR (
# MAGIC       a.metric_name IN ('2_PreDunningAR', '3_PostDunningAR', '')
# MAGIC       AND a.metric_group IN ('1_1_Overall Total Box Candidates')
# MAGIC       AND a.dimension_name IN ('_Overall', 'PaymentMethod')
# MAGIC     )
# MAGIC     OR (
# MAGIC       a.metric_name IN ('3_PostDunningAR')
# MAGIC       AND a.metric_group IN ('1_2_Loyalty: LL0 (Initial charges)')
# MAGIC       AND a.dimension_name IN ('_Overall')
# MAGIC     )
# MAGIC     OR (
# MAGIC       a.metric_name IN ('0_ShipRate', '2_Recovery_12wkCohort', '5_DunningBadDebtRate_12wkCohort', '1_ChargeBackRate')
# MAGIC       AND a.dimension_name IN ('_Overall')
# MAGIC     )
# MAGIC   )
# MAGIC GROUP BY ALL

# COMMAND ----------

# MAGIC %md
# MAGIC Dev: to run quicker for minor changes

# COMMAND ----------

# template = """
# SELECT
# '{}' AS focus_group
# , '{}' AS metric_group
# , '{}' AS date_granularity
# , {} AS date_value
# , b.reporting_cluster
# , CASE WHEN b.reporting_cluster = 'Overall' THEN b.business_unit ELSE 'Null' END AS business_unit
# , b.country_cluster
# , '{}' AS metric_name
# , '{}' AS dimension_name
# , STRING({}) AS dimension_value
# , '{}' AS metric_type
# , '{}' AS flag_more_is_good
# , '{}' AS flag_is_p0
# , {} AS metric_value_numerator
# , {} AS metric_value_denominator
# , {} AS metric_value_numerator_2
# , {} AS metric_value_denominator_2
# FROM {}.{} AS a
# JOIN (
#   SELECT
#   business_unit
#   , explode(reporting_cluster_array) AS reporting_cluster
#   , 'Null' AS country_cluster

#   FROM payments_hf.business_units

#   UNION ALL

#   SELECT
#   business_unit
#   , 'Overall' AS reporting_cluster
#   , CASE 
#     WHEN brand_code IN ('F75', 'YF') THEN 'RTE'
#     WHEN brand NOT IN ('hellofresh') THEN 'WL'
#     WHEN business_unit IN ('AU', 'NZ') THEN 'AUNZ'
#     WHEN business_unit IN ('BE', 'NL', 'LU', 'FR') THEN 'BENELUXFR'
#     WHEN business_unit IN ('DE', 'AT', 'CH') THEN 'DACH'
#     WHEN business_unit IN ('NO', 'SE', 'DK') THEN 'NORDICS'
#     WHEN business_unit IN ('ES', 'IT') THEN 'SOUTH EU'
#     ELSE business_unit
#     END AS country_cluster

#   FROM payments_hf.business_units
#   ) AS b
# ON a.{} = b.business_unit
# {}
# GROUP BY ALL

# """

# count_ = 1
# final_sql_script = ""

# for x in metric_schema.values():
#   if x['focus_group'] == "3_Active":
#     for date_granularity, date_granularity_value in x['date_granularity_mapping'].items():
#       for dimension_name, dimension_value in x['dimension_value_mapping'].items():
#         for metric_name, metric_script in x['metric_list'].items():
#           if metric_name in x['dimension_mapping'][dimension_name]:
#             if metric_script['metric_type'] == 'ratio-ratio':
#               sql_script = template.format(x['focus_group'],
#                                         x['metric_group'],
#                                         date_granularity,
#                                         date_granularity_value,
#                                         metric_name,
#                                         dimension_name,
#                                         dimension_value,
#                                         metric_script['metric_type'],
#                                         metric_script['more_is_good'],
#                                         metric_script['is_p0'],
#                                         metric_script['numerator'],
#                                         metric_script['denominator'],
#                                         metric_script['numerator_2'],
#                                         metric_script['denominator_2'],
#                                         x['database_name'],
#                                         x['table_name'],
#                                         x['country'],
#                                         x['where_filter'])
#             else:
#                 sql_script = template.format(x['focus_group'],
#                                             x['metric_group'],
#                                             date_granularity,
#                                             date_granularity_value,
#                                             metric_name,
#                                             dimension_name,
#                                             dimension_value,
#                                             metric_script['metric_type'],
#                                             metric_script['more_is_good'],
#                                             metric_script['is_p0'],
#                                             metric_script['numerator'],
#                                             metric_script['denominator'],
#                                             'NULL',
#                                             'NULL',
#                                             x['database_name'],
#                                             x['table_name'],
#                                             x['country'],
#                                             x['where_filter'])
#             if count_ == 1:
#               final_sql_script = sql_script
#               count_ += 1
#             else:
#               final_sql_script = final_sql_script + "UNION ALL" + sql_script

# # print(final_sql_script)

# final_sql_script_with_flags = """
# WITH date_lkup AS (
#   SELECT
#   'WEEK' AS date_granularity
#     , hellofresh_week AS date_value
#     , dd.hellofresh_year AS date_year
#     , INT(SPLIT(dd.hellofresh_week, '-W')[1]) AS date_granularity_num
#   FROM dimensions.date_dimension dd
#   WHERE
#     hellofresh_week >= '2021-W01'
#     AND DATE(date_string_backwards) < CURRENT_DATE()
#   GROUP BY ALL

#   UNION ALL

#   SELECT
#   'MONTH' AS date_granularity
#     , CONCAT(dd.hellofresh_year, '-', dd.hellofresh_month) AS date_value
#     , dd.hellofresh_year AS date_year
#     , INT(dd.hellofresh_month) AS date_granularity_num
#   FROM dimensions.date_dimension dd
#   WHERE
#     hellofresh_week >= '2021-W01'
#     AND DATE(date_string_backwards) < CURRENT_DATE()    
#   GROUP BY ALL

#   UNION ALL

#   SELECT
#   'QUARTER' AS date_granularity
#     , CONCAT(dd.hellofresh_year, '-', dd.hellofresh_quarter) AS date_value
#     , dd.hellofresh_year AS date_year
#     , INT(SPLIT(dd.hellofresh_quarter, 'Q')[1]) AS date_granularity_num
#   FROM dimensions.date_dimension dd
#   WHERE
#     hellofresh_week >= '2021-W01'
#     AND DATE(date_string_backwards) < CURRENT_DATE()    
#   GROUP BY ALL
#   )
#    , date_lkup_row AS (
#   SELECT
#   date_granularity
#     , date_value
#     , date_year
#     , date_granularity_num
#     , ROW_NUMBER() OVER (PARTITION BY date_granularity ORDER BY date_year, date_granularity_num ) AS date_value_row_num

#   FROM date_lkup
#   )
#    , final_date_lkup AS (
#   -- ignoring the W53 performance
#   SELECT
#   a.date_granularity
#     , a.date_value
#     , a.date_year
#     , a.date_granularity_num
#     , a.date_value_row_num
#     , pdl.date_value AS prev_date_value
#     , CASE 
#         WHEN a.date_granularity IN ('MONTH', 'QUARTER') THEN pdl.date_value
#         WHEN a.date_granularity IN ('WEEK') THEN pdl2.date_value
#       END AS prev_date_value_v2
#     , pydl.date_value AS prev_year_date_value
#   FROM date_lkup_row AS a
#   LEFT JOIN date_lkup_row AS pdl
#        ON a.date_granularity = pdl.date_granularity
#        AND a.date_value_row_num = pdl.date_value_row_num + 1

#   LEFT JOIN date_lkup_row AS pdl2
#        ON a.date_granularity = pdl2.date_granularity
#        AND a.date_value_row_num = pdl2.date_value_row_num + 4

#   JOIN date_lkup_row AS pydl
#        ON a.date_granularity = pydl.date_granularity
#        AND a.date_granularity_num = pydl.date_granularity_num
#        AND a.date_year = pydl.date_year + 1
#   )
#   , union_all_statement AS (
#   {}
# )
# , union_all_data AS (
# SELECT
# a.focus_group
# , a.metric_group
# , a.date_granularity
# , b.date_year
# , a.date_value
# , b.date_value_row_num
# , a.reporting_cluster
# , a.business_unit
# , a.country_cluster
# , a.metric_name
# , a.dimension_name
# , a.dimension_value
# , a.metric_type
# , a.flag_more_is_good
# , a.flag_is_p0
# , a.metric_value_numerator
# , a.metric_value_denominator
# , a.metric_value_numerator_2
# , a.metric_value_denominator_2
# , 'Current' AS data_selection
# FROM union_all_statement AS a
# JOIN final_date_lkup AS b
# ON a.date_granularity = b.date_granularity
# AND a.date_value = b.date_value

# UNION ALL

# SELECT
# a.focus_group
# , a.metric_group
# , a.date_granularity
# , b.date_year
# , b.date_value
# , b.date_value_row_num
# , a.reporting_cluster
# , a.business_unit
# , a.country_cluster
# , a.metric_name
# , a.dimension_name
# , a.dimension_value
# , a.metric_type
# , a.flag_more_is_good
# , a.flag_is_p0
# , a.metric_value_numerator
# , a.metric_value_denominator
# , a.metric_value_numerator_2
# , a.metric_value_denominator_2
# , 'PrevDateValue' AS data_selection
# FROM union_all_statement AS a
# JOIN final_date_lkup AS b
# ON a.date_granularity = b.date_granularity
# AND a.date_value = b.prev_date_value

# UNION ALL

# SELECT
# a.focus_group
# , a.metric_group
# , a.date_granularity
# , b.date_year
# , b.date_value
# , b.date_value_row_num
# , a.reporting_cluster
# , a.business_unit
# , a.country_cluster
# , a.metric_name
# , a.dimension_name
# , a.dimension_value
# , a.metric_type
# , a.flag_more_is_good
# , a.flag_is_p0
# , a.metric_value_numerator
# , a.metric_value_denominator
# , a.metric_value_numerator_2
# , a.metric_value_denominator_2
# , 'PrevDateValueV2' AS data_selection
# FROM union_all_statement AS a
# JOIN final_date_lkup AS b
# ON a.date_granularity = b.date_granularity
# AND a.date_value = b.prev_date_value_v2

# UNION ALL

# SELECT
# a.focus_group
# , a.metric_group
# , a.date_granularity
# , b.date_year
# , b.date_value
# , b.date_value_row_num
# , a.reporting_cluster
# , a.business_unit
# , a.country_cluster
# , a.metric_name
# , a.dimension_name
# , a.dimension_value
# , a.metric_type
# , a.flag_more_is_good
# , a.flag_is_p0
# , a.metric_value_numerator
# , a.metric_value_denominator
# , a.metric_value_numerator_2
# , a.metric_value_denominator_2
# , 'PrevYearDateValue' AS data_selection
# FROM union_all_statement AS a
# JOIN final_date_lkup AS b
# ON a.date_granularity = b.date_granularity
# AND a.date_value = b.prev_year_date_value
# )
# SELECT
# date_granularity
# , date_year
# , date_value
# , date_value_row_num AS date_value_order
# , reporting_cluster
# , business_unit
# , country_cluster
# , focus_group
# , metric_group
# , metric_name
# , INT(SPLIT(metric_name, '_')[0]) AS metric_name_order
# , dimension_name
# , dimension_value
# , metric_type
# , flag_more_is_good
# , flag_is_p0
# , SUM(CASE WHEN data_selection = 'Current' THEN metric_value_numerator ELSE 0 END) AS current_metric_value_numerator
# , SUM(CASE WHEN data_selection = 'Current' THEN metric_value_denominator ELSE 0 END) AS current_metric_value_denominator
# , SUM(CASE WHEN data_selection = 'Current' THEN metric_value_numerator_2 ELSE 0 END) AS current_metric_value_numerator_2
# , SUM(CASE WHEN data_selection = 'Current' THEN metric_value_denominator_2 ELSE 0 END) AS current_metric_value_denominator_2
# , SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_numerator ELSE 0 END) AS prev_metric_value_numerator
# , SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_denominator ELSE 0 END) AS prev_metric_value_denominator
# , SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_numerator_2 ELSE 0 END) AS prev_metric_value_numerator_2
# , SUM(CASE WHEN data_selection = 'PrevDateValue' THEN metric_value_denominator_2 ELSE 0 END) AS prev_metric_value_denominator_2
# , SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_numerator ELSE 0 END) AS prev_yr_metric_value_numerator
# , SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_denominator ELSE 0 END) AS prev_yr_metric_value_denominator
# , SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_numerator_2 ELSE 0 END) AS prev_yr_metric_value_numerator_2
# , SUM(CASE WHEN data_selection = 'PrevYearDateValue' THEN metric_value_denominator_2 ELSE 0 END) AS prev_yr_metric_value_denominator_2
# , SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_numerator ELSE 0 END) AS prev_v2_metric_value_numerator
# , SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_denominator ELSE 0 END) AS prev_v2_metric_value_denominator
# , SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_numerator_2 ELSE 0 END) AS prev_v2_metric_value_numerator_2
# , SUM(CASE WHEN data_selection = 'PrevDateValueV2' THEN metric_value_denominator_2 ELSE 0 END) AS prev_v2_metric_value_denominator_2
# , CURRENT_TIMESTAMP AS last_update_ts
# FROM union_all_data
# WHERE date_year >= (EXTRACT(YEAR FROM CURRENT_DATE()) - 1)
# GROUP BY ALL

# """

# refresh_table_template = "REFRESH TABLE {}.{};"

# for x in metric_schema.values():
#   spark.sql(refresh_table_template.format(x['database_name'], x['table_name']))

# spark.sql("REFRESH TABLE payments_hf.business_units;")

# df = spark.sql(final_sql_script_with_flags.format(final_sql_script))

# save_path = (f's3://hf-payments-data-lake-live-main/payments_hf/payments_p0_metrics_active')

# database = "payments_hf"
# table_name = "payments_p0_metrics_active"
# # write table
# (
#     df.write.format("delta")
#     .mode("overwrite")
#     .option("path", save_path)
#     .option("overwriteSchema", "true")
#     .option("spark.databricks.delta.autoCompact.enabled", "true")
#     .option("spark.databricks.delta.optimizeWrite.enabled", "true")
#     .option("spark.databricks.delta.vacuum.parallelDelete.enabled", "true")
#     .saveAsTable(f"{database}.{table_name}")
# )

# COMMAND ----------

# %sql
# DROP TABLE IF EXISTS payments_hf.payments_p0_metrics_temp;
# CREATE TABLE payments_hf.payments_p0_metrics_temp AS SELECT * FROM payments_hf.payments_p0_metrics;

# DELETE FROM payments_hf.payments_p0_metrics
# WHERE focus_group = "3_Active";

# INSERT INTO payments_hf.payments_p0_metrics
# SELECT * FROM payments_hf.payments_p0_metrics_active;

# COMMAND ----------

# MAGIC %md
# MAGIC # Refresh P0 dashboard

# COMMAND ----------

!! pip install tableauserverclient
import sys
sys.path.append('/Workspace/Users/aoez@hellofresh.com/local')

from utils.tableau_api import TableauApi

# Payments P0 Metrics
# https://tableau.hellofresh.io/#/workbooks/13486/views
workbook_id = 'a2f8cb08-d3cf-4195-92b6-5f5b48998fb8'

TableauApi.trigger_extract_refresh(workbook_id=workbook_id)

# COMMAND ----------

# MAGIC %md
# MAGIC # Generate Weekly Steering Report
# MAGIC
# MAGIC Run the steering report generation notebook to create the weekly steering report.
# MAGIC This will generate a comprehensive report from the `payments_hf.payments_p0_metrics` table.

# COMMAND ----------

# Run the steering report generation notebook
# File location: https://github.com/vkvb-hf/cursor-databricks/blob/feature/long-term-steering-report/projects/long_term_steering_report/
dbutils.notebook.run("/Workspace/Users/visal.kumar@hellofresh.com/generate_steering_report", timeout_seconds=3600)

# COMMAND ----------

# MAGIC %md
# MAGIC # [Obsolete] Steering meeting document:

# COMMAND ----------

# MAGIC %md
# MAGIC ### Steps to generate AI insights:
# MAGIC 1) Ensure the `payments_hf.payments_p0_metrics` table is updated with latest information
# MAGIC 2) Modify (`folder_path`) and run the script below, to generate steering folder in databricks
# MAGIC 3) Download the folder (or the three files) to local location where Cursor/AI can access it
# MAGIC 4) Use Prompt 1 to generate the steering document (you need three documents as input: 
# MAGIC - detailed_summary.txt (script generated)
# MAGIC - Payments P0 Metrics.md (markdown file: shared below)
# MAGIC - REPORT_PROMPT.md (markdown file: shared below)
# MAGIC 5) Upload to git, and copy paste it to steering document
# MAGIC
# MAGIC [Link to sample git folder with analysis document](https://github.com/hellofresh/ddi-pays-pipelines/tree/patch/PY-2983-steering-Sep-3/ddi_pays_pipelines/steering) 
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Script

# COMMAND ----------

import pyspark.sql.functions as F
from pyspark.sql.types import DoubleType
import math
import os
import errno
import shutil  # For directory removal operations
import pandas as pd  # Explicitly import pandas
from time import time  # For performance tracking

# Modify the path to the workspace folder
WORKSPACE_FOLDER = f'/Workspace/Users/elizaveta.dmitrieva@hellofresh.com'

# Define metrics and constants for reporting
REPORTING_CLUSTERS = ['Overall', 'HF-NA', 'HF-INTL', 'US-HF', 'RTE', 'WL']

# List of metrics to generate reports for
STEERING_METRICS = [
    '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess',
    '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 2_SelectToSuccess',
    '1_Activation (Paid + Referrals) - 1_Checkout Funnel (backend) - 1_PaymentPageVisitToSuccess',
    '1_Activation (Paid + Referrals) - 2_Voucher Fraud - 1_Total Duplicate Rate',
    '1_Activation (Paid + Referrals) - 2_Voucher Fraud - 2_Total Duplicate Block Rate',
    '1_Activation (Paid + Referrals) - 3_Payment Fraud - 1_Payment Fraud Block Rate',
    '2_Reactivations - 1_ReactivationFunnel - 1_ReactivationRate',
    '3_Active - 1_1_Overall Total Box Candidates - 2_PreDunningAR',
    '3_Active - 1_2_Loyalty: LL0 (Initial charges) - 2_PreDunningAR',
    '3_Active - 1_3_Loyalty: LL0 and LL1+ (Recurring charges) - 2_PreDunningAR',
    '3_Active - 2_1_Boxes Shipped - 0_ShipRate',
    '3_Active - 2_1_Boxes Shipped - 1_RecoveryW0',
    '3_Active - 2_2_Boxes Shipped - 12wk lag - 2_Recovery_12wkCohort',
    '3_Active - 2_2_Boxes Shipped - 12wk lag - 3_DunningAvgNetProfit_12wkCohort'
]

# Get the latest complete week data for reporting
# We need a complete week (7 days) that's already passed to ensure data completeness
start_time = time()
latest_date_query = """
    SELECT
    hellofresh_week
    FROM dimensions.date_dimension dd
    WHERE
      hellofresh_week >= '2021-W01'
      AND DATE(date_string_backwards) < CURRENT_DATE()
    GROUP BY 1
    HAVING COUNT(*)=7
    ORDER BY hellofresh_week DESC
    LIMIT 1
    """
latest_date = spark.sql(latest_date_query)
latest_date_str = latest_date.toPandas().values[0][0]
print(f"Latest reporting week: {latest_date_str}")
print(f"Time to get latest date: {time() - start_time:.2f} seconds")

# Output directory path for storing steering reports
# Format: /Workspace/Users/{username}/steering-{YYYY-Www}
# Each run creates a new directory with the latest week's data
OUTPUT_FOLDER = f'{WORKSPACE_FOLDER}/steering-{latest_date_str}'
print(f"Reports will be saved to: {OUTPUT_FOLDER}")

# Refresh table data to ensure we have the latest metrics
print("Refreshing tables...")
start_time = time()
spark.sql("REFRESH TABLE payments_hf.payments_p0_metrics")

# Define metrics to exclude from analysis
EXCLUDED_METRICS = [
    '5_DunningBadDebtRate_12wkCohort',
    '6_TotalBadDebtRate_12wkCohort',
    '3_PaymentProcessingFees%',
    '1_ChargeBackRate', 
    '3_PostDunningAR'
]

# Metrics that require special dimension handling
SPECIAL_METRICS = ['0_ShipRate', '1_RecoveryW0', '2_Recovery_12wkCohort', '3_DunningAvgNetProfit_12wkCohort']

# Excluded dimensions
EXCLUDED_DIMENSIONS = ['LoyaltySegment', 'PaymentMethod_OrderType']

# Build and execute the main metrics query
print("Fetching latest metrics data...")
metrics_query = f"""
-- Main query to fetch metrics data with two parts:
-- 1. Metrics at cluster level
-- 2. Metrics at business unit level (derived from 'Overall' cluster)
SELECT 
a.date_value,
a.reporting_cluster,
CASE WHEN a.reporting_cluster = 'Overall' THEN "Null" ELSE a.business_unit END AS business_unit,
CONCAT(a.focus_group, ' - ', a.metric_group, ' - ',a.metric_name) as metric_final_name,
CASE 
  WHEN a.metric_name IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])}) THEN '_Overall' 
  ELSE dimension_name 
END AS dimension_name,
a.dimension_value,
a.flag_more_is_good,
a.flag_is_p0,
a.metric_type,
SUM(a.current_metric_value_numerator) AS current_metric_value_numerator,
SUM(a.current_metric_value_denominator) AS current_metric_value_denominator,
SUM(a.prev_metric_value_numerator) AS prev_metric_value_numerator,
SUM(a.prev_metric_value_denominator) AS prev_metric_value_denominator
FROM payments_hf.payments_p0_metrics a
WHERE 1=1
  AND metric_type IN ('ratio', 'dollar-ratio')
  AND metric_name not in ({','.join([f"'{m}'" for m in EXCLUDED_METRICS])})
  AND flag_is_p0 = 'TRUE'
  AND date_granularity = 'WEEK'
  AND dimension_name NOT LIKE '%DeclineReason%'
  AND dimension_name not in ({','.join([f"'{d}'" for d in EXCLUDED_DIMENSIONS])})
  AND (
    (a.metric_name not IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])})) 
    OR (a.metric_name IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])}) AND dimension_value in ('Good'))
    )
  AND date_value = '{latest_date_str}'
  GROUP BY ALL
UNION ALL
SELECT 
a.date_value,
'bu_level' AS reporting_cluster,
a.business_unit,
CONCAT(a.focus_group, ' - ', a.metric_group, ' - ',a.metric_name) as metric_final_name,
a.dimension_name,
a.dimension_value,
a.flag_more_is_good,
a.flag_is_p0,
a.metric_type,
SUM(a.current_metric_value_numerator) AS current_metric_value_numerator,
SUM(a.current_metric_value_denominator) AS current_metric_value_denominator,
SUM(a.prev_metric_value_numerator) AS prev_metric_value_numerator,
SUM(a.prev_metric_value_denominator) AS prev_metric_value_denominator
FROM payments_hf.payments_p0_metrics a
WHERE 1=1
  AND metric_type IN ('ratio', 'dollar-ratio')
  AND metric_name not in ({','.join([f"'{m}'" for m in EXCLUDED_METRICS])})
  AND flag_is_p0 = 'TRUE'
  AND date_granularity = 'WEEK'
  AND (
    (a.dimension_name = '_Overall' AND a.metric_name not IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])})) 
    OR (a.metric_name IN ({','.join([f"'{m}'" for m in SPECIAL_METRICS])}) AND dimension_value in ('Good'))
    )
  AND reporting_cluster = 'Overall'
  AND date_value = '{latest_date_str}'
  GROUP BY ALL
"""

latest_data = spark.sql(metrics_query)
print(f"Fetched {latest_data.count()} rows of metrics data in {time() - start_time:.2f} seconds")

# Function to calculate z-score for statistical significance testing
@F.udf(returnType=DoubleType())
def calculate_z_score(n1, d1, n2, d2, metric_type='proportion'):
    """
    Calculate z-score for difference between two proportions or averages
    
    Parameters:
    -----------
    n1 : float
        Numerator for current period
    d1 : float
        Denominator for current period
    n2 : float
        Numerator for previous period
    d2 : float
        Denominator for previous period
    metric_type : str
        Type of metric: 'ratio' (for proportions) or 'dollar-ratio' (for monetary values)
        
    For ratio metrics: n is number of successes, d is total trials
    For dollar-ratio metrics: n is sum of values, d is count of values
    
    Returns:
    --------
    float or None
        Z-score for the difference between periods, or None if calculation not possible
    """
    # Basic validation - require minimum sample size for statistical validity
    # and protect against None values
    MIN_SAMPLE_SIZE = 30
    if d1 is None or d2 is None or d1 < MIN_SAMPLE_SIZE or d2 < MIN_SAMPLE_SIZE:
        return None
    
    try:
        # Convert to float to ensure proper division
        n1, d1, n2, d2 = float(n1), float(d1), float(n2), float(d2)
        
        # Calculate values for both periods
        value1 = n1 / d1 if d1 > 0 else 0
        value2 = n2 / d2 if d2 > 0 else 0
        
        # Different calculation methods based on metric type
        if metric_type.lower() == 'ratio':
            # For proportions (e.g., success rates, conversion rates)
            # Use pooled estimate for standard error calculation
            pooled_p = (n1 + n2) / (d1 + d2)
            
            # Avoid division by zero and invalid math domain errors
            if pooled_p == 0 or pooled_p == 1:
                return None
                
            # Standard error using pooled estimate
            se = math.sqrt(pooled_p * (1 - pooled_p) * (1/d1 + 1/d2))
            
        else:  # dollar-ratio metrics
            # For averages of monetary values
            # We need variance estimates but only have sum (n) and count (d)
            # Use a simplified approach with the difference as variance estimate
            
            # Estimated pooled variance (simplified approximation)
            pooled_var = max((abs(value1 - value2) / 2) ** 2, 0.0001)  # Ensure minimum variance
            
            # Standard error for difference of means
            se = math.sqrt(pooled_var * (1/d1 + 1/d2))
        
        # Calculate z-score (standardized difference)
        if se > 0:
            z_score = (value1 - value2) / se
            return z_score
            
    except (ValueError, ZeroDivisionError, TypeError) as e:
        # Handle any calculation errors safely
        return None
        
    return None

      
# Define a mapping of z-scores to significance levels for easier maintenance
# Format: (z_score_threshold, significance_level, confidence_percentage)
SIGNIFICANCE_LEVELS = [
    (6.361, 7.0, 99.99999),  # Extremely high significance
    (5.612, 6.0, 99.9999),
    (4.892, 5.0, 99.999),
    (4.265, 4.0, 99.99),
    (3.719, 3.5, 99.95),
    (3.291, 3.0, 99.9),
    (3.090, 2.8, 99.8),
    (2.807, 2.5, 99.5),
    (2.576, 2.0, 99.0),
    (2.326, 1.8, 98.0),
    (2.054, 1.6, 96.0),
    (1.96, 1.5, 95.0),
    (1.645, 1.0, 90.0)
]

# Build significance level case expression dynamically
significance_case = None
for threshold, level, percentage in SIGNIFICANCE_LEVELS:
    if significance_case is None:
        significance_case = F.when(F.abs(F.col("prev_week_z_score")) > threshold, level)
    else:
        significance_case = significance_case.when(F.abs(F.col("prev_week_z_score")) > threshold, level)
significance_case = significance_case.otherwise(0.0)

# Calculate metrics with significance
print("Calculating statistical significance and metrics...")
start_time = time()
significance_df = (
    latest_data
    # Calculate current and previous ratios with safety checks
    .withColumn("current_week_ratio", 
                F.when(F.col("current_metric_value_denominator") > 0,
                       F.col("current_metric_value_numerator") / F.col("current_metric_value_denominator"))
                .otherwise(0))
    .withColumn("prev_week_ratio", 
                F.when(F.col("prev_metric_value_denominator") > 0,
                       F.col("prev_metric_value_numerator") / F.col("prev_metric_value_denominator"))
                .otherwise(0))
        
    # Calculate z-score for statistical significance
    .withColumn("prev_week_z_score", 
                calculate_z_score(
                    F.col("current_metric_value_numerator"),
                    F.col("current_metric_value_denominator"),
                    F.col("prev_metric_value_numerator"),
                    F.col("prev_metric_value_denominator"),
                    F.col("metric_type")
                ))
        
    # Apply the dynamically created significance level case expression
    .withColumn("prev_week_significance_level", significance_case)
    
    # Calculate absolute and relative changes with protection against division by zero
    .withColumn("absolute_change", F.col("current_week_ratio") - F.col("prev_week_ratio"))
    .withColumn("relative_change_pct", 
                F.when(F.col("prev_week_ratio") > 0,
                       (F.col("absolute_change") / F.col("prev_week_ratio")) * 100)
                .otherwise(0))  # Default to 0 instead of None for easier calculations later

    # Determine business impact direction based on flag_more_is_good and direction of change
    .withColumn("impact_direction",
                F.when(
                    (F.col("flag_more_is_good") == "TRUE") & (F.col("absolute_change") > 0), "Positive"
                ).when(
                    (F.col("flag_more_is_good") == "TRUE") & (F.col("absolute_change") < 0), "Negative"
                ).when(
                    (F.col("flag_more_is_good") == "FALSE") & (F.col("absolute_change") > 0), "Negative"
                ).when(
                    (F.col("flag_more_is_good") == "FALSE") & (F.col("absolute_change") < 0), "Positive"
                ).otherwise("Neutral"))
)

# Convert to Pandas DataFrame for further processing
print("Converting to Pandas DataFrame...")
df = significance_df.toPandas()
print(f"DataFrame shape: {df.shape}")
print(f"Metrics calculation completed in {time() - start_time:.2f} seconds")

# Fetch business unit to reporting cluster mapping
print("Loading business unit mappings...")
start_time = time()
spark.sql("REFRESH TABLE payments_hf.business_units")

# Query to map business units to their reporting clusters
# This is used to filter business units by their parent cluster
country_mapping_query = """
    SELECT
      business_unit,
      explode(reporting_cluster_array) AS reporting_cluster
    FROM payments_hf.business_units
"""
country_mapping = spark.sql(country_mapping_query)
country_mapping_df = country_mapping.toPandas()
print(f"Loaded {len(country_mapping_df)} business unit mappings in {time() - start_time:.2f} seconds")

def format_number(num):
    """
    Format numbers for readability with appropriate scale indicators
    
    Parameters:
    -----------
    num : float or int
        The number to format
    
    Returns:
    --------
    str
        Human-readable formatted number string with appropriate suffix:
        - Numbers < 1000: As is with 1 decimal place if needed
        - 1K-999K: With 'K' suffix (thousands)
        - 1M+: With 'M' suffix (millions)
        - Negative numbers maintain their sign
    """
    if num is None:
        return "0"
        
    try:
        # Handle different numeric types safely
        num = float(num)
        abs_num = abs(num)
        
        # Format based on magnitude
        if abs_num < 1000:
            # For small numbers, show whole number if it's an integer
            return f"{num:.0f}" if num == int(num) else f"{num:.1f}"
        elif abs_num < 1000000:
            # For thousands, use K suffix with 1 decimal place
            return f"{num/1000:.1f}K"
        else:
            # For millions and above, use M suffix with 1 decimal place
            return f"{num/1000000:.1f}M"
    except (TypeError, ValueError):
        # Handle any errors gracefully
        return "0"
      
def generate_overall_summary(row):
    """
    Generate a formatted summary for overall metrics with insights on change significance and impact.
    
    Parameters:
    -----------
    row : pandas.Series
        A row from the metrics dataframe containing all metric data and calculated fields
    
    Returns:
    --------
    str
        A well-formatted summary string describing the metric change and its business impact
    """
    # Extract key values from the row
    metric_name = row['metric_final_name']
    cluster = row['reporting_cluster']
    metric_type = row['metric_type']
    
    # Calculate impact values
    rel_change = row['relative_change_pct']
    abs_change = row['absolute_change'] * 100  # Convert to percentage points for ratio metrics
    
    try:
        # Calculate volume impacted by the change
        volume_impacted = row['current_metric_value_denominator'] * abs(rel_change) / 100
    except (TypeError, ValueError):
        volume_impacted = 0
    
    # Determine statistical significance text based on level
    sig_level = row.get('prev_week_significance_level', 0)
    sig_text = "significant" if sig_level >= 3 else "not statistically significant"
    
    # Determine magnitude description based on relative change percentage
    if abs(rel_change) >= 20:
        magnitude = "substantial"
    elif abs(rel_change) >= 10:
        magnitude = "notable"
    else:
        magnitude = "slight"
    
    # Direction of change (increased or decreased)
    direction = "increased" if abs_change > 0 else "decreased"
    
    # Business impact from the calculated impact direction
    impact = row['impact_direction'].lower()
    
    # Format the summary based on the metric type
    if metric_type == 'ratio':
        # For ratio metrics (like percentages)
        current_ratio = row['current_week_ratio'] * 100  # Convert to percentage
        prev_ratio = row['prev_week_ratio'] * 100  # Convert to percentage
        
        summary = (
            f"For {cluster} cluster, the {metric_name} {direction} from {prev_ratio:.2f}% to {current_ratio:.2f}%, "
            f"a {magnitude} {abs(rel_change):.2f}% {direction[:-1]} (volume impacted: {format_number(volume_impacted)}). "
            f"This change is {sig_text} and has a {impact} business impact."
        )
    else:
        # For monetary metrics (like Euro values)
        current_ratio = row['current_week_ratio']
        prev_ratio = row['prev_week_ratio']
        
        summary = (
            f"For {cluster} cluster, the {metric_name} {direction} from €{prev_ratio:.2f} to €{current_ratio:.2f}, "
            f"a {magnitude} {abs(rel_change):.2f}% {direction[:-1]} (volume impacted: {format_number(volume_impacted)}). "
            f"This change is {sig_text} and has a {impact} business impact."
        )
              
    return summary
def write_metrics_data(summary_file, detailed_file, title, data_df, is_business_unit=False, write_header=True):
    """
    Helper function to write metrics data to both summary and detailed summary files.
    This avoids code duplication and ensures consistent formatting across files.
    
    Parameters:
    -----------
    summary_file : file object
        Open file handle for the summary file
    detailed_file : file object
        Open file handle for the detailed summary file
    title : str
        Title for the section being written
    data_df : pandas.DataFrame
        DataFrame containing the data to write
    is_business_unit : bool, default=False
        Whether this data represents business unit data (affects filtering)
    write_header : bool, default=True
        Whether to write a header before the data
    """
    # Create a copy to avoid SettingWithCopyWarning
    df_copy = data_df.copy()
    
    # Calculate the values needed for sorting and filtering
    df_copy.loc[:, 'abs_rel_change'] = abs(df_copy['relative_change_pct'])
    df_copy.loc[:, 'volume_impacted'] = df_copy['current_metric_value_denominator']*df_copy['abs_rel_change']/100
    
    # Sort and filter data
    if is_business_unit:
        sorted_data = df_copy.sort_values('volume_impacted', ascending=False)
    else:
        sorted_data = df_copy.sort_values(['dimension_name', 'volume_impacted'], ascending=False)
    
    # Filter to only show significant changes
    sorted_data = sorted_data[(sorted_data['abs_rel_change']>10) | (sorted_data['volume_impacted']>30)]
    
    if sorted_data.empty:
        return  # Nothing to write
        
    # Write header if needed
    if write_header:
        summary_file.write(f"\n{title}")
        detailed_file.write(f"\n{title}")
    
    # Write data to both files
    for _, row in sorted_data.iterrows():
        # Handle business unit vs dimension formatting
        if is_business_unit:
            if row['business_unit'] == "Null":
                continue  # Skip null business units
            item_name = row['business_unit']
        else:
            item_name = f"{row['dimension_name']} {row['dimension_value']}"
        
        # Common calculations
        direction = "increase" if row['absolute_change'] > 0 else "decrease"
        change = abs(row['relative_change_pct'])
        volume_impacted = row['volume_impacted']
        metric_type = row['metric_type']
        
        # Format based on metric type
        if metric_type == 'ratio':
            current = row['current_week_ratio'] * 100
            prev = row['prev_week_ratio'] * 100
            line = f"\n- {item_name}: {prev:.2f}% to {current:.2f}% ({change:.2f}% {direction}, volume impacted: {format_number(volume_impacted)})"
        else:
            current = row['current_week_ratio']
            prev = row['prev_week_ratio']
            line = f"\n- {item_name}: €{prev:.2f} to €{current:.2f} ({change:.2f}% {direction}, volume impacted: {format_number(volume_impacted)})"
        
        # Write to both files
        summary_file.write(line)
        detailed_file.write(line)


def write_formatted_summaries(df, output_folder):
    """
    Write formatted summaries for all metrics according to the specified structure.
    
    This function generates two types of output files:
    1. A main detailed_summary.txt with all metrics and their analysis
    2. Individual summary files for each metric in separate directories
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The metrics dataframe with all calculated values
    output_folder : str
        Base folder path for output
    """
    print(f"\nGenerating reports in {output_folder}...")
    start_time = time()
    
    # Define the output folder
    output_folder_dir = f'{output_folder}'
    
    # Clean up: Check if directory exists, delete and recreate it
    print("Cleaning up previous output directory...")
    if os.path.exists(output_folder_dir):
        try:
            shutil.rmtree(output_folder_dir)
            print(f"Removed existing directory: {output_folder_dir}")
        except Exception as e:
            print(f"Warning: Failed to remove directory: {e}")
    
    # Create fresh directory for summaries
    try:
        os.makedirs(output_folder_dir)
        print(f"Created directory: {output_folder_dir}")
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            print(f"Error creating directory: {exc}")
            raise

    with open(f'{output_folder_dir}/detailed_summary.txt', 'w') as f:
        f.write(f"{latest_date_str} Steering Document")

    # Process each metric in the defined list
    metrics_count = len(STEERING_METRICS)
    print(f"Generating reports for {metrics_count} metrics...")
    
    for idx, mn in enumerate(STEERING_METRICS, 1):
        print(f"  Processing metric {idx}/{metrics_count}: {mn}")
        metric_start_time = time()
        
        # Filter data for this metric
        df_metric = df[df['metric_final_name'] == mn]
        
        if df_metric.empty:
            print(f"  Warning: No data found for metric '{mn}'")
            continue
            
        # Create directory for this metric's summary
        summary_dir = f'{output_folder}/{mn}'
        
        if not os.path.exists(summary_dir):
            try:
                os.makedirs(summary_dir)
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

        with open(f'{summary_dir}/summary.txt', 'w') as f:
          f.write(f"{mn}")

        with open(f'{output_folder_dir}/detailed_summary.txt', 'a') as f:
            f.write(f"\n\n{mn}")

        # Process each reporting cluster
        for rc in REPORTING_CLUSTERS:
            
            # 1. Level 1 - Overall summary
            level1_rows = df_metric[(df_metric['reporting_cluster'] == rc) & 
                                   (df_metric['dimension_name'] == '_Overall')]
            
            if not level1_rows.empty:
                # Open both files once for efficiency
                with open(f'{summary_dir}/summary.txt', 'a') as summary_file, \
                     open(f'{output_folder_dir}/detailed_summary.txt', 'a') as detailed_file:
                    
                    summary_file.write("\n\n")
                    detailed_file.write("\n\n")
                    
                    # Process each row and write to both files
                    for _, row in level1_rows.iterrows():
                        summary = generate_overall_summary(row)
                        summary_file.write(f"{summary}")
                        detailed_file.write(f"{summary}")


            # 2. Level 2 - Dimensions summary
            level2_dims_rows = df_metric[(df_metric['reporting_cluster'] == rc) & 
                                       (df_metric['dimension_name'] != '_Overall')]
            
            if not level2_dims_rows.empty:
                # Open both files once and write to them using our helper function
                with open(f'{summary_dir}/summary.txt', 'a') as summary_file, \
                     open(f'{output_folder_dir}/detailed_summary.txt', 'a') as detailed_file:
                    
                    # Write dimensions data to both files
                    write_metrics_data(
                        summary_file=summary_file,
                        detailed_file=detailed_file,
                        title="Top dimensions by change magnitude:",
                        data_df=level2_dims_rows,
                        is_business_unit=False
                    )

            # else:
            #     print(f"  Warning: No data found for dimensions for metric '{mn}'")

            # 3. Level 2 - Business Units summary (only for non-Overall clusters)
            if rc != 'Overall':
                # Get business units for this reporting cluster
                rc_bu = country_mapping_df[country_mapping_df['reporting_cluster'] == rc].business_unit.tolist()
                level2_bu_rows = df_metric[(df_metric['business_unit'].isin(rc_bu))]
                
                if not level2_bu_rows.empty:
                    # Open both files once and write to them using our helper function
                    with open(f'{summary_dir}/summary.txt', 'a') as summary_file, \
                         open(f'{output_folder_dir}/detailed_summary.txt', 'a') as detailed_file:
                        
                        # Write business unit data to both files
                        write_metrics_data(
                            summary_file=summary_file,
                            detailed_file=detailed_file,
                            title="All business units by change magnitude:",
                            data_df=level2_bu_rows,
                            is_business_unit=True
                        )
                else:
                    print(f"  Warning: No data found for business units for metric '{mn}'")

        # Print timing for this metric        
        print(f"    Completed in {time() - metric_start_time:.2f} seconds")
    
    # Print summary of files generated
    total_time = time() - start_time
    print(f"\nReport generation complete:")
    print(f"  - Main summary file: {output_folder_dir}/detailed_summary.txt")
    print(f"  - Individual metric folders: {metrics_count}")
    print(f"  - Total generation time: {total_time:.2f} seconds")

# Main execution point
if __name__ == "__main__":
    print("Starting steering metrics generation...")
    start_time_total = time()
    
    # Generate the formatted summaries
    write_formatted_summaries(df, OUTPUT_FOLDER)
    
    # Print execution summary
    total_time = time() - start_time_total
    print(f"\nSteering metrics generation completed!")
    print(f"Total execution time: {total_time:.2f} seconds")
    print(f"Output directory: {OUTPUT_FOLDER}")
    print(f"Generated reports for week: {latest_date_str}")

# COMMAND ----------

# import pyspark.sql.functions as F
# from pyspark.sql.types import DoubleType
# import math

# latest_date = spark.sql(f"""
#     SELECT
#     hellofresh_week
#     FROM dimensions.date_dimension dd
#     WHERE
#       hellofresh_week >= '2021-W01'
#       AND DATE(date_string_backwards) < CURRENT_DATE()
#     GROUP BY 1
#     HAVING COUNT(*)=7
#     ORDER BY hellofresh_week DESC
#     LIMIT 1
#     """)

# latest_date_str = latest_date.toPandas().values[0][0]

# # modify this
# folder_path = f'/Workspace/Users/visal.kumar@hellofresh.com/steering-{latest_date_str}'

# refresh_data = spark.sql("REFRESH TABLE payments_hf.payments_p0_metrics")

# latest_data = spark.sql(f"""
# SELECT 
# a.date_value,
# a.reporting_cluster,
# CASE WHEN a.reporting_cluster = 'Overall' THEN "Null" ELSE a.business_unit END AS business_unit,
# CONCAT(a.focus_group, ' - ', a.metric_group, ' - ',a.metric_name) as metric_final_name,
# a.dimension_name,
# a.dimension_value,
# a.flag_more_is_good,
# a.flag_is_p0,
# SUM(a.current_metric_value_numerator) AS current_metric_value_numerator,
# SUM(a.current_metric_value_denominator) AS current_metric_value_denominator,
# SUM(a.prev_metric_value_numerator) AS prev_metric_value_numerator,
# SUM(a.prev_metric_value_denominator) AS prev_metric_value_denominator
# FROM payments_hf.payments_p0_metrics a
# WHERE 1=1
#   AND metric_type = 'ratio'
#   AND metric_name not in ('5_DunningBadDebtRate_12wkCohort','6_TotalBadDebtRate_12wkCohort', '3_PaymentProcessingFees%','1_ChargeBackRate', '3_PostDunningAR')
#   AND flag_is_p0 = 'TRUE'
#   AND date_granularity = 'WEEK'
#   AND dimension_name NOT LIKE '%DeclineReason%'
#   AND date_value = (
#     SELECT
#     hellofresh_week
#     FROM dimensions.date_dimension dd
#     WHERE
#       hellofresh_week >= '2021-W01'
#       AND DATE(date_string_backwards) < CURRENT_DATE()
#     GROUP BY 1
#     HAVING COUNT(*)=7
#     ORDER BY hellofresh_week DESC
#     LIMIT 1
#   )
#   GROUP BY ALL
#   """)

# # Function to calculate z-score for difference in proportions
# @F.udf(returnType=DoubleType())
# def calculate_z_score(n1, d1, n2, d2):
#     """
#     Calculate z-score for difference between two proportions
#     n1, d1: numerator and denominator for current period
#     n2, d2: numerator and denominator for previous period
#     """
#     if d1 is None or d2 is None or d1 < 30 or d2 < 30:
#         return None
    
#     # Calculate proportions
#     p1 = float(n1) / float(d1) if d1 > 0 else 0
#     p2 = float(n2) / float(d2) if d2 > 0 else 0
    
#     # Pooled proportion for standard error
#     pooled_p = (float(n1) + float(n2)) / (float(d1) + float(d2))
    
#     # Standard error
#     se = math.sqrt(pooled_p * (1 - pooled_p) * (1/float(d1) + 1/float(d2)))
    
#     # Z-score
#     if se > 0:
#         z_score = (p1 - p2) / se
#         return z_score
#     else:
#         return None
      
# # Calculate metrics with significance
# significance_df = (
#     latest_data
#     # Calculate current and previous ratios
#     .withColumn("current_week_ratio", 
#                 F.when(F.col("current_metric_value_denominator") > 0,
#                        F.col("current_metric_value_numerator") / F.col("current_metric_value_denominator"))
#                 .otherwise(0))
#     .withColumn("prev_week_ratio", 
#                 F.when(F.col("prev_metric_value_denominator") > 0,
#                        F.col("prev_metric_value_numerator") / F.col("prev_metric_value_denominator"))
#                 .otherwise(0))
#     # .withColumn("prev_month_ratio", 
#     #             F.when(F.col("prev_v2_metric_value_denominator") > 0,
#     #                    F.col("prev_v2_metric_value_numerator") / F.col("prev_v2_metric_value_denominator"))
#     #             .otherwise(0))
        
#     # Calculate z-score for statistical significance
#     .withColumn("prev_week_z_score", 
#                 calculate_z_score(F.col("current_metric_value_numerator"),
#                                 F.col("current_metric_value_denominator"),
#                                 F.col("prev_metric_value_numerator"),
#                                 F.col("prev_metric_value_denominator")))
    
#     # .withColumn("prev_month_z_score", 
#     #             calculate_z_score(F.col("current_metric_value_numerator"),
#     #                             F.col("current_metric_value_denominator"),
#     #                             F.col("prev_v2_metric_value_numerator"),
#     #                             F.col("prev_v2_metric_value_denominator")))    
#     # Calculate significance level as number of 9s after decimal point
#     # Using the relationship between z-score and p-value for two-tailed test
#     .withColumn("prev_week_significance_level",
#                 F.when(F.abs(F.col("prev_week_z_score")) > 6.361, 7.0)  # 99.99999%
#                 .when(F.abs(F.col("prev_week_z_score")) > 5.612, 6.0)  # 99.9999%
#                 .when(F.abs(F.col("prev_week_z_score")) > 4.892, 5.0)  # 99.999%
#                 .when(F.abs(F.col("prev_week_z_score")) > 4.265, 4.0)  # 99.99%
#                 .when(F.abs(F.col("prev_week_z_score")) > 3.719, 3.5)  # 99.95%
#                 .when(F.abs(F.col("prev_week_z_score")) > 3.291, 3.0)  # 99.9%
#                 .when(F.abs(F.col("prev_week_z_score")) > 3.090, 2.8)  # 99.8%
#                 .when(F.abs(F.col("prev_week_z_score")) > 2.807, 2.5)  # 99.5%
#                 .when(F.abs(F.col("prev_week_z_score")) > 2.576, 2.0)  # 99%
#                 .when(F.abs(F.col("prev_week_z_score")) > 2.326, 1.8)  # 98%
#                 .when(F.abs(F.col("prev_week_z_score")) > 2.054, 1.6)  # 96%
#                 .when(F.abs(F.col("prev_week_z_score")) > 1.96, 1.5)   # 95%
#                 .when(F.abs(F.col("prev_week_z_score")) > 1.645, 1.0)  # 90%
#                 .otherwise(0.0))

#     # .withColumn("prev_month_significance_level",
#     #             F.when(F.abs(F.col("prev_month_z_score")) > 6.361, 7.0)  # 99.99999%
#     #             .when(F.abs(F.col("prev_month_z_score")) > 5.612, 6.0)  # 99.9999%
#     #             .when(F.abs(F.col("prev_month_z_score")) > 4.892, 5.0)  # 99.999%
#     #             .when(F.abs(F.col("prev_month_z_score")) > 4.265, 4.0)  # 99.99%
#     #             .when(F.abs(F.col("prev_month_z_score")) > 3.719, 3.5)  # 99.95%
#     #             .when(F.abs(F.col("prev_month_z_score")) > 3.291, 3.0)  # 99.9%
#     #             .when(F.abs(F.col("prev_month_z_score")) > 3.090, 2.8)  # 99.8%
#     #             .when(F.abs(F.col("prev_month_z_score")) > 2.807, 2.5)  # 99.5%
#     #             .when(F.abs(F.col("prev_month_z_score")) > 2.576, 2.0)  # 99%
#     #             .when(F.abs(F.col("prev_month_z_score")) > 2.326, 1.8)  # 98%
#     #             .when(F.abs(F.col("prev_month_z_score")) > 2.054, 1.6)  # 96%
#     #             .when(F.abs(F.col("prev_month_z_score")) > 1.96, 1.5)   # 95%
#     #             .when(F.abs(F.col("prev_month_z_score")) > 1.645, 1.0)  # 90%
#     #             .otherwise(0.0))
    
#     # Calculate absolute and relative changes
#     .withColumn("absolute_change", F.col("current_week_ratio") - F.col("prev_week_ratio"))
#     .withColumn("relative_change_pct", 
#                 F.when(F.col("prev_week_ratio") > 0,
#                        (F.col("absolute_change") / F.col("prev_week_ratio")) * 100)
#                 .otherwise(None))

#     # Adjust for direction based on flag_more_is_good
#     .withColumn("impact_direction",
#                 F.when(
#                     (F.col("flag_more_is_good") == "TRUE") & (F.col("absolute_change") > 0), "Positive"
#                 ).when(
#                     (F.col("flag_more_is_good") == "TRUE") & (F.col("absolute_change") < 0), "Negative"
#                 ).when(
#                     (F.col("flag_more_is_good") == "FALSE") & (F.col("absolute_change") > 0), "Negative"
#                 ).when(
#                     (F.col("flag_more_is_good") == "FALSE") & (F.col("absolute_change") < 0), "Positive"
#                 ).otherwise("Neutral"))
    
#     # # Create impact score (combines statistical significance with business impact)
#     # .withColumn("impact_score",
#     #             F.when(F.col("prev_week_z_score").isNotNull(),
#     #                    F.abs(F.col("prev_week_z_score")) * F.abs(F.col("relative_change_pct")) / 100)
#     #             .otherwise(0))
    
#     # # Calculate impact volume - how many units/customers were affected by this change
#     # # This represents the absolute difference in volume multiplied by the ratio change
#     # .withColumn("impact_volume",
#     #             F.when((F.col("absolute_change").isNotNull()) & 
#     #                    (F.col("current_metric_value_denominator") > 0),
#     #                    F.abs(F.col("absolute_change")) * F.col("current_metric_value_denominator"))
#     #             .otherwise(0))
    
#     # # Alternative impact volume calculation showing the difference in actual units affected
#     # .withColumn("impact_volume_diff",
#     #             F.abs((F.col("current_week_ratio") * F.col("current_metric_value_denominator")) - 
#     #                   (F.col("prev_week_ratio") * F.col("prev_metric_value_denominator"))))
    
#     # Filter for minimum denominator threshold
# )

# df = significance_df.toPandas()

# country_mapping = spark.sql(f"""
#     SELECT
#   business_unit
#   , explode(reporting_cluster_array) AS reporting_cluster
#   FROM payments_hf.business_units
# """)

# country_mapping_df = country_mapping.toPandas()

# import os
# import errno

# for mn in df.metric_final_name.unique():
#   df_filter = df[df['metric_final_name']==mn]
#   # for rc in df_filter.reporting_cluster.unique():
#   for rc in ['Overall', 'HF-NA', 'HF-INTL', 'US-HF', 'RTE', 'WL']:
#     file_name = f'{folder_path}/{mn}/{rc}/significance_df_level_1_overall.csv'
#     f2 = f'{folder_path}/{mn}/{rc}/significance_df_level_2_overall_dimensions.csv'
#     f3 = f'{folder_path}/{mn}/{rc}/significance_df_level_2_overall_business_units.csv'
#     f4 = f'{folder_path}/{mn}/{rc}/significance_df_level_3_business_units_dimensions.csv'
#     if not os.path.exists(os.path.dirname(file_name)):
#       try:
#           os.makedirs(os.path.dirname(file_name))
#       except OSError as exc: # Guard against race condition
#           if exc.errno != errno.EEXIST:
#               raise
#     df_filter[(df_filter['reporting_cluster']==rc) & (df_filter['dimension_name']=='_Overall')].to_csv(f'{file_name}', index=False)
#     df_filter[(df_filter['reporting_cluster']==rc) & (df_filter['dimension_name']!='_Overall')].to_csv(f'{f2}', index=False)    
#     if rc != 'Overall':
#       rc_bu = country_mapping_df[country_mapping_df['reporting_cluster']==rc].business_unit.tolist()
#       df_filter[(df_filter['business_unit'].isin(rc_bu)) & (df_filter['dimension_name']=='_Overall')].to_csv(f'{f3}', index=False)    
#     # df_filter[(df_filter['business_unit'].isin(rc_bu)) & (df_filter['dimension_name']!='_Overall')].to_csv(f'{f4}', index=False)

# COMMAND ----------

# MAGIC %md
# MAGIC # Payments P0 Metrics.md

# COMMAND ----------

# MAGIC %md
# MAGIC # Payments P0 Metrics ([Table](https://tableau.hellofresh.io/views/PaymentsP0metrics_17284783585740/PaymentsP0Metrics) / [Chart](https://tableau.hellofresh.io/views/PaymentsP0metrics_17284783585740/TrendofP0Metrics) / [Sheet](https://docs.google.com/spreadsheets/d/1mBc1VhdlsOq35mpPBJR8LwTqgJyvn6o3EBzcfyti5T4/edit?gid=308499628#gid=308499628))
# MAGIC
# MAGIC 1. ## Activation (Paid \+ Referrals) [Elizaveta Dmitrieva](mailto:elizaveta.dmitrieva@hellofresh.com)
# MAGIC
# MAGIC    1. ### Checkout Funnel (Frontend)
# MAGIC
# MAGIC       1. **Payment Page Visit to Success (Ratio) [Khaled ElSayed](mailto:khaled.elsayed@hellofresh.com)**
# MAGIC          Conversion rate from checkout page visit to successful checkout.
# MAGIC          **Formula:** Successful Checkouts / Payment Page Visits
# MAGIC       2. **Select to Success (Ratio) [Khaled ElSayed](mailto:khaled.elsayed@hellofresh.com)**
# MAGIC          Conversion rate from selecting a payment method to successful checkout.
# MAGIC          **Formula:** Successful Checkouts / Payment Method Selections
# MAGIC
# MAGIC    2. ### Checkout Funnel (Backend)
# MAGIC
# MAGIC       1. **Payment Page Visit to Success (Ratio) [Khaled ElSayed](mailto:khaled.elsayed@hellofresh.com)**
# MAGIC
# MAGIC 2. ## Reactivations  [Elizaveta Dmitrieva](mailto:elizaveta.dmitrieva@hellofresh.com)
# MAGIC
# MAGIC    1. ### Reactivation Funnel
# MAGIC
# MAGIC       1. **Reactivation Success Rate (Ratio) [Khaled ElSayed](mailto:khaled.elsayed@hellofresh.com)**
# MAGIC          Percentage of reactivated customers who clicked CTA.
# MAGIC          **Formula:** Reactivated Customers / Reactivation Attempts
# MAGIC
# MAGIC 3. ## Fraud [Visal Kumar Vazhavandan Baskar](mailto:visal.kumar@hellofresh.com)[Cagdas Ozek](mailto:aoez@hellofresh.com)
# MAGIC
# MAGIC    1. ### Voucher Fraud
# MAGIC
# MAGIC       1. **Duplicate Rate (Ratio) [Anna Bauhofer](mailto:abau@hellofresh.com)**
# MAGIC          Percentage of checkout attempts identified as duplicate accounts.
# MAGIC          **Formula:** Duplicate Accounts / Checkout Attempts
# MAGIC       2. **Duplicate Block Rate (Ratio) [Anna Bauhofer](mailto:abau@hellofresh.com)**
# MAGIC          Percentage of blocked duplicate checkout attempts
# MAGIC          **Formula:** Blocked Duplicate Accounts / Checkout Attempts
# MAGIC
# MAGIC    2. ### Payment Fraud
# MAGIC
# MAGIC       1. **Payment Fraud Block Rate (Ratio) [Anna Bauhofer](mailto:abau@hellofresh.com)**
# MAGIC          Percentage of fraudulent checkout attempts blocked at checkout.
# MAGIC          **Formula:** Blocked Fraud Checkouts / Checkout Attempts
# MAGIC
# MAGIC 4. ## Recurring Payments
# MAGIC
# MAGIC    1. ### Total Box Candidates [Tatiana Anikina](mailto:tatiana.anikina@hellofresh.com)
# MAGIC
# MAGIC       1. **Acceptance Rate Before Risk Assessment (Pre-Dunning)	 (Ratio) [Zeeshan Akram](mailto:zeeshan.akram@hellofresh.com)**
# MAGIC          Percentage of paid orders before the dunning process.
# MAGIC          **Formula:** Paid Orders Before Dunning / Total Orders
# MAGIC       2. **Final Acceptance Rate (Post-Dunning) (Ratio) [Zeeshan Akram](mailto:zeeshan.akram@hellofresh.com)[Hasan Yagiz Söylemez](mailto:hasan.soeylemez@hellofresh.com)**
# MAGIC          Percentage of paid orders after the dunning process.
# MAGIC          **Formula:** Paid Orders After Dunning / Total Orders
# MAGIC       3. **LL0 (Initial charges): Final Acceptance Rate [Khaled ElSayed](mailto:khaled.elsayed@hellofresh.com)**
# MAGIC          (Same as Final Acceptance Rate AR but specific to initial charges).
# MAGIC          **Formula:** Paid Initial Orders After Dunning / Total Initial Orders
# MAGIC
# MAGIC    2. ### Boxes Shipped [Tatiana Anikina](mailto:tatiana.anikina@hellofresh.com)[Cagdas Ozek](mailto:aoez@hellofresh.com)
# MAGIC
# MAGIC       1. **Ship Rate after Dunning Decision (Ratio) [Hasan Yagiz Söylemez](mailto:hasan.soeylemez@hellofresh.com)**
# MAGIC          Percentage of unpaid orders that were shipped.
# MAGIC          **Formula:** Shipped Unpaid Orders / Unpaid Orders
# MAGIC       2. **Recovery Rate (Ratio) [Hasan Yagiz Söylemez](mailto:hasan.soeylemez@hellofresh.com)**
# MAGIC          Percentage of shipped unpaid orders that were recovered
# MAGIC          **Formula:** Recovered Orders / Shipped Unpaid Orders
# MAGIC       3. **Dunning Net Profit (12wk lag) (Monetary) [Hasan Yagiz Söylemez](mailto:hasan.soeylemez@hellofresh.com)**
# MAGIC          Net profit from recoveries of shipped unpaid orders.
# MAGIC          **Formula:** Recovered Revenue \- Costs of Shipped Unpaid Orders
# MAGIC       4. **Dunning Avg Net Profit (12wk lag) (Monetary) [Hasan Yagiz Söylemez](mailto:hasan.soeylemez@hellofresh.com)**
# MAGIC          Average net profit from recoveries of shipped unpaid orders over all orders with prediction.
# MAGIC          **Formula:** (Recovered Revenue \- Costs of Shipped Unpaid Orders) / ~~Shipped Unpaid~~ Orders with Prediction
# MAGIC       5. **Dunning Bad Debt (12wk lag) (Monetary) [Hasan Yagiz Söylemez](mailto:hasan.soeylemez@hellofresh.com)**
# MAGIC          Total amount written off as bad debt after 6 months.
# MAGIC          **Formula:** Unpaid Amount After 6 months
# MAGIC       6. **Dunning Bad Debt Rate (12wk lag) (Ratio) [Hasan Yagiz Söylemez](mailto:hasan.soeylemez@hellofresh.com)**
# MAGIC          Total amount written off as bad debt after ~~6 months~~ 12 weeks / Shipped Order Revenue.
# MAGIC          **Formula:** Unpaid Amount After ~~6 months~~ 12 weeks / Shipped Order Revenue
# MAGIC       7. **Profit Coverage Rate (Ratio) [Hasan Yagiz Söylemez](mailto:hasan.soeylemez@hellofresh.com)**
# MAGIC          Represents the proportion of actual net profit from recoveries relative to the theoretical maximum, calculated by scaling holdout group recoveries to the entire audience.
# MAGIC          **Formula:** Dunning Net Profit / Potential Maximum Dunning Net Profit
# MAGIC
# MAGIC    3. ### Chargebacks [Anna Bauhofer](mailto:abau@hellofresh.com)[Visal Kumar Vazhavandan Baskar](mailto:visal.kumar@hellofresh.com)
# MAGIC
# MAGIC       1. **Chargeback Rate (13w lag) (Ratio)**
# MAGIC          Percentage of transactions that resulted in a chargeback.
# MAGIC          **Formula:** Chargeback Transactions / Total Transactions
# MAGIC
# MAGIC 5. ## Cash Credits [Tatiana Anikina](mailto:tatiana.anikina@hellofresh.com)
# MAGIC
# MAGIC    1. ### Top-Ups \- *out of scope for now*
# MAGIC
# MAGIC       1. **Cash Credits Added Through Top-Ups (Monetary)**
# MAGIC          Total amount added via customer top-ups.
# MAGIC          **Formula:** Sum of Top-Up Transactions
# MAGIC
# MAGIC 6. ## Payment Costs [Cagdas Ozek](mailto:aoez@hellofresh.com)
# MAGIC
# MAGIC    1. ### Payment Processing \- *out of scope for now*
# MAGIC
# MAGIC       1. **Fees as % of GR	 (Ratio)**
# MAGIC          Percentage of total payments spent on processing fees.
# MAGIC          **Formula:** Total Payment Processing Fees / Total Payments Processed
# MAGIC       2. **Cost Per Order (Monetary)**
# MAGIC          Average payment processing cost per order.
# MAGIC          **Formula:** Total Payment Costs / Total Orders
# MAGIC
# MAGIC ## Formula Component Definitions
# MAGIC
# MAGIC * **Successful Checkouts**: Number of checkouts successfully completed.
# MAGIC * **Payment Page Visits**: Total visits to the checkout page.
# MAGIC * **Payment Method Selections**: Instances where a payment method is chosen at checkout page.
# MAGIC * **Duplicate Accounts**: Number of accounts flagged as duplicates (both pre/post checkout).
# MAGIC * **Checkout Attempts**: Total checkout attempts (*Place Order click*) made by customers.
# MAGIC * **Blocked Duplicate Accounts**: Duplicate accounts prevented from completing checkout due to high discount.
# MAGIC * **Blocked Fraud Checkouts**: Checkout attempts blocked due to suspected payment fraud.
# MAGIC * **Reactivated Customers**: Customers who successfully reactivated their account with a valid payment method
# MAGIC * **Reactivation Attempts**: Total number of customers clicked reactivation CTA
# MAGIC * **Paid Orders Before Dunning**: Orders successfully paid before logistics cutoff prior to packaging
# MAGIC * **Total Orders**: All orders created and got ready for payment during a specific period.
# MAGIC * **Paid Orders After Dunning**: Orders successfully paid (post-dunning) including the recovered orders
# MAGIC * **Paid Initial Orders After Dunning**: Initial orders successfully paid (post-dunning) including the recovered orders
# MAGIC * **Total Initial Orders**: All initial orders attempted.
# MAGIC * **Shipped Unpaid Orders**: Orders shipped despite not being paid initially.
# MAGIC * **Unpaid Orders**: Orders not being paid initially.
# MAGIC * **Recovered Orders**: Shipped unpaid orders that were recovered
# MAGIC * **Recovered Revenue \- Costs of Shipped Unpaid Orders**: Profit from recovered unpaid orders including the cost of goods.
# MAGIC * **Unpaid Amount After 6 months**: Outstanding debt after six months.
# MAGIC * **Chargeback Transactions**: Transactions that resulted in chargebacks.
# MAGIC * **Total Transactions**: All payment transactions processed.
# MAGIC * **Sum of Top-Up Transactions**: Total value of top-up payments made.
# MAGIC * **Total Payment Processing Fees**: Fees paid for processing payments.
# MAGIC * **Total Payments Processed**: Total amount of payments handled.
# MAGIC * **Total Payment Costs**: Overall costs related to payment processing.
# MAGIC * **Potential Maximum Dunning Net Profit:** The estimated upper limit of net profit that could be achieved if unpaid orders were perfectly predicted and shipped only to customers who would eventually pay. This is calculated by extrapolating the net profit of recovered payments in the holdout group to the entire audience, providing a benchmark for evaluating dunning efficiency.
# MAGIC
# MAGIC ---
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### REPORT_PROMPT.md

# COMMAND ----------

# MAGIC %md
# MAGIC # Weekly Payments Metrics Steering Report Prompt
# MAGIC
# MAGIC ## Instructions for Creating Weekly Reports
# MAGIC
# MAGIC ### Input Requirements
# MAGIC 1. Read "Payments P0 Metrics.md" to understand metric definitions
# MAGIC 2. Read the current week's metrics TSV file (YYYY-WXX_metrics.tsv)
# MAGIC 3. Input structure: Metric Name -> Summary.txt
# MAGIC
# MAGIC ### Report Structure
# MAGIC
# MAGIC Create a weekly payments metrics steering table with the following columns:
# MAGIC - **Metrics** (metric name only)
# MAGIC - **Anomaly/Callout** (important insights for each metric, cell content must not exceed 1000 characters)
# MAGIC - **Notes** (empty cell to be filled later)
# MAGIC
# MAGIC ### Metric Groups (in order)
# MAGIC 1. Payment Page Visit to Success (frontend, backend)
# MAGIC 2. Select to Success
# MAGIC 3. Duplicate Rate/Duplicate Block Rate
# MAGIC 4. Payment Fraud Block Rate
# MAGIC 5. Reactivation Rate
# MAGIC 6. AR Pre Dunning
# MAGIC 7. Acceptance LL0 (Initial Charge)
# MAGIC 8. Acceptance LL0 and LL1+ (Recurring Charge)
# MAGIC 9. Ship Rate/Recovery W0
# MAGIC 10. Recovery W12 - DW21
# MAGIC 11. Dunning Profit
# MAGIC
# MAGIC ### Report Requirements
# MAGIC
# MAGIC **Format Requirements:**
# MAGIC - **IMPORTANT: Use proper Markdown bullet points (`-`) NOT unicode bullets (`•`)**
# MAGIC - Use `<br>` for line breaks within table cells
# MAGIC - Use unicode arrows: ↑ (green up arrow) for increases, ↓ (red down arrow) for decreases
# MAGIC - Keep all content in table cells under 1000 characters
# MAGIC
# MAGIC **Content Requirements:**
# MAGIC - Always show the performance of Reporting Clusters: ['Overall', 'HF-NA', 'HF-INTL', 'US-HF', 'RTE', 'WL'] 
# MAGIC - Show current week vs previous week percentages with relative changes
# MAGIC - Check with previous month values to make trend statements
# MAGIC - Show significance scores for each change
# MAGIC - Use proper market naming: (BU) Brand-Country format (e.g., (US) HelloFresh-US)
# MAGIC - Consolidate different dimensions of the same metric for a market
# MAGIC - Group findings by metric categories
# MAGIC - Highlight major improvements and concerns
# MAGIC - Highlight where (business units/dimensions) for the significant differences
# MAGIC - Avoid repetitive information
# MAGIC - For Ship Rate, Recovery W0, Recovery W12, Dunning Profit: Only report on Good Customers Performance
# MAGIC
# MAGIC **Key Insights Section:**
# MAGIC - Add above the table
# MAGIC - Maximum 1000 characters
# MAGIC - **Use proper Markdown bullet points (`-`) NOT unicode bullets**
# MAGIC - Include 3-4 key insights covering:
# MAGIC   - Critical issues
# MAGIC   - Positive trends
# MAGIC   - Risk shifts
# MAGIC   - Emerging concerns
# MAGIC
# MAGIC ### Example Format
# MAGIC
# MAGIC ```markdown
# MAGIC # YYYY-WXX Weekly Payments Metrics Steering
# MAGIC
# MAGIC ## Key Insights
# MAGIC - **Critical Issues:** [Key problem areas with impact]
# MAGIC - **Positive Trends:** [Major improvements]
# MAGIC - **Risk Shifts:** [Strategic changes observed]
# MAGIC - **Emerging Concerns:** [New issues to watch]
# MAGIC
# MAGIC | Metrics | Anomaly/Callout | Notes |
# MAGIC | :--- | :--- | :--- |
# MAGIC | **Payment Page Visit to Success** | - **Overall**: 31.52% vs 31.36% (↑0.53%, not significant, volume: 213.3K)<br>- **HF-NA**: 31.52% vs 31.36% (↑0.53%, not significant, volume: 213.3K)<br>- **HF-INTL**: 31.52% vs 31.36% (↑0.53%, not significant, volume: 213.3K)<br>- **RTE**: 31.52% vs 31.36% (↑0.53%, not significant, volume: 213.3K)<br>- **WL**: 31.52% vs 31.36% (↑0.53%, not significant, volume: 213.3K)<br><br>**Deep Insights**<br>- **Overall** has a drop because of {dimension_name}, 19.28% to 19.64% (1.82% increase, volume impacted:457.3K)<br>- **HF-INTL** shows a decreases because of drop because of {dimension_name}, 19.28% to 19.64% (1.82% increase, volume impacted:457.3K) and drop because in the below markets<br>- GB: 36.05% to 38.45% (6.64% increase, volume impacted:121.7K)<br>| |
# MAGIC ```
# MAGIC
# MAGIC ### Important Notes
# MAGIC - **Always use `-` for bullet points in Markdown, never use unicode bullets**
# MAGIC - Consolidate insights for the same market/metric combination
# MAGIC - Focus on high significance scores (typically 4-10)
# MAGIC - Include both positive and negative changes
# MAGIC - Ensure readability by grouping related insights
# MAGIC - When using bullet points in table cells, start with `-` followed by a space
# MAGIC
# MAGIC ### Current Week Template
# MAGIC current week: YYYY-WXX
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Prompt 1

# COMMAND ----------

# MAGIC %md
# MAGIC Begin with a concise checklist (3-7 bullets) of what you will do; keep items conceptual, not implementation-level. Read `REPORT_PROMPT.md` thoroughly to understand requirements. Summarize the key points from `detailed_summary.txt`. Compile these key points into a steering analysis document titled `WXX_steering.md`. After compiling the document, validate in 1-2 lines that all summary key points are present and the requirements from `REPORT_PROMPT.md` are addressed before finishing.

# COMMAND ----------

# %md
# Read REPORT_PROMPT.md 

# Create an analysis document for the following metric:
# 1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess

# List of reporting clusters:
# ['Overall', 'HF-NA', 'HF-INTL', 'US-HF', 'RTE', 'WL']

# Use the below TO DO list for each metric list
# 1) Create a metric analysis summary document in the metric folder
# 2) Analyse Overall folder
# 3) Add analysis summary from Overall folder metric document folder
# 4) Analyse HF-NA folder
# 5) Add analysis summary from HF-NA folder metric document folder
# 6) Analyse HF-INTL folder
# 7) Add analysis summary from HF-INTL folder metric document
# 8) Analyse US-HF folder
# 9) Add analysis summary from US-HF folder metric document
# 10) Analyse RTE folder
# 11) Add analysis summary from RTE folder metric document
# 12) Analyse WL folder
# 13) Add analysis summary from WL folder metric document

# Task for each reporting folder:
# a) Read level_1 data for overall insights, and level_2 for granular insights about business units and dimensions
# b) Update metric_summary.md in metric folder using insights from each reporting cluster. Important: Update this document before moving on to next reporting cluster folder

# Additional instructions to follow:
# - go to the metric folder, create a metric analysis summary document, list all the 5 reporting cluster folder
# - then for every reporting cluster folder, create a analysis summary:
# by reading level_1 data for overall insights, and level_2 for granular insights about business units and dimensions (to do: read 3 files in every reporting cluster folder)
# - Format the metrics properly while writing the analysis report, make it percentages
# - append the reporting cluster analysis in analysis report in metric folder
# - go to the next reporting folder
# - for every file that has been read, print the number of lines in the file, perform a checks to see if the entire file has been read, if the entire file is not read, read the entire file, once the file is read fully, confirm it by stating "file is read completely". In the end, you should have 15 files for each metric, so 195 files read
# - combine insights and put in the metric folder as a md file
# - Important: dont read partial files, read the entire document, if the file is big, spilt into multiple  documents and read it  

# COMMAND ----------

# %md
# Read REPORT_PROMPT.md 

# Read all the summary document under each metric folder and merge them to form one consolidated steering report.

# list of metric folder:
# [
#        '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
#        '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 2_SelectToSuccess',
#        '1_Activation (Paid + Referrals) - 1_Checkout Funnel (backend) - 1_PaymentPageVisitToSuccess',
#        '1_Activation (Paid + Referrals) - 2_Voucher Fraud - 1_Total Duplicate Rate',
#        '1_Activation (Paid + Referrals) - 2_Voucher Fraud - 2_Total Duplicate Block Rate',
#        '1_Activation (Paid + Referrals) - 3_Payment Fraud - 1_Payment Fraud Block Rate',
#        '2_Reactivations - 1_ReactivationFunnel - 1_ReactivationRate',
#        '3_Active - 1_1_Overall Total Box Candidates - 2_PreDunningAR',
#        '3_Active - 1_2_Loyalty: LL0 (Initial charges) - 2_PreDunningAR',
#        '3_Active - 1_3_Loyalty: LL0 and LL1+ (Recurring charges) - 2_PreDunningAR',
#        '3_Active - 2_1_Boxes Shipped - 0_ShipRate',
#        '3_Active - 2_1_Boxes Shipped - 1_RecoveryW0',
#        '3_Active - 2_2_Boxes Shipped - 12wk lag - 2_Recovery_12wkCohort',
#        '3_Active - 2_2_Boxes Shipped - 12wk lag - 3_DunningAvgNetProfit_12wkCohort'
# ]

# tasks to do:
# - Create a p0 steering analysis document in the steering folder
# - Read the summary document from 14 individual metric document folders and paste summarised version in p0 steering analysis document
# - Save the p0 steering analysis document in steering folder

# Create a TODO list for the above task to keep track of it

# Important note: after every metric folder, paste summarised version in p0 steering analysis document

# Then once all the metric are completed, find patterns and sumarise the document using REPORT_PROMPT.md 