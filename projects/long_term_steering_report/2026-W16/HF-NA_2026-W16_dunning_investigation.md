# Dunning Investigation: HF-NA 2026-W16

**Metric:** Dunning Ship Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 48.19% → 48.03% (-0.16pp)  
**Volume:** 18,142 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined marginally by -0.16pp (48.19% → 48.03%) during the Pre-Payday → Payday transition, driven primarily by a significant drop in CA (-6.7%) that offset improvements in US (+1.9%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | Stable | -0.1% | ✅ |
| Discount % | Increased | +5.4% | ⚠️ |
| PC2 | Stable | +0.3% | ✅ |
| Ship Rate | Declined | -0.3% | ⚠️ |

**Key Findings:**
- CA experienced a sharp Ship Rate decline of -6.7% (53.04% → 49.51%) despite stable Pre-Dunning AR (+0.1%) and PC2 (+0.1%), making it the primary contributor to the cluster-level decline
- Discount % increased significantly across the cluster (+5.4%), with US showing the largest increase (+6.6%) yet still improving Ship Rate (+1.9%)
- US volume grew by 11.6% (12,619 → 14,086 orders) and Ship Rate improved +1.9%, partially offsetting CA's decline
- Mix shift toward lower-performing US (Medium SR tier) diluted overall cluster performance despite US's internal improvement
- The Payday phase transition correlates with increased discounting but did not uniformly improve Ship Rate across countries

**Action:** Investigate – CA's -6.7% Ship Rate decline during Payday phase requires root cause analysis; the disconnect between increased discounting and declining conversion suggests potential issues with discount effectiveness or customer segment behavior in CA.

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

**Analysis:** The -0.16pp decline in Dunning Ship Rate is primarily attributable to CA's significant underperformance (-6.7%) during the Payday transition, which was not fully compensated by US's modest improvement (+1.9%). The cluster-wide increase in Discount % (+5.4%) failed to drive expected conversion gains in CA, indicating potential discount strategy inefficiencies or shifting customer behavior that warrants further investigation into CA-specific dunning tactics.

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
