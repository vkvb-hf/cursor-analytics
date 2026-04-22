# Dunning Investigation: US-HF 2026-W16

**Metric:** Dunning Ship Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 46.72% → 47.61% (+0.89pp)  
**Volume:** 14,086 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate improved by +0.89pp (46.72% → 47.61%) in US-HF during 2026-W16, coinciding with the transition from Pre-Payday to Payday phase and a volume increase of 11.6% (12,619 → 14,086 eligible orders).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.09% → 92.97% | -0.1% | ✅ Stable |
| Discount % | 13.95% → 14.87% | +6.6% | ⚠️ Increased |
| PC2 | 52.07% → 52.23% | +0.3% | ✅ Stable |
| Ship Rate | 46.72% → 47.61% | +1.9% | ✅ Improved |

**Key Findings:**
- Ship Rate improvement of +0.89pp is primarily driven by the Payday phase timing, which typically correlates with increased customer liquidity and payment completion
- Discount % increased significantly by +6.6% (13.95% → 14.87%), which typically has a negative relationship with Ship Rate, yet Ship Rate still improved—suggesting Payday effect outweighed discount pressure
- Pre-Dunning AR remained stable (-0.1%), indicating upstream acceptance quality was consistent
- PC2 remained essentially flat (+0.3%), showing no meaningful shift in payment collection at step 2
- Volume increased by 11.6% with no signs of Simpson's Paradox affecting the rate improvement

**Action:** Monitor — The improvement aligns with expected Payday phase behavior. Continue tracking to confirm the discount increase does not erode gains in subsequent weeks.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 12,619 | 46.72% | - | 93.09% | - | 13.95% | - | 52.07% | - |
| 2026-W16 | Payday | 14,086 | 47.61% | →+1.9% | 92.97% | →-0.1% | 14.87% | ↑+6.6% | 52.23% | →+0.3% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 12,619 | 46.72% | - | 93.09% | - | 13.95% | - | 52.07% | - |
| 2026-W16 | Payday | 14,086 | 47.61% | →+1.9% | 92.97% | →-0.1% | 14.87% | ↑+6.6% | 52.23% | →+0.3% |

**Analysis:** The +0.89pp improvement in Dunning Ship Rate for US-HF is consistent with the natural Payday cycle effect, as customer payment capacity typically increases during this phase. While the +6.6% increase in Discount % warrants monitoring (given its normally negative relationship with Ship Rate), the Payday timing appears to have been the dominant driver of improved performance this week.


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
| US | →+1.9% | →-0.1% | ↑+6.6% | →+0.3% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 12,619 | 46.72% | 14,086 | 47.61% | 11.6% | Medium |

---


---

*Report: 2026-04-22*
