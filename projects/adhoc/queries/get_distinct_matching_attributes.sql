-- Get all distinct attribute names and their occurrence counts
-- This will show us what values actually exist in matching_attributes

WITH spider_data AS (
  SELECT 
    value.details.business_unit,
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
  FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
  WHERE 
    1=1
    AND get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
    AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
),
flattened AS (
  SELECT 
    business_unit,
    explode(matching_attributes) as attr_name
  FROM spider_data
  WHERE matching_attributes IS NOT NULL
    AND size(matching_attributes) > 0
)
SELECT 
  attr_name,
  COUNT(*) as occurrence_count,
  COUNT(DISTINCT business_unit) as distinct_business_units,
  COLLECT_SET(business_unit) as business_units_list
FROM flattened
GROUP BY attr_name
ORDER BY occurrence_count DESC;

