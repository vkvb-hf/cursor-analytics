# Databricks notebook source
# MAGIC %md
# MAGIC # Diagnose event_date = '2025-11-03' Issue
# MAGIC 
# MAGIC This notebook traces where event_date = '2025-11-03' data comes from when running for 2025-11-04

# COMMAND ----------

import time
from datetime import date, datetime, timedelta
from typing import Optional, List, Union
from pyspark.sql import DataFrame

# COMMAND ----------

# MAGIC %md
# MAGIC ## Configuration

# COMMAND ----------

# Test configuration - running for Nov 4th only
test_start_date = "2025-11-04"
test_end_date = "2025-11-04"

print("=" * 100)
print("DIAGNOSTIC CONFIGURATION")
print("=" * 100)
print(f"Start Date: {test_start_date}")
print(f"End Date: {test_end_date}")
print(f"Looking for: event_date = '2025-11-03' (should NOT exist)")
print("=" * 100)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Check Temp Tables for Nov 3 Data

# COMMAND ----------

# Check if temp tables exist and contain Nov 3 data
# Note: In real scenario, these would be created by create_parquet_tables
# For diagnostic purposes, we'll check what dates are in the source Parquet files

print("\n" + "=" * 100)
print("STEP 1: Checking source Parquet files for Nov 3 data")
print("=" * 100)

# Check payment method listed
try:
    pm_df = spark.read.parquet(
        "s3://hf-dp-shared-proto-s3-sinker-non-pii-raw-live/events/kafka/"
        "parquet/topics/public.payment.method-listed.v1beta1/year=2025/month=11/day=04"
    )
    
    # Calculate event_date from timestamp
    from pyspark.sql.functions import col, from_unixtime, date as spark_date
    pm_with_date = pm_df.withColumn(
        "event_date", 
        spark_date(from_unixtime(col("timestamp") / 1000))
    )
    
    # Check what dates we have
    date_counts = pm_with_date.groupBy("event_date").count().orderBy("event_date")
    print("\n📊 Payment Method Listed - Date distribution:")
    date_counts.show(100, truncate=False)
    
    # Check specifically for Nov 3
    nov3_count = pm_with_date.filter(col("event_date") == "2025-11-03").count()
    print(f"\n🔍 Nov 3 rows in Nov 4 partition: {nov3_count:,}")
    
    if nov3_count > 0:
        print("\n⚠️  FOUND NOV 3 DATA in payment_method_listed!")
        print("Sample Nov 3 rows:")
        pm_with_date.filter(col("event_date") == "2025-11-03").select(
            "timestamp", 
            from_unixtime(col("timestamp") / 1000).alias("datetime"),
            "event_date"
        ).show(10, truncate=False)
    
except Exception as e:
    print(f"❌ Error reading payment method listed: {str(e)}")

# COMMAND ----------

# Check customer checkout
try:
    cc_df = spark.read.parquet(
        "s3://hf-dp-shared-proto-s3-sinker-non-pii-raw-live/events/kafka/"
        "parquet/topics/public.customer.checkout.v1beta2/year=2025/month=11/day=04"
    )
    
    from pyspark.sql.functions import col, from_unixtime, date as spark_date
    cc_with_date = cc_df.withColumn(
        "event_date", 
        spark_date(from_unixtime(col("timestamp") / 1000))
    )
    
    date_counts = cc_with_date.groupBy("event_date").count().orderBy("event_date")
    print("\n📊 Customer Checkout - Date distribution:")
    date_counts.show(100, truncate=False)
    
    nov3_count = cc_with_date.filter(col("event_date") == "2025-11-03").count()
    print(f"\n🔍 Nov 3 rows in Nov 4 partition: {nov3_count:,}")
    
    if nov3_count > 0:
        print("\n⚠️  FOUND NOV 3 DATA in customer_checkout!")
        print("Sample Nov 3 rows:")
        cc_with_date.filter(col("event_date") == "2025-11-03").select(
            "timestamp", 
            from_unixtime(col("timestamp") / 1000).alias("datetime"),
            "event_date"
        ).show(10, truncate=False)
    
except Exception as e:
    print(f"❌ Error reading customer checkout: {str(e)}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Check Timezone Settings

# COMMAND ----------

print("\n" + "=" * 100)
print("STEP 2: Checking Spark timezone settings")
print("=" * 100)

# Get Spark timezone
spark_tz = spark.conf.get("spark.sql.session.timeZone")
print(f"\n📅 Spark session timezone: {spark_tz}")

# Test timestamp conversion
test_timestamp = 1730678400000  # Nov 4, 2025 00:00:00 UTC
test_result = spark.sql(f"""
    SELECT 
        {test_timestamp} AS timestamp_ms,
        from_unixtime({test_timestamp} / 1000) AS datetime,
        date(from_unixtime({test_timestamp} / 1000)) AS event_date
""").collect()[0]

print(f"\n🧪 Test timestamp conversion:")
print(f"   Timestamp (ms): {test_timestamp}")
print(f"   Datetime: {test_result['datetime']}")
print(f"   Event Date: {test_result['event_date']}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3: Simulate SQL Query CTEs

# COMMAND ----------

print("\n" + "=" * 100)
print("STEP 3: Tracing through SQL CTEs to find Nov 3 data")
print("=" * 100)

# Simulate backend_events_base
try:
    backend_base_query = f"""
    SELECT
        a.value.customer_uuid AS customer_uuid,
        date(from_unixtime(a.timestamp / 1000)) AS event_date,
        from_unixtime(a.timestamp / 1000) AS event_timestamp,
        a.timestamp
    FROM
        parquet.`s3://hf-dp-shared-proto-s3-sinker-non-pii-raw-live/events/kafka/parquet/topics/public.payment.method-listed.v1beta1/year=2025/month=11/day=04` AS a
    WHERE
        a.value.workflows = 'checkout'
        AND a.value.browser_version <> '51.0.2704'
        -- NOTE: NOT filtering by event_date to diagnose original issue
    """
    
    backend_base_df = spark.sql(backend_base_query)
    backend_date_counts = backend_base_df.groupBy("event_date").count().orderBy("event_date")
    
    print("\n📊 backend_events_base - Date distribution (after filter):")
    backend_date_counts.show(100, truncate=False)
    
    nov3_count = backend_base_df.filter(col("event_date") == "2025-11-03").count()
    if nov3_count > 0:
        print(f"\n⚠️  FOUND NOV 3 DATA in backend_events_base after filter!")
        print("Sample:")
        backend_base_df.filter(col("event_date") == "2025-11-03").select(
            "timestamp",
            "event_timestamp",
            "event_date"
        ).show(10, truncate=False)
    else:
        print(f"\n✅ No Nov 3 data in backend_events_base")
        
except Exception as e:
    print(f"❌ Error in backend_events_base: {str(e)}")

# COMMAND ----------

# Check ops_events_base
try:
    ops_base_query = f"""
    SELECT
        COALESCE(value.attempt.customer_uuid, value.failure.customer_uuid, value.success.customer_uuid) AS customer_uuid,
        DATE(from_unixtime(timestamp/1000)) AS event_date,
        timestamp
    FROM
        parquet.`s3://hf-dp-shared-proto-s3-sinker-non-pii-raw-live/events/kafka/parquet/topics/public.customer.checkout.v1beta2/year=2025/month=11/day=04`
    WHERE
        1 = 1
        -- NOTE: NOT filtering by event_date to diagnose original issue
    """
    
    ops_base_df = spark.sql(ops_base_query)
    ops_date_counts = ops_base_df.groupBy("event_date").count().orderBy("event_date")
    
    print("\n📊 ops_events_base - Date distribution (after filter):")
    ops_date_counts.show(100, truncate=False)
    
    nov3_count = ops_base_df.filter(col("event_date") == "2025-11-03").count()
    if nov3_count > 0:
        print(f"\n⚠️  FOUND NOV 3 DATA in ops_events_base after filter!")
        print("Sample:")
        ops_base_df.filter(col("event_date") == "2025-11-03").select(
            "timestamp",
            "event_date"
        ).show(10, truncate=False)
    else:
        print(f"\n✅ No Nov 3 data in ops_events_base")
        
except Exception as e:
    print(f"❌ Error in ops_events_base: {str(e)}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 4: Check All CTEs in union_all

# COMMAND ----------

print("\n" + "=" * 100)
print("STEP 4: Check all CTEs that contribute to union_all")
print("=" * 100)

# Check fs_backend_event (fraud_decision table)
try:
    fs_query = f"""
    SELECT
        CAST(SUBSTR(details.customer_reference, 3, LENGTH(details.customer_reference)) AS BIGINT) AS customer_id,
        SUBSTR(details.customer_reference, 0, 2) AS country,
        DATE(from_unixtime(HEADER.datetime)) AS event_date
    FROM
        abili_hf.fraud_decision
    WHERE
        1 = 1
        -- NOTE: NOT filtering by event_date to diagnose original issue
        -- Original query had: AND DATE(from_unixtime(header.datetime)) BETWEEN {start_date} and {end_date}
    GROUP BY customer_id, country, event_date
    """
    
    fs_df = spark.sql(fs_query)
    fs_date_counts = fs_df.groupBy("event_date").count().orderBy("event_date")
    
    print("\n📊 fs_backend_event (fraud_decision) - Date distribution:")
    fs_date_counts.show(100, truncate=False)
    
    nov3_count = fs_df.filter(col("event_date") == "2025-11-03").count()
    if nov3_count > 0:
        print(f"\n⚠️  FOUND NOV 3 DATA in fs_backend_event!")
        print("Sample:")
        fs_df.filter(col("event_date") == "2025-11-03").show(10, truncate=False)
    else:
        print(f"\n✅ No Nov 3 data in fs_backend_event")
        
except Exception as e:
    print(f"❌ Error in fs_backend_event: {str(e)}")

# COMMAND ----------

# Check spider_logs_backend_event
try:
    spider_query = f"""
    SELECT
        CAST(a.value.details.customer_id AS BIGINT) AS customer_id,
        a.value.details.business_unit AS country,
        DATE(from_unixtime(a.timestamp / 1000)) AS event_date
    FROM
        parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=04` AS a
    WHERE
        1 = 1
        -- NOTE: NOT filtering by event_date to diagnose original issue
    GROUP BY customer_id, country, event_date
    """
    
    spider_df = spark.sql(spider_query)
    spider_date_counts = spider_df.groupBy("event_date").count().orderBy("event_date")
    
    print("\n📊 spider_logs_backend_event - Date distribution:")
    spider_date_counts.show(100, truncate=False)
    
    nov3_count = spider_df.filter(col("event_date") == "2025-11-03").count()
    if nov3_count > 0:
        print(f"\n⚠️  FOUND NOV 3 DATA in spider_logs_backend_event!")
        print("Sample:")
        spider_df.filter(col("event_date") == "2025-11-03").show(10, truncate=False)
    else:
        print(f"\n✅ No Nov 3 data in spider_logs_backend_event")
        
except Exception as e:
    print(f"❌ Error in spider_logs_backend_event: {str(e)}")

# COMMAND ----------

# Check verifications_backend_event, pvs_backend_event, success_backend_event
# These come from Delta tables, so we need to check them differently

print("\n📊 Checking Delta table sources:")
print("   - verifications_backend_event (from payments_hf.verifications)")
print("   - pvs_backend_event (from payments_hf.pvs)")
print("   - success_backend_event (from payments_hf.success)")

try:
    # Check verifications
    verif_query = f"""
    SELECT
        f.customer_id,
        f.country,
        DATE(f.created_at) AS event_date
    FROM
        payments_hf.verifications AS f
    WHERE
        1 = 1
        AND f.workflow LIKE 'checkout%'
        -- NOTE: NOT filtering by event_date to diagnose original issue
        -- Original query had: AND DATE(f.created_at) BETWEEN {start_date} and {end_date}
    GROUP BY customer_id, country, event_date
    """
    
    verif_df = spark.sql(verif_query)
    verif_date_counts = verif_df.groupBy("event_date").count().orderBy("event_date")
    
    print("\n📊 verifications_backend_event - Date distribution:")
    verif_date_counts.show(100, truncate=False)
    
    nov3_count = verif_df.filter(col("event_date") == "2025-11-03").count()
    if nov3_count > 0:
        print(f"\n⚠️  FOUND NOV 3 DATA in verifications_backend_event!")
    else:
        print(f"\n✅ No Nov 3 data in verifications_backend_event")
        
except Exception as e:
    print(f"❌ Error in verifications_backend_event: {str(e)}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 5: Simulate union_all

# COMMAND ----------

print("\n" + "=" * 100)
print("STEP 5: Simulate union_all to see if Nov 3 appears")
print("=" * 100)

# Try to create a simplified union_all from what we've checked
# This is a diagnostic, so we'll use what we have

print("\n💡 Key Finding:")
print("   The union_all CTE collects event_date from ALL source CTEs.")
print("   If ANY source has Nov 3 data, it will appear in union_all.")
print("   Then the final query joins on event_date, which can create Nov 3 rows.")
print("\n🔍 Check which CTEs have Nov 3 data above to identify the source.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Write Results to DBFS

# COMMAND ----------

output_file = "/tmp/diagnose_event_date_2025_11_03_results.txt"

output_content = f"""
{'='*100}
DIAGNOSTIC RESULTS: event_date = '2025-11-03' Investigation
{'='*100}

Configuration:
  Start Date: {test_start_date}
  End Date: {test_end_date}
  Spark Timezone: {spark_tz}

Investigation Steps:
  1. Checked source Parquet files for Nov 3 data
  2. Checked Spark timezone settings
  3. Traced through SQL CTEs

{'='*100}
"""

dbutils.fs.put(output_file, output_content, overwrite=True)

print(f"✅ Results written to: {output_file}")
print("\n" + output_content)

