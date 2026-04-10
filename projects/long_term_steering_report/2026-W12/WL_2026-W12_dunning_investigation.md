# Dunning Investigation: WL 2026-W12

**Metric:** Dunning Ship Rate  
**Period:** 2026-W11 → 2026-W12  
**Observation:** 33.11% → 32.20% (-0.91pp)  
**Volume:** 8,367 eligible orders  
**Payday Phase:** Post-Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined by 0.91pp (33.11% → 32.20%) week-over-week during the Post-Payday phase, with stable volume of 8,367 eligible orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 91.16% → 91.06% | -0.10pp | ✅ |
| Discount % | 14.74% → 15.8% | +1.06pp | ✅ |
| PC2 | 51.42% → 47.31% | -4.11pp | ⚠️ |
| Ship Rate | 33.11% → 32.20% | -0.91pp | ⚠️ |

**Key Findings:**
- **MR Country Collapse:** MR experienced a catastrophic ship rate decline from 13.20% to 0.80% (-12.40pp), with volume also dropping 12.7% — this is the primary driver of the overall decline
- **PC2 Deterioration:** Post-checkout conversion (PC2) dropped significantly by 4.11pp (51.42% → 47.31%), indicating issues converting dunning attempts to shipments
- **Mix Shift Toward Lower-Performing Markets:** KN volume increased 8.8% while its ship rate declined from 20.48% to 16.97% (-3.51pp), amplifying negative impact
- **High-Performer Stability:** AO maintained strong performance at 63.45% ship rate with minimal volume change (-1.8%)
- **Discount Increase Ineffective:** Despite discount % increasing by 1.06pp, ship rate still declined, suggesting pricing is not the bottleneck

**Action:** **Escalate** — Immediate investigation required for MR country where ship rate collapsed to near-zero (0.80%), indicating potential operational or technical failure.

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
