# Complete List of Core Functions and Executables

## Core Package Exports (from `core/__init__.py`)

1. **DatabricksJobRunner** - Class for creating and running Databricks jobs
2. **TableInspector** - Class for inspecting and validating tables
3. **print_table** - Function to format and display query results
4. **run_query** - Function to execute SQL queries
5. **interactive_sql_main** - Function to start interactive SQL shell
6. **run_sql_file** - Function to execute SQL from files
7. **create_workspace_directory** - Function to create workspace directories
8. **upload_csv_to_workspace** - Function to upload CSV files to workspace

---

## Query Utilities (`core/query_util.py`)

### Functions:
1. **format_value(value: Any) -> str**
   - Formats values for display
   - Handles None, int, float, Decimal, bool, string

2. **print_table(results, column_names=None, limit=None, title=None)**
   - Prints query results in formatted table
   - Supports Row objects, lists, tuples
   - Auto-detects column names

3. **run_query(query: str, limit: Optional[int] = None, title: Optional[str] = None)**
   - Executes SQL query against Databricks
   - Returns list of Row objects
   - Displays formatted results

### Executable:
- Can be run as script: `python core/query_util.py "SELECT * FROM table"`

---

## Table Inspector (`core/table_inspector.py`)

### Class: TableInspector

#### Methods:
1. **get_table_schema(table_name: str) -> List[Dict]**
   - Returns table schema with column names, types, comments

2. **get_table_stats(table_name: str) -> Dict**
   - Returns table statistics (row count, column count, column names)

3. **check_duplicates_by_column(table_name: str, column_name: str, limit: int = 20) -> List[Dict]**
   - Finds duplicate values in a column

4. **check_cross_column_conflicts(table_name, identifier_column, check_columns, limit=20) -> Dict**
   - Checks if identifier has multiple values in check columns

5. **compare_csv_to_table(table_name, csv_row_counts, identifier_column='source_filename') -> Dict**
   - Compares CSV row counts with table row counts

6. **inspect_table(table_name: str, sample_rows: int = 3) -> Dict**
   - Comprehensive table inspection (stats, schema, sample data)

### Executable:
- Can be run as script: `python core/table_inspector.py schema.table --check-duplicates column`

---

## Job Runner (`core/databricks_job_runner.py`)

### Class: DatabricksJobRunner

#### Methods:
1. **create_notebook(notebook_path: str, content: str, overwrite: bool = True) -> bool**
   - Creates notebook in Databricks workspace

2. **create_job(notebook_path: str, job_name: str = None, timeout_seconds: int = 3600, max_retries: int = 0) -> Optional[str]**
   - Creates Databricks job that runs a notebook
   - Returns job_id

3. **run_job(job_id: str) -> Optional[str]**
   - Runs a Databricks job
   - Returns run_id

4. **get_run_status(run_id: str) -> Optional[Dict]**
   - Gets status of a job run

5. **get_task_output(task_run_id: str) -> Optional[Dict]**
   - Gets output from a specific task run

6. **monitor_job(run_id: str, poll_interval: int = 10, max_wait: int = 3600, show_output: bool = True) -> Dict**
   - Monitors job execution and displays output

7. **create_and_run(notebook_path, notebook_content, job_name=None, timeout_seconds=3600, poll_interval=10, max_wait=3600, show_output=True) -> Dict**
   - Complete workflow: create notebook, create job, run job, monitor

### Executable:
- Can be run as script: `python core/databricks_job_runner.py --notebook-path /path --notebook-file file.py`

---

## SQL File Execution (`core/run_sql_file.py`)

### Functions:
1. **run_sql_file(sql_file_path, output_format='show', limit=100)**
   - Executes SQL from file
   - Output formats: 'show', 'csv', 'json'

### Executable:
- Can be run as script: `python core/run_sql_file.py query.sql csv 1000`

---

## Interactive SQL (`core/interactive_sql.py`)

### Functions:
1. **main()**
   - Starts interactive SQL shell
   - Allows entering SQL queries interactively

### Executable:
- Can be run as script: `python core/interactive_sql.py`

---

## Workspace Operations (`core/databricks_workspace.py`)

### Functions:
1. **create_workspace_directory(databricks_path: str, workspace_host: str, token: str) -> None**
   - Creates directory structure in Databricks workspace

2. **upload_csv_to_workspace(csv_file_path: str, csv_filename: str, databricks_path: str, workspace_host: str, token: str) -> Dict**
   - Uploads CSV file to Databricks workspace
   - Returns success status and file info

---

## Table Creation (`core/create_table.py`)

### Functions:
1. **create_table(sql_file_path, table_name, drop_if_exists=False)**
   - Creates table from SQL file
   - Uses CREATE OR REPLACE TABLE ... AS SELECT

### Executable:
- Can be run as script: `python core/create_table.py query.sql schema.table --drop-if-exists`

---

## CSV to Table (`core/csv_to_table.py`)

### Functions:
1. **get_csv_files_from_workspace(workspace_path, workspace_host, token) -> List[str]**
   - Gets list of CSV files from workspace

2. **download_csv_from_workspace(file_path, workspace_host, token) -> Optional[str]**
   - Downloads CSV content from workspace

3. **infer_csv_schema(csv_content, sample_rows=100) -> Tuple[List[str], Dict[str, str]]**
   - Infers schema from CSV content

4. **sanitize_column_name(col_name: str) -> str**
   - Sanitizes column names for SQL

5. **create_column_mapping(original_columns: List[str]) -> Dict[str, str]**
   - Maps original to sanitized column names

6. **create_table_schema_sql(table_name, columns, column_types, additional_columns=None, column_mapping=None, table_location=None) -> str**
   - Generates CREATE TABLE SQL

7. **load_csv_data_to_table(csv_files, workspace_path, table_name, workspace_host, token, custom_columns=None, column_mapping=None) -> Dict**
   - Loads CSV data into table using INSERT statements

8. **create_table_from_csvs(workspace_path, table_name, custom_columns=None, drop_if_exists=False, verify=True, test_mode=False) -> bool**
   - Complete workflow: create table from CSV files in workspace

### Executable:
- Can be run as script: `python core/csv_to_table.py --workspace-path /path --table-name schema.table`

---

## Other Utilities

### `core/get_cluster_logs.py`
- **get_cluster_logs(cluster_id: str, run_id: str = None)**
  - Gets cluster logs from Databricks

### `core/unzip_csvs.py`
- **unzip_and_rename_csvs(source_dir: str, output_dir: str) -> dict**
  - Extracts and renames CSV files from zip archives

### `core/upload_csvs.py`
- **upload_csv_files(extract_dir, databricks_path, workspace_host, token, test_mode=False) -> Dict**
  - Uploads multiple CSV files to workspace

### `core/inspect_table.py`
- **inspect_table()**
  - CLI tool for table inspection

---

## CLI Scripts (`scripts/`)

1. **scripts/run_sql.py**
   - CLI for running SQL queries from files
   - Usage: `python scripts/run_sql.py queries/my_query.sql csv 1000`

2. **scripts/interactive_sql.py**
   - CLI for interactive SQL shell
   - Usage: `python scripts/interactive_sql.py`

3. **scripts/inspect_table.py**
   - CLI for inspecting tables
   - Usage: `python scripts/inspect_table.py schema.table --stats --schema --sample 20`

4. **scripts/create_notebook.py**
   - CLI for creating and running notebooks
   - Usage: `python scripts/create_notebook.py --notebook-path /path --file notebook.py`

---

## Summary

- **Total Core Functions**: 36+ functions/executables
- **Main Categories**:
  - Query execution (3 functions)
  - Table inspection (6 methods)
  - Job management (7 methods)
  - Workspace operations (2 functions)
  - Table creation (2 functions)
  - CSV operations (8+ functions)
  - CLI scripts (4 scripts)

---

## Testing

To test all functions:
```bash
# Install dependencies first
pip install -r requirements.txt

# Run comprehensive test
python test_all_core_functions.py
```

