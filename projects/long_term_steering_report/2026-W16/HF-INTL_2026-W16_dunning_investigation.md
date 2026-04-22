# Dunning Investigation: HF-INTL 2026-W16

**Metric:** Dunning Ship Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 65.58% → 66.73% (+1.15pp)  
**Volume:** 30,285 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate improved from 65.58% to 66.73% (+1.15pp) week-over-week, with volume increasing by 11.0% (27,283 → 30,285 eligible orders) as the cluster transitioned from Pre-Payday to Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.84% → 93.76% | -0.1% | ✅ Stable |
| Discount % | 13.81% → 13.92% | +0.8% | ✅ Stable |
| PC2 | 46.31% → 46.22% | -0.2% | ✅ Stable |
| Ship Rate | 65.58% → 66.73% | +1.8% | ✅ Improved |

**Key Findings:**
- **AU** showed strong improvement (+7.0% SR) driven primarily by an 8.7% reduction in Discount %, indicating better payment behavior during Payday phase
- **NO** achieved the highest Ship Rate gain (+7.3%) with a significant 21.9% decrease in Discount % and 59.0% volume increase, suggesting strong Payday effect
- **NZ** is a concern with Ship Rate declining 13.3% despite Payday phase, accompanied by a 17.7% increase in Discount % usage
- **GB** improved (+4.1% SR) despite increased Discount % (+3.4%), suggesting Payday liquidity offset discount pressure; volume grew 22.4%
- Mix shift detected: NO volume increased 59.0% (high-performing at 88.19% SR), while BE volume decreased 15.3% (high-performing at 86.80% SR)

**Action:** **Investigate** - NZ requires immediate attention due to counter-cyclical performance decline during Payday; determine if this is a localized issue (payment processor, campaign, or cohort-specific)

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 27,283 | 65.58% | - | 93.84% | - | 13.81% | - | 46.31% | - |
| 2026-W16 | Payday | 30,285 | 66.73% | →+1.8% | 93.76% | →-0.1% | 13.92% | →+0.8% | 46.22% | →-0.2% |

---

## L1: Country-Level Analysis

### AU (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 5,021 | 64.73% | - | 90.80% | - | 13.66% | - | 50.91% | - |
| 2026-W16 | Payday | 5,169 | 69.26% | ↑+7.0% | 91.18% | →+0.4% | 12.47% | ↓-8.7% | 51.22% | →+0.6% |

**Analysis:** The HF-INTL cluster demonstrated healthy improvement in Dunning Ship Rate during the Payday phase, with AU and NO driving gains through reduced discount dependency. However, NZ's significant underperformance (-13.3% SR with +17.7% Discount %) warrants investigation as it runs counter to expected Payday behavior. The overall positive trajectory is supported by favorable mix shift toward higher-volume, higher-performing markets like NO and GB.

### GB (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 6,292 | 56.99% | - | 94.14% | - | 17.18% | - | 48.86% | - |
| 2026-W16 | Payday | 7,701 | 59.30% | ↑+4.1% | 93.92% | →-0.2% | 17.77% | ↑+3.4% | 48.61% | →-0.5% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### NO (Rank #3 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 1,268 | 82.18% | - | 91.00% | - | 7.76% | - | 39.22% | - |
| 2026-W16 | Payday | 2,016 | 88.19% | ↑+7.3% | 89.15% | →-2.0% | 6.06% | ↓-21.9% | 38.71% | →-1.3% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### NZ (Rank #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 1,132 | 69.52% | - | 89.03% | - | 14.0% | - | 48.27% | - |
| 2026-W16 | Payday | 1,269 | 60.28% | ↓-13.3% | 88.98% | →-0.1% | 16.48% | ↑+17.7% | 47.12% | →-2.4% |

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
| AU | ↑+7.0% | →+0.4% | ↓-8.7% | →+0.6% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| GB | ↑+4.1% | →-0.2% | ↑+3.4% | →-0.5% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| NO | ↑+7.3% | →-2.0% | ↓-21.9% | →-1.3% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| NZ | ↓-13.3% | →-0.1% | ↑+17.7% | →-2.4% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| GB | 6,292 | 56.99% | 7,701 | 59.30% | 22.4% | High |
| FR | 5,272 | 61.48% | 5,335 | 60.73% | 1.2% | High |
| AU | 5,021 | 64.73% | 5,169 | 69.26% | 2.9% | High |
| DE | 3,160 | 67.31% | 3,454 | 65.72% | 9.3% | High |
| BE | 1,995 | 87.57% | 1,689 | 86.80% | -15.3% | High |
| NO | 1,268 | 82.18% | 2,016 | 88.19% | 59.0% | High |
| NZ | 1,132 | 69.52% | 1,269 | 60.28% | 12.1% | High |
| IE | 877 | 61.80% | 947 | 66.00% | 8.0% | High |
| SE | 690 | 61.16% | 905 | 65.52% | 31.2% | High |
| DK | 557 | 67.68% | 734 | 71.25% | 31.8% | High |

---


---

*Report: 2026-04-22*
