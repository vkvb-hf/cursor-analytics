# AR Initial (LL0) Investigation: US-HF 2026-W19

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 88.21% → 89.29% (+1.22%)  
**Volume:** 11,545 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved from 88.21% to 89.29% (+1.08 pp) week-over-week, representing a statistically significant positive change on 11,545 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.97 pp | ✅ |
| 2_PreDunningAR | Reported Metric | +1.08 pp | ✅ |
| 3_PostDunningAR | Post-Dunning | +1.06 pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +1.12 pp | ✅ |

**Key Findings:**
- Credit Card acceptance rate improved significantly (+2.72 pp to 91.07%), driving overall improvement given its dominant volume (6,308 orders, 55% of total)
- ProcessOut provider showed strong improvement (+2.78 pp to 91.19%) on 6,195 orders, aligning with Credit Card gains
- "Unknown" PaymentProvider experienced a severe decline (-15.99 pp to 78.07%), though limited to 114 orders
- "Others" PaymentMethod declined (-4.86 pp to 90.0%) on 290 orders, warranting monitoring
- All funnel stages (FirstRun through PaymentApproval) moved in consistent positive direction, indicating systemic improvement rather than isolated anomaly

**Action:** Monitor — The improvement is broad-based across the payment funnel with Credit Card/ProcessOut driving gains. Continue tracking "Unknown" provider performance and "Others" payment method, but no escalation required given low volumes.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 89.29% | 11,545 | +1.22% ← REPORTED CHANGE |
| 2026-W18 | 88.21% | 10,934 | -0.90% |
| 2026-W17 | 89.01% | 12,985 | +0.23% |
| 2026-W16 | 88.81% | 12,359 | -0.89% |
| 2026-W15 | 89.61% | 10,862 | +0.69% |
| 2026-W14 | 89.0% | 11,548 | +1.49% |
| 2026-W13 | 87.69% | 10,894 | -1.21% |
| 2026-W12 | 88.76% | 14,790 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 89.29% | 88.21% | +1.23% | 11,545 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 90.0% | 94.59% | -4.86% | 290 | ⚠️ |
| Paypal | 89.85% | 90.23% | -0.42% | 926 |  |
| Apple Pay | 86.32% | 86.57% | -0.28% | 4,021 |  |
| Credit Card | 91.07% | 88.66% | +2.72% | 6,308 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Adyen | 96.1% | nan% | +nan% | 77 |  |
| Unknown | 78.07% | 92.93% | -15.99% | 114 | ⚠️ |
| Braintree | 86.92% | 87.22% | -0.34% | 5,062 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 97 |  |
| ProcessOut | 91.19% | 88.72% | +2.78% | 6,195 | ⚠️ |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.38% | 87.41% | +1.11% | 11,545 | 10,934 |  |
| 2_PreDunningAR | 89.29% | 88.21% | +1.23% | 11,545 | 10,934 |  |
| 3_PostDunningAR | 89.44% | 88.38% | +1.21% | 11,545 | 10,934 |  |
| 6_PaymentApprovalRate | 89.62% | 88.5% | +1.26% | 11,545 | 10,934 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 10,934 | 11,545 | +5.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-12*
