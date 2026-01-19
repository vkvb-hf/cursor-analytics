-- Test xbrand detection using degree field
SELECT 
  value.details.business_unit,
  cast(value.details.customer_id as bigint) as customer_id,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') as parent_id,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree') as parent_degree,
  -- Test xbrand detection
  coalesce(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree') = 'second', false) as is_xbrand_match,
  CASE 
    WHEN get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree') = 'second' THEN 'CROSS-BRAND'
    WHEN get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree') = 'first' THEN 'SAME-BRAND'
    ELSE 'UNKNOWN'
  END as match_type
FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
WHERE 
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
  AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
ORDER BY is_xbrand_match DESC, business_unit, customer_id
LIMIT 50;

-- Summary of degree distribution
SELECT 
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree') as parent_degree,
  COUNT(*) as match_count,
  COUNT(DISTINCT value.details.business_unit) as distinct_business_units,
  ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) as percentage
FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
WHERE 
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
  AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
GROUP BY get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree')
ORDER BY match_count DESC;

