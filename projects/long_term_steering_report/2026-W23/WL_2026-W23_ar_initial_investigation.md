# AR Initial (LL0) Investigation: WL 2026-W23

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 91.04% → 92.08% (+1.14%)  
**Volume:** 12,491 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate (Initial Charges) improved from 91.04% to 92.08% (+1.14%), representing a significant positive change with 12,491 orders processed in W23.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend Stability | Rate within historical range (91.25%-92.15%) | +1.14% | ✅ |
| Country Variance | 2 countries exceed ±2.5% threshold (AO, CK) | AO -2.98%, CK +4.93% | ⚠️ |
| Payment Method Variance | PayPal shows significant improvement | +6.30% | ⚠️ |
| Payment Provider Variance | All providers within normal range | Max +1.55% (Braintree) | ✅ |
| Related Metrics Alignment | All funnel metrics improved consistently | +1.07% to +1.36% | ✅ |

**Key Findings:**
- CK drove significant improvement (+4.93%) with PayPal acceptance surging from 64.96% to 87.78% (+35.13%) via Braintree, accompanied by a 3.41pp decrease in "Refused" declines
- AO declined (-2.98%) due to Apple Pay via ProcessOut dropping from 80.23% to 75.85% (-5.47%), with Insufficient Funds increasing by +1.32pp
- Overall PayPal performance improved dramatically (+6.30%), suggesting potential payment processor optimizations taking effect
- Mix shift analysis shows stable volume distribution across AR tiers with no concerning shifts
- All related metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) improved in alignment, confirming genuine acceptance rate gains

**Action:** Monitor - The overall improvement is positive and driven by legitimate performance gains in CK/PayPal. Continue monitoring AO's ProcessOut/Apple Pay performance for potential intervention if decline persists beyond 2 weeks.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 92.08% | 12,491 | +1.14% ← REPORTED CHANGE |
| 2026-W22 | 91.04% | 11,291 | -0.85% |
| 2026-W21 | 91.82% | 11,166 | - |
| 2026-W20 | 91.82% | 12,112 | -0.30% |
| 2026-W19 | 92.1% | 12,197 | +0.17% |
| 2026-W18 | 91.94% | 11,375 | -0.23% |
| 2026-W17 | 92.15% | 11,531 | +0.99% |
| 2026-W16 | 91.25% | 12,995 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AO | 78.93% | 81.36% | -2.98% | 731 | ⚠️ |
| MR | 97.54% | 96.83% | +0.74% | 3,010 |  |
| CG | 94.16% | 93.37% | +0.85% | 1,405 |  |
| GN | 94.85% | 92.61% | +2.41% | 1,009 |  |
| CK | 85.80% | 81.77% | +4.93% | 2,211 | ⚠️ |

**Countries exceeding ±2.5% threshold:** AO, CK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 99.38% | 99.39% | -0.02% | 1,608 |  |
| Apple Pay | 92.94% | 92.54% | +0.43% | 3,256 |  |
| Credit Card | 89.31% | 88.79% | +0.59% | 6,247 |  |
| Paypal | 94.13% | 88.55% | +6.30% | 1,380 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 99.34% | 99.36% | -0.02% | 1,523 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 17 |  |
| ProcessOut | 90.22% | 89.71% | +0.56% | 2,791 |  |
| Adyen | 84.38% | 83.56% | +0.98% | 2,324 |  |
| Braintree | 94.12% | 92.69% | +1.55% | 5,836 |  |

---

## L2: AO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 2 | 0 |  |
| None | 0.00% | 0.00% | +0.00% | 0 | 1 |  |
| cashcredit | 100.00% | 0.00% | +0.00% | 1 | 0 |  |
| applepay | 75.85% | 80.23% | -5.47% | 236 | 258 | ⚠️ |
| paypal | 88.80% | 92.52% | -4.02% | 125 | 107 |  |
| credit_card | 77.93% | 79.13% | -1.52% | 367 | 369 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.00% | 0.00% | +0.00% | 1 | 0 |  |
| Unknown | 0.00% | 0.00% | +0.00% | 2 | 1 |  |
| ProcessOut | 75.85% | 80.23% | -5.47% | 236 | 258 | ⚠️ |
| Braintree | 88.80% | 92.52% | -4.02% | 125 | 107 |  |
| Adyen | 77.93% | 79.13% | -1.52% | 367 | 369 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 577 | 598 | 78.93% | 81.36% | -2.43 |
| Insufficient Funds | 128 | 119 | 17.51% | 16.19% | +1.32 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 15 | 11 | 2.05% | 1.50% | +0.56 |
| Other reasons | 9 | 6 | 1.23% | 0.82% | +0.41 |
| Unknown | 2 | 1 | 0.27% | 0.14% | +0.14 |

**Root Cause:** applepay + ProcessOut + Insufficient

---

## L2: CK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 4 | 0 |  |
| None | 0.00% | 0.00% | +0.00% | 0 | 4 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 4 | 2 |  |
| applepay | 94.61% | 94.12% | +0.52% | 371 | 289 |  |
| credit_card | 83.67% | 82.51% | +1.42% | 1,611 | 1,349 |  |
| paypal | 87.78% | 64.96% | +35.13% | 221 | 254 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 4 | 4 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 4 | 2 |  |
| Adyen | 83.67% | 82.51% | +1.42% | 1,611 | 1,349 |  |
| Braintree | 92.06% | 80.48% | +14.39% | 592 | 543 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,897 | 1,552 | 85.80% | 81.77% | +4.03 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 69 | 124 | 3.12% | 6.53% | -3.41 |
| Other reasons | 44 | 45 | 1.99% | 2.37% | -0.38 |
| Insufficient Funds | 197 | 173 | 8.91% | 9.11% | -0.20 |
| Unknown | 4 | 4 | 0.18% | 0.21% | -0.03 |

**Root Cause:** paypal + Braintree + Refused

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.5% | 88.3% | +1.36% | 12,491 | 11,291 |  |
| 2_PreDunningAR | 92.08% | 91.04% | +1.15% | 12,491 | 11,291 |  |
| 3_PostDunningAR | 92.26% | 91.29% | +1.07% | 12,491 | 11,291 |  |
| 6_PaymentApprovalRate | 92.49% | 91.48% | +1.10% | 12,491 | 11,291 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| MR | High (>92%) | 2,616 | 3,010 | +15.1% | Stable |
| KN | High (>92%) | 2,138 | 2,585 | +20.9% | Stable |
| CK | Low (>85%) | 1,898 | 2,211 | +16.5% | Stable |
| CG | High (>92%) | 1,479 | 1,405 | -5.0% | Stable |
| ER | Medium (>85%) | 1,356 | 1,540 | +13.6% | Stable |
| GN | High (>92%) | 1,069 | 1,009 | -5.6% | Stable |
| AO | Low (>85%) | 735 | 731 | -0.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| AO | ↓ -2.98% | applepay -5.5% | ProcessOut -5.5% | Insufficient Funds +1.32pp | applepay + ProcessOut + Insufficient |
| CK | ↑ +4.93% | paypal +35.1% | Braintree +14.4% | Refused - eg: Declined, Closed Card, Do Not Honor, etc. -3.41pp | paypal + Braintree + Refused |

---

*Report: 2026-06-09*
