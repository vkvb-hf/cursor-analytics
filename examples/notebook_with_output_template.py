#!/usr/bin/env python3
"""
Template: Databricks Notebook with Output Framework

This template shows how to use the NotebookOutput framework to capture
all print statements and results, then display them in terminal after job completion.
"""

# This is the notebook content that will be created in Databricks
NOTEBOOK_TEMPLATE = """# Databricks notebook source
# MAGIC %md
# MAGIC # Example Notebook with Output Framework
# MAGIC 
# MAGIC This notebook demonstrates how to use the NotebookOutput framework
# MAGIC to capture all output and display it in terminal after job completion.

# COMMAND ----------

# Import the output framework
# Note: This assumes the NotebookOutput class is available in your Databricks environment
# You may need to install it or make it available via workspace files

# For now, we'll define a simple version inline
import json
from datetime import datetime

class NotebookOutput:
    def __init__(self, output_path="/tmp/notebook_outputs/notebook_output.txt"):
        self.output_path = output_path
        self.sections = []
        self.errors = []
    
    def add_section(self, title, content):
        self.sections.append({'title': title, 'content': content})
    
    def print(self, *args, sep=" ", end="\\n"):
        message = sep.join(str(arg) for arg in args) + end
        print(message, end="")  # Print to console
        self.add_section("Print Output", message.strip())  # Capture for file
    
    def write_to_dbfs(self):
        # Ensure directory exists
        dir_path = "/".join(self.output_path.split("/")[:-1])
        if dir_path:
            dbutils.fs.mkdirs(dir_path)
        
        # Build output
        output_lines = []
        output_lines.append("=" * 100)
        output_lines.append("NOTEBOOK OUTPUT")
        output_lines.append("=" * 100)
        output_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        output_lines.append("")
        
        for i, section in enumerate(self.sections, 1):
            output_lines.append("-" * 100)
            output_lines.append(f"📊 [{i}] {section['title']}")
            output_lines.append("-" * 100)
            output_lines.append(section['content'])
            output_lines.append("")
        
        if self.errors:
            output_lines.append("-" * 100)
            output_lines.append("❌ ERRORS")
            output_lines.append("-" * 100)
            for error in self.errors:
                output_lines.append(error)
            output_lines.append("")
        
        output_lines.append("=" * 100)
        output_text = "\\n".join(output_lines)
        
        # Write to DBFS
        dbutils.fs.put(self.output_path, output_text, overwrite=True)
        print("\\n✅ Output written to:", self.output_path)

# COMMAND ----------

# Initialize output handler
output = NotebookOutput(output_path="/tmp/notebook_outputs/example_notebook_output.txt")

# COMMAND ----------

# Example 1: Print statements
output.print("=" * 80)
output.print("Starting Analysis")
output.print("=" * 80)
output.print("")
output.print("This is a test notebook to demonstrate output capture.")
output.print("All print statements are captured and saved to DBFS.")
output.print("")

# COMMAND ----------

# Example 2: Query results
output.print("\\nRunning SQL query...")

query = \"\"\"SELECT 
    business_unit,
    COUNT(*) as customer_count,
    COUNT(DISTINCT customer_id) as unique_customers
FROM payments_hf.duplicate_customers
WHERE subscription_date_local >= CURRENT_DATE - INTERVAL 7 DAYS
GROUP BY business_unit
ORDER BY customer_count DESC
LIMIT 10\"\"\"

try:
    result_df = spark.sql(query)
    pandas_df = result_df.toPandas()
    
    output.print("\\nQuery Results:")
    output.print("-" * 80)
    output.print(pandas_df.to_string())
    output.print("")
    output.print(f"Total rows: {len(pandas_df)}")
    
    # Also add as a section
    output.add_section("Query Results", f"Query:\\n{query}\\n\\nResults:\\n{pandas_df.to_string()}")
    
except Exception as e:
    error_msg = f"Error running query: {str(e)}"
    output.print(f"❌ {error_msg}")
    output.errors.append(error_msg)

# COMMAND ----------

# Example 3: Data processing
output.print("\\nProcessing data...")

try:
    # Example: Get some statistics
    stats_query = \"\"\"SELECT 
        COUNT(*) as total_duplicates,
        COUNT(DISTINCT business_unit) as business_units,
        MIN(subscription_date_local) as earliest_date,
        MAX(subscription_date_local) as latest_date
    FROM payments_hf.duplicate_customers
    WHERE subscription_date_local >= CURRENT_DATE - INTERVAL 7 DAYS\"\"\"
    
    stats_df = spark.sql(stats_query)
    stats_pandas = stats_df.toPandas()
    
    output.print("\\nStatistics:")
    output.print("-" * 80)
    output.print(stats_pandas.to_string())
    
    output.add_section("Statistics", stats_pandas.to_string())
    
except Exception as e:
    error_msg = f"Error processing data: {str(e)}"
    output.print(f"❌ {error_msg}")
    output.errors.append(error_msg)

# COMMAND ----------

# Example 4: Summary
output.print("\\n" + "=" * 80)
output.print("Analysis Complete")
output.print("=" * 80)
output.print("")
output.print("All output has been captured and will be displayed in terminal")
output.print("after the job completes.")

# COMMAND ----------

# CRITICAL: Write output to DBFS
# This is what allows the output to be retrieved after job completion
output.write_to_dbfs()

output.print("\\n✅ Notebook execution complete!")
output.print(f"📁 Output saved to: {output.output_path}")
"""


def create_example_notebook():
    """Create an example notebook using the template."""
    from databricks_api import DatabricksAPI
    
    db = DatabricksAPI()
    
    print("Creating example notebook with output framework...")
    
    result = db.job_runner.create_and_run(
        notebook_path="/Workspace/Users/visal.kumar@hellofresh.com/example_notebook_with_output",
        notebook_content=NOTEBOOK_TEMPLATE,
        job_name="Example Notebook with Output",
        timeout_seconds=600,
        poll_interval=5,
        max_wait=600,
        show_output=True,
        auto_read_output=True  # Automatically read output after job completes
    )
    
    if result.get('success'):
        print("\n✅ Example notebook executed successfully!")
        print(f"   Job ID: {result.get('job_id')}")
        print(f"   Run ID: {result.get('run_id')}")
    else:
        print("\n❌ Notebook execution failed")
        print(f"   Error: {result.get('error')}")


if __name__ == "__main__":
    create_example_notebook()

