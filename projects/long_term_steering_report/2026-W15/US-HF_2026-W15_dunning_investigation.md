# Dunning Investigation: US-HF 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 47.76% → 46.74% (-1.02pp)  
**Volume:** 12,639 eligible orders  
**Payday Phase:** Pre-Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined by 1.02pp (47.76% → 46.74%) in US-HF during W15, coinciding with a Pre-Payday phase and an 8.4% decrease in eligible order volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.78% → 93.09% | +0.31pp | ✅ |
| Discount % | 14.6% → 13.93% | -0.67pp | ⚠️ |
| PC2 | 49.34% → 52.09% | +2.75pp | ✅ |
| Ship Rate | 47.76% → 46.74% | -1.02pp | ⚠️ |

**Key Findings:**
- Ship Rate declined 1.02pp despite Pre-Dunning AR improving by 0.31pp (93.09%)
- Discount percentage decreased by 0.67pp (14.6% → 13.93%), potentially reducing conversion incentives
- PC2 (payment conversion) improved significantly by 2.75pp (52.09%), yet this did not translate to higher ship rates
- Order volume dropped 8.4% (13,795 → 12,639), shifting from Mid-Cycle to Pre-Payday phase
- The disconnect between improved PC2 and declining Ship Rate suggests post-payment fulfillment or inventory issues

**Action:** Investigate — The divergence between improving upstream metrics (Pre-Dunning AR, PC2) and declining Ship Rate warrants deeper analysis into post-payment fulfillment processes and the impact of reduced discount incentives.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Pre-Dunning AR | Discount % | PC2 |
|------|--------------|--------|-----------|----------------|------------|-----|
| 2026-W14 | Mid-Cycle | 13,795 | 47.76% | 92.78% | 14.6% | 49.34% |
| 2026-W15 | Pre-Payday | 12,639 | 46.74% | 93.09% | 13.93% | 52.09% |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 13,795 | 47.76% | 12,639 | 46.74% | -8.4% | Medium |

---


---

*Report: 2026-04-15*
