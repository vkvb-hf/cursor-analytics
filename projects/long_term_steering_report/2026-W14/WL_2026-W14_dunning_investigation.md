# Dunning Investigation: WL 2026-W14

**Metric:** Dunning Ship Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 29.39% → 28.35% (-1.04pp)  
**Volume:** 8,053 eligible orders  
**Payday Phase:** Mid-Cycle

## Executive Summary

**Overall:** Dunning Ship Rate declined by 1.04pp (29.39% → 28.35%) week-over-week during a Mid-Cycle payday phase, with eligible volume decreasing from 8,700 to 8,053 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 91.18% → 90.71% | -0.47pp | ⚠️ |
| Discount % | 16.35% → 15.46% | -0.89pp | ⚠️ |
| PC2 | 47.52% → 47.03% | -0.49pp | ⚠️ |
| Ship Rate | 29.39% → 28.35% | -1.04pp | ⚠️ |

**Key Findings:**
- **Simpson's Paradox detected:** AO (highest SR tier at 72.58%) experienced a -59.6% volume drop (1,228 → 496 orders), disproportionately removing high-converting orders from the mix
- **Individual country performance improved:** 6 of 7 countries showed SR increases (ER +2.93pp, CK +4.15pp, AO +5.32pp, CG +2.85pp, GN +0.97pp), yet cluster-level SR declined
- **Low-tier volume expansion:** KN (15.10% SR) increased volume by 17.4%, adding more low-converting orders to the mix
- **Discount reduction:** Discount % dropped by 0.89pp, potentially reducing conversion incentives across the funnel
- **MR remains near-zero:** MR maintained 0.00% ship rate on 1,421 orders, representing significant untapped potential

**Action:** Monitor — The decline is primarily driven by mix shift (Simpson's Paradox) rather than true performance degradation. Investigate the root cause of AO's 59.6% volume drop to determine if this is a temporary anomaly or systemic issue requiring intervention.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Pre-Dunning AR | Discount % | PC2 |
|------|--------------|--------|-----------|----------------|------------|-----|
| 2026-W13 | Mid-Cycle | 8,700 | 29.39% | 91.18% | 16.35% | 47.52% |
| 2026-W14 | Mid-Cycle | 8,053 | 28.35% | 90.71% | 15.46% | 47.03% |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,563 | 23.64% | 2,559 | 26.57% | -0.2% | Low |
| MR | 1,466 | 0.07% | 1,421 | 0.00% | -3.1% | Low |
| CK | 1,440 | 43.61% | 1,497 | 47.76% | 4.0% | Medium |
| AO | 1,228 | 67.26% | 496 | 72.58% | -59.6% | High |
| CG | 798 | 21.93% | 779 | 24.78% | -2.4% | Low |
| GN | 635 | 36.06% | 632 | 37.03% | -0.5% | Medium |
| KN | 570 | 16.14% | 669 | 15.10% | 17.4% | Low |

---


---

*Report: 2026-04-09*
