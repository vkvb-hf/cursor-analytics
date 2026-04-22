# Dunning Investigation: US-HF 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 47.74% → 46.72% (-1.02pp)  
**Volume:** 12,619 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined from 47.74% to 46.72% (-1.02pp) week-over-week, representing a -2.1% relative decrease amid the transition from Mid-Cycle to Pre-Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.78% → 93.09% | +0.31pp | ✅ |
| Discount % | 14.6% → 13.95% | -0.65pp | ✅ |
| PC2 | 52.76% → 52.07% | -0.69pp | ⚠️ |
| Ship Rate | 47.74% → 46.72% | -1.02pp | ⚠️ |

**Key Findings:**
- US accounts for 100% of cluster volume and drove the entire -1.02pp Ship Rate decline
- Pre-Dunning Approval Rate improved slightly (+0.3%), indicating upstream eligibility is not the issue
- Discount % decreased by -4.5% (from 14.6% to 13.95%), which should positively impact Ship Rate per the decision framework, yet Ship Rate still declined
- PC2 (Payment Conversion 2) dropped -1.3% (from 52.76% to 52.07%), suggesting downstream payment completion issues
- Volume contracted by -8.5% (13,786 → 12,619 orders), coinciding with the Pre-Payday phase transition

**Action:** Investigate — The decline in Ship Rate despite favorable Discount % movement, combined with PC2 degradation during Pre-Payday phase, suggests customer payment behavior issues warrant deeper analysis into payment failure reasons and cash flow timing impacts.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 13,786 | 47.74% | - | 92.78% | - | 14.6% | - | 52.76% | - |
| 2026-W15 | Pre-Payday | 12,619 | 46.72% | →-2.1% | 93.09% | →+0.3% | 13.95% | ↓-4.5% | 52.07% | →-1.3% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 13,786 | 47.74% | - | 92.78% | - | 14.6% | - | 52.76% | - |
| 2026-W15 | Pre-Payday | 12,619 | 46.72% | →-2.1% | 93.09% | →+0.3% | 13.95% | ↓-4.5% | 52.07% | →-1.3% |

**Analysis:** The -1.02pp decline in US-HF Dunning Ship Rate appears primarily driven by deteriorating payment conversion (PC2 down -1.3%) during the Pre-Payday phase, when customers typically have reduced liquidity. Despite improved Pre-Dunning AR and reduced discount rates, the payment completion step is underperforming and should be investigated for specific failure codes or timing patterns. Monitoring through the payday transition in W16 will confirm whether this is a cyclical cash-flow effect or a structural issue requiring intervention.


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
| US | →-2.1% | →+0.3% | ↓-4.5% | →-1.3% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 13,786 | 47.74% | 12,619 | 46.72% | -8.5% | Medium |

---


---

*Report: 2026-04-22*
