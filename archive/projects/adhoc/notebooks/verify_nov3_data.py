# Databricks notebook source
# MAGIC %md
# MAGIC # Verify Nov 3 Data in checkout_funnel_backend
# MAGIC 
# MAGIC Detailed check for Nov 3 and surrounding dates

# COMMAND ----------

table_name = "payments_hf.checkout_funnel_backend"

# COMMAND ----------

# MAGIC %md
# MAGIC ## Check Nov 3 and surrounding dates with row counts

# COMMAND ----------

print("=" * 100)
print("VERIFYING NOV 3 DATA")
print("=" * 100)

# Check dates from Nov 1 to Nov 12
dates_to_check = [f"2025-11-{i:02d}" for i in range(1, 13)]

query = f"""
SELECT 
    event_date,
    COUNT(*) AS row_count,
    COUNT(DISTINCT customer_id) AS distinct_customers,
    COUNT(DISTINCT country) AS distinct_countries
FROM {table_name}
WHERE event_date IN ({','.join([f"'{d}'" for d in dates_to_check])})
GROUP BY event_date
ORDER BY event_date
"""

result_df = spark.sql(query)
print("\n📊 November 2025 dates with row counts:")
result_df.show(20, truncate=False)

# Check specifically for Nov 3
nov3_check = spark.sql(f"""
SELECT 
    COUNT(*) AS total_rows,
    COUNT(DISTINCT customer_id) AS distinct_customers
FROM {table_name}
WHERE event_date = '2025-11-03'
""").collect()[0]

print(f"\n🔍 Nov 3 (2025-11-03) specific check:")
print(f"   Total rows: {nov3_check['total_rows']:,}")
print(f"   Distinct customers: {nov3_check['distinct_customers']:,}")

if nov3_check['total_rows'] == 0:
    print("   ⚠️  WARNING: Nov 3 has 0 rows!")
else:
    print("   ✅ Nov 3 has data")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Compare Nov 3 vs Nov 4

# COMMAND ----------

comparison_query = f"""
SELECT 
    event_date,
    COUNT(*) AS row_count,
    COUNT(DISTINCT customer_id) AS distinct_customers
FROM {table_name}
WHERE event_date IN ('2025-11-03', '2025-11-04')
GROUP BY event_date
ORDER BY event_date
"""

comparison_df = spark.sql(comparison_query)
print("\n📊 Comparison: Nov 3 vs Nov 4")
comparison_df.show(truncate=False)

# Get average row count for context
avg_query = f"""
SELECT 
    AVG(row_count) AS avg_rows,
    MIN(row_count) AS min_rows,
    MAX(row_count) AS max_rows
FROM (
    SELECT 
        event_date,
        COUNT(*) AS row_count
    FROM {table_name}
    WHERE event_date >= '2025-11-01' AND event_date <= '2025-11-12'
    GROUP BY event_date
)
"""

avg_result = spark.sql(avg_query).collect()[0]
print(f"\n📊 November 2025 context (Nov 1-12):")
print(f"   Average rows per date: {avg_result['avg_rows']:,.0f}")
print(f"   Min rows: {avg_result['min_rows']:,}")
print(f"   Max rows: {avg_result['max_rows']:,}")

nov3_rows = comparison_df.filter(comparison_df.event_date == "2025-11-03").collect()
nov4_rows = comparison_df.filter(comparison_df.event_date == "2025-11-04").collect()

if nov3_rows:
    nov3_count = nov3_rows[0]['row_count']
    if nov4_rows:
        nov4_count = nov4_rows[0]['row_count']
        print(f"\n⚠️  Nov 3 has {nov3_count:,} rows vs Nov 4 has {nov4_count:,} rows")
        if nov3_count < nov4_count * 0.1:  # Less than 10% of Nov 4
            print("   ⚠️  WARNING: Nov 3 has significantly fewer rows than Nov 4!")
            print("   This suggests Nov 3 data may have been partially lost.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Check all dates in range 2024-01-01 to 2025-11-12

# COMMAND ----------

range_query = f"""
SELECT 
    MIN(event_date) AS min_date,
    MAX(event_date) AS max_date,
    COUNT(DISTINCT event_date) AS distinct_dates,
    COUNT(*) AS total_rows
FROM {table_name}
WHERE event_date >= '2024-01-01' AND event_date <= '2025-11-12'
"""

range_result = spark.sql(range_query).collect()[0]
print("\n📊 Date range summary (2024-01-01 to 2025-11-12):")
print(f"   Min date: {range_result['min_date']}")
print(f"   Max date: {range_result['max_date']}")
print(f"   Distinct dates: {range_result['distinct_dates']:,}")
print(f"   Total rows: {range_result['total_rows']:,}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Find all missing dates in range

# COMMAND ----------

# Generate all expected dates
from datetime import datetime, timedelta
start = datetime(2024, 1, 1)
end = datetime(2025, 11, 12)

expected_dates = set()
current = start
while current <= end:
    expected_dates.add(current.strftime("%Y-%m-%d"))
    current += timedelta(days=1)

# Get actual dates
actual_dates_query = f"""
SELECT DISTINCT event_date
FROM {table_name}
WHERE event_date >= '2024-01-01' AND event_date <= '2025-11-12'
ORDER BY event_date
"""

actual_dates_df = spark.sql(actual_dates_query)
actual_dates = set([str(row['event_date']) for row in actual_dates_df.collect()])

missing_dates = sorted(expected_dates - actual_dates)

print(f"\n📊 Missing dates analysis:")
print(f"   Expected dates: {len(expected_dates):,}")
print(f"   Actual dates: {len(actual_dates):,}")
print(f"   Missing dates: {len(missing_dates):,}")

if missing_dates:
    print(f"\n❌ Missing dates:")
    for date in missing_dates[:50]:
        print(f"   {date}")
    if len(missing_dates) > 50:
        print(f"   ... and {len(missing_dates) - 50} more")
    
    if "2025-11-03" in missing_dates:
        print("\n⚠️  CRITICAL: 2025-11-03 is in the missing dates list!")
else:
    print("\n✅ No missing dates!")
    if "2025-11-03" in actual_dates:
        print("✅ 2025-11-03 is present in the table")

# COMMAND ----------

# Write results
output_file = "/tmp/verify_nov3_data_results.txt"
output_content = f"""
{'='*100}
NOV 3 DATA VERIFICATION: {table_name}
{'='*100}

Nov 3 Row Count: {nov3_check['total_rows']:,}
Nov 3 Distinct Customers: {nov3_check['distinct_customers']:,}

Date Range (2024-01-01 to 2025-11-12):
  Min Date: {range_result['min_date']}
  Max Date: {range_result['max_date']}
  Distinct Dates: {range_result['distinct_dates']:,}
  Total Rows: {range_result['total_rows']:,}

Missing Dates: {len(missing_dates):,}
"""

if "2025-11-03" in missing_dates:
    output_content += "\n⚠️  CRITICAL: 2025-11-03 is MISSING!\n"
elif nov3_check['total_rows'] == 0:
    output_content += "\n⚠️  WARNING: 2025-11-03 exists but has 0 rows!\n"
else:
    output_content += "\n✅ 2025-11-03 is present with data\n"

output_content += f"\n{'='*100}\n"

dbutils.fs.put(output_file, output_content, overwrite=True)
print(f"\n✅ Results written to: {output_file}")

