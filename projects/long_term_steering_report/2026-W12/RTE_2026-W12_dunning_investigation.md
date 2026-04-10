# Dunning Investigation: RTE 2026-W12

**Metric:** Dunning Ship Rate  
**Period:** 2026-W11 → 2026-W12  
**Observation:** 40.58% → 43.89% (+3.31pp)  
**Volume:** 20,396 eligible orders  
**Payday Phase:** Post-Payday

## Executive Summary

**Overall:** Dunning Ship Rate improved from 40.58% to 43.89% (+3.31pp) in 2026-W12, with total eligible volume relatively stable at 20,396 orders during the Post-Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.77% → 93.65% | -0.12pp | ✅ |
| Discount % | 18.26% → 17.95% | -0.31pp | ✅ |
| PC2 | 47.66% → 43.41% | -4.25pp | ⚠️ |
| Ship Rate | 40.58% → 43.89% | +3.31pp | ✅ |

**Key Findings:**
- FJ (largest market at 68% of volume) showed strong improvement with Ship Rate increasing from 38.44% to 42.72% (+4.28pp)
- TZ demonstrated the most dramatic improvement, jumping from 3.87% to 22.15% (+18.28pp) despite volume declining 12.7%
- YE maintained the highest Ship Rate tier at 61.69% (+1.30pp) while experiencing a 4.5% volume decrease
- PC2 declined by 4.25pp (47.66% → 43.41%) despite overall Ship Rate improvement, suggesting efficiency gains in later funnel stages
- TO was the only country showing Ship Rate decline, dropping from 24.84% to 19.66% (-5.18pp)

**Action:** Monitor - The improvement appears driven by genuine performance gains across major markets (FJ, TZ) rather than mix shift effects. Continue tracking TO for potential intervention.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Pre-Dunning AR | Discount % | PC2 |
|------|--------------|--------|-----------|----------------|------------|-----|
| 2026-W11 | Payday | 20,679 | 40.58% | 93.77% | 18.26% | 47.66% |
| 2026-W12 | Post-Payday | 20,396 | 43.89% | 93.65% | 17.95% | 43.41% |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| FJ | 14,089 | 38.44% | 13,953 | 42.72% | -1.0% | Medium |
| YE | 3,635 | 60.39% | 3,472 | 61.69% | -4.5% | High |
| CF | 2,147 | 30.32% | 2,180 | 31.83% | 1.5% | Medium |
| TO | 322 | 24.84% | 295 | 19.66% | -8.4% | Low |
| TZ | 181 | 3.87% | 158 | 22.15% | -12.7% | Low |
| TK | 117 | 6.84% | 120 | 8.33% | 2.6% | Low |
| TV | 100 | 7.00% | 109 | 13.76% | 9.0% | Low |
| TT | 88 | 31.82% | 109 | 33.03% | 23.9% | Medium |

---


---

*Report: 2026-04-10*
