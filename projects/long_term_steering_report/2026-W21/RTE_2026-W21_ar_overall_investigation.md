# AR Overall Investigation: RTE 2026-W21

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 92.72% → 92.76% (+0.04%)  
**Volume:** 401,555 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate remained stable at 92.76%, increasing marginally by +0.04pp from the prior week, a statistically non-significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.02pp | ✅ |
| 2_PreDunningAR | Reported Metric | +0.04pp | ✅ |
| 3_PostDunningAR | Recovery | -0.02pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.07pp | ✅ |

**Key Findings:**
- All funnel stages show minimal movement (<0.1pp), indicating stable end-to-end payment performance
- No countries exceeded the ±2.5% threshold; largest declines observed in TZ (-0.93pp), TT (-0.89pp), and TK (-0.83pp), all low-volume markets
- PaymentProvider "Unknown" flagged with +6.79pp change, but volume is negligible (130 orders)
- Volume declined -3.2% WoW (414,675 → 401,555 orders) with consistent decreases across most countries
- Mix shift analysis shows all country tiers remained stable with no material impact on overall rate

**Action:** Monitor — No significant changes or threshold breaches requiring investigation. Continue standard weekly tracking.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 92.76% | 401,555 | +0.04% ← REPORTED CHANGE |
| 2026-W20 | 92.72% | 414,675 | +0.78% |
| 2026-W19 | 92.0% | 427,696 | -0.59% |
| 2026-W18 | 92.55% | 430,745 | -0.20% |
| 2026-W17 | 92.74% | 430,820 | +0.11% |
| 2026-W16 | 92.64% | 429,384 | -0.20% |
| 2026-W15 | 92.83% | 421,405 | +0.41% |
| 2026-W14 | 92.45% | 431,855 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TZ | 91.92% | 92.78% | -0.93% | 2,957 |  |
| TT | 96.48% | 97.35% | -0.89% | 4,517 |  |
| TK | 93.88% | 94.66% | -0.83% | 1,928 |  |
| CF | 93.62% | 93.85% | -0.24% | 50,646 |  |
| FJ | 93.72% | 93.70% | +0.02% | 362,650 |  |
| YE | 89.60% | 88.87% | +0.82% | 41,846 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 97.96% | 98.25% | -0.30% | 5,431 |  |
| Paypal | 96.45% | 96.51% | -0.07% | 51,447 |  |
| Credit Card | 92.43% | 92.39% | +0.04% | 294,609 |  |
| Apple Pay | 90.38% | 90.14% | +0.26% | 50,068 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 500 |  |
| ProcessOut | 91.64% | 91.63% | +0.01% | 83,154 |  |
| Braintree | 93.79% | 93.78% | +0.02% | 244,756 |  |
| Adyen | 90.58% | 90.37% | +0.23% | 73,015 |  |
| Unknown | 66.15% | 61.95% | +6.79% | 130 | ⚠️ |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.1% | 91.08% | +0.02% | 401,555 | 414,675 |  |
| 2_PreDunningAR | 92.76% | 92.72% | +0.04% | 401,555 | 414,675 |  |
| 3_PostDunningAR | 94.25% | 94.27% | -0.02% | 401,555 | 414,675 |  |
| 6_PaymentApprovalRate | 94.85% | 94.78% | +0.07% | 401,555 | 414,675 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 375,015 | 362,650 | -3.3% | Stable |
| CF | High (>92%) | 52,629 | 50,646 | -3.8% | Stable |
| YE | Medium (>85%) | 44,478 | 41,846 | -5.9% | Stable |
| TT | High (>92%) | 4,567 | 4,517 | -1.1% | Stable |
| TZ | High (>92%) | 2,937 | 2,957 | +0.7% | Stable |
| TO | Medium (>85%) | 2,871 | 2,954 | +2.9% | Stable |
| TK | High (>92%) | 1,949 | 1,928 | -1.1% | Stable |
| TV | High (>92%) | 1,823 | 1,795 | -1.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-26*
