# Dunning Investigation: WL 2026-W13

**Metric:** Dunning Ship Rate  
**Period:** 2026-W12 → 2026-W13  
**Observation:** 32.20% → 29.38% (-2.82pp)  
**Volume:** 8,699 eligible orders  
**Payday Phase:** Mid-Cycle

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined from 32.20% to 29.38% (-2.82pp) week-over-week, driven primarily by significant underperformance in key countries and unfavorable mix shifts during the Mid-Cycle payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 91.06% → 91.18% | +0.12pp | ✅ |
| Discount % | 15.8% → 16.35% | +0.55pp | ✅ |
| PC2 | 47.31% → 47.51% | +0.20pp | ✅ |
| Ship Rate | 32.20% → 29.38% | -2.82pp | ⚠️ |

**Key Findings:**
- **ER underperformance:** Largest volume country (2,562 orders) saw Ship Rate drop from 28.74% to 23.61% (-5.13pp) while volume increased 5.3%
- **Unfavorable mix shift:** MR volume surged +30.4% (1,124 → 1,466 orders) but has near-zero Ship Rate (0.80% → 0.07%), diluting overall performance
- **High-performer contraction:** CK (Medium SR tier) volume decreased -8.5% while AO (High SR tier) decreased -2.8%, reducing contribution from better-converting countries
- **Payday phase impact:** Shift from Post-Payday to Mid-Cycle correlates with the decline, consistent with typical cash-flow constraints
- **GN positive signal:** One bright spot with Ship Rate improving from 28.00% to 36.06% (+8.06pp)

**Action:** **Investigate** — The -2.82pp decline is material and concentrated in specific countries (ER, MR). Recommend deep-dive into ER's -5.13pp drop and evaluate whether MR volume growth is sustainable given its near-zero conversion rate.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Pre-Dunning AR | Discount % | PC2 |
|------|--------------|--------|-----------|----------------|------------|-----|
| 2026-W12 | Post-Payday | 8,367 | 32.20% | 91.06% | 15.8% | 47.31% |
| 2026-W13 | Mid-Cycle | 8,699 | 29.38% | 91.18% | 16.35% | 47.51% |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,432 | 28.74% | 2,562 | 23.61% | 5.3% | Low |
| CK | 1,573 | 45.90% | 1,440 | 43.61% | -8.5% | Medium |
| AO | 1,264 | 63.45% | 1,228 | 67.26% | -2.8% | High |
| MR | 1,124 | 0.80% | 1,466 | 0.07% | 30.4% | Low |
| CG | 779 | 24.78% | 798 | 21.93% | 2.4% | Low |
| GN | 600 | 28.00% | 635 | 36.06% | 5.8% | Low |
| KN | 595 | 16.97% | 570 | 16.14% | -4.2% | Low |

---


---

*Report: 2026-04-10*
