#!/usr/bin/env python3
"""
Notebook Output Framework

Standardized way to capture and display notebook output in terminal.
All output is written to DBFS files in a structured format, then retrieved after job completion.
"""

import time
from datetime import datetime
from typing import List, Dict, Optional, Any


class NotebookOutput:
    """
    Standardized output handler for Databricks notebooks.
    
    Usage in notebook:
        from core.notebook_output import NotebookOutput
        
        output = NotebookOutput(output_path="/tmp/notebook_output.txt")
        
        # Add sections
        output.add_section("Query Results", "Your results here")
        output.add_dataframe("Summary", df)
        
        # Write to DBFS
        output.write_to_dbfs()
    """
    
    def __init__(self, output_path: str = None, job_name: str = None, run_id: str = None):
        """
        Initialize output handler.
        
        Args:
            output_path: DBFS path for output file (default: auto-generated)
            job_name: Optional job name for file organization
            run_id: Optional run ID for file organization
        """
        if output_path is None:
            # Auto-generate path with structure
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            if job_name:
                safe_job_name = job_name.replace(" ", "_").replace("/", "_")
                output_path = f"/tmp/notebook_outputs/{safe_job_name}_{timestamp}.txt"
            else:
                output_path = f"/tmp/notebook_outputs/notebook_{timestamp}.txt"
        
        self.output_path = output_path
        self.job_name = job_name
        self.run_id = run_id
        self.sections: List[Dict[str, Any]] = []
        self.metadata: Dict[str, Any] = {
            'created_at': datetime.now().isoformat(),
            'job_name': job_name,
            'run_id': run_id
        }
        self.errors: List[str] = []
    
    def add_section(self, title: str, content: str, format: str = "text"):
        """
        Add a section to output.
        
        Args:
            title: Section title
            content: Section content (text)
            format: Content format (text, json, table, etc.)
        """
        self.sections.append({
            'title': title,
            'content': content,
            'format': format,
            'timestamp': datetime.now().isoformat()
        })
    
    def add_dataframe(self, title: str, df, max_rows: int = 100):
        """
        Add DataFrame output.
        
        Args:
            title: Section title
            df: DataFrame (pandas or Spark)
            max_rows: Maximum rows to display
        """
        try:
            import pandas as pd
            
            # Convert Spark DataFrame to pandas if needed
            if hasattr(df, 'toPandas'):
                df = df.toPandas()
            elif not isinstance(df, pd.DataFrame):
                df = pd.DataFrame(df)
            
            # Limit rows for display
            display_df = df.head(max_rows)
            content = display_df.to_string()
            
            # Add row count info
            if len(df) > max_rows:
                content += f"\n\n... ({len(df) - max_rows} more rows not shown)"
            
            self.add_section(title, content, format="dataframe")
            
        except Exception as e:
            self.add_section(title, f"Error displaying DataFrame: {str(e)}", format="error")
    
    def add_query_result(self, title: str, query: str, results, max_rows: int = 100):
        """
        Add SQL query results.
        
        Args:
            title: Section title
            query: SQL query string
            results: Query results (DataFrame or list)
            max_rows: Maximum rows to display
        """
        try:
            import pandas as pd
            
            # Convert to pandas if needed
            if hasattr(results, 'toPandas'):
                df = results.toPandas()
            elif isinstance(results, pd.DataFrame):
                df = results
            else:
                df = pd.DataFrame(results)
            
            # Build content
            content_lines = []
            content_lines.append(f"Query:")
            content_lines.append("-" * 80)
            content_lines.append(query)
            content_lines.append("")
            content_lines.append("Results:")
            content_lines.append("-" * 80)
            
            # Limit rows
            display_df = df.head(max_rows)
            content_lines.append(display_df.to_string())
            
            if len(df) > max_rows:
                content_lines.append(f"\n... ({len(df) - max_rows} more rows not shown)")
            
            content = "\n".join(content_lines)
            self.add_section(title, content, format="query")
            
        except Exception as e:
            self.add_section(title, f"Error displaying query results: {str(e)}", format="error")
    
    def add_error(self, error_message: str, error_type: str = "Error"):
        """Add an error message."""
        self.errors.append(f"{error_type}: {error_message}")
        self.add_section(f"{error_type}", error_message, format="error")
    
    def add_metadata(self, key: str, value: Any):
        """Add metadata."""
        self.metadata[key] = value
    
    def print(self, *args, sep: str = " ", end: str = "\n"):
        """
        Print statement that also captures output.
        
        Usage: output.print("Hello", "World") instead of print("Hello", "World")
        """
        message = sep.join(str(arg) for arg in args) + end
        # Also print to console (for UI visibility)
        print(message, end="")
        # Capture for output file (only if message has content)
        message_stripped = message.strip()
        if message_stripped:  # Only add section if message has content
            self.add_section("Print Output", message_stripped, format="text")
    
    def write_to_dbfs(self, also_print: bool = True):
        """
        Write formatted output to DBFS file.
        
        Args:
            also_print: If True, also print to console (for UI visibility)
        """
        try:
            # Ensure directory exists
            dir_path = "/".join(self.output_path.split("/")[:-1])
            if dir_path:
                dbutils.fs.mkdirs(dir_path)
            
            # Build output text
            output_lines = []
            output_lines.append("=" * 100)
            output_lines.append("NOTEBOOK OUTPUT")
            output_lines.append("=" * 100)
            output_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            if self.job_name:
                output_lines.append(f"Job: {self.job_name}")
            if self.run_id:
                output_lines.append(f"Run ID: {self.run_id}")
            output_lines.append("")
            
            # Add metadata
            if self.metadata:
                output_lines.append("-" * 100)
                output_lines.append("METADATA")
                output_lines.append("-" * 100)
                for key, value in self.metadata.items():
                    if key not in ['created_at', 'job_name', 'run_id']:
                        output_lines.append(f"{key}: {value}")
                output_lines.append("")
            
            # Add sections (filter out empty content)
            section_num = 0
            for section in self.sections:
                # Skip sections with empty content
                if not section.get('content', '').strip():
                    continue
                section_num += 1
                output_lines.append("-" * 100)
                output_lines.append(f"📊 [{section_num}] {section['title']}")
                output_lines.append("-" * 100)
                output_lines.append(section['content'])
                output_lines.append("")
            
            # Add errors if any
            if self.errors:
                output_lines.append("-" * 100)
                output_lines.append("❌ ERRORS")
                output_lines.append("-" * 100)
                for error in self.errors:
                    output_lines.append(error)
                output_lines.append("")
            
            output_lines.append("=" * 100)
            output_lines.append(f"Output file: {self.output_path}")
            output_lines.append("=" * 100)
            
            output_text = "\n".join(output_lines)
            
            # Write to DBFS
            dbutils.fs.put(self.output_path, output_text, overwrite=True)
            
            # Also print for UI visibility
            if also_print:
                print("\n" + output_text)
            
            return True
            
        except Exception as e:
            error_msg = f"Error writing output to DBFS: {str(e)}"
            print(error_msg)
            # Try to write error to a fallback location
            try:
                fallback_path = "/tmp/notebook_output_error.txt"
                dbutils.fs.put(fallback_path, error_msg, overwrite=True)
            except:
                pass
            return False
    
    def write_json(self, json_path: str = None):
        """
        Write structured JSON output (optional, for programmatic access).
        
        Args:
            json_path: DBFS path for JSON file (default: auto-generated)
        """
        import json
        
        if json_path is None:
            json_path = self.output_path.replace(".txt", ".json")
        
        try:
            output = {
                'metadata': self.metadata,
                'sections': self.sections,
                'errors': self.errors,
                'timestamp': datetime.now().isoformat(),
                'output_path': self.output_path
            }
            
            # Ensure directory exists
            dir_path = "/".join(json_path.split("/")[:-1])
            if dir_path:
                dbutils.fs.mkdirs(dir_path)
            
            dbutils.fs.put(json_path, json.dumps(output, indent=2), overwrite=True)
            return True
            
        except Exception as e:
            print(f"Error writing JSON output: {str(e)}")
            return False

