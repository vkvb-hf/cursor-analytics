-- Sample customers showing degree information
SELECT 
  value.details.business_unit,
  cast(value.details.customer_id as bigint) as customer_id,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') as parent_0_id,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree') as parent_0_degree,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[1].id') as parent_1_id,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[1].degree') as parent_1_degree,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[2].id') as parent_2_id,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[2].degree') as parent_2_degree,
  -- Extract all degrees
  TRANSFORM(
    FROM_JSON(
      value.details.raw_payload,
      'struct<parent_ids_with_checkout_success:array<struct<degree:string>>>'
    ).parent_ids_with_checkout_success,
    x -> x.degree
  ) as all_degrees,
  -- Classification
  CASE 
    WHEN ARRAY_CONTAINS(
      TRANSFORM(
        FROM_JSON(
          value.details.raw_payload,
          'struct<parent_ids_with_checkout_success:array<struct<degree:string>>>'
        ).parent_ids_with_checkout_success,
        x -> x.degree
      ),
      'first'
    ) AND ARRAY_CONTAINS(
      TRANSFORM(
        FROM_JSON(
          value.details.raw_payload,
          'struct<parent_ids_with_checkout_success:array<struct<degree:string>>>'
        ).parent_ids_with_checkout_success,
        x -> x.degree
      ),
      'second'
    ) THEN 'has_both'
    WHEN ARRAY_CONTAINS(
      TRANSFORM(
        FROM_JSON(
          value.details.raw_payload,
          'struct<parent_ids_with_checkout_success:array<struct<degree:string>>>'
        ).parent_ids_with_checkout_success,
        x -> x.degree
      ),
      'first'
    ) THEN 'only_first'
    WHEN ARRAY_CONTAINS(
      TRANSFORM(
        FROM_JSON(
          value.details.raw_payload,
          'struct<parent_ids_with_checkout_success:array<struct<degree:string>>>'
        ).parent_ids_with_checkout_success,
        x -> x.degree
      ),
      'second'
    ) THEN 'only_second'
    ELSE 'unknown'
  END as classification
FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
WHERE 
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
  AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
ORDER BY 
  CASE 
    WHEN ARRAY_CONTAINS(
      TRANSFORM(
        FROM_JSON(
          value.details.raw_payload,
          'struct<parent_ids_with_checkout_success:array<struct<degree:string>>>'
        ).parent_ids_with_checkout_success,
        x -> x.degree
      ),
      'first'
    ) AND ARRAY_CONTAINS(
      TRANSFORM(
        FROM_JSON(
          value.details.raw_payload,
          'struct<parent_ids_with_checkout_success:array<struct<degree:string>>>'
        ).parent_ids_with_checkout_success,
        x -> x.degree
      ),
      'second'
    ) THEN 1
    ELSE 2
  END,
  value.details.business_unit,
  cast(value.details.customer_id as bigint)
LIMIT 30;

