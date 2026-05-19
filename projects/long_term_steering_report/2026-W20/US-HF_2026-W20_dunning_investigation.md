# Dunning Investigation: US-HF 2026-W20

**Metric:** Dunning Ship Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 46.38% → 47.14% (+0.76pp)  
**Volume:** 13,078 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

**Overall:** Dunning Ship Rate improved by +0.76pp (46.38% → 47.14%) during the transition from Pre-Payday to Payday phase in 2026-W20, with stable volume of 13,078 eligible orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.86% → 92.93% | +0.1% | ✅ |
| Discount % | 13.4% → 14.69% | +9.6% | ⚠️ |
| PC2 | 54.51% → 50.53% | -7.3% | ⚠️ |
| Ship Rate | 46.38% → 47.14% | +1.6% | ✅ |

**Key Findings:**
- Ship Rate improvement of +0.76pp coincides with the transition from Pre-Payday to Payday phase, suggesting improved customer payment capacity
- Discount % increased significantly by +9.6% (13.4% → 14.69%), which typically correlates negatively with Ship Rate, yet Ship Rate still improved
- PC2 declined by -7.3% (54.51% → 50.53%), indicating potential downstream conversion concerns despite overall Ship Rate gains
- Pre-Dunning AR remained stable at ~93%, providing a consistent upstream funnel foundation
- Volume remained essentially flat (-0.2%), ruling out mix shift as a contributing factor to the Ship Rate change

**Action:** Monitor - The Ship Rate improvement aligns with expected Payday phase behavior. However, the elevated Discount % (+9.6%) warrants monitoring to ensure profitability is not being traded for conversion. Continue tracking PC2 decline trend in subsequent weeks.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W19 | Pre-Payday | 13,103 | 46.38% | - | 92.86% | - | 13.4% | - | 54.51% | - |
| 2026-W20 | Payday | 13,078 | 47.14% | →+1.6% | 92.93% | →+0.1% | 14.69% | ↑+9.6% | 50.53% | ↓-7.3% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W19 | Pre-Payday | 13,103 | 46.38% | - | 92.86% | - | 13.4% | - | 54.51% | - |
| 2026-W20 | Payday | 13,078 | 47.14% | →+1.6% | 92.93% | →+0.1% | 14.69% | ↑+9.6% | 50.53% | ↓-7.3% |

**Analysis:** The +0.76pp improvement in US-HF Dunning Ship Rate is primarily attributable to the favorable Payday phase timing, which typically increases customer payment success rates. While the improvement is positive, the concurrent +9.6% increase in Discount % and -7.3% decline in PC2 suggest that aggressive discounting may be masking underlying conversion challenges that could impact downstream performance. Continued monitoring of these counterbalancing metrics is recommended through the post-Payday phase.


---

## Decision Framework

**How Ship Rate relates to other metrics:**

| Metric | Relationship | If metric ↑ | If metric ↓ |
|--------|--------------|-------------|-------------|
| Pre-Dunning AR | Positive | Ship Rate ↑ | Ship Rate ↓ |
| Discount % | Negative | Ship Rate ↓ | Ship Rate ↑ |
| PC2 | Positive | Ship Rate ↑ | Ship Rate ↓ |

**Root Cause Derivation:**

| Country | Ship Rate | Pre-Dunning AR | Discount % | PC2 | Payday Phase | Root Cause |
|---------|-----------|----------------|------------|-----|--------------|------------|
| US | →+1.6% | →+0.1% | ↑+9.6% | ↓-7.3% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 13,103 | 46.38% | 13,078 | 47.14% | -0.2% | Medium |

---


---

*Report: 2026-05-19*
