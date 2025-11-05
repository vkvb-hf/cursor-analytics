#!/usr/bin/env python3
"""
Template for creating Databricks notebooks that output to terminal.

This template shows how to write notebook code that will display output
in the terminal after job execution.

Usage:
1. Copy this template
2. Modify the SQL query and analysis
3. Ensure output is written to DBFS using dbutils.fs.put()
4. Run using create_and_run_notebook_job.py or databricks_api.py
"""
import uuid

# Generate unique output file name
output_file_id = str(uuid.uuid4())[:8]
output_file_path = f"/tmp/notebook_output_{output_file_id}.txt"

# NOTEBOOK TEMPLATE
notebook_template = f"""# Databricks notebook source
# MAGIC %md
# MAGIC # Your Analysis Title
# MAGIC 
# MAGIC Description of what this notebook does.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- SQL queries work too, but output won't be captured
# MAGIC -- For terminal output, use Python cells below

# COMMAND ----------

# Run your SQL query
query = \"\"\"SELECT *
FROM schema.table_name
WHERE your_condition = 'value'
LIMIT 10\"\"\"

# Execute query
result_df = spark.sql(query)

# Convert to pandas for better formatting
import pandas as pd
pandas_df = result_df.toPandas()

# Build output string
output_lines = []
output_lines.append("=" * 100)
output_lines.append("QUERY RESULTS:")
output_lines.append("=" * 100)
output_lines.append("\\n")
output_lines.append(pandas_df.to_string())
output_lines.append("\\n")
output_lines.append("=" * 100)
output_lines.append(f"Total records: {{len(pandas_df)}}")
output_lines.append("=" * 100)

# IMPORTANT: Write output to DBFS so we can retrieve it
output_text = "\\n".join(output_lines)
dbutils.fs.put("{output_file_path}", output_text, overwrite=True)

# Also display in notebook (for UI visibility)
print(output_text)

# COMMAND ----------

# Add more analysis cells as needed
# Each cell that produces output should write to DBFS

# Example: Additional analysis
summary_stats = {{
    "total_rows": len(pandas_df),
    "columns": list(pandas_df.columns),
    "sample_size": min(10, len(pandas_df))
}}

summary_text = f"\\nSUMMARY STATISTICS:\\n{{summary_stats}}"
dbutils.fs.put("{output_file_path}", output_text + "\\n" + summary_text, overwrite=True)
print(summary_text)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Analysis completed successfully!
# MAGIC Output written to: {output_file_path}
"""

# Example usage:
if __name__ == "__main__":
    print("Notebook Template")
    print("=" * 80)
    print("This is a template for creating notebooks with terminal output.")
    print("Copy the notebook_template variable and modify for your use case.")
    print()
    print("Output file path:", output_file_path)
    print()
    print("To use:")
    print("1. Modify the SQL query in the template")
    print("2. Use this template with create_and_run_notebook_job.py")
    print("3. Output will be visible in terminal after job completes")

