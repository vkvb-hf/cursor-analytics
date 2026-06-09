# AR Overall Investigation: HF-NA 2026-W23

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 91.73% → 92.04% (+0.34%)  
**Volume:** 462,577 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate improved slightly from 91.73% to 92.04% (+0.31 pp), a non-significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within range | +0.47 pp | ✅ |
| 2_PreDunningAR | Within range | +0.34 pp | ✅ |
| 3_PostDunningAR | Within range | +0.12 pp | ✅ |
| 6_PaymentApprovalRate | Within range | +0.26 pp | ✅ |

**Key Findings:**
- All funnel stages showed modest improvement week-over-week, with FirstRunAR showing the largest gain (+0.47 pp)
- No countries exceeded the ±2.5% threshold; both US (+0.31 pp) and CA (+0.22 pp) showed stable, slight improvements
- Unknown PaymentProvider flagged with +14.45 pp change, but represents minimal volume (539 orders, <0.12% of total)
- 8-week trend shows metric recovering toward W16-W17 levels (~92.2-92.3%) after dipping to 91.73% in W22
- Volume mix remains stable with both US and CA showing slight volume increases (+1.9% and +1.5% respectively)

**Action:** Monitor — No significant deviations detected; continue standard weekly tracking.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 92.04% | 462,577 | +0.34% ← REPORTED CHANGE |
| 2026-W22 | 91.73% | 452,783 | -0.13% |
| 2026-W21 | 91.85% | 469,030 | -0.34% |
| 2026-W20 | 92.16% | 487,816 | +0.16% |
| 2026-W19 | 92.01% | 508,072 | -0.11% |
| 2026-W18 | 92.11% | 506,530 | -0.09% |
| 2026-W17 | 92.19% | 510,134 | -0.12% |
| 2026-W16 | 92.3% | 513,445 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 94.30% | 94.09% | +0.22% | 99,037 |  |
| US | 92.70% | 92.41% | +0.31% | 464,277 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 95.24% | 95.27% | -0.03% | 55,727 |  |
| Credit Card | 92.56% | 92.26% | +0.33% | 341,539 |  |
| Apple Pay | 86.0% | 85.43% | +0.67% | 61,003 |  |
| Others | 95.24% | 94.57% | +0.71% | 4,308 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 3,162 |  |
| ProcessOut | 89.29% | 89.19% | +0.12% | 96,646 |  |
| Adyen | 94.6% | 94.37% | +0.24% | 25,031 |  |
| Braintree | 92.61% | 92.24% | +0.40% | 337,199 |  |
| Unknown | 63.82% | 55.77% | +14.45% | 539 | ⚠️ |

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
