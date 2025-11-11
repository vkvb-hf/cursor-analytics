# Adyen ML Transactions Project

Project-specific implementation for processing Adyen payment transaction data.

## Overview

This project processes CSV files containing Adyen payment transactions, adds risk profile mappings, and creates a Delta table for analysis.

## Files

### Main Scripts

- **`run_adyen_ml_job.py`**: Main ETL script that creates the table via Databricks job
  - Downloads CSV files from workspace to DBFS
  - Reads files with Spark
  - Adds custom columns (source_filename, profile_reference, risk_profile)
  - Creates Delta table `payments_hf.adyen_ml_test_data`

### Data Validation

- **`check_duplicates.py`**: Checks for duplicate records
- **`check_conflicting_attributes.py`**: Validates data consistency
- **`verify_table_counts.py`**: Compares CSV row counts with table
- **`verify_table_data.py`**: Comprehensive data verification
- **`inspect_table.py`**: Table inspection utility (project-specific version)

### Legacy/Reference

- **`create_adyen_ml_table.py`**: Original SQL-based approach (legacy)
- **`create_adyen_ml_spark.py`**: Spark approach (reference)
- **`create_adyen_ml_spark_notebook.py`**: Notebook version (reference)
- **`create_adyen_ml_table_parallel.py`**: Parallel processing approach (reference)

## Usage

### Run Full Pipeline

```bash
python run_adyen_ml_job.py --drop-if-exists --timeout 3600
```

### Verify Data

```bash
python verify_table_counts.py
python check_duplicates.py
python check_conflicting_attributes.py
```

## Risk Profile Mapping

The project maps profile references to risk profiles:

| Profile Reference | Risk Profile |
|------------------|-------------|
| THLH73H2VSWDN842 | Jade1314 CANADA ML |
| QNN7MK9V6T5T87F3 | Very_High_ecomm |
| TBDLJCJZX8LLWWF3 | Medium_ecomm |
| J2M3VKGZMHZNZ4Q9 | Medium |
| DXPLDK9V6T5T87F3 | High_ecomm |
| QLKKNG4S2Q9428Q9 | Very_High |
| ZDGX3H4S2Q9428Q9 | High |

## Table Schema

Table: `payments_hf.adyen_ml_test_data`

- Original CSV columns (PSP_Reference, Merchant_Reference, etc.)
- `source_filename`: Source CSV filename
- `profile_reference`: Extracted from filename
- `risk_profile`: Mapped from profile_reference

## Dependencies

- Uses utilities from `../../utils/`
- Requires `config.py` with Databricks credentials
- Databricks cluster with Spark enabled



