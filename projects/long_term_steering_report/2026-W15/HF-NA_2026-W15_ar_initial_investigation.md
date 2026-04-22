# AR Initial (LL0) Investigation: HF-NA 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 89.82% → 89.44% (-0.42%)  
**Volume:** 18,103 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) for HF-NA declined slightly from 89.82% to 89.44% (-0.38 pp) in 2026-W16, a statistically non-significant change within normal weekly fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (89.15%-90.82%) | -0.42% | ✅ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | CA -0.69%, US +0.63% | ✅ |
| L1: Payment Method | No method exceeds threshold | Others -1.85%, Paypal -1.16% | ✅ |
| L1: Payment Provider | No provider exceeds threshold | Unknown -1.95%, Adyen -0.61% | ✅ |
| L3: Related Metrics | All funnel metrics stable/improving | +0.20% to +0.41% | ✅ |
| Mix Shift | Volume distribution stable | US -6.2%, CA -6.4% | ✅ |

**Key Findings:**
- The -0.42% week-over-week decline is within normal variance; 8-week range spans 89.15% to 90.82%
- CA declined by -0.69 pp (91.35% → 90.72%) while US improved by +0.63 pp (88.83% → 89.39%), offsetting each other
- "Others" payment method showed the largest decline (-1.85 pp) but represents only 802 orders (4.4% of volume)
- All related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) showed slight improvements (+0.20% to +0.41%)
- Volume decreased from ~17,161 to ~18,103 orders with stable mix between US and CA markets

**Action:** Monitor — No investigation required. The change is not statistically significant, no dimensions exceeded alert thresholds, and related metrics are trending positively.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 89.44% | 18,103 | -0.42% |
| 2026-W15 | 89.82% | 16,084 | +0.20% ← REPORTED CHANGE |
| 2026-W14 | 89.64% | 17,161 | +0.55% |
| 2026-W13 | 89.15% | 16,163 | -0.57% |
| 2026-W12 | 89.66% | 21,062 | -1.28% |
| 2026-W11 | 90.82% | 21,784 | +1.09% |
| 2026-W10 | 89.84% | 25,446 | +0.25% |
| 2026-W09 | 89.62% | 25,208 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 90.72% | 91.35% | -0.69% | 5,162 |  |
| US | 89.39% | 88.83% | +0.63% | 10,922 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 97.01% | 98.83% | -1.85% | 802 |  |
| Paypal | 89.15% | 90.2% | -1.16% | 1,309 |  |
| Apple Pay | 88.37% | 88.32% | +0.06% | 4,997 |  |
| Credit Card | 90.07% | 89.46% | +0.68% | 8,976 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 96.47% | 98.39% | -1.95% | 652 |  |
| Adyen | 92.55% | 93.12% | -0.61% | 94 |  |
| Braintree | 88.33% | 88.57% | -0.27% | 6,445 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 126 |  |
| ProcessOut | 90.24% | 89.6% | +0.71% | 8,767 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.78% | 88.42% | +0.41% | 16,084 | 17,161 |  |
| 2_PreDunningAR | 89.82% | 89.64% | +0.20% | 16,084 | 17,161 |  |
| 3_PostDunningAR | 90.03% | 89.81% | +0.24% | 16,084 | 17,161 |  |
| 6_PaymentApprovalRate | 90.25% | 90.04% | +0.23% | 16,084 | 17,161 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 11,645 | 10,922 | -6.2% | Stable |
| CA | Medium (>85%) | 5,516 | 5,162 | -6.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
