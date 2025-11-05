# Notebooks Directory

This directory contains utilities and templates for creating and managing Databricks notebooks.

## Files

- `create_and_run_databricks_job.py` - Create and execute Databricks jobs
- `get_job_output.py` - Retrieve output from Databricks job runs
- `get_notebook_content.py` - Get notebook content from workspace
- `get_notebook_from_job.py` - Extract notebook from job runs
- `get_notebook_from_url.py` - Download notebook from URL
- `check_job_status.py` - Check status of running jobs

## Usage

```python
from notebooks.create_and_run_databricks_job import create_and_run_job

# Create and run a notebook as a job
result = create_and_run_job(
    notebook_path="/Workspace/path/to/notebook",
    notebook_content="# Your notebook code",
    job_name="My Job"
)
```

## Templates

Create notebook templates in this directory for common use cases:
- `template_*.py` - Reusable notebook templates

