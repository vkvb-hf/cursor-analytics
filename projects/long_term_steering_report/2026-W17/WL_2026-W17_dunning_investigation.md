# Dunning Investigation: WL 2026-W17

**Metric:** Dunning Ship Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 31.81% → 31.30% (-0.51pp)  
**Volume:** 8,164 eligible orders  
**Payday Phase:** Payday → Post-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined from 31.81% to 31.30% (-0.51pp) week-over-week, driven primarily by mix shift away from high-performing countries during the Post-Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 89.87% → 90.11% | +0.24pp | ✅ |
| Discount % | 18.08% → 16.59% | -1.49pp | ✅ |
| PC2 | 32.34% → 39.93% | +7.59pp | ✅ |
| Ship Rate | 31.81% → 31.30% | -0.51pp | ⚠️ |

**Key Findings:**
- **Simpson's Paradox detected:** Individual country performance improved (ER +9.1%, GN +13.6%), yet overall Ship Rate declined due to mix shift
- **AO volume dropped -10.1%** (1,134 → 1,020 orders) - this high-SR tier country (67.65%) losing share significantly impacted overall performance
- **ER gained volume (+5.1%)** but operates at a low-SR tier (27.38%), diluting the aggregate rate
- **Discount reduction drove improvements** in ER (-11.1% discount) and GN (-13.5% discount), correlating with their Ship Rate gains
- **AO decline unexplained by standard metrics:** Pre-Dunning AR improved (+1.8%), Discount stable (+0.3%), PC2 improved (+20.5%), yet Ship Rate fell -4.2% - suggests Post-Payday customer liquidity constraints

**Action:** Monitor - The decline is primarily compositional (mix shift) rather than operational. Individual country fundamentals are healthy. Track AO volume recovery and investigate potential payday-related payment timing issues in AO specifically.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 8,314 | 31.81% | - | 89.87% | - | 18.08% | - | 32.34% | - |
| 2026-W17 | Post-Payday | 8,164 | 31.30% | →-1.6% | 90.11% | →+0.3% | 16.59% | ↓-8.2% | 39.93% | ↑+23.5% |

---

## L1: Country-Level Analysis

### ER (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 2,519 | 25.09% | - | 90.18% | - | 17.38% | - | 38.81% | - |
| 2026-W17 | Post-Payday | 2,648 | 27.38% | ↑+9.1% | 90.18% | →+0.0% | 15.45% | ↓-11.1% | 43.69% | ↑+12.6% |

**Analysis:** The -0.51pp decline in Dunning Ship Rate is attributable to unfavorable mix shift rather than deteriorating conversion fundamentals. High-performing AO experienced a -10.1% volume reduction while low-performing ER gained +5.1% share, creating a Simpson's Paradox where improving country-level metrics yielded a declining aggregate. The transition from Payday to Post-Payday phase likely contributed to reduced payment capacity in AO, warranting continued monitoring of volume distribution patterns.

### AO (Rank #2 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 1,134 | 70.63% | - | 87.79% | - | 14.45% | - | 37.59% | - |
| 2026-W17 | Post-Payday | 1,020 | 67.65% | ↓-4.2% | 89.40% | →+1.8% | 14.5% | →+0.3% | 45.3% | ↑+20.5% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### GN (Rank #3 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 508 | 36.81% | - | 94.19% | - | 22.81% | - | 50.64% | - |
| 2026-W17 | Post-Payday | 512 | 41.80% | ↑+13.6% | 94.36% | →+0.2% | 19.73% | ↓-13.5% | 50.32% | →-0.6% |

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
| ER | ↑+9.1% | →+0.0% | ↓-11.1% | ↑+12.6% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| AO | ↓-4.2% | →+1.8% | →+0.3% | ↑+20.5% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| GN | ↑+13.6% | →+0.2% | ↓-13.5% | →-0.6% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,519 | 25.09% | 2,648 | 27.38% | 5.1% | Low |
| CK | 1,658 | 43.91% | 1,501 | 43.30% | -9.5% | Medium |
| AO | 1,134 | 70.63% | 1,020 | 67.65% | -10.1% | High |
| MR | 1,116 | 0.09% | 1,138 | 0.18% | 2.0% | Low |
| CG | 741 | 24.43% | 750 | 23.20% | 1.2% | Low |
| KN | 638 | 18.03% | 595 | 16.81% | -6.7% | Low |
| GN | 508 | 36.81% | 512 | 41.80% | 0.8% | Medium |

---


---

*Report: 2026-04-28*
