#!/usr/bin/env python3
"""
Output Helper Functions

Simple helper functions to write output to DBFS for terminal display.
This is the most reliable approach that actually works.
"""

def write_output_to_dbfs(output_text: str, output_path: str = None, job_name: str = None):
    """
    Write output text to DBFS file.
    
    This is the simplest and most reliable way to see notebook output in terminal.
    
    Args:
        output_text: Text to write
        output_path: Optional specific path (auto-generated if None)
        job_name: Optional job name for path generation
    
    Returns:
        Path where output was written
    """
    from datetime import datetime
    
    if output_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if job_name:
            safe_job_name = job_name.replace(" ", "_").replace("/", "_")
            output_path = f"/tmp/notebook_outputs/{safe_job_name}_{timestamp}.txt"
        else:
            output_path = f"/tmp/notebook_outputs/notebook_{timestamp}.txt"
    
    # Write to DBFS
    dbutils.fs.put(output_path, output_text, overwrite=True)
    print(f"✅ Output written to: {output_path}")
    
    return output_path


def format_query_results(title: str, pandas_df, summary: str = None) -> str:
    """
    Format query results as output text.
    
    Args:
        title: Section title
        pandas_df: Pandas DataFrame with results
        summary: Optional summary text
    
    Returns:
        Formatted output text
    """
    import io
    
    buffer = io.StringIO()
    buffer.write("=" * 80)
    buffer.write("\n")
    buffer.write(title)
    buffer.write("\n")
    buffer.write("=" * 80)
    buffer.write("\n\n")
    buffer.write(pandas_df.to_string(index=False))
    buffer.write("\n\n")
    
    if summary:
        buffer.write("=" * 80)
        buffer.write("\n")
        buffer.write(summary)
        buffer.write("\n")
        buffer.write("=" * 80)
        buffer.write("\n")
    
    return buffer.getvalue()

