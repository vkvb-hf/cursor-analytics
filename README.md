# Databricks Python Utilities

A collection of generic, reusable utilities for working with Databricks, plus project-specific implementations.

## 📁 Project Structure

```
cursor_databricks/
├── config.py                 # Databricks connection configuration
├── utils/                    # Generic, reusable utilities
│   ├── databricks_job_runner.py    # Job creation and execution
│   ├── databricks_workspace.py    # Workspace file operations
│   ├── table_inspector.py         # Table inspection and validation
│   ├── csv_to_table.py            # CSV to Delta table conversion
│   ├── upload_csvs.py             # CSV file upload utilities
│   ├── unzip_csvs.py              # File extraction utilities
│   └── query_util.py              # SQL query utilities
├── projects/                 # Project-specific implementations
│   └── adyen_ml/            # Adyen ML project files
│       ├── run_adyen_ml_job.py
│       └── ...
├── tests/                    # Test and debugging scripts
└── docs/                     # Documentation
    └── AI_UTILITY_GUIDE.md  # AI model utility selection guide
```

## 🚀 Quick Start

1. **Setup Configuration**
   ```bash
   cp config.py.example config.py
   # Edit config.py with your Databricks credentials
   ```

2. **Install Dependencies**
   ```bash
   pip install databricks-sql-connector requests
   ```

3. **Use Utilities**
   ```python
   from utils import DatabricksJobRunner, TableInspector
   
   # Run a notebook as a job
   runner = DatabricksJobRunner()
   result = runner.create_and_run(
       notebook_path="/Workspace/path/to/notebook",
       notebook_content="# Your notebook code",
       job_name="My Job"
   )
   
   # Inspect a table
   inspector = TableInspector()
   stats = inspector.get_table_stats("my_schema.my_table")
   ```

## 📚 Utility Modules

### Core Utilities

#### `databricks_job_runner.py`
**Purpose**: Create and run Databricks notebooks as jobs programmatically.

**Use Cases**:
- Running notebooks as scheduled jobs
- Automating notebook execution
- Monitoring job status and output

**Key Classes**:
- `DatabricksJobRunner`: Main class for job operations

#### `databricks_workspace.py`
**Purpose**: Workspace file operations (upload, download, list).

**Use Cases**:
- Uploading files to Databricks workspace
- Creating workspace directories
- Managing workspace files

**Key Functions**:
- `create_workspace_directory()`: Create directories
- `upload_csv_to_workspace()`: Upload CSV files

#### `table_inspector.py`
**Purpose**: Table inspection, validation, and quality checks.

**Use Cases**:
- Checking table schema and statistics
- Finding duplicates
- Detecting data conflicts
- Comparing CSV files with tables

**Key Classes**:
- `TableInspector`: Main inspection class

#### `csv_to_table.py`
**Purpose**: Convert CSV files to Delta tables.

**Use Cases**:
- Bulk loading CSV data
- Schema inference and table creation
- Data transformation during import

#### `upload_csvs.py` & `unzip_csvs.py`
**Purpose**: File management utilities.

**Use Cases**:
- Extracting and preparing CSV files
- Uploading multiple files to Databricks

### Query Utilities

#### `query_util.py`, `interactive_sql.py`, `run_sql_file.py`
**Purpose**: SQL query execution utilities.

**Use Cases**:
- Running SQL queries programmatically
- Executing SQL files
- Interactive SQL sessions

## 🔧 Projects

### Adyen ML Project
Located in `projects/adyen_ml/`, this contains:
- ETL pipeline for Adyen payment data
- Risk profile mapping
- Data validation scripts

See `projects/adyen_ml/README.md` for details.

## 📖 Documentation

- **SETUP.md**: Initial setup instructions
- **QUICK_START.md**: Quick start guide
- **docs/AI_UTILITY_GUIDE.md**: Guide for AI models to select utilities
- **CSV_UPLOAD_README.md**: CSV upload process documentation

## 🧪 Testing

Test scripts are located in `tests/`. These are primarily for debugging and validation.

## 🤖 For AI Models

See `docs/AI_UTILITY_GUIDE.md` for a comprehensive guide on when to use which utility.

## ⚙️ Configuration

Edit `config.py` with your Databricks credentials:
- `SERVER_HOSTNAME`: Your workspace hostname
- `HTTP_PATH`: SQL warehouse HTTP path
- `TOKEN`: Personal access token
- `DATABRICKS_HOST`: Full workspace URL

**⚠️ Never commit `config.py` with real credentials to version control!**

## 📝 Best Practices

1. **Use Generic Utilities**: Prefer utilities in `utils/` over project-specific code
2. **Keep Projects Separate**: Project-specific code belongs in `projects/`
3. **Document Dependencies**: Add docstrings and type hints
4. **Test Utilities**: Validate utilities work before using in production
5. **Handle Errors**: Always include error handling and logging

## 🔄 Contributing

When adding new utilities:
1. Place generic utilities in `utils/`
2. Follow existing patterns and naming conventions
3. Add docstrings and type hints
4. Update `docs/AI_UTILITY_GUIDE.md` if adding a new utility category

## 📄 License

Internal use only.
