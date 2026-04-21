# Dunning Investigation: RTE 2026-W16

**Metric:** Dunning Ship Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 42.62% → 43.92% (+1.30pp)  
**Volume:** 20,623 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

**Overall:** Dunning Ship Rate improved from 42.62% to 43.92% (+1.30pp) during the transition from Pre-Payday to Payday phase, driven primarily by strong PC2 gains and reduced discount rates across most countries.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | Stable intake quality | -0.1% | ✅ |
| Discount % | Lower discounts → better SR | -4.1% | ✅ |
| PC2 | Payment conversion improved | +15.5% | ✅ |
| Ship Rate | Final outcome | +3.1% | ✅ |

**Key Findings:**
- **PC2 surge across markets:** Cluster-wide PC2 increased +15.5% (41.56% → 48.01%), with YE showing exceptional +42.8% improvement and FJ contributing +13.6%, indicating stronger payment conversion during Payday phase
- **Discount optimization working:** Average discount rate decreased -4.1% (17.5% → 16.79%), with TV showing the largest reduction at -14.1% and YE at -7.2%, correlating with improved ship rates
- **TV showed dramatic recovery:** Ship Rate surged +109.5% (12.50% → 26.19%) despite being a low-volume market, primarily driven by the -14.1% discount reduction and slight AR improvement (+1.5%)
- **TK is the outlier concern:** Despite Payday phase and -5.5% discount reduction, TK saw Ship Rate decline -11.7% (32.00% → 28.26%) alongside a -1.8% Pre-Dunning AR drop, warranting investigation
- **Volume growth concentrated in FJ and CF:** FJ grew +5.5% and CF grew +20.3%, both maintaining or improving ship rates, indicating healthy scaling

**Action:** **Monitor** - The improvement is consistent with expected Payday phase behavior. Continue tracking TK performance as the sole underperformer despite favorable conditions.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 19,546 | 42.62% | - | 92.82% | - | 17.5% | - | 41.56% | - |
| 2026-W16 | Payday | 20,623 | 43.92% | ↑+3.1% | 92.76% | →-0.1% | 16.79% | ↓-4.1% | 48.01% | ↑+15.5% |

---

## L1: Country-Level Analysis

### FJ (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 13,701 | 41.17% | - | 93.97% | - | 17.16% | - | 43.96% | - |
| 2026-W16 | Payday | 14,450 | 42.80% | ↑+4.0% | 93.79% | →-0.2% | 16.68% | ↓-2.8% | 49.94% | ↑+13.6% |

**Analysis:** The +1.30pp improvement in Dunning Ship Rate is primarily attributable to the Payday phase transition, which drove significant PC2 gains (+15.5%) and enabled lower discount deployment (-4.1%) while maintaining stable Pre-Dunning AR. FJ and YE, representing 86% of volume, both showed healthy improvements aligned with the Payday pattern. TK requires monitoring as the only market showing declining performance despite favorable macro conditions, though its small volume (92 orders) limits overall impact.

### YE (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 3,324 | 58.81% | - | 87.77% | - | 16.24% | - | 34.94% | - |
| 2026-W16 | Payday | 3,272 | 61.31% | ↑+4.3% | 87.83% | →+0.1% | 15.07% | ↓-7.2% | 49.91% | ↑+42.8% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### TV (Rank #3 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 96 | 12.50% | - | 92.14% | - | 17.76% | - | 38.93% | - |
| 2026-W16 | Payday | 84 | 26.19% | ↑+109.5% | 93.52% | →+1.5% | 15.26% | ↓-14.1% | 38.25% | →-1.7% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### TK (Rank #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 50 | 32.00% | - | 95.33% | - | 18.87% | - | 38.33% | - |
| 2026-W16 | Payday | 92 | 28.26% | ↓-11.7% | 93.65% | →-1.8% | 17.84% | ↓-5.5% | 39.61% | ↑+3.3% |

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
| FJ | ↑+4.0% | →-0.2% | ↓-2.8% | ↑+13.6% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| YE | ↑+4.3% | →+0.1% | ↓-7.2% | ↑+42.8% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| TV | ↑+109.5% | →+1.5% | ↓-14.1% | →-1.7% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| TK | ↓-11.7% | →-1.8% | ↓-5.5% | ↑+3.3% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| FJ | 13,701 | 41.17% | 14,450 | 42.80% | 5.5% | Medium |
| YE | 3,324 | 58.81% | 3,272 | 61.31% | -1.6% | High |
| CF | 1,882 | 30.29% | 2,264 | 30.43% | 20.3% | Medium |
| TO | 268 | 23.88% | 231 | 23.81% | -13.8% | Low |
| TZ | 130 | 26.15% | 145 | 29.66% | 11.5% | Low |
| TV | 96 | 12.50% | 84 | 26.19% | -12.5% | Low |
| TT | 95 | 40.00% | 85 | 38.82% | -10.5% | Medium |
| TK | 50 | 32.00% | 92 | 28.26% | 84.0% | Medium |

---


---

*Report: 2026-04-21*
