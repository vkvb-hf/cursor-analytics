# AR Initial (LL0) Investigation: HF-INTL 2026-W20

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 92.66% → 92.6% (-0.06%)  
**Volume:** 29,602 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate for HF-INTL decreased marginally from 92.66% to 92.6% (-0.06pp) in W20, a change that is not statistically significant and remains within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend Stability | Rate within historical range (89.61%-92.66%) | -0.06pp | ✅ |
| Country Threshold (±2.5%) | 2 countries flagged: NZ (-3.37%), LU (+3.08%) | Mixed | ⚠️ |
| Payment Method Variance | All within threshold (<±2.5%) | Max -0.91pp | ✅ |
| Payment Provider Variance | Unknown flagged (+3.38%) | Low volume | ✅ |
| Related Metrics Alignment | All metrics stable (±0.10pp) | Consistent | ✅ |
| Mix Shift Impact | DE (-36.1%), AT (-34.5%) volume shifts | High-AR tiers | ⚠️ |

**Key Findings:**
- NZ experienced the largest decline (-3.37pp), driven by increased "Insufficient Funds" declines (+2.28pp) and Braintree performance degradation (-12.0%)
- LU improved (+3.08pp) due to reduced "Insufficient Funds" declines (-5.63pp), though volume is minimal (71 orders)
- DE volume dropped significantly (-36.1%) while FR volume increased (+34.1%), representing a notable mix shift between high-AR countries
- Apple Pay and PayPal show slight declines (-0.91pp and -0.11pp respectively), but remain within acceptable thresholds
- All related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) moved consistently, indicating no isolated breakage

**Action:** Monitor — The overall change is not significant and the metric remains at a healthy 92.6%. Continue tracking NZ Insufficient Funds trends and Braintree performance for potential escalation if degradation persists beyond W21.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 92.6% | 29,602 | -0.06% ← REPORTED CHANGE |
| 2026-W19 | 92.66% | 31,873 | +1.76% |
| 2026-W18 | 91.06% | 27,168 | - |
| 2026-W17 | 91.06% | 31,460 | +0.26% |
| 2026-W16 | 90.82% | 33,031 | -0.44% |
| 2026-W15 | 91.22% | 25,662 | +1.80% |
| 2026-W14 | 89.61% | 29,779 | -0.42% |
| 2026-W13 | 89.99% | 33,680 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| NZ | 75.84% | 78.48% | -3.37% | 745 | ⚠️ |
| IE | 89.64% | 91.27% | -1.79% | 1,264 |  |
| SE | 94.43% | 95.94% | -1.58% | 897 |  |
| DE | 95.50% | 95.23% | +0.28% | 5,200 |  |
| FR | 95.50% | 94.49% | +1.07% | 5,426 |  |
| LU | 94.37% | 91.55% | +3.08% | 71 | ⚠️ |

**Countries exceeding ±2.5% threshold:** NZ, LU

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 89.08% | 89.89% | -0.91% | 9,364 |  |
| Paypal | 97.28% | 97.39% | -0.11% | 5,220 |  |
| Others | 97.03% | 96.5% | +0.55% | 5,217 |  |
| Credit Card | 91.11% | 90.0% | +1.24% | 9,801 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Braintree | 93.31% | 94.05% | -0.79% | 13,473 |  |
| Adyen | 97.35% | 97.67% | -0.33% | 3,734 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 62 |  |
| ProcessOut | 89.58% | 88.57% | +1.14% | 10,540 |  |
| Unknown | 94.87% | 91.76% | +3.38% | 1,793 | ⚠️ |

---

## L2: NZ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 100.00% | 0.00% | +0.00% | 24 | 0 |  |
| None | 0.00% | 100.00% | -100.00% | 0 | 2 | ⚠️ |
| paypal | 56.00% | 63.64% | -12.00% | 25 | 22 | ⚠️ |
| applepay | 69.38% | 74.86% | -7.32% | 209 | 175 | ⚠️ |
| credit_card | 78.35% | 80.42% | -2.57% | 485 | 429 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 2 | 4 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 100.00% | 0.00% | +0.00% | 1 | 0 |  |
| Braintree | 56.00% | 63.64% | -12.00% | 25 | 22 | ⚠️ |
| ProcessOut | 75.47% | 78.45% | -3.79% | 685 | 580 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 2 | 4 |  |
| Adyen | 96.88% | 88.46% | +9.51% | 32 | 26 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 565 | 496 | 75.84% | 78.48% | -2.64 |
| Insufficient Funds | 149 | 112 | 20.00% | 17.72% | +2.28 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 11 | 8 | 1.48% | 1.27% | +0.21 |
| Other reasons | 20 | 16 | 2.68% | 2.53% | +0.15 |

**Root Cause:** None + Braintree + Insufficient

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 100.00% | 0.00% | +0.00% | 8 | 0 |  |
| None | 0.00% | 100.00% | -100.00% | 0 | 6 | ⚠️ |
| paypal | 80.00% | 100.00% | -20.00% | 10 | 8 | ⚠️ |
| sepadirectdebit | 100.00% | 100.00% | +0.00% | 4 | 3 |  |
| credit_card | 92.59% | 90.00% | +2.88% | 27 | 30 |  |
| applepay | 100.00% | 87.50% | +14.29% | 22 | 24 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 100.00% | 100.00% | +0.00% | 2 | 1 |  |
| Unknown | 100.00% | 100.00% | +0.00% | 8 | 6 |  |
| Adyen | 93.10% | 90.63% | +2.73% | 29 | 32 |  |
| Braintree | 93.75% | 90.63% | +3.45% | 32 | 32 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Insufficient Funds | 0 | 4 | 0.00% | 5.63% | -5.63 |
| Other reasons | 2 | 0 | 2.82% | 0.00% | +2.82 |
| 1. SUCCESSFULL | 67 | 65 | 94.37% | 91.55% | +2.82 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 2 | 2 | 2.82% | 2.82% | +0.00 |

**Root Cause:** None + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.54% | 90.55% | -0.01% | 29,602 | 31,873 |  |
| 2_PreDunningAR | 92.6% | 92.66% | -0.07% | 29,602 | 31,873 |  |
| 3_PostDunningAR | 93.03% | 93.12% | -0.10% | 29,602 | 31,873 |  |
| 6_PaymentApprovalRate | 93.39% | 93.33% | +0.06% | 29,602 | 31,873 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | High (>92%) | 8,208 | 8,704 | +6.0% | Stable |
| DE | High (>92%) | 8,132 | 5,200 | -36.1% | ⚠️ Major mix shift |
| FR | High (>92%) | 4,046 | 5,426 | +34.1% | Stable |
| AU | Low (>85%) | 2,868 | 2,585 | -9.9% | Stable |
| BE | High (>92%) | 1,817 | 1,579 | -13.1% | Stable |
| NL | High (>92%) | 1,392 | 1,244 | -10.6% | Stable |
| IE | Medium (>85%) | 1,295 | 1,264 | -2.4% | Stable |
| SE | High (>92%) | 1,085 | 897 | -17.3% | Stable |
| DK | High (>92%) | 1,044 | 904 | -13.4% | Stable |
| NO | Medium (>85%) | 720 | 583 | -19.0% | Stable |
| NZ | Low (>85%) | 632 | 745 | +17.9% | Stable |
| AT | High (>92%) | 441 | 289 | -34.5% | ⚠️ Major mix shift |
| CH | Medium (>85%) | 122 | 111 | -9.0% | Stable |
| LU | Medium (>85%) | 71 | 71 | +0.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| NZ | ↓ -3.37% | None -100.0% | Braintree -12.0% | Insufficient Funds +2.28pp | None + Braintree + Insufficient |
| LU | ↑ +3.08% | None -100.0% | → Stable | Insufficient Funds -5.63pp | None + Insufficient |

---

*Report: 2026-05-19*
