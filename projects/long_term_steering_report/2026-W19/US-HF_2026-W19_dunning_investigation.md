# Dunning Investigation: US-HF 2026-W19

**Metric:** Dunning Ship Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 47.98% → 46.40% (-1.58pp)  
**Volume:** 13,113 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined by -1.58pp (47.98% → 46.40%) in US-HF during W19, representing a -3.3% relative decrease amid the transition from Mid-Cycle to Pre-Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.98% → 92.86% | -0.1% | ✅ |
| Discount % | 13.44% → 13.39% | -0.4% | ✅ |
| PC2 | 50.97% → 51.40% | +0.8% | ✅ |
| Ship Rate | 47.98% → 46.40% | -3.3% | ⚠️ |

**Key Findings:**
- Ship Rate declined -3.3% despite all upstream metrics remaining stable or slightly improving
- Volume decreased by -6.4% (14,003 → 13,113 orders), indicating reduced eligible order flow
- Payday phase shifted from Mid-Cycle to Pre-Payday, which typically correlates with tighter consumer budgets
- PC2 slightly improved (+0.8%) but did not translate into improved shipping outcomes
- Pre-Dunning AR and Discount % showed negligible movement (→-0.1% and →-0.4% respectively), ruling out funnel degradation as root cause

**Action:** Monitor — The decline appears primarily driven by external payday cycle timing rather than operational issues. All controllable metrics (AR, Discount, PC2) are stable. Continue tracking into W20 to confirm recovery as payday phase shifts.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W18 | Mid-Cycle | 14,003 | 47.98% | - | 92.98% | - | 13.44% | - | 50.97% | - |
| 2026-W19 | Pre-Payday | 13,113 | 46.40% | ↓-3.3% | 92.86% | →-0.1% | 13.39% | →-0.4% | 51.4% | →+0.8% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W18 | Mid-Cycle | 14,003 | 47.98% | - | 92.98% | - | 13.44% | - | 50.97% | - |
| 2026-W19 | Pre-Payday | 13,113 | 46.40% | ↓-3.3% | 92.86% | →-0.1% | 13.39% | →-0.4% | 51.4% | →+0.8% |

**Analysis:** The -1.58pp Ship Rate decline in US for W19 is most likely attributable to the payday phase transition from Mid-Cycle to Pre-Payday, when customers typically have reduced purchasing capacity. With all upstream funnel metrics holding steady and no signs of operational degradation, this decline follows expected seasonal payment cycle patterns and should recover as the payday phase advances in the coming week.


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
| US | ↓-3.3% | →-0.1% | →-0.4% | →+0.8% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 14,003 | 47.98% | 13,113 | 46.40% | -6.4% | Medium |

---


---

*Report: 2026-05-12*
