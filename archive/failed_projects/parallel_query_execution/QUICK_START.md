# Quick Start Guide - Parallel Query Execution

## What is This?

A new parallel query execution system that allows you to run multiple SQL queries concurrently in Databricks, instead of waiting for each one to complete sequentially.

## Why Use It?

**Before (Sequential):**
- Query 1: 10 seconds
- Query 2: 10 seconds  
- Query 3: 10 seconds
- **Total: 30 seconds**

**After (Parallel with 3 workers):**
- All queries run at the same time
- **Total: ~10 seconds** (3x faster!)

## Installation

No installation needed! Just use the scripts in the `parallel/` directory.

## Quick Examples

### 1. Run Multiple Queries from Command Line

```bash
cd /Users/visal.kumar/Documents/databricks/cursor_databricks
source ../databricks_env/bin/activate

python parallel/run_parallel_queries.py \
  --queries \
    "SELECT COUNT(*) FROM schema.table1" \
    "SELECT COUNT(*) FROM schema.table2" \
    "SELECT COUNT(*) FROM schema.table3"
```

### 2. Run SQL Files in Parallel

```bash
python parallel/run_parallel_sql_files.py query1.sql query2.sql query3.sql
```

### 3. Use from Python Script

```python
from parallel.parallel_query_api import run_parallel

results = run_parallel([
    "SELECT COUNT(*) FROM table1",
    "SELECT COUNT(*) FROM table2",
    "SELECT COUNT(*) FROM table3"
])

for query_id, result in results.items():
    print(f"{query_id}: {result}")
```

## Key Features

✅ **Non-blocking**: Queries run concurrently, not sequentially  
✅ **Status Tracking**: See which queries are running, completed, or failed  
✅ **Error Handling**: One failed query doesn't stop others  
✅ **Flexible**: Use from command line or Python scripts  
✅ **Safe**: Doesn't modify existing core files  

## Common Use Cases

1. **Running multiple independent queries**: Count queries, aggregations, etc.
2. **Testing multiple SQL files**: Run all test queries at once
3. **Data validation**: Check multiple tables simultaneously
4. **ETL pipelines**: Run independent transformations in parallel

## Monitoring Queries

The system automatically tracks all queries:

```
================================================================================
QUERY TRACKER STATUS
================================================================================
Total queries: 3
  Pending:   0
  Running:   1
  Completed: 2
  Failed:    0
================================================================================
```

## Next Steps

- See `README.md` for detailed documentation
- Check `example_usage.py` for more examples
- Run `python parallel/example_usage.py` to see it in action

## Important Notes

- **Max Workers**: Default is 5 concurrent queries. Adjust with `--max-workers`
- **Timeouts**: Default is 300 seconds per query. Adjust with `--timeout`
- **Cluster Capacity**: Don't exceed your Databricks cluster's capacity
- **Existing Scripts**: All existing scripts continue to work unchanged

