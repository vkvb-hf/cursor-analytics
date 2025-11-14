-- Sample records with both first and second degree matches
SELECT 
  value.details.business_unit,
  cast(value.details.customer_id as bigint) as customer_id,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') as parent_0_id,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree') as parent_0_degree,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[1].id') as parent_1_id,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[1].degree') as parent_1_degree,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[2].id') as parent_2_id,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[2].degree') as parent_2_degree
FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
WHERE 
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
  AND (
    (get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree') = 'first' 
     AND (get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[1].degree') = 'second'
       OR get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[2].degree') = 'second'))
    OR
    (get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree') = 'second'
     AND (get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[1].degree') = 'first'
       OR get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[2].degree') = 'first'))
  )
LIMIT 20;

