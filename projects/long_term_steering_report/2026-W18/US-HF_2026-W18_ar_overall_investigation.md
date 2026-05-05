# AR Overall Investigation: US-HF 2026-W18

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 92.07% → 91.91% (-0.17%)  
**Volume:** 414,919 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined modestly from 92.07% to 91.91% (-0.16 pp) in W18, a statistically non-significant change affecting 414,919 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | -0.19 pp | ✅ |
| 2_PreDunningAR | Within normal range | -0.16 pp | ✅ |
| 3_PostDunningAR | Within normal range | -0.21 pp | ✅ |
| 6_PaymentApprovalRate | Within normal range | -0.17 pp | ✅ |

**Key Findings:**
- All funnel metrics showed slight parallel declines (-0.16 to -0.21 pp), indicating a systemic rather than stage-specific issue
- No countries exceeded the ±2.5% threshold; US showed minimal movement at -0.01 pp
- "Others" payment method showed the largest decline at -0.62 pp (88.81% → 88.19%), though volume is modest at 61,326 orders
- "Unknown" payment provider declined -0.62 pp (88.43% → 87.81%), representing 59,345 orders
- 8-week trend shows rate has fluctuated within a narrow band (91.91% - 92.22%), with current week at the lower end of this range

**Action:** Monitor — The decline is not statistically significant, no dimensional flags were triggered, and the rate remains within normal 8-week variance. Continue standard monitoring for W19.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 91.91% | 414,919 | -0.17% ← REPORTED CHANGE |
| 2026-W17 | 92.07% | 419,106 | -0.02% |
| 2026-W16 | 92.09% | 421,947 | -0.14% |
| 2026-W15 | 92.22% | 408,630 | +0.33% |
| 2026-W14 | 91.92% | 415,885 | -0.07% |
| 2026-W13 | 91.98% | 424,103 | +0.05% |
| 2026-W12 | 91.93% | 433,761 | -0.17% |
| 2026-W11 | 92.09% | 444,619 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.98% | 92.99% | -0.01% | 516,129 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 88.19% | 88.81% | -0.70% | 61,326 |  |
| Apple Pay | 85.29% | 85.56% | -0.32% | 56,761 |  |
| Credit Card | 93.52% | 93.59% | -0.08% | 246,004 |  |
| Paypal | 95.98% | 95.93% | +0.05% | 50,828 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | nan% | +nan% | 0 |  |
| Unknown | 87.81% | 88.43% | -0.71% | 59,345 |  |
| Braintree | 92.55% | 92.62% | -0.08% | 353,188 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1,950 |  |
| Adyen | 94.95% | 94.86% | +0.10% | 436 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.65% | 90.84% | -0.21% | 414,919 | 419,106 |  |
| 2_PreDunningAR | 91.91% | 92.07% | -0.18% | 414,919 | 419,106 |  |
| 3_PostDunningAR | 92.95% | 93.16% | -0.23% | 414,919 | 419,106 |  |
| 6_PaymentApprovalRate | 93.62% | 93.79% | -0.18% | 414,919 | 419,106 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 508,019 | 516,129 | +1.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
