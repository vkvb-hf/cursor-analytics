# PAR Investigation: HF-NA 2026-W23

**Metric:** Payment Approval Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 93.43% → 93.67% (+0.26%)  
**Volume:** 462,577 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate improved slightly from 93.43% to 93.67% (+0.24 pp) in HF-NA for 2026-W23, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.47 pp | ✅ |
| 2_PreDunningAR | Within normal range | +0.34 pp | ✅ |
| 3_PostDunningAR | Within normal range | +0.12 pp | ✅ |
| 6_PaymentApprovalRate | Within normal range | +0.26 pp | ✅ |

**Key Findings:**
- All funnel stages showed modest improvement, with FirstRunAR contributing the largest gain (+0.47 pp), indicating better initial payment success
- No countries exceeded the ±2.5% threshold; both US (+0.24 pp) and CA (+0.18 pp) showed stable, slight improvements
- Unknown payment provider showed a significant rate increase (+14.58 pp to 64.38%), though volume is minimal (539 orders)
- 8-week trend shows a gradual decline from 94.12% (W16) to 93.67% (W23), suggesting the current week's uptick partially reverses recent softening
- Volume mix remains stable with both US and CA maintaining high AR tiers (>92%)

**Action:** Monitor — The change is not significant and all dimensions are within normal operating ranges. Continue standard weekly tracking.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 93.67% | 462,577 | +0.26% ← REPORTED CHANGE |
| 2026-W22 | 93.43% | 452,783 | -0.22% |
| 2026-W21 | 93.64% | 469,030 | -0.23% |
| 2026-W20 | 93.86% | 487,816 | +0.20% |
| 2026-W19 | 93.67% | 508,072 | -0.27% |
| 2026-W18 | 93.92% | 506,530 | -0.10% |
| 2026-W17 | 94.01% | 510,134 | -0.12% |
| 2026-W16 | 94.12% | 513,445 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 96.07% | 95.89% | +0.18% | 99,037 |  |
| US | 94.17% | 93.94% | +0.24% | 464,277 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 95.93% | 96.01% | -0.09% | 55,727 |  |
| Credit Card | 94.23% | 93.98% | +0.27% | 341,539 |  |
| Apple Pay | 88.35% | 87.94% | +0.47% | 61,003 |  |
| Others | 95.31% | 94.64% | +0.71% | 4,308 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 3,162 |  |
| ProcessOut | 91.31% | 91.26% | +0.05% | 96,646 |  |
| Adyen | 96.74% | 96.46% | +0.29% | 25,031 |  |
| Braintree | 94.11% | 93.81% | +0.31% | 337,199 |  |
| Unknown | 64.38% | 56.18% | +14.58% | 539 | ⚠️ |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.88% | 90.46% | +0.47% | 462,577 | 452,783 |  |
| 2_PreDunningAR | 92.04% | 91.73% | +0.34% | 462,577 | 452,783 |  |
| 3_PostDunningAR | 92.91% | 92.81% | +0.12% | 462,577 | 452,783 |  |
| 6_PaymentApprovalRate | 93.67% | 93.43% | +0.26% | 462,577 | 452,783 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 455,576 | 464,277 | +1.9% | Stable |
| CA | High (>92%) | 97,531 | 99,037 | +1.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-09*
