# Dunning Investigation: HF-INTL 2026-W19

**Metric:** Dunning Ship Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 72.12% → 68.77% (-3.35pp)  
**Volume:** 29,657 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined by -3.35pp (72.12% → 68.77%) during the transition from Mid-Cycle to Pre-Payday phase, with volume decreasing 16% from 35,330 to 29,657 eligible orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | Stable/Improved | +0.3% | ✅ |
| Discount % | Increased (Negative) | +4.5% | ⚠️ |
| PC2 | Increased (Positive) | +5.6% | ✅ |
| Payday Phase | Mid-Cycle → Pre-Payday | - | ⚠️ |

**Key Findings:**
- **SE** experienced the largest Ship Rate decline (-14.8%) despite strong Pre-Dunning AR improvement (+2.5%), driven by a massive +26.7% increase in Discount % and -56.5% volume drop
- **GB** contributed most to the overall decline with -13.3% Ship Rate drop and -26.1% volume reduction; elevated Discount % (+6.2%) is the primary driver as AR remained stable
- **DE** showed a -6.3% Ship Rate decline with the steepest Discount % increase (+10.9%) and a notable PC2 drop (-12.7%), suggesting both pricing pressure and fulfillment issues
- The Pre-Payday phase transition correlates with increased discount activity across all major markets, indicating customers are more price-sensitive before payday
- Mix shift toward lower-performing markets (SE volume down 56.5%, GB down 26.1%) partially contributes to the cluster-level decline

**Action:** **Investigate** - The widespread Discount % increases across GB, DE, and SE during Pre-Payday phase suggest a systemic pricing/affordability issue requiring review of dunning discount strategy and payday-aligned offer timing.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W18 | Mid-Cycle | 35,330 | 72.12% | - | 93.53% | - | 11.87% | - | 42.56% | - |
| 2026-W19 | Pre-Payday | 29,657 | 68.77% | ↓-4.6% | 93.82% | →+0.3% | 12.4% | ↑+4.5% | 44.95% | ↑+5.6% |

---

## L1: Country-Level Analysis

### GB (Rank #1 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W18 | Mid-Cycle | 8,518 | 67.32% | - | 93.63% | - | 15.41% | - | 45.28% | - |
| 2026-W19 | Pre-Payday | 6,294 | 58.40% | ↓-13.3% | 94.62% | →+1.1% | 16.36% | ↑+6.2% | 46.92% | ↑+3.6% |

**Analysis:** The -3.35pp Ship Rate decline in HF-INTL during W19 is primarily driven by elevated Discount % across all major markets during the Pre-Payday phase, with GB, DE, and SE contributing most significantly to the drop. While Pre-Dunning AR and PC2 metrics remain healthy, the correlation between payday timing and increased discount-seeking behavior warrants a strategic review of dunning offer cadence and discount thresholds to optimize recovery rates during financially constrained periods.

### DE (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W18 | Mid-Cycle | 4,386 | 75.06% | - | 96.93% | - | 13.45% | - | 44.0% | - |
| 2026-W19 | Pre-Payday | 3,568 | 70.35% | ↓-6.3% | 97.42% | →+0.5% | 14.92% | ↑+10.9% | 38.4% | ↓-12.7% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### SE (Rank #3 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W18 | Mid-Cycle | 1,277 | 73.84% | - | 94.91% | - | 7.98% | - | 37.95% | - |
| 2026-W19 | Pre-Payday | 555 | 62.88% | ↓-14.8% | 97.31% | ↑+2.5% | 10.11% | ↑+26.7% | 41.28% | ↑+8.8% |

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
| GB | ↓-13.3% | →+1.1% | ↑+6.2% | ↑+3.6% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| DE | ↓-6.3% | →+0.5% | ↑+10.9% | ↓-12.7% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| SE | ↓-14.8% | ↑+2.5% | ↑+26.7% | ↑+8.8% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| GB | 8,518 | 67.32% | 6,294 | 58.40% | -26.1% | High |
| FR | 6,528 | 68.03% | 6,076 | 67.92% | -6.9% | High |
| AU | 5,415 | 69.53% | 5,477 | 68.76% | 1.1% | High |
| DE | 4,386 | 75.06% | 3,568 | 70.35% | -18.7% | High |
| BE | 2,825 | 91.75% | 2,202 | 90.60% | -22.1% | High |
| NO | 1,329 | 79.61% | 1,338 | 81.46% | 0.7% | High |
| SE | 1,277 | 73.84% | 555 | 62.88% | -56.5% | High |
| IE | 1,275 | 64.86% | 871 | 59.70% | -31.7% | High |
| NZ | 1,213 | 63.97% | 1,305 | 66.82% | 7.6% | High |
| DK | 1,187 | 78.60% | 978 | 75.87% | -17.6% | High |

---


---

*Report: 2026-05-12*
