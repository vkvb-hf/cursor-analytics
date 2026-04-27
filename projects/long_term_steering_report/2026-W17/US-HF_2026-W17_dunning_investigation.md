# Dunning Investigation: US-HF 2026-W17

**Metric:** Dunning Ship Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 47.59% → 47.69% (+0.10pp)  
**Volume:** 14,281 eligible orders  
**Payday Phase:** Payday → Post-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate improved marginally from 47.59% to 47.69% (+0.10pp) in W17, with volume increasing by 1.5% to 14,281 eligible orders during the Post-Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.97% → 92.99% | +0.0% | ✅ |
| Discount % | 14.88% → 14.61% | -1.8% | ✅ |
| PC2 | 49.9% → 51.85% | +3.9% | ✅ |
| Ship Rate | 47.59% → 47.69% | +0.2% | ✅ |

**Key Findings:**
- PC2 showed the strongest improvement at +3.9%, rising from 49.9% to 51.85%, indicating better payment collection performance in the second payment cycle
- Discount % decreased by 1.8% (14.88% → 14.61%), which positively contributed to Ship Rate per the decision framework (negative relationship)
- Pre-Dunning AR remained essentially flat (+0.0%), showing stable authorization rates entering the dunning process
- Volume increased modestly by 1.5% (14,073 → 14,281 orders) with no Simpson's Paradox detected in mix shift
- The transition from Payday to Post-Payday phase did not negatively impact performance as might typically be expected

**Action:** Monitor — All metrics are trending positively or stable. Continue tracking PC2 improvement sustainability and Discount % trends.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 14,073 | 47.59% | - | 92.97% | - | 14.88% | - | 49.9% | - |
| 2026-W17 | Post-Payday | 14,281 | 47.69% | →+0.2% | 92.99% | →+0.0% | 14.61% | →-1.8% | 51.85% | ↑+3.9% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 14,073 | 47.59% | - | 92.97% | - | 14.88% | - | 49.9% | - |
| 2026-W17 | Post-Payday | 14,281 | 47.69% | →+0.2% | 92.99% | →+0.0% | 14.61% | →-1.8% | 51.85% | ↑+3.9% |

**Analysis:** The US-HF cluster demonstrated healthy performance in W17 with a slight Ship Rate improvement driven primarily by a +3.9% increase in PC2 and a -1.8% reduction in Discount %. The positive trajectory during the Post-Payday phase suggests effective dunning operations; no immediate intervention is required, but continued monitoring of PC2 trends is recommended to confirm sustained improvement.


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
| US | →+0.2% | →+0.0% | →-1.8% | ↑+3.9% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 14,073 | 47.59% | 14,281 | 47.69% | 1.5% | Medium |

---


---

*Report: 2026-04-27*
