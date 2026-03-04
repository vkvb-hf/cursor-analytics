Profile the table: $ARGUMENTS

Follow these steps exactly:

1. **Schema inspection**: Run `DESCRIBE EXTENDED $ARGUMENTS` via the `execute_sql` MCP tool
2. **Sample data**: Run `SELECT * FROM $ARGUMENTS LIMIT 10` to see actual values
3. **Column statistics**: For each column, run a single query:
   ```sql
   SELECT
     '$COL' as column_name,
     COUNT(*) as total_rows,
     COUNT($COL) as non_null,
     COUNT(*) - COUNT($COL) as null_count,
     COUNT(DISTINCT $COL) as distinct_values,
     MIN($COL) as min_value,
     MAX($COL) as max_value
   FROM $ARGUMENTS
   ```
   Combine all columns into one UNION ALL query for efficiency.
4. **Summary**: Present a concise profile with:
   - Table name, total row count, column count
   - Per-column: type, null rate, cardinality, min/max
   - Flag any columns with >50% nulls or suspiciously low cardinality
   - Suggest follow-up analyses based on what you find
