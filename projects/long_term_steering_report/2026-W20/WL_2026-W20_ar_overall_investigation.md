# AR Overall Investigation: WL 2026-W20

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 89.66% → 89.65% (-0.01%)  
**Volume:** 159,098 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate remained essentially flat at 89.65%, declining by just -0.01pp from the prior week, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within tolerance | +0.19pp | ✅ |
| 2_PreDunningAR | Within tolerance | -0.01pp | ✅ |
| 3_PostDunningAR | Within tolerance | -0.10pp | ✅ |
| 6_PaymentApprovalRate | Within tolerance | +0.05pp | ✅ |

**Key Findings:**
- The -0.01pp week-over-week change is well within normal variance; the 8-week trend shows the metric fluctuating between 89.32% and 90.09%
- KN experienced the largest country-level decline at -2.01pp (88.48% → 86.70%), but remains below the ±2.5% investigation threshold
- No payment methods or providers showed concerning movements; all changes were under ±0.30pp except ProcessOut which improved by +1.25pp
- Order volume decreased by 3.6% (165,009 → 159,098), consistent with typical weekly fluctuation
- Mix shift analysis shows all country tiers remained stable with no meaningful volume redistribution impacting the overall rate

**Action:** Monitor — No investigation required. Continue standard weekly tracking.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 89.65% | 159,098 | -0.01% ← REPORTED CHANGE |
| 2026-W19 | 89.66% | 165,009 | +0.08% |
| 2026-W18 | 89.59% | 166,895 | -0.56% |
| 2026-W17 | 90.09% | 166,258 | +0.09% |
| 2026-W16 | 90.01% | 164,785 | -0.09% |
| 2026-W15 | 90.09% | 160,979 | +0.86% |
| 2026-W14 | 89.32% | 165,018 | -0.43% |
| 2026-W13 | 89.71% | 169,667 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| KN | 86.70% | 88.48% | -2.01% | 11,084 |  |
| CK | 93.22% | 93.00% | +0.24% | 40,466 |  |
| ER | 89.66% | 89.33% | +0.38% | 66,405 |  |
| AO | 88.30% | 87.91% | +0.44% | 14,758 |  |
| GN | 95.56% | 94.92% | +0.67% | 15,192 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 94.59% | 94.8% | -0.22% | 23,738 |  |
| Credit Card | 89.07% | 89.07% | +0.00% | 112,982 |  |
| Others | 99.35% | 99.3% | +0.06% | 1,854 |  |
| Apple Pay | 86.3% | 86.05% | +0.29% | 20,524 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Braintree | 90.41% | 90.65% | -0.26% | 103,450 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 638 |  |
| Unknown | 99.22% | 99.12% | +0.10% | 1,153 |  |
| Adyen | 90.46% | 90.32% | +0.15% | 36,997 |  |
| ProcessOut | 82.18% | 81.17% | +1.25% | 16,860 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 87.83% | 87.66% | +0.19% | 159,098 | 165,009 |  |
| 2_PreDunningAR | 89.65% | 89.66% | -0.01% | 159,098 | 165,009 |  |
| 3_PostDunningAR | 90.73% | 90.82% | -0.10% | 159,098 | 165,009 |  |
| 6_PaymentApprovalRate | 91.31% | 91.27% | +0.05% | 159,098 | 165,009 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 67,441 | 66,405 | -1.5% | Stable |
| CG | High (>92%) | 44,290 | 41,024 | -7.4% | Stable |
| CK | High (>92%) | 41,704 | 40,466 | -3.0% | Stable |
| MR | Low (>85%) | 20,895 | 20,886 | +0.0% | Stable |
| AO | Medium (>85%) | 15,233 | 14,758 | -3.1% | Stable |
| GN | High (>92%) | 14,255 | 15,192 | +6.6% | Stable |
| KN | Medium (>85%) | 11,044 | 11,084 | +0.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-19*
