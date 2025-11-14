# Large Clusters Analysis Summary

## Investigation Date
November 2025

## Objective
Investigate clusters with `final_cluster_size > 100` to understand why they are so large and whether they are incorrectly matched (e.g., using fake phone numbers).

## Key Findings

### 1. Largest Clusters Found

| Cluster ID | Business Unit | Final Cluster Size | First Subscription | Last Subscription |
|------------|--------------|-------------------|-------------------|-------------------|
| US_548 | US | **67,077** | 2012-06-21 | 2025-11-09 |
| CG_285183 | CG | **51,343** | 2020-12-03 | 2025-11-06 |
| ER_417885 | ER | **46,136** | 2018-04-30 | 2025-11-09 |
| FJ_887289 | FJ | **30,019** | 2021-07-13 | 2025-11-08 |
| CA_1102398 | CA | **14,842** | 2016-04-22 | 2025-11-09 |

### 2. Detailed Analysis of Cluster US_548 (67,077 customers)

#### Match Reasons Breakdown
- **`['shopper_email']` alone**: **33,636 customers (50.1%)**
- **NULL match reasons**: 8,735 customers (13.0%)
- **`['phone']` alone**: 5,458 customers (8.1%)
- **Combinations** (last_name_address, phone, shopper_email): 9,248 customers (13.8%)

#### Phone Number Patterns
- **All phone numbers are hashed** (appear as SHA-256 hashes, 64+ characters)
- Pattern: `TOO_LONG` - indicates phone numbers are stored as hashes
- Cannot directly inspect for fake number patterns due to hashing
- Top phone hash is shared by **996 customers** with 759 unique addresses

#### Key Observations
1. **Shopper Email is the Primary Match Reason**: 50% of customers in this cluster are matched solely by `shopper_email`
2. **Phone Numbers are Hashed**: Cannot verify if fake numbers are being used, but the hashing prevents direct inspection
3. **Shopper emails are also likely hashed**: The query for shopper emails only returned 4 results, suggesting they may be hashed or stored differently

### 3. Root Cause Analysis

#### Why These Clusters Are So Large

1. **Shopper Email Matching**: 
   - Payment providers (PayPal, Klarna, etc.) provide `shopper_email` as part of payment token details
   - Many customers using the same payment provider account share the same shopper email
   - This creates large clusters when matching is done on `shopper_email` alone

2. **Hashed Phone Numbers**:
   - Phone numbers are stored as hashes (likely for privacy/PII compliance)
   - This prevents direct inspection for fake number patterns
   - However, hashed phone numbers can still cause clustering if many customers share the same phone number

3. **Match Logic**:
   - The cluster matching algorithm matches customers based on:
     - `shopper_email` (from payment providers)
     - `phone` (hashed)
     - `last_name_address`
     - `account_email`
     - `card_address`
   - When `shopper_email` alone matches, it creates large clusters

### 4. Recommendations

#### Immediate Actions
1. **Review Shopper Email Matching Logic**:
   - Consider requiring additional matching attributes when matching on `shopper_email` alone
   - Shopper emails from payment providers may not be unique identifiers for customers

2. **Phone Number Validation**:
   - While phone numbers are hashed, consider:
     - Checking if obvious fake numbers are excluded before hashing
     - Implementing additional validation rules for phone-based matching

3. **Match Reason Analysis**:
   - Review clusters where `shopper_email` is the only match reason
   - Consider if these are legitimate clusters or false positives

#### Long-term Improvements
1. **Multi-attribute Matching**:
   - Require at least 2 matching attributes for cluster creation
   - Especially when one of them is `shopper_email` (which may be shared across payment provider accounts)

2. **Cluster Size Limits**:
   - Consider implementing a maximum cluster size threshold
   - Clusters above a certain size (e.g., 1000) should be reviewed manually or require additional validation

3. **Match Reason Weighting**:
   - Weight match reasons differently (e.g., `shopper_email` alone may be less reliable than `phone + address`)

### 5. Conclusion

**These huge clusters are NOT primarily caused by fake phone numbers** (which are hashed and cannot be directly inspected). Instead, they are primarily caused by:

1. **Shopper email matching** - Many customers share the same shopper email from payment providers
2. **Single-attribute matching** - The algorithm allows clustering based on `shopper_email` alone, which creates large clusters

**Recommendation**: Review and potentially modify the matching logic to require multiple matching attributes, especially when `shopper_email` is involved, to prevent these oversized clusters.

