#!/usr/bin/env python3
"""
Working Example: Daily Counts with Output in Terminal

This example shows the WORKING approach to see notebook output in terminal.
"""

from databricks_api import DatabricksAPI

# Notebook with explicit DBFS writing - THIS WORKS!
notebook = '''# Databricks notebook source
# MAGIC %md
# MAGIC # Daily Counts: checkout_funnel_backend

# COMMAND ----------

# Query for daily counts
query = \"\"\"
SELECT 
    event_date as date,
    COUNT(*) as daily_count
FROM payments_hf.checkout_funnel_backend
WHERE event_date >= CURRENT_DATE - INTERVAL 7 DAYS
GROUP BY event_date
ORDER BY date DESC
\"\"\"

print('Executing query...')
result_df = spark.sql(query)
pandas_df = result_df.toPandas()

# Build output text using StringIO (avoids string escaping issues)
import io
buffer = io.StringIO()
buffer.write('=' * 80)
buffer.write(chr(10))  # Newline
buffer.write('Daily Counts Results (Last 7 Days)')
buffer.write(chr(10))
buffer.write('=' * 80)
buffer.write(chr(10))
buffer.write(chr(10))
buffer.write(pandas_df.to_string(index=False))
buffer.write(chr(10))
buffer.write(chr(10))
total_count = pandas_df["daily_count"].sum()
buffer.write('=' * 80)
buffer.write(chr(10))
buffer.write(f'Total records in last 7 days: {{total_count:,}}')
buffer.write(chr(10))
buffer.write('=' * 80)
buffer.write(chr(10))

output_text = buffer.getvalue()

# Write to DBFS - THIS WORKS!
# Use job name in path so it can be auto-read
dbutils.fs.put('/tmp/notebook_outputs/Daily_Counts_Checkout_Funnel_output.txt', output_text, overwrite=True)
print('Output written to DBFS')
'''

if __name__ == "__main__":
    db = DatabricksAPI()
    
    result = db.run_notebook_job(
        notebook_path='/Workspace/Users/visal.kumar@hellofresh.com/daily_counts_checkout_funnel',
        notebook_content=notebook,
        job_name='Daily Counts Checkout Funnel',
        auto_inject_output=False,  # Don't use auto-injection (not working)
        auto_read_output=True       # Auto-read from standard location
    )
    
    if result.get('success'):
        print("\n✅ SUCCESS! Output should be displayed above!")
    else:
        print(f"\n❌ Error: {result.get('error')}")

