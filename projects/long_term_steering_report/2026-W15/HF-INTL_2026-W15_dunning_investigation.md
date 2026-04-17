# Dunning Investigation: HF-INTL 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 70.87% → 65.62% (-5.25pp)  
**Volume:** 27,317 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined significantly from 70.87% to 65.62% (-5.25pp) in HF-INTL during 2026-W15, coinciding with a transition from Mid-Cycle to Pre-Payday phase and a 25.5% reduction in eligible order volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.06% → 93.83% | +0.77pp | ✅ Stable |
| Discount % | 13.57% → 13.8% | +0.23pp | ✅ Stable |
| PC2 | 42.92% → 46.31% | +3.39pp | ✅ Improved |
| Ship Rate | 70.87% → 65.62% | -5.25pp | ⚠️ Declined |

**Key Findings:**
- All four analyzed countries (GB, FR, DE, SE) experienced double-digit Ship Rate declines despite stable or improving upstream metrics (Pre-Dunning AR, PC2)
- SE showed the steepest Ship Rate decline (-14.7%) paired with an 18.7% increase in Discount %, suggesting aggressive discounting failed to convert during Pre-Payday
- DE experienced both elevated Discount % (+8.2%) and PC2 (+10.1%) increases, yet Ship Rate still fell 9.9%, indicating payment conversion issues downstream
- Volume contracted significantly across all major markets: DK (-54.7%), BE (-38.1%), FR (-30.8%), DE (-29.9%), GB (-27.7%)
- The payday phase shift from Mid-Cycle to Pre-Payday appears to be the primary driver, as all input metrics remained stable or positive while output Ship Rate declined uniformly

**Action:** **Investigate** — The disconnect between improving upstream metrics (Pre-Dunning AR, PC2) and declining Ship Rate across all markets warrants deeper analysis into payment method failures, bank decline rates, and timing sensitivity during Pre-Payday periods.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 36,656 | 70.87% | - | 93.06% | - | 13.57% | - | 42.92% | - |
| 2026-W15 | Pre-Payday | 27,317 | 65.62% | ↓-7.4% | 93.83% | →+0.8% | 13.8% | →+1.7% | 46.31% | ↑+7.9% |

---

## L1: Country-Level Analysis

### GB (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 8,721 | 64.99% | - | 93.07% | - | 16.87% | - | 46.13% | - |
| 2026-W15 | Pre-Payday | 6,301 | 57.02% | ↓-12.3% | 94.14% | →+1.1% | 17.17% | →+1.8% | 48.87% | ↑+5.9% |

**Analysis:** The 5.25pp decline in Dunning Ship Rate is primarily attributed to the Pre-Payday phase timing effect, as evidenced by uniform declines across GB (-12.3%), FR (-11.9%), DE (-9.9%), and SE (-14.7%) despite stable Pre-Dunning Acceptance Rates and increased customer engagement (PC2). Increased discounting in SE (+18.7%) and DE (+8.2%) failed to offset the payday-related payment friction, suggesting the decline is cyclical rather than systemic. Recommend monitoring through the payday transition in W16 to confirm recovery before escalating.

### FR (Rank #2 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 7,645 | 69.97% | - | 92.95% | - | 12.07% | - | 42.27% | - |
| 2026-W15 | Pre-Payday | 5,294 | 61.64% | ↓-11.9% | 94.49% | →+1.7% | 12.09% | →+0.2% | 45.11% | ↑+6.7% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### DE (Rank #3 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 4,511 | 74.73% | - | 96.44% | - | 15.89% | - | 38.13% | - |
| 2026-W15 | Pre-Payday | 3,162 | 67.33% | ↓-9.9% | 97.33% | →+0.9% | 17.19% | ↑+8.2% | 42.0% | ↑+10.1% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### SE (Rank #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 808 | 71.66% | - | 96.24% | - | 9.16% | - | 40.1% | - |
| 2026-W15 | Pre-Payday | 690 | 61.16% | ↓-14.7% | 95.19% | →-1.1% | 10.87% | ↑+18.7% | 41.77% | ↑+4.2% |

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
| GB | ↓-12.3% | →+1.1% | →+1.8% | ↑+5.9% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| FR | ↓-11.9% | →+1.7% | →+0.2% | ↑+6.7% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| DE | ↓-9.9% | →+0.9% | ↑+8.2% | ↑+10.1% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| SE | ↓-14.7% | →-1.1% | ↑+18.7% | ↑+4.2% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| GB | 8,721 | 64.99% | 6,301 | 57.02% | -27.7% | High |
| FR | 7,645 | 69.97% | 5,294 | 61.64% | -30.8% | High |
| AU | 5,849 | 66.10% | 5,021 | 64.73% | -14.2% | High |
| DE | 4,511 | 74.73% | 3,162 | 67.33% | -29.9% | High |
| BE | 3,221 | 90.50% | 1,995 | 87.57% | -38.1% | High |
| NZ | 1,302 | 61.29% | 1,132 | 69.52% | -13.1% | High |
| DK | 1,229 | 76.00% | 557 | 67.68% | -54.7% | High |
| IE | 1,149 | 65.88% | 877 | 61.80% | -23.7% | High |
| NO | 943 | 79.22% | 1,269 | 82.19% | 34.6% | High |
| SE | 808 | 71.66% | 690 | 61.16% | -14.6% | High |

---


---

*Report: 2026-04-17*
