# Dunning Investigation: HF-NA 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 49.18% → 48.19% (-0.99pp)  
**Volume:** 16,450 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined by -0.99pp (49.18% → 48.19%) in HF-NA during W15, with volume decreasing by 7.0% (17,686 → 16,450 orders) amid a transition from Mid-Cycle to Pre-Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.93% → 93.18% | +0.25pp | ✅ |
| Discount % | 15.61% → 15.07% | -0.54pp | ✅ |
| PC2 | 52.45% → 51.84% | -0.61pp | ⚠️ |
| Ship Rate | 49.18% → 48.19% | -0.99pp | ⚠️ |

**Key Findings:**
- Both US (-2.1%) and CA (-2.2%) experienced similar Ship Rate declines, with US contributing the majority of volume impact (12,619 of 16,450 orders)
- PC2 declined across both countries (US: -1.3%, CA: -0.5%), correlating with the Ship Rate decrease per the decision framework
- Discount % decreased in both markets (US: -4.5%, CA: -2.2%), which should positively impact Ship Rate but did not offset PC2 weakness
- Pre-Dunning AR remained stable or slightly improved (+0.3% US, +0.0% CA), ruling out upstream acceptance issues as a root cause
- Payday phase shift from Mid-Cycle to Pre-Payday likely contributed to customer payment behavior changes affecting PC2 and final conversion

**Action:** Monitor - The decline appears primarily driven by cyclical payday timing effects rather than structural issues. Pre-Dunning AR stability and reduced discounting suggest operational health; recommend tracking W16 (Payday phase) for expected recovery.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 17,686 | 49.18% | - | 92.93% | - | 15.61% | - | 52.45% | - |
| 2026-W15 | Pre-Payday | 16,450 | 48.19% | →-2.0% | 93.18% | →+0.3% | 15.07% | ↓-3.5% | 51.84% | →-1.2% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 13,786 | 47.74% | - | 92.78% | - | 14.6% | - | 52.76% | - |
| 2026-W15 | Pre-Payday | 12,619 | 46.72% | →-2.1% | 93.09% | →+0.3% | 13.95% | ↓-4.5% | 52.07% | →-1.3% |

**Analysis:** The -0.99pp Ship Rate decline in HF-NA W15 is primarily attributable to PC2 weakness across both US and CA markets during the Pre-Payday phase transition, despite stable Pre-Dunning acceptance and reduced discounting. This pattern is consistent with typical payday cycle effects on customer payment behavior. No immediate escalation is required, but W16 performance should be monitored to confirm recovery as customers enter the Payday phase.

### CA (Rank #2 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 3,900 | 54.26% | - | 93.47% | - | 19.17% | - | 51.36% | - |
| 2026-W15 | Pre-Payday | 3,831 | 53.04% | →-2.2% | 93.49% | →+0.0% | 18.75% | →-2.2% | 51.08% | →-0.5% |

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
| US | →-2.1% | →+0.3% | ↓-4.5% | →-1.3% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| CA | →-2.2% | →+0.0% | →-2.2% | →-0.5% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 13,786 | 47.74% | 12,619 | 46.72% | -8.5% | Medium |
| CA | 3,900 | 54.26% | 3,831 | 53.04% | -1.8% | High |

---


---

*Report: 2026-04-22*
