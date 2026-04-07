# PCR Investigation: HF-INTL 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 34.88% → 36.04% (+1.16pp)  
**Volume:** ~62K payment visits

---

## Executive Summary

**Overall:** Payment Conversion Rate improved by +1.16pp from 34.88% to 36.04% despite a 23.9% decrease in payment visit volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ✅ | +0.42pp | Improved |
| Click Submit Form | ✅ | +0.59pp | Improved |
| FE Validation Passed | ✅ | +0.68pp | Improved |
| Enter Fraud Service | ✅ | +0.40pp | Improved |
| Approved by Fraud Service | ⚠️ | -0.24pp | Slight decline |
| Call to PVS | ✅ | -0.01pp | Stable |
| Successful Checkout | ✅ | +0.85pp | Strong improvement |

**Key Findings:**
- Final checkout conversion improved significantly by +0.85pp (93.94% → 94.79%), driving the overall PCR increase
- Braintree_ApplePay showed strong performance improvement with +2.84pp increase (81.34% → 84.18%)
- Adyen_CreditCard had exceptional improvement (+30.11pp) but on very low volume (116 → 69 attempts)
- Fraud Service approval rate slightly declined by -0.24pp, though this was offset by better downstream performance
- Most payment methods maintained stable conversion rates, with only minor variations

**Action:** Monitor

---

---

## Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 82,373 | 62,648 | -19,725 | -23.9% | - | - | - |
| Select Payment Method | 45,198 | 34,641 | -10,557 | -23.4% | 54.87% | 55.29% | +0.42pp |
| Click Submit Form | 36,437 | 28,131 | -8,306 | -22.8% | 80.62% | 81.21% | +0.59pp |
| FE Validation Passed | 33,860 | 26,333 | -7,527 | -22.2% | 92.93% | 93.61% | +0.68pp |
| Enter Fraud Service | 32,610 | 25,466 | -7,144 | -21.9% | 96.31% | 96.71% | +0.40pp |
| Approved by Fraud Service | 30,635 | 23,863 | -6,772 | -22.1% | 93.94% | 93.71% | -0.24pp |
| Call to PVS | 30,583 | 23,821 | -6,762 | -22.1% | 99.83% | 99.82% | -0.01pp |
| **Successful Checkout** | 28,731 | 22,580 | -6,151 | -21.4% | 93.94% | 94.79% | +0.85pp |
| **PCR Rate** | | | | | 34.88% | 36.04% | **+1.16pp** |

---

## Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 17,791 | 14,375 | 80.80% | 14,680 | 11,933 | 81.29% | +0.49pp |
| Braintree_ApplePay | 13,360 | 10,867 | 81.34% | 10,592 | 8,916 | 84.18% | +2.84pp |
| Braintree_Paypal | 9,125 | 7,940 | 87.01% | 7,030 | 6,071 | 86.36% | -0.66pp |
| Adyen_Klarna | 2,195 | 1,135 | 51.71% | 1,481 | 784 | 52.94% | +1.23pp |
| Adyen_IDeal | 1,887 | 1,597 | 84.63% | 1,322 | 1,087 | 82.22% | -2.41pp |
| ProcessOut_ApplePay | 1,558 | 1,430 | 91.78% | 1,213 | 1,098 | 90.52% | -1.26pp |
| Adyen_Sepa | 984 | 0 | 0.00% | 1,024 | 1 | 0.10% | +0.10pp |
| Adyen_BcmcMobile | 475 | 320 | 67.37% | 384 | 274 | 71.35% | +3.99pp |
| Adyen_CreditCard | 116 | 34 | 29.31% | 69 | 41 | 59.42% | +30.11pp |
| NoPayment | 105 | 0 | 0.00% | 42 | 0 | 0.00% | +0.00pp |

---

## Conclusion

The PCR improvement of +1.16pp represents a positive trend driven primarily by better final checkout conversion (+0.85pp) and improvements across most funnel steps. While payment visit volume decreased significantly (-23.9%), the quality of traffic appears higher with better conversion rates throughout the funnel, suggesting effective optimization or natural market conditions favoring conversion.

---

*Report: 2026-04-07*
