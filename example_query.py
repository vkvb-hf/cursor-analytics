#!/usr/bin/env python3
"""
Example: Query sample records from adyen_ml_test_cust_data
Using the new databricks_api structure
"""
from databricks_api import sql, DatabricksAPI

# Option 1: Using the convenience function
print("=" * 80)
print("Using convenience function: sql()")
print("=" * 80)

query = """
SELECT *
FROM payments_hf.adyen_ml_test_cust_data
WHERE customer_uuid IS NOT NULL
LIMIT 10
"""

results = sql(query)

# Option 2: Using the full API class (more control)
print("\n" + "=" * 80)
print("Using DatabricksAPI class (more control)")
print("=" * 80)

db = DatabricksAPI()
results = db.run_sql(query, limit=10, display=True)

print(f"\n✓ Retrieved {len(results) if results else 0} records")

