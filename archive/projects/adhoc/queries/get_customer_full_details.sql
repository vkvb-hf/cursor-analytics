-- Extract all information for specific customer from spider logs
-- Customer: AO, ID: 360138
SELECT 
  value.details.business_unit,
  cast(value.details.customer_id as bigint) as customer_id,
  cast(timestamp / 1000.0 as timestamp) as event_timestamp,
  
  -- Parent information - extract all parents
  TRANSFORM(
    FROM_JSON(
      value.details.raw_payload,
      'struct<parent_ids_with_checkout_success:array<struct<id:string,degree:string,matching_attributes:array<struct<attribute_name:string>>>>>'
    ).parent_ids_with_checkout_success,
    x -> struct(
      x.id as parent_id,
      x.degree as degree,
      split(split(x.id, ':')[1], '_')[0] as parent_business_unit,
      split(split(x.id, ':')[1], '_')[1] as parent_uuid,
      x.matching_attributes as matching_attributes
    )
  ) as all_parents,
  
  -- Individual parent details (first 3)
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') as parent_0_id,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].degree') as parent_0_degree,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[1].id') as parent_1_id,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[1].degree') as parent_1_degree,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[2].id') as parent_2_id,
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[2].degree') as parent_2_degree,
  
  -- All degrees array
  TRANSFORM(
    FROM_JSON(
      value.details.raw_payload,
      'struct<parent_ids_with_checkout_success:array<struct<degree:string>>>'
    ).parent_ids_with_checkout_success,
    x -> x.degree
  ) as all_degrees,
  
  -- Other key fields from raw_payload
  get_json_object(value.details.raw_payload, '$.voucher_fraud_decision') as voucher_fraud_decision,
  get_json_object(value.details.raw_payload, '$.reason') as reason,
  get_json_object(value.details.raw_payload, '$.experiment_group') as experiment_group,
  
  -- Matching attributes (flattened)
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
  
  -- Top-level matching_attributes if it exists
  get_json_object(value.details.raw_payload, '$.matching_attributes') as matching_attributes_top_level,
  
  -- Full raw_payload (for complete inspection)
  value.details.raw_payload as raw_payload_full
  
FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
WHERE 
  value.details.business_unit = 'AO'
  AND cast(value.details.customer_id as bigint) = 360138
ORDER BY 
  cast(timestamp / 1000.0 as timestamp) DESC;

