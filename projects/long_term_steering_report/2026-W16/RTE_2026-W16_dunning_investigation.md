# Dunning Investigation: RTE 2026-W16

**Metric:** Dunning Ship Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 42.61% → 43.82% (+1.21pp)  
**Volume:** 20,587 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate improved from 42.61% to 43.82% (+1.21pp) week-over-week, coinciding with the transition from Pre-Payday to Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | Stable funnel entry | -0.1% | ✅ |
| Discount % | Lower discount pressure | -4.1% | ✅ |
| PC2 | Payment conversion | -1.1% | ⚠️ |
| Ship Rate | Final conversion | +2.8% | ✅ |

**Key Findings:**
- **Payday Effect Driving Gains:** The Pre-Payday → Payday phase transition correlates with improved ship rates across most countries, with discount requirements dropping 4.1% cluster-wide
- **TV showed exceptional improvement:** Ship Rate surged +109.5% (12.50% → 26.19%) driven by the largest discount reduction (-14.1%) despite low volume (84 orders)
- **YE outperformed with strong fundamentals:** +4.2% Ship Rate improvement with -7.1% discount reduction and stable Pre-Dunning AR (+0.1%)
- **TK is a negative outlier:** Despite Payday phase, Ship Rate declined -11.7% with deteriorating Pre-Dunning AR (-1.8%) and PC2 (-2.0%), warranting investigation
- **No Simpson's Paradox detected:** FJ (largest market) grew volume +5.3% while improving Ship Rate +3.7%, supporting the aggregate trend

**Action:** **Monitor** - The improvement is consistent with expected Payday phase behavior. Continue monitoring TK for sustained underperformance; if decline persists into W17, escalate for deeper investigation.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 19,543 | 42.61% | - | 92.82% | - | 17.5% | - | 48.53% | - |
| 2026-W16 | Payday | 20,587 | 43.82% | ↑+2.8% | 92.76% | →-0.1% | 16.79% | ↓-4.1% | 48.01% | →-1.1% |

---

## L1: Country-Level Analysis

### FJ (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 13,700 | 41.17% | - | 93.97% | - | 17.16% | - | 50.35% | - |
| 2026-W16 | Payday | 14,422 | 42.68% | ↑+3.7% | 93.79% | →-0.2% | 16.68% | ↓-2.8% | 49.95% | →-0.8% |

**Analysis:** The +1.21pp improvement in Dunning Ship Rate is primarily attributed to the Payday phase transition, which reduced discount requirements across all markets while maintaining stable funnel entry rates. FJ and YE drove the majority of absolute gains through volume and rate improvements respectively, while TK requires monitoring due to counter-trend performance despite favorable timing conditions.

### YE (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 3,322 | 58.79% | - | 87.77% | - | 16.24% | - | 50.46% | - |
| 2026-W16 | Payday | 3,268 | 61.26% | ↑+4.2% | 87.83% | →+0.1% | 15.09% | ↓-7.1% | 49.85% | →-1.2% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### TV (Rank #3 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 96 | 12.50% | - | 92.14% | - | 17.76% | - | 38.46% | - |
| 2026-W16 | Payday | 84 | 26.19% | ↑+109.5% | 93.52% | →+1.5% | 15.26% | ↓-14.1% | 38.25% | →-0.5% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### TK (Rank #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 50 | 32.00% | - | 95.33% | - | 18.87% | - | 40.42% | - |
| 2026-W16 | Payday | 92 | 28.26% | ↓-11.7% | 93.65% | →-1.8% | 17.84% | ↓-5.5% | 39.61% | →-2.0% |

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
| FJ | ↑+3.7% | →-0.2% | ↓-2.8% | →-0.8% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| YE | ↑+4.2% | →+0.1% | ↓-7.1% | →-1.2% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| TV | ↑+109.5% | →+1.5% | ↓-14.1% | →-0.5% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| TK | ↓-11.7% | →-1.8% | ↓-5.5% | →-2.0% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| FJ | 13,700 | 41.17% | 14,422 | 42.68% | 5.3% | Medium |
| YE | 3,322 | 58.79% | 3,268 | 61.26% | -1.6% | High |
| CF | 1,882 | 30.29% | 2,262 | 30.37% | 20.2% | Medium |
| TO | 268 | 23.88% | 230 | 23.48% | -14.2% | Low |
| TZ | 130 | 26.15% | 144 | 29.17% | 10.8% | Low |
| TV | 96 | 12.50% | 84 | 26.19% | -12.5% | Low |
| TT | 95 | 40.00% | 85 | 38.82% | -10.5% | Medium |
| TK | 50 | 32.00% | 92 | 28.26% | 84.0% | Medium |

---


---

*Report: 2026-04-22*
