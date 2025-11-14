-- Sample records showing different degree patterns with customer and parent details
WITH spider_data AS (
  SELECT 
    value.details.business_unit,
    cast(value.details.customer_id as bigint) as customer_id,
    -- Extract all parent info
    TRANSFORM(
      FROM_JSON(
        value.details.raw_payload,
        'struct<parent_ids_with_checkout_success:array<struct<id:string,degree:string>>>'
      ).parent_ids_with_checkout_success,
      x -> struct(
        x.id as parent_id,
        x.degree as degree
      )
    ) as all_parents,
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
    END as pattern_type
  FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
  WHERE 
    get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
    AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
),
-- Flatten to show each parent separately
flattened AS (
  SELECT 
    business_unit,
    customer_id,
    pattern_type,
    all_degrees,
    size(all_parents) as parent_count,
    parent_info.parent_id,
    parent_info.degree,
    row_number() OVER (PARTITION BY business_unit, customer_id ORDER BY parent_info.parent_id) as parent_index
  FROM spider_data
  LATERAL VIEW POSEXPLODE(all_parents) AS pos, parent_info
)
SELECT 
  business_unit,
  customer_id,
  pattern_type,
  parent_count,
  all_degrees,
  parent_index,
  parent_id,
  degree,
  -- Extract business unit from parent_id (format: customer:BU_uuid)
  split(split(parent_id, ':')[1], '_')[0] as parent_business_unit
FROM flattened
WHERE pattern_type IN ('has_both', 'only_first', 'only_second')
ORDER BY 
  CASE pattern_type
    WHEN 'has_both' THEN 1
    WHEN 'only_second' THEN 2
    WHEN 'only_first' THEN 3
  END,
  business_unit,
  customer_id,
  parent_index
LIMIT 50;

