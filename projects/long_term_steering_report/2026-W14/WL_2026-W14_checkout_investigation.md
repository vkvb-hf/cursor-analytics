# PCR Investigation: WL 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 30.03% → 29.88% (-0.15pp)  
**Volume:** ~35K payment visits

---

## Executive Summary

**Overall:** Payment Conversion Rate declined from 30.03% to 29.88% (-0.15pp) in 2026-W14, with ~35K payment visits experiencing reduced conversion performance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ⚠️ | -0.26pp | Slight decline in selection rate |
| Click Submit Form | ✅ | +0.09pp | Minor improvement |
| FE Validation Passed | ✅ | +0.21pp | Improved validation success |
| Enter Fraud Service | ✅ | +0.21pp | Higher fraud service entry rate |
| Approved by Fraud Service | ⚠️ | -0.11pp | Slightly lower approval rate |
| Call to PVS | ⚠️ | -0.52pp | Notable decline in PVS call success |
| Successful Checkout | ✅ | +0.25pp | Improved final checkout conversion |

**Key Findings:**
- ProcessOut_CreditCard experienced severe degradation with success rate dropping from 90.06% to 71.38% (-18.68pp), representing the largest impact
- Braintree_ApplePay also declined significantly from 90.37% to 82.51% (-7.86pp), affecting a high-volume payment method
- Braintree_Paypal dropped from 91.30% to 78.77% (-12.52pp), showing consistent payment processor issues
- Call to PVS conversion declined by -0.52pp, indicating potential payment processing system issues
- Adyen_CreditCard bucked the trend with improvement of +1.29pp, suggesting processor-specific problems rather than systemic issues

**Action:** Investigate - Focus on ProcessOut and Braintree payment processor performance and PVS integration issues.

---

---

## Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 38,531 | 35,420 | -3,111 | -8.1% | - | - | - |
| Select Payment Method | 15,773 | 14,406 | -1,367 | -8.7% | 40.94% | 40.67% | -0.26pp |
| Click Submit Form | 13,947 | 12,751 | -1,196 | -8.6% | 88.42% | 88.51% | +0.09pp |
| FE Validation Passed | 13,240 | 12,131 | -1,109 | -8.4% | 94.93% | 95.14% | +0.21pp |
| Enter Fraud Service | 12,710 | 11,671 | -1,039 | -8.2% | 96.00% | 96.21% | +0.21pp |
| Approved by Fraud Service | 12,027 | 11,031 | -996 | -8.3% | 94.63% | 94.52% | -0.11pp |
| Call to PVS | 12,004 | 10,952 | -1,052 | -8.8% | 99.81% | 99.28% | -0.52pp |
| **Successful Checkout** | 11,571 | 10,584 | -987 | -8.5% | 96.39% | 96.64% | +0.25pp |
| **PCR Rate** | | | | | 30.03% | 29.88% | **-0.15pp** |

---

## Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 4,073 | 3,668 | 90.06% | 3,917 | 2,796 | 71.38% | -18.68pp |
| Braintree_ApplePay | 4,162 | 3,761 | 90.37% | 3,733 | 3,080 | 82.51% | -7.86pp |
| Adyen_CreditCard | 2,682 | 2,304 | 85.91% | 2,796 | 2,438 | 87.20% | +1.29pp |
| Braintree_Paypal | 1,850 | 1,689 | 91.30% | 1,663 | 1,310 | 78.77% | -12.52pp |
| Braintree_CreditCard | 1,602 | 1,434 | 89.51% | 1,317 | 1,143 | 86.79% | -2.72pp |
| ProcessOut_ApplePay | 411 | 349 | 84.91% | 283 | 265 | 93.64% | +8.72pp |
|  | 0 | 0 | 0.00% | 2 | 2 | 100.00% | +100.00pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 1 | 1 | 100.00% | +0.00pp |
| NoPayment | 1 | 0 | 0.00% | 1 | 0 | 0.00% | +0.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Conclusion

The PCR decline of -0.15pp appears driven primarily by payment processor-specific issues, particularly with ProcessOut_CreditCard (-18.68pp) and Braintree payment methods showing significant degradation. While overall funnel health remains stable with improvements in validation and final checkout steps, the concentrated impact on high-volume payment methods requires immediate investigation into processor reliability and PVS system integration.

---

*Report: 2026-04-07*
