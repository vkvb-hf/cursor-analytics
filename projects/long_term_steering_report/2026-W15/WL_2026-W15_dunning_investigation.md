# Dunning Investigation: WL 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 28.34% → 31.07% (+2.73pp)  
**Volume:** 7,709 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate improved by +2.73pp (28.34% → 31.07%) at the cluster level in W15, despite all three top contributing countries showing individual declines—indicating a classic Simpson's Paradox driven by mix shift.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 89.14% → 90.00% | +0.86pp | ✅ |
| Discount % | 17.63% → 17.92% | +0.29pp | ⚠️ |
| PC2 | 37.98% → 39.89% | +1.91pp | ✅ |
| Ship Rate | 28.34% → 31.07% | +2.73pp | ✅ |

**Key Findings:**
- **Simpson's Paradox confirmed:** AO volume increased +123.6% (496 → 1,109 orders) with the highest SR tier (66.37%), shifting mix toward high-performing segment despite AO's own SR declining -8.6%
- **GN showed largest individual decline:** Ship Rate dropped -22.0% (37.03% → 28.89%) with volume contracting -21.7%, likely driven by increased Discount % (+4.3%) while PC2 remained flat
- **AO root cause:** Sharp Discount % increase (+26.2%) and PC2 surge (+21.2%) suggest aggressive discounting attracted price-sensitive customers who converted at payment but churned before shipping
- **ER decline:** Despite improved Pre-Dunning AR (+1.2%) and lower discounts (-4.4%), Ship Rate fell -9.1%—PC2 increase (+6.6%) not translating to shipments suggests fulfillment or inventory constraints
- **Payday phase transition (Mid-Cycle → Pre-Payday):** Cluster-wide improvements in AR and PC2 align with typical pre-payday liquidity patterns

**Action:** Monitor — Cluster-level improvement is positive but driven entirely by mix shift toward AO. Investigate AO's discount strategy sustainability and ER's conversion-to-ship gap if trends persist in W16.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 8,041 | 28.34% | - | 89.14% | - | 17.63% | - | 37.98% | - |
| 2026-W15 | Pre-Payday | 7,709 | 31.07% | ↑+9.6% | 90.00% | →+1.0% | 17.92% | →+1.6% | 39.89% | ↑+5.0% |

---

## L1: Country-Level Analysis

### AO (Rank #1 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 496 | 72.58% | - | 85.21% | - | 13.65% | - | 36.81% | - |
| 2026-W15 | Pre-Payday | 1,109 | 66.37% | ↓-8.6% | 87.06% | →+2.2% | 17.22% | ↑+26.2% | 44.6% | ↑+21.2% |

**Analysis:** The +2.73pp cluster-level Ship Rate improvement in W15 is attributable to favorable mix shift rather than genuine performance gains, as AO's 123.6% volume surge (despite its own -8.6% SR decline) mathematically lifted the aggregate rate. All three top countries experienced individual Ship Rate declines, with GN's -22.0% drop being most concerning. Continued monitoring is warranted to assess whether AO's volume growth is sustainable and to identify root causes for ER and GN underperformance.

### ER (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 2,556 | 26.60% | - | 89.22% | - | 19.48% | - | 40.95% | - |
| 2026-W15 | Pre-Payday | 2,345 | 24.18% | ↓-9.1% | 90.32% | →+1.2% | 18.63% | ↓-4.4% | 43.65% | ↑+6.6% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### GN (Rank #3 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 632 | 37.03% | - | 92.33% | - | 22.96% | - | 51.25% | - |
| 2026-W15 | Pre-Payday | 495 | 28.89% | ↓-22.0% | 93.32% | →+1.1% | 23.95% | ↑+4.3% | 50.54% | →-1.4% |

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
| AO | ↓-8.6% | →+2.2% | ↑+26.2% | ↑+21.2% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| ER | ↓-9.1% | →+1.2% | ↓-4.4% | ↑+6.6% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| GN | ↓-22.0% | →+1.1% | ↑+4.3% | →-1.4% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,556 | 26.60% | 2,345 | 24.18% | -8.3% | Low |
| CK | 1,491 | 47.75% | 1,439 | 47.05% | -3.5% | Medium |
| MR | 1,420 | 0.00% | 1,064 | 0.19% | -25.1% | Low |
| CG | 777 | 24.71% | 732 | 23.63% | -5.8% | Low |
| KN | 669 | 15.10% | 525 | 18.48% | -21.5% | Low |
| GN | 632 | 37.03% | 495 | 28.89% | -21.7% | Medium |
| AO | 496 | 72.58% | 1,109 | 66.37% | 123.6% | High |

---


---

*Report: 2026-04-17*
