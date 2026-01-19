# Databricks notebook source
# MAGIC %md
# MAGIC # Test checkout_funnel_backend Table Name Replacement
# MAGIC 
# MAGIC Testing that table name placeholders are replaced correctly while date placeholders remain untouched
# MAGIC 
# MAGIC **Note:** This test does NOT create tables, it only tests the string replacement logic.

# COMMAND ----------

# Test SQL query with placeholders (similar to actual checkout_funnel_backend.sql)
test_query = """
WITH backend_events_base AS (
  SELECT
    a.value.customer_uuid,
    a.timestamp
  FROM
    {temp_payment_method_listed_table} AS a
  WHERE
    1 = 1
    AND DATE(from_unixtime(a.timestamp/1000)) BETWEEN {start_date} and {end_date}
),
customer_checkout AS (
  SELECT
    value.customer_uuid,
    value.attempt
  FROM
    {temp_customer_checkout_table}
  WHERE
    1 = 1
    AND DATE(from_unixtime(timestamp/1000)) BETWEEN {start_date} and {end_date}
),
fraud_data AS (
  SELECT
    value.customer_uuid,
    value.details
  FROM
    {temp_fraud_checkout_customer_data_table} AS a
  WHERE
    1 = 1
    AND DATE(from_unixtime(a.timestamp/1000)) BETWEEN {start_date} and {end_date}
)
SELECT * FROM backend_events_base
"""

print("=" * 100)
print("ORIGINAL QUERY (with placeholders):")
print("=" * 100)
print(test_query)
print("=" * 100)

# COMMAND ----------

# Simulate table mapping (as would be created by create_parquet_tables)
# Using a test date range
table_mapping = {
    'payments_hf.temp_payment_method_listed': 'payments_hf.temp_payment_method_listed_20251110_20251110',
    'payments_hf.temp_customer_checkout': 'payments_hf.temp_customer_checkout_20251110_20251110',
    'payments_hf.temp_fraud_checkout_customer_data': 'payments_hf.temp_fraud_checkout_customer_data_20251110_20251110',
}

# Simulate date values
start_date = "2025-11-10"
end_date = "2025-11-10"

print("\n📊 Test Configuration:")
print("-" * 100)
print("Table mapping:")
for base, full in table_mapping.items():
    print(f"  {base}")
    print(f"    -> {full}")
print(f"\nDates: start_date='{start_date}', end_date='{end_date}'")
print("-" * 100)

# COMMAND ----------

# Test the replacement logic (same as in checkout_funnel_backend.py)
table_replacements = {
    '{temp_payment_method_listed_table}': table_mapping['payments_hf.temp_payment_method_listed'],
    '{temp_customer_checkout_table}': table_mapping['payments_hf.temp_customer_checkout'],
    '{temp_fraud_checkout_customer_data_table}': table_mapping['payments_hf.temp_fraud_checkout_customer_data'],
}

# Replace only table name placeholders, leaving {start_date} and {end_date} untouched
query = test_query
for placeholder, replacement in table_replacements.items():
    query = query.replace(placeholder, replacement)

print("\n" + "=" * 100)
print("AFTER TABLE NAME REPLACEMENT:")
print("=" * 100)
print(query)
print("=" * 100)

# COMMAND ----------

# Verify the replacement worked correctly
import re

print("\n" + "=" * 100)
print("VERIFICATION:")
print("=" * 100)

# Check 1: Date placeholders should still be present
date_placeholders = re.findall(r'\{start_date\}|\{end_date\}', query)
date_count = len(date_placeholders)
print(f"\n1. Date placeholders found: {date_count} occurrences")
if date_count >= 4:  # Should have at least 4 (one in each CTE)
    print("   ✅ SUCCESS: Date placeholders are preserved for Spark SQL parameter substitution")
else:
    print(f"   ❌ ERROR: Expected at least 4 date placeholders, found {date_count}")

# Check 2: Table placeholders should be replaced
table_placeholders = re.findall(r'\{temp_\w+_table\}', query)
if len(table_placeholders) == 0:
    print("\n2. Table name placeholders:")
    print("   ✅ SUCCESS: All table name placeholders have been replaced")
else:
    print(f"\n2. Table name placeholders:")
    print(f"   ❌ ERROR: Unreplaced table placeholders found: {table_placeholders}")

# Check 3: Verify specific table names are in the query
expected_tables = [
    'payments_hf.temp_payment_method_listed_20251110_20251110',
    'payments_hf.temp_customer_checkout_20251110_20251110',
    'payments_hf.temp_fraud_checkout_customer_data_20251110_20251110',
]

print("\n3. Expected table names in query:")
all_found = True
for table in expected_tables:
    count = query.count(table)
    if count > 0:
        print(f"   ✅ Found '{table}' ({count} times)")
    else:
        print(f"   ❌ Missing '{table}'")
        all_found = False

# Check 4: Verify no base table names (without date suffix) are present
base_table_names = [
    'payments_hf.temp_payment_method_listed',
    'payments_hf.temp_customer_checkout',
    'payments_hf.temp_fraud_checkout_customer_data',
]

print("\n4. Base table names (should NOT be in query):")
base_found = False
for base_table in base_table_names:
    if base_table in query and f"{base_table}_" not in query:
        print(f"   ❌ ERROR: Found unreplaced base table name: {base_table}")
        base_found = True
if not base_found:
    print("   ✅ SUCCESS: No unreplaced base table names found")

print("\n" + "=" * 100)

# COMMAND ----------

# Simulate what Spark SQL would do with the date parameters
print("\n" + "=" * 100)
print("SIMULATED SPARK SQL PARAMETER SUBSTITUTION:")
print("=" * 100)
print(f"\nIf we call: spark.sql(query, start_date='{start_date}', end_date='{end_date}')")
print("\nSpark SQL would replace:")
print(f"  {{start_date}} -> '{start_date}'")
print(f"  {{end_date}} -> '{end_date}'")
print("\nFinal query would have:")
final_query_example = query.replace('{start_date}', f"'{start_date}'").replace('{end_date}', f"'{end_date}'")
print(final_query_example[:500] + "...")
print("=" * 100)

# COMMAND ----------

# Summary
print("\n" + "=" * 100)
print("TEST SUMMARY:")
print("=" * 100)

test_passed = (
    date_count >= 4 and
    len(table_placeholders) == 0 and
    all_found and
    not base_found
)

if test_passed:
    print("✅ ALL TESTS PASSED!")
    print("\nThe replacement logic works correctly:")
    print("  - Table name placeholders are replaced with dynamic table names")
    print("  - Date placeholders remain untouched for Spark SQL parameter substitution")
else:
    print("❌ SOME TESTS FAILED!")
    print("Please review the verification results above.")

print("=" * 100)

# COMMAND ----------

# Write results to DBFS
output_file = "/tmp/test_checkout_funnel_backend_replacement_results.txt"

output_content = f"""
{'='*100}
TEST RESULTS: checkout_funnel_backend Table Name Replacement
{'='*100}

Test Status: {'PASSED' if test_passed else 'FAILED'}

Table Replacements:
  - {{temp_payment_method_listed_table}} -> {table_mapping['payments_hf.temp_payment_method_listed']}
  - {{temp_customer_checkout_table}} -> {table_mapping['payments_hf.temp_customer_checkout']}
  - {{temp_fraud_checkout_customer_data_table}} -> {table_mapping['payments_hf.temp_fraud_checkout_customer_data']}

Date Placeholders:
  - Found {date_count} date placeholders ({{start_date}} and {{end_date}})
  - These remain in query for Spark SQL parameter substitution

Verification:
  - Table placeholders replaced: {len(table_placeholders) == 0}
  - Expected tables found: {all_found}
  - No base table names: {not base_found}

{'='*100}
"""

dbutils.fs.put(output_file, output_content, overwrite=True)

print(f"\n✅ Results written to: {output_file}")
