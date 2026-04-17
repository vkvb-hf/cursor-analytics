# Dunning Investigation: WL 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 28.34% → 31.07% (+2.73pp)  
**Volume:** 7,709 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate improved from 28.34% to 31.07% (+2.73pp) in W15, despite all three major contributing countries (AO, ER, GN) experiencing individual Ship Rate declines—indicating a Simpson's Paradox driven by mix shift toward higher-performing segments.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 89.14% → 90.00% | +0.86pp | ✅ |
| Discount % | 17.63% → 17.92% | +0.29pp | ⚠️ |
| PC2 | 37.98% → 39.89% | +1.91pp | ✅ |
| Ship Rate | 28.34% → 31.07% | +2.73pp | ✅ |

**Key Findings:**
- **Simpson's Paradox confirmed:** Cluster-level Ship Rate increased +2.73pp while AO (-8.6%), ER (-9.1%), and GN (-22.0%) all declined individually
- **AO volume surge (+123.6%)** from 496 to 1,109 orders shifted mix toward this high-SR tier country (66.37% SR), masking country-level declines
- **GN experienced the steepest SR decline (-22.0%)** with a +4.3% increase in Discount % suggesting aggressive discounting failed to convert
- **AO Discount % spiked +26.2%** (13.65% → 17.22%) correlating with its SR decline despite strong PC2 improvement (+21.2%)
- **Payday phase transition** (Mid-Cycle → Pre-Payday) coincided with improved Pre-Dunning AR across all countries (+1.0% to +2.2%)

**Action:** **Monitor** — The cluster improvement is mechanically driven by favorable mix shift rather than operational gains. Track whether AO's elevated volume and discount levels are sustainable, and investigate GN's -22.0% SR drop if it persists into W16.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 8,041 | 28.34% | - | 89.14% | - | 17.63% | - | 37.98% | - |
| 2026-W15 | Pre-Payday | 7,709 | 31.07% | ↑+9.6% | 90.00% | →+1.0% | 17.92% | →+1.6% | 39.89% | ↑+5.0% |

---

## L1: Country-Level Analysis

### AO (Rank #1 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 496 | 72.58% | - | 85.21% | - | 13.65% | - | 36.81% | - |
| 2026-W15 | Pre-Payday | 1,109 | 66.37% | ↓-8.6% | 87.06% | →+2.2% | 17.22% | ↑+26.2% | 44.6% | ↑+21.2% |

**Analysis:** The +2.73pp improvement in Dunning Ship Rate is primarily attributable to a significant volume shift toward AO (+123.6% volume increase), a high-performing country that elevated the weighted average despite declining at the individual level. Underlying country performance deteriorated across all top contributors, with aggressive discounting (particularly AO's +26.2% increase) failing to prevent SR erosion. Continued monitoring is warranted to determine if this mix-driven improvement is sustainable or if the country-level declines signal emerging collection challenges.

### ER (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 2,556 | 26.60% | - | 89.22% | - | 19.48% | - | 40.95% | - |
| 2026-W15 | Pre-Payday | 2,345 | 24.18% | ↓-9.1% | 90.32% | →+1.2% | 18.63% | ↓-4.4% | 43.65% | ↑+6.6% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### GN (Rank #3 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 632 | 37.03% | - | 92.33% | - | 22.96% | - | 51.25% | - |
| 2026-W15 | Pre-Payday | 495 | 28.89% | ↓-22.0% | 93.32% | →+1.1% | 23.95% | ↑+4.3% | 50.54% | →-1.4% |

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
| AO | ↓-8.6% | →+2.2% | ↑+26.2% | ↑+21.2% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| ER | ↓-9.1% | →+1.2% | ↓-4.4% | ↑+6.6% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| GN | ↓-22.0% | →+1.1% | ↑+4.3% | →-1.4% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,556 | 26.60% | 2,345 | 24.18% | -8.3% | Low |
| CK | 1,491 | 47.75% | 1,439 | 47.05% | -3.5% | Medium |
| MR | 1,420 | 0.00% | 1,064 | 0.19% | -25.1% | Low |
| CG | 777 | 24.71% | 732 | 23.63% | -5.8% | Low |
| KN | 669 | 15.10% | 525 | 18.48% | -21.5% | Low |
| GN | 632 | 37.03% | 495 | 28.89% | -21.7% | Medium |
| AO | 496 | 72.58% | 1,109 | 66.37% | 123.6% | High |

---


---

*Report: 2026-04-17*
