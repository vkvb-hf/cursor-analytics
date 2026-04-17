# Dunning Investigation: US-HF 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 47.75% → 46.73% (-1.02pp)  
**Volume:** 12,628 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined by 1.02pp (from 47.75% to 46.73%) in US-HF during W15, representing a -2.1% relative decrease amid a transition from Mid-Cycle to Pre-Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.78% → 93.09% | +0.31pp (+0.3%) | ✅ |
| Discount % | 14.6% → 13.94% | -0.66pp (-4.5%) | ✅ |
| PC2 | 49.33% → 52.08% | +2.75pp (+5.6%) | ✅ |
| Ship Rate | 47.75% → 46.73% | -1.02pp (-2.1%) | ⚠️ |

**Key Findings:**
- Ship Rate declined despite favorable movement in all upstream metrics (Pre-Dunning AR, Discount %, and PC2 all improved)
- Volume decreased by 8.4% (13,791 → 12,628 orders), suggesting mix shift effects may be masking underlying improvements
- Discount % decreased by 4.5%, which should positively impact Ship Rate per the decision framework, yet Ship Rate still fell
- PC2 improved significantly (+5.6%), indicating stronger payment completion at step 2, but this didn't translate to overall ship improvement
- Payday phase transition (Mid-Cycle → Pre-Payday) likely introduced external customer liquidity pressures overriding operational gains

**Action:** Investigate — The paradoxical pattern of declining Ship Rate despite improving supporting metrics suggests Simpson's Paradox or external factors (payday timing, customer segment mix) are driving the decline. Deeper cohort analysis by customer segment and payment timing is recommended.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 13,791 | 47.75% | - | 92.78% | - | 14.6% | - | 49.33% | - |
| 2026-W15 | Pre-Payday | 12,628 | 46.73% | →-2.1% | 93.09% | →+0.3% | 13.94% | ↓-4.5% | 52.08% | ↑+5.6% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 13,791 | 47.75% | - | 92.78% | - | 14.6% | - | 49.33% | - |
| 2026-W15 | Pre-Payday | 12,628 | 46.73% | →-2.1% | 93.09% | →+0.3% | 13.94% | ↓-4.5% | 52.08% | ↑+5.6% |

**Analysis:** The US-HF cluster experienced a 1.02pp decline in Dunning Ship Rate during W15 despite improvements across all key operational metrics (Pre-Dunning AR, Discount %, PC2). This counterintuitive pattern, combined with an 8.4% volume reduction and the Mid-Cycle to Pre-Payday phase transition, strongly suggests that external customer liquidity factors and potential mix shift effects are outweighing operational improvements. Further investigation into customer segment composition and payday-aligned behavioral patterns is warranted before the next reporting cycle.


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
| US | →-2.1% | →+0.3% | ↓-4.5% | ↑+5.6% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 13,791 | 47.75% | 12,628 | 46.73% | -8.4% | Medium |

---


---

*Report: 2026-04-17*
