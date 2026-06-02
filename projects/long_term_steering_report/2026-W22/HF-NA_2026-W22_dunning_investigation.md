# Dunning Investigation: HF-NA 2026-W22

**Metric:** Dunning Ship Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 46.48% → 44.69% (-1.79pp)  
**Volume:** 16,610 eligible orders  
**Payday Phase:** Post-Payday → Mid-Cycle

## Executive Summary

**Overall:** Dunning Ship Rate declined from 46.48% to 44.69% (-1.79pp) during the transition from Post-Payday to Mid-Cycle phase, with CA experiencing the steepest decline (-7.3%) while US showed moderate decline (-2.8%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | Stable? | -0.2% | ✅ |
| Discount % | Stable? | +18.8% | ⚠️ |
| PC2 | Stable? | +3.3% | ✅ |
| Ship Rate | Improved? | -3.9% | ⚠️ |

**Key Findings:**
- Discount % increased significantly (+18.8% cluster-wide), which has a negative relationship with Ship Rate and is the primary driver of the decline
- CA showed the largest Ship Rate drop (-7.3%) despite improved Pre-Dunning AR (+0.5%) and higher PC2 (+8.8%), indicating discount increases (+9.7%) overwhelmed positive signals
- US saw the largest absolute discount increase (+21.9%) contributing to its -2.8% Ship Rate decline
- Mix shift shows CA (high SR tier at 50.20%) lost volume (-2.4%) while lower-performing US gained volume (+1.8%), creating modest compositional headwind
- Payday phase transition from Post-Payday to Mid-Cycle aligns with typical mid-cycle liquidity constraints

**Action:** Investigate - The significant discount increases across both countries suggest potential pricing or promotional strategy changes that warrant review; evaluate whether discount thresholds are calibrated appropriately for mid-cycle timing.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W21 | Post-Payday | 16,461 | 46.48% | - | 92.89% | - | 14.5% | - | 49.01% | - |
| 2026-W22 | Mid-Cycle | 16,610 | 44.69% | ↓-3.9% | 92.75% | →-0.2% | 17.23% | ↑+18.8% | 50.64% | ↑+3.3% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W21 | Post-Payday | 12,977 | 45.48% | - | 92.71% | - | 13.87% | - | 49.95% | - |
| 2026-W22 | Mid-Cycle | 13,209 | 44.21% | ↓-2.8% | 92.42% | →-0.3% | 16.91% | ↑+21.9% | 50.93% | →+2.0% |

**Analysis:** The 1.79pp decline in Dunning Ship Rate is primarily attributable to substantial discount percentage increases (+18.8% cluster-wide) during the Mid-Cycle payday phase, with CA contributing disproportionately to the decline (-7.3% SR change) despite stable or improving upstream metrics. The combination of aggressive discounting and unfavorable payday timing suggests a review of discount strategy calibration is warranted to determine if current thresholds are appropriate for mid-cycle customer liquidity conditions.

### CA (Rank #2 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W21 | Post-Payday | 3,484 | 50.20% | - | 93.54% | - | 16.83% | - | 45.51% | - |
| 2026-W22 | Mid-Cycle | 3,401 | 46.55% | ↓-7.3% | 94.02% | →+0.5% | 18.46% | ↑+9.7% | 49.52% | ↑+8.8% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]


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
| US | ↓-2.8% | →-0.3% | ↑+21.9% | →+2.0% | Post-Payday → Mid-Cycle | [AI_SUMMARY_PLACEHOLDER] |
| CA | ↓-7.3% | →+0.5% | ↑+9.7% | ↑+8.8% | Post-Payday → Mid-Cycle | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 12,977 | 45.48% | 13,209 | 44.21% | 1.8% | Medium |
| CA | 3,484 | 50.20% | 3,401 | 46.55% | -2.4% | High |

---


---

*Report: 2026-06-02*
