# Dunning Investigation: WL 2026-W14

**Metric:** Dunning Ship Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 29.39% → 28.35% (-1.04pp)  
**Volume:** 8,053 eligible orders  
**Payday Phase:** Mid-Cycle

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined from 29.39% to 28.35% (-1.04pp) week-over-week during Mid-Cycle payday phase, with eligible volume decreasing from 8,700 to 8,053 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 91.18% → 90.71% | -0.47pp | ⚠️ |
| Discount % | 16.35% → 15.46% | -0.89pp | ⚠️ |
| PC2 | 47.52% → 47.03% | -0.49pp | ⚠️ |
| Ship Rate | 29.39% → 28.35% | -1.04pp | ⚠️ |

**Key Findings:**
- **Simpson's Paradox Detected:** AO (highest performing country at 72.58% SR) experienced a -59.6% volume drop (1,228 → 496 orders), significantly reducing the mix of high-converting traffic
- **Individual country performance improved:** ER (+2.93pp), CK (+4.15pp), AO (+5.32pp), CG (+2.85pp), and GN (+0.97pp) all showed ship rate improvements despite the cluster-level decline
- **Low-tier country KN expanded:** Volume increased 17.4% (570 → 669) while ship rate declined slightly (16.14% → 15.10%), adding more low-converting orders to the mix
- **MR remains effectively non-converting:** Ship rate dropped from 0.07% to 0.00% with 1,421 orders contributing zero conversions
- **All funnel metrics showed slight declines:** Pre-Dunning AR, Discount %, and PC2 each dropped by approximately 0.5-0.9pp

**Action:** **Investigate** – The cluster-level decline is primarily driven by mix shift (Simpson's Paradox) rather than true performance degradation. Prioritize understanding why AO volume dropped 59.6% and evaluate whether MR orders should remain in the dunning flow.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Pre-Dunning AR | Discount % | PC2 |
|------|--------------|--------|-----------|----------------|------------|-----|
| 2026-W13 | Mid-Cycle | 8,700 | 29.39% | 91.18% | 16.35% | 47.52% |
| 2026-W14 | Mid-Cycle | 8,053 | 28.35% | 90.71% | 15.46% | 47.03% |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,563 | 23.64% | 2,559 | 26.57% | -0.2% | Low |
| MR | 1,466 | 0.07% | 1,421 | 0.00% | -3.1% | Low |
| CK | 1,440 | 43.61% | 1,497 | 47.76% | 4.0% | Medium |
| AO | 1,228 | 67.26% | 496 | 72.58% | -59.6% | High |
| CG | 798 | 21.93% | 779 | 24.78% | -2.4% | Low |
| GN | 635 | 36.06% | 632 | 37.03% | -0.5% | Medium |
| KN | 570 | 16.14% | 669 | 15.10% | 17.4% | Low |

---


---

*Report: 2026-04-09*
