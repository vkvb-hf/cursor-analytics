# PCR Investigation: RTE 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 37.81% → 39.36% (+1.56pp)  
**Volume:** ~63K payment visits

---

## Executive Summary

**Overall:** Payment Conversion Rate improved from 37.81% to 39.36%, representing a +1.56pp increase despite a 10.4% decline in payment visit volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ✅ | +1.76pp | Strong improvement in initial engagement |
| Click Submit Form | ✅ | +0.90pp | Continued positive momentum |
| FE Validation Passed | ⚠️ | -0.46pp | Minor decline in validation success |
| Enter Fraud Service | ⚠️ | -0.21pp | Slight decrease in fraud service entry |
| Approved by Fraud Service | ⚠️ | -0.12pp | Small reduction in fraud approval rate |
| Call to PVS | ⚠️ | -0.09pp | Minor decline in PVS call success |
| Successful Checkout | ✅ | +0.32pp | Recovery with improved final conversion |

**Key Findings:**
- Strong performance gains in early funnel stages (+1.76pp at payment method selection) more than offset minor declines in mid-funnel validation and fraud processing steps
- Adyen_CreditCard experienced significant performance degradation (-5.91pp to 84.68%) while other major payment methods maintained or improved rates
- Braintree_Paypal declined -2.29pp to 90.78%, representing the second-largest payment method deterioration
- Volume decreased across all funnel steps by approximately 6-7%, indicating consistent traffic reduction rather than step-specific issues
- Despite lower overall traffic, the improved conversion efficiency resulted in only a 6.7% decline in successful checkouts versus the 10.4% visit decline

**Action:** Monitor closely, particularly Adyen_CreditCard performance and mid-funnel validation processes.

---

---

## Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 70,720 | 63,359 | -7,361 | -10.4% | - | - | - |
| Select Payment Method | 34,070 | 31,640 | -2,430 | -7.1% | 48.18% | 49.94% | +1.76pp |
| Click Submit Form | 30,387 | 28,506 | -1,881 | -6.2% | 89.19% | 90.09% | +0.90pp |
| FE Validation Passed | 29,662 | 27,695 | -1,967 | -6.6% | 97.61% | 97.15% | -0.46pp |
| Enter Fraud Service | 29,066 | 27,080 | -1,986 | -6.8% | 97.99% | 97.78% | -0.21pp |
| Approved by Fraud Service | 27,934 | 25,992 | -1,942 | -7.0% | 96.11% | 95.98% | -0.12pp |
| Call to PVS | 27,902 | 25,940 | -1,962 | -7.0% | 99.89% | 99.80% | -0.09pp |
| **Successful Checkout** | 26,738 | 24,941 | -1,797 | -6.7% | 95.83% | 96.15% | +0.32pp |
| **PCR Rate** | | | | | 37.81% | 39.36% | **+1.56pp** |

---

## Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 17,491 | 16,288 | 93.12% | 17,123 | 15,986 | 93.36% | +0.24pp |
| Braintree_ApplePay | 11,367 | 10,476 | 92.16% | 10,528 | 9,742 | 92.53% | +0.37pp |
| Adyen_CreditCard | 9,936 | 9,001 | 90.59% | 9,248 | 7,831 | 84.68% | -5.91pp |
| Braintree_Paypal | 5,297 | 4,930 | 93.07% | 4,880 | 4,430 | 90.78% | -2.29pp |
| Adyen_IDeal | 809 | 592 | 73.18% | 676 | 475 | 70.27% | -2.91pp |
| Adyen_Klarna | 378 | 244 | 64.55% | 297 | 187 | 62.96% | -1.59pp |
| Braintree_CreditCard | 125 | 24 | 19.20% | 91 | 17 | 18.68% | -0.52pp |
| Braintree_Venmo | 4 | 4 | 100.00% | 6 | 6 | 100.00% | +0.00pp |
|  | 4 | 4 | 100.00% | 1 | 1 | 100.00% | +0.00pp |

---

## Conclusion

The +1.56pp improvement in PCR demonstrates strong conversion optimization despite reduced traffic volume. While early funnel engagement improved significantly, the notable decline in Adyen_CreditCard performance (-5.91pp) and minor deteriorations in validation/fraud processing steps warrant continued monitoring to ensure sustainable performance gains.

---

*Report: 2026-04-07*
