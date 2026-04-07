# PCR Investigation: HF-NA 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 28.63% → 27.95% (-0.68pp)  
**Volume:** ~59K payment visits

---

## Executive Summary

**Overall:** Payment Conversion Rate declined by 0.68pp from 28.63% to 27.95% in 2026-W14, representing a decrease of 358 successful checkouts despite stable visit volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ⚠️ | -0.34pp | Conversion dropped to 40.76% |
| Click Submit Form | ⚠️ | -0.41pp | Conversion dropped to 85.15% |
| FE Validation Passed | ⚠️ | -0.67pp | Conversion dropped to 94.25% |
| Enter Fraud Service | ⚠️ | -0.15pp | Conversion dropped to 97.71% |
| Approved by Fraud Service | ⚠️ | -0.33pp | Conversion dropped to 93.20% |
| Call to PVS | ⚠️ | -0.18pp | Conversion dropped to 99.74% |
| Successful Checkout | ✅ | +0.28pp | Conversion improved to 94.08% |

**Key Findings:**
- Front-end validation showed the largest conversion drop at -0.67pp, indicating potential technical issues with form validation
- Every funnel step through PVS calls experienced declining conversion rates, with cumulative impact leading to overall PCR decline
- Payment method performance was mixed: Apple Pay (+1.71pp) and ProcessOut Credit Card (+1.48pp) improved, while Braintree Credit Card declined significantly (-7.49pp)
- Final checkout step actually improved (+0.28pp), suggesting issues are concentrated in earlier funnel stages rather than payment processing
- Payment visit volume remained stable with only 161 additional visits (+0.3%), indicating the decline is conversion-driven rather than volume-driven

**Action:** Investigate - Focus on front-end validation issues and Braintree Credit Card performance decline.

---

---

## Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 59,286 | 59,447 | 161 | 0.3% | - | - | - |
| Select Payment Method | 24,367 | 24,232 | -135 | -0.6% | 41.10% | 40.76% | -0.34pp |
| Click Submit Form | 20,847 | 20,633 | -214 | -1.0% | 85.55% | 85.15% | -0.41pp |
| FE Validation Passed | 19,788 | 19,446 | -342 | -1.7% | 94.92% | 94.25% | -0.67pp |
| Enter Fraud Service | 19,364 | 19,001 | -363 | -1.9% | 97.86% | 97.71% | -0.15pp |
| Approved by Fraud Service | 18,111 | 17,708 | -403 | -2.2% | 93.53% | 93.20% | -0.33pp |
| Call to PVS | 18,097 | 17,662 | -435 | -2.4% | 99.92% | 99.74% | -0.18pp |
| **Successful Checkout** | 16,975 | 16,617 | -358 | -2.1% | 93.80% | 94.08% | +0.28pp |
| **PCR Rate** | | | | | 28.63% | 27.95% | **-0.68pp** |

---

## Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 14,991 | 11,597 | 77.36% | 13,953 | 11,000 | 78.84% | +1.48pp |
| Braintree_ApplePay | 7,428 | 6,136 | 82.61% | 7,371 | 6,215 | 84.32% | +1.71pp |
| Braintree_Paypal | 1,961 | 1,585 | 80.83% | 2,071 | 1,680 | 81.12% | +0.29pp |
| Adyen_CreditCard | 130 | 3 | 2.31% | 241 | 6 | 2.49% | +0.18pp |
| Braintree_CreditCard | 281 | 40 | 14.23% | 178 | 12 | 6.74% | -7.49pp |
|  | 136 | 129 | 94.85% | 120 | 119 | 99.17% | +4.31pp |
| Braintree_Venmo | 0 | 0 | 0.00% | 1 | 1 | 100.00% | +100.00pp |
| ApplePay | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |
| NoPayment | 1 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Conclusion

The 0.68pp decline in PCR appears to be driven primarily by technical issues in the early-to-mid funnel stages, particularly around front-end validation which showed the largest conversion drop. While individual payment methods showed mixed performance and the final checkout step actually improved, the cumulative effect of declining conversion rates through multiple funnel steps resulted in 358 fewer successful payments. Immediate investigation into front-end validation processes and Braintree Credit Card integration is recommended to address the root causes.

---

*Report: 2026-04-07*
