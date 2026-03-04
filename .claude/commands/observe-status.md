Check monitoring health status for: $ARGUMENTS

If no specific source is given, check all configured sources.

## 1. Read Monitoring Config
Read the file `observe/config/sources.yml` to understand configured data sources, their tables, date columns, and expected columns.

## 2. Data Freshness
For each source (or the specified one), check when data was last updated:
```sql
SELECT MAX(date_column) as latest_data, DATEDIFF(CURRENT_DATE(), MAX(date_column)) as days_stale
FROM database.table
```

## 3. Recent Alerts
Query the observe metrics/alerts tables if they exist:
```sql
SELECT * FROM payments_hf.observe_alerts_daily
WHERE alert_date >= DATE_SUB(CURRENT_DATE(), 7)
ORDER BY alert_date DESC
```

```sql
SELECT * FROM payments_hf.observe_metrics_daily
WHERE metric_date >= DATE_SUB(CURRENT_DATE(), 7)
ORDER BY metric_date DESC
```

If these tables don't exist, skip and note it.

## 4. Quick Health Check per Source
For each configured source, run:
```sql
SELECT COUNT(*) as row_count, COUNT(DISTINCT date_column) as distinct_dates
FROM database.table
WHERE date_column >= DATE_SUB(CURRENT_DATE(), 7)
```

## 5. Summary Dashboard
Present results as:

| Source | Table | Latest Data | Staleness | 7d Row Count | Status |
|--------|-------|-------------|-----------|--------------|--------|
| name | db.table | date | N days | count | OK/STALE/ALERT |

- **OK**: Data is fresh (< 2 days old)
- **STALE**: Data is > 2 days old
- **ALERT**: Active alerts in last 7 days

Flag any issues and suggest remediation.
