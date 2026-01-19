# Databricks notebook source
# MAGIC %md
# MAGIC # Verify Table Data Integrity
# MAGIC 
# MAGIC Comprehensive check of checkout_funnel_backend table data

# COMMAND ----------

table_name = "payments_hf.checkout_funnel_backend"

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Overall Table Statistics

# COMMAND ----------

print("=" * 100)
print("OVERALL TABLE STATISTICS")
print("=" * 100)

overall_query = f"""
SELECT 
    COUNT(*) AS total_rows,
    COUNT(DISTINCT event_date) AS distinct_dates,
    COUNT(DISTINCT customer_id) AS distinct_customers,
    COUNT(DISTINCT country) AS distinct_countries,
    MIN(event_date) AS min_date,
    MAX(event_date) AS max_date
FROM {table_name}
"""

overall_result = spark.sql(overall_query).collect()[0]

print(f"\n📊 Overall Statistics:")
print(f"   Total rows: {overall_result['total_rows']:,}")
print(f"   Distinct dates: {overall_result['distinct_dates']:,}")
print(f"   Distinct customers: {overall_result['distinct_customers']:,}")
print(f"   Distinct countries: {overall_result['distinct_countries']:,}")
print(f"   Date range: {overall_result['min_date']} to {overall_result['max_date']}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Verify 2023-12-31 is Deleted

# COMMAND ----------

print("\n" + "=" * 100)
print("VERIFYING 2023-12-31 DELETION")
print("=" * 100)

check_2023_query = f"""
SELECT 
    COUNT(*) AS row_count
FROM {table_name}
WHERE event_date = '2023-12-31'
"""

check_2023_result = spark.sql(check_2023_query).collect()[0]

if check_2023_result['row_count'] == 0:
    print("\n✅ 2023-12-31 partition successfully deleted (0 rows)")
else:
    print(f"\n⚠️  WARNING: 2023-12-31 still has {check_2023_result['row_count']:,} rows")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3: Check Affected Dates Status

# COMMAND ----------

print("\n" + "=" * 100)
print("CHECKING AFFECTED DATES STATUS")
print("=" * 100)

affected_dates = [
    "2024-04-30",
    "2024-07-31",
    "2024-09-30",
    "2024-10-31",
    "2024-11-30",
    "2025-06-29",
    "2025-09-29",
    "2025-11-03"
]

affected_query = f"""
SELECT 
    event_date,
    COUNT(*) AS row_count,
    COUNT(DISTINCT customer_id) AS distinct_customers
FROM {table_name}
WHERE event_date IN ({','.join([f"'{d}'" for d in affected_dates])})
GROUP BY event_date
ORDER BY event_date
"""

affected_df = spark.sql(affected_query)
affected_list = affected_df.collect()
affected_results = {str(row['event_date']): {'row_count': row['row_count'], 'customers': row['distinct_customers']} 
                    for row in affected_list}

# Also check each date individually to be sure
print("\n🔍 Individual date checks:")
for date in affected_dates:
    individual_query = f"""
    SELECT 
        COUNT(*) AS row_count,
        COUNT(DISTINCT customer_id) AS distinct_customers
    FROM {table_name}
    WHERE event_date = '{date}'
    """
    individual_result = spark.sql(individual_query).collect()[0]
    print(f"   {date}: {individual_result['row_count']:,} rows, {individual_result['distinct_customers']:,} customers")
    if date not in affected_results:
        affected_results[date] = {
            'row_count': individual_result['row_count'],
            'customers': individual_result['distinct_customers']
        }

print("\n📊 Affected Dates Status:")
print(f"{'Date':<12} {'Row Count':<15} {'Customers':<12} {'Status'}")
print("-" * 60)

for date in affected_dates:
    if date in affected_results:
        result = affected_results[date]
        count = result['row_count']
        customers = result['customers']
        
        # Determine status
        if count < 1000:
            status = "⚠️  Low (needs backfill)"
        elif count < 50000:
            status = "⚠️  Below average"
        else:
            status = "✅ OK"
        
        print(f"{date:<12} {count:<15,} {customers:<12,} {status}")
    else:
        print(f"{date:<12} {'0':<15} {'0':<12} ❌ Missing")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 4: Check Date Range Coverage

# COMMAND ----------

print("\n" + "=" * 100)
print("CHECKING DATE RANGE COVERAGE (2024-01-01 to 2025-11-12)")
print("=" * 100)

from datetime import datetime, timedelta

start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 11, 12)

expected_dates = set()
current = start_date
while current <= end_date:
    expected_dates.add(current.strftime("%Y-%m-%d"))
    current += timedelta(days=1)

coverage_query = f"""
SELECT DISTINCT event_date
FROM {table_name}
WHERE event_date >= '2024-01-01' AND event_date <= '2025-11-12'
ORDER BY event_date
"""

coverage_df = spark.sql(coverage_query)
actual_dates = set([str(row['event_date']) for row in coverage_df.collect()])

missing_dates = sorted(expected_dates - actual_dates)

print(f"\n📊 Coverage Analysis:")
print(f"   Expected dates: {len(expected_dates):,}")
print(f"   Actual dates: {len(actual_dates):,}")
print(f"   Missing dates: {len(missing_dates):,}")

if missing_dates:
    print(f"\n❌ Missing dates:")
    for date in missing_dates[:20]:
        print(f"   {date}")
    if len(missing_dates) > 20:
        print(f"   ... and {len(missing_dates) - 20} more")
else:
    print("\n✅ All dates present in range!")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 5: Sample Recent Dates

# COMMAND ----------

print("\n" + "=" * 100)
print("SAMPLE RECENT DATES (Last 10 days)")
print("=" * 100)

recent_query = f"""
SELECT 
    event_date,
    COUNT(*) AS row_count,
    COUNT(DISTINCT customer_id) AS distinct_customers
FROM {table_name}
WHERE event_date >= '2025-11-03' AND event_date <= '2025-11-12'
GROUP BY event_date
ORDER BY event_date
"""

recent_df = spark.sql(recent_query)
print("\n📊 Recent dates (Nov 3-12):")
recent_df.show(truncate=False)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 6: Check for Data Quality Issues

# COMMAND ----------

print("\n" + "=" * 100)
print("DATA QUALITY CHECKS")
print("=" * 100)

# Check for NULL event_dates
null_check = spark.sql(f"""
SELECT COUNT(*) AS null_event_dates
FROM {table_name}
WHERE event_date IS NULL
""").collect()[0]

print(f"\n🔍 NULL Checks:")
print(f"   NULL event_dates: {null_check['null_event_dates']:,}")

# Check for NULL customer_ids
null_customer_check = spark.sql(f"""
SELECT COUNT(*) AS null_customers
FROM {table_name}
WHERE customer_id IS NULL
""").collect()[0]

print(f"   NULL customer_ids: {null_customer_check['null_customers']:,}")

# Check for NULL countries
null_country_check = spark.sql(f"""
SELECT COUNT(*) AS null_countries
FROM {table_name}
WHERE country IS NULL
""").collect()[0]

print(f"   NULL countries: {null_country_check['null_countries']:,}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Write Results

# COMMAND ----------

output_file = "/tmp/verify_table_data_results.txt"

output_content = f"""
{'='*100}
TABLE DATA VERIFICATION: {table_name}
{'='*100}

Overall Statistics:
  Total rows: {overall_result['total_rows']:,}
  Distinct dates: {overall_result['distinct_dates']:,}
  Distinct customers: {overall_result['distinct_customers']:,}
  Date range: {overall_result['min_date']} to {overall_result['max_date']}

2023-12-31 Status: {'✅ Deleted' if check_2023_result['row_count'] == 0 else f"⚠️  Still has {check_2023_result['row_count']:,} rows"}

Affected Dates Status:
"""

for date in affected_dates:
    if date in affected_results:
        result = affected_results[date]
        status = "⚠️  Low" if result['row_count'] < 1000 else "✅ OK"
        output_content += f"  {date}: {result['row_count']:,} rows - {status}\n"
    else:
        output_content += f"  {date}: Missing\n"

output_content += f"""
Date Range Coverage (2024-01-01 to 2025-11-12):
  Expected: {len(expected_dates):,} dates
  Actual: {len(actual_dates):,} dates
  Missing: {len(missing_dates):,} dates

Data Quality:
  NULL event_dates: {null_check['null_event_dates']:,}
  NULL customer_ids: {null_customer_check['null_customers']:,}
  NULL countries: {null_country_check['null_countries']:,}

{'='*100}
"""

dbutils.fs.put(output_file, output_content, overwrite=True)
print(f"\n✅ Results written to: {output_file}")
print("\n" + output_content)

