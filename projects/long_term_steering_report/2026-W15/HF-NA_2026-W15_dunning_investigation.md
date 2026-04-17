# Dunning Investigation: HF-NA 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 49.17% → 48.17% (-1.00pp)  
**Volume:** 16,480 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined by 1.00pp (49.17% → 48.17%) in 2026-W15, with volume decreasing by 6.9% (17,700 → 16,480 eligible orders) during the transition from Mid-Cycle to Pre-Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.94% → 93.19% | +0.25pp | ✅ |
| Discount % | 15.6% → 15.04% | -0.56pp | ✅ |
| PC2 | 49.6% → 51.85% | +2.25pp | ✅ |
| Ship Rate | 49.17% → 48.17% | -1.00pp | ⚠️ |

**Key Findings:**
- Despite positive movements in supporting metrics (Pre-Dunning AR +0.3%, Discount % -3.6%, PC2 +4.5%), Ship Rate still declined by 1.00pp, suggesting external factors are overriding funnel improvements
- CA showed the largest Ship Rate decline (-2.4%) despite having the highest absolute Ship Rate (52.88%) in the cluster
- US contributed most to the overall decline due to volume weight (76.6% of cluster volume) with Ship Rate dropping -2.1%
- Volume declined across both countries (US -8.4%, CA -1.5%), with the Pre-Payday phase potentially impacting customer payment behavior
- The disconnect between improved funnel metrics and declining Ship Rate indicates possible customer-level payment capacity constraints during the Pre-Payday period

**Action:** Monitor - The metric movement appears linked to the natural Pre-Payday phase transition rather than operational issues. All controllable funnel metrics are moving favorably. Continue monitoring through the full payday cycle to confirm recovery post-payday.

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

**Analysis:** The 1.00pp decline in Dunning Ship Rate for HF-NA in 2026-W15 appears primarily driven by the payday cycle transition from Mid-Cycle to Pre-Payday, affecting both US and CA markets despite improvements in Pre-Dunning AR, Discount optimization, and PC2 metrics. Given that all controllable metrics are trending positively and the decline aligns with expected Pre-Payday customer cash flow constraints, this warrants continued monitoring rather than immediate intervention. Ship Rate recovery is anticipated as the cluster moves into the Post-Payday phase in the coming week.

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
