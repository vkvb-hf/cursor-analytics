# Dunning Investigation: HF-NA 2026-W13

**Metric:** Dunning Ship Rate  
**Period:** 2026-W12 → 2026-W13  
**Observation:** 48.27% → 46.71% (-1.56pp)  
**Volume:** 17,743 eligible orders  
**Payday Phase:** Mid-Cycle

## Executive Summary

**Overall:** Dunning Ship Rate declined by -1.56pp (48.27% → 46.71%) during the Mid-Cycle payday phase, with relatively stable volume of 17,743 eligible orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.89% → 92.98% | +0.09pp | ✅ |
| Discount % | 16.03% → 16.67% | +0.64pp | ✅ |
| PC2 | 51.15% → 51.30% | +0.15pp | ✅ |
| Ship Rate | 48.27% → 46.71% | -1.56pp | ⚠️ |

**Key Findings:**
- US drove the decline with Ship Rate dropping -2.60pp (47.68% → 45.08%) while maintaining 78% of total volume
- CA showed positive performance with Ship Rate improving +2.16pp (50.30% → 52.46%), partially offsetting US decline
- Upstream funnel metrics (Pre-Dunning AR, Discount %, PC2) all showed slight improvements, indicating the issue is isolated to final conversion
- Mid-Cycle payday phase typically shows softer performance compared to Post-Payday, which may partially explain the decline
- Volume remained stable (-0.6% WoW), ruling out significant mix shift as the primary driver

**Action:** Investigate – The decline is concentrated in US despite stable upstream metrics. Recommend deeper analysis into US-specific dunning messaging effectiveness and payment method availability during Mid-Cycle.

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
