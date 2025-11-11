-- Check the actual format of parent_id to understand the structure
SELECT 
  value.details.business_unit as child_business_unit,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') as parent_id_full,
  split(
    get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id'), ':'
  )[0] as part_after_colon_0,
  split(
    get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id'), ':'
  )[1] as part_after_colon_1,
  split(
    split(
      get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id'), ':'
    )[1], '_'
  )[0] as business_unit_from_parent_id
FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
WHERE 
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
  AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
LIMIT 10;

