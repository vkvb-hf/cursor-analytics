-- Query to identify duplicates that were blocked in first attempts and then converted at full price
-- Uses checkout_backend_funnel table
-- Aggregated at customer X date level

SELECT
  cbf.country,
  cbf.customer_id,
  cbf.event_date,
  cbf.event_fs_blocked_voucher_abuse,
  cbf.event_fs_blocked,
  cbf.event_checkout_success,
  cbf.any_fs_payload.flag_any_blocked AS flag_any_blocked,
  cbf.fraudservice_last_payload.voucher_code AS voucher_code,
  CASE 
    WHEN cbf.fraudservice_last_payload.voucher_code IS NULL 
      OR cbf.fraudservice_last_payload.voucher_code = ''
    THEN 1 
    ELSE 0 
  END AS is_full_price,
  -- Count customers: flag_any_blocked = 1, then event_fs_blocked = 0, then event_checkout_success = 1
  CASE 
    WHEN cbf.any_fs_payload.flag_any_blocked = 1 
      AND cbf.event_fs_blocked = 0 
      AND cbf.event_checkout_success = 1 
    THEN 1 
    ELSE 0 
  END AS blocked_then_succeeded
FROM
  payments_hf.checkout_funnel_backend cbf
WHERE
  cbf.event_checkout_attempt = 1
  AND cbf.any_fs_payload.flag_any_blocked = 1
ORDER BY
  cbf.country,
  cbf.customer_id,
  cbf.event_date

