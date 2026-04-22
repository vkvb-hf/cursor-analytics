# Dunning Investigation: HF-INTL 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 70.87% → 65.58% (-5.29pp)  
**Volume:** 27,283 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined significantly from 70.87% to 65.58% (-5.29pp) in HF-INTL during 2026-W15, coinciding with a payday phase transition from Mid-Cycle to Pre-Payday and a 25.6% reduction in eligible order volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.06% → 93.84% | +0.78pp | ✅ |
| Discount % | 13.58% → 13.81% | +0.23pp | ⚠️ |
| PC2 | 46.28% → 46.31% | +0.03pp | ✅ |
| Ship Rate | 70.87% → 65.58% | -5.29pp | ⚠️ |

**Key Findings:**
- SE experienced the largest Ship Rate decline (-14.7%), despite an 18.7% increase in Discount % which typically correlates negatively with Ship Rate performance
- GB and FR, the two largest markets by volume contribution, both saw Ship Rate drops exceeding 12% while maintaining stable Pre-Dunning AR and Discount metrics, suggesting payday phase timing as the primary driver
- DE showed a notable 8.2% increase in Discount % alongside a -9.9% Ship Rate decline, indicating potential discount ineffectiveness during Pre-Payday periods
- Volume declined across 9 of 10 top countries, with DK experiencing the steepest drop (-54.7%), while NO was the only country showing volume growth (+34.5%) and Ship Rate improvement (+2.96pp)
- Pre-Dunning AR remained stable or improved across most markets, confirming the Ship Rate decline is occurring post-approval in the dunning funnel

**Action:** Monitor — The decline appears primarily driven by the predictable Pre-Payday phase transition. Track 2026-W16 performance to confirm recovery as customers enter Post-Payday phase. Investigate SE and DE discount strategy effectiveness if underperformance persists.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 36,650 | 70.87% | - | 93.06% | - | 13.58% | - | 46.28% | - |
| 2026-W15 | Pre-Payday | 27,283 | 65.58% | ↓-7.5% | 93.84% | →+0.8% | 13.81% | →+1.7% | 46.31% | →+0.1% |

---

## L1: Country-Level Analysis

### GB (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 8,720 | 64.99% | - | 93.07% | - | 16.87% | - | 48.61% | - |
| 2026-W15 | Pre-Payday | 6,292 | 56.99% | ↓-12.3% | 94.14% | →+1.1% | 17.18% | →+1.8% | 48.86% | →+0.5% |

**Analysis:** The 5.29pp decline in Dunning Ship Rate for HF-INTL is predominantly attributable to the cyclical payday phase shift from Mid-Cycle to Pre-Payday, a period when customer payment capacity is typically constrained. While all major markets showed rate declines, the stability of Pre-Dunning AR (+0.78pp) indicates upstream approval quality remains intact, and the issue is concentrated in customer payment behavior during this phase. Performance should be reassessed in W16 to confirm expected recovery post-payday.

### FR (Rank #2 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 7,642 | 69.96% | - | 92.95% | - | 12.08% | - | 45.75% | - |
| 2026-W15 | Pre-Payday | 5,272 | 61.48% | ↓-12.1% | 94.49% | →+1.7% | 12.11% | →+0.2% | 45.12% | →-1.4% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### DE (Rank #3 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 4,511 | 74.73% | - | 96.43% | - | 15.89% | - | 42.14% | - |
| 2026-W15 | Pre-Payday | 3,160 | 67.31% | ↓-9.9% | 97.34% | →+0.9% | 17.19% | ↑+8.2% | 42.0% | →-0.3% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### SE (Rank #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 808 | 71.66% | - | 96.24% | - | 9.16% | - | 41.28% | - |
| 2026-W15 | Pre-Payday | 690 | 61.16% | ↓-14.7% | 95.19% | →-1.1% | 10.87% | ↑+18.7% | 41.77% | →+1.2% |

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
| GB | ↓-12.3% | →+1.1% | →+1.8% | →+0.5% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| FR | ↓-12.1% | →+1.7% | →+0.2% | →-1.4% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| DE | ↓-9.9% | →+0.9% | ↑+8.2% | →-0.3% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| SE | ↓-14.7% | →-1.1% | ↑+18.7% | →+1.2% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| GB | 8,720 | 64.99% | 6,292 | 56.99% | -27.8% | High |
| FR | 7,642 | 69.96% | 5,272 | 61.48% | -31.0% | High |
| AU | 5,848 | 66.11% | 5,021 | 64.73% | -14.1% | High |
| DE | 4,511 | 74.73% | 3,160 | 67.31% | -29.9% | High |
| BE | 3,221 | 90.50% | 1,995 | 87.57% | -38.1% | High |
| NZ | 1,302 | 61.29% | 1,132 | 69.52% | -13.1% | High |
| DK | 1,229 | 76.00% | 557 | 67.68% | -54.7% | High |
| IE | 1,148 | 65.85% | 877 | 61.80% | -23.6% | High |
| NO | 943 | 79.22% | 1,268 | 82.18% | 34.5% | High |
| SE | 808 | 71.66% | 690 | 61.16% | -14.6% | High |

---


---

*Report: 2026-04-22*
