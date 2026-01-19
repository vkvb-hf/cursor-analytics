#!/usr/bin/env python3
"""
Quick Test: Notebook Output Framework

This is a simple test to verify the output framework works.
Run this to see the complete workflow in action.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from databricks_api import DatabricksAPI

# Simple test notebook
NOTEBOOK = """# Databricks notebook source
# MAGIC %md
# MAGIC # Test Notebook Output
# MAGIC 
# MAGIC This is a simple test to verify output capture works.

# COMMAND ----------

# Simple NotebookOutput class
from datetime import datetime

class NotebookOutput:
    def __init__(self, output_path="/tmp/notebook_outputs/test_output.txt"):
        self.output_path = output_path
        self.sections = []
        self.errors = []
    
    def print(self, *args, sep=" ", end="\\n"):
        message = sep.join(str(arg) for arg in args) + end
        print(message, end="")
        # Only capture if message has content
        message_stripped = message.strip()
        if message_stripped:
            self.add_section("Print Output", message_stripped)
    
    def add_section(self, title, content):
        self.sections.append({'title': title, 'content': content})
    
    def write_to_dbfs(self):
        dir_path = "/".join(self.output_path.split("/")[:-1])
        if dir_path:
            dbutils.fs.mkdirs(dir_path)
        
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
        
        output_lines.append("=" * 100)
        output_text = "\\n".join(output_lines)
        dbutils.fs.put(self.output_path, output_text, overwrite=True)
        print("\\n✅ Output written to:", self.output_path)

# COMMAND ----------

output = NotebookOutput()

output.print("=" * 80)
output.print("Test Notebook Output Framework")
output.print("=" * 80)
output.print("")
output.print("This is a test to verify output capture works.")
output.print("")
output.print("Print statement 1: Hello World")
output.print("Print statement 2: Testing output framework")
output.print("Print statement 3: All output should be captured")
output.print("")

# Simple query
output.print("Running test query...")
try:
    result = spark.sql("SELECT 'Test' as message, 123 as number")
    pandas_df = result.toPandas()
    output.print("\\nQuery Results:")
    output.print(pandas_df.to_string())
    output.add_section("Query Results", pandas_df.to_string())
except Exception as e:
    output.print(f"❌ Error: {str(e)}")
    output.errors.append(str(e))

output.print("\\n" + "=" * 80)
output.print("Test Complete")
output.print("=" * 80)

# Write output
output.write_to_dbfs()
"""


def main():
    """Run the test."""
    print("=" * 80)
    print("Test: Notebook Output Framework")
    print("=" * 80)
    print()
    
    db = DatabricksAPI()
    
    result = db.job_runner.create_and_run(
        notebook_path="/Workspace/Users/visal.kumar@hellofresh.com/test_notebook_output",
        notebook_content=NOTEBOOK,
        job_name="Test Notebook Output",
        timeout_seconds=300,
        poll_interval=5,
        max_wait=300,
        show_output=True,
        auto_read_output=True
    )
    
    if result.get('success'):
        print("\n✅ Test passed! Output was captured and displayed.")
    else:
        print("\n❌ Test failed!")
        print(f"Error: {result.get('error')}")
        sys.exit(1)


if __name__ == "__main__":
    main()

