# Databricks notebook source
# MAGIC %md
# MAGIC # Observe Backfill
# MAGIC 
# MAGIC Run observe_daily for a range of dates to backfill historical data.
# MAGIC 
# MAGIC **Usage**: Update START_DATE and END_DATE below, then run all cells.

# COMMAND ----------

# Configuration - UPDATE THESE
START_DATE = "2025-01-01"
END_DATE = "2025-02-25"

# COMMAND ----------

from datetime import datetime, timedelta

start = datetime.strptime(START_DATE, "%Y-%m-%d")
end = datetime.strptime(END_DATE, "%Y-%m-%d")

dates = []
current = start
while current <= end:
    dates.append(current.strftime("%Y-%m-%d"))
    current += timedelta(days=1)

print(f"Backfilling {len(dates)} days: {START_DATE} to {END_DATE}")

# COMMAND ----------

# Get the path to observe_daily notebook (same folder)
notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
daily_notebook = notebook_path.rsplit("/", 1)[0] + "/observe_daily"
print(f"Will run: {daily_notebook}")

# COMMAND ----------

results = []
for date_str in dates:
    print(f"Processing {date_str}...", end=" ")
    try:
        result = dbutils.notebook.run(daily_notebook, timeout_seconds=600, arguments={"target_date": date_str})
        results.append({"date": date_str, "status": "success", "result": result})
        print("OK")
    except Exception as e:
        results.append({"date": date_str, "status": "failed", "error": str(e)})
        print(f"FAILED: {e}")

# COMMAND ----------

# Summary
success = sum(1 for r in results if r["status"] == "success")
failed = sum(1 for r in results if r["status"] == "failed")

print(f"\n{'='*50}")
print(f"BACKFILL COMPLETE")
print(f"{'='*50}")
print(f"Success: {success}/{len(dates)}")
print(f"Failed: {failed}/{len(dates)}")

if failed > 0:
    print("\nFailed dates:")
    for r in results:
        if r["status"] == "failed":
            print(f"  - {r['date']}: {r['error']}")

# COMMAND ----------

# Verify data
print("\nVerifying backfilled data...")

metrics_count = spark.sql(f"""
    SELECT COUNT(*) as cnt FROM payments_hf.observe_metrics_daily 
    WHERE date BETWEEN '{START_DATE}' AND '{END_DATE}'
""").collect()[0].cnt

alerts_count = spark.sql(f"""
    SELECT COUNT(*) as cnt FROM payments_hf.observe_alerts_daily 
    WHERE date BETWEEN '{START_DATE}' AND '{END_DATE}'
""").collect()[0].cnt

print(f"Metrics records: {metrics_count:,}")
print(f"Alerts records: {alerts_count:,}")
