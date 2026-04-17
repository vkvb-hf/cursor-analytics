# Dunning Investigation: HF-NA 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 49.17% → 48.17% (-1.00pp)  
**Volume:** 16,480 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined by -1.00pp (49.17% → 48.17%) in HF-NA during 2026-W15, with volume decreasing by 6.9% (17,700 → 16,480 eligible orders) as the payday phase shifted from Mid-Cycle to Pre-Payday.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.94% → 93.19% | +0.3% | ✅ |
| Discount % | 15.6% → 15.04% | -3.6% | ✅ |
| PC2 | 49.6% → 51.85% | +4.5% | ✅ |
| Ship Rate | 49.17% → 48.17% | -2.0% | ⚠️ |

**Key Findings:**
- Ship Rate declined despite improvements in all supporting metrics (Pre-Dunning AR +0.3%, Discount -3.6%, PC2 +4.5%), suggesting payday timing is the primary driver
- US contributed the largest absolute impact (Rank #1) with Ship Rate declining -2.1% on -8.4% volume reduction
- CA showed the steepest Ship Rate decline (-2.4%) despite being a high-performing tier (52.88% SR)
- Both US and CA experienced Pre-Payday liquidity constraints, with discount reductions (US -4.5%, CA -2.5%) failing to offset timing headwinds
- Volume contraction was concentrated in US (-8.4%), while CA remained relatively stable (-1.5%)

**Action:** Monitor — Declines align with expected Pre-Payday behavior; supporting metrics trending positively indicate recovery likely in upcoming payday window.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 17,700 | 49.17% | - | 92.94% | - | 15.6% | - | 49.6% | - |
| 2026-W15 | Pre-Payday | 16,480 | 48.17% | →-2.0% | 93.19% | →+0.3% | 15.04% | ↓-3.6% | 51.85% | ↑+4.5% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 13,791 | 47.75% | - | 92.78% | - | 14.6% | - | 49.33% | - |
| 2026-W15 | Pre-Payday | 12,628 | 46.73% | →-2.1% | 93.09% | →+0.3% | 13.94% | ↓-4.5% | 52.08% | ↑+5.6% |

**Analysis:** The -1.00pp Ship Rate decline in HF-NA for 2026-W15 is primarily attributable to the payday phase transition from Mid-Cycle to Pre-Payday, which typically constrains customer liquidity despite operational improvements. Both US and CA showed metric improvements in Pre-Dunning AR, Discount %, and PC2, indicating the dunning process is functioning effectively and the decline is cyclical rather than systemic. Performance should be monitored through the payday period to confirm expected recovery.

### CA (Rank #2 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 3,909 | 54.16% | - | 93.49% | - | 19.11% | - | 50.53% | - |
| 2026-W15 | Pre-Payday | 3,852 | 52.88% | →-2.4% | 93.51% | →+0.0% | 18.63% | ↓-2.5% | 51.08% | →+1.1% |

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
| US | →-2.1% | →+0.3% | ↓-4.5% | ↑+5.6% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| CA | →-2.4% | →+0.0% | ↓-2.5% | →+1.1% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 13,791 | 47.75% | 12,628 | 46.73% | -8.4% | Medium |
| CA | 3,909 | 54.16% | 3,852 | 52.88% | -1.5% | High |

---


---

*Report: 2026-04-17*
