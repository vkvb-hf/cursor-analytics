# Data Source Verification

This document confirms that the new notebook **does NOT overwrite any original data sources** from the shared notebooks.

## Original Notebooks Data Flow

### 1. Neptune Backfill Data Notebook
**Reads from:**
- `payments_hf.customer_identifiers` (table) - **READ ONLY**

**Writes to:**
- `s3://hf-payments-data-lake-live-main/voucher_abuse/neptune_backfill/20250305/edges/` (CSV files)
- `s3://hf-payments-data-lake-live-main/voucher_abuse/neptune_backfill/20250305/vertices/` (CSV files)

### 2. Graph Duplicate Detection Notebook
**Reads from:**
- `payments_hf.checkout_customer_details_bob` (table) - **READ ONLY**
- `payments_hf.checkout_customer_details_spider` (table) - **READ ONLY**
- `payments_hf.business_units` (table) - **READ ONLY**

**Writes to:**
- `payments_hf.customer_identifiers` (table) - **WRITES TO THIS TABLE**

## New Notebook: [PY-3368] post-spider revamp

### Reads from (ALL READ-ONLY):
1. **S3 CSV files** (read-only):
   - `s3://hf-payments-data-lake-live-main/voucher_abuse/neptune_backfill/20250305/edges/` - **READ ONLY** ✅
   - `s3://hf-payments-data-lake-live-main/voucher_abuse/neptune_backfill/20250305/vertices/` - **READ ONLY** ✅

2. **Source tables** (read-only):
   - `payments_hf.checkout_customer_details_spider` - **READ ONLY** (only SELECT queries) ✅
   - `payments_hf.business_units` - **READ ONLY** (only SELECT queries) ✅

### Writes to (NEW TABLE ONLY):
- `payments_hf.customer_identifiers_20251121` - **NEW TABLE, DIFFERENT NAME** ✅

## Verification Checklist

| Data Source | Original Notebooks | New Notebook | Overwrite? |
|------------|-------------------|--------------|------------|
| `payments_hf.customer_identifiers` | Graph Duplicate Detection **WRITES** | **NOT USED** | ❌ No |
| `payments_hf.checkout_customer_details_bob` | Graph Duplicate Detection **READS** | **NOT USED** | ❌ No |
| `payments_hf.checkout_customer_details_spider` | Graph Duplicate Detection **READS** | **READS ONLY** | ❌ No |
| `payments_hf.business_units` | Graph Duplicate Detection **READS** | **READS ONLY** | ❌ No |
| S3 CSV files (edges/vertices) | Neptune Backfill **WRITES** | **READS ONLY** | ❌ No |
| `payments_hf.customer_identifiers_20251121` | **DOES NOT EXIST** | **WRITES (NEW)** | ✅ New table |

## Key Points

1. ✅ **No overwrites of original tables**: We never write to `payments_hf.customer_identifiers`
2. ✅ **No overwrites of S3 CSV files**: We only read from them, never write
3. ✅ **Read-only access to source tables**: We only use SELECT queries on source tables
4. ✅ **New output table**: We write to a completely new table `customer_identifiers_20251121`
5. ✅ **No modifications to original notebooks**: We don't modify or touch the original notebooks

## Code Evidence

### New Notebook Only Reads from Source Tables:
```python
# Line 210-211: Only REFRESH and SELECT, no writes
spark.sql("REFRESH TABLE payments_hf.business_units")
spark.sql("REFRESH TABLE payments_hf.checkout_customer_details_spider")

# Line 219: Only SELECT query
spider_df = spark.table("payments_hf.checkout_customer_details_spider")
    .filter(F.col("subscribed_at_local") > max_csv_date)
    .select(columns)
```

### New Notebook Only Reads from S3 CSV:
```python
# Line 106-111: Only READ operations
vertices_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "false")
    .csv(f"{save_path}/vertices")  # READ ONLY
)
```

### New Notebook Writes to NEW Table Only:
```python
# Line 33: Different table name
output_table = "payments_hf.customer_identifiers_20251121"  # NEW NAME

# Line 532: Only writes to new table
save(final_df, "customer_identifiers_20251121")  # NEW TABLE
```

## Conclusion

✅ **CONFIRMED**: The new notebook does NOT overwrite any original data sources. It:
- Only reads from source tables and S3 CSV files
- Writes to a new table with a different name
- Does not modify or touch any original data sources






