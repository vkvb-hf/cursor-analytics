# Dunning Investigation: US-HF 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 47.75% → 46.83% (-0.92pp)  
**Volume:** 12,662 eligible orders  
**Payday Phase:** Pre-Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined by 0.92pp (47.75% → 46.83%) in US-HF during Pre-Payday phase, with volume down 8.2% (13,796 → 12,662 eligible orders).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.78% → 93.10% | +0.32pp | ✅ |
| Discount % | 14.59% → 13.91% | -0.68pp | ⚠️ |
| PC2 | 49.34% → 52.11% | +2.77pp | ✅ |
| Ship Rate | 47.75% → 46.83% | -0.92pp | ⚠️ |

**Key Findings:**
- Ship Rate declined 0.92pp despite improved Pre-Dunning AR (+0.32pp) and PC2 (+2.77pp), suggesting conversion issues downstream in the funnel
- Discount rate decreased by 0.68pp (14.59% → 13.91%), which may have contributed to lower ship rate as fewer customers received discount incentives
- Volume dropped 8.2% week-over-week, indicating reduced eligible order flow into the dunning process
- Pre-Payday phase typically shows stronger payment behavior, yet ship rate still declined, which is counter to expected seasonal patterns
- US is the sole market in this cluster and shows Medium SR tier performance

**Action:** Investigate — The disconnect between improving upstream metrics (Pre-Dunning AR, PC2) and declining Ship Rate warrants deeper analysis into the discount strategy reduction and its impact on final conversion.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Pre-Dunning AR | Discount % | PC2 |
|------|--------------|--------|-----------|----------------|------------|-----|
| 2026-W14 | Mid-Cycle | 13,796 | 47.75% | 92.78% | 14.59% | 49.34% |
| 2026-W15 | Pre-Payday | 12,662 | 46.83% | 93.10% | 13.91% | 52.11% |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 13,796 | 47.75% | 12,662 | 46.83% | -8.2% | Medium |

---


---

*Report: 2026-04-14*
