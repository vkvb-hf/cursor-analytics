# Databricks notebook source
# MAGIC %md
# MAGIC # Find Dates Affected Like Nov 3
# MAGIC 
# MAGIC Find dates with suspiciously low row counts that may have been partially overwritten

# COMMAND ----------

table_name = "payments_hf.checkout_funnel_backend"
start_date = "2024-01-01"
end_date = "2025-11-12"

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Get Row Counts for All Dates

# COMMAND ----------

print("=" * 100)
print("ANALYZING ROW COUNTS FOR ALL DATES")
print("=" * 100)

# Get row counts for all dates
row_counts_query = f"""
SELECT 
    event_date,
    COUNT(*) AS row_count,
    COUNT(DISTINCT customer_id) AS distinct_customers,
    COUNT(DISTINCT country) AS distinct_countries
FROM {table_name}
WHERE event_date >= '{start_date}' AND event_date <= '{end_date}'
GROUP BY event_date
ORDER BY event_date
"""

row_counts_df = spark.sql(row_counts_query)
row_counts_list = row_counts_df.collect()

print(f"\n📊 Analyzing {len(row_counts_list)} dates...")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Calculate Statistics

# COMMAND ----------

from pyspark.sql.functions import col, avg, min as spark_min, max as spark_max, percentile_approx

# Calculate statistics
stats = row_counts_df.agg(
    avg("row_count").alias("avg_rows"),
    spark_min("row_count").alias("min_rows"),
    spark_max("row_count").alias("max_rows"),
    percentile_approx("row_count", 0.5).alias("median_rows"),
    percentile_approx("row_count", 0.25).alias("q1_rows"),
    percentile_approx("row_count", 0.75).alias("q3_rows")
).collect()[0]

avg_rows = stats['avg_rows']
min_rows = stats['min_rows']
max_rows = stats['max_rows']
median_rows = stats['median_rows']
q1_rows = stats['q1_rows']
q3_rows = stats['q3_rows']
iqr = q3_rows - q1_rows

print("\n📊 Row Count Statistics:")
print(f"   Average: {avg_rows:,.0f}")
print(f"   Median: {median_rows:,.0f}")
print(f"   Min: {min_rows:,}")
print(f"   Max: {max_rows:,}")
print(f"   Q1 (25th percentile): {q1_rows:,.0f}")
print(f"   Q3 (75th percentile): {q3_rows:,.0f}")
print(f"   IQR: {iqr:,.0f}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3: Identify Suspicious Dates

# COMMAND ----------

print("\n" + "=" * 100)
print("IDENTIFYING SUSPICIOUS DATES")
print("=" * 100)

# Define thresholds for suspicious dates
# A date is suspicious if:
# 1. Row count is less than 10% of median
# 2. Row count is less than Q1 - 1.5 * IQR (outlier detection)
# 3. Row count is less than 1000 (absolute threshold)

threshold_10pct_median = median_rows * 0.1
threshold_outlier = q1_rows - 1.5 * iqr
threshold_absolute = 1000

print(f"\n🔍 Thresholds for suspicious dates:")
print(f"   Less than 10% of median: < {threshold_10pct_median:,.0f}")
print(f"   Outlier (Q1 - 1.5*IQR): < {threshold_outlier:,.0f}")
print(f"   Absolute threshold: < {threshold_absolute:,}")

suspicious_dates = []
for row in row_counts_list:
    date = str(row['event_date'])
    count = row['row_count']
    
    is_suspicious = (
        count < threshold_10pct_median or
        count < threshold_outlier or
        count < threshold_absolute
    )
    
    if is_suspicious:
        suspicious_dates.append({
            'date': date,
            'row_count': count,
            'distinct_customers': row['distinct_customers'],
            'reason': []
        })
        
        if count < threshold_10pct_median:
            suspicious_dates[-1]['reason'].append(f"< 10% of median ({threshold_10pct_median:,.0f})")
        if count < threshold_outlier:
            suspicious_dates[-1]['reason'].append(f"outlier (< {threshold_outlier:,.0f})")
        if count < threshold_absolute:
            suspicious_dates[-1]['reason'].append(f"< absolute threshold ({threshold_absolute:,})")

print(f"\n⚠️  Found {len(suspicious_dates)} suspicious dates")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 4: Analyze Suspicious Dates

# COMMAND ----------

if suspicious_dates:
    print("\n" + "=" * 100)
    print("SUSPICIOUS DATES DETAILS")
    print("=" * 100)
    
    # Sort by row count
    suspicious_dates.sort(key=lambda x: x['row_count'])
    
    print("\n📋 Dates with suspiciously low row counts:")
    print(f"{'Date':<12} {'Row Count':<15} {'Customers':<12} {'Reason(s)'}")
    print("-" * 100)
    
    for item in suspicious_dates[:50]:  # Show first 50
        reasons = ", ".join(item['reason'])
        print(f"{item['date']:<12} {item['row_count']:<15,} {item['distinct_customers']:<12,} {reasons}")
    
    if len(suspicious_dates) > 50:
        print(f"\n... and {len(suspicious_dates) - 50} more suspicious dates")
    
    # Check if Nov 3 is in the list
    nov3_found = any(item['date'] == '2025-11-03' for item in suspicious_dates)
    if nov3_found:
        nov3_item = next(item for item in suspicious_dates if item['date'] == '2025-11-03')
        print(f"\n✅ Nov 3 (2025-11-03) is in the suspicious dates list:")
        print(f"   Row count: {nov3_item['row_count']:,}")
        print(f"   Reasons: {', '.join(nov3_item['reason'])}")
    
    # Group by month to see patterns
    from collections import defaultdict
    by_month = defaultdict(list)
    for item in suspicious_dates:
        month = item['date'][:7]  # YYYY-MM
        by_month[month].append(item)
    
    print(f"\n📊 Suspicious dates by month:")
    for month in sorted(by_month.keys()):
        print(f"   {month}: {len(by_month[month])} dates")
    
else:
    print("\n✅ No suspicious dates found!")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 5: Compare with Neighboring Dates

# COMMAND ----------

print("\n" + "=" * 100)
print("COMPARING SUSPICIOUS DATES WITH NEIGHBORS")
print("=" * 100)

# Create a date to row_count mapping
date_to_count = {str(row['event_date']): row['row_count'] for row in row_counts_list}

from datetime import datetime, timedelta

if suspicious_dates:
    print("\n📊 Comparing suspicious dates with day before and after:")
    print(f"{'Date':<12} {'Count':<15} {'Day-1':<15} {'Day+1':<15} {'Ratio vs Day-1':<20} {'Ratio vs Day+1':<20}")
    print("-" * 100)
    
    for item in suspicious_dates[:20]:  # Show first 20
        date = item['date']
        count = item['row_count']
        
        # Get previous and next day
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        prev_date = (date_obj - timedelta(days=1)).strftime("%Y-%m-%d")
        next_date = (date_obj + timedelta(days=1)).strftime("%Y-%m-%d")
        
        prev_count = date_to_count.get(prev_date, 0)
        next_count = date_to_count.get(next_date, 0)
        
        ratio_prev = (count / prev_count * 100) if prev_count > 0 else 0
        ratio_next = (count / next_count * 100) if next_count > 0 else 0
        
        print(f"{date:<12} {count:<15,} {prev_count:<15,} {next_count:<15,} {ratio_prev:<20.1f}% {ratio_next:<20.1f}%")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Write Results

# COMMAND ----------

output_file = "/tmp/find_affected_dates_results.txt"

output_content = f"""
{'='*100}
AFFECTED DATES ANALYSIS: {table_name}
{'='*100}

Date Range: {start_date} to {end_date}
Total Dates Analyzed: {len(row_counts_list)}

Statistics:
  Average rows: {avg_rows:,.0f}
  Median rows: {median_rows:,.0f}
  Min rows: {min_rows:,}
  Max rows: {max_rows:,}

Suspicious Dates Found: {len(suspicious_dates)}

"""

if suspicious_dates:
    output_content += "\nSuspicious Dates (sorted by row count):\n"
    for i, item in enumerate(suspicious_dates[:100], 1):
        reasons = ", ".join(item['reason'])
        output_content += f"  {i}. {item['date']}: {item['row_count']:,} rows ({reasons})\n"
    
    if len(suspicious_dates) > 100:
        output_content += f"  ... and {len(suspicious_dates) - 100} more\n"
    
    # Summary by month
    from collections import defaultdict
    by_month = defaultdict(int)
    for item in suspicious_dates:
        month = item['date'][:7]
        by_month[month] += 1
    
    output_content += "\n\nSuspicious dates by month:\n"
    for month in sorted(by_month.keys()):
        output_content += f"  {month}: {by_month[month]} dates\n"
else:
    output_content += "\n✅ No suspicious dates found!\n"

output_content += f"\n{'='*100}\n"

dbutils.fs.put(output_file, output_content, overwrite=True)
print(f"\n✅ Results written to: {output_file}")
print("\n" + output_content)

