# AR Overall Investigation: HF-NA 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 92.42% → 92.31% (-0.12%)  
**Volume:** 513,372 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined marginally from 92.42% to 92.31% (-0.11pp) in W16, a statistically insignificant change within normal weekly variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.26pp | ⚠️ |
| 2_PreDunningAR | Reported Metric | -0.12pp | ✅ |
| 3_PostDunningAR | Post-Recovery | -0.20pp | ⚠️ |
| 6_PaymentApprovalRate | Final Approval | +0.04pp | ✅ |

**Key Findings:**
- The -0.12pp decline is not statistically significant and falls within the 8-week variance range (91.59% to 92.42%)
- US showed a minor decline (-0.13pp to 92.97%) while CA improved slightly (+0.09pp to 93.58%); no countries exceeded the ±2.5% threshold
- Credit Card payments experienced the largest method decline (-0.21pp) but remain the dominant volume driver at 377,622 orders
- Unknown payment provider showed notable decline (-1.78pp) but represents minimal volume (669 orders)
- Mix shift analysis shows stable composition with both US (+3.7%) and CA (+1.3%) maintaining High AR tier status

**Action:** Monitor — No action required. The change is within normal operating variance and no dimensions exceeded investigation thresholds.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 92.31% | 513,372 | -0.12% ← REPORTED CHANGE |
| 2026-W15 | 92.42% | 497,775 | +0.28% |
| 2026-W14 | 92.16% | 507,189 | -0.07% |
| 2026-W13 | 92.22% | 517,599 | +0.10% |
| 2026-W12 | 92.13% | 526,516 | -0.16% |
| 2026-W11 | 92.28% | 539,763 | +0.30% |
| 2026-W10 | 92.0% | 554,777 | +0.45% |
| 2026-W09 | 91.59% | 553,112 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.97% | 93.09% | -0.13% | 511,272 |  |
| CA | 93.58% | 93.49% | +0.09% | 104,640 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 92.74% | 92.93% | -0.21% | 377,622 |  |
| Others | 98.3% | 98.28% | +0.02% | 4,346 |  |
| Paypal | 95.71% | 95.59% | +0.13% | 62,665 |  |
| Apple Pay | 86.46% | 86.28% | +0.22% | 68,739 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 89.84% | 91.46% | -1.78% | 669 |  |
| Braintree | 92.72% | 92.82% | -0.10% | 383,333 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,642 |  |
| Adyen | 93.26% | 93.12% | +0.15% | 24,945 |  |
| ProcessOut | 90.24% | 90.07% | +0.19% | 100,783 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.06% | 91.29% | -0.26% | 513,372 | 497,775 |  |
| 2_PreDunningAR | 92.31% | 92.42% | -0.12% | 513,372 | 497,775 |  |
| 3_PostDunningAR | 93.31% | 93.5% | -0.20% | 513,372 | 497,775 |  |
| 6_PaymentApprovalRate | 94.13% | 94.1% | +0.04% | 513,372 | 497,775 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 492,811 | 511,272 | +3.7% | Stable |
| CA | High (>92%) | 103,253 | 104,640 | +1.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
