# Dunning Investigation: HF-INTL 2026-W17

**Metric:** Dunning Ship Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 66.70% → 68.33% (+1.63pp)  
**Volume:** 31,786 eligible orders  
**Payday Phase:** Payday → Post-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate improved from 66.70% to 68.33% (+1.63pp) in W17, driven primarily by strong performance in GB (+8.3%) and SE (+11.2%), partially offset by a significant decline in NO (-9.6%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.76% → 94.06% | +0.3% | ✅ |
| Discount % | 13.92% → 13.22% | -5.0% | ✅ |
| PC2 | 43.48% → 45.94% | +5.7% | ✅ |
| Ship Rate | 66.70% → 68.33% | +2.4% | ✅ |

**Key Findings:**
- **GB** drove the largest absolute contribution with +8.3% Ship Rate improvement on 8,001 orders, primarily due to a 7.8% reduction in Discount % while Pre-Dunning AR remained flat
- **NO** experienced a sharp -9.6% Ship Rate decline despite Pre-Dunning AR improving +4.5%, caused by a significant +26.1% increase in Discount % and a -37.7% volume reduction indicating potential mix shift
- **SE** showed the strongest relative improvement (+11.2% Ship Rate) driven by lower discounting (-6.0%) and improved PC2 (+3.5%)
- **AU** contributed steady gains (+2.6% Ship Rate) with notable PC2 improvement (+10.4%) offsetting modest discount reductions
- Mix shift detected: NO volume dropped -37.7% while BE (+29.9%) and SE (+28.3%) saw significant volume increases, shifting mix toward lower-performing but improving markets

**Action:** **Monitor** - Overall trend is positive with all funnel metrics improving. Investigate NO's elevated discount rate (+26.1%) to understand if this is intentional strategy or requires correction.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 30,246 | 66.70% | - | 93.76% | - | 13.92% | - | 43.48% | - |
| 2026-W17 | Post-Payday | 31,786 | 68.33% | →+2.4% | 94.06% | →+0.3% | 13.22% | ↓-5.0% | 45.94% | ↑+5.7% |

---

## L1: Country-Level Analysis

### GB (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 7,688 | 59.25% | - | 93.92% | - | 17.78% | - | 47.25% | - |
| 2026-W17 | Post-Payday | 8,001 | 64.19% | ↑+8.3% | 93.91% | →-0.0% | 16.4% | ↓-7.8% | 47.66% | →+0.9% |

**Analysis:** The HF-INTL cluster showed healthy improvement in Dunning Ship Rate during the Post-Payday phase, with 3 of 4 key countries contributing positive gains through reduced discounting and improved PC2 rates. NO represents an isolated concern requiring attention due to aggressive discounting eroding ship rate gains despite better pre-dunning approval. The overall trajectory is positive and warrants continued monitoring rather than immediate intervention.

### NO (Rank #2 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 2,016 | 88.19% | - | 89.15% | - | 6.06% | - | 39.19% | - |
| 2026-W17 | Post-Payday | 1,256 | 79.70% | ↓-9.6% | 93.19% | ↑+4.5% | 7.64% | ↑+26.1% | 39.27% | →+0.2% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### AU (Rank #3 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 5,168 | 69.25% | - | 91.18% | - | 12.47% | - | 46.64% | - |
| 2026-W17 | Post-Payday | 4,857 | 71.03% | ↑+2.6% | 92.12% | →+1.0% | 12.01% | ↓-3.7% | 51.49% | ↑+10.4% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### SE (Rank #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 905 | 65.52% | - | 96.32% | - | 8.9% | - | 40.93% | - |
| 2026-W17 | Post-Payday | 1,161 | 72.87% | ↑+11.2% | 95.59% | →-0.8% | 8.37% | ↓-6.0% | 42.35% | ↑+3.5% |

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
| GB | ↑+8.3% | →-0.0% | ↓-7.8% | →+0.9% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| NO | ↓-9.6% | ↑+4.5% | ↑+26.1% | →+0.2% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| AU | ↑+2.6% | →+1.0% | ↓-3.7% | ↑+10.4% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| SE | ↑+11.2% | →-0.8% | ↓-6.0% | ↑+3.5% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| GB | 7,688 | 59.25% | 8,001 | 64.19% | 4.1% | High |
| FR | 5,314 | 60.61% | 5,926 | 61.51% | 11.5% | High |
| AU | 5,168 | 69.25% | 4,857 | 71.03% | -6.0% | High |
| DE | 3,453 | 65.71% | 3,745 | 67.74% | 8.5% | High |
| NO | 2,016 | 88.19% | 1,256 | 79.70% | -37.7% | High |
| BE | 1,688 | 86.79% | 2,192 | 88.78% | 29.9% | High |
| NZ | 1,268 | 60.25% | 1,340 | 59.10% | 5.7% | High |
| IE | 947 | 66.00% | 1,104 | 64.86% | 16.6% | High |
| SE | 905 | 65.52% | 1,161 | 72.87% | 28.3% | High |
| DK | 734 | 71.25% | 912 | 71.05% | 24.3% | High |

---


---

*Report: 2026-04-28*
