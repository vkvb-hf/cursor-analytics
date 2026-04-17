# Dunning Investigation: RTE 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 44.24% → 42.60% (-1.64pp)  
**Volume:** 19,565 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined from 44.24% to 42.60% (-1.64pp) week-over-week, coinciding with a payday phase transition from Mid-Cycle to Pre-Payday.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.53% → 92.82% | +0.29pp | ✅ |
| Discount % | 17.76% → 17.49% | -0.27pp | ✅ |
| PC2 | 42.79% → 48.54% | +5.75pp | ✅ |
| Ship Rate | 44.24% → 42.60% | -1.64pp | ⚠️ |

**Key Findings:**
- **FJ drove the majority of decline:** As the largest volume country (70% of orders), FJ's ship rate dropped -5.5% (43.54% → 41.16%) despite improving Pre-Dunning AR (+0.4%) and lower discounts (-3.2%)
- **TV experienced severe collapse:** Ship rate plummeted -59.4% (30.77% → 12.50%) on small volume (96 orders), representing the largest relative decline across all countries
- **TO showed significant deterioration:** Ship rate fell -24.6% (31.67% → 23.88%) with a concerning +9.4% increase in Discount % suggesting affordability pressure
- **PC2 increased universally:** All countries showed PC2 increases (+13.3% to +20.5%), yet ship rates declined, indicating payment capacity did not translate to conversions
- **Volume contracted -9.7%:** Total eligible orders dropped from 21,660 to 19,565, with high-SR country YE maintaining relative stability (→-1.4%)

**Action:** **Investigate** - The disconnect between improving upstream metrics (Pre-Dunning AR, PC2) and declining Ship Rate, particularly in FJ and TV, suggests potential issues with dunning messaging effectiveness or timing during the Pre-Payday phase transition.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 21,660 | 44.24% | - | 92.53% | - | 17.76% | - | 42.79% | - |
| 2026-W15 | Pre-Payday | 19,565 | 42.60% | ↓-3.7% | 92.82% | →+0.3% | 17.49% | →-1.5% | 48.54% | ↑+13.4% |

---

## L1: Country-Level Analysis

### FJ (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 15,137 | 43.54% | - | 93.62% | - | 17.72% | - | 43.98% | - |
| 2026-W15 | Pre-Payday | 13,715 | 41.16% | ↓-5.5% | 93.97% | →+0.4% | 17.15% | ↓-3.2% | 50.36% | ↑+14.5% |

**Analysis:** The -1.64pp decline in Dunning Ship Rate appears driven primarily by FJ's underperformance and severe drops in smaller markets TV and TO, despite stable or improving Pre-Dunning AR and PC2 metrics across all countries. The payday phase transition to Pre-Payday typically correlates with customer liquidity constraints, which may explain the universal pattern of increased PC2 not converting to actual shipments. Recommend investigating dunning touchpoint effectiveness and timing optimization for Pre-Payday periods, with particular focus on FJ given its dominant volume contribution.

### YE (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 3,485 | 59.63% | - | 88.15% | - | 15.93% | - | 41.87% | - |
| 2026-W15 | Pre-Payday | 3,324 | 58.81% | →-1.4% | 87.77% | →-0.4% | 16.24% | →+1.9% | 50.47% | ↑+20.5% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### TO (Rank #3 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 341 | 31.67% | - | 84.89% | - | 24.68% | - | 29.13% | - |
| 2026-W15 | Pre-Payday | 268 | 23.88% | ↓-24.6% | 86.67% | →+2.1% | 26.99% | ↑+9.4% | 33.0% | ↑+13.3% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### TV (Rank #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 91 | 30.77% | - | 93.41% | - | 17.27% | - | 33.38% | - |
| 2026-W15 | Pre-Payday | 96 | 12.50% | ↓-59.4% | 92.14% | →-1.4% | 17.76% | ↑+2.8% | 38.46% | ↑+15.2% |

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
| FJ | ↓-5.5% | →+0.4% | ↓-3.2% | ↑+14.5% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| YE | →-1.4% | →-0.4% | →+1.9% | ↑+20.5% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| TO | ↓-24.6% | →+2.1% | ↑+9.4% | ↑+13.3% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| TV | ↓-59.4% | →-1.4% | ↑+2.8% | ↑+15.2% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| FJ | 15,137 | 43.54% | 13,715 | 41.16% | -9.4% | Medium |
| YE | 3,485 | 59.63% | 3,324 | 58.81% | -4.6% | High |
| CF | 2,194 | 30.36% | 1,887 | 30.26% | -14.0% | Medium |
| TO | 341 | 31.67% | 268 | 23.88% | -21.4% | Medium |
| TZ | 194 | 26.80% | 130 | 26.15% | -33.0% | Low |
| TK | 146 | 24.66% | 50 | 32.00% | -65.8% | Low |
| TV | 91 | 30.77% | 96 | 12.50% | 5.5% | Medium |
| TT | 72 | 33.33% | 95 | 40.00% | 31.9% | Medium |

---


---

*Report: 2026-04-17*
