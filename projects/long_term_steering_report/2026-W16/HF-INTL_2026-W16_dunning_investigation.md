# Dunning Investigation: HF-INTL 2026-W16

**Metric:** Dunning Ship Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 65.58% → 66.73% (+1.15pp)  
**Volume:** 30,285 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate improved from 65.58% to 66.73% (+1.15pp) in W16, driven by the transition from Pre-Payday to Payday phase, with volume increasing 11.0% to 30,285 eligible orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.83% → 93.76% | -0.1% | ✅ |
| Discount % | 13.81% → 13.92% | +0.8% | ✅ |
| PC2 | 46.31% → 46.22% | -0.2% | ✅ |
| Ship Rate | 65.58% → 66.73% | +1.8% | ✅ |

**Key Findings:**
- **AU** showed strong improvement (+7.0% SR) driven primarily by an 8.7% decrease in Discount %, consistent with Payday phase behavior where customers need fewer incentives
- **NO** had the highest SR gain (+7.3%) paired with a significant 21.9% decrease in Discount % and 59.0% volume increase, indicating strong Payday effect
- **NZ** is a concern: Ship Rate declined 13.3% despite Payday phase, with Discount % increasing 17.7% – suggesting structural issues beyond payment timing
- **GB** volume grew 22.4% (largest absolute contributor) with moderate SR improvement (+4.1%), though Discount % increased 3.4% which partially offset gains
- Mix shift toward higher-volume, lower-SR markets (GB +22.4% volume at 59.30% SR) may be masking stronger underlying performance in other countries

**Action:** **Monitor** – Overall improvement is healthy and aligned with expected Payday phase patterns. **Investigate NZ** specifically to understand the counter-trend decline despite favorable payment timing.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 27,283 | 65.58% | - | 93.83% | - | 13.81% | - | 46.31% | - |
| 2026-W16 | Payday | 30,285 | 66.73% | →+1.8% | 93.76% | →-0.1% | 13.92% | →+0.8% | 46.22% | →-0.2% |

---

## L1: Country-Level Analysis

### AU (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 5,021 | 64.73% | - | 90.80% | - | 13.66% | - | 50.91% | - |
| 2026-W16 | Payday | 5,169 | 69.26% | ↑+7.0% | 91.18% | →+0.4% | 12.47% | ↓-8.7% | 51.22% | →+0.6% |

**Analysis:** The HF-INTL cluster's Ship Rate improvement of +1.15pp is primarily attributable to the Pre-Payday to Payday phase transition, with AU and NO demonstrating textbook Payday behavior (higher conversion with lower discounting). However, NZ's significant decline (-13.3% SR) despite the favorable payment phase warrants targeted investigation, as the 17.7% increase in Discount % suggests potential issues with customer payment capability or product-market fit in that region.

### GB (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 6,292 | 56.99% | - | 94.13% | - | 17.18% | - | 48.86% | - |
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
| 2026-W16 | Payday | 1,269 | 60.28% | ↓-13.3% | 88.97% | →-0.1% | 16.48% | ↑+17.7% | 47.12% | →-2.4% |

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
