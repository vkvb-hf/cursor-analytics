#!/usr/bin/env python3
"""
Example: Create and run a Databricks notebook with output framework

This demonstrates the complete workflow:
1. Create a notebook with print statements
2. Run it as a job
3. Automatically retrieve and display output from DBFS
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from databricks_api import DatabricksAPI

# Notebook content with output framework
NOTEBOOK_CONTENT = """# Databricks notebook source
# MAGIC %md
# MAGIC # Test Notebook with Output
# MAGIC 
# MAGIC This notebook demonstrates capturing print statements and displaying them in terminal.

# COMMAND ----------

# Simple NotebookOutput class (inline version)
import json
from datetime import datetime

class NotebookOutput:
    def __init__(self, output_path="/tmp/notebook_outputs/test_output.txt"):
        self.output_path = output_path
        self.sections = []
        self.errors = []
    
    def add_section(self, title, content):
        self.sections.append({'title': title, 'content': content})
    
    def print(self, *args, sep=" ", end="\\n"):
        message = sep.join(str(arg) for arg in args) + end
        print(message, end="")  # Print to console
        # Only capture if message has content
        message_stripped = message.strip()
        if message_stripped:
            self.add_section("Print Output", message_stripped)  # Capture for file
    
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
        
        # Filter out empty sections
        section_num = 0
        for section in self.sections:
            if not section.get('content', '').strip():
                continue
            section_num += 1
            output_lines.append("-" * 100)
            output_lines.append(f"📊 [{section_num}] {section['title']}")
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

# Initialize output
output = NotebookOutput(output_path="/tmp/notebook_outputs/test_output.txt")

# COMMAND ----------

# Print statements
output.print("=" * 80)
output.print("Starting Test Notebook")
output.print("=" * 80)
output.print("")
output.print("This is a test to demonstrate output capture.")
output.print("All print statements are captured.")
output.print("")

# COMMAND ----------

# Example query
output.print("\\nRunning test query...")

try:
    query = "SELECT 1 as test_column, 'Hello World' as message"
    result_df = spark.sql(query)
    pandas_df = result_df.toPandas()
    
    output.print("\\nQuery Results:")
    output.print("-" * 80)
    output.print(pandas_df.to_string())
    output.print("")
    
    output.add_section("Query Results", pandas_df.to_string())
    
except Exception as e:
    error_msg = f"Error: {str(e)}"
    output.print(f"❌ {error_msg}")
    output.errors.append(error_msg)

# COMMAND ----------

# More print statements
output.print("\\n" + "=" * 80)
output.print("Test Complete")
output.print("=" * 80)

# COMMAND ----------

# CRITICAL: Write output to DBFS
output.write_to_dbfs()

output.print("\\n✅ Output saved to DBFS!")
"""


def main():
    """Run the example."""
    print("=" * 80)
    print("Example: Notebook with Output Framework")
    print("=" * 80)
    print()
    
    # Initialize API
    db = DatabricksAPI()
    
    # Create and run notebook
    result = db.job_runner.create_and_run(
        notebook_path="/Workspace/Users/visal.kumar@hellofresh.com/test_notebook_with_output",
        notebook_content=NOTEBOOK_CONTENT,
        job_name="Test Notebook with Output",
        timeout_seconds=600,
        poll_interval=5,
        max_wait=600,
        show_output=True,
        auto_read_output=True  # This automatically reads output from DBFS after job completes
    )
    
    # Check result
    if result.get('success'):
        print("\n" + "=" * 80)
        print("✅ SUCCESS: Notebook executed and output retrieved!")
        print("=" * 80)
        print(f"Job ID: {result.get('job_id')}")
        print(f"Run ID: {result.get('run_id')}")
        print(f"Notebook: {result.get('notebook_path')}")
    else:
        print("\n" + "=" * 80)
        print("❌ FAILED: Notebook execution failed")
        print("=" * 80)
        print(f"Error: {result.get('error')}")
        sys.exit(1)


if __name__ == "__main__":
    main()

