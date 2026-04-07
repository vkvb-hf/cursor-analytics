# PCR Investigation: US-HF 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 26.77% → 26.40% (-0.37pp)  
**Volume:** ~44K payment visits

---

## Executive Summary

**Overall:** Payment Conversion Rate declined from 26.77% to 26.40% (-0.37pp) during week 14, representing a -2.1% decrease in successful checkouts.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ⚠️ | -0.42pp | Conversion dropped from 37.60% to 37.18% |
| Click Submit Form | ✅ | +0.02pp | Stable at 88.32% |
| FE Validation Passed | ⚠️ | -0.41pp | Conversion dropped from 94.99% to 94.58% |
| Enter Fraud Service | ✅ | +0.11pp | Slight improvement to 98.11% |
| Approved by Fraud Service | ✅ | -0.00pp | Stable at 93.67% |
| Call to PVS | ⚠️ | -0.23pp | Conversion dropped from 100.04% to 99.81% |
| Successful Checkout | ✅ | +0.26pp | Improved from 92.43% to 92.68% |

**Key Findings:**
- Primary conversion drop occurs early in funnel at Payment Method Selection (-0.42pp) and Frontend Validation (-0.41pp) stages
- ProcessOut_CreditCard and Braintree_ApplePay showed improved success rates (+2.50pp and +1.83pp respectively)
- Braintree_CreditCard experienced significant degradation, dropping from 14.23% to 6.74% (-7.49pp)
- Adyen_CreditCard remains at 0% success rate with doubled attempt volume (108→212)
- Overall payment visit volume decreased slightly by 319 visits (-0.7%)

**Action:** Investigate - Focus on frontend validation issues and Braintree_CreditCard payment method degradation.

---

---

## Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 44,370 | 44,051 | -319 | -0.7% | - | - | - |
| Select Payment Method | 16,684 | 16,377 | -307 | -1.8% | 37.60% | 37.18% | -0.42pp |
| Click Submit Form | 14,732 | 14,464 | -268 | -1.8% | 88.30% | 88.32% | +0.02pp |
| FE Validation Passed | 13,994 | 13,680 | -314 | -2.2% | 94.99% | 94.58% | -0.41pp |
| Enter Fraud Service | 13,714 | 13,422 | -292 | -2.1% | 98.00% | 98.11% | +0.11pp |
| Approved by Fraud Service | 12,847 | 12,573 | -274 | -2.1% | 93.68% | 93.67% | -0.00pp |
| Call to PVS | 12,852 | 12,549 | -303 | -2.4% | 100.04% | 99.81% | -0.23pp |
| **Successful Checkout** | 11,879 | 11,631 | -248 | -2.1% | 92.43% | 92.68% | +0.26pp |
| **PCR Rate** | | | | | 26.77% | 26.40% | **-0.37pp** |

---

## Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 10,229 | 8,132 | 79.50% | 9,309 | 7,633 | 82.00% | +2.50pp |
| Braintree_ApplePay | 5,750 | 4,813 | 83.70% | 5,745 | 4,914 | 85.54% | +1.83pp |
| Braintree_Paypal | 1,298 | 1,105 | 85.13% | 1,384 | 1,166 | 84.25% | -0.88pp |
| Adyen_CreditCard | 108 | 0 | 0.00% | 212 | 0 | 0.00% | +0.00pp |
| Braintree_CreditCard | 281 | 40 | 14.23% | 178 | 12 | 6.74% | -7.49pp |
|  | 136 | 129 | 94.85% | 120 | 119 | 99.17% | +4.31pp |
| Braintree_Venmo | 0 | 0 | 0.00% | 1 | 1 | 100.00% | +100.00pp |

---

## Conclusion

The 0.37pp decline in PCR appears to be driven primarily by early-funnel conversion issues, particularly in payment method selection and frontend validation steps. While some payment methods like ProcessOut_CreditCard showed improvement, the significant degradation in Braintree_CreditCard success rates and continued issues with Adyen_CreditCard warrant immediate technical investigation to identify and resolve underlying payment processing problems.

---

*Report: 2026-04-07*
