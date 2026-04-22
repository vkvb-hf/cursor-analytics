# Dunning Investigation: US-HF 2026-W16

**Metric:** Dunning Ship Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 46.72% → 47.61% (+0.89pp)  
**Volume:** 14,086 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

**Overall:** Dunning Ship Rate improved by +0.89pp (46.72% → 47.61%) week-over-week during the transition from Pre-Payday to Payday phase, with volume increasing 11.6% to 14,086 eligible orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.09% → 92.97% | -0.1% | ⚠️ |
| Discount % | 13.95% → 14.87% | +6.6% | ⚠️ |
| PC2 | 52.07% → 52.23% | +0.3% | ✅ |
| Ship Rate | 46.72% → 47.61% | +1.9% | ✅ |

**Key Findings:**
- Ship Rate improved +1.9% in US despite Pre-Dunning AR declining slightly (-0.1%), indicating strong downstream conversion performance
- Discount % increased significantly (+6.6%), which typically has a negative relationship with Ship Rate, yet Ship Rate still improved—suggesting Payday timing effects outweighed discount pressure
- PC2 showed marginal improvement (+0.3%), contributing positively to the Ship Rate gain
- Volume increased 11.6% (12,619 → 14,086 orders), consistent with Payday phase influx
- The Payday phase transition appears to be the primary driver of improved conversion, overcoming headwinds from higher discounting

**Action:** Monitor — Ship Rate improvement aligns with expected Payday phase behavior. Continue tracking to confirm sustained performance and watch Discount % trend, as the +6.6% increase may compress margins if it persists post-Payday.

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

**Analysis:** The +0.89pp improvement in Dunning Ship Rate for US-HF in 2026-W16 is primarily attributable to the Payday phase transition, which drove increased customer payment capacity despite a +6.6% rise in Discount % that would typically suppress conversion. The slight decline in Pre-Dunning AR (-0.1%) had minimal impact, and the overall performance suggests healthy dunning operations that should be monitored for consistency as the payday cycle progresses.


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
