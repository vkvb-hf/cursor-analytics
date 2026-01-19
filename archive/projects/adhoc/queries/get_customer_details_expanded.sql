-- Extract all information for specific customer from spider logs with expanded parent details
-- Customer: AO, ID: 360138
WITH customer_data AS (
  SELECT 
    value.details.business_unit,
    cast(value.details.customer_id as bigint) as customer_id,
    cast(timestamp / 1000.0 as timestamp) as event_timestamp,
    value.details.raw_payload as raw_payload,
    
    -- Extract all parents with full details
    FROM_JSON(
      value.details.raw_payload,
      'struct<parent_ids_with_checkout_success:array<struct<id:string,degree:string,matching_attributes:array<struct<attribute_name:string>>>>>'
    ).parent_ids_with_checkout_success as parent_array,
    
    -- Other key fields
    get_json_object(value.details.raw_payload, '$.voucher_fraud_decision') as voucher_fraud_decision,
    get_json_object(value.details.raw_payload, '$.reason') as reason,
    get_json_object(value.details.raw_payload, '$.experiment_group') as experiment_group,
    get_json_object(value.details.raw_payload, '$.matching_attributes') as matching_attributes_top_level
    
  FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
  WHERE 
    value.details.business_unit = 'AO'
    AND cast(value.details.customer_id as bigint) = 360138
)
SELECT 
  business_unit,
  customer_id,
  event_timestamp,
  voucher_fraud_decision,
  reason,
  experiment_group,
  matching_attributes_top_level,
  size(parent_array) as total_parents,
  -- Show each parent with index
  parent_array[0].id as parent_1_id,
  parent_array[0].degree as parent_1_degree,
  split(split(parent_array[0].id, ':')[1], '_')[0] as parent_1_bu,
  split(split(parent_array[0].id, ':')[1], '_')[1] as parent_1_uuid,
  parent_array[0].matching_attributes as parent_1_matching_attrs,
  CASE WHEN size(parent_array) > 1 THEN parent_array[1].id ELSE NULL END as parent_2_id,
  CASE WHEN size(parent_array) > 1 THEN parent_array[1].degree ELSE NULL END as parent_2_degree,
  CASE WHEN size(parent_array) > 1 THEN split(split(parent_array[1].id, ':')[1], '_')[0] ELSE NULL END as parent_2_bu,
  CASE WHEN size(parent_array) > 1 THEN split(split(parent_array[1].id, ':')[1], '_')[1] ELSE NULL END as parent_2_uuid,
  CASE WHEN size(parent_array) > 1 THEN parent_array[1].matching_attributes ELSE NULL END as parent_2_matching_attrs,
  CASE WHEN size(parent_array) > 2 THEN parent_array[2].id ELSE NULL END as parent_3_id,
  CASE WHEN size(parent_array) > 2 THEN parent_array[2].degree ELSE NULL END as parent_3_degree,
  CASE WHEN size(parent_array) > 2 THEN split(split(parent_array[2].id, ':')[1], '_')[0] ELSE NULL END as parent_3_bu,
  CASE WHEN size(parent_array) > 2 THEN split(split(parent_array[2].id, ':')[1], '_')[1] ELSE NULL END as parent_3_uuid,
  CASE WHEN size(parent_array) > 2 THEN parent_array[2].matching_attributes ELSE NULL END as parent_3_matching_attrs,
  -- All degrees
  TRANSFORM(parent_array, x -> x.degree) as all_degrees,
  -- Full raw payload
  raw_payload
FROM customer_data
ORDER BY event_timestamp DESC;

