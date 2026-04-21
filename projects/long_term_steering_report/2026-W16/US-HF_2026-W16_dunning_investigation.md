# Dunning Investigation: US-HF 2026-W16

**Metric:** Dunning Ship Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 46.72% → 47.68% (+0.96pp)  
**Volume:** 14,106 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

**Overall:** Dunning Ship Rate improved by +0.96pp (46.72% → 47.68%) week-over-week, coinciding with a transition from Pre-Payday to Payday phase and an 11.8% increase in eligible order volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.09% → 92.97% | -0.1% | ✅ |
| Discount % | 13.95% → 14.87% | +6.6% | ⚠️ |
| PC2 | 51.24% → 52.22% | +1.9% | ✅ |
| Ship Rate | 46.72% → 47.68% | +2.1% | ✅ |

**Key Findings:**
- Ship Rate improvement of +0.96pp driven primarily by Payday phase timing, which typically increases customer payment capacity
- Discount % increased significantly (+6.6%), which normally correlates negatively with Ship Rate, yet Ship Rate still improved—suggesting Payday effect outweighed discount headwinds
- PC2 conversion showed modest improvement (+1.9%), contributing positively to overall Ship Rate gains
- Pre-Dunning AR remained essentially flat (-0.1%), indicating stable upstream funnel performance
- Volume increased by 11.8% (12,620 → 14,106 orders) with no evidence of Simpson's Paradox affecting the results

**Action:** Monitor — The improvement aligns with expected Payday phase behavior. Continue tracking to confirm Ship Rate maintains elevated levels through the Payday period and watch Discount % trend, as the +6.6% increase warrants attention if it continues rising in subsequent weeks.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 12,620 | 46.72% | - | 93.09% | - | 13.95% | - | 51.24% | - |
| 2026-W16 | Payday | 14,106 | 47.68% | →+2.1% | 92.97% | →-0.1% | 14.87% | ↑+6.6% | 52.22% | →+1.9% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 12,620 | 46.72% | - | 93.09% | - | 13.95% | - | 51.24% | - |
| 2026-W16 | Payday | 14,106 | 47.68% | →+2.1% | 92.97% | →-0.1% | 14.87% | ↑+6.6% | 52.22% | →+1.9% |

**Analysis:** The +0.96pp improvement in Dunning Ship Rate for US-HF during 2026-W16 is attributable to favorable Payday phase timing, which offset the negative pressure from increased discounting (+6.6%). The modest gains in PC2 conversion (+1.9%) further supported the positive outcome, while Pre-Dunning AR remained stable. No immediate action is required, but continued monitoring of Discount % trends is recommended to ensure profitability is not being eroded to achieve Ship Rate gains.


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
| US | →+2.1% | →-0.1% | ↑+6.6% | →+1.9% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 12,620 | 46.72% | 14,106 | 47.68% | 11.8% | Medium |

---


---

*Report: 2026-04-21*
