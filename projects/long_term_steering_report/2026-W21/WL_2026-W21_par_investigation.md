# PAR Investigation: WL 2026-W21

**Metric:** Payment Approval Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 91.3% → 91.14% (-0.18%)  
**Volume:** 153,361 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate declined slightly from 91.3% to 91.14% (-0.16pp) in WL 2026-W21, a change that is not statistically significant and remains within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Largest decline in funnel | -0.57pp | ⚠️ |
| 2_PreDunningAR | Moderate decline | -0.22pp | ⚠️ |
| 3_PostDunningAR | Moderate decline | -0.32pp | ⚠️ |
| 6_PaymentApprovalRate | Final metric | -0.17pp | ✅ |

**Key Findings:**
- The decline originated primarily at the FirstRunAR step (-0.57pp), indicating initial payment attempts are performing worse than prior week
- No country exceeded the ±2.5% threshold; MR showed the largest country-level decline at -1.11pp (81.19% → 82.10%)
- All payment providers declined slightly, with Braintree (-0.35pp) and ProcessOut (-0.29pp) showing the largest drops
- Volume decreased by ~3.6% (159,098 → 153,361 orders), but mix shift analysis shows all countries remained stable
- 8-week trend shows the rate remains within a narrow band (91.04% - 91.68%), indicating normal fluctuation

**Action:** Monitor — The decline is not statistically significant, no dimensions exceeded investigation thresholds, and the metric remains within historical range. Continue standard monitoring for W22.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 91.14% | 153,361 | -0.18% ← REPORTED CHANGE |
| 2026-W20 | 91.3% | 159,098 | +0.03% |
| 2026-W19 | 91.27% | 165,009 | +0.03% |
| 2026-W18 | 91.24% | 166,895 | -0.47% |
| 2026-W17 | 91.67% | 166,258 | -0.01% |
| 2026-W16 | 91.68% | 164,785 | +0.03% |
| 2026-W15 | 91.65% | 160,979 | +0.67% |
| 2026-W14 | 91.04% | 165,018 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| MR | 81.19% | 82.10% | -1.11% | 20,786 |  |
| ER | 90.75% | 90.97% | -0.24% | 60,964 |  |
| GN | 96.40% | 96.52% | -0.13% | 14,205 |  |
| CG | 97.04% | 96.98% | +0.06% | 40,366 |  |
| KN | 88.05% | 87.76% | +0.33% | 11,080 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 95.19% | 95.42% | -0.23% | 22,927 |  |
| Credit Card | 90.77% | 90.96% | -0.21% | 109,124 |  |
| Others | 99.17% | 99.35% | -0.18% | 1,929 |  |
| Apple Pay | 87.6% | 87.62% | -0.03% | 19,381 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Braintree | 91.12% | 91.44% | -0.35% | 99,707 |  |
| ProcessOut | 83.13% | 83.37% | -0.29% | 15,687 |  |
| Unknown | 99.06% | 99.22% | -0.16% | 1,273 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 598 |  |
| Adyen | 94.22% | 94.1% | +0.13% | 36,096 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 87.33% | 87.83% | -0.57% | 153,361 | 159,098 |  |
| 2_PreDunningAR | 89.44% | 89.64% | -0.22% | 153,361 | 159,098 |  |
| 3_PostDunningAR | 90.52% | 90.81% | -0.32% | 153,361 | 159,098 |  |
| 6_PaymentApprovalRate | 91.14% | 91.3% | -0.17% | 153,361 | 159,098 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 66,405 | 60,964 | -8.2% | Stable |
| CG | High (>92%) | 41,024 | 40,366 | -1.6% | Stable |
| CK | High (>92%) | 40,466 | 38,880 | -3.9% | Stable |
| MR | Low (>85%) | 20,886 | 20,786 | -0.5% | Stable |
| GN | High (>92%) | 15,192 | 14,205 | -6.5% | Stable |
| AO | High (>92%) | 14,758 | 14,291 | -3.2% | Stable |
| KN | Medium (>85%) | 11,084 | 11,080 | +0.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-26*
