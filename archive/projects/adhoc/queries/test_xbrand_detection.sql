-- Test xbrand detection using top-level matching_attributes
SELECT 
  value.details.business_unit,
  cast(value.details.customer_id as bigint) as customer_id,
  get_json_object(value.details.raw_payload, '$.matching_attributes') as matching_attributes_top_level,
  -- Test different methods to check for cross_brand
  get_json_object(value.details.raw_payload, '$.matching_attributes') LIKE '%cross_brand%' as is_xbrand_like,
  contains(get_json_object(value.details.raw_payload, '$.matching_attributes'), 'cross_brand') as is_xbrand_contains,
  CASE 
    WHEN get_json_object(value.details.raw_payload, '$.matching_attributes') IS NOT NULL
      AND get_json_object(value.details.raw_payload, '$.matching_attributes') LIKE '%cross_brand%'
    THEN true
    ELSE false
  END as is_xbrand_case
FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
WHERE 
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
  AND get_json_object(value.details.raw_payload, '$.matching_attributes') IS NOT NULL
LIMIT 10;

