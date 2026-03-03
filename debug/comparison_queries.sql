-- SQL queries used for comparison
-- Run these in Databricks to reproduce the analysis

-- Step 1: Raw bu_level data for HF-INTL BUs
CREATE OR REPLACE TABLE hive_metastore.visal_debug.compare_step1_raw AS
SELECT 
    metric_final_name,
    CASE 
        WHEN metric_final_name LIKE '%PaymentPageVisitToSuccess%' THEN 'WORKING'
        ELSE 'BROKEN'
    END as metric_status,
    business_unit,
    current_metric_value_numerator,
    current_metric_value_denominator,
    prev_metric_value_numerator,
    prev_metric_value_denominator
FROM hive_metastore.visal_debug.debug_step3_full
WHERE reporting_cluster = 'bu_level'
  AND business_unit IN ('AT', 'AU', 'BE', 'CH', 'DE', 'DK', 'ES', 'FR', 'GB', 'IE', 'IT', 'LU', 'NL', 'NO', 'NZ', 'SE');

-- Step 2: Calculate ratios and changes
CREATE OR REPLACE TABLE hive_metastore.visal_debug.compare_step2_calculated AS
SELECT 
    *,
    current_metric_value_numerator / current_metric_value_denominator as current_ratio,
    prev_metric_value_numerator / prev_metric_value_denominator as prev_ratio,
    ((current_metric_value_numerator / current_metric_value_denominator) - 
     (prev_metric_value_numerator / prev_metric_value_denominator)) / 
    (prev_metric_value_numerator / prev_metric_value_denominator) * 100 as relative_change_pct,
    ABS(((current_metric_value_numerator / current_metric_value_denominator) - 
         (prev_metric_value_numerator / prev_metric_value_denominator)) / 
        (prev_metric_value_numerator / prev_metric_value_denominator) * 100) as abs_rel_change,
    current_metric_value_denominator * 
    ABS(((current_metric_value_numerator / current_metric_value_denominator) - 
         (prev_metric_value_numerator / prev_metric_value_denominator)) / 
        (prev_metric_value_numerator / prev_metric_value_denominator) * 100) / 100 as volume_impacted
FROM hive_metastore.visal_debug.compare_step1_raw
WHERE prev_metric_value_denominator > 0 AND prev_metric_value_numerator > 0;

-- Step 3: Apply significance filter with thresholds
CREATE OR REPLACE TABLE hive_metastore.visal_debug.compare_step3_filtered AS
SELECT 
    *,
    CASE 
        WHEN metric_status = 'WORKING' THEN 10.0
        WHEN metric_status = 'BROKEN' THEN 2.5
    END as threshold,
    CASE 
        WHEN metric_status = 'WORKING' AND (abs_rel_change >= 10.0 OR volume_impacted > 30) THEN 'PASS'
        WHEN metric_status = 'BROKEN' AND (abs_rel_change >= 2.5 OR volume_impacted > 30) THEN 'PASS'
        ELSE 'FAIL'
    END as filter_result
FROM hive_metastore.visal_debug.compare_step2_calculated;

-- Step 4: Bucket assignment
CREATE OR REPLACE TABLE hive_metastore.visal_debug.compare_step4_bucketed AS
SELECT 
    *,
    CASE 
        WHEN abs_rel_change >= 50 THEN 'HIGH'
        WHEN abs_rel_change >= 20 THEN 'MEDIUM'
        WHEN filter_result = 'PASS' THEN 'LOW'
        ELSE 'NONE'
    END as expected_bucket
FROM hive_metastore.visal_debug.compare_step3_filtered;

-- Summary query
SELECT 
    metric_status,
    COUNT(*) as total_bus,
    SUM(CASE WHEN filter_result = 'PASS' THEN 1 ELSE 0 END) as significant_bus,
    SUM(CASE WHEN expected_bucket = 'HIGH' THEN 1 ELSE 0 END) as high_bucket,
    SUM(CASE WHEN expected_bucket = 'MEDIUM' THEN 1 ELSE 0 END) as medium_bucket,
    SUM(CASE WHEN expected_bucket = 'LOW' THEN 1 ELSE 0 END) as low_bucket,
    SUM(CASE WHEN expected_bucket = 'NONE' THEN 1 ELSE 0 END) as none_bucket
FROM hive_metastore.visal_debug.compare_step4_bucketed
GROUP BY metric_status
ORDER BY metric_status;
