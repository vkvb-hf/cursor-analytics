# PAR Investigation: HF-NA 2026-W21

**Metric:** Payment Approval Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 93.87% → 93.64% (-0.25%)  
**Volume:** 468,983 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate declined slightly from 93.87% to 93.64% (-0.23pp) week-over-week, a statistically non-significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.27pp | ✅ |
| 2_PreDunningAR | vs Step 1 | -0.03pp | ✅ |
| 3_PostDunningAR | vs Step 2 | -0.09pp | ✅ |
| 6_PaymentApprovalRate | vs Step 3 | +0.18pp | ✅ |

**Key Findings:**
- The -0.23pp decline is within the normal 8-week fluctuation range (93.64% - 94.12%), with no statistical significance flagged
- No countries exceeded the ±2.5% threshold; US declined -0.19pp and CA declined -0.02pp, both minor movements
- PaymentProvider "Unknown" shows a ⚠️ flag with -3.48pp decline, but represents only 497 orders (0.1% of volume) - negligible impact
- All funnel steps show parallel small declines (-0.27pp to -0.42pp), suggesting a slight upstream softening at FirstRunAR rather than a specific breakpoint
- Volume declined 3.9% WoW (468,983 vs 487,754), with mix shift analysis showing stable tier composition across US (-3.1%) and CA (-4.4%)

**Action:** Monitor — No intervention required. The decline is non-significant, no thresholds were breached, and the rate remains within normal historical bounds.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 93.64% | 468,983 | -0.25% ← REPORTED CHANGE |
| 2026-W20 | 93.87% | 487,754 | +0.21% |
| 2026-W19 | 93.67% | 508,007 | -0.27% |
| 2026-W18 | 93.92% | 506,464 | -0.11% |
| 2026-W17 | 94.02% | 510,064 | -0.11% |
| 2026-W16 | 94.12% | 513,373 | +0.02% |
| 2026-W15 | 94.1% | 497,777 | +0.12% |
| 2026-W14 | 93.99% | 507,190 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 94.25% | 94.43% | -0.19% | 478,645 |  |
| CA | 95.90% | 95.92% | -0.02% | 95,083 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 95.29% | 96.27% | -1.01% | 4,037 |  |
| Apple Pay | 88.19% | 88.83% | -0.72% | 62,360 |  |
| Paypal | 96.34% | 96.54% | -0.20% | 56,726 |  |
| Credit Card | 94.16% | 94.31% | -0.15% | 345,860 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 63.58% | 65.87% | -3.48% | 497 | ⚠️ |
| ProcessOut | 91.65% | 91.89% | -0.26% | 95,728 |  |
| Braintree | 94.01% | 94.23% | -0.24% | 345,910 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,091 |  |
| Adyen | 96.17% | 96.06% | +0.11% | 23,757 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.69% | 90.96% | -0.30% | 468,983 | 487,754 |  |
| 2_PreDunningAR | 91.84% | 92.15% | -0.33% | 468,983 | 487,754 |  |
| 3_PostDunningAR | 92.83% | 93.22% | -0.42% | 468,983 | 487,754 |  |
| 6_PaymentApprovalRate | 93.64% | 93.87% | -0.24% | 468,983 | 487,754 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 493,780 | 478,645 | -3.1% | Stable |
| CA | High (>92%) | 99,511 | 95,083 | -4.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-26*
