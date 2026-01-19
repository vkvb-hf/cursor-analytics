# File Analysis and Consolidation Recommendations

## Current File Structure

### Core Files (8 Python files)

1. **`long_term_steering_report.py`** (935 lines)
   - **Purpose**: Parameterized Databricks notebook
   - **Use Case**: Run in Databricks with `COMPARISON_TYPE` parameter
   - **Output**: Generates one comparison type at a time
   - **Status**: ✅ Main file, keep

2. **`generate_steering_report.py`** (1948 lines)
   - **Purpose**: Full Databricks notebook generating all 3 comparison types
   - **Use Case**: Comprehensive report generation
   - **Output**: All comparison types in one run
   - **Status**: ⚠️ Large file, overlaps with long_term_steering_report.py

3. **`generate_steering_report_notebook.py`** (427 lines)
   - **Purpose**: Simplified notebook version
   - **Use Case**: Lighter version of generate_steering_report.py
   - **Status**: ⚠️ Appears to be duplicate/simplified version

4. **`generate_steering_report_from_source.py`** (338 lines)
   - **Purpose**: Python script using DatabricksAPI (not notebook)
   - **Use Case**: Run from local machine, not Databricks
   - **Status**: ⚠️ Different approach, but incomplete (template)

5. **`run_generate_steering_report.py`** (280 lines)
   - **Purpose**: Runner script for generate_steering_report.py
   - **Use Case**: Executes generate_steering_report.py as Databricks job
   - **Status**: ✅ Utility, keep if using generate_steering_report.py

6. **`run_long_term_steering.py`** (226 lines)
   - **Purpose**: Runner script for long_term_steering_report.py
   - **Use Case**: Executes long_term_steering_report.py for all comparison types
   - **Status**: ✅ Utility, keep

7. **`validate_output.py`** (374 lines)
   - **Purpose**: Validates generated output files
   - **Use Case**: Quality assurance for reports
   - **Status**: ✅ Utility, keep

8. **`check_unknown_dimension.py`** (87 lines)
   - **Purpose**: Checks for unknown dimensions in data
   - **Use Case**: Data quality check
   - **Status**: ✅ Utility, keep

## Why So Many Files?

### Historical Evolution
The files appear to have evolved over time with different approaches:

1. **Initial approach**: `long_term_steering_report.py` - parameterized notebook
2. **Expansion**: `generate_steering_report.py` - full-featured version
3. **Simplification**: `generate_steering_report_notebook.py` - lighter version
4. **Alternative approach**: `generate_steering_report_from_source.py` - local execution
5. **Automation**: Runner scripts for each main file

### Overlap Analysis

**High Overlap:**
- `generate_steering_report.py` and `generate_steering_report_notebook.py` - Both generate reports, similar functionality
- `generate_steering_report.py` and `long_term_steering_report.py` - Both generate reports, different approaches

**Different Purposes:**
- `long_term_steering_report.py` - Parameterized (one comparison at a time)
- `generate_steering_report.py` - All comparisons at once
- `generate_steering_report_from_source.py` - Local execution (incomplete)

## Consolidation Recommendations

### Option 1: Keep Current Structure (Recommended for now)
**Keep:**
- ✅ `long_term_steering_report.py` - Main parameterized notebook
- ✅ `run_long_term_steering.py` - Runner for main notebook
- ✅ `validate_output.py` - Validation utility
- ✅ `check_unknown_dimension.py` - Data quality utility

**Archive/Remove:**
- ⚠️ `generate_steering_report.py` - If not actively used, archive
- ⚠️ `generate_steering_report_notebook.py` - If duplicate, remove
- ⚠️ `generate_steering_report_from_source.py` - If incomplete, remove or complete
- ⚠️ `run_generate_steering_report.py` - If not using generate_steering_report.py, remove

### Option 2: Consolidate to Single Approach
**Keep only:**
- `long_term_steering_report.py` - Main notebook
- `run_long_term_steering.py` - Runner
- `validate_output.py` - Validator
- `check_unknown_dimension.py` - Utility

**Remove:**
- All other generate_* files (if functionality is covered by main file)

### Option 3: Organize by Purpose
**Create subdirectories:**
```
long_term_steering_report/
├── notebooks/          # Databricks notebooks
│   ├── long_term_steering_report.py
│   └── generate_steering_report.py (if needed)
├── runners/            # Runner scripts
│   ├── run_long_term_steering.py
│   └── run_generate_steering_report.py (if needed)
└── utils/              # Utilities
    ├── validate_output.py
    └── check_unknown_dimension.py
```

## File Path Updates Needed

After moving output files to `output/` directory, these files need path updates:

1. **`validate_output.py`** (lines 341-343)
   - Currently: `script_dir / 'detailed_summary_*.txt'`
   - Should be: `script_dir / 'output' / 'detailed_summary_*.txt'`

2. **`run_long_term_steering.py`** (lines 84-86)
   - Currently: Hardcoded filenames
   - Should check: `output/` directory

3. **`long_term_steering_report.py`** (lines 775-781)
   - Currently: `f'{output_folder}/{filename}'`
   - Should be: `f'{output_folder}/output/{filename}'` or update output_folder

## Recommendations

1. **Immediate**: Update file paths to use `output/` directory
2. **Short-term**: Decide which generate_* files are actually needed
3. **Long-term**: Consolidate duplicate functionality

## Questions to Answer

1. Is `generate_steering_report.py` actively used?
2. Is `generate_steering_report_notebook.py` different enough to keep?
3. Is `generate_steering_report_from_source.py` complete/needed?
4. Which approach is preferred: parameterized or all-at-once?

