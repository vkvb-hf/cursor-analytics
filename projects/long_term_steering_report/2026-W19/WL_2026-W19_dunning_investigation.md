# Dunning Investigation: WL 2026-W19

**Metric:** Dunning Ship Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 31.06% → 32.96% (+1.90pp)  
**Volume:** 7,749 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate improved from 31.06% to 32.96% (+1.90pp, +6.1% relative) in W19 as the payday phase shifted from Mid-Cycle to Pre-Payday, with significant variation across countries.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 89.52% → 89.81% | +0.29pp | ✅ Stable |
| Discount % | 16.08% → 16.23% | +0.15pp | ✅ Stable |
| PC2 | 5.88% → 40.16% | +34.28pp | ⚠️ Major Increase |
| Ship Rate | 31.06% → 32.96% | +1.90pp | ✅ Improved |

**Key Findings:**
- **PC2 surged dramatically (+583.0%)** from 5.88% to 40.16%, representing the most significant metric shift and a key driver of improved ship rates at the cluster level
- **CG showed strongest improvement** (+18.4% relative in Ship Rate) despite stable metrics, suggesting payday phase timing as the primary driver
- **ER underperformed** with Ship Rate declining -7.4% despite being the largest market, driven by increased Discount % (+7.3%) which typically suppresses ship rates
- **GN experienced the largest decline** (-11.6% in Ship Rate) despite favorable Pre-Dunning AR (+0.9%) and lower Discount % (-2.8%), indicating unexplained factors
- **Mix shift detected:** GN volume dropped -23.9% while high-performing AO increased +7.8%, contributing positively to overall cluster performance (Simpson's Paradox consideration)

**Action:** Monitor — Overall improvement is positive but investigate ER's discount increase and GN's unexplained decline for potential intervention opportunities.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W18 | Mid-Cycle | 8,498 | 31.06% | - | 89.52% | - | 16.08% | - | 5.88% | - |
| 2026-W19 | Pre-Payday | 7,749 | 32.96% | ↑+6.1% | 89.81% | →+0.3% | 16.23% | →+0.9% | 40.16% | ↑+583.0% |

---

## L1: Country-Level Analysis

### ER (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W18 | Mid-Cycle | 2,528 | 26.31% | - | 89.71% | - | 15.2% | - | 41.68% | - |
| 2026-W19 | Pre-Payday | 2,359 | 24.37% | ↓-7.4% | 89.34% | →-0.4% | 16.31% | ↑+7.3% | 43.43% | ↑+4.2% |

**Analysis:** The Dunning Ship Rate improvement of +1.90pp is primarily driven by the payday phase transition from Mid-Cycle to Pre-Payday and a dramatic increase in PC2 (+34.28pp). While CK and CG contributed positively to the improvement, attention should be given to ER where increased discounting appears to be suppressing ship rates, and GN where significant volume and rate declines warrant further investigation despite favorable underlying metrics.

### CK (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W18 | Mid-Cycle | 1,587 | 46.38% | - | 93.13% | - | 26.56% | - | 46.85% | - |
| 2026-W19 | Pre-Payday | 1,491 | 48.63% | ↑+4.9% | 93.00% | →-0.1% | 24.97% | ↓-6.0% | 47.54% | →+1.5% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### CG (Rank #3 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W18 | Mid-Cycle | 786 | 19.47% | - | 96.79% | - | 15.77% | - | 49.31% | - |
| 2026-W19 | Pre-Payday | 729 | 23.05% | ↑+18.4% | 96.62% | →-0.2% | 15.82% | →+0.3% | 48.41% | →-1.8% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### GN (Rank #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W18 | Mid-Cycle | 535 | 44.49% | - | 94.09% | - | 19.4% | - | 49.74% | - |
| 2026-W19 | Pre-Payday | 407 | 39.31% | ↓-11.6% | 94.92% | →+0.9% | 18.86% | ↓-2.8% | 50.45% | →+1.4% |

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
| ER | ↓-7.4% | →-0.4% | ↑+7.3% | ↑+4.2% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| CK | ↑+4.9% | →-0.1% | ↓-6.0% | →+1.5% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| CG | ↑+18.4% | →-0.2% | →+0.3% | →-1.8% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| GN | ↓-11.6% | →+0.9% | ↓-2.8% | →+1.4% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,528 | 26.31% | 2,359 | 24.37% | -6.7% | Low |
| CK | 1,587 | 46.38% | 1,491 | 48.63% | -6.0% | Medium |
| MR | 1,261 | 0.16% | 979 | 0.31% | -22.4% | Low |
| AO | 1,088 | 68.11% | 1,173 | 70.08% | 7.8% | High |
| CG | 786 | 19.47% | 729 | 23.05% | -7.3% | Low |
| KN | 713 | 14.59% | 611 | 16.53% | -14.3% | Low |
| GN | 535 | 44.49% | 407 | 39.31% | -23.9% | Medium |

---


---

*Report: 2026-05-12*
