-- Test query for run_sql_file.py
SELECT 
    country,
    COUNT(*) as order_count,
    SUM(count_chargebacks) as total_chargebacks
FROM payments_hf.chargebacks_dashboard
WHERE country IN ('US', 'GB', 'DE', 'NL', 'CA')
GROUP BY country
ORDER BY total_chargebacks DESC
LIMIT 10

