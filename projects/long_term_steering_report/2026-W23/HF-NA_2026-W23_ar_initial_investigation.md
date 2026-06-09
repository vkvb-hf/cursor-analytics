# AR Initial (LL0) Investigation: HF-NA 2026-W23

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 86.92% → 87.06% (+0.16%)  
**Volume:** 15,446 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-NA improved marginally from 86.92% to 87.06% (+0.14 pp) in W23, a statistically non-significant change against a backdrop of a declining 8-week trend (down from 90.18% in W17).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.52 pp | ✅ |
| 2_PreDunningAR | Within normal range | +0.14 pp | ✅ |
| 3_PostDunningAR | Within normal range | +0.15 pp | ✅ |
| 6_PaymentApprovalRate | Within normal range | +0.34 pp | ✅ |

**Key Findings:**
- The 8-week trend shows a sustained decline of -3.12 pp from W17 (90.18%) to W23 (87.06%), indicating a longer-term degradation pattern despite this week's slight uptick
- "Unknown" PaymentProvider showed a significant improvement of +11.55 pp (77.04% → 85.94%), though on low volume (320 orders)
- "Others" PaymentMethod improved +3.44 pp (92.04% → 95.21%) on 1,022 orders, exceeding the ±2.5% threshold
- CA outperformed US with a rate of 90.61% vs 85.50%, and showed stronger week-over-week improvement (+1.26 pp vs -0.24 pp)
- No countries exceeded the ±2.5% threshold requiring deep-dive investigation

**Action:** Monitor — The weekly change is not significant and all funnel steps are healthy; however, the persistent 8-week downward trend warrants continued observation to ensure the metric stabilizes.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 87.06% | 15,446 | +0.16% ← REPORTED CHANGE |
| 2026-W22 | 86.92% | 14,518 | -1.51% |
| 2026-W21 | 88.25% | 13,744 | -1.11% |
| 2026-W20 | 89.24% | 15,004 | -0.56% |
| 2026-W19 | 89.74% | 15,375 | +0.36% |
| 2026-W18 | 89.42% | 15,684 | -0.84% |
| 2026-W17 | 90.18% | 18,020 | +0.82% |
| 2026-W16 | 89.45% | 17,968 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 85.50% | 85.71% | -0.24% | 10,716 |  |
| CA | 90.61% | 89.48% | +1.26% | 4,730 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 87.31% | 87.83% | -0.59% | 8,489 |  |
| Apple Pay | 86.28% | 86.22% | +0.07% | 4,642 |  |
| Paypal | 81.83% | 80.59% | +1.53% | 1,293 |  |
| Others | 95.21% | 92.04% | +3.44% | 1,022 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | 87.37% | 87.85% | -0.54% | 8,181 |  |
| Adyen | 96.75% | 96.92% | -0.17% | 739 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 132 |  |
| Braintree | 85.25% | 84.71% | +0.63% | 6,074 |  |
| Unknown | 85.94% | 77.04% | +11.55% | 320 | ⚠️ |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 86.03% | 85.51% | +0.60% | 15,446 | 14,518 |  |
| 2_PreDunningAR | 87.06% | 86.92% | +0.17% | 15,446 | 14,518 |  |
| 3_PostDunningAR | 87.19% | 87.04% | +0.18% | 15,446 | 14,518 |  |
| 6_PaymentApprovalRate | 87.41% | 87.07% | +0.39% | 15,446 | 14,518 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 9,850 | 10,716 | +8.8% | Stable |
| CA | Medium (>85%) | 4,668 | 4,730 | +1.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-09*
