Create and run a Databricks notebook for: $ARGUMENTS

## 1. Clarify Objective
Ask the user (if not already clear from the arguments):
- What question are we answering?
- What table(s) are involved?
- What output do they want (table, chart, summary)?

## 2. Generate Notebook Cells
Build a notebook with these cells:

**Cell 1 — Markdown header:**
```
# Analysis: <title>
**Objective:** <what we're answering>
**Data Source:** <schema.table>
**Filters:** <country, date range>
**Date:** <today>
```

**Cell 2 — Imports:**
```python
import pandas as pd
import matplotlib.pyplot as plt
try:
    plt.style.use('seaborn-v0_8-whitegrid')
except:
    plt.style.use('seaborn-whitegrid')
```

**Cell 3 — Query:**
```python
df = spark.sql("""
  SELECT ...
  FROM schema.table
  WHERE country = '...' AND date >= '...'
""").toPandas()
print(f"Total records: {len(df):,}")
df.head(10)
```

**Cell 4 — Analysis/Visualization:**
Build the appropriate chart or aggregation based on the objective.

**Cell 5 — Summary:**
```python
# Print key findings
print("Key Findings:")
print(f"- Metric 1: {value}")
print(f"- Metric 2: {value}")
```

## 3. Create & Run
- Use the `run_notebook` MCP tool to create and execute the notebook
- The notebook path should be: `/Workspace/Users/visal.kumar@hellofresh.com/temp/<descriptive_name>`

## 4. Monitor
- Use `get_job_status` MCP tool to check execution status
- If it fails, retrieve error details and fix
- Once complete, share the notebook path with the user
