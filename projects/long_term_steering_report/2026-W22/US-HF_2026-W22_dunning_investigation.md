# Dunning Investigation: US-HF 2026-W22

**Metric:** Dunning Ship Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 45.48% → 44.21% (-1.27pp)  
**Volume:** 13,209 eligible orders  
**Payday Phase:** Post-Payday → Mid-Cycle

## Executive Summary

**Overall:** Dunning Ship Rate declined by 1.27pp (45.48% → 44.21%) in US-HF during 2026-W22, representing a -2.8% relative decrease amid the transition from Post-Payday to Mid-Cycle phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.71% → 92.42% | -0.3% | ✅ |
| Discount % | 13.87% → 16.91% | +21.9% | ⚠️ |
| PC2 | 49.95% → 50.93% | +2.0% | ✅ |
| Ship Rate | 45.48% → 44.21% | -2.8% | ⚠️ |

**Key Findings:**
- Discount % increased significantly by +21.9% (13.87% → 16.91%), which has a negative relationship with Ship Rate and is the primary driver of the decline
- Pre-Dunning AR remained essentially stable with only a marginal -0.3% decrease (92.71% → 92.42%), indicating upstream authorization is not the issue
- PC2 showed slight improvement (+2.0%), suggesting payment collection efforts are functioning adequately
- Volume increased modestly by 1.8% (12,977 → 13,209 orders), ruling out significant mix shift as a contributing factor
- Payday phase transition from Post-Payday to Mid-Cycle aligns with expected mid-cycle financial constraints driving higher discount usage

**Action:** Monitor — The decline is primarily driven by increased discount utilization during the Mid-Cycle payday phase, which is a known cyclical pattern. No immediate escalation required, but track whether Ship Rate recovers in the next Post-Payday period.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W21 | Post-Payday | 12,977 | 45.48% | - | 92.71% | - | 13.87% | - | 49.95% | - |
| 2026-W22 | Mid-Cycle | 13,209 | 44.21% | ↓-2.8% | 92.42% | →-0.3% | 16.91% | ↑+21.9% | 50.93% | →+2.0% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W21 | Post-Payday | 12,977 | 45.48% | - | 92.71% | - | 13.87% | - | 49.95% | - |
| 2026-W22 | Mid-Cycle | 13,209 | 44.21% | ↓-2.8% | 92.42% | →-0.3% | 16.91% | ↑+21.9% | 50.93% | →+2.0% |

**Analysis:** The 1.27pp decline in Dunning Ship Rate for US is attributable to a substantial +21.9% increase in Discount % during the Mid-Cycle payday phase, when customers typically face tighter liquidity and require more aggressive discounting to convert. Given the cyclical nature of this pattern and stable upstream metrics (Pre-Dunning AR, PC2), this represents expected mid-cycle behavior rather than a systemic issue requiring intervention.


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
| US | ↓-2.8% | →-0.3% | ↑+21.9% | →+2.0% | Post-Payday → Mid-Cycle | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 12,977 | 45.48% | 13,209 | 44.21% | 1.8% | Medium |

---


---

*Report: 2026-06-02*
