#!/usr/bin/env python3
"""
DBFS Output Injector

Automatically injects code to write output to DBFS for terminal display.
This is the WORKING approach that actually shows output in terminal.
"""

from typing import Optional


def inject_dbfs_output(notebook_content: str, job_name: Optional[str] = None) -> str:
    """
    Inject DBFS output writing code into notebook.
    
    This adds:
    1. Helper function to write output to DBFS
    2. Automatic output collection
    3. Automatic writing at the end
    
    Args:
        notebook_content: Original notebook content
        job_name: Optional job name for output path
    
    Returns:
        Notebook content with DBFS output code injected
    """
    # Generate output path
    if job_name:
        safe_job_name = job_name.replace(" ", "_").replace("/", "_")
        output_path = f"/tmp/notebook_outputs/{safe_job_name}_output.txt"
    else:
        output_path = "/tmp/notebook_outputs/notebook_output.txt"
    
    # Helper code to inject
    helper_code = f'''
# Auto-injected: DBFS Output Helper (for terminal display)
# This ensures all output is written to DBFS and visible in terminal

import io
from datetime import datetime

# Output collection
_output_lines = []

def _add_output(text):
    """Add text to output collection."""
    _output_lines.append(str(text))

def _write_output_to_dbfs():
    """Write collected output to DBFS."""
    try:
        # Build final output
        header = '=' * 80 + chr(10)
        header += 'NOTEBOOK OUTPUT' + chr(10)
        header += f'Generated: {{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}}' + chr(10)
        header += '=' * 80 + chr(10) + chr(10)
        
        output_text = header + chr(10).join(_output_lines)
        
        # Write to DBFS
        dbutils.fs.put("{output_path}", output_text, overwrite=True)
        print(f'✅ Output written to: {output_path}')
    except Exception as e:
        print(f'⚠️  Error writing output: {{e}}')

# Helper function for easy output
def show_output(title, content):
    """Add output section (for terminal display)."""
    _add_output('=' * 80)
    _add_output(title)
    _add_output('=' * 80)
    _add_output('')
    _add_output(str(content))
    _add_output('')

# Helper function for query results
def show_query_results(title, pandas_df, summary=None):
    """Show query results in output."""
    _add_output('=' * 80)
    _add_output(title)
    _add_output('=' * 80)
    _add_output('')
    _add_output(pandas_df.to_string(index=False))
    _add_output('')
    if summary:
        _add_output('=' * 80)
        _add_output(summary)
        _add_output('=' * 80)
    _add_output('')

# COMMAND ----------
'''
    
    # Find insertion point
    insertion_point = _find_insertion_point(notebook_content)
    
    # Inject helper code
    if insertion_point == 0:
        modified_content = helper_code + "\n" + notebook_content
    else:
        modified_content = (
            notebook_content[:insertion_point] + 
            helper_code + 
            notebook_content[insertion_point:]
        )
    
    # Add auto-write at the end
    modified_content = _add_auto_write(modified_content)
    
    return modified_content


def _find_insertion_point(notebook_content: str) -> int:
    """Find the best insertion point for helper code."""
    command_marker = "# COMMAND ----------"
    first_command = notebook_content.find(command_marker)
    
    if first_command != -1:
        end_of_line = notebook_content.find("\n", first_command)
        if end_of_line != -1:
            return end_of_line + 1
    
    return 0


def _add_auto_write(notebook_content: str) -> str:
    """Add automatic output writing at the end of notebook."""
    # Check if already present
    if "_write_output_to_dbfs()" in notebook_content:
        return notebook_content
    
    # Find last COMMAND marker
    last_command = notebook_content.rfind("# COMMAND ----------")
    
    auto_write_code = '''

# Auto-injected: Write output to DBFS (for terminal display)
_write_output_to_dbfs()
'''
    
    if last_command != -1:
        end_of_section = notebook_content.find("\n", last_command)
        if end_of_section != -1:
            return notebook_content[:end_of_section + 1] + auto_write_code + notebook_content[end_of_section + 1:]
    
    return notebook_content + auto_write_code

