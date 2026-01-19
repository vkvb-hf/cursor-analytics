# Databricks notebook source
# MAGIC %md
# MAGIC # Check Missing Event Dates in checkout_funnel_backend
# MAGIC 
# MAGIC This notebook checks which event dates are present and missing in the table

# COMMAND ----------

from datetime import datetime, timedelta

# COMMAND ----------

# MAGIC %md
# MAGIC ## Configuration

# COMMAND ----------

# Date range to check
start_date = "2024-01-01"
end_date = "2025-11-12"

table_name = "payments_hf.checkout_funnel_backend"

print("=" * 100)
print("CHECKING EVENT DATES IN TABLE")
print("=" * 100)
print(f"Table: {table_name}")
print(f"Date Range: {start_date} to {end_date}")
print("=" * 100)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Get All Event Dates in Table

# COMMAND ----------

print("\n" + "=" * 100)
print("STEP 1: Getting all event dates present in the table")
print("=" * 100)

# First check if table exists and has any data
print("\n🔍 Checking if table exists and has data...")
try:
    check_query = f"SELECT COUNT(*) AS total_rows FROM {table_name}"
    total_rows = spark.sql(check_query).collect()[0]['total_rows']
    print(f"   Total rows in table: {total_rows:,}")
    
    if total_rows == 0:
        print("   ⚠️  Table is empty!")
    else:
        # Get date range in table
        date_range_query = f"""
        SELECT 
            MIN(event_date) AS min_date,
            MAX(event_date) AS max_date,
            COUNT(DISTINCT event_date) AS distinct_dates
        FROM {table_name}
        """
        date_range = spark.sql(date_range_query).collect()[0]
        print(f"   Date range: {date_range['min_date']} to {date_range['max_date']}")
        print(f"   Distinct dates: {date_range['distinct_dates']:,}")
        
except Exception as e:
    print(f"   ❌ Error accessing table: {str(e)}")
    raise

# Get distinct event dates
dates_query = f"""
SELECT 
    event_date,
    COUNT(*) AS row_count
FROM {table_name}
WHERE event_date >= '{start_date}' 
  AND event_date <= '{end_date}'
GROUP BY event_date
ORDER BY event_date
"""

dates_df = spark.sql(dates_query)
dates_list = [str(row['event_date']) for row in dates_df.collect()]

print(f"\n📊 Found {len(dates_list)} distinct event dates in the table")
print("\nFirst 20 dates:")
dates_df.show(20, truncate=False)

print("\nLast 20 dates:")
dates_df.tail(20)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Generate Expected Date Range

# COMMAND ----------

print("\n" + "=" * 100)
print("STEP 2: Generating expected date range")
print("=" * 100)

# Generate all dates in range
start = datetime.strptime(start_date, "%Y-%m-%d")
end = datetime.strptime(end_date, "%Y-%m-%d")

expected_dates = []
current = start
while current <= end:
    expected_dates.append(current.strftime("%Y-%m-%d"))
    current += timedelta(days=1)

print(f"\n📅 Expected dates in range: {len(expected_dates)}")
print(f"   From: {expected_dates[0]}")
print(f"   To: {expected_dates[-1]}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3: Find Missing Dates

# COMMAND ----------

print("\n" + "=" * 100)
print("STEP 3: Finding missing event dates")
print("=" * 100)

# Convert dates_list to set for faster lookup
dates_set = set(dates_list)

# Find missing dates
missing_dates = [date for date in expected_dates if date not in dates_set]

print(f"\n❌ Missing dates: {len(missing_dates)}")
if missing_dates:
    print("\nFirst 50 missing dates:")
    for i, date in enumerate(missing_dates[:50]):
        print(f"  {date}")
        if (i + 1) % 10 == 0:
            print()
    
    if len(missing_dates) > 50:
        print(f"\n... and {len(missing_dates) - 50} more missing dates")
        print("\nLast 20 missing dates:")
        for date in missing_dates[-20:]:
            print(f"  {date}")
else:
    print("✅ No missing dates in the range!")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 4: Analyze Date Gaps

# COMMAND ----------

print("\n" + "=" * 100)
print("STEP 4: Analyzing date gaps")
print("=" * 100)

if missing_dates:
    # Find consecutive missing date ranges
    gaps = []
    gap_start = None
    gap_end = None
    
    for date in missing_dates:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        if gap_start is None:
            gap_start = date_obj
            gap_end = date_obj
        elif (date_obj - gap_end).days == 1:
            gap_end = date_obj
        else:
            gaps.append((gap_start, gap_end))
            gap_start = date_obj
            gap_end = date_obj
    
    if gap_start is not None:
        gaps.append((gap_start, gap_end))
    
    print(f"\n📊 Found {len(gaps)} gap(s) in the data:")
    for i, (start_gap, end_gap) in enumerate(gaps, 1):
        days = (end_gap - start_gap).days + 1
        if start_gap == end_gap:
            print(f"  {i}. Single missing date: {start_gap.strftime('%Y-%m-%d')}")
        else:
            print(f"  {i}. Missing range: {start_gap.strftime('%Y-%m-%d')} to {end_gap.strftime('%Y-%m-%d')} ({days} days)")
else:
    print("\n✅ No gaps found - all dates are present!")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 5: Check Specific Dates of Interest

# COMMAND ----------

print("\n" + "=" * 100)
print("STEP 5: Checking specific dates of interest")
print("=" * 100)

# Check the dates that were run in the loop script
dates_to_check = [
    "2025-05-31",
    "2025-06-30", 
    "2025-09-30",
    "2025-11-04",
    "2025-11-03",  # The problematic date
    "2025-11-12",  # Last date present
    "2025-11-13",  # First missing date
]

print("\n🔍 Checking specific dates:")
for date in dates_to_check:
    exists = date in dates_set
    status = "✅ Present" if exists else "❌ Missing"
    
    if exists:
        row_count_row = dates_df.filter(dates_df.event_date == date).collect()
        if row_count_row:
            row_count = row_count_row[0]['row_count']
            print(f"  {date}: {status} ({row_count:,} rows)")
        else:
            print(f"  {date}: {status} (count not available)")
    else:
        print(f"  {date}: {status}")

# Also check dates around Nov 3-4
print("\n🔍 Checking dates around Nov 3-4:")
for i in range(-2, 3):
    check_date = (datetime.strptime("2025-11-04", "%Y-%m-%d") + timedelta(days=i)).strftime("%Y-%m-%d")
    exists = check_date in dates_set
    status = "✅ Present" if exists else "❌ Missing"
    
    if exists:
        row_count_row = dates_df.filter(dates_df.event_date == check_date).collect()
        if row_count_row:
            row_count = row_count_row[0]['row_count']
            print(f"  {check_date}: {status} ({row_count:,} rows)")
        else:
            print(f"  {check_date}: {status}")
    else:
        print(f"  {check_date}: {status}")

# Check November 2025 specifically
print("\n🔍 Checking all dates in November 2025:")
nov_dates = [f"2025-11-{i:02d}" for i in range(1, 13)]
for date in nov_dates:
    exists = date in dates_set
    status = "✅" if exists else "❌"
    
    if exists:
        row_count_row = dates_df.filter(dates_df.event_date == date).collect()
        if row_count_row:
            row_count = row_count_row[0]['row_count']
            print(f"  {date}: {status} ({row_count:,} rows)")
        else:
            print(f"  {date}: {status}")
    else:
        print(f"  {date}: {status} MISSING")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Write Results to DBFS

# COMMAND ----------

output_file = "/tmp/check_missing_event_dates_results.txt"

output_content = f"""
{'='*100}
MISSING EVENT DATES ANALYSIS: {table_name}
{'='*100}

Date Range: {start_date} to {end_date}
Total Expected Dates: {len(expected_dates)}
Dates Present: {len(dates_list)}
Missing Dates: {len(missing_dates)}

"""

if missing_dates:
    output_content += f"""
Missing Dates Summary:
  Total Missing: {len(missing_dates)}
  First Missing: {missing_dates[0] if missing_dates else 'N/A'}
  Last Missing: {missing_dates[-1] if missing_dates else 'N/A'}

Gaps Found: {len(gaps) if missing_dates else 0}
"""
    for i, (start_gap, end_gap) in enumerate(gaps[:20], 1):
        days = (end_gap - start_gap).days + 1
        if start_gap == end_gap:
            output_content += f"  {i}. {start_gap.strftime('%Y-%m-%d')}\n"
        else:
            output_content += f"  {i}. {start_gap.strftime('%Y-%m-%d')} to {end_gap.strftime('%Y-%m-%d')} ({days} days)\n"
    
    if len(gaps) > 20:
        output_content += f"  ... and {len(gaps) - 20} more gaps\n"
    
    # Check specifically for Nov 3
    if "2025-11-03" in missing_dates:
        output_content += "\n⚠️  IMPORTANT: 2025-11-03 is MISSING!\n"
    else:
        output_content += "\n✅ 2025-11-03 is present\n"
else:
    output_content += "\n✅ No missing dates in the specified range!\n"
    # Double-check Nov 3 specifically
    if "2025-11-03" in dates_set:
        output_content += "✅ 2025-11-03 is confirmed present\n"
    else:
        output_content += "⚠️  WARNING: 2025-11-03 not found in dates_set!\n"

output_content += f"\n{'='*100}\n"

dbutils.fs.put(output_file, output_content, overwrite=True)

print(f"✅ Results written to: {output_file}")
print("\n" + output_content)

