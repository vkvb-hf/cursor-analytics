# Usage Example: Query adyen_ml_test_cust_data

## Using the New Structure

### Option 1: Using the CLI Tool

```bash
# From the cursor_databricks directory
python databricks_cli.py sql --query "SELECT * FROM payments_hf.adyen_ml_test_cust_data WHERE customer_uuid IS NOT NULL LIMIT 10"
```

Or using a SQL file:

```bash
# Run the SQL file
python databricks_cli.py sql --file queries/sample_adyen_ml_cust_data.sql --format show
```

### Option 2: Using Python API (from Cursor)

```python
# In any Python file in Cursor
from databricks_api import sql

# Query the table
results = sql("""
    SELECT *
    FROM payments_hf.adyen_ml_test_cust_data
    WHERE customer_uuid IS NOT NULL
    LIMIT 10
""")
```

### Option 3: Using Full API Class

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

# Run query with display
results = db.run_sql("""
    SELECT *
    FROM payments_hf.adyen_ml_test_cust_data
    WHERE customer_uuid IS NOT NULL
    LIMIT 10
""", limit=10, display=True)

# Or run without display (just get results)
results = db.run_sql("""
    SELECT *
    FROM payments_hf.adyen_ml_test_cust_data
    WHERE customer_uuid IS NOT NULL
    LIMIT 10
""", display=False)

# Process results
for row in results:
    print(row)
```

### Option 4: Using SQL File

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()
db.run_sql_file("queries/sample_adyen_ml_cust_data.sql", output_format="csv", limit=10)
```

## Quick Command

```bash
python databricks_cli.py sql --query "SELECT * FROM payments_hf.adyen_ml_test_cust_data WHERE customer_uuid IS NOT NULL LIMIT 10"
```


