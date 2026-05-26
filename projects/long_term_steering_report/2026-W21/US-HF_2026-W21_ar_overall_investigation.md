# AR Overall Investigation: US-HF 2026-W21

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 91.89% → 91.58% (-0.34%)  
**Volume:** 386,911 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined by -0.31 pp (91.89% → 91.58%) on 386,911 orders in 2026-W21, a change that is **not statistically significant**.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | First attempt acceptance | -0.29 pp | ✅ |
| 2_PreDunningAR | Pre-dunning recovery | -0.31 pp | ✅ |
| 3_PostDunningAR | Post-dunning recovery | -0.41 pp | ✅ |
| 6_PaymentApprovalRate | Final approval | -0.27 pp | ✅ |

**Key Findings:**
- **No significant driver identified:** US showed only -0.23 pp decline, well within normal variance and below the ±2.5% threshold
- **Gradual downward trend:** Rate has declined from 92.22% (W15) to 91.58% (W21), representing a cumulative -0.64 pp erosion over 6 weeks
- **Payment method "Others" showed largest decline:** -1.60 pp (93.74% → 92.24%), but volume is minimal at 2,204 orders
- **Unknown PaymentProvider flagged:** +4.93 pp change but on only 335 orders (negligible impact)
- **Volume declining:** Order volume dropped from 401,763 to 386,911 (-3.7% WoW), consistent with mix shift showing US High-tier volume down -3.1%

**Action:** **Monitor** – The weekly change is not significant and no dimensions exceed investigation thresholds. However, the gradual 6-week downward trend warrants continued observation to determine if this becomes a sustained pattern.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 91.58% | 386,911 | -0.34% ← REPORTED CHANGE |
| 2026-W20 | 91.89% | 401,763 | +0.12% |
| 2026-W19 | 91.78% | 416,723 | -0.13% |
| 2026-W18 | 91.9% | 414,920 | -0.18% |
| 2026-W17 | 92.07% | 419,106 | -0.02% |
| 2026-W16 | 92.09% | 421,948 | -0.14% |
| 2026-W15 | 92.22% | 408,631 | +0.33% |
| 2026-W14 | 91.92% | 415,886 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.71% | 92.92% | -0.23% | 478,645 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 92.24% | 93.74% | -1.60% | 2,204 |  |
| Apple Pay | 84.51% | 85.29% | -0.91% | 52,341 |  |
| Credit Card | 92.2% | 92.43% | -0.25% | 285,517 |  |
| Paypal | 95.69% | 95.87% | -0.19% | 46,849 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Adyen | 93.01% | 94.35% | -1.41% | 458 |  |
| ProcessOut | 87.05% | 87.51% | -0.52% | 58,388 |  |
| Braintree | 92.38% | 92.64% | -0.28% | 325,970 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1,760 |  |
| Unknown | 50.75% | 48.36% | +4.93% | 335 | ⚠️ |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.37% | 90.66% | -0.31% | 386,911 | 401,763 |  |
| 2_PreDunningAR | 91.58% | 91.89% | -0.34% | 386,911 | 401,763 |  |
| 3_PostDunningAR | 92.46% | 92.87% | -0.45% | 386,911 | 401,763 |  |
| 6_PaymentApprovalRate | 93.23% | 93.5% | -0.28% | 386,911 | 401,763 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 493,780 | 478,645 | -3.1% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-26*
