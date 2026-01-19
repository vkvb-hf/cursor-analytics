# How to See Notebook Output in Terminal

**Simple Rule**: Use `output.print()` instead of `print()` to see output in terminal!

## Quick Start

The `output` variable is **automatically available** in all notebooks. Just use it:

```python
# Instead of this:
print("Hello World")

# Use this:
output.print("Hello World")
```

That's it! The output will automatically appear in your terminal after the job completes.

## Complete Example

```python
# Databricks notebook source
# MAGIC %md
# MAGIC # My Analysis

# COMMAND ----------

# Query data
query = """
SELECT 
    event_date as date,
    COUNT(*) as daily_count
FROM payments_hf.checkout_funnel_backend
WHERE event_date >= CURRENT_DATE - INTERVAL 7 DAYS
GROUP BY event_date
ORDER BY date DESC
"""

# Use output.print() to see results in terminal
output.print("=" * 80)
output.print("Querying data...")
output.print("=" * 80)

result_df = spark.sql(query)
pandas_df = result_df.toPandas()

# Display results
output.print("")
output.print("Daily Counts Results:")
output.print("=" * 80)
output.print(pandas_df.to_string(index=False))

# Add structured section
output.add_section("Summary", f"Total records: {pandas_df['daily_count'].sum():,}")

# Output is automatically written to DBFS and displayed in terminal!
```

## Available Methods

### `output.print(*args, sep=" ", end="\n")`
Works exactly like `print()`, but captures output for terminal display.

```python
output.print("Hello", "World")  # Same as print("Hello", "World")
output.print(f"Count: {count}")  # Same as print(f"Count: {count}")
```

### `output.add_section(title, content)`
Add a structured section to the output.

```python
output.add_section("Query Results", pandas_df.to_string())
output.add_section("Summary", "Total: 1000 records")
```

### `output.add_dataframe(title, df)`
Add a DataFrame as a formatted section.

```python
output.add_dataframe("Results", pandas_df)
```

### `output.write_to_dbfs()`
Manually write output to DBFS (usually called automatically at the end).

## Why This Approach?

✅ **Simple**: Just use `output.print()` instead of `print()`  
✅ **Reliable**: Works consistently, no scope issues  
✅ **Universal**: Works for any notebook  
✅ **Automatic**: `output` variable is auto-injected  
✅ **Structured**: Can add sections, DataFrames, etc.

## Migration Guide

### Before (doesn't show in terminal):
```python
print("Starting analysis...")
print(f"Results: {results}")
```

### After (shows in terminal):
```python
output.print("Starting analysis...")
output.print(f"Results: {results}")
```

That's the only change needed!

## Tips

1. **Use `output.print()` for important messages** you want to see in terminal
2. **Regular `print()` still works** for UI visibility, but won't appear in terminal
3. **Use `output.add_section()`** for structured data
4. **Output is automatically written** at the end of the notebook

## Troubleshooting

**Q: `output` variable not available?**  
A: Make sure `auto_inject_output=True` (it's the default)

**Q: Output not showing in terminal?**  
A: Make sure you're using `output.print()`, not just `print()`

**Q: Want to see regular print() too?**  
A: Use `output.print()` for everything you want in terminal

