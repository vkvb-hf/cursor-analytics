-- Check xbrand match counts in checkout_customer_actuals
SELECT 
  COUNT(*) as total_records,
  COUNT(CASE WHEN COALESCE(is_xbrand_match, FALSE) THEN 1 END) as xbrand_match_count,
  ROUND(100.0 * COUNT(CASE WHEN COALESCE(is_xbrand_match, FALSE) THEN 1 END) / COUNT(*), 2) as xbrand_percentage,
  COUNT(CASE WHEN COALESCE(is_checkout_duplicate, FALSE) AND COALESCE(is_xbrand_match, FALSE) THEN 1 END) as checkout_xbrand_count,
  COUNT(CASE WHEN COALESCE(is_inhouse_duplicate, FALSE) AND COALESCE(is_xbrand_match, FALSE) THEN 1 END) as spider_xbrand_count
FROM payments_hf.checkout_customer_actuals
WHERE is_actual = true
  AND (COALESCE(is_checkout_duplicate, FALSE) OR COALESCE(is_inhouse_duplicate, FALSE));

