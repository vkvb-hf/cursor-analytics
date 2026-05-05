# Dunning Investigation: WL 2026-W18

**Metric:** Dunning Ship Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 31.33% → 31.06% (-0.27pp)  
**Volume:** 8,504 eligible orders  
**Payday Phase:** Post-Payday → Mid-Cycle

## Executive Summary

**Overall:** The Dunning Ship Rate declined slightly from 31.33% to 31.06% (-0.27pp) week-over-week, with volume increasing by 4.7% (8,125 → 8,504 orders) during the transition from Post-Payday to Mid-Cycle phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 90.11% → 89.54% | -0.57pp | ⚠️ |
| Discount % | 16.65% → 16.09% | -0.56pp | ✅ |
| PC2 | 9.21% → 39.75% | +30.54pp | ✅ |
| Ship Rate | 31.33% → 31.06% | -0.27pp | ⚠️ |

**Key Findings:**
- CG experienced the largest Ship Rate decline (-15.4%), despite stable Pre-Dunning AR (96.80%) and reduced Discount % (-2.8%), suggesting unexplained conversion issues unrelated to standard funnel metrics
- CK showed strong improvement (+7.1% Ship Rate) driven primarily by reduced Discount % (-5.9%), partially offsetting cluster-level decline
- ER, the highest-volume country (2,528 orders), declined -4.3% in Ship Rate with minimal movement in Pre-Dunning AR (-0.5%) and Discount % (-1.6%), indicating Mid-Cycle payday phase impact
- PC2 increased dramatically at cluster level (+331.6%), yet Ship Rate still declined, suggesting PC2 gains did not translate to conversions
- Mix shift shows MR (+12.3% volume) and KN (+19.8% volume) growing disproportionately—both are Low SR tier countries, contributing to overall rate dilution

**Action:** Monitor — The decline is modest (-0.27pp) and largely attributable to payday phase transition and unfavorable mix shift toward low-performing countries. Investigate CG specifically if decline persists next week.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W17 | Post-Payday | 8,125 | 31.33% | - | 90.11% | - | 16.65% | - | 9.21% | - |
| 2026-W18 | Mid-Cycle | 8,504 | 31.06% | →-0.9% | 89.54% | →-0.6% | 16.09% | ↓-3.4% | 39.75% | ↑+331.6% |

---

## L1: Country-Level Analysis

### CK (Rank #1 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W17 | Post-Payday | 1,493 | 43.34% | - | 93.77% | - | 28.2% | - | 47.13% | - |
| 2026-W18 | Mid-Cycle | 1,590 | 46.42% | ↑+7.1% | 93.13% | →-0.7% | 26.53% | ↓-5.9% | 47.5% | →+0.8% |

**Analysis:** The W18 Dunning Ship Rate decline of 0.27pp is primarily driven by the transition from Post-Payday to Mid-Cycle phase, compounded by volume growth in low-performing countries (MR, KN) diluting overall rates. CG requires targeted attention given its outsized -15.4% decline without clear metric-based explanation, while CK's strong performance (+7.1%) demonstrates that discount optimization continues to be effective in select markets.

### ER (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W17 | Post-Payday | 2,637 | 27.42% | - | 90.18% | - | 15.46% | - | 41.78% | - |
| 2026-W18 | Mid-Cycle | 2,528 | 26.23% | ↓-4.3% | 89.72% | →-0.5% | 15.22% | →-1.6% | 43.85% | ↑+5.0% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### CG (Rank #3 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W17 | Post-Payday | 748 | 23.13% | - | 96.86% | - | 16.2% | - | 50.36% | - |
| 2026-W18 | Mid-Cycle | 787 | 19.57% | ↓-15.4% | 96.80% | →-0.1% | 15.75% | ↓-2.8% | 50.86% | →+1.0% |

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
| CK | ↑+7.1% | →-0.7% | ↓-5.9% | →+0.8% | Post-Payday → Mid-Cycle | [AI_SUMMARY_PLACEHOLDER] |
| ER | ↓-4.3% | →-0.5% | →-1.6% | ↑+5.0% | Post-Payday → Mid-Cycle | [AI_SUMMARY_PLACEHOLDER] |
| CG | ↓-15.4% | →-0.1% | ↓-2.8% | →+1.0% | Post-Payday → Mid-Cycle | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,637 | 27.42% | 2,528 | 26.23% | -4.1% | Low |
| CK | 1,493 | 43.34% | 1,590 | 46.42% | 6.5% | Medium |
| MR | 1,124 | 0.18% | 1,262 | 0.16% | 12.3% | Low |
| AO | 1,018 | 67.58% | 1,089 | 68.14% | 7.0% | High |
| CG | 748 | 23.13% | 787 | 19.57% | 5.2% | Low |
| KN | 595 | 16.81% | 713 | 14.59% | 19.8% | Low |
| GN | 510 | 41.57% | 535 | 44.49% | 4.9% | Medium |

---


---

*Report: 2026-05-05*
