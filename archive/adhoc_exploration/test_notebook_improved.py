# Databricks notebook source
from datetime import datetime, timedelta

# Add workspace path for importing utils
import sys
sys.path.append('/Workspace/Users/aoez@hellofresh.com/local')

# Import parquet utility
from utils.parquet import read_parquet_time_filtered

end_date = datetime.now().date()
start_date = end_date - timedelta(days=30)

read_parquet_time_filtered(
    "s3://hf-dp-shared-proto-s3-sinker-non-pii-raw-live/events/kafka/parquet/topics/public.payment.orchestrator.psp.transaction.v1beta1",
    str(start_date),
    str(end_date + timedelta(days=1)),
).createOrReplaceTempView("kafka_public_payment_orchestrator_psp_transaction_v1beta1")

# COMMAND ----------

# MAGIC %sql
# MAGIC refresh table payments_hf.business_units;
# MAGIC refresh table payments_hf.business_units_view;
# MAGIC select * from kafka_public_payment_orchestrator_psp_transaction_v1beta1 limit 10
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC create
# MAGIC or replace temp view payment_orchestrator_event as with a as (
# MAGIC   SELECT
# MAGIC     -- Convert timestamp from milliseconds to timestamp
# MAGIC     from_unixtime(timestamp / 1000) AS event_timestamp,
# MAGIC     -- Key field (already flat)
# MAGIC     key,
# MAGIC     -- Value fields (flattened)
# MAGIC     value.transaction_id,
# MAGIC     value.merchant_ref,
# MAGIC     concat(
# MAGIC       upper(value.business_unit),
# MAGIC       '_',
# MAGIC       split(value.reference, ':') [1]
# MAGIC     ) as unique_order_nr,
# MAGIC     value.psp_ref,
# MAGIC     -- Provider enum resolved to string
# MAGIC     value.provider AS provider_code,
# MAGIC     CASE
# MAGIC       value.provider
# MAGIC       WHEN 0 THEN 'UNSPECIFIED'
# MAGIC       WHEN 1 THEN 'ADYEN'
# MAGIC       WHEN 2 THEN 'BRAINTREE'
# MAGIC       WHEN 3 THEN 'PROCESSOUT'
# MAGIC       ELSE CONCAT('UNKNOWN_', value.provider)
# MAGIC     END AS provider_name,
# MAGIC     -- Transaction type enum resolved to string
# MAGIC     value.transaction_type AS transaction_type_code,
# MAGIC     CASE
# MAGIC       value.transaction_type
# MAGIC       WHEN 0 THEN 'UNSPECIFIED'
# MAGIC       WHEN 1 THEN 'SYNC'
# MAGIC       WHEN 2 THEN 'ASYNC'
# MAGIC       ELSE CONCAT('UNKNOWN_', value.transaction_type)
# MAGIC     END AS transaction_type_name,
# MAGIC     -- Event enum resolved to string
# MAGIC     value.event AS event_code,
# MAGIC     CASE
# MAGIC       value.event
# MAGIC       WHEN 0 THEN 'UNSPECIFIED'
# MAGIC       WHEN 1 THEN 'CHARGE'
# MAGIC       WHEN 2 THEN 'REFUND'
# MAGIC       ELSE CONCAT('UNKNOWN_', value.event)
# MAGIC     END AS event_name,
# MAGIC     value.raw_request,
# MAGIC     value.raw_response,
# MAGIC     upper(value.business_unit) as business_unit,
# MAGIC     value.op
# MAGIC   FROM
# MAGIC     kafka_public_payment_orchestrator_psp_transaction_v1beta1
# MAGIC ),
# MAGIC b as (
# MAGIC   select
# MAGIC     case
# MAGIC       ------------- MAP PROCESSOUT FIELDS
# MAGIC       ------------------------------
# MAGIC       when provider_name = 'PROCESSOUT' then struct(
# MAGIC         -- split(get_json_object(raw_response, '$.metadata.reference'), ':')[1] as order_nr,
# MAGIC         coalesce(
# MAGIC           cast(
# MAGIC             get_json_object(raw_response, '$.authorized') as boolean
# MAGIC           ),
# MAGIC           false
# MAGIC         ) as authorized,
# MAGIC         get_json_object(raw_response, '$.error_message') as error_message,
# MAGIC         get_json_object(raw_response, '$.metadata.payment_method') as payment_method_raw,
# MAGIC         get_json_object(raw_response, '$.card.iin') as card_bin,
# MAGIC         get_json_object(raw_response, '$.card.last_4_digits') as card_last_4
# MAGIC       ) ------------- MAP ADYEN FIELDS
# MAGIC       ------------------------------
# MAGIC       when provider_name = 'ADYEN' then struct(
# MAGIC         -- split(get_json_object(raw_response, '$.metadata.reference'), ':')[1] as order_nr,
# MAGIC         coalesce(
# MAGIC           cast(
# MAGIC             get_json_object(raw_response, '$.response.resultCode') = 'Authorised'
# MAGIC             or get_json_object(raw_response, '$.response.success') = 'true' as boolean
# MAGIC           ),
# MAGIC           false
# MAGIC         ) as authorized,
# MAGIC         case
# MAGIC           when not coalesce(
# MAGIC             cast(
# MAGIC               get_json_object(raw_response, '$.response.resultCode') = 'Authorised'
# MAGIC               or get_json_object(raw_response, '$.response.success') = 'true' as boolean
# MAGIC             ),
# MAGIC             false
# MAGIC           ) then get_json_object(
# MAGIC             raw_response,
# MAGIC             '$.response.additionalData.refusalReasonRaw'
# MAGIC           )
# MAGIC         end as error_message,
# MAGIC         -- get_json_object(raw_response, '$.error_message') as error_message,
# MAGIC         coalesce(
# MAGIC           case
# MAGIC             when get_json_object(
# MAGIC               raw_response,
# MAGIC               '$.response.additionalData.cardBin'
# MAGIC             ) is not null then 'card'
# MAGIC           end,
# MAGIC           get_json_object(raw_response, '$.response.paymentMethod.type'),
# MAGIC           get_json_object(raw_response, '$.response.paymentMethod'),
# MAGIC           get_json_object(raw_request, '$.paymentMethod.type')
# MAGIC         ) as payment_method_raw,
# MAGIC         get_json_object(
# MAGIC           raw_response,
# MAGIC           '$.response.additionalData.cardBin'
# MAGIC         ) as card_bin,
# MAGIC         get_json_object(
# MAGIC           raw_response,
# MAGIC           '$.response.additionalData.cardSummary'
# MAGIC         ) as card_last_4
# MAGIC       ) ------------- MAP BRAINTREE FIELDS
# MAGIC       ------------------------------
# MAGIC       when provider_name = 'BRAINTREE' then struct(
# MAGIC         -- split(get_json_object(raw_request, '$.customFields.reference'), ':')[1] as order_nr,
# MAGIC         coalesce(
# MAGIC           get_json_object(raw_response, '$.response.Message') in ('submitted_for_settlement', 'settling'),
# MAGIC           false
# MAGIC         ) as authorized,
# MAGIC         case
# MAGIC           when get_json_object(raw_response, '$.response.Message') not in ('submitted_for_settlement', 'settling') then get_json_object(raw_response, '$.response.Message')
# MAGIC         end as error_message,
# MAGIC         get_json_object(
# MAGIC           raw_response,
# MAGIC           '$.response.Transaction.paymentInstrumentType'
# MAGIC         ) as payment_method_raw,
# MAGIC         get_json_object(
# MAGIC           raw_response,
# MAGIC           '$.response.Transaction.creditCard.bin'
# MAGIC         ) as card_bin,
# MAGIC         get_json_object(
# MAGIC           raw_response,
# MAGIC           '$.response.additionalData.cardSummary'
# MAGIC         ) as card_last_4
# MAGIC       )
# MAGIC     end as details,
# MAGIC     -- array_sort(
# MAGIC     --   filter(
# MAGIC     --     array(
# MAGIC     --       case
# MAGIC     --         when get_json_object(raw_response, '$.response.eventCode') = 'REFUND' then 'REFUND_IN_CHARGE'
# MAGIC     --       END,
# MAGIC     --       case
# MAGIC     --         when get_json_object(raw_response, '$.response.Message') like '%Payment method token is invalid%' then 'INVALID_PAYMENT_TOKEN'
# MAGIC     --       END,
# MAGIC     --       case
# MAGIC     --         when get_json_object(raw_response, '$.response.Message') like '%Merchant account does not support payment instrument%' then 'UNSUPPORTED_PAYMENT_INSTRUMENT'
# MAGIC     --       END,
# MAGIC     --       case
# MAGIC     --         when provider_name = 'BRAINTREE'
# MAGIC     --         and coalesce(
# MAGIC     --           get_json_object(raw_response, '$.error'),
# MAGIC     --           get_json_object(raw_response, '$.response.Message'),
# MAGIC     --           get_json_object(raw_response, '$.response.Transaction')
# MAGIC     --         ) is null then 'NULL_RESPONSE'
# MAGIC     --       END
# MAGIC     --     ),
# MAGIC     --     e -> e is not null
# MAGIC     --   )
# MAGIC     -- ) as problems,
# MAGIC     struct(a.*) as base_payload
# MAGIC   from
# MAGIC     a
# MAGIC   where
# MAGIC     event_name = 'CHARGE' -- and provider_name not in ('PROCESSOUT', 'BRAINTREE') -- , 'PROCESSOUT'
# MAGIC     -- and provider_name = 'BRAINTREE'
# MAGIC ),
# MAGIC c as (
# MAGIC   select
# MAGIC     base_payload.*,
# MAGIC     -- base_payload.provider_name,
# MAGIC     -- regexp_extract(base_payload.raw_response, '\\b(\\d{6})\\b', 1) AS extracted_value,
# MAGIC     -- problems,
# MAGIC     case
# MAGIC       when details.payment_method_raw in ('credit_card', 'card') then 'card'
# MAGIC       when details.payment_method_raw in ('apple_pay_card', 'apple_pay') then 'apple_pay'
# MAGIC       when details.payment_method_raw = 'paypal_account' then 'paypal'
# MAGIC       when details.payment_method_raw = 'venmo_account' then 'venmo'
# MAGIC       when details.payment_method_raw = 'sepadirectdebit' then 'sepa'
# MAGIC       when details.payment_method_raw = 'klarna' then 'klarna'
# MAGIC       when details.payment_method_raw = 'ratepay' then 'ratepay'
# MAGIC     end as payment_method,
# MAGIC     details.* -- base_payload.raw_request,
# MAGIC     -- base_payload.raw_response,
# MAGIC   from
# MAGIC     b
# MAGIC )
# MAGIC select
# MAGIC   *
# MAGIC from
# MAGIC   c
# MAGIC

# COMMAND ----------

from utils.staging_writer import save_to_staging
# DBTITLE 1,Write to Staging
save_to_staging(spark.table('payment_orchestrator_event'), 'payment_orchestrator_event')

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace temp view psp_transaction_agg as
# MAGIC with so as (
# MAGIC   select
# MAGIC     business_unit,
# MAGIC     id_sales_order,
# MAGIC     order_nr
# MAGIC   from
# MAGIC     dl_bob_live_non_pii.sales_order so
# MAGIC   where
# MAGIC     year >= 2025),
# MAGIC soi as (
# MAGIC   select
# MAGIC     business_unit,
# MAGIC     fk_sales_order,
# MAGIC     first(delivery_date, true) as delivery_date
# MAGIC   from
# MAGIC     dl_bob_live_non_pii.sales_order_item soi
# MAGIC   where
# MAGIC     year >= 2025
# MAGIC   group by
# MAGIC     business_unit,
# MAGIC     fk_sales_order
# MAGIC ),
# MAGIC f as (
# MAGIC   select
# MAGIC     psp_ref,
# MAGIC     max(struct(event_timestamp as max_event_timestamp, struct(f.*) as payload)) as last_message
# MAGIC   from
# MAGIC     payments_hf_staging.payment_orchestrator_event f
# MAGIC   where
# MAGIC     unique_order_nr is not null
# MAGIC   group by
# MAGIC     psp_ref
# MAGIC ),
# MAGIC f2 as (
# MAGIC   select
# MAGIC     last_message.payload.*
# MAGIC   from
# MAGIC     f
# MAGIC ),
# MAGIC a as (
# MAGIC   select
# MAGIC     first(business_unit, true) as business_unit,
# MAGIC     unique_order_nr,
# MAGIC     min(struct(event_timestamp, struct(f.*) as payload)) as first_attempt,
# MAGIC     max(struct(event_timestamp, struct(f.*) as payload)) as last_attempt,
# MAGIC     count(*) as attempt_count -- provider_name,
# MAGIC   -- payment_method,
# MAGIC   -- count(*)
# MAGIC   from
# MAGIC     f2 f
# MAGIC   group by
# MAGIC     unique_order_nr
# MAGIC ),
# MAGIC b as (
# MAGIC   SELECT
# MAGIC     a.business_unit,
# MAGIC     unique_order_nr,
# MAGIC     soi.delivery_date,
# MAGIC     replace(bob_ui_url_order, '{order_id}', id_sales_order) as bob_ui_order,
# MAGIC     -- First attempt details
# MAGIC     date_trunc('hour', first_attempt.event_timestamp) as first_hour_utc,
# MAGIC     to_utc_timestamp(first_attempt.event_timestamp, bu.timezone) as first_hour_local,
# MAGIC     first_attempt.payload.provider_name as first_provider,
# MAGIC     first_attempt.payload.payment_method as first_payment_method,
# MAGIC     first_attempt.payload.authorized as first_authorized,
# MAGIC     first_attempt.payload.error_message as first_error_message,
# MAGIC     -- Last attempt details
# MAGIC     date_trunc('hour', last_attempt.event_timestamp) as last_hour_utc,
# MAGIC     to_utc_timestamp(last_attempt.event_timestamp, bu.timezone) as last_hour_local,
# MAGIC     last_attempt.payload.provider_name as last_provider,
# MAGIC     last_attempt.payload.payment_method as last_payment_method,
# MAGIC     last_attempt.payload.authorized as last_authorized,
# MAGIC     last_attempt.payload.error_message as last_error_message,
# MAGIC     -- Total attempts
# MAGIC     attempt_count as total_attempts
# MAGIC   FROM
# MAGIC     a
# MAGIC       left join so
# MAGIC         on a.business_unit = so.business_unit
# MAGIC         and split(a.unique_order_nr, '_')[1] = so.order_nr
# MAGIC       left join soi
# MAGIC         on a.business_unit = soi.business_unit
# MAGIC         and soi.fk_sales_order = so.id_sales_order
# MAGIC       left join payments_hf.business_units_view bu
# MAGIC         on a.business_unit = bu.business_unit
# MAGIC ),
# MAGIC agg as (
# MAGIC   select
# MAGIC     business_unit,
# MAGIC     delivery_date,
# MAGIC     left(least(date(first_hour_local), delivery_date), 10) as meal_selection_cutoff,
# MAGIC     first_hour_utc,
# MAGIC     first_provider,
# MAGIC     first_payment_method,
# MAGIC     first_authorized,
# MAGIC     first_error_message,
# MAGIC     last_hour_utc,
# MAGIC     last_provider,
# MAGIC     last_payment_method,
# MAGIC     last_authorized,
# MAGIC     last_error_message,
# MAGIC     total_attempts,
# MAGIC     first(bob_ui_order, true) as sample,
# MAGIC     count(*) as order_count
# MAGIC   from
# MAGIC     b
# MAGIC   group by
# MAGIC     business_unit,
# MAGIC     delivery_date,
# MAGIC     meal_selection_cutoff,
# MAGIC     first_hour_utc,
# MAGIC     first_provider,
# MAGIC     first_payment_method,
# MAGIC     first_authorized,
# MAGIC     first_error_message,
# MAGIC     last_hour_utc,
# MAGIC     last_provider,
# MAGIC     last_payment_method,
# MAGIC     last_authorized,
# MAGIC     last_error_message,
# MAGIC     total_attempts
# MAGIC )
# MAGIC select
# MAGIC   *
# MAGIC from
# MAGIC   agg
# MAGIC

# COMMAND ----------



# COMMAND ----------

import pyspark.sql.functions as F

save_to_staging(
    spark.table("psp_transaction_agg").filter(
        F.col("delivery_date") >= start_date
    ),
    "psp_transaction_agg",
)

# COMMAND ----------

!! pip install tableauserverclient
from utils.tableau_api import TableauApi

workbook_id = '47bbf8ad-c1e9-4d4f-b443-5ad2769567dd'
TableauApi.trigger_extract_refresh(workbook_id=workbook_id)