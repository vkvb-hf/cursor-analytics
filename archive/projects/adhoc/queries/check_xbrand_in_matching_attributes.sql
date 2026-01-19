-- Check if 'xbrand' appears in matching_attributes from spider logs
-- This query checks the raw spider logs to see what values appear in matching_attributes

WITH spider_sample AS (
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
    get_json_object(value.details.raw_payload, '$.matching_attributes') AS matching_attributes_raw_json
  FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/`
  WHERE 
    cast(timestamp / 1000.0 as timestamp) >= current_timestamp() - INTERVAL 7 DAYS
    AND get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
    AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
)
SELECT 
  business_unit,
  customer_id,
  matching_attributes,
  array_contains(matching_attributes, 'xbrand') as has_xbrand,
  array_contains(matching_attributes, 'cross_brand') as has_cross_brand,
  array_contains(matching_attributes, 'crossbrand') as has_crossbrand,
  size(matching_attributes) as attr_count,
  matching_attributes_raw_json
FROM spider_sample
WHERE matching_attributes IS NOT NULL
  AND size(matching_attributes) > 0
ORDER BY size(matching_attributes) DESC
LIMIT 50;

-- Also check distinct attribute names to see what values actually exist
WITH spider_attributes AS (
  SELECT 
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
    ) AS matching_attributes
  FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/`
  WHERE 
    cast(timestamp / 1000.0 as timestamp) >= current_timestamp() - INTERVAL 7 DAYS
    AND get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
    AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
),
flattened_attrs AS (
  SELECT 
    explode(matching_attributes) as attr_name
  FROM spider_attributes
  WHERE matching_attributes IS NOT NULL
    AND size(matching_attributes) > 0
)
SELECT 
  attr_name,
  COUNT(*) as occurrence_count
FROM flattened_attrs
GROUP BY attr_name
ORDER BY occurrence_count DESC;

