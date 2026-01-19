-- Check actual values in matching_attributes from spider logs
-- This will show us what attribute names actually exist

WITH spider_data AS (
  SELECT 
    value.details.business_unit,
    cast(value.details.customer_id as bigint) as customer_id,
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
flattened AS (
  SELECT 
    business_unit,
    customer_id,
    explode(matching_attributes) as attr_name
  FROM spider_data
  WHERE matching_attributes IS NOT NULL
    AND size(matching_attributes) > 0
)
SELECT 
  attr_name,
  COUNT(*) as occurrence_count,
  COUNT(DISTINCT business_unit) as distinct_business_units
FROM flattened
GROUP BY attr_name
ORDER BY occurrence_count DESC;

