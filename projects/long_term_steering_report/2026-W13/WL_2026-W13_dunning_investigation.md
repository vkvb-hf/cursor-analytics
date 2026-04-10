# Dunning Investigation: WL 2026-W13

**Metric:** Dunning Ship Rate  
**Period:** 2026-W12 → 2026-W13  
**Observation:** 32.20% → 29.38% (-2.82pp)  
**Volume:** 8,699 eligible orders  
**Payday Phase:** Mid-Cycle

## Executive Summary

**Overall:** Dunning Ship Rate declined from 32.20% to 29.38% (-2.82pp) in W13, with volume increasing modestly from 8,367 to 8,699 eligible orders during a Mid-Cycle payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 91.06% → 91.18% | +0.12pp | ✅ |
| Discount % | 15.8% → 16.35% | +0.55pp | ✅ |
| PC2 | 47.31% → 47.51% | +0.20pp | ✅ |
| Ship Rate | 32.20% → 29.38% | -2.82pp | ⚠️ |

**Key Findings:**
- ER saw a significant Ship Rate decline (-5.13pp, from 28.74% to 23.61%) while volume grew +5.3%, amplifying negative impact on overall performance
- MR volume surged +30.4% (1,124 → 1,466 orders) while Ship Rate collapsed to near-zero (0.80% → 0.07%), indicating potential mix shift drag
- CK, a Medium-tier performer, lost -8.5% volume share while maintaining relatively stable SR (-2.29pp), reducing positive contribution to the cluster
- AO showed positive momentum with SR improving +3.81pp (63.45% → 67.26%) despite slight volume decline
- Mid-Cycle payday phase timing may be contributing to lower conversion compared to Post-Payday in W12

**Action:** Investigate – Focus on root cause analysis for ER's sharp SR decline and MR's near-zero conversion despite major volume increase; assess if MR orders should be excluded or require different dunning treatment.

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
