# Dunning Investigation: HF-NA 2026-W21

**Metric:** Dunning Ship Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 47.65% → 46.52% (-1.13pp)  
**Volume:** 16,483 eligible orders  
**Payday Phase:** Payday → Post-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined from 47.65% to 46.52% (-1.13pp) week-over-week, coinciding with the transition from Payday to Post-Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.11% → 92.89% | -0.22pp | ✅ |
| Discount % | 14.8% → 14.49% | -0.31pp | ✅ |
| PC2 | 49.97% → 50.35% | +0.38pp | ✅ |
| Ship Rate | 47.65% → 46.52% | -1.13pp | ⚠️ |

**Key Findings:**
- CA experienced the steepest Ship Rate decline (-3.5%), despite increased Discount % (+2.6%) and improved PC2 (+2.6%), suggesting the Payday → Post-Payday transition is the primary driver
- US contributed most to absolute volume impact with -2.0% Ship Rate decline on 12,995 orders, while Discount % decreased by -3.4%
- Mix shift shows CA (high-performing tier at 50.23% SR) lost -1.6% volume share while lower-performing US gained +0.8%, creating compositional headwinds
- Pre-Dunning AR remained stable across both countries (US: -0.2%, CA: -0.3%), indicating payment eligibility was not a limiting factor
- The Post-Payday phase timing is the common factor across both countries' declines, consistent with expected cyclical payment behavior

**Action:** Monitor — The decline aligns with expected Post-Payday seasonality. Track W22 performance to confirm recovery during the next Payday phase before escalating.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W20 | Payday | 16,440 | 47.65% | - | 93.11% | - | 14.8% | - | 49.97% | - |
| 2026-W21 | Post-Payday | 16,483 | 46.52% | →-2.4% | 92.89% | →-0.2% | 14.49% | →-2.1% | 50.35% | →+0.8% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W20 | Payday | 12,895 | 46.44% | - | 92.92% | - | 14.35% | - | 50.41% | - |
| 2026-W21 | Post-Payday | 12,995 | 45.53% | →-2.0% | 92.71% | →-0.2% | 13.86% | ↓-3.4% | 50.54% | →+0.3% |

**Analysis:** The -1.13pp decline in Dunning Ship Rate from W20 to W21 is primarily attributable to the Payday → Post-Payday phase transition, a known cyclical pattern affecting customer payment behavior. CA showed the most pronounced decline (-3.5%) despite favorable Discount and PC2 movements, while US experienced a moderate decline (-2.0%) with reduced discounting. No intervention is recommended at this time; continued monitoring through the next Payday cycle will confirm whether performance normalizes as expected.

### CA (Rank #2 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W20 | Payday | 3,545 | 52.07% | - | 93.80% | - | 16.42% | - | 48.38% | - |
| 2026-W21 | Post-Payday | 3,488 | 50.23% | ↓-3.5% | 93.54% | →-0.3% | 16.84% | ↑+2.6% | 49.63% | ↑+2.6% |

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
| US | →-2.0% | →-0.2% | ↓-3.4% | →+0.3% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| CA | ↓-3.5% | →-0.3% | ↑+2.6% | ↑+2.6% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 12,895 | 46.44% | 12,995 | 45.53% | 0.8% | Medium |
| CA | 3,545 | 52.07% | 3,488 | 50.23% | -1.6% | High |

---


---

*Report: 2026-05-26*
