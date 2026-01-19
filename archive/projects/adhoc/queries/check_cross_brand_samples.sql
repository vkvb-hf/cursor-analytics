-- Check raw_payload for cross-brand matches - Sample records
-- Examine the parent_id structure and compare business units

WITH spider_raw AS (
  SELECT 
    value.details.business_unit as child_business_unit,
    cast(value.details.customer_id as bigint) as customer_id,
    get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') as parent_id_full,
    -- Extract business_unit from parent_id format: "customer:US_uuid" -> "US"
    split(
      split(
        get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id'), ':'
      )[1], '_'
    )[0] as parent_business_unit_from_id,
    split(
      get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id'), ':'
    )[1] as parent_node,
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
    get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
    AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
),
spider_with_parent AS (
  SELECT 
    s.*,
    split(s.parent_node, '_')[1] as parent_uuid,
    c.business_unit as parent_business_unit_actual,
    c.id_customer as parent_id_actual,
    CASE 
      WHEN s.parent_business_unit_from_id IS NOT NULL 
        AND s.parent_business_unit_from_id != s.child_business_unit 
      THEN true
      WHEN c.business_unit IS NOT NULL 
        AND c.business_unit != s.child_business_unit 
      THEN true
      ELSE false
    END as is_cross_brand_match
  FROM spider_raw s
  LEFT JOIN dl_bob_live_non_pii.customer c
    ON c.uuid = split(s.parent_node, '_')[1]
  WHERE s.parent_node IS NOT NULL
)
SELECT 
  child_business_unit,
  customer_id,
  parent_id_full,
  parent_business_unit_from_id,
  parent_business_unit_actual,
  is_cross_brand_match,
  matching_attributes,
  CASE 
    WHEN is_cross_brand_match THEN 'CROSS-BRAND'
    ELSE 'SAME-BRAND'
  END as match_type
FROM spider_with_parent
ORDER BY is_cross_brand_match DESC, child_business_unit, customer_id
LIMIT 100;

