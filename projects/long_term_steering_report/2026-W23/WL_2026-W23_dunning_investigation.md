# Dunning Investigation: WL 2026-W23

**Metric:** Dunning Ship Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 30.82% → 31.38% (+0.56pp)  
**Volume:** 7,528 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate improved from 30.82% to 31.38% (+0.56pp) in W23, driven primarily by strong performance in GN despite declines in ER and AO.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 89.42% → 89.86% | +0.44pp | ✅ |
| Discount % | 17.39% → 19.32% | +1.93pp | ⚠️ |
| PC2 | 51.44% → 38.95% | -12.49pp | ⚠️ |
| Ship Rate | 30.82% → 31.38% | +0.56pp | ✅ |

**Key Findings:**
- **GN drove cluster improvement:** Ship Rate surged +20.7% (38.48% → 46.45%) with lower discounts (-7.7%) and stable PC2, indicating genuine conversion improvement
- **ER underperformed significantly:** Despite being the largest market, Ship Rate declined -9.9% (29.59% → 26.66%) driven by higher discounts (+11.6%) and increased PC2 (+16.0%)
- **AO volume grew but SR declined:** Volume increased +15.2% while Ship Rate dropped -3.2%, with discounts up +9.5% and PC2 up +24.4%
- **Simpson's Paradox detected:** AO (high-SR tier) volume expansion (+15.2%) offset individual country declines, masking underlying performance issues
- **Payday phase transition:** Mid-Cycle → Pre-Payday shift correlates with increased discount usage cluster-wide (+11.1%)

**Action:** **Investigate** — The cluster-level improvement masks concerning trends in ER and AO. Recommend deep-dive into ER's -9.9% decline and evaluate if increased discounting is sustainable.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W22 | Mid-Cycle | 7,537 | 30.82% | - | 89.42% | - | 17.39% | - | 51.44% | - |
| 2026-W23 | Pre-Payday | 7,528 | 31.38% | →+1.8% | 89.86% | →+0.5% | 19.32% | ↑+11.1% | 38.95% | ↓-24.3% |

---

## L1: Country-Level Analysis

### ER (Rank #1 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W22 | Mid-Cycle | 2,001 | 29.59% | - | 89.48% | - | 16.39% | - | 37.32% | - |
| 2026-W23 | Pre-Payday | 1,977 | 26.66% | ↓-9.9% | 89.87% | →+0.4% | 18.29% | ↑+11.6% | 43.28% | ↑+16.0% |

**Analysis:** The +0.56pp Ship Rate improvement in W23 is largely compositional, driven by GN's exceptional +20.7% gain and favorable mix shift toward high-SR market AO, rather than broad-based improvement. ER and AO both showed declining conversion despite increased discount utilization, suggesting the Pre-Payday phase may be masking underlying payment capacity issues. Continued monitoring of ER performance and discount efficiency is recommended heading into W24.

### GN (Rank #2 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W22 | Mid-Cycle | 382 | 38.48% | - | 94.60% | - | 21.57% | - | 50.01% | - |
| 2026-W23 | Pre-Payday | 394 | 46.45% | ↑+20.7% | 95.30% | →+0.7% | 19.91% | ↓-7.7% | 50.38% | →+0.7% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### AO (Rank #3 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W22 | Mid-Cycle | 1,007 | 69.12% | - | 88.85% | - | 14.49% | - | 35.45% | - |
| 2026-W23 | Pre-Payday | 1,160 | 66.90% | ↓-3.2% | 88.10% | →-0.8% | 15.86% | ↑+9.5% | 44.11% | ↑+24.4% |

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
| ER | ↓-9.9% | →+0.4% | ↑+11.6% | ↑+16.0% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| GN | ↑+20.7% | →+0.7% | ↓-7.7% | →+0.7% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| AO | ↓-3.2% | →-0.8% | ↑+9.5% | ↑+24.4% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,001 | 29.59% | 1,977 | 26.66% | -1.2% | Low |
| CK | 1,549 | 38.54% | 1,652 | 38.38% | 6.6% | Medium |
| MR | 1,178 | 0.25% | 1,080 | 0.56% | -8.3% | Low |
| AO | 1,007 | 69.12% | 1,160 | 66.90% | 15.2% | High |
| KN | 758 | 15.96% | 660 | 15.00% | -12.9% | Low |
| CG | 662 | 25.23% | 605 | 22.64% | -8.6% | Low |
| GN | 382 | 38.48% | 394 | 46.45% | 3.1% | Medium |

---


---

*Report: 2026-06-09*
