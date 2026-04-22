# Dunning Investigation: WL 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 28.34% → 31.07% (+2.73pp)  
**Volume:** 7,702 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate improved from 28.34% to 31.07% (+2.73pp) in W15, despite individual country-level declines across all major markets—indicating a classic Simpson's Paradox driven by mix shift toward higher-performing segments.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 89.14% → 90.00% | +0.86pp | ✅ |
| Discount % | 17.64% → 17.93% | +0.29pp | ⚠️ |
| PC2 | 38.43% → 39.91% | +1.48pp | ✅ |
| Ship Rate | 28.34% → 31.07% | +2.73pp | ✅ |

**Key Findings:**
- **Simpson's Paradox confirmed:** AO volume surged +123.6% (496 → 1,109 orders) while maintaining the highest SR tier (66.37%), driving cluster-level improvement despite its own -8.6% SR decline
- **AO discount spike:** Discount % increased +26.2% (13.65% → 17.22%), correlating with the -8.6% Ship Rate decline per the negative relationship framework
- **GN largest SR decline:** GN experienced the steepest Ship Rate drop (-21.8%, from 36.93% to 28.89%) with modest discount increase (+4.4%) and flat PC2
- **ER volume contraction:** Largest market by volume declined -8.3% in orders with SR dropping -9.2%, partially offset by favorable discount reduction (-4.4%)
- **Low-tier market shrinkage:** MR (-25.0%), KN (-21.5%), and GN (-21.6%) all contracted significantly, reducing drag on cluster-level metrics

**Action:** Monitor — The cluster-level improvement is primarily composition-driven rather than operational. Track AO volume sustainability and investigate the +26.2% discount increase in AO which may indicate margin pressure.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 8,034 | 28.34% | - | 89.14% | - | 17.64% | - | 38.43% | - |
| 2026-W15 | Pre-Payday | 7,702 | 31.07% | ↑+9.6% | 90.00% | →+1.0% | 17.93% | →+1.6% | 39.91% | ↑+3.9% |

---

## L1: Country-Level Analysis

### AO (Rank #1 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 496 | 72.58% | - | 85.21% | - | 13.65% | - | 43.32% | - |
| 2026-W15 | Pre-Payday | 1,109 | 66.37% | ↓-8.6% | 87.06% | →+2.2% | 17.22% | ↑+26.2% | 44.6% | ↑+3.0% |

**Analysis:** The +2.73pp Ship Rate improvement at cluster level masks underlying performance challenges, as all three top-contributing countries (AO, ER, GN) experienced individual Ship Rate declines ranging from -8.6% to -21.8%. The improvement is attributable to a significant mix shift toward AO, whose volume more than doubled (+123.6%) while maintaining the highest-tier Ship Rate despite its decline. Continued monitoring is warranted to assess whether AO's volume growth is sustainable and whether the aggressive discounting (+26.2%) in that market represents a strategic trade-off or emerging concern.

### ER (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 2,556 | 26.60% | - | 89.22% | - | 19.48% | - | 43.85% | - |
| 2026-W15 | Pre-Payday | 2,344 | 24.15% | ↓-9.2% | 90.32% | →+1.2% | 18.63% | ↓-4.4% | 43.66% | →-0.4% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### GN (Rank #3 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 631 | 36.93% | - | 92.33% | - | 22.93% | - | 50.59% | - |
| 2026-W15 | Pre-Payday | 495 | 28.89% | ↓-21.8% | 93.32% | →+1.1% | 23.95% | ↑+4.4% | 50.54% | →-0.1% |

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
| AO | ↓-8.6% | →+2.2% | ↑+26.2% | ↑+3.0% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| ER | ↓-9.2% | →+1.2% | ↓-4.4% | →-0.4% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| GN | ↓-21.8% | →+1.1% | ↑+4.4% | →-0.1% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,556 | 26.60% | 2,344 | 24.15% | -8.3% | Low |
| CK | 1,490 | 47.72% | 1,437 | 47.04% | -3.6% | Medium |
| MR | 1,415 | 0.00% | 1,061 | 0.19% | -25.0% | Low |
| CG | 777 | 24.71% | 731 | 23.67% | -5.9% | Low |
| KN | 669 | 15.10% | 525 | 18.48% | -21.5% | Low |
| GN | 631 | 36.93% | 495 | 28.89% | -21.6% | Medium |
| AO | 496 | 72.58% | 1,109 | 66.37% | 123.6% | High |

---


---

*Report: 2026-04-22*
