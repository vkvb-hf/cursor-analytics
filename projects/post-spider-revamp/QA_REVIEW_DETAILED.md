# Comprehensive QA Review: [PY-3368] post-spider revamp Notebook

## Executive Summary

**Status**: ⚠️ **REQUIRES FIXES BEFORE PRODUCTION**

This document provides a cell-by-cell technical review with:
1. Logic correctness validation
2. Data quality checks
3. Source data validation (checkout_customer_details_bob)
4. Downstream impact analysis
5. Edge case handling

---

## 🔴 CRITICAL ISSUES

### Issue #1: **Missing checkout_customer_details_view_20251121 Creation**

**Location**: Step 1-2 (View creation is missing from current notebook)

**Problem**: 
- The notebook references `checkout_customer_details_view_20251121` (line 560) but **never creates it**
- The view creation code was removed during refactoring
- This will cause a **runtime error** when the notebook tries to use the view

**Impact**: 
- ❌ **CRITICAL**: Notebook will fail immediately when trying to read the view
- ❌ All downstream processing will fail

**Evidence**:
```python
# Line 560: References view that doesn't exist
combined_df = spark.table("checkout_customer_details_view_20251121").select(columns)
```

**Fix Required**: Add the view creation code from the refactored version (Step 1-2)

---

### Issue #2: **CSV Data Missing Customer Attributes**

**Location**: Step 1 (checkout_customer_details_CSV creation)

**Problem**:
- CSV files only contain graph structure (edges/vertices), not customer attributes
- We create `checkout_customer_details_CSV` with all customer detail fields set to NULL
- When `AttributeProcessor` processes this data, it will generate **NO identifiers** because:
  - `first_name`, `last_name`, `phone`, `postcode`, `address`, `account_email`, `card_first_6`, `card_last_2`, `shopper_email` are all NULL
  - All identifier generation logic requires at least one non-NULL field

**Impact**:
- ❌ **CRITICAL**: CSV customers will have **ZERO identifiers** generated
- ❌ CSV data will contribute **NO edges** to the graph
- ❌ The entire purpose of using CSV data is defeated
- ❌ Only spider data will be processed, making CSV inclusion pointless

**Evidence**:
```python
# Line 412-418: AttributeProcessor._process requires customer attributes
processed_dict["identifiers"] = AttributeProcessor._generate_identifiers(
    processed_dict["attributes"]
)
# But all attributes will be None for CSV data
```

**Validation Needed**:
- Sample customers from CSV on 2025-01-01
- Check if they exist in `checkout_customer_details_bob` (excluding GDPR: `account_email NOT LIKE '%gdpr%'`)
- Verify if their attributes can be retrieved

**Fix Required**:
1. **Option A**: Join CSV customer nodes with `checkout_customer_details_bob` to get attributes
2. **Option B**: Store customer attributes in CSV files (requires re-export)
3. **Option C**: Use original `customer_identifiers` table instead of CSV files

---

### Issue #3: **customer_uuid Mismatch Between CSV and Spider**

**Location**: Throughout notebook

**Problem**:
- **CSV data**: `customer_uuid` is NULL (line 730 in old code, now in view creation)
- **Spider data**: `customer_uuid` is populated
- **AttributeProcessor**: Uses `customer_uuid` to create customer node: `customer:{business_unit}_{customer_uuid}` (line 412-414)
- For CSV data, this will create: `customer:{business_unit}_None` or fail

**Impact**:
- ❌ **CRITICAL**: Customer node format will be inconsistent
- ❌ Graph connectivity will break
- ❌ Connected components will fail

**Evidence**:
```python
# Line 412-414: AttributeProcessor creates customer node
processed_dict["customer"] = AttributeProcessor.CUSTOMER_NODE.format(
    business_unit=row_dict["business_unit"],
    customer_uuid=row_dict["customer_uuid"],  # NULL for CSV!
)
```

**Fix Required**:
- For CSV data, use `customer_id` instead of `customer_uuid` in customer node
- OR join with `checkout_customer_details_bob` to get `customer_uuid`

---

### Issue #4: **Missing GDPR Filter**

**Location**: Step 1 (checkout_customer_details_CSV creation)

**Problem**:
- When joining CSV with `checkout_customer_details_bob` (if we fix Issue #2), we need to exclude GDPR-affected customers
- GDPR customers are identified by: `account_email LIKE '%gdpr%'`
- Current code doesn't filter these out

**Impact**:
- ⚠️ **MEDIUM**: GDPR-affected customers will be included in the graph
- ⚠️ May violate data privacy requirements
- ⚠️ Inconsistent with original notebook behavior

**Fix Required**:
- Add filter: `WHERE account_email NOT LIKE '%gdpr%'` when joining with BOB

---

### Issue #5: **Date Comparison Logic Error**

**Location**: Step 1 (max_csv_date calculation)

**Problem**:
- `max_csv_date_str` is extracted as a string from CSV
- Used in SQL view creation with string comparison: `WHERE subscribed_at_local <= '{max_csv_date_str}'`
- If `subscribed_at_local` is a timestamp, string comparison may fail or give incorrect results

**Impact**:
- ⚠️ **MEDIUM**: Date boundary logic may be incorrect
- ⚠️ Some customers may be included/excluded incorrectly

**Evidence**:
```python
# Line 512: String from CSV
max_csv_date_str = max_date_result['max_created_at']

# Line in view creation: String comparison
WHERE subscribed_at_local <= '{max_csv_date_str}'
```

**Fix Required**:
- Cast `max_csv_date_str` to timestamp in SQL
- OR ensure consistent date format

---

### Issue #6: **Variable Scope Issues**

**Location**: Multiple cells

**Problem**:
- `csv_count` and `spider_count` are referenced in summary output (lines 809, 810, 827, 828)
- But these variables are only defined in Step 1-2 (view creation), which is missing
- Will cause `NameError` at runtime

**Impact**:
- ❌ **HIGH**: Summary output will fail
- ❌ Notebook execution will crash

**Evidence**:
```python
# Lines 809, 810, 827, 828: References undefined variables
output_lines.append(f"📅 CSV customers: {csv_count:,}")
output_lines.append(f"📅 Spider customers: {spider_count:,}")
```

**Fix Required**:
- Define `csv_count` and `spider_count` before using them
- OR calculate them from the final table

---

## 🟡 MEDIUM PRIORITY ISSUES

### Issue #7: **No Validation Against Source Data**

**Location**: Verification section

**Problem**:
- No validation queries to check if CSV customers match `checkout_customer_details_bob`
- No validation for sample customers on specific dates (e.g., 2025-01-01)
- No check for GDPR exclusion

**Impact**:
- ⚠️ **MEDIUM**: Cannot verify data correctness
- ⚠️ May include incorrect or GDPR-affected customers

**Fix Required**:
- Add validation queries:
  ```sql
  -- Sample validation for 2025-01-01 customers
  SELECT 
    csv.business_unit,
    csv.customer_id,
    csv.subscribed_at_local,
    bob.customer_uuid,
    bob.first_name,
    bob.last_name,
    bob.account_email
  FROM checkout_customer_details_csv_temp csv
  LEFT JOIN payments_hf.checkout_customer_details_bob bob
    ON csv.business_unit = bob.business_unit
    AND csv.customer_id = bob.customer_id
    AND DATE(csv.subscribed_at_local) = DATE(bob.subscribed_at_local)
  WHERE DATE(csv.subscribed_at_local) = '2025-01-01'
    AND bob.account_email NOT LIKE '%gdpr%'
  LIMIT 100
  ```

---

### Issue #8: **Parent Relationship Recalculation May Be Incorrect**

**Location**: Step 4 (Parent relationship recalculation)

**Problem**:
- We recalculate parent relationships on the combined dataset
- But CSV data already had parent relationships from original processing
- The recalculation may change parent assignments for CSV customers
- This could break existing graph relationships

**Impact**:
- ⚠️ **MEDIUM**: Parent relationships for CSV customers may change
- ⚠️ Downstream `graph_customers` table will have different parent assignments
- ⚠️ May affect duplicate detection logic

**Validation Needed**:
- Compare parent relationships for sample CSV customers:
  - Original: From `payments_hf.customer_identifiers` (source of CSV)
  - New: From `payments_hf.customer_identifiers_20251121`
  - Should match for CSV customers (unless there's a good reason to change)

---

### Issue #9: **Missing Error Handling**

**Location**: Throughout notebook

**Problem**:
- No try-catch blocks for critical operations
- No validation for empty DataFrames
- No check if CSV files exist
- No check if max_csv_date is NULL

**Impact**:
- ⚠️ **MEDIUM**: Notebook will fail with cryptic errors
- ⚠️ Hard to debug production issues

**Fix Required**:
- Add error handling and validation checks

---

### Issue #10: **Performance Issues**

**Location**: Multiple cells

**Problem**:
- Reading CSV files multiple times (vertices read in Step 1, edges read separately)
- No caching of intermediate DataFrames
- Window functions recalculated multiple times

**Impact**:
- ⚠️ **LOW**: Slower execution
- ⚠️ Higher resource usage

**Fix Required**:
- Cache frequently used DataFrames
- Optimize window function calculations

---

## 🟢 LOW PRIORITY ISSUES

### Issue #11: **Inconsistent Variable Naming**

**Location**: Throughout notebook

**Problem**:
- `combined_df` is reused for different purposes (edges vs customer details)
- `edges_df` is used for both graph edges and customer_identifiers edges
- Confusing variable names

**Fix Required**:
- Use more descriptive variable names
- Document variable purposes

---

### Issue #12: **Missing Documentation**

**Location**: Throughout notebook

**Problem**:
- Missing comments explaining why we recalculate metrics
- Missing explanation of data format differences
- Missing troubleshooting guide

**Fix Required**:
- Add comprehensive comments
- Document assumptions and design decisions

---

## 📋 VALIDATION QUERIES NEEDED

### Query 1: Validate CSV Customers Against BOB (2025-01-01)

```sql
-- Check if CSV customers exist in BOB and have attributes
SELECT 
  csv.business_unit,
  csv.customer_id,
  csv.subscribed_at_local as csv_date,
  bob.customer_uuid,
  bob.subscribed_at_local as bob_date,
  bob.first_name,
  bob.last_name,
  bob.phone,
  bob.postcode,
  bob.address,
  bob.account_email,
  bob.card_first_6,
  bob.card_last_2,
  bob.shopper_email,
  CASE WHEN bob.account_email LIKE '%gdpr%' THEN 1 ELSE 0 END as is_gdpr
FROM checkout_customer_details_csv_temp csv
LEFT JOIN payments_hf.checkout_customer_details_bob bob
  ON csv.business_unit = bob.business_unit
  AND csv.customer_id = bob.customer_id
  AND DATE(csv.subscribed_at_local) = DATE(bob.subscribed_at_local)
WHERE DATE(csv.subscribed_at_local) = '2025-01-01'
ORDER BY csv.business_unit, csv.customer_id
LIMIT 100
```

**Expected Results**:
- All CSV customers should have matching records in BOB
- `is_gdpr` should be 0 for all (or we need to filter)
- Customer attributes should be populated

---

### Query 2: Validate Identifier Generation

```sql
-- Check if identifiers are generated for CSV customers
SELECT 
  ci.business_unit,
  ci.customer_id,
  ci.src,
  ci.dst,
  ci.identifier_source,
  COUNT(*) as identifier_count
FROM payments_hf.customer_identifiers_20251121 ci
WHERE DATE(ci.created_at) = '2025-01-01'
  AND ci.src LIKE 'customer:%'  -- CSV format
GROUP BY ci.business_unit, ci.customer_id, ci.src, ci.dst, ci.identifier_source
ORDER BY identifier_count DESC
LIMIT 100
```

**Expected Results**:
- CSV customers should have identifiers generated
- Identifier sources should match expected types (phone, email, card_address, etc.)

---

### Query 3: Validate Parent Relationships

```sql
-- Compare parent relationships for sample customers
WITH original AS (
  SELECT 
    business_unit,
    customer_id,
    src,
    direct_parent_in_business_unit,
    direct_parent
  FROM payments_hf.customer_identifiers
  WHERE DATE(created_at) = '2025-01-01'
    AND src NOT LIKE 'customer:%'  -- Original format
),
new AS (
  SELECT 
    business_unit,
    customer_id,
    src,
    direct_parent_in_business_unit,
    direct_parent
  FROM payments_hf.customer_identifiers_20251121
  WHERE DATE(created_at) = '2025-01-01'
    AND src LIKE 'customer:%'  -- New format
)
SELECT 
  o.business_unit,
  o.customer_id,
  o.direct_parent_in_business_unit as orig_parent_bu,
  n.direct_parent_in_business_unit as new_parent_bu,
  o.direct_parent as orig_parent,
  n.direct_parent as new_parent,
  CASE 
    WHEN o.direct_parent_in_business_unit = n.direct_parent_in_business_unit THEN 'MATCH'
    ELSE 'MISMATCH'
  END as parent_bu_match,
  CASE 
    WHEN o.direct_parent = n.direct_parent THEN 'MATCH'
    ELSE 'MISMATCH'
  END as parent_match
FROM original o
JOIN new n 
  ON o.business_unit = n.business_unit
  AND o.customer_id = n.customer_id
LIMIT 100
```

**Expected Results**:
- Parent relationships should match for CSV customers
- If mismatches exist, investigate why

---

## 📊 DOWNSTREAM IMPACT ANALYSIS

### Tables Created:
1. `customer_identifiers_20251121` - **AFFECTED BY Issues #1, #2, #3, #5, #6**
2. `connected_components_20251121` - **AFFECTED BY Issues #2, #3**
3. `graph_customers_20251121` - **AFFECTED BY Issues #2, #3, #8**
4. `graph_customers_with_match_reasons_20251121` - **AFFECTED BY ALL ABOVE**

### Downstream Consumers:
- Any queries using these tables will have incorrect or missing data
- Graph analysis will be wrong
- Duplicate detection will fail
- Match reasons will be incorrect or missing

---

## ✅ RECOMMENDED FIXES (Priority Order)

1. **🔴 CRITICAL**: Add missing `checkout_customer_details_view_20251121` creation (Issue #1)
2. **🔴 CRITICAL**: Fix CSV customer attributes - join with BOB (Issue #2)
3. **🔴 CRITICAL**: Fix `customer_uuid` handling for CSV data (Issue #3)
4. **🔴 CRITICAL**: Fix variable scope issues (Issue #6)
5. **🟡 MEDIUM**: Add GDPR filter (Issue #4)
6. **🟡 MEDIUM**: Fix date comparison logic (Issue #5)
7. **🟡 MEDIUM**: Add validation queries (Issue #7)
8. **🟡 MEDIUM**: Validate parent relationships (Issue #8)
9. **🟡 MEDIUM**: Add error handling (Issue #9)
10. **🟢 LOW**: Performance optimization (Issue #10)

---

## 🧪 TESTING RECOMMENDATIONS

1. **Unit Tests**:
   - Test CSV view creation with sample data
   - Test AttributeProcessor with NULL attributes (should fail gracefully)
   - Test date comparison logic
   - Test parent relationship calculation

2. **Integration Tests**:
   - Test full pipeline with small CSV + spider dataset
   - Verify identifiers are generated for CSV customers
   - Verify connected components work correctly
   - Verify graph_customers has correct parent relationships
   - Verify match_reasons are correct

3. **Validation Tests**:
   - Run validation queries against sample date (2025-01-01)
   - Compare row counts: CSV edges + spider edges = final table edges
   - Verify no NULL `created_at` in final table
   - Verify `src` format is consistent
   - Verify date ranges are correct
   - Verify parent relationships are logical
   - Verify GDPR customers are excluded

---

## ✅ CONCLUSION

**The notebook is NOT ready for production** due to critical issues:

1. **Missing view creation** - will cause immediate failure
2. **CSV data will generate zero identifiers** - defeats the purpose
3. **customer_uuid mismatch** - will break graph connectivity
4. **Variable scope issues** - will cause runtime errors

**Recommendation**: 
1. Fix all critical issues before running
2. Run validation queries against sample data (2025-01-01)
3. Compare results with original `customer_identifiers` table
4. Test with small dataset first
5. Only proceed to production after validation passes






