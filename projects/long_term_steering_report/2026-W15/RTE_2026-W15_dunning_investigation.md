# Dunning Investigation: RTE 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 44.24% → 42.60% (-1.64pp)  
**Volume:** 19,565 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined from 44.24% to 42.60% (-1.64pp) in W15, driven primarily by FJ's -5.5% relative decline and severe drops in smaller markets TV (-59.4%) and TO (-24.6%), amid a Pre-Payday phase transition.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.53% → 92.82% | +0.29pp | ✅ |
| Discount % | 17.76% → 17.49% | -0.27pp | ✅ |
| PC2 | 42.79% → 48.54% | +5.75pp | ✅ |
| Ship Rate | 44.24% → 42.60% | -1.64pp | ⚠️ |

**Key Findings:**
- **FJ dominates the decline:** As the largest market (70% of volume), FJ's ship rate dropped -5.5% (43.54% → 41.16%) despite improved Pre-Dunning AR (+0.4%) and lower Discount % (-3.2%), suggesting customer payment behavior issues during Pre-Payday phase
- **TV experienced catastrophic decline:** Ship rate plummeted -59.4% (30.77% → 12.50%) on small volume (96 orders), with PC2 rising +15.2% indicating customers are deferring payments to second payment cycle
- **TO shows concerning trajectory:** -24.6% ship rate decline paired with significant Discount % increase (+9.4%) suggests deeper customer financial stress
- **PC2 spike across all markets:** Every country showed PC2 increases (+13.3% to +20.5%), indicating systematic payment deferral behavior consistent with Pre-Payday cash constraints
- **Volume contraction observed:** Total eligible orders dropped -9.7% (21,660 → 19,565), with TK (-65.8%) and TZ (-33.0%) showing largest volume declines

**Action:** **Investigate** — The disconnect between improving upstream metrics (Pre-Dunning AR, Discount %) and declining Ship Rate, combined with universal PC2 spikes, suggests Pre-Payday timing is causing systematic payment deferrals. Prioritize FJ deep-dive given volume contribution.

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

**Analysis:** The W15 Dunning Ship Rate decline is primarily attributable to Pre-Payday phase timing effects, evidenced by the cluster-wide PC2 surge (+13.4%) as customers defer payments until payday. FJ requires immediate attention given its volume dominance and -5.5% relative decline, while TV and TO warrant monitoring despite lower volumes due to severe rate deterioration. Recommend tracking W16 performance post-payday to confirm cyclical pattern versus structural degradation.

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
