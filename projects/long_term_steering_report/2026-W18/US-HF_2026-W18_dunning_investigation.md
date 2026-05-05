# Dunning Investigation: US-HF 2026-W18

**Metric:** Dunning Ship Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 47.58% → 48.00% (+0.42pp)  
**Volume:** 14,017 eligible orders  
**Payday Phase:** Post-Payday → Mid-Cycle

## Executive Summary

**Overall:** Dunning Ship Rate improved modestly from 47.58% to 48.00% (+0.42pp) in US-HF 2026-W18, driven primarily by reduced discount dependency and improved PC2 conversion during the Mid-Cycle payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.99% → 92.98% | -0.01pp | ✅ Stable |
| Discount % | 14.64% → 13.42% | -1.22pp | ✅ Improved (lower reliance) |
| PC2 | 49.42% → 51.71% | +2.29pp | ✅ Improved |
| Ship Rate | 47.58% → 48.00% | +0.42pp | ✅ Improved |

**Key Findings:**
- US Ship Rate increased +0.9% (47.58% → 48.00%) despite transitioning from Post-Payday to Mid-Cycle phase, which typically shows weaker performance
- Discount % decreased significantly by -8.3% (14.64% → 13.42%), indicating improved conversion efficiency without heavy discounting
- PC2 conversion strengthened by +4.6% (49.42% → 51.71%), serving as the primary driver of Ship Rate improvement
- Pre-Dunning AR remained essentially flat (-0.0%), ruling out upstream approval changes as a factor
- Volume decreased slightly by -1.6% (14,240 → 14,017 orders), no significant mix shift detected

**Action:** Monitor — The improvement is positive but modest (+0.42pp). Continue tracking PC2 performance and discount efficiency through the remainder of the Mid-Cycle phase to confirm sustainability.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W17 | Post-Payday | 14,240 | 47.58% | - | 92.99% | - | 14.64% | - | 49.42% | - |
| 2026-W18 | Mid-Cycle | 14,017 | 48.00% | →+0.9% | 92.98% | →-0.0% | 13.42% | ↓-8.3% | 51.71% | ↑+4.6% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W17 | Post-Payday | 14,240 | 47.58% | - | 92.99% | - | 14.64% | - | 49.42% | - |
| 2026-W18 | Mid-Cycle | 14,017 | 48.00% | →+0.9% | 92.98% | →-0.0% | 13.42% | ↓-8.3% | 51.71% | ↑+4.6% |

**Analysis:** The US-HF cluster demonstrated healthy Dunning performance in 2026-W18, with Ship Rate improving despite the less favorable Mid-Cycle timing. The gains were driven by stronger PC2 conversion (+4.6%) and reduced discount reliance (-8.3%), suggesting improved messaging or customer payment behavior. No intervention is required at this time; continued monitoring through the next payday cycle is recommended to validate trend stability.


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
| US | →+0.9% | →-0.0% | ↓-8.3% | ↑+4.6% | Post-Payday → Mid-Cycle | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 14,240 | 47.58% | 14,017 | 48.00% | -1.6% | Medium |

---


---

*Report: 2026-05-05*
