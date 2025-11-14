-- Summary: Count cross-brand vs same-brand matches

WITH spider_raw AS (
  SELECT 
    value.details.business_unit as child_business_unit,
    cast(value.details.customer_id as bigint) as customer_id,
    -- Extract business_unit from parent_id format: "customer:US_uuid" -> "US"
    split(
      split(
        get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id'), ':'
      )[1], '_'
    )[0] as parent_business_unit_from_id,
    split(
      get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id'), ':'
    )[1] as parent_node
  FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
  WHERE 
    get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
    AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
),
spider_with_parent AS (
  SELECT 
    s.*,
    c.business_unit as parent_business_unit_actual,
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
  CASE 
    WHEN is_cross_brand_match THEN 'CROSS-BRAND'
    ELSE 'SAME-BRAND'
  END as match_type,
  COUNT(*) as match_count,
  COUNT(DISTINCT child_business_unit) as distinct_child_business_units,
  COUNT(DISTINCT COALESCE(parent_business_unit_from_id, parent_business_unit_actual)) as distinct_parent_business_units,
  ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) as percentage
FROM spider_with_parent
GROUP BY is_cross_brand_match
ORDER BY match_count DESC;

