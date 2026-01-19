-- Check if customers can have both direct (first) and xbrand (second) matches
WITH spider_data AS (
  SELECT 
    value.details.business_unit,
    cast(value.details.customer_id as bigint) as customer_id,
    get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree') as parent_0_degree,
    get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[1].degree') as parent_1_degree,
    get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[2].degree') as parent_2_degree,
    -- Check if has both first and second degree
    CASE 
      WHEN get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree') = 'first' 
        AND (get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[1].degree') = 'second'
          OR get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[2].degree') = 'second')
      THEN true
      WHEN get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree') = 'second'
        AND (get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[1].degree') = 'first'
          OR get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[2].degree') = 'first')
      THEN true
      ELSE false
    END as has_both_first_and_second
  FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
  WHERE 
    get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
    AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
)
SELECT 
  COUNT(*) as total_records,
  COUNT(CASE WHEN parent_0_degree = 'first' THEN 1 END) as has_first_degree_only,
  COUNT(CASE WHEN parent_0_degree = 'second' THEN 1 END) as has_second_degree_only,
  COUNT(CASE WHEN has_both_first_and_second THEN 1 END) as has_both_degrees,
  COUNT(CASE WHEN parent_0_degree = 'first' AND parent_1_degree = 'second' THEN 1 END) as first_then_second,
  COUNT(CASE WHEN parent_0_degree = 'second' AND parent_1_degree = 'first' THEN 1 END) as second_then_first,
  ROUND(100.0 * COUNT(CASE WHEN has_both_first_and_second THEN 1 END) / COUNT(*), 2) as pct_with_both
FROM spider_data;

