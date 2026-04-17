# Dunning Investigation: US-HF 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 47.75% → 46.73% (-1.02pp)  
**Volume:** 12,628 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined by 1.02pp (47.75% → 46.73%) week-over-week, representing a -2.1% relative decrease during the transition from Mid-Cycle to Pre-Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.78% → 93.09% | +0.31pp | ✅ |
| Discount % | 14.6% → 13.94% | -0.66pp | ✅ |
| PC2 | 49.33% → 52.08% | +2.75pp | ✅ |
| Ship Rate | 47.75% → 46.73% | -1.02pp | ⚠️ |

**Key Findings:**
- Ship Rate declined despite positive movements in all upstream metrics (Pre-Dunning AR +0.3%, Discount -4.5%, PC2 +5.6%)
- Volume decreased by 8.4% (13,791 → 12,628 orders), indicating fewer orders entered the dunning funnel
- The payday phase shift from Mid-Cycle to Pre-Payday correlates with the performance decline, suggesting timing-related payment constraints
- The paradox of improving individual metrics but declining Ship Rate suggests the volume reduction disproportionately removed higher-converting orders (compositional effect)
- Lower discount offering (-4.5%) may have reduced conversion incentive despite the metric relationship suggesting this should help

**Action:** Investigate — The disconnect between improving funnel metrics and declining Ship Rate warrants deeper analysis into the volume composition change and whether the Pre-Payday phase is creating systematic payment barriers for customers.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 13,791 | 47.75% | - | 92.78% | - | 14.6% | - | 49.33% | - |
| 2026-W15 | Pre-Payday | 12,628 | 46.73% | →-2.1% | 93.09% | →+0.3% | 13.94% | ↓-4.5% | 52.08% | ↑+5.6% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 13,791 | 47.75% | - | 92.78% | - | 14.6% | - | 49.33% | - |
| 2026-W15 | Pre-Payday | 12,628 | 46.73% | →-2.1% | 93.09% | →+0.3% | 13.94% | ↓-4.5% | 52.08% | ↑+5.6% |

**Analysis:** The 1.02pp decline in US-HF Dunning Ship Rate appears driven primarily by the payday phase transition to Pre-Payday combined with an 8.4% volume reduction that likely removed higher-propensity orders from the eligible pool. While individual funnel metrics showed improvement, the compositional shift in the order mix and timing of the dunning cycle relative to customer paydays created headwinds that outweighed these gains. Recommend monitoring through the payday transition to confirm recovery and analyzing the characteristics of orders that exited the funnel.


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
| US | →-2.1% | →+0.3% | ↓-4.5% | ↑+5.6% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 13,791 | 47.75% | 12,628 | 46.73% | -8.4% | Medium |

---


---

*Report: 2026-04-17*
