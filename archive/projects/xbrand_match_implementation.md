# XBrand Match Implementation Summary

## Overview
Added xbrand match identification to duplicate customers datasets and xbrand match rate metrics to the simplified duplicate dashboard.

## Findings from Data Exploration

### Matching Attributes Analysis
After querying sample records from spider logs (date: 2025-11-01), we found:

**Actual matching_attributes values:**
- `phone` (4,392 occurrences, 33 business units)
- `last_name_address` (3,279 occurrences, 30 business units)
- `shopper_email` (811 occurrences, 24 business units)
- `account_email` (643 occurrences, 29 business units)
- `card_address` (306 occurrences, 21 business units)
- `name_card` (222 occurrences, 24 business units)
- `last_name_address2` (201 occurrences, 14 business units)
- `card_address2` (41 occurrences, 6 business units)

**Key Finding:** There is NO 'xbrand' attribute in the matching_attributes array. Therefore, xbrand matches must be detected by comparing business units between parent and child customers.

## Implementation

### 1. duplicate_customers.sql

#### Added parent_business_unit extraction (line 141):
- Extracts business_unit from parent_id string: `split(..., ':')[0] as parent_business_unit_from_id`
- This allows us to detect cross-brand matches even before joining to customer table

#### Updated xbrand match detection in spider CTE (lines 190-198):
- Changed from checking array for 'xbrand' to comparing business units
- Logic: A match is xbrand if:
  - The parent_business_unit_from_id (from the ID string) differs from child business_unit, OR
  - The actual parent customer's business_unit (from customer table) differs from child business_unit
- Changed join from INNER to LEFT JOIN to allow detection even if parent customer lookup fails

#### Added is_xbrand_match to decisions struct (line 441):
- Added `coalesce(spi.is_xbrand_match, false) as is_xbrand_match` to the decisions struct
- This makes the xbrand match indicator available throughout the duplicate_customers dataset

### 2. simplified_duplicate_dashboard.sql

#### Added xbrand match metrics:

**Pre-checkout metrics:**
- `spider_xbrand_duplicate_at_pre_checkout` (line 56): Count of spider duplicates that are xbrand matches at pre-checkout
- `prod_xbrand_duplicate_at_pre_checkout` (line 58): Count of production duplicates that are xbrand matches at pre-checkout

**Overall metrics:**
- `spider_xbrand_duplicate_overall` (line 70): Count of spider duplicates (pre + post checkout) that are xbrand matches
- `prod_xbrand_duplicate_overall` (line 72): Count of production duplicates (pre + post checkout) that are xbrand matches

**Matching attributes:**
- `spider_xbrand_match` (line 83): Count of records where is_xbrand_match is true

## Logic Details

### XBrand Detection Method

Since 'xbrand' is not an attribute in matching_attributes, we detect cross-brand matches by:

1. **Extracting parent business_unit from ID string:**
   - The parent_id format appears to be: `business_unit:uuid_...`
   - We extract: `split(parent_id, ':')[0]` to get parent business_unit

2. **Comparing business units:**
   - If `parent_business_unit_from_id != child_business_unit` → xbrand match
   - OR if `parent_customer.business_unit != child_business_unit` → xbrand match

3. **Fallback handling:**
   - Uses LEFT JOIN instead of INNER JOIN to allow detection even if customer lookup fails
   - Uses COALESCE to handle NULL cases safely

## Testing

### Sample Data Results
- Tested on date: 2025-11-01
- Found 0 xbrand matches in 50 sample records (all were same-brand matches)
- This is expected as most duplicates are within the same business unit

### Verification Queries
Queries created in `cursor_databricks/queries/`:
- `get_distinct_matching_attributes.sql` - Lists all matching attribute types
- `check_matching_attributes_complete.sql` - Sample records with xbrand detection

## Files Modified

1. `/Users/visal.kumar/Documents/GitHub/ddi-pays-pipelines/ddi_pays_pipelines/analytics_etl/queries/duplicate_customers.sql`
   - Added parent_business_unit_from_id extraction
   - Updated is_xbrand_match logic to compare business units
   - Changed join to LEFT JOIN for cross-brand detection

2. `/Users/visal.kumar/Documents/GitHub/ddi-pays-pipelines/ddi_pays_pipelines/analytics_etl/queries/simplified_duplicate_dashboard.sql`
   - Added xbrand match rate metrics at pre-checkout and overall levels

## Next Steps

1. **Test with full dataset:** Run the updated duplicate_customers.sql to verify xbrand detection works correctly
2. **Validate metrics:** Check that xbrand match rates are reasonable (typically low percentage)
3. **Monitor performance:** Ensure the LEFT JOIN doesn't significantly impact query performance
4. **Documentation:** Update any downstream documentation that references duplicate detection logic
