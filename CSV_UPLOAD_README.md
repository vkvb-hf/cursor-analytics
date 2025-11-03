# CSV File Upload to Databricks

This directory contains scripts for uploading CSV files from zip archives to Databricks workspace.

## Architecture

The scripts follow a modular design with shared utilities:

- **`databricks_workspace.py`** - Shared module for Databricks workspace operations
- **`unzip_csvs.py`** - Extracts CSV files from zip archives and adds zip name prefix
- **`upload_csvs.py`** - Uploads CSV files to Databricks workspace

## Usage

### Step 1: Extract CSV files from zip archives

```bash
python unzip_csvs.py
```

This will:
- Read zip files from `~/Downloads/to_upload`
- Extract CSV files to a temporary directory
- Add the zip file name as a prefix to each CSV filename

Options:
- `--source-dir DIR` - Specify source directory (default: `~/Downloads/to_upload`)
- `--output-dir DIR` - Specify output directory (default: temp directory)

### Step 2: Upload CSV files to Databricks

**Test mode** (upload only the largest file):
```bash
python upload_csvs.py --test
```

**Upload all files**:
```bash
python upload_csvs.py
```

Options:
- `--extract-dir DIR` - Directory containing extracted CSV files
- `--databricks-path PATH` - Target Databricks workspace path
- `--test` - Test mode: only upload the largest file

## Configuration

The scripts use `config.py` for Databricks connection settings:
- `DATABRICKS_HOST` - Workspace hostname
- `TOKEN` - Personal access token

## Example Workflow

```bash
# 1. Extract CSV files from zip archives
python unzip_csvs.py

# 2. Test upload with largest file
python upload_csvs.py --test

# 3. Upload all CSV files
python upload_csvs.py
```

## File Naming Convention

Extracted CSV files are renamed with the format:
```
{zip_name_without_extension}_{original_csv_filename}
```

Example:
- Zip file: `GB_QLKKNG4S2Q9428Q9.zip`
- CSV inside: `Jade1314 2025-08-15T10_13_55Z.csv`
- Result: `GB_QLKKNG4S2Q9428Q9_Jade1314 2025-08-15T10_13_55Z.csv`

This makes it easy to identify which zip file each CSV came from.

