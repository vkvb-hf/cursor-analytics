# AR Initial (LL0) Investigation: HF-NA 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 89.64% → 89.98% (+0.38%)  
**Volume:** 17,332 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved modestly from 89.64% to 89.98% (+0.34 pp) in 2026-W15, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend Stability | Within normal range (89.23%-90.82%) | +0.34 pp | ✅ |
| Country Threshold (±2.5%) | No countries exceeded | US +0.96 pp, CA -0.70 pp | ✅ |
| Payment Method Variance | All within normal range | -1.69 pp to +0.85 pp | ✅ |
| Payment Provider Variance | All within normal range | -1.92 pp to +0.87 pp | ✅ |
| Related Metrics Alignment | All metrics moved directionally together | +0.37 pp to +0.64 pp | ✅ |

**Key Findings:**
- US showed the strongest improvement at +0.96 pp (88.81% → 89.66%), representing 70% of total volume (12,162 orders)
- CA declined by -0.70 pp (91.38% → 90.74%) but remains the higher-performing country
- "Others" payment method saw the largest decline at -1.69 pp (98.83% → 97.16%), though volume is minimal (810 orders)
- All related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) improved in parallel, indicating broad-based stability
- Volume decreased 24% from W10-W11 (~25K) to W14-W15 (~17K), reflecting expected seasonal patterns

**Action:** Monitor — No intervention required. All checks passed, change is not significant, and the metric remains stable within the 8-week historical range.

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
| CA | 90.74% | 91.38% | -0.70% | 5,170 |  |
| US | 89.66% | 88.81% | +0.96% | 12,162 |  |

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
| US | Medium (>85%) | 11,533 | 12,162 | +5.5% | Stable |
| CA | Medium (>85%) | 5,519 | 5,170 | -6.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-17*
