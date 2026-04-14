# Dunning Investigation: RTE 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 44.24% → 42.67% (-1.57pp)  
**Volume:** 19,602 eligible orders  
**Payday Phase:** Pre-Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined by 1.57pp (44.24% → 42.67%) week-over-week during the Pre-Payday phase, with total volume decreasing by 9.5% (21,668 → 19,602 orders).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.05% → 93.42% | +0.37pp | ✅ |
| Discount % | 17.8% → 17.48% | -0.32pp | ✅ |
| PC2 | 43.35% → 49.36% | +6.01pp | ✅ |
| Ship Rate | 44.24% → 42.67% | -1.57pp | ⚠️ |

**Key Findings:**
- FJ, the largest market (70% of volume), saw Ship Rate decline by 2.29pp (43.53% → 41.24%) while losing 9.3% of volume
- TV experienced a severe Ship Rate collapse of 18.27pp (30.77% → 12.50%) despite a 5.5% volume increase
- TO showed significant deterioration with Ship Rate dropping 7.23pp (31.67% → 24.44%) alongside a 20.8% volume decline
- YE, the highest-performing country, remained relatively stable with only a 0.85pp decline (59.65% → 58.80%)
- PC2 improved substantially (+6.01pp) yet Ship Rate still declined, suggesting conversion issues downstream in the funnel

**Action:** Investigate — Focus on FJ performance decline given its outsized impact on overall metrics, and conduct root cause analysis on TV's dramatic Ship Rate collapse despite stable volume.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Pre-Dunning AR | Discount % | PC2 |
|------|--------------|--------|-----------|----------------|------------|-----|
| 2026-W14 | Mid-Cycle | 21,668 | 44.24% | 93.05% | 17.8% | 43.35% |
| 2026-W15 | Pre-Payday | 19,602 | 42.67% | 93.42% | 17.48% | 49.36% |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| FJ | 15,141 | 43.53% | 13,740 | 41.24% | -9.3% | Medium |
| YE | 3,487 | 59.65% | 3,328 | 58.80% | -4.6% | High |
| CF | 2,196 | 30.33% | 1,891 | 30.30% | -13.9% | Medium |
| TO | 341 | 31.67% | 270 | 24.44% | -20.8% | Medium |
| TZ | 194 | 26.80% | 132 | 27.27% | -32.0% | Low |
| TK | 146 | 24.66% | 50 | 32.00% | -65.8% | Low |
| TV | 91 | 30.77% | 96 | 12.50% | 5.5% | Medium |
| TT | 72 | 33.33% | 95 | 40.00% | 31.9% | Medium |

---


---

*Report: 2026-04-14*
