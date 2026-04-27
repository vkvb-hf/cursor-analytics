# AR Overall Investigation: RTE 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 92.64% → 92.76% (+0.13%)  
**Volume:** 430,821 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate improved marginally from 92.64% to 92.76% (+0.12 pp) in W17, a non-significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within range | +0.16 pp | ✅ |
| 2_PreDunningAR | Within range | +0.12 pp | ✅ |
| 3_PostDunningAR | Within range | -0.14 pp | ✅ |
| 6_PaymentApprovalRate | Within range | +0.03 pp | ✅ |

**Key Findings:**
- No countries exceeded the ±2.5% threshold; the largest decline was TK at -1.79 pp (low volume: 2,081 orders)
- All payment methods remained stable with Credit Card (+0.39 pp) showing the largest improvement across 235,907 orders
- ProcessOut payment provider shows no volume in W17 (down from active in W16), though overall impact is negligible
- Mix shift analysis shows all countries stable with no meaningful volume redistribution between AR tiers
- 8-week trend shows rate fluctuating within a narrow 91.55%-93.20% band, indicating consistent performance

**Action:** Monitor — No significant changes detected; all dimensions within normal operating parameters.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 92.76% | 430,821 | +0.13% ← REPORTED CHANGE |
| 2026-W16 | 92.64% | 429,385 | -0.20% |
| 2026-W15 | 92.83% | 421,406 | +0.41% |
| 2026-W14 | 92.45% | 431,856 | -0.36% |
| 2026-W13 | 92.78% | 442,530 | -0.33% |
| 2026-W12 | 93.09% | 443,994 | -0.12% |
| 2026-W11 | 93.2% | 458,408 | +1.80% |
| 2026-W10 | 91.55% | 467,998 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TK | 91.98% | 93.65% | -1.79% | 2,081 |  |
| TZ | 91.68% | 92.91% | -1.32% | 3,221 |  |
| TO | 87.92% | 88.79% | -0.98% | 3,295 |  |
| TV | 92.62% | 93.52% | -0.96% | 2,101 |  |
| FJ | 93.81% | 93.79% | +0.02% | 389,383 |  |
| CF | 93.94% | 93.47% | +0.51% | 54,258 |  |
| YE | 88.43% | 87.83% | +0.68% | 44,188 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 91.97% | 92.59% | -0.68% | 84,895 |  |
| Apple Pay | 90.56% | 90.58% | -0.01% | 54,842 |  |
| Paypal | 96.69% | 96.62% | +0.08% | 55,177 |  |
| Credit Card | 92.63% | 92.27% | +0.39% | 235,907 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 91.44% | +nan% | 0 |  |
| Unknown | 91.49% | 91.84% | -0.37% | 79,263 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 562 |  |
| Braintree | 93.87% | 93.73% | +0.15% | 272,741 |  |
| Adyen | 90.09% | 89.63% | +0.51% | 78,255 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.14% | 90.99% | +0.16% | 430,821 | 429,385 |  |
| 2_PreDunningAR | 92.76% | 92.64% | +0.12% | 430,821 | 429,385 |  |
| 3_PostDunningAR | 94.08% | 94.21% | -0.14% | 430,821 | 429,385 |  |
| 6_PaymentApprovalRate | 94.84% | 94.81% | +0.03% | 430,821 | 429,385 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 395,303 | 389,383 | -1.5% | Stable |
| CF | High (>92%) | 53,579 | 54,258 | +1.3% | Stable |
| YE | Medium (>85%) | 43,089 | 44,188 | +2.6% | Stable |
| TT | High (>92%) | 4,817 | 4,649 | -3.5% | Stable |
| TO | Medium (>85%) | 3,301 | 3,295 | -0.2% | Stable |
| TZ | High (>92%) | 3,216 | 3,221 | +0.2% | Stable |
| TK | High (>92%) | 2,079 | 2,081 | +0.1% | Stable |
| TV | High (>92%) | 2,053 | 2,101 | +2.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-27*
