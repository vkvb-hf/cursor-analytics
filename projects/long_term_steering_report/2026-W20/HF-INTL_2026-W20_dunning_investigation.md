# Dunning Investigation: HF-INTL 2026-W20

**Metric:** Dunning Ship Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 68.53% → 67.23% (-1.30pp)  
**Volume:** 26,467 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined from 68.53% to 67.23% (-1.30pp) in W20, with 26,467 eligible orders during the Payday phase transition.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.80% → 94.21% | +0.41pp | ✅ |
| Discount % | 12.45% → 12.93% | +0.48pp | ⚠️ |
| PC2 | 43.04% → 45.21% | +2.17pp | ✅ |
| Ship Rate | 68.53% → 67.23% | -1.30pp | ⚠️ |

**Key Findings:**
- **FR drove the decline:** FR experienced the largest Ship Rate drop (-6.1%, from 67.27% to 63.15%) despite improved Pre-Dunning AR (+1.8pp), with Discount % increasing significantly (+9.8%)
- **Volume mix shift detected:** FR volume dropped -25.7% (5,954 → 4,423) while lower-performing GB increased +6.0%, contributing to Simpson's Paradox effects
- **SE and CH showed strong improvement:** SE Ship Rate surged +14.6% with a -17.5% reduction in Discount %, while CH improved +10.8%
- **AU positive outlier:** AU improved +3.4% in Ship Rate driven by reduced discounting (-3.6%) and strong PC2 growth (+15.3%)
- **Discount % inversely correlated:** Countries with increased discounting (FR, GB) saw Ship Rate declines, while those reducing discounts (SE, AU) improved

**Action:** **Investigate** - FR requires immediate deep-dive analysis to understand the disconnect between improved Pre-Dunning AR and declining Ship Rate, particularly examining the +9.8% discount increase impact and -25.7% volume drop during Payday transition.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W19 | Pre-Payday | 29,419 | 68.53% | - | 93.80% | - | 12.45% | - | 43.04% | - |
| 2026-W20 | Payday | 26,467 | 67.23% | →-1.9% | 94.21% | →+0.4% | 12.93% | ↑+3.9% | 45.21% | ↑+5.0% |

---

## L1: Country-Level Analysis

### FR (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W19 | Pre-Payday | 5,954 | 67.27% | - | 93.10% | - | 10.17% | - | 41.73% | - |
| 2026-W20 | Payday | 4,423 | 63.15% | ↓-6.1% | 94.79% | →+1.8% | 11.17% | ↑+9.8% | 45.16% | ↑+8.2% |

**Analysis:** The -1.30pp Ship Rate decline is primarily driven by FR's significant underperformance (-6.1%) combined with unfavorable volume mix shifts away from higher-performing markets. While Pre-Dunning AR and PC2 metrics improved cluster-wide, the elevated Discount % (+3.9%) indicates potential pricing or offer strategy issues that are counteracting funnel improvements. Immediate focus should be placed on FR's discount strategy and understanding why Payday phase benefits are not materializing in this market.

### AU (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W19 | Pre-Payday | 5,473 | 68.76% | - | 91.30% | - | 12.61% | - | 44.87% | - |
| 2026-W20 | Payday | 5,212 | 71.09% | ↑+3.4% | 91.91% | →+0.7% | 12.16% | ↓-3.6% | 51.74% | ↑+15.3% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### GB (Rank #3 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W19 | Pre-Payday | 6,268 | 58.25% | - | 94.61% | - | 16.4% | - | 47.36% | - |
| 2026-W20 | Payday | 6,641 | 57.28% | →-1.7% | 94.75% | →+0.1% | 16.66% | →+1.6% | 46.96% | →-0.8% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### SE (Rank #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W19 | Pre-Payday | 549 | 62.48% | - | 97.31% | - | 10.12% | - | 36.78% | - |
| 2026-W20 | Payday | 690 | 71.59% | ↑+14.6% | 96.65% | →-0.7% | 8.35% | ↓-17.5% | 41.39% | ↑+12.5% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### CH (Rank #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W19 | Pre-Payday | 112 | 68.75% | - | 92.57% | - | 3.07% | - | 42.92% | - |
| 2026-W20 | Payday | 84 | 76.19% | ↑+10.8% | 93.74% | →+1.3% | 3.66% | ↑+19.2% | 41.77% | ↓-2.7% |

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
| FR | ↓-6.1% | →+1.8% | ↑+9.8% | ↑+8.2% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| AU | ↑+3.4% | →+0.7% | ↓-3.6% | ↑+15.3% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| GB | →-1.7% | →+0.1% | →+1.6% | →-0.8% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| SE | ↑+14.6% | →-0.7% | ↓-17.5% | ↑+12.5% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| CH | ↑+10.8% | →+1.3% | ↑+19.2% | ↓-2.7% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| GB | 6,268 | 58.25% | 6,641 | 57.28% | 6.0% | High |
| FR | 5,954 | 67.27% | 4,423 | 63.15% | -25.7% | High |
| AU | 5,473 | 68.76% | 5,212 | 71.09% | -4.8% | High |
| DE | 3,549 | 70.19% | 2,945 | 68.46% | -17.0% | High |
| BE | 2,192 | 90.56% | 1,527 | 87.56% | -30.3% | High |
| NZ | 1,304 | 66.79% | 1,176 | 64.46% | -9.8% | High |
| NO | 1,302 | 80.95% | 1,621 | 82.79% | 24.5% | High |
| DK | 975 | 75.79% | 487 | 70.02% | -50.1% | High |
| IE | 866 | 59.47% | 918 | 62.31% | 6.0% | High |
| SE | 549 | 62.48% | 690 | 71.59% | 25.7% | High |

---


---

*Report: 2026-05-19*
