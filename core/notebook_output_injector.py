#!/usr/bin/env python3
"""
Notebook Output Injector

Automatically injects NotebookOutput framework into Databricks notebook content.
This allows all notebooks to automatically capture output without manual setup.
"""

from typing import Optional


def inject_notebook_output(
    notebook_content: str,
    output_path: Optional[str] = None,
    job_name: Optional[str] = None,
    auto_write: bool = True
) -> str:
    """
    Inject NotebookOutput framework into notebook content.
    
    Args:
        notebook_content: Original notebook content
        output_path: Optional specific output path (auto-generated if None)
        job_name: Optional job name for output path generation
        auto_write: If True, automatically call write_to_dbfs() at the end
    
    Returns:
        Notebook content with NotebookOutput framework injected
    """
    # Check if NotebookOutput is already present
    if "class NotebookOutput" in notebook_content or "NotebookOutput" in notebook_content:
        # Already has NotebookOutput, just ensure write_to_dbfs() is called
        if auto_write and "output.write_to_dbfs()" not in notebook_content:
            # Add write_to_dbfs() at the end if not present
            notebook_content = add_auto_write(notebook_content)
        return notebook_content
    
    # Generate output path if not provided
    if output_path is None:
        if job_name:
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_job_name = job_name.replace(" ", "_").replace("/", "_")
            output_path = f"/tmp/notebook_outputs/{safe_job_name}_{timestamp}.txt"
        else:
            output_path = "/tmp/notebook_outputs/notebook_output.txt"
    
    # NotebookOutput class definition (inline version for Databricks)
    # Use triple-quoted string with proper escaping for Databricks
    notebook_output_class = f'''# Auto-injected NotebookOutput framework
import json
from datetime import datetime

class NotebookOutput:
    def __init__(self, output_path="{output_path}"):
        self.output_path = output_path
        self.sections = []
        self.errors = []
    
    def add_section(self, title, content):
        self.sections.append({{'title': title, 'content': content}})
    
    def print(self, *args, sep=" ", end="\\n"):
        message = sep.join(str(arg) for arg in args) + end
        print(message, end="")  # Print to console
        # Only capture if message has content
        message_stripped = message.strip()
        if message_stripped:
            self.add_section("Print Output", message_stripped)
    
    def add_dataframe(self, title, df, max_rows=100):
        try:
            import pandas as pd
            if hasattr(df, 'toPandas'):
                df = df.toPandas()
            elif not isinstance(df, pd.DataFrame):
                df = pd.DataFrame(df)
            display_df = df.head(max_rows)
            content = display_df.to_string()
            if len(df) > max_rows:
                content += f"\\n\\n... ({{len(df) - max_rows}} more rows not shown)"
            self.add_section(title, content)
        except Exception as e:
            self.add_section(title, f"Error displaying DataFrame: {{str(e)}}")
    
    def add_query_result(self, title, query, results, max_rows=100):
        try:
            import pandas as pd
            if hasattr(results, 'toPandas'):
                df = results.toPandas()
            elif isinstance(results, pd.DataFrame):
                df = results
            else:
                df = pd.DataFrame(results)
            display_df = df.head(max_rows)
            content_lines = []
            content_lines.append(f"Query:")
            content_lines.append("-" * 80)
            content_lines.append(query)
            content_lines.append("")
            content_lines.append("Results:")
            content_lines.append("-" * 80)
            content_lines.append(display_df.to_string())
            if len(df) > max_rows:
                content_lines.append(f"\\n... ({{len(df) - max_rows}} more rows not shown)")
            self.add_section(title, "\\n".join(content_lines))
        except Exception as e:
            self.add_section(title, f"Error displaying query results: {{str(e)}}")
    
    def add_error(self, error_message, error_type="Error"):
        self.errors.append(f"{{error_type}}: {{error_message}}")
        self.add_section(f"{{error_type}}", error_message)
    
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
        output_lines.append(f"Generated: {{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}}")
        output_lines.append("")
        
        # Filter out empty sections
        section_num = 0
        for section in self.sections:
            if not section.get('content', '').strip():
                continue
            section_num += 1
            output_lines.append("-" * 100)
            output_lines.append(f"📊 [{{section_num}}] {{section['title']}}")
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

# Initialize output handler (available as 'output' variable)
# IMPORTANT: This must execute successfully for output variable to be available
try:
    output = NotebookOutput(output_path="{output_path}")
    # Verify it worked - this print will show in job output if there's an issue
    print("✅ NotebookOutput framework initialized - output variable available")
    
    # Intercept regular print() statements to capture them automatically
    import builtins
    _original_print = builtins.print
    
    def _capturing_print(*args, **kwargs):
        """Wrapper around print() that captures output."""
        # Call original print
        _original_print(*args, **kwargs)
        # Also capture for output file
        try:
            message = ' '.join(str(arg) for arg in args)
            if message.strip():
                output.add_section("Print Output", message.strip())
        except:
            pass  # Don't break if capture fails
    
    # Replace built-in print with our capturing version
    builtins.print = _capturing_print
    
except Exception as init_error:
    # If initialization fails, create a minimal fallback
    print(f"⚠️  NotebookOutput initialization failed: {{init_error}}")
    print("   Creating minimal fallback...")
    class MinimalOutput:
        def __init__(self):
            self.sections = []
            self.errors = []
            self.output_path = "{output_path}"
        def print(self, *args, sep=" ", end="\\n"):
            # Just print, don't capture
            print(*args, sep=sep, end=end)
        def add_section(self, title, content):
            pass
        def write_to_dbfs(self):
            print("⚠️  Minimal output handler - output not saved to DBFS")
    output = MinimalOutput()
    print("✅ Fallback output handler created")

# COMMAND ----------
'''
    
    # Find the insertion point (after first COMMAND ---------- or at the beginning)
    insertion_point = find_insertion_point(notebook_content)
    
    # Inject the framework
    if insertion_point == 0:
        # Insert at the beginning
        modified_content = notebook_output_class + "\n" + notebook_content
    else:
        # Insert after first COMMAND ----------
        modified_content = (
            notebook_content[:insertion_point] + 
            notebook_output_class + 
            notebook_content[insertion_point:]
        )
    
    # Add auto-write at the end if requested
    if auto_write:
        modified_content = add_auto_write(modified_content)
    
    return modified_content


def find_insertion_point(notebook_content: str) -> int:
    """
    Find the best insertion point for NotebookOutput framework.
    
    Returns:
        Index where to insert the framework
    """
    # Look for first COMMAND ---------- marker
    command_marker = "# COMMAND ----------"
    first_command = notebook_content.find(command_marker)
    
    if first_command != -1:
        # Find the end of this line
        end_of_line = notebook_content.find("\n", first_command)
        if end_of_line != -1:
            return end_of_line + 1
    
    # If no COMMAND marker, insert at the beginning
    return 0


def add_auto_write(notebook_content: str) -> str:
    """
    Add output.write_to_dbfs() at the end of notebook if not present.
    
    Args:
        notebook_content: Notebook content
    
    Returns:
        Modified notebook content with auto-write added
    """
    # Check if write_to_dbfs is already called
    if "output.write_to_dbfs()" in notebook_content:
        return notebook_content
    
    # Find the last COMMAND ---------- marker
    last_command = notebook_content.rfind("# COMMAND ----------")
    
    if last_command != -1:
        # Find the end of this section
        end_of_section = notebook_content.find("\n", last_command)
        if end_of_section != -1:
            # Add auto-write after the last section
            auto_write_code = '''

# Auto-injected: Write output to DBFS
try:
    output.write_to_dbfs()
except NameError:
    # output not initialized, skip
    pass
except Exception as e:
    print(f"⚠️  Error writing output: {{e}}")
'''
            return notebook_content[:end_of_section + 1] + auto_write_code + notebook_content[end_of_section + 1:]
    
    # If no COMMAND marker, append at the end
    auto_write_code = '''

# Auto-injected: Write output to DBFS
try:
    output.write_to_dbfs()
except NameError:
    # output not initialized, skip
    pass
except Exception as e:
    print(f"⚠️  Error writing output: {{e}}")
'''
    return notebook_content + auto_write_code


def is_output_enabled(notebook_content: str) -> bool:
    """
    Check if NotebookOutput framework is already enabled in notebook.
    
    Args:
        notebook_content: Notebook content
    
    Returns:
        True if NotebookOutput is present, False otherwise
    """
    return "class NotebookOutput" in notebook_content or "NotebookOutput" in notebook_content

