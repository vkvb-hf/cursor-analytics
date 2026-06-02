# Dunning Investigation: WL 2026-W22

**Metric:** Dunning Ship Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 31.67% → 30.84% (-0.83pp)  
**Volume:** 7,555 eligible orders  
**Payday Phase:** Post-Payday → Mid-Cycle

## Executive Summary

**Overall:** Dunning Ship Rate declined by 0.83pp (31.67% → 30.84%) week-over-week, representing a -2.6% relative decrease during the transition from Post-Payday to Mid-Cycle phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 89.24% → 89.45% | +0.2% | ✅ |
| Discount % | 15.79% → 17.34% | +9.8% | ⚠️ |
| PC2 | 51.86% → 37.92% | -26.9% | ⚠️ |
| Ship Rate | 31.67% → 30.84% | -2.6% | ⚠️ |

**Key Findings:**
- CK drove the majority of the decline with a -20.7% drop in Ship Rate (48.42% → 38.42%) despite stable Pre-Dunning AR, correlating with a significant +37.3% increase in Discount % (20.46% → 28.10%)
- PC2 experienced a substantial cluster-wide decline of -26.9% (51.86% → 37.92%), indicating reduced payment completion at step 2
- ER partially offset losses with a +16.5% Ship Rate improvement (25.54% → 29.75%) accompanied by a +9.0% increase in PC2
- Mix shift toward CK (+5.1% volume share) amplified negative impact, as CK's Ship Rate fell from highest-performing (48.42%) to medium tier (38.42%)
- Payday phase transition from Post-Payday to Mid-Cycle aligns with expected cyclical decline in customer payment capacity

**Action:** Investigate - Focus on CK's +37.3% Discount increase and determine if aggressive discounting strategy is cannibalizing Ship Rate; also investigate root cause of cluster-wide PC2 decline (-26.9%)

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W21 | Post-Payday | 7,720 | 31.67% | - | 89.24% | - | 15.79% | - | 51.86% | - |
| 2026-W22 | Mid-Cycle | 7,555 | 30.84% | ↓-2.6% | 89.45% | →+0.2% | 17.34% | ↑+9.8% | 37.92% | ↓-26.9% |

---

## L1: Country-Level Analysis

### CK (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W21 | Post-Payday | 1,483 | 48.42% | - | 92.83% | - | 20.46% | - | 44.53% | - |
| 2026-W22 | Mid-Cycle | 1,559 | 38.42% | ↓-20.7% | 92.73% | →-0.1% | 28.1% | ↑+37.3% | 45.77% | ↑+2.8% |

**Analysis:** The -0.83pp decline in Dunning Ship Rate is primarily attributed to CK's significant performance drop (-20.7%) driven by increased discounting (+37.3%) that failed to convert to shipments, combined with a substantial cluster-wide PC2 decline (-26.9%). While ER and CG showed positive momentum (+16.5% and +14.1% respectively), CK's outsized contribution and increased volume share amplified its negative impact on the overall metric. Immediate investigation into CK's discount strategy effectiveness and the underlying causes of PC2 deterioration is recommended before the next payday cycle.

### ER (Rank #2 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W21 | Post-Payday | 2,099 | 25.54% | - | 89.65% | - | 16.68% | - | 38.52% | - |
| 2026-W22 | Mid-Cycle | 2,007 | 29.75% | ↑+16.5% | 89.48% | →-0.2% | 16.34% | →-2.0% | 42.0% | ↑+9.0% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### CG (Rank #3 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W21 | Post-Payday | 755 | 22.12% | - | 96.52% | - | 16.7% | - | 51.27% | - |
| 2026-W22 | Mid-Cycle | 662 | 25.23% | ↑+14.1% | 96.53% | →+0.0% | 16.63% | →-0.4% | 47.95% | ↓-6.5% |

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
| CK | ↓-20.7% | →-0.1% | ↑+37.3% | ↑+2.8% | Post-Payday → Mid-Cycle | [AI_SUMMARY_PLACEHOLDER] |
| ER | ↑+16.5% | →-0.2% | →-2.0% | ↑+9.0% | Post-Payday → Mid-Cycle | [AI_SUMMARY_PLACEHOLDER] |
| CG | ↑+14.1% | →+0.0% | →-0.4% | ↓-6.5% | Post-Payday → Mid-Cycle | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,099 | 25.54% | 2,007 | 29.75% | -4.4% | Low |
| CK | 1,483 | 48.42% | 1,559 | 38.42% | 5.1% | Medium |
| MR | 1,154 | 0.43% | 1,179 | 0.25% | 2.2% | Low |
| AO | 1,046 | 70.65% | 1,008 | 69.05% | -3.6% | High |
| KN | 772 | 15.80% | 758 | 15.96% | -1.8% | Low |
| CG | 755 | 22.12% | 662 | 25.23% | -12.3% | Low |
| GN | 411 | 38.44% | 382 | 38.48% | -7.1% | Medium |

---


---

*Report: 2026-06-02*
