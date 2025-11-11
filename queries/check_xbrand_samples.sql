-- Sample records with xbrand matches from checkout_customer_actuals
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

