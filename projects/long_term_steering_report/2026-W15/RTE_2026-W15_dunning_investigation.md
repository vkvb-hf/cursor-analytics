# Dunning Investigation: RTE 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 44.24% → 42.59% (-1.65pp)  
**Volume:** 19,573 eligible orders  
**Payday Phase:** Pre-Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined by 1.65pp (44.24% → 42.59%) during the Pre-Payday phase, with total volume decreasing by 2,091 orders (9.7% reduction).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.05% → 93.42% | +0.37pp | ✅ |
| Discount % | 17.8% → 17.48% | -0.32pp | ✅ |
| PC2 | 43.35% → 49.37% | +6.02pp | ✅ |
| Ship Rate | 44.24% → 42.59% | -1.65pp | ⚠️ |

**Key Findings:**
- FJ, the highest-volume country (70% of orders), saw ship rate decline 2.37pp (43.53% → 41.16%) while volume dropped 9.4%
- TV experienced a severe ship rate collapse of 18.27pp (30.77% → 12.50%) despite slight volume increase (+5.5%)
- TO showed significant degradation with ship rate falling 7.79pp (31.67% → 23.88%) alongside 21.4% volume decline
- YE maintained strong performance as the highest SR tier (58.80%) with minimal decline (-0.85pp)
- PC2 improved substantially (+6.02pp) indicating better payment capture, yet overall ship rate still declined

**Action:** Investigate — The disconnect between improved PC2/Pre-Dunning AR metrics and declining ship rate, combined with severe drops in TV and TO, warrants deeper investigation into country-specific fulfillment or operational issues.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Pre-Dunning AR | Discount % | PC2 |
|------|--------------|--------|-----------|----------------|------------|-----|
| 2026-W14 | Mid-Cycle | 21,664 | 44.24% | 93.05% | 17.8% | 43.35% |
| 2026-W15 | Pre-Payday | 19,573 | 42.59% | 93.42% | 17.48% | 49.37% |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| FJ | 15,138 | 43.53% | 13,721 | 41.16% | -9.4% | Medium |
| YE | 3,487 | 59.65% | 3,325 | 58.80% | -4.6% | High |
| CF | 2,195 | 30.34% | 1,888 | 30.24% | -14.0% | Medium |
| TO | 341 | 31.67% | 268 | 23.88% | -21.4% | Medium |
| TZ | 194 | 26.80% | 130 | 26.15% | -33.0% | Low |
| TK | 146 | 24.66% | 50 | 32.00% | -65.8% | Low |
| TV | 91 | 30.77% | 96 | 12.50% | 5.5% | Medium |
| TT | 72 | 33.33% | 95 | 40.00% | 31.9% | Medium |

---


---

*Report: 2026-04-15*
