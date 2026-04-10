# Dunning Investigation: WL 2026-W12

**Metric:** Dunning Ship Rate  
**Period:** 2026-W11 → 2026-W12  
**Observation:** 33.11% → 32.20% (-0.91pp)  
**Volume:** 8,367 eligible orders  
**Payday Phase:** Post-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined from 33.11% to 32.20% (-0.91pp) week-over-week during the Post-Payday phase, with relatively stable volume (8,367 orders).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 91.16% → 91.06% | -0.10pp | ✅ |
| Discount % | 14.74% → 15.80% | +1.06pp | ✅ |
| PC2 | 51.42% → 47.31% | -4.11pp | ⚠️ |
| Ship Rate | 33.11% → 32.20% | -0.91pp | ⚠️ |

**Key Findings:**
- MR experienced a severe Ship Rate collapse from 13.20% to 0.80% (-12.40pp) while volume decreased by 12.7%, indicating a critical issue requiring immediate attention
- PC2 (Payment Conversion 2) dropped significantly by 4.11pp (51.42% → 47.31%), suggesting downstream payment issues are driving the overall decline
- KN showed declining performance with Ship Rate falling from 20.48% to 16.97% (-3.51pp) despite an 8.8% volume increase
- CK increased volume by 8.0% but Ship Rate slightly declined (-0.46pp), potentially contributing to mix shift effects
- Higher-performing countries (AO, CK) showed stable rates, suggesting the decline is concentrated in lower-tier markets

**Action:** Escalate — The MR market requires immediate investigation due to near-zero Ship Rate performance; additionally, investigate root cause of PC2 decline across the cluster.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Pre-Dunning AR | Discount % | PC2 |
|------|--------------|--------|-----------|----------------|------------|-----|
| 2026-W11 | Payday | 8,387 | 33.11% | 91.16% | 14.74% | 51.42% |
| 2026-W12 | Post-Payday | 8,367 | 32.20% | 91.06% | 15.8% | 47.31% |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,413 | 27.60% | 2,432 | 28.74% | 0.8% | Low |
| CK | 1,456 | 46.36% | 1,573 | 45.90% | 8.0% | Medium |
| MR | 1,288 | 13.20% | 1,124 | 0.80% | -12.7% | Low |
| AO | 1,287 | 63.09% | 1,264 | 63.45% | -1.8% | High |
| CG | 819 | 23.93% | 779 | 24.78% | -4.9% | Low |
| GN | 577 | 25.30% | 600 | 28.00% | 4.0% | Low |
| KN | 547 | 20.48% | 595 | 16.97% | 8.8% | Low |

---


---

*Report: 2026-04-10*
