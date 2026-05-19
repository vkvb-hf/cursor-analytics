# Dunning Investigation: HF-NA 2026-W20

**Metric:** Dunning Ship Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 47.63% → 48.29% (+0.66pp)  
**Volume:** 16,660 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate improved from 47.63% to 48.29% (+0.66pp) in W20, driven by the transition from Pre-Payday to Payday phase across 16,660 eligible orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.99% → 93.12% | +0.13pp | ✅ |
| Discount % | 13.87% → 15.07% | +1.20pp | ⚠️ |
| PC2 | 53.39% → 50.41% | -2.98pp | ⚠️ |
| Ship Rate | 47.63% → 48.29% | +0.66pp | ✅ |

**Key Findings:**
- US contributed the largest improvement with Ship Rate increasing +1.6% (46.38% → 47.14%), despite a significant PC2 decline of -7.3%
- CA maintained the highest Ship Rate tier at 52.51% with a +1.0% improvement and stable PC2 (+1.1%)
- Discount % increased across both markets (US +9.6%, CA +5.9%), which typically has a negative relationship with Ship Rate, yet Ship Rate still improved—suggesting Payday phase effects outweighed discount pressure
- Pre-Dunning AR remained stable with minimal positive movement (+0.1% US, +0.4% CA)
- No significant Simpson's Paradox detected; volume mix remained stable with US at -0.2% and CA at -4.1% volume change

**Action:** Monitor — Ship Rate improvement is consistent with expected Payday phase behavior; track whether PC2 declines in US stabilize in post-payday weeks.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W19 | Pre-Payday | 16,837 | 47.63% | - | 92.99% | - | 13.87% | - | 53.39% | - |
| 2026-W20 | Payday | 16,660 | 48.29% | →+1.4% | 93.12% | →+0.1% | 15.07% | ↑+8.7% | 50.41% | ↓-5.6% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W19 | Pre-Payday | 13,103 | 46.38% | - | 92.86% | - | 13.4% | - | 54.51% | - |
| 2026-W20 | Payday | 13,078 | 47.14% | →+1.6% | 92.93% | →+0.1% | 14.69% | ↑+9.6% | 50.53% | ↓-7.3% |

**Analysis:** The +0.66pp improvement in Dunning Ship Rate for HF-NA in W20 is primarily attributable to the Payday phase transition, with both US and CA showing gains despite increased discount activity and PC2 pressure in US. The improvement aligns with expected seasonal payment behavior patterns. Continued monitoring is recommended to validate performance sustainability as the region moves into post-payday periods.

### CA (Rank #2 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W19 | Pre-Payday | 3,734 | 52.01% | - | 93.43% | - | 15.54% | - | 49.45% | - |
| 2026-W20 | Payday | 3,582 | 52.51% | →+1.0% | 93.80% | →+0.4% | 16.46% | ↑+5.9% | 49.98% | →+1.1% |

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
| US | →+1.6% | →+0.1% | ↑+9.6% | ↓-7.3% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| CA | →+1.0% | →+0.4% | ↑+5.9% | →+1.1% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 13,103 | 46.38% | 13,078 | 47.14% | -0.2% | Medium |
| CA | 3,734 | 52.01% | 3,582 | 52.51% | -4.1% | High |

---


---

*Report: 2026-05-19*
