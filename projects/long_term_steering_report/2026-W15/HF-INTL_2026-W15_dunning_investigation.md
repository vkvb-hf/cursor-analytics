# Dunning Investigation: HF-INTL 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 70.87% → 65.62% (-5.25pp)  
**Volume:** 27,317 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined significantly from 70.87% to 65.62% (-5.25pp) week-over-week, coinciding with a transition from Mid-Cycle to Pre-Payday phase and a 25.5% reduction in eligible order volume (36,656 → 27,317).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | Stable/Improved | +0.8% | ✅ |
| Discount % | Slight Increase | +1.7% | ⚠️ |
| PC2 (Payment Capture) | Increased | +7.9% | ✅ |
| Ship Rate | Declined | -7.4% | ⚠️ |

**Key Findings:**
- **Payday Phase Impact:** All four analyzed countries (GB, FR, DE, SE) transitioned from Mid-Cycle to Pre-Payday, correlating with universal Ship Rate declines ranging from -9.9% to -14.7%
- **SE Most Impacted:** SE showed the steepest Ship Rate decline (-14.7%) paired with the largest Discount % increase (+18.7%), suggesting aggressive discounting failed to offset Pre-Payday liquidity constraints
- **GB Largest Contributor:** GB contributed most to the overall decline with Ship Rate falling from 64.99% to 57.02% (-12.3%) despite stable Pre-Dunning AR (+1.1%) and improving PC2 (+5.9%)
- **Volume Contraction Broad-Based:** Significant volume drops across major markets (DK -54.7%, BE -38.1%, FR -30.8%, DE -29.9%) indicate systematic reduction in dunning-eligible orders
- **Metric Divergence:** Pre-Dunning AR and PC2 improved across most countries, yet Ship Rate declined—suggesting the conversion breakdown occurs between payment capture and actual shipment

**Action:** **Investigate** — The disconnect between improving upstream metrics (Pre-Dunning AR, PC2) and declining Ship Rate during Pre-Payday phase warrants deeper analysis into post-payment fulfillment barriers and whether payday timing adjustments to dunning campaigns could improve outcomes.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 36,656 | 70.87% | - | 93.06% | - | 13.57% | - | 42.92% | - |
| 2026-W15 | Pre-Payday | 27,317 | 65.62% | ↓-7.4% | 93.83% | →+0.8% | 13.8% | →+1.7% | 46.31% | ↑+7.9% |

---

## L1: Country-Level Analysis

### GB (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 8,721 | 64.99% | - | 93.07% | - | 16.87% | - | 46.13% | - |
| 2026-W15 | Pre-Payday | 6,301 | 57.02% | ↓-12.3% | 94.14% | →+1.1% | 17.17% | →+1.8% | 48.87% | ↑+5.9% |

**Analysis:** The 5.25pp decline in Dunning Ship Rate is primarily driven by the Pre-Payday phase transition, which negatively impacted conversion despite stable approval rates and improved payment capture metrics across all major markets. GB, FR, DE, and SE all experienced double-digit percentage declines in Ship Rate, with increased discounting in DE (+8.2%) and SE (+18.7%) failing to counteract the payday-related headwinds. Recommend investigating the timing of dunning campaigns relative to payday cycles and analyzing post-PC2 drop-off points to identify actionable interventions.

### FR (Rank #2 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 7,645 | 69.97% | - | 92.95% | - | 12.07% | - | 42.27% | - |
| 2026-W15 | Pre-Payday | 5,294 | 61.64% | ↓-11.9% | 94.49% | →+1.7% | 12.09% | →+0.2% | 45.11% | ↑+6.7% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### DE (Rank #3 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 4,511 | 74.73% | - | 96.44% | - | 15.89% | - | 38.13% | - |
| 2026-W15 | Pre-Payday | 3,162 | 67.33% | ↓-9.9% | 97.33% | →+0.9% | 17.19% | ↑+8.2% | 42.0% | ↑+10.1% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### SE (Rank #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 808 | 71.66% | - | 96.24% | - | 9.16% | - | 40.1% | - |
| 2026-W15 | Pre-Payday | 690 | 61.16% | ↓-14.7% | 95.19% | →-1.1% | 10.87% | ↑+18.7% | 41.77% | ↑+4.2% |

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
| GB | ↓-12.3% | →+1.1% | →+1.8% | ↑+5.9% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| FR | ↓-11.9% | →+1.7% | →+0.2% | ↑+6.7% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| DE | ↓-9.9% | →+0.9% | ↑+8.2% | ↑+10.1% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| SE | ↓-14.7% | →-1.1% | ↑+18.7% | ↑+4.2% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| GB | 8,721 | 64.99% | 6,301 | 57.02% | -27.7% | High |
| FR | 7,645 | 69.97% | 5,294 | 61.64% | -30.8% | High |
| AU | 5,849 | 66.10% | 5,021 | 64.73% | -14.2% | High |
| DE | 4,511 | 74.73% | 3,162 | 67.33% | -29.9% | High |
| BE | 3,221 | 90.50% | 1,995 | 87.57% | -38.1% | High |
| NZ | 1,302 | 61.29% | 1,132 | 69.52% | -13.1% | High |
| DK | 1,229 | 76.00% | 557 | 67.68% | -54.7% | High |
| IE | 1,149 | 65.88% | 877 | 61.80% | -23.7% | High |
| NO | 943 | 79.22% | 1,269 | 82.19% | 34.6% | High |
| SE | 808 | 71.66% | 690 | 61.16% | -14.6% | High |

---


---

*Report: 2026-04-17*
