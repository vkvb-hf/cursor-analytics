#!/usr/bin/env python3
"""
Universal Output Capture for Databricks Notebooks

This module provides a simple, universal way to capture all notebook output
and write it to DBFS, which can then be retrieved and displayed in terminal.

Works by redirecting stdout/stderr to a file that's written to DBFS.
"""

def get_output_capture_code(output_path: str) -> str:
    """
    Generate code to capture all stdout/stderr and write to DBFS.
    
    This is a simpler, more reliable approach than print interception.
    It works universally for any notebook without complex scope management.
    
    Args:
        output_path: DBFS path where output will be written
    
    Returns:
        Python code string to inject into notebook
    """
    return f'''
# Auto-injected: Universal Output Capture
# This captures ALL output (print statements, query results, errors) and writes to DBFS
import sys
import io
from datetime import datetime

# Create a custom file-like object that writes to both console and buffer
class TeeOutput:
    def __init__(self, original_stream, output_path):
        self.original_stream = original_stream
        self.output_path = output_path
        self.buffer = io.StringIO()
        self.captured_lines = []
    
    def write(self, text):
        # Write to original stream (console)
        self.original_stream.write(text)
        # Also capture in buffer
        self.buffer.write(text)
        self.captured_lines.append(text)
        return len(text)
    
    def flush(self):
        self.original_stream.flush()
        self.buffer.flush()
    
    def write_to_dbfs(self):
        """Write captured output to DBFS file."""
        try:
            # Get all captured output
            output_text = ''.join(self.captured_lines)
            
            # Add header
            header = f\"\"\"{'=' * 100}
NOTEBOOK OUTPUT
{'=' * 100}
Generated: {{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}}
{'=' * 100}

\"\"\"
            
            full_output = header + output_text
            
            # Write to DBFS
            dbutils.fs.put(self.output_path, full_output, overwrite=True)
            print(f\"\\n✅ Output written to: {{self.output_path}}\")
        except Exception as e:
            print(f\"⚠️  Error writing output to DBFS: {{e}}\")

# Redirect stdout and stderr
_original_stdout = sys.stdout
_original_stderr = sys.stderr

_tee_stdout = TeeOutput(_original_stdout, "{output_path}")
_tee_stderr = TeeOutput(_original_stderr, "{output_path}")

sys.stdout = _tee_stdout
sys.stderr = _tee_stderr

# Store references for cleanup
import sys as _sys_module
if not hasattr(_sys_module.modules.get('__main__', _sys_module), '_output_capture'):
    _sys_module.modules['__main__']._output_capture = {{
        'stdout': _tee_stdout,
        'stderr': _tee_stderr,
        'output_path': "{output_path}"
    }}

# Function to write output at end of notebook
def _write_output_to_dbfs():
    try:
        if hasattr(_sys_module.modules.get('__main__', None), '_output_capture'):
            capture = _sys_module.modules['__main__']._output_capture
            capture['stdout'].write_to_dbfs()
    except Exception as e:
        print(f"⚠️  Error in output capture cleanup: {{e}}")

# COMMAND ----------
'''

