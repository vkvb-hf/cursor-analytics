#!/usr/bin/env python3
"""
Run the query to show sample records from adyen_ml_test_cust_data
"""
from databricks_api import sql

query = """
SELECT *
FROM payments_hf.adyen_ml_test_cust_data
WHERE customer_uuid IS NOT NULL
LIMIT 10
"""

print("=" * 80)
print("Querying payments_hf.adyen_ml_test_cust_data")
print("WHERE customer_uuid IS NOT NULL")
print("=" * 80)
print()

results = sql(query)

if results:
    print(f"\n✓ Successfully retrieved {len(results)} records")
else:
    print("\n✗ Query failed or returned no results")


