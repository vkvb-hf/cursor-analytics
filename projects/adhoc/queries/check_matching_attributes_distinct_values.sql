-- Get distinct values of top-level matching_attributes
-- Check for format like "1:cross_brand__2:cross_brand__3:cross_brand"

SELECT 
  get_json_object(value.details.raw_payload, '$.matching_attributes') as matching_attributes_value,
  COUNT(*) as occurrence_count,
  COUNT(DISTINCT value.details.business_unit) as distinct_business_units
FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
WHERE 
  get_json_object(value.details.raw_payload, '$.matching_attributes') IS NOT NULL
  AND length(get_json_object(value.details.raw_payload, '$.matching_attributes')) > 0
GROUP BY get_json_object(value.details.raw_payload, '$.matching_attributes')
ORDER BY occurrence_count DESC
LIMIT 100;

