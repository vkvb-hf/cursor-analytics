-- Sample records from adyen_ml_test_cust_data where customer_uuid is not null
SELECT *
FROM payments_hf.adyen_ml_test_cust_data
WHERE customer_uuid IS NOT NULL
LIMIT 10


