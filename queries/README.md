# Queries Directory

This directory contains SQL query files organized by purpose or use case.

## Organization

Organize queries by:
- **Use case**: `fraud_detection/`, `payment_analysis/`, etc.
- **Table**: `f_pvs_replica/`, `f_pps_charges/`, etc.
- **Type**: `exploration/`, `production/`, `validation/`

## Running Queries

### Using the CLI script:
```bash
python scripts/run_sql.py queries/my_query.sql csv 1000
```

### Using Python:
```python
from core.run_sql_file import run_sql_file

run_sql_file('queries/my_query.sql', output_format='csv', limit=1000)
```

### Interactive SQL:
```bash
python scripts/interactive_sql.py
```

## Output Formats

- `show` - Display results in terminal (default)
- `csv` - Save as CSV file
- `json` - Save as JSON file

