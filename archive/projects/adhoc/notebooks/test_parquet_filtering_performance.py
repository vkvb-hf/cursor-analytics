# Databricks notebook source
# MAGIC %md
# MAGIC # Parquet Filtering Performance Test
# MAGIC 
# MAGIC Comparing old approach (DATE conversion) vs new approach (timestamp filtering) for Parquet reads

# COMMAND ----------

import time
from datetime import datetime, timedelta

# Test configuration
test_periods = 5
base_date = datetime(2024, 11, 1)  # Starting from Nov 1, 2024

# Generate 5 different test periods
test_ranges = []
for i in range(test_periods):
    start = base_date + timedelta(days=i*7)  # Each period starts 7 days after previous
    test_ranges.append({
        'period': i + 1,
        'start_date': start.strftime('%Y-%m-%d'),
        'end_date_7d': (start + timedelta(days=6)).strftime('%Y-%m-%d'),  # 7 days
        'end_date_30d': (start + timedelta(days=29)).strftime('%Y-%m-%d')  # 30 days
    })

print("=" * 100)
print("TEST CONFIGURATION")
print("=" * 100)
for tr in test_ranges:
    print(f"Period {tr['period']}: {tr['start_date']} to {tr['end_date_7d']} (7d) / {tr['end_date_30d']} (30d)")
print("=" * 100)

# COMMAND ----------

# Parquet path
parquet_path = "s3://hf-dp-shared-proto-s3-sinker-non-pii-raw-live/events/kafka/parquet/topics/public.payment.method-listed.v1beta1"

print(f"\n📁 Parquet Path: {parquet_path}")
print(f"🔍 Testing both filtering approaches\n")

# COMMAND ----------

results = []

for test_range in test_ranges:
    period = test_range['period']
    start_date = test_range['start_date']
    
    print(f"\n{'='*100}")
    print(f"PERIOD {period}: {start_date}")
    print(f"{'='*100}")
    
    # Test 7-day window
    for window_days, end_date_key in [(7, 'end_date_7d'), (30, 'end_date_30d')]:
        end_date = test_range[end_date_key]
        
        print(f"\n📊 Testing {window_days}-day window: {start_date} to {end_date}")
        
        # OLD APPROACH: DATE conversion in WHERE clause
        print(f"\n⏱️  OLD APPROACH: DATE(from_unixtime(timestamp/1000)) BETWEEN ...")
        old_query = f"""
        SELECT COUNT(*) as row_count
        FROM parquet.`{parquet_path}`
        WHERE value.workflows = 'checkout'
          AND value.browser_version <> '51.0.2704'
          AND DATE(from_unixtime(timestamp/1000)) BETWEEN '{start_date}' AND '{end_date}'
        """
        
        start_time = time.time()
        try:
            old_df = spark.sql(old_query)
            old_count = old_df.collect()[0]['row_count']
            old_time = time.time() - start_time
            print(f"   ✅ Completed in {old_time:.2f} seconds")
            print(f"   📊 Rows: {old_count:,}")
        except Exception as e:
            old_time = None
            old_count = None
            print(f"   ❌ Error: {str(e)}")
        
        # NEW APPROACH: Timestamp filtering
        print(f"\n⏱️  NEW APPROACH: timestamp >= unix_timestamp(...) * 1000")
        new_query = f"""
        SELECT COUNT(*) as row_count
        FROM parquet.`{parquet_path}`
        WHERE value.workflows = 'checkout'
          AND value.browser_version <> '51.0.2704'
          AND timestamp >= unix_timestamp('{start_date}') * 1000
          AND timestamp < (unix_timestamp('{end_date}') + 86400) * 1000
        """
        
        start_time = time.time()
        try:
            new_df = spark.sql(new_query)
            new_count = new_df.collect()[0]['row_count']
            new_time = time.time() - start_time
            print(f"   ✅ Completed in {new_time:.2f} seconds")
            print(f"   📊 Rows: {new_count:,}")
        except Exception as e:
            new_time = None
            new_count = None
            print(f"   ❌ Error: {str(e)}")
        
        # Calculate improvement
        if old_time and new_time:
            improvement = ((old_time - new_time) / old_time) * 100
            speedup = old_time / new_time if new_time > 0 else None
            print(f"\n📈 Performance Comparison:")
            print(f"   Old: {old_time:.2f}s | New: {new_time:.2f}s")
            print(f"   Improvement: {improvement:+.1f}%")
            if speedup:
                print(f"   Speedup: {speedup:.2f}x")
            
            # Verify row counts match
            if old_count == new_count:
                print(f"   ✅ Row counts match: {old_count:,}")
            else:
                print(f"   ⚠️  Row count mismatch! Old: {old_count:,}, New: {new_count:,}")
        else:
            improvement = None
            speedup = None
        
        # Store results
        results.append({
            'period': period,
            'window_days': window_days,
            'start_date': start_date,
            'end_date': end_date,
            'old_time': old_time,
            'new_time': new_time,
            'old_count': old_count,
            'new_count': new_count,
            'improvement_pct': improvement,
            'speedup': speedup
        })

# COMMAND ----------

# Summary and output
print("\n" + "=" * 100)
print("SUMMARY RESULTS")
print("=" * 100)

# Build summary table
output_lines = []
output_lines.append("=" * 100)
output_lines.append("PARQUET FILTERING PERFORMANCE TEST RESULTS")
output_lines.append("=" * 100)
output_lines.append("")
output_lines.append(f"Test Path: {parquet_path}")
output_lines.append(f"Test Periods: {test_periods}")
output_lines.append(f"Window Sizes: 7 days, 30 days")
output_lines.append("")
output_lines.append("-" * 100)
output_lines.append(f"{'Period':<8} {'Window':<8} {'Date Range':<25} {'Old (s)':<12} {'New (s)':<12} {'Improvement':<15} {'Speedup':<10}")
output_lines.append("-" * 100)

for r in results:
    period = r['period']
    window = r['window_days']
    date_range = f"{r['start_date']} to {r['end_date']}"
    old_time_str = f"{r['old_time']:.2f}" if r['old_time'] else "ERROR"
    new_time_str = f"{r['new_time']:.2f}" if r['new_time'] else "ERROR"
    improvement_str = f"{r['improvement_pct']:+.1f}%" if r['improvement_pct'] is not None else "N/A"
    speedup_str = f"{r['speedup']:.2f}x" if r['speedup'] else "N/A"
    
    output_lines.append(f"{period:<8} {window:<8} {date_range:<25} {old_time_str:<12} {new_time_str:<12} {improvement_str:<15} {speedup_str:<10}")

output_lines.append("-" * 100)

# Calculate averages
valid_results = [r for r in results if r['old_time'] and r['new_time']]
if valid_results:
    avg_old = sum(r['old_time'] for r in valid_results) / len(valid_results)
    avg_new = sum(r['new_time'] for r in valid_results) / len(valid_results)
    avg_improvement = ((avg_old - avg_new) / avg_old) * 100
    avg_speedup = avg_old / avg_new if avg_new > 0 else None
    
    output_lines.append("")
    output_lines.append("AVERAGES:")
    output_lines.append(f"  Old Approach: {avg_old:.2f}s")
    output_lines.append(f"  New Approach: {avg_new:.2f}s")
    output_lines.append(f"  Average Improvement: {avg_improvement:+.1f}%")
    if avg_speedup:
        output_lines.append(f"  Average Speedup: {avg_speedup:.2f}x")

# Breakdown by window size
output_lines.append("")
output_lines.append("BREAKDOWN BY WINDOW SIZE:")
for window in [7, 30]:
    window_results = [r for r in valid_results if r['window_days'] == window]
    if window_results:
        avg_old_w = sum(r['old_time'] for r in window_results) / len(window_results)
        avg_new_w = sum(r['new_time'] for r in window_results) / len(window_results)
        avg_improvement_w = ((avg_old_w - avg_new_w) / avg_old_w) * 100
        avg_speedup_w = avg_old_w / avg_new_w if avg_new_w > 0 else None
        
        output_lines.append(f"  {window}-day window:")
        output_lines.append(f"    Old: {avg_old_w:.2f}s | New: {avg_new_w:.2f}s")
        output_lines.append(f"    Improvement: {avg_improvement_w:+.1f}%")
        if avg_speedup_w:
            output_lines.append(f"    Speedup: {avg_speedup_w:.2f}x")

# Conclusion
output_lines.append("")
output_lines.append("=" * 100)
if valid_results:
    if avg_improvement > 0:
        output_lines.append("✅ CONCLUSION: New approach (timestamp filtering) is FASTER")
    elif avg_improvement < 0:
        output_lines.append("⚠️  CONCLUSION: Old approach (DATE conversion) is FASTER")
    else:
        output_lines.append("➡️  CONCLUSION: Both approaches perform similarly")
else:
    output_lines.append("❌ CONCLUSION: Could not complete tests due to errors")
output_lines.append("=" * 100)

# Write output to DBFS
output_text = "\n".join(output_lines)
output_file = "/tmp/parquet_filtering_performance_test.txt"
dbutils.fs.put(output_file, output_text, overwrite=True)

# Also print
print(output_text)

