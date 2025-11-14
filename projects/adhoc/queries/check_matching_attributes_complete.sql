-- Complete query to check matching_attributes values and identify xbrand matches
-- Run this directly in Databricks SQL or via the query_util script

-- Part 1: Sample records with matching_attributes
SELECT 
  value.details.business_unit,
  cast(value.details.customer_id as bigint) as customer_id,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') as parent_id,
  ARRAY_DISTINCT(
    FLATTEN(
      TRANSFORM(
        FROM_JSON(
          value.details.raw_payload,
          'struct<parent_ids_with_checkout_success:array<struct<matching_attributes:array<struct<attribute_name:string>>>>>'
        ).parent_ids_with_checkout_success,
        x -> TRANSFORM(x.matching_attributes, y -> y.attribute_name)
      )
    )
  ) AS matching_attributes,
  array_contains(
    ARRAY_DISTINCT(
      FLATTEN(
        TRANSFORM(
          FROM_JSON(
            value.details.raw_payload,
            'struct<parent_ids_with_checkout_success:array<struct<matching_attributes:array<struct<attribute_name:string>>>>>'
          ).parent_ids_with_checkout_success,
          x -> TRANSFORM(x.matching_attributes, y -> y.attribute_name)
        )
      )
    ),
    'xbrand'
  ) as has_xbrand,
  coalesce(
    array_contains(
      ARRAY_DISTINCT(
        FLATTEN(
          TRANSFORM(
            FROM_JSON(
              value.details.raw_payload,
              'struct<parent_ids_with_checkout_success:array<struct<matching_attributes:array<struct<attribute_name:string>>>>>'
            ).parent_ids_with_checkout_success,
            x -> TRANSFORM(x.matching_attributes, y -> y.attribute_name)
          )
        )
      ),
      'xbrand'
    ),
    false
  ) as is_xbrand_match
FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
WHERE 
  1=1
  AND get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
  AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
LIMIT 50;

