# Dunning Investigation: HF-NA 2026-W19

**Metric:** Dunning Ship Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 48.33% → 47.67% (-0.66pp)  
**Volume:** 16,859 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined by -0.66pp (48.33% → 47.67%) in 2026-W19, driven primarily by US underperformance (-3.3% SR decline) despite CA showing strong improvement (+5.2%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.09% → 93.00% | -0.09pp | ✅ |
| Discount % | 14.13% → 13.86% | -0.27pp | ✅ |
| PC2 | 50.6% → 51.22% | +0.62pp | ✅ |
| Ship Rate | 48.33% → 47.67% | -0.66pp | ⚠️ |

**Key Findings:**
- US drove the cluster decline with Ship Rate dropping -3.3% (47.98% → 46.40%) despite stable Pre-Dunning AR and Discount % metrics
- CA showed strong counter-trend improvement with Ship Rate up +5.2% (49.52% → 52.11%), correlated with a -5.9% decrease in Discount %
- Volume decreased across both countries (US: -6.4%, CA: -9.2%), with CA's higher-performing segment shrinking proportionally more
- Payday Phase shifted from Mid-Cycle to Pre-Payday, which may explain US behavioral changes but did not negatively impact CA
- No Simpson's Paradox detected; US decline is a genuine performance issue not explained by mix shift

**Action:** Investigate – US Ship Rate decline requires deeper analysis into customer payment behavior during Pre-Payday phase, as upstream funnel metrics remained stable while conversion dropped significantly.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W18 | Mid-Cycle | 18,129 | 48.33% | - | 93.09% | - | 14.13% | - | 50.6% | - |
| 2026-W19 | Pre-Payday | 16,859 | 47.67% | →-1.4% | 93.00% | →-0.1% | 13.86% | →-1.9% | 51.22% | →+1.2% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W18 | Mid-Cycle | 14,003 | 47.98% | - | 92.98% | - | 13.44% | - | 50.97% | - |
| 2026-W19 | Pre-Payday | 13,113 | 46.40% | ↓-3.3% | 92.86% | →-0.1% | 13.39% | →-0.4% | 51.4% | →+0.8% |

**Analysis:** The HF-NA cluster experienced a -0.66pp decline in Dunning Ship Rate driven almost entirely by US performance degradation (-3.3%), which was partially offset by strong CA improvement (+5.2%). The Pre-Payday phase transition appears to have negatively impacted US customer payment behavior without corresponding issues in upstream metrics, suggesting the root cause lies in customer-level payment timing or liquidity factors rather than dunning process effectiveness. Further investigation into US customer segments and payment patterns during Pre-Payday periods is recommended.

### CA (Rank #2 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W18 | Mid-Cycle | 4,126 | 49.52% | - | 93.48% | - | 16.47% | - | 49.35% | - |
| 2026-W19 | Pre-Payday | 3,746 | 52.11% | ↑+5.2% | 93.50% | →+0.0% | 15.5% | ↓-5.9% | 50.57% | →+2.5% |

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
| US | ↓-3.3% | →-0.1% | →-0.4% | →+0.8% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| CA | ↑+5.2% | →+0.0% | ↓-5.9% | →+2.5% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 14,003 | 47.98% | 13,113 | 46.40% | -6.4% | Medium |
| CA | 4,126 | 49.52% | 3,746 | 52.11% | -9.2% | Medium |

---


---

*Report: 2026-05-12*
