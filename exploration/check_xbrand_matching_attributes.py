#!/usr/bin/env python3
"""
Check sample records from spider logs to understand xbrand matching_attributes structure

Usage:
    cd /Users/visal.kumar/Documents/databricks
    source databricks_env/bin/activate
    cd cursor_databricks
    python exploration/check_xbrand_matching_attributes.py
"""
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from databricks import sql
from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN

def format_value(value):
    """Format a value for display"""
    if value is None:
        return 'NULL'
    if isinstance(value, (list, tuple)):
        return str(list(value))
    return str(value)

def print_table(results, column_names=None, limit=None):
    """Print query results in a formatted table"""
    if not results:
        print("No results returned.")
        return
    
    display_results = results[:limit] if limit else results
    
    if not column_names and results:
        first_row = results[0]
        if hasattr(first_row, '_fields'):
            column_names = list(first_row._fields)
        elif isinstance(first_row, (list, tuple)):
            column_names = [f"col_{i+1}" for i in range(len(first_row))]
        else:
            column_names = ["value"]
    
    if not column_names:
        column_names = ["value"]
    
    # Calculate column widths
    col_widths = {}
    for i, col in enumerate(column_names):
        width = len(str(col))
        for row in display_results:
            try:
                if isinstance(row, (list, tuple)) and i < len(row):
                    val = row[i]
                elif hasattr(row, col):
                    val = getattr(row, col)
                else:
                    val = row[i] if hasattr(row, '__getitem__') else str(row)
                width = max(width, len(format_value(val)))
            except:
                pass
        col_widths[col] = width
    
    # Print header
    header = " | ".join(str(col).ljust(col_widths.get(col, len(str(col)))) for col in column_names)
    print(header)
    print("-" * len(header))
    
    # Print rows
    for row in display_results:
        row_str = " | ".join(
            format_value(
                row[i] if isinstance(row, (list, tuple)) and i < len(row) 
                else getattr(row, col, row[i] if hasattr(row, '__getitem__') else str(row))
            ).ljust(col_widths.get(col, 20))
            for i, col in enumerate(column_names)
        )
        print(row_str)

def run_query(query):
    """Run a query and return results"""
    try:
        with sql.connect(
            server_hostname=SERVER_HOSTNAME,
            http_path=HTTP_PATH,
            access_token=TOKEN,
            timeout_seconds=300
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return None

# Query to get distinct attribute names and their counts
# Using specific date path to reduce runtime
query_distinct_attrs = """
WITH spider_data AS (
  SELECT 
    value.details.business_unit,
    ARRAY_DISTINCT(
      FLATTEN(
        TRANSFORM(
          FROM_JSON(
            value.details.raw_payload,
            'struct<parent_ids_with_checkout_success:array<struct<matching_attributes:array<struct<attribute_name:string>>>>>'
          ).parent_ids_with_checkout_success,
          x -> TRANSFORM(x.matching_attributes, y -> y.attribute_name)
        )
      )
    ) AS matching_attributes
  FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
  WHERE 
    get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
    AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
),
flattened AS (
  SELECT 
    business_unit,
    explode(matching_attributes) as attr_name
  FROM spider_data
  WHERE matching_attributes IS NOT NULL
    AND size(matching_attributes) > 0
)
SELECT 
  attr_name,
  COUNT(*) as occurrence_count,
  COUNT(DISTINCT business_unit) as distinct_business_units
FROM flattened
GROUP BY attr_name
ORDER BY occurrence_count DESC
"""

# Query to check sample records with xbrand detection
query_samples = """
SELECT 
  value.details.business_unit,
  cast(value.details.customer_id as bigint) as customer_id,
  ARRAY_DISTINCT(
    FLATTEN(
      TRANSFORM(
        FROM_JSON(
          value.details.raw_payload,
          'struct<parent_ids_with_checkout_success:array<struct<matching_attributes:array<struct<attribute_name:string>>>>>'
        ).parent_ids_with_checkout_success,
        x -> TRANSFORM(x.matching_attributes, y -> y.attribute_name)
      )
    )
  ) AS matching_attributes,
  coalesce(
    array_contains(
      ARRAY_DISTINCT(
        FLATTEN(
          TRANSFORM(
            FROM_JSON(
              value.details.raw_payload,
              'struct<parent_ids_with_checkout_success:array<struct<matching_attributes:array<struct<attribute_name:string>>>>>'
            ).parent_ids_with_checkout_success,
            x -> TRANSFORM(x.matching_attributes, y -> y.attribute_name)
          )
        )
      ),
      'xbrand'
    ),
    false
  ) as is_xbrand_match
FROM parquet.`s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2/year=2025/month=11/day=01`
WHERE 
  get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id') IS NOT NULL
  AND length(get_json_object(value.details.raw_payload, '$.parent_ids_with_checkout_success[0].id')) > 0
LIMIT 50
"""

if __name__ == "__main__":
    print("=" * 80)
    print("Checking matching_attributes values from spider logs")
    print("Using date path: year=2025/month=11/day=01 for faster testing")
    print("=" * 80)
    
    print("\n1. Distinct attribute names and occurrence counts:")
    print("-" * 80)
    results1 = run_query(query_distinct_attrs)
    if results1:
        print_table(results1, limit=100)
        
        # Check if xbrand exists
        xbrand_found = False
        xbrand_variants = []
        for row in results1:
            attr_name = row[0] if isinstance(row, (list, tuple)) else getattr(row, 'attr_name', None)
            if attr_name:
                attr_str = str(attr_name).lower()
                if 'xbrand' in attr_str or 'cross' in attr_str or 'brand' in attr_str:
                    xbrand_found = True
                    xbrand_variants.append(attr_name)
        
        print("\n" + "=" * 80)
        if xbrand_found:
            print(f"✓ Found potential xbrand-related attributes: {xbrand_variants}")
        else:
            print("⚠ Warning: No 'xbrand', 'cross', or 'brand' related attributes found")
            print("   Please check the attribute list above to identify the correct name")
    else:
        print("No results or error occurred")
    
    print("\n" + "=" * 80)
    print("2. Sample records with matching_attributes and xbrand check:")
    print("-" * 80)
    results2 = run_query(query_samples)
    if results2:
        print_table(results2, limit=50)
        
        # Count how many have xbrand
        xbrand_count = 0
        total_count = len(results2)
        for row in results2:
            is_xbrand = row[-1] if isinstance(row, (list, tuple)) else getattr(row, 'is_xbrand_match', False)
            if is_xbrand:
                xbrand_count += 1
        
        print(f"\n✓ Found {xbrand_count} out of {total_count} sample records with xbrand match")
    else:
        print("No results or error occurred")
