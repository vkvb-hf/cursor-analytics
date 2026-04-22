# Dunning Investigation: WL 2026-W16

**Metric:** Dunning Ship Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 31.07% → 31.81% (+0.74pp)  
**Volume:** 8,319 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate improved from 31.07% to 31.81% (+0.74pp, +2.4% relative) in W16, driven by strong gains in AO and GN that offset a decline in CK, during the transition from Pre-Payday to Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 90.00% → 89.88% | -0.1% | ✅ Stable |
| Discount % | 17.93% → 18.07% | +0.8% | ✅ Stable |
| PC2 | 39.91% → 40.27% | +0.9% | ✅ Stable |
| Ship Rate | 31.07% → 31.81% | +2.4% | ✅ Improved |

**Key Findings:**
- **GN** showed the strongest improvement with Ship Rate up +27.4% (28.89% → 36.81%), likely driven by slightly improved Pre-Dunning AR (+0.9%) and reduced Discount % (-4.8%)
- **AO** improved Ship Rate by +6.4% (66.37% → 70.63%), correlating with a significant Discount % reduction of -16.1% during Payday phase
- **CK** declined -6.6% in Ship Rate (47.04% → 43.92%) despite being the #1 contributor by volume, with Discount % increasing +14.9% as the primary driver
- **Mix shift detected:** KN volume grew +21.5% and CK grew +15.5%, both in lower SR tiers, partially masking underlying improvements
- Payday phase transition appears beneficial for AO and GN but negatively impacted CK performance

**Action:** **Monitor** - Overall metric improved modestly. Investigate CK's elevated discount rates to understand if this is a deliberate strategy or requires correction.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 7,702 | 31.07% | - | 90.00% | - | 17.93% | - | 39.91% | - |
| 2026-W16 | Payday | 8,319 | 31.81% | →+2.4% | 89.88% | →-0.1% | 18.07% | →+0.8% | 40.27% | →+0.9% |

---

## L1: Country-Level Analysis

### CK (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 1,437 | 47.04% | - | 93.91% | - | 25.79% | - | 47.45% | - |
| 2026-W16 | Payday | 1,660 | 43.92% | ↓-6.6% | 93.32% | →-0.6% | 29.63% | ↑+14.9% | 47.3% | →-0.3% |

**Analysis:** The Dunning Ship Rate showed healthy improvement of +0.74pp in W16, with the Payday phase positively influencing most markets. The divergent performance between CK (declining due to higher discounts) and AO/GN (improving with lower discounts) suggests discount strategy optimization could yield further gains. Continued monitoring of CK's discount levels and their impact on ship rate is recommended for the coming weeks.

### AO (Rank #2 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 1,109 | 66.37% | - | 87.06% | - | 17.22% | - | 44.6% | - |
| 2026-W16 | Payday | 1,134 | 70.63% | ↑+6.4% | 87.79% | →+0.8% | 14.45% | ↓-16.1% | 43.94% | →-1.5% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### GN (Rank #3 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 495 | 28.89% | - | 93.32% | - | 23.95% | - | 50.54% | - |
| 2026-W16 | Payday | 508 | 36.81% | ↑+27.4% | 94.19% | →+0.9% | 22.81% | ↓-4.8% | 50.65% | →+0.2% |

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
| CK | ↓-6.6% | →-0.6% | ↑+14.9% | →-0.3% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| AO | ↑+6.4% | →+0.8% | ↓-16.1% | →-1.5% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| GN | ↑+27.4% | →+0.9% | ↓-4.8% | →+0.2% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,344 | 24.15% | 2,521 | 25.07% | 7.6% | Low |
| CK | 1,437 | 47.04% | 1,660 | 43.92% | 15.5% | Medium |
| AO | 1,109 | 66.37% | 1,134 | 70.63% | 2.3% | High |
| MR | 1,061 | 0.19% | 1,117 | 0.09% | 5.3% | Low |
| CG | 731 | 23.67% | 741 | 24.43% | 1.4% | Low |
| KN | 525 | 18.48% | 638 | 18.03% | 21.5% | Low |
| GN | 495 | 28.89% | 508 | 36.81% | 2.6% | Low |

---


---

*Report: 2026-04-22*
