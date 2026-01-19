-- Check if xbrand metrics exist in simplified_duplicate_dashboard table
SELECT 
  COUNT(*) as total_rows,
  SUM(spider_xbrand_match) as total_spider_xbrand_match,
  SUM(spider_xbrand_duplicate_at_pre_checkout) as total_spider_xbrand_pre_checkout,
  SUM(spider_xbrand_duplicate_overall) as total_spider_xbrand_overall,
  SUM(prod_xbrand_duplicate_at_pre_checkout) as total_prod_xbrand_pre_checkout,
  SUM(prod_xbrand_duplicate_overall) as total_prod_xbrand_overall
FROM payments_hf.simplified_duplicate_dashboard;

-- Sample rows with xbrand matches
SELECT 
  business_unit,
  checkout_date,
  spider_xbrand_match,
  spider_xbrand_duplicate_at_pre_checkout,
  spider_xbrand_duplicate_overall,
  prod_xbrand_duplicate_at_pre_checkout,
  prod_xbrand_duplicate_overall
FROM payments_hf.simplified_duplicate_dashboard
WHERE spider_xbrand_match > 0
  OR spider_xbrand_duplicate_at_pre_checkout > 0
  OR prod_xbrand_duplicate_at_pre_checkout > 0
LIMIT 20;

