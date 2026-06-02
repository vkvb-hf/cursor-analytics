# AR Overall Investigation: HF-INTL 2026-W22

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 94.94% → 94.48% (-0.48%)  
**Volume:** 701,486 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined by -0.48pp (94.94% → 94.48%) on 701,486 orders in 2026-W22, a change that is **not statistically significant**.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.59pp | ⚠️ |
| 2_PreDunningAR | Reported Metric | -0.48pp | ⚠️ |
| 3_PostDunningAR | Recovery | -0.38pp | ⚠️ |
| 6_PaymentApprovalRate | Final Approval | -0.12pp | ✅ |

**Key Findings:**
- All funnel stages show parallel declines (-0.12pp to -0.59pp), indicating a broad systemic trend rather than an isolated issue at a single stage
- No countries exceeded the ±2.5% threshold; AT (-1.57pp), LU (-1.41pp), and BE (-1.21pp) showed the largest declines but remain within tolerance
- Apple Pay showed the largest payment method decline at -1.05pp (88.94%), though volume is relatively modest at 92,061 orders
- Volume decreased -6.3% WoW (748,329 → 701,486), with notable volume drops in DE (-11.0%), NO (-11.0%), and LU (-19.2%)
- Mix shift analysis shows all countries maintaining stable tier positions despite volume fluctuations

**Action:** **Monitor** – The decline is not statistically significant and no dimensional breakdowns exceed alert thresholds. Continue standard monitoring through W23 to assess if the trend persists.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 94.48% | 701,486 | -0.48% ← REPORTED CHANGE |
| 2026-W21 | 94.94% | 748,329 | -0.14% |
| 2026-W20 | 95.07% | 747,471 | +0.50% |
| 2026-W19 | 94.6% | 789,069 | +0.73% |
| 2026-W18 | 93.91% | 780,744 | -0.73% |
| 2026-W17 | 94.6% | 794,597 | -0.20% |
| 2026-W16 | 94.79% | 804,152 | +0.07% |
| 2026-W15 | 94.72% | 744,637 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AT | 94.32% | 95.83% | -1.57% | 11,910 |  |
| LU | 94.48% | 95.83% | -1.41% | 2,538 |  |
| BE | 95.18% | 96.35% | -1.21% | 67,481 |  |
| DK | 96.62% | 97.43% | -0.83% | 32,657 |  |
| DE | 97.05% | 97.63% | -0.59% | 182,115 |  |
| FR | 94.06% | 94.56% | -0.53% | 128,778 |  |
| GB | 93.75% | 94.24% | -0.52% | 177,783 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 88.94% | 89.88% | -1.05% | 92,061 |  |
| Credit Card | 92.88% | 93.3% | -0.46% | 323,451 |  |
| Paypal | 97.6% | 97.94% | -0.35% | 171,045 |  |
| Others | 98.81% | 99.13% | -0.32% | 114,929 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Braintree | 94.88% | 95.42% | -0.57% | 257,549 |  |
| ProcessOut | 92.54% | 92.99% | -0.49% | 199,428 |  |
| Adyen | 95.62% | 96.0% | -0.39% | 238,662 |  |
| No Payment | 99.98% | 100.0% | -0.02% | 4,251 |  |
| Unknown | 89.1% | 88.26% | +0.94% | 1,596 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 92.4% | 92.94% | -0.59% | 701,486 | 748,329 |  |
| 2_PreDunningAR | 94.48% | 94.94% | -0.48% | 701,486 | 748,329 |  |
| 3_PostDunningAR | 96.6% | 96.97% | -0.38% | 701,486 | 748,329 |  |
| 6_PaymentApprovalRate | 97.45% | 97.57% | -0.12% | 701,486 | 748,329 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 204,608 | 182,115 | -11.0% | Stable |
| GB | High (>92%) | 194,230 | 177,783 | -8.5% | Stable |
| FR | High (>92%) | 134,066 | 128,778 | -3.9% | Stable |
| NL | High (>92%) | 99,062 | 96,213 | -2.9% | Stable |
| AU | High (>92%) | 95,841 | 94,369 | -1.5% | Stable |
| BE | High (>92%) | 67,838 | 67,481 | -0.5% | Stable |
| DK | High (>92%) | 35,110 | 32,657 | -7.0% | Stable |
| SE | High (>92%) | 34,022 | 33,392 | -1.9% | Stable |
| NO | High (>92%) | 20,266 | 18,033 | -11.0% | Stable |
| NZ | Medium (>85%) | 19,034 | 19,909 | +4.6% | Stable |
| IE | Medium (>85%) | 18,635 | 17,988 | -3.5% | Stable |
| AT | High (>92%) | 12,530 | 11,910 | -4.9% | Stable |
| LU | High (>92%) | 3,142 | 2,538 | -19.2% | Stable |
| CH | High (>92%) | 2,147 | 2,142 | -0.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-02*
