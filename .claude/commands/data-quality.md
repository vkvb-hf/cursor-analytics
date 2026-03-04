Run data quality checks on: $ARGUMENTS

Execute each check via the `execute_sql` MCP tool and compile a scorecard.

## 1. Row Count & Date Range
```sql
SELECT COUNT(*) as total_rows, MIN(date_col) as earliest, MAX(date_col) as latest
FROM $ARGUMENTS
```
(Identify the date column from `DESCRIBE EXTENDED` first)

## 2. Null Analysis
For every column, compute null counts:
```sql
SELECT
  COUNT(*) as total,
  COUNT(col1) as col1_non_null,
  COUNT(col2) as col2_non_null,
  ...
FROM $ARGUMENTS
```

## 3. Duplicate Check
Check for duplicate rows on likely key columns:
```sql
SELECT key_col, COUNT(*) as cnt
FROM $ARGUMENTS
GROUP BY key_col
HAVING COUNT(*) > 1
ORDER BY cnt DESC
LIMIT 20
```

## 4. Cross-Column Conflicts
Check for logical inconsistencies:
```sql
SELECT id_col, COUNT(DISTINCT status_col) as status_count
FROM $ARGUMENTS
GROUP BY id_col
HAVING COUNT(DISTINCT status_col) > 1
LIMIT 20
```

## 5. Value Distributions
For categorical columns, show top values:
```sql
SELECT col, COUNT(*) as cnt, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) as pct
FROM $ARGUMENTS
GROUP BY col
ORDER BY cnt DESC
LIMIT 20
```

## 6. Scorecard
Present a summary table:

| Check | Status | Details |
|-------|--------|---------|
| Row count | OK/WARN | N rows |
| Null rate | OK/WARN | Columns with >10% nulls |
| Duplicates | OK/WARN | N duplicate keys found |
| Conflicts | OK/WARN | N conflicting records |
| Date range | OK/WARN | Earliest — Latest, any gaps |
| Value dist | OK/WARN | Any unexpected distributions |

Flag anything that looks anomalous.
