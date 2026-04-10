# Dunning Investigation: WL 2026-W14

**Metric:** Dunning Ship Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 29.38% → 28.34% (-1.04pp)  
**Volume:** 8,051 eligible orders  
**Payday Phase:** Mid-Cycle

## Executive Summary

**Overall:** Dunning Ship Rate declined by 1.04pp (29.38% → 28.34%) week-over-week during Mid-Cycle payday phase, with volume decreasing by 648 orders (8,699 → 8,051).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 91.18% → 90.71% | -0.47pp | ⚠️ |
| Discount % | 16.35% → 15.46% | -0.89pp | ⚠️ |
| PC2 | 47.51% → 47.03% | -0.48pp | ⚠️ |
| Ship Rate | 29.38% → 28.34% | -1.04pp | ⚠️ |

**Key Findings:**
- **Simpson's Paradox Detected:** Despite the overall decline, 6 of 7 countries showed improved Ship Rates individually; the decline is driven by mix shift away from high-performing AO (volume dropped 59.6%, from 1,228 to 496 orders)
- **AO volume collapse:** AO, the highest-performing country (72.58% SR), saw dramatic volume reduction, significantly impacting the weighted average
- **Low-tier country KN grew:** KN volume increased 17.4% while maintaining a low Ship Rate (15.10%), further diluting overall performance
- **All funnel metrics declined marginally:** Pre-Dunning AR (-0.47pp), Discount % (-0.89pp), and PC2 (-0.48pp) all showed slight deterioration
- **CK improvement:** CK showed both volume growth (+3.8%) and SR improvement (43.61% → 47.76%), a positive signal

**Action:** Investigate — The Simpson's Paradox finding requires investigation into why AO volume dropped so significantly; this mix shift is masking underlying country-level improvements.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Pre-Dunning AR | Discount % | PC2 |
|------|--------------|--------|-----------|----------------|------------|-----|
| 2026-W13 | Mid-Cycle | 8,699 | 29.38% | 91.18% | 16.35% | 47.51% |
| 2026-W14 | Mid-Cycle | 8,051 | 28.34% | 90.71% | 15.46% | 47.03% |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,562 | 23.61% | 2,559 | 26.57% | -0.1% | Low |
| MR | 1,466 | 0.07% | 1,421 | 0.00% | -3.1% | Low |
| CK | 1,440 | 43.61% | 1,495 | 47.76% | 3.8% | Medium |
| AO | 1,228 | 67.26% | 496 | 72.58% | -59.6% | High |
| CG | 798 | 21.93% | 779 | 24.78% | -2.4% | Low |
| GN | 635 | 36.06% | 632 | 37.03% | -0.5% | Medium |
| KN | 570 | 16.14% | 669 | 15.10% | 17.4% | Low |

---


---

*Report: 2026-04-10*
