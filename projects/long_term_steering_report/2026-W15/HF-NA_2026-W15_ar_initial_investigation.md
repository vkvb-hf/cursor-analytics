# AR Initial (LL0) Investigation: HF-NA 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 89.64% → 89.98% (+0.38%)  
**Volume:** 17,332 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate for HF-NA Initial Charges improved marginally from 89.64% to 89.98% (+0.34 pp) in W15, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (89.23%-90.82%) | +0.34 pp | ✅ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | US +1.13%, CA -0.46% | ✅ |
| L1: Payment Method | All methods within tolerance | Range -1.69% to +0.85% | ✅ |
| L1: Payment Provider | All providers within tolerance | Range -1.92% to +0.87% | ✅ |
| L3: Related Metrics | All funnel metrics moved directionally aligned | +0.37% to +0.64% | ✅ |
| Mix Shift | Volume shifts stable | US -3.2%, CA -4.0% | ✅ |

**Key Findings:**
- The +0.34 pp improvement continues a two-week upward trend following the W13 low point of 89.23%
- US showed the strongest improvement at +1.13% while CA declined slightly by -0.46%, though neither crossed investigation thresholds
- All related metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) improved in parallel, indicating broad-based funnel health
- Volume declined 15.5% compared to W12 (17,332 vs 21,103), but this appears to be a normalization after elevated W10-W12 volumes
- "Others" payment method showed the largest rate decline (-1.69%) but represents only 4.7% of volume (810 orders)

**Action:** Monitor — No investigation required. The metric change is not significant and all dimension checks passed without flags.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 89.98% | 17,332 | +0.38% ← REPORTED CHANGE |
| 2026-W14 | 89.64% | 17,052 | +0.46% |
| 2026-W13 | 89.23% | 16,205 | -0.47% |
| 2026-W12 | 89.65% | 21,103 | -1.29% |
| 2026-W11 | 90.82% | 21,784 | +1.09% |
| 2026-W10 | 89.84% | 25,446 | +0.25% |
| 2026-W09 | 89.62% | 25,208 | -0.19% |
| 2026-W08 | 89.79% | 25,674 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 80.51% | 80.88% | -0.46% | 7,465 |  |
| US | 70.51% | 69.72% | +1.13% | 23,822 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 97.16% | 98.83% | -1.69% | 810 |  |
| Paypal | 89.72% | 90.17% | -0.50% | 1,410 |  |
| Apple Pay | 88.57% | 88.36% | +0.24% | 5,417 |  |
| Credit Card | 90.21% | 89.45% | +0.85% | 9,695 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 96.49% | 98.38% | -1.92% | 655 |  |
| Adyen | 92.55% | 93.12% | -0.61% | 94 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 132 |  |
| Braintree | 88.64% | 88.61% | +0.03% | 6,970 |  |
| ProcessOut | 90.36% | 89.58% | +0.87% | 9,481 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.95% | 88.38% | +0.64% | 17,332 | 17,052 |  |
| 2_PreDunningAR | 89.98% | 89.64% | +0.38% | 17,332 | 17,052 |  |
| 3_PostDunningAR | 90.16% | 89.83% | +0.37% | 17,332 | 17,052 |  |
| 6_PaymentApprovalRate | 90.43% | 90.07% | +0.40% | 17,332 | 17,052 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Low (>85%) | 24,598 | 23,822 | -3.2% | Stable |
| CA | Low (>85%) | 7,779 | 7,465 | -4.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-15*
