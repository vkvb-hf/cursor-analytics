# AR Initial (LL0) Investigation: WL 2026-W22

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 91.97% → 91.07% (-0.98%)  
**Volume:** 11,295 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) declined from 91.97% to 91.07% (-0.90pp) in W22, with the change flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal range (90.99%-92.15%) | -0.90pp | ✅ |
| L1: Country Variance | 3 countries exceed ±2.5% threshold | CK -8.24%, AO -3.85%, ER +2.85% | ⚠️ |
| L1: Payment Method | Credit Card decline | -2.79% | ⚠️ |
| L1: Payment Provider | Adyen significant decline | -6.28% | ⚠️ |
| L2: Root Causes Identified | Multiple country-specific issues | See below | ⚠️ |
| L3: Related Metrics | All funnel metrics declining | -0.98% to -1.70% | ⚠️ |

**Key Findings:**
- **CK experienced the largest decline (-8.24pp):** Driven by PayPal transactions via Braintree with a 24.02% drop; "Insufficient Funds" declines increased by +4.04pp
- **AO declined -3.85pp:** Credit card transactions via Adyen dropped 5.24%, with "Insufficient Funds" rising +2.90pp
- **ER improved +2.85pp:** Apple Pay via Braintree showed strong recovery (+6.35% and +8.87% respectively), with "Refused" declines decreasing by -2.59pp
- **Adyen provider shows systemic weakness:** Overall -6.28% decline affecting both CK and AO markets
- **Mix shift shows AO volume increased +28.5%:** Higher volume from this low-performing tier (81.36% AR) contributed to overall decline

**Action:** **Monitor** — The overall change is not statistically significant and remains within the 8-week trend range. However, closely monitor CK and AO markets for continued "Insufficient Funds" decline patterns, particularly PayPal/Braintree in CK and Credit Card/Adyen in AO. Escalate if decline persists into W23.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 91.07% | 11,295 | -0.98% ← REPORTED CHANGE |
| 2026-W21 | 91.97% | 11,162 | +0.15% |
| 2026-W20 | 91.83% | 12,110 | -0.31% |
| 2026-W19 | 92.12% | 12,190 | +0.20% |
| 2026-W18 | 91.94% | 11,376 | -0.23% |
| 2026-W17 | 92.15% | 11,532 | +0.99% |
| 2026-W16 | 91.25% | 12,996 | +0.29% |
| 2026-W15 | 90.99% | 11,557 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CK | 81.92% | 89.28% | -8.24% | 1,903 | ⚠️ |
| AO | 81.36% | 84.62% | -3.85% | 735 | ⚠️ |
| MR | 96.90% | 98.14% | -1.26% | 2,616 |  |
| KN | 95.32% | 93.52% | +1.93% | 2,138 |  |
| ER | 87.49% | 85.06% | +2.85% | 1,359 | ⚠️ |

**Countries exceeding ±2.5% threshold:** CK, AO, ER

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 88.81% | 91.36% | -2.79% | 5,704 | ⚠️ |
| Others | 99.47% | 99.17% | +0.30% | 1,317 |  |
| Paypal | 88.54% | 87.89% | +0.74% | 1,152 |  |
| Apple Pay | 92.57% | 91.55% | +1.12% | 3,122 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Adyen | 83.69% | 89.29% | -6.28% | 2,078 | ⚠️ |
| ProcessOut | 89.65% | 91.15% | -1.65% | 2,743 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 15 |  |
| Unknown | 99.44% | 99.13% | +0.31% | 1,250 |  |
| Braintree | 92.72% | 91.62% | +1.20% | 5,209 |  |

---

## L2: CK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 4 | 0 |  |
| None | 0.00% | 0.00% | +0.00% | 0 | 3 |  |
| paypal | 64.96% | 85.50% | -24.02% | 254 | 200 | ⚠️ |
| credit_card | 82.72% | 89.27% | -7.34% | 1,354 | 1,258 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 2 | 4 |  |
| applepay | 94.12% | 92.86% | +1.36% | 289 | 280 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 4 | 3 |  |
| Braintree | 80.48% | 89.79% | -10.37% | 543 | 480 | ⚠️ |
| Adyen | 82.72% | 89.27% | -7.34% | 1,354 | 1,258 | ⚠️ |
| No Payment | 100.00% | 100.00% | +0.00% | 2 | 4 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,559 | 1,558 | 81.92% | 89.28% | -7.36 |
| Insufficient Funds | 174 | 89 | 9.14% | 5.10% | +4.04 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 123 | 57 | 6.46% | 3.27% | +3.20 |
| Other reasons | 43 | 38 | 2.26% | 2.18% | +0.08 |
| Unknown | 4 | 3 | 0.21% | 0.17% | +0.04 |

**Root Cause:** paypal + Braintree + Insufficient

---

## L2: AO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| None | 0.00% | 0.00% | +0.00% | 0 | 1 |  |
| credit_card | 79.13% | 83.51% | -5.24% | 369 | 291 | ⚠️ |
| applepay | 80.31% | 82.47% | -2.63% | 259 | 194 |  |
| paypal | 92.45% | 94.19% | -1.84% | 106 | 86 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 1 | 1 |  |
| Adyen | 79.13% | 83.51% | -5.24% | 369 | 291 | ⚠️ |
| ProcessOut | 80.31% | 82.47% | -2.63% | 259 | 194 |  |
| Braintree | 92.45% | 94.19% | -1.84% | 106 | 86 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 598 | 484 | 81.36% | 84.62% | -3.25 |
| Insufficient Funds | 119 | 76 | 16.19% | 13.29% | +2.90 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 11 | 7 | 1.50% | 1.22% | +0.27 |
| Other reasons | 6 | 4 | 0.82% | 0.70% | +0.12 |
| Unknown | 1 | 1 | 0.14% | 0.17% | -0.04 |

**Root Cause:** credit_card + Adyen + Insufficient

---

## L2: ER Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 0 | 2 |  |
| credit_card | 84.49% | 86.71% | -2.55% | 761 | 805 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 2 | 2 |  |
| applepay | 90.65% | 85.24% | +6.35% | 460 | 481 | ⚠️ |
| paypal | 93.38% | 78.82% | +18.48% | 136 | 203 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 0 | 2 |  |
| ProcessOut | 84.55% | 86.63% | -2.40% | 738 | 778 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 2 | 2 |  |
| Braintree | 90.95% | 83.54% | +8.87% | 619 | 711 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 13 | 53 | 0.96% | 3.55% | -2.59 |
| 1. SUCCESSFULL | 1,189 | 1,270 | 87.49% | 85.06% | +2.43 |
| Other reasons | 43 | 42 | 3.16% | 2.81% | +0.35 |
| Unknown | 0 | 2 | 0.00% | 0.13% | -0.13 |
| Insufficient Funds | 114 | 126 | 8.39% | 8.44% | -0.05 |

**Root Cause:** applepay + Braintree + Refused

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.27% | 89.8% | -1.70% | 11,295 | 11,162 |  |
| 2_PreDunningAR | 91.07% | 91.97% | -0.98% | 11,295 | 11,162 |  |
| 3_PostDunningAR | 91.26% | 92.64% | -1.48% | 11,295 | 11,162 |  |
| 6_PaymentApprovalRate | 91.45% | 92.86% | -1.52% | 11,295 | 11,162 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| KN | High (>92%) | 2,392 | 2,138 | -10.6% | Stable |
| MR | High (>92%) | 2,261 | 2,616 | +15.7% | Stable |
| CK | Medium (>85%) | 1,745 | 1,903 | +9.1% | Stable |
| ER | Medium (>85%) | 1,493 | 1,359 | -9.0% | Stable |
| CG | Medium (>85%) | 1,483 | 1,474 | -0.6% | Stable |
| GN | High (>92%) | 1,216 | 1,070 | -12.0% | Stable |
| AO | Low (>85%) | 572 | 735 | +28.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| CK | ↓ -8.24% | paypal -24.0% | Braintree -10.4% | Insufficient Funds +4.04pp | paypal + Braintree + Insufficient |
| AO | ↓ -3.85% | credit_card -5.2% | Adyen -5.2% | Insufficient Funds +2.90pp | credit_card + Adyen + Insufficient |
| ER | ↑ +2.85% | applepay +6.4% | Braintree +8.9% | Refused - eg: Declined, Closed Card, Do Not Honor, etc. -2.59pp | applepay + Braintree + Refused |

---

*Report: 2026-06-02*
