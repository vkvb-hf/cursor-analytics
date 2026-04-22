# Dunning Investigation: HF-NA 2026-W16

**Metric:** Dunning Ship Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 48.19% → 48.03% (-0.16pp)  
**Volume:** 18,142 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined marginally by -0.16pp (48.19% → 48.03%) during the Pre-Payday to Payday transition, driven primarily by a significant drop in CA that offset gains in US.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | Stable | -0.1% | ✅ |
| Discount % | Increased | +5.4% | ⚠️ |
| PC2 | Stable | +0.3% | ✅ |
| Ship Rate | Declined | -0.3% | ⚠️ |

**Key Findings:**
- **CA drove the decline:** CA Ship Rate dropped significantly by -6.7pp (53.04% → 49.51%) despite stable Pre-Dunning AR (+0.1%) and PC2 (+0.1%), suggesting the +3.4% increase in Discount % negatively impacted conversion
- **US showed resilience:** US Ship Rate improved by +1.9% (46.72% → 47.61%) even with a +6.6% increase in Discount %, indicating stronger customer response during Payday phase
- **Mix shift partially masked decline:** US volume grew +11.6% while CA grew only +5.9%, but since CA has higher SR tier (53% vs 47%), the shift toward lower-performing US contributed to cluster-level decline
- **Discount increases across both markets:** Both CA (+3.4%) and US (+6.6%) saw increased discount rates, which typically has a negative relationship with Ship Rate per the decision framework
- **Volume increased overall:** Total eligible orders grew from 16,450 to 18,142 (+10.3%), indicating healthy funnel entry during Payday phase

**Action:** Investigate — The significant -6.7pp drop in CA requires deeper analysis to understand why increased discounts during Payday phase did not improve conversion as expected in that market.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 16,450 | 48.19% | - | 93.18% | - | 15.07% | - | 51.84% | - |
| 2026-W16 | Payday | 18,142 | 48.03% | →-0.3% | 93.11% | →-0.1% | 15.88% | ↑+5.4% | 51.98% | →+0.3% |

---

## L1: Country-Level Analysis

### CA (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 3,831 | 53.04% | - | 93.49% | - | 18.75% | - | 51.08% | - |
| 2026-W16 | Payday | 4,056 | 49.51% | ↓-6.7% | 93.58% | →+0.1% | 19.38% | ↑+3.4% | 51.12% | →+0.1% |

**Analysis:** The -0.16pp decline in Dunning Ship Rate masks divergent country performance: CA experienced a substantial -6.7pp drop despite favorable Payday timing, while US improved +1.9%. The cluster-wide increase in Discount % (+5.4%) did not translate to improved Ship Rates, particularly in CA, suggesting potential issues with discount effectiveness or customer payment capacity during this Payday cycle. Further investigation into CA-specific factors and discount strategy optimization is recommended before the next billing cycle.

### US (Rank #2 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 12,619 | 46.72% | - | 93.09% | - | 13.95% | - | 52.07% | - |
| 2026-W16 | Payday | 14,086 | 47.61% | →+1.9% | 92.97% | →-0.1% | 14.87% | ↑+6.6% | 52.23% | →+0.3% |

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
| CA | ↓-6.7% | →+0.1% | ↑+3.4% | →+0.1% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| US | →+1.9% | →-0.1% | ↑+6.6% | →+0.3% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 12,619 | 46.72% | 14,086 | 47.61% | 11.6% | Medium |
| CA | 3,831 | 53.04% | 4,056 | 49.51% | 5.9% | High |

---


---

*Report: 2026-04-22*
