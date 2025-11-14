-- Summary table of customer counts by degree type
WITH spider_data AS (
  SELECT 
    value.details.business_unit,
    cast(value.details.customer_id as bigint) as customer_id,
    get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree') as parent_0_degree,
    get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[1].degree') as parent_1_degree,
    get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[2].degree') as parent_2_degree,
    -- Extract all degrees from array
    TRANSFORM(
      FROM_JSON(
        value.details.raw_payload,
        'struct<parent_ids_with_checkout_success:array<struct<degree:string>>>'
      ).parent_ids_with_checkout_success,
      x -> x.degree
    ) as all_degrees,
    -- Check if has first degree
    ARRAY_CONTAINS(
      TRANSFORM(
        FROM_JSON(
          value.details.raw_payload,
          'struct<parent_ids_with_checkout_success:array<struct<degree:string>>>'
        ).parent_ids_with_checkout_success,
        x -> x.degree
      ),
      'first'
    ) as has_first,
    -- Check if has second degree
    ARRAY_CONTAINS(
      TRANSFORM(
        FROM_JSON(
          value.details.raw_payload,
          'struct<parent_ids_with_checkout_success:array<struct<degree:string>>>'
        ).parent_ids_with_checkout_success,
        x -> x.degree
      ),
      'second'
    ) as has_second
  FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
  WHERE 
    get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
    AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
)
SELECT 
  COUNT(*) as total_customer_count,
  COUNT(CASE WHEN has_first AND NOT has_second THEN 1 END) as has_only_first_degree,
  COUNT(CASE WHEN has_second AND NOT has_first THEN 1 END) as has_only_second_degree,
  COUNT(CASE WHEN has_first AND has_second THEN 1 END) as has_both_degrees,
  COUNT(CASE WHEN has_first AND has_second AND parent_0_degree = 'second' THEN 1 END) as has_both_second_in_element_0,
  COUNT(CASE WHEN has_first AND has_second AND parent_0_degree = 'first' THEN 1 END) as has_both_first_in_element_0,
  ROUND(100.0 * COUNT(CASE WHEN has_first AND NOT has_second THEN 1 END) / COUNT(*), 2) as pct_only_first,
  ROUND(100.0 * COUNT(CASE WHEN has_second AND NOT has_first THEN 1 END) / COUNT(*), 2) as pct_only_second,
  ROUND(100.0 * COUNT(CASE WHEN has_first AND has_second THEN 1 END) / COUNT(*), 2) as pct_both
FROM spider_data;

