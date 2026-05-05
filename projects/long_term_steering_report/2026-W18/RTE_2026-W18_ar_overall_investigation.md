# AR Overall Investigation: RTE 2026-W18

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 92.75% → 92.56% (-0.20%)  
**Volume:** 430,746 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined slightly from 92.75% to 92.56% (-0.19pp) on a volume of 430,746 orders; this change is **not statistically significant**.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Rate change | -0.21% | ✅ |
| 2_PreDunningAR | Rate change | -0.21% | ✅ |
| 3_PostDunningAR | Rate change | -0.29% | ⚠️ |
| 6_PaymentApprovalRate | Rate change | -0.19% | ✅ |

**Key Findings:**
- The -0.20% week-over-week decline is within normal fluctuation range; the 8-week trend shows rates oscillating between 92.45% and 93.20%
- No countries exceeded the ±2.5% investigation threshold; TV (-2.48%) and TK (-1.89%) showed the largest declines but on very low volumes (1,964 and 2,017 orders respectively)
- All payment methods showed minor declines: Others (-0.34%), Apple Pay (-0.22%), Credit Card (-0.16%), PayPal (-0.15%)
- FJ dominates volume (396,039 orders, 92% of total) with a minimal -0.12% decline, keeping overall impact low
- Mix shift analysis shows stable volume distribution across all countries with no significant structural changes

**Action:** **Monitor** — No investigation required. The decline is not statistically significant, no dimensions breach alert thresholds, and the change falls within normal weekly variance observed over the 8-week period.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 92.56% | 430,746 | -0.20% ← REPORTED CHANGE |
| 2026-W17 | 92.75% | 430,821 | +0.12% |
| 2026-W16 | 92.64% | 429,385 | -0.20% |
| 2026-W15 | 92.83% | 421,406 | +0.41% |
| 2026-W14 | 92.45% | 431,856 | -0.36% |
| 2026-W13 | 92.78% | 442,530 | -0.33% |
| 2026-W12 | 93.09% | 443,994 | -0.12% |
| 2026-W11 | 93.2% | 458,408 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 90.33% | 92.62% | -2.48% | 1,964 |  |
| TK | 90.23% | 91.98% | -1.89% | 2,017 |  |
| TO | 86.87% | 87.92% | -1.20% | 3,214 |  |
| TZ | 91.19% | 91.68% | -0.53% | 3,134 |  |
| CF | 93.81% | 93.93% | -0.14% | 53,548 |  |
| FJ | 93.69% | 93.80% | -0.12% | 396,039 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 91.73% | 92.04% | -0.34% | 88,400 |  |
| Apple Pay | 90.36% | 90.56% | -0.22% | 55,496 |  |
| Credit Card | 92.45% | 92.6% | -0.16% | 231,519 |  |
| Paypal | 96.54% | 96.68% | -0.15% | 55,331 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | nan% | +nan% | 0 |  |
| Unknown | 91.29% | 91.57% | -0.31% | 82,865 |  |
| Adyen | 89.82% | 90.08% | -0.29% | 77,411 |  |
| Braintree | 93.72% | 93.84% | -0.13% | 269,912 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 558 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.95% | 91.14% | -0.21% | 430,746 | 430,821 |  |
| 2_PreDunningAR | 92.56% | 92.75% | -0.21% | 430,746 | 430,821 |  |
| 3_PostDunningAR | 94.05% | 94.33% | -0.29% | 430,746 | 430,821 |  |
| 6_PaymentApprovalRate | 94.65% | 94.83% | -0.19% | 430,746 | 430,821 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 389,383 | 396,039 | +1.7% | Stable |
| CF | High (>92%) | 54,258 | 53,548 | -1.3% | Stable |
| YE | Medium (>85%) | 44,188 | 45,256 | +2.4% | Stable |
| TT | High (>92%) | 4,649 | 4,511 | -3.0% | Stable |
| TO | Medium (>85%) | 3,295 | 3,214 | -2.5% | Stable |
| TZ | Medium (>85%) | 3,221 | 3,134 | -2.7% | Stable |
| TV | High (>92%) | 2,101 | 1,964 | -6.5% | Stable |
| TK | Medium (>85%) | 2,081 | 2,017 | -3.1% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
