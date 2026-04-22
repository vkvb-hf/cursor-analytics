# AR Overall Investigation: HF-NA 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 92.42% → 92.31% (-0.12%)  
**Volume:** 513,372 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate (Overall) for HF-NA declined marginally from 92.42% to 92.31% (-0.11pp) in 2026-W16, a change that is not statistically significant and remains within normal weekly fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | -0.23pp | ⚠️ |
| 2_PreDunningAR | Within normal range | -0.11pp | ✅ |
| 3_PostDunningAR | Within normal range | -0.19pp | ⚠️ |
| 6_PaymentApprovalRate | Stable | +0.03pp | ✅ |

**Key Findings:**
- No countries exceeded the ±2.5% threshold; US declined -0.13pp while CA improved +0.11pp
- Credit Card payment method showed the largest decline at -0.21pp, contributing most to the overall drop given its high volume (377,623 orders)
- Unknown PaymentProvider showed notable volatility (-1.63pp) but with minimal volume impact (668 orders)
- 8-week trend shows stable performance between 91.59% and 92.42%, with current week within historical range
- Mix shift analysis confirms stable volume distribution across both US and CA with no structural changes

**Action:** Monitor — The decline is not significant, falls within normal variance, and no dimensional breakdowns exceeded alert thresholds. Continue standard weekly monitoring.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 92.31% | 513,372 | -0.12% ← REPORTED CHANGE |
| 2026-W15 | 92.42% | 497,776 | +0.28% |
| 2026-W14 | 92.16% | 507,189 | -0.07% |
| 2026-W13 | 92.22% | 517,599 | +0.10% |
| 2026-W12 | 92.13% | 526,516 | -0.15% |
| 2026-W11 | 92.27% | 539,763 | +0.29% |
| 2026-W10 | 92.0% | 554,777 | +0.45% |
| 2026-W09 | 91.59% | 553,112 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.97% | 93.09% | -0.13% | 511,272 |  |
| CA | 93.58% | 93.48% | +0.11% | 104,640 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 92.74% | 92.93% | -0.21% | 377,623 |  |
| Others | 98.32% | 98.28% | +0.04% | 4,345 |  |
| Paypal | 95.71% | 95.59% | +0.13% | 62,665 |  |
| Apple Pay | 86.46% | 86.27% | +0.22% | 68,739 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 89.97% | 91.46% | -1.63% | 668 |  |
| Braintree | 92.72% | 92.82% | -0.11% | 383,334 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,642 |  |
| ProcessOut | 90.24% | 90.07% | +0.19% | 100,783 |  |
| Adyen | 93.25% | 93.06% | +0.21% | 24,945 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.06% | 91.29% | -0.26% | 513,372 | 497,776 |  |
| 2_PreDunningAR | 92.31% | 92.42% | -0.12% | 513,372 | 497,776 |  |
| 3_PostDunningAR | 93.32% | 93.51% | -0.20% | 513,372 | 497,776 |  |
| 6_PaymentApprovalRate | 94.13% | 94.1% | +0.03% | 513,372 | 497,776 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 492,812 | 511,272 | +3.7% | Stable |
| CA | High (>92%) | 103,253 | 104,640 | +1.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
