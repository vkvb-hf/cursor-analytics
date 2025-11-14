-- Check if xbrand matches are present in simplified duplicate dashboard
-- First check the source table (checkout_customer_actuals) which has is_xbrand_match

SELECT 
  COUNT(*) as total_records,
  COUNT(CASE WHEN COALESCE(is_xbrand_match, FALSE) THEN 1 END) as xbrand_match_count,
  ROUND(100.0 * COUNT(CASE WHEN COALESCE(is_xbrand_match, FALSE) THEN 1 END) / COUNT(*), 2) as xbrand_percentage,
  COUNT(CASE WHEN COALESCE(is_checkout_duplicate, FALSE) AND COALESCE(is_xbrand_match, FALSE) THEN 1 END) as checkout_xbrand_count,
  COUNT(CASE WHEN COALESCE(is_inhouse_duplicate, FALSE) AND COALESCE(is_xbrand_match, FALSE) THEN 1 END) as spider_xbrand_count
FROM payments_hf.checkout_customer_actuals
WHERE is_actual = true
  AND (COALESCE(is_checkout_duplicate, FALSE) OR COALESCE(is_inhouse_duplicate, FALSE));

-- Sample records with xbrand matches
SELECT 
  business_unit,
  customer_id,
  checkout_date,
  COALESCE(is_xbrand_match, FALSE) as is_xbrand_match,
  COALESCE(is_checkout_duplicate, FALSE) as is_checkout_duplicate,
  COALESCE(is_inhouse_duplicate, FALSE) as is_inhouse_duplicate,
  decisions.spider_matching_attributes
FROM payments_hf.checkout_customer_actuals
WHERE is_actual = true
  AND COALESCE(is_xbrand_match, FALSE) = true
LIMIT 20;

