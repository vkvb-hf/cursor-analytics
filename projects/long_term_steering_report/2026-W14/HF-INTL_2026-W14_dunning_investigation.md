# Dunning Ship Rate Investigation: HF-INTL 2026-W14

**Metric:** Ship Rate (Good Customers)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 68.51% → 70.91% (+3.50pp)  
**Volume:** 36,718 orders

---

## Executive Summary

**Overall:** Ship Rate improved from 68.51% to 70.91% (+3.50pp) for HF-INTL cluster in 2026-W14, with volume increasing to 36,718 orders.

**Funnel Analysis:**

| Step | Check | Δ Value | Result |
| ---- | ----- | ------- | ------ |
| Pre-Dunning AR | 94.78% → 94.31% | -0.50pp | ⚠️ |
| Discount % | 13.73% → 13.32% | -2.99pp | ✅ |
| PC2 | 43.11% → 45.92% | +6.52pp | ✅ |

**Key Findings:**
- Ship Rate increased by +3.50pp despite a slight decline in Pre-Dunning Approval Rate (-0.50pp), suggesting other factors drove the improvement
- Discount % decreased by -2.99pp (from 13.73% to 13.32%), which has a negative relationship with Ship Rate—this reduction supports the observed Ship Rate improvement
- PC2 showed the strongest positive movement at +6.52pp (43.11% → 45.92%), likely the primary driver of the Ship Rate increase
- Both weeks remained in Mid-Cycle payday phase, eliminating payday timing as a confounding variable
- Order volume increased modestly from 35,560 to 36,718 orders

**Action:** Monitor — The Ship Rate improvement is driven by positive shifts in Discount % and PC2, with metrics moving in expected directions per the decision framework. No investigation required unless trend reverses.

---

---

## HF-INTL (Cluster)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 35,560 | 68.51% | - | 94.78% | - | 13.73% | - | 43.11% | - |
| 2026-W14 | Mid-Cycle | 36,718 | 70.91% | +3.50pp | 94.31% | -0.50pp | 13.32% | -2.99pp | 45.92% | +6.52pp |

---

## Decision Framework

| Metric | Relationship | If metric ↑ | If metric ↓ |
| ------ | ------------ | ----------- | ----------- |
| Pre-Dunning AR | Positive | Ship Rate ↑ | Ship Rate ↓ |
| Discount % | Negative | Ship Rate ↓ | Ship Rate ↑ |
| PC2 | Positive | Ship Rate ↑ | Ship Rate ↓ |

---

## Conclusion

The +3.50pp improvement in Ship Rate for HF-INTL in 2026-W14 is primarily attributed to a significant increase in PC2 (+6.52pp) and a reduction in Discount % (-2.99pp), both of which align with expected positive impacts on Ship Rate per the decision framework. The minor decline in Pre-Dunning AR (-0.50pp) did not materially offset these gains, and the consistent Mid-Cycle payday phase across both weeks confirms this is a genuine operational improvement rather than a timing artifact.

---

*Report: 2026-04-08*
