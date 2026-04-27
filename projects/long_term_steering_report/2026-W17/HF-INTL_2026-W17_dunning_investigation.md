# Dunning Investigation: HF-INTL 2026-W17

**Metric:** Dunning Ship Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 66.70% → 68.46% (+1.76pp)  
**Volume:** 31,916 eligible orders  
**Payday Phase:** Payday → Post-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate improved from 66.70% to 68.46% (+1.76pp) in W17, with volume increasing 5.5% (30,248 → 31,916 orders) during the transition from Payday to Post-Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.76% → 94.06% | +0.30pp | ✅ |
| Discount % | 13.92% → 13.20% | -0.72pp | ✅ |
| PC2 | 43.51% → 45.95% | +2.44pp | ✅ |
| Ship Rate | 66.70% → 68.46% | +1.76pp | ✅ |

**Key Findings:**
- **GB** drove the largest absolute contribution with +4.98pp Ship Rate improvement (59.25% → 64.23%) on highest volume (8,013 orders), primarily driven by a 7.8% reduction in Discount %
- **NO** showed significant deterioration (-8.48pp Ship Rate) despite improved Pre-Dunning AR (+4.5%), caused by a sharp 25.9% increase in Discount % and 37.6% volume decline
- **SE** achieved the strongest relative improvement (+11.2% Ship Rate change) with reduced discounting (-5.7%) and improved PC2 (+3.5%)
- **AU** benefited from a substantial PC2 increase (+10.4%) contributing to +1.78pp Ship Rate gain
- **Mix shift detected:** NO (high-performing at 88.19%) saw 37.6% volume decline while lower-performing markets (GB, FR, BE, SE) gained share

**Action:** Monitor — Overall improvement is healthy and aligned with Post-Payday phase expectations. Investigate NO's discount strategy increase to prevent further erosion in a historically high-performing market.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 30,248 | 66.70% | - | 93.76% | - | 13.92% | - | 43.51% | - |
| 2026-W17 | Post-Payday | 31,916 | 68.46% | ↑+2.6% | 94.06% | →+0.3% | 13.2% | ↓-5.2% | 45.95% | ↑+5.6% |

---

## L1: Country-Level Analysis

### GB (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 7,688 | 59.25% | - | 93.92% | - | 17.78% | - | 47.27% | - |
| 2026-W17 | Post-Payday | 8,013 | 64.23% | ↑+8.4% | 93.91% | →-0.0% | 16.39% | ↓-7.8% | 47.67% | →+0.8% |

**Analysis:** The HF-INTL cluster showed healthy Ship Rate improvement in W17, driven primarily by reduced discounting across major markets (GB, AU, SE) and improved payment conversion (PC2). The Post-Payday phase transition delivered expected benefits in most countries, though NO requires attention due to its counter-trend performance linked to aggressive discounting. The volume mix shift away from high-performing NO toward lower-performing markets partially masked stronger underlying country-level improvements.

### NO (Rank #2 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 2,016 | 88.19% | - | 89.15% | - | 6.06% | - | 39.21% | - |
| 2026-W17 | Post-Payday | 1,257 | 79.71% | ↓-9.6% | 93.19% | ↑+4.5% | 7.63% | ↑+25.9% | 39.26% | →+0.1% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### AU (Rank #3 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 5,168 | 69.25% | - | 91.18% | - | 12.47% | - | 46.63% | - |
| 2026-W17 | Post-Payday | 4,857 | 71.03% | ↑+2.6% | 92.12% | →+1.0% | 12.01% | ↓-3.7% | 51.49% | ↑+10.4% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### SE (Rank #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 905 | 65.52% | - | 96.32% | - | 8.9% | - | 40.93% | - |
| 2026-W17 | Post-Payday | 1,162 | 72.89% | ↑+11.2% | 95.59% | →-0.8% | 8.39% | ↓-5.7% | 42.35% | ↑+3.5% |

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
| GB | ↑+8.4% | →-0.0% | ↓-7.8% | →+0.8% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| NO | ↓-9.6% | ↑+4.5% | ↑+25.9% | →+0.1% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| AU | ↑+2.6% | →+1.0% | ↓-3.7% | ↑+10.4% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| SE | ↑+11.2% | →-0.8% | ↓-5.7% | ↑+3.5% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| GB | 7,688 | 59.25% | 8,013 | 64.23% | 4.2% | High |
| FR | 5,314 | 60.61% | 6,007 | 62.03% | 13.0% | High |
| AU | 5,168 | 69.25% | 4,857 | 71.03% | -6.0% | High |
| DE | 3,454 | 65.72% | 3,757 | 67.85% | 8.8% | High |
| NO | 2,016 | 88.19% | 1,257 | 79.71% | -37.6% | High |
| BE | 1,689 | 86.80% | 2,204 | 88.84% | 30.5% | High |
| NZ | 1,268 | 60.25% | 1,340 | 59.10% | 5.7% | High |
| IE | 947 | 66.00% | 1,105 | 64.89% | 16.7% | High |
| SE | 905 | 65.52% | 1,162 | 72.89% | 28.4% | High |
| DK | 734 | 71.25% | 915 | 71.15% | 24.7% | High |

---


---

*Report: 2026-04-27*
