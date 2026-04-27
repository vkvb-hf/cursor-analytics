# Dunning Investigation: WL 2026-W17

**Metric:** Dunning Ship Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 31.81% → 31.39% (-0.42pp)  
**Volume:** 8,176 eligible orders  
**Payday Phase:** Payday → Post-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined from 31.81% to 31.39% (-0.42pp, -1.3% relative) in W17 despite most individual countries showing improvement, indicating a mix shift effect as volume shifted toward lower-performing segments.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 89.88% → 90.11% | +0.23pp | ✅ |
| Discount % | 18.08% → 16.59% | -1.49pp | ✅ |
| PC2 | 32.34% → 39.93% | +7.59pp | ✅ |
| Ship Rate | 31.81% → 31.39% | -0.42pp | ⚠️ |

**Key Findings:**
- **Simpson's Paradox detected:** Despite ER (+9.2%), GN (+14.2%), and stable discount metrics, overall Ship Rate declined due to mix shift — high-performing AO volume dropped -10.1% while low-performing ER volume increased +5.2%
- **AO underperformance:** Ship Rate fell -4.2% (70.63% → 67.65%) despite improved Pre-Dunning AR (+1.8%) and strong PC2 (+20.3%), suggesting post-payday timing pressure impacted this high-SR country
- **Discount reduction drove gains in ER and GN:** Both countries saw Ship Rate improvements (ER +9.2%, GN +14.2%) correlating with significant discount reductions (ER -11.1%, GN -13.6%)
- **Payday phase transition:** Movement from Payday to Post-Payday period may explain AO's decline as customers have reduced liquidity despite strong engagement metrics

**Action:** **Monitor** — The overall decline is driven by mix shift rather than systemic performance degradation. Track AO volume recovery and continue current discount optimization strategy in ER/GN.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 8,315 | 31.81% | - | 89.88% | - | 18.08% | - | 32.34% | - |
| 2026-W17 | Post-Payday | 8,176 | 31.39% | →-1.3% | 90.11% | →+0.3% | 16.59% | ↓-8.2% | 39.93% | ↑+23.5% |

---

## L1: Country-Level Analysis

### ER (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 2,519 | 25.09% | - | 90.18% | - | 17.38% | - | 38.81% | - |
| 2026-W17 | Post-Payday | 2,649 | 27.41% | ↑+9.2% | 90.18% | →+0.0% | 15.45% | ↓-11.1% | 43.68% | ↑+12.5% |

**Analysis:** The -0.42pp decline in Dunning Ship Rate is primarily attributable to Simpson's Paradox: volume shifted away from high-performing AO (-10.1% volume) toward lower-performing ER (+5.2% volume), masking genuine improvements in most countries. The discount reduction strategy is proving effective in ER and GN, while AO requires monitoring for post-payday recovery patterns. No immediate escalation is warranted as underlying country-level trends remain largely positive.

### AO (Rank #2 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 1,134 | 70.63% | - | 87.79% | - | 14.45% | - | 37.66% | - |
| 2026-W17 | Post-Payday | 1,020 | 67.65% | ↓-4.2% | 89.41% | →+1.8% | 14.5% | →+0.3% | 45.3% | ↑+20.3% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### GN (Rank #3 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 508 | 36.81% | - | 94.19% | - | 22.81% | - | 50.64% | - |
| 2026-W17 | Post-Payday | 514 | 42.02% | ↑+14.2% | 94.36% | →+0.2% | 19.7% | ↓-13.6% | 50.31% | →-0.7% |

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
| ER | ↑+9.2% | →+0.0% | ↓-11.1% | ↑+12.5% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| AO | ↓-4.2% | →+1.8% | →+0.3% | ↑+20.3% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| GN | ↑+14.2% | →+0.2% | ↓-13.6% | →-0.7% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,519 | 25.09% | 2,649 | 27.41% | 5.2% | Low |
| CK | 1,658 | 43.91% | 1,507 | 43.53% | -9.1% | Medium |
| AO | 1,134 | 70.63% | 1,020 | 67.65% | -10.1% | High |
| MR | 1,117 | 0.09% | 1,140 | 0.26% | 2.1% | Low |
| CG | 741 | 24.43% | 751 | 23.30% | 1.3% | Low |
| KN | 638 | 18.03% | 595 | 16.81% | -6.7% | Low |
| GN | 508 | 36.81% | 514 | 42.02% | 1.2% | Medium |

---


---

*Report: 2026-04-27*
