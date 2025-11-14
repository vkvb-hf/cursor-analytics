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
    auto_write: bool = True,
    use_universal_capture: bool = True  # New: Use simpler stdout/stderr capture
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
        
        # If no sections were captured, add a note
        if section_num == 0:
            output_lines.append("-" * 100)
            output_lines.append("⚠️  NO OUTPUT CAPTURED")
            output_lines.append("-" * 100)
            output_lines.append("No print statements or output sections were captured.")
            output_lines.append("")
            output_lines.append("Possible reasons:")
            output_lines.append("1. Print interception may not have worked")
            output_lines.append("2. No print() statements were executed")
            output_lines.append("3. Output variable was not accessible to print interceptor")
            output_lines.append("")
            output_lines.append("To ensure output is captured:")
            output_lines.append("- Use output.print() explicitly")
            output_lines.append("- Use output.add_section() for structured output")
            output_lines.append("")
        
        if self.errors:
            output_lines.append("-" * 100)
            output_lines.append("❌ ERRORS")
            output_lines.append("-" * 100)
            for error in self.errors:
                output_lines.append(error)
            output_lines.append("")
        
        output_lines.append("=" * 100)
        output_lines.append(f"Output file: {{self.output_path}}")
        output_lines.append(f"Total sections captured: {{section_num}}")
        output_lines.append("=" * 100)
        output_text = "\\n".join(output_lines)
        
        # Write to DBFS
        dbutils.fs.put(self.output_path, output_text, overwrite=True)
        print("\\n✅ Output written to:", self.output_path)
        if section_num == 0:
            print("⚠️  Warning: No sections were captured in this run")

# Initialize output handler (available as 'output' variable)
# IMPORTANT: This must execute successfully for output variable to be available
try:
    output = NotebookOutput(output_path="{output_path}")
    # Verify it worked - this print will show in job output if there's an issue
    print("✅ NotebookOutput framework initialized - output variable available")
    
    # Intercept regular print() statements to capture them automatically
    # IMPORTANT: Store output in a way that persists across cells
    import builtins
    # Get the TRUE built-in print function (not a wrapper)
    # Store it in a way that persists
    if not hasattr(builtins, '_true_print'):
        builtins._true_print = builtins.print
    _original_print = builtins._true_print
    
    # Store output reference in a way that works across cells
    # Use a module-level variable that persists across cell executions
    import sys
    # Store in __main__ module which persists across cells in Databricks
    main_module = sys.modules.get('__main__', None)
    if main_module:
        main_module._notebook_output_handler = output
        # Also store in a global dict that persists
        if not hasattr(main_module, '_notebook_globals'):
            main_module._notebook_globals = {{}}
        main_module._notebook_globals['output'] = output
    
    def _capturing_print(*args, **kwargs):
        """Wrapper around print() that captures output."""
        # Call original print first
        _original_print(*args, **kwargs)
        # Also capture for output file
        try:
            # Try multiple ways to get output reference
            output_ref = None
            
            # Method 1: Try globals() in current scope
            try:
                if 'output' in globals():
                    output_ref = globals()['output']
            except:
                pass
            
            # Method 2: Try __main__ module storage
            if not output_ref:
                try:
                    main_mod = sys.modules.get('__main__', None)
                    if main_mod and hasattr(main_mod, '_notebook_output_handler'):
                        output_ref = main_mod._notebook_output_handler
                    elif main_mod and hasattr(main_mod, '_notebook_globals'):
                        output_ref = main_mod._notebook_globals.get('output')
                except:
                    pass
            
            # Method 3: Try to find output in current frame
            if not output_ref:
                try:
                    import inspect
                    frame = inspect.currentframe()
                    if frame:
                        # Check frame's globals
                        frame_globals = frame.f_globals
                        if 'output' in frame_globals:
                            output_ref = frame_globals['output']
                except:
                    pass
            
            if output_ref:
                # Handle sep and end kwargs properly
                sep = kwargs.get('sep', ' ')
                end = kwargs.get('end', '\\n')
                message = sep.join(str(arg) for arg in args) + end
                message_stripped = message.strip()
                if message_stripped:
                    output_ref.add_section("Print Output", message_stripped)
        except Exception as e:
            # Don't break if capture fails - silently continue
            # Logging here would cause infinite recursion
            pass
    
    # Replace built-in print with our capturing version
    builtins.print = _capturing_print
    
    # Also re-initialize in each cell by adding this to auto-write
    # This ensures print interception is set up in every cell
    
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
    
    # Choose injection method
    if use_universal_capture:
        # Use simpler stdout/stderr redirection (universal, works for any notebook)
        from core.universal_output_capture import get_output_capture_code
        
        capture_code = get_output_capture_code(output_path)
        
        # Find insertion point
        insertion_point = find_insertion_point(notebook_content)
        
        # Inject at the beginning
        if insertion_point == 0:
            modified_content = capture_code + "\n" + notebook_content
        else:
            modified_content = (
                notebook_content[:insertion_point] + 
                capture_code + 
                notebook_content[insertion_point:]
            )
        
        # Add auto-write at the end
        if auto_write:
            # Add call to write output at the end
            auto_write_code = '''

# Auto-injected: Write captured output to DBFS
_write_output_to_dbfs()
'''
            # Find last COMMAND marker
            last_command = modified_content.rfind("# COMMAND ----------")
            if last_command != -1:
                end_of_section = modified_content.find("\n", last_command)
                if end_of_section != -1:
                    modified_content = modified_content[:end_of_section + 1] + auto_write_code + modified_content[end_of_section + 1:]
            else:
                modified_content = modified_content + auto_write_code
        
        return modified_content
    else:
        # Use NotebookOutput framework (original approach)
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
        
        # Add print interception setup at the start of each user cell
        modified_content = add_print_interception_to_cells(modified_content)
        
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


def add_print_interception_to_cells(notebook_content: str) -> str:
    """
    Add print interception setup at the start of each user cell.
    This ensures print interception works even if Databricks resets builtins between cells.
    
    Args:
        notebook_content: Notebook content
    
    Returns:
        Modified notebook content with print interception in each cell
    """
    # Setup code to re-initialize print interception at the start of each cell
    setup_code = '''
# Auto-injected: Setup print interception (re-initialize in case Databricks reset it)
try:
    import builtins
    import sys
    
    # Get output reference from persistent storage
    output_ref = None
    if 'output' in globals():
        output_ref = globals()['output']
    elif hasattr(sys.modules.get('__main__', None), '_notebook_output_handler'):
        output_ref = sys.modules['__main__']._notebook_output_handler
        # Also restore to globals for this cell
        if output_ref:
            globals()['output'] = output_ref
    
    # Re-setup print interception if we have output reference
    if output_ref:
        # IMPORTANT: Get the TRUE built-in print, not a wrapped version
        if hasattr(builtins, '_true_print'):
            _original_print = builtins._true_print
        else:
            # Store it for future use
            builtins._true_print = builtins.print
            _original_print = builtins._true_print
            # But if current print is already a wrapper, we need the real one
            if hasattr(builtins.print, '__name__') and builtins.print.__name__ == '_capturing_print':
                # Current print is our wrapper, get the real one from Python's builtins
                import builtins as _real_builtins
                _original_print = _real_builtins.__dict__.get('print', print)
                builtins._true_print = _original_print
        
        def _capturing_print(*args, **kwargs):
            _original_print(*args, **kwargs)
            try:
                sep = kwargs.get('sep', ' ')
                end = kwargs.get('end', '\\n')
                message = sep.join(str(arg) for arg in args) + end
                if message.strip():
                    output_ref.add_section("Print Output", message.strip())
            except:
                pass
        
        builtins.print = _capturing_print
except:
    pass

'''
    
    # Split by COMMAND markers
    parts = notebook_content.split("# COMMAND ----------")
    
    if len(parts) <= 1:
        # No COMMAND markers, return as is
        return notebook_content
    
    # Add setup code at the start of each user cell
    # The first part (before first COMMAND) contains the NotebookOutput class - keep as is
    result_parts = [parts[0]]
    
    # Add setup code to ALL subsequent cells (user cells)
    # This ensures print interception is re-initialized in each cell
    for part in parts[1:]:
        # Always add setup code at the start of each user cell
        # This re-initializes print interception in case Databricks reset it
        result_parts.append("# COMMAND ----------" + setup_code + part)
    
    return "".join(result_parts)


def add_auto_write(notebook_content: str) -> str:
    """
    Add output.write_to_dbfs() at the end of notebook if not present.
    Also re-initializes print interception in each cell.
    
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
    
    # Setup code to re-initialize print interception and write output
    auto_write_code = '''

# Auto-injected: Re-initialize print interception (Databricks may reset builtins between cells)
try:
    import builtins
    import sys
    
    # Get output reference from persistent storage
    output_ref = None
    if 'output' in globals():
        output_ref = globals()['output']
    elif hasattr(sys.modules.get('__main__', None), '_notebook_output_handler'):
        output_ref = sys.modules['__main__']._notebook_output_handler
        # Also restore to globals for this cell
        if output_ref:
            globals()['output'] = output_ref
    
    # Re-setup print interception if we have output reference
    if output_ref:
        # IMPORTANT: Get the TRUE built-in print, not a wrapped version
        # Use the stored true print if available, otherwise get it safely
        if hasattr(builtins, '_true_print'):
            _original_print = builtins._true_print
        else:
            # Store it for future use
            builtins._true_print = builtins.print
            _original_print = builtins._true_print
            # But if current print is already a wrapper, we need the real one
            if hasattr(builtins.print, '__name__') and builtins.print.__name__ == '_capturing_print':
                # Current print is our wrapper, get the real one from Python's builtins
                import builtins as _real_builtins
                _original_print = _real_builtins.__dict__.get('print', print)
                builtins._true_print = _original_print
        
        def _capturing_print(*args, **kwargs):
            _original_print(*args, **kwargs)
            try:
                sep = kwargs.get('sep', ' ')
                end = kwargs.get('end', '\\n')
                message = sep.join(str(arg) for arg in args) + end
                if message.strip():
                    output_ref.add_section("Print Output", message.strip())
            except:
                pass
        
        builtins.print = _capturing_print
except:
    pass

# Auto-injected: Write output to DBFS
try:
    if 'output' in globals():
        output.write_to_dbfs()
    elif hasattr(sys.modules.get('__main__', None), '_notebook_output_handler'):
        sys.modules['__main__']._notebook_output_handler.write_to_dbfs()
except NameError:
    pass
except Exception as e:
    try:
        print(f"⚠️  Error writing output: {{e}}")
    except:
        pass
'''
    
    if last_command != -1:
        # Find the end of this section
        end_of_section = notebook_content.find("\n", last_command)
        if end_of_section != -1:
            return notebook_content[:end_of_section + 1] + auto_write_code + notebook_content[end_of_section + 1:]
    
    # If no COMMAND marker, append at the end
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

