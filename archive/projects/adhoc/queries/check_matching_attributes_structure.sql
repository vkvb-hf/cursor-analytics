-- Check the structure of matching_attributes in raw_payload
-- The user mentioned: get_json_object(raw_payload, '$.matching_attributes')
-- Let's check both the nested path and the top-level path

SELECT 
  value.details.business_unit,
  cast(value.details.customer_id as bigint) as customer_id,
  
  -- Current extraction from nested path
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
  ) AS matching_attributes_nested,
  
  -- Top-level matching_attributes (as user mentioned)
  get_json_object(value.details.raw_payload, '$.matching_attributes') AS matching_attributes_top_level,
  
  -- Check if top-level is an array or object
  get_json_object(value.details.raw_payload, '$.matching_attributes[0]') AS matching_attributes_array_first,
  
  -- Full raw_payload structure (limited to see structure)
  get_json_object(value.details.raw_payload, '$') AS raw_payload_full
  
FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/`
WHERE 
  cast(timestamp / 1000.0 as timestamp) >= current_timestamp() - INTERVAL 7 DAYS
  AND get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
  AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
  AND get_json_object(value.details.raw_payload, '$.matching_attributes') IS NOT NULL
LIMIT 20;

-- Check what the top-level matching_attributes contains
SELECT 
  get_json_object(value.details.raw_payload, '$.matching_attributes') AS matching_attributes_raw,
  typeof(get_json_object(value.details.raw_payload, '$.matching_attributes')) AS attr_type
FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/`
WHERE 
  cast(timestamp / 1000.0 as timestamp) >= current_timestamp() - INTERVAL 7 DAYS
  AND get_json_object(value.details.raw_payload, '$.matching_attributes') IS NOT NULL
LIMIT 10;

