-- Clean sample records showing different degree patterns
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
        x.degree as degree,
        split(split(x.id, ':')[1], '_')[0] as parent_bu
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
)
SELECT 
  business_unit as customer_bu,
  customer_id,
  pattern_type,
  size(all_parents) as total_parents,
  size(FILTER(all_degrees, x -> x = 'first')) as first_degree_count,
  size(FILTER(all_degrees, x -> x = 'second')) as second_degree_count,
  all_degrees,
  -- Show parent details in a cleaner format
  all_parents[0].parent_id as parent_1_id,
  all_parents[0].degree as parent_1_degree,
  all_parents[0].parent_bu as parent_1_bu,
  CASE WHEN size(all_parents) > 1 THEN all_parents[1].parent_id ELSE NULL END as parent_2_id,
  CASE WHEN size(all_parents) > 1 THEN all_parents[1].degree ELSE NULL END as parent_2_degree,
  CASE WHEN size(all_parents) > 1 THEN all_parents[1].parent_bu ELSE NULL END as parent_2_bu,
  CASE WHEN size(all_parents) > 2 THEN all_parents[2].parent_id ELSE NULL END as parent_3_id,
  CASE WHEN size(all_parents) > 2 THEN all_parents[2].degree ELSE NULL END as parent_3_degree,
  CASE WHEN size(all_parents) > 2 THEN all_parents[2].parent_bu ELSE NULL END as parent_3_bu
FROM spider_data
WHERE pattern_type IN ('has_both', 'only_first', 'only_second')
ORDER BY 
  CASE pattern_type
    WHEN 'has_both' THEN 1
    WHEN 'only_second' THEN 2
    WHEN 'only_first' THEN 3
  END,
  business_unit,
  customer_id
LIMIT 30;

