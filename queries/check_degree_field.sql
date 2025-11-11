-- Check the degree field in parent_ids_with_checkout_success
-- degree='first' = direct match, degree='second' = cross-brand match

SELECT 
  value.details.business_unit,
  cast(value.details.customer_id as bigint) as customer_id,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') as parent_id,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree') as first_parent_degree,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[1].degree') as second_parent_degree,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[2].degree') as third_parent_degree,
  -- Check if any parent has degree='second' (cross-brand)
  CASE 
    WHEN get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree') = 'second' THEN true
    WHEN get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[1].degree') = 'second' THEN true
    WHEN get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[2].degree') = 'second' THEN true
    ELSE false
  END as has_second_degree,
  -- Get all degrees from the array
  FROM_JSON(
    value.details.raw_payload,
    'struct<parent_ids_with_checkout_success:array<struct<degree:string>>>'
  ).parent_ids_with_checkout_success as parent_degrees_array
FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
WHERE 
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
  AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
LIMIT 50;

