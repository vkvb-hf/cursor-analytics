# Dunning Investigation: HF-NA 2026-W13

**Metric:** Dunning Ship Rate  
**Period:** 2026-W12 → 2026-W13  
**Observation:** 48.27% → 46.71% (-1.56pp)  
**Volume:** 17,743 eligible orders  
**Payday Phase:** Mid-Cycle

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined from 48.27% to 46.71% (-1.56pp) week-over-week as the cluster transitioned from Post-Payday to Mid-Cycle phase, with volume remaining relatively stable at 17,743 eligible orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.89% → 92.98% | +0.09pp | ✅ |
| Discount % | 16.03% → 16.67% | +0.64pp | ✅ |
| PC2 | 51.15% → 51.3% | +0.15pp | ✅ |
| Ship Rate | 48.27% → 46.71% | -1.56pp | ⚠️ |

**Key Findings:**
- US market experienced a significant Ship Rate decline from 47.68% to 45.08% (-2.60pp) while maintaining near-identical volume (13,814 vs 13,822 orders)
- CA market showed improvement with Ship Rate increasing from 50.30% to 52.46% (+2.16pp) despite a -2.5% volume reduction
- The overall decline is primarily driven by US performance, which represents ~78% of total volume
- Upstream metrics (Pre-Dunning AR, Discount %, PC2) all showed slight improvements, indicating the issue is isolated to the final conversion step
- Payday phase shift from Post-Payday to Mid-Cycle is a likely contributing factor to reduced customer payment capacity

**Action:** Investigate — The -2.60pp US Ship Rate decline warrants deeper analysis into US-specific factors (payment method mix, customer cohort behavior, messaging timing) given stable upstream metrics and the disproportionate impact on overall performance.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Pre-Dunning AR | Discount % | PC2 |
|------|--------------|--------|-----------|----------------|------------|-----|
| 2026-W12 | Post-Payday | 17,852 | 48.27% | 92.89% | 16.03% | 51.15% |
| 2026-W13 | Mid-Cycle | 17,743 | 46.71% | 92.98% | 16.67% | 51.3% |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 13,822 | 47.68% | 13,814 | 45.08% | -0.1% | Medium |
| CA | 4,030 | 50.30% | 3,929 | 52.46% | -2.5% | High |

---


---

*Report: 2026-04-10*
