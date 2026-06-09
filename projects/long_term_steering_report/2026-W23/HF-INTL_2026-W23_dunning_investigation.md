# Dunning Investigation: HF-INTL 2026-W23

**Metric:** Dunning Ship Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 70.45% → 70.61% (+0.16pp)  
**Volume:** 28,979 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate for HF-INTL improved marginally from 70.45% to 70.61% (+0.16pp) in 2026-W23, with volume increasing slightly from 28,387 to 28,979 eligible orders during the transition from Mid-Cycle to Pre-Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 94.12% → 94.07% | -0.05pp | ✅ Stable |
| Discount % | 12.8% → 12.78% | -0.02pp | ✅ Stable |
| PC2 | 41.08% → 45.27% | +4.19pp | ✅ Improved |
| Ship Rate | 70.45% → 70.61% | +0.16pp | ✅ Improved |

**Key Findings:**
- **DK drove cluster improvement:** Ship Rate surged +9.7pp (75.32% → 82.59%) with volume up 45.4%, fueled by a -10.7% reduction in Discount % despite slight AR decline
- **SE experienced significant decline:** Ship Rate dropped -17.3pp (72.32% → 59.80%) with volume contracting -41.2%, driven by a +27.1% spike in Discount %
- **CH also declined sharply:** Ship Rate fell -15.4pp (77.52% → 65.56%) with Discount % up +31.3% and PC2 down -10.4%, though volume impact limited (90 orders)
- **Mix shift detected (Simpson's Paradox potential):** DK (+45.4% volume, high SR) expanded while SE (-41.2% volume, declining SR) contracted, favorably shifting the cluster mix
- **PC2 improved cluster-wide (+10.2%)** indicating stronger payment commitment in second payment cycle

**Action:** **Monitor** - The cluster-level improvement is modest and masked by offsetting country dynamics. Continue monitoring SE and CH for Discount % normalization in upcoming weeks; no escalation required given overall positive trajectory.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W22 | Mid-Cycle | 28,387 | 70.45% | - | 94.12% | - | 12.8% | - | 41.08% | - |
| 2026-W23 | Pre-Payday | 28,979 | 70.61% | →+0.2% | 94.07% | →-0.1% | 12.78% | →-0.2% | 45.27% | ↑+10.2% |

---

## L1: Country-Level Analysis

### DK (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W22 | Mid-Cycle | 786 | 75.32% | - | 96.62% | - | 7.26% | - | 40.29% | - |
| 2026-W23 | Pre-Payday | 1,143 | 82.59% | ↑+9.7% | 95.65% | →-1.0% | 6.48% | ↓-10.7% | 42.49% | ↑+5.5% |

**Analysis:** The HF-INTL cluster achieved a marginal +0.16pp Ship Rate improvement in 2026-W23, primarily driven by strong performance in DK (+9.7pp) which benefited from reduced discounting and significant volume expansion. However, this masks concerning deterioration in SE (-17.3pp) and CH (-15.4pp) where aggressive discounting failed to translate into improved ship rates. The favorable mix shift—with high-performing DK gaining share while underperforming SE contracted—contributed to the cluster-level stability, warranting continued monitoring rather than immediate intervention.

### FR (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W22 | Mid-Cycle | 5,147 | 68.82% | - | 94.06% | - | 10.34% | - | 41.0% | - |
| 2026-W23 | Pre-Payday | 5,899 | 70.15% | →+1.9% | 93.67% | →-0.4% | 10.62% | ↑+2.7% | 43.88% | ↑+7.0% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### SE (Rank #3 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W22 | Mid-Cycle | 867 | 72.32% | - | 96.20% | - | 7.67% | - | 38.1% | - |
| 2026-W23 | Pre-Payday | 510 | 59.80% | ↓-17.3% | 97.41% | →+1.3% | 9.75% | ↑+27.1% | 39.55% | ↑+3.8% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### CH (Rank #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W22 | Mid-Cycle | 129 | 77.52% | - | 91.55% | - | 4.12% | - | 46.42% | - |
| 2026-W23 | Pre-Payday | 90 | 65.56% | ↓-15.4% | 93.89% | ↑+2.6% | 5.41% | ↑+31.3% | 41.61% | ↓-10.4% |

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
| DK | ↑+9.7% | →-1.0% | ↓-10.7% | ↑+5.5% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| FR | →+1.9% | →-0.4% | ↑+2.7% | ↑+7.0% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| SE | ↓-17.3% | →+1.3% | ↑+27.1% | ↑+3.8% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| CH | ↓-15.4% | ↑+2.6% | ↑+31.3% | ↓-10.4% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| GB | 6,839 | 63.53% | 6,476 | 62.55% | -5.3% | High |
| FR | 5,147 | 68.82% | 5,899 | 70.15% | 14.6% | High |
| AU | 4,707 | 67.84% | 4,978 | 67.60% | 5.8% | High |
| DE | 3,440 | 73.14% | 3,254 | 72.96% | -5.4% | High |
| BE | 2,293 | 89.84% | 2,555 | 89.98% | 11.4% | High |
| NZ | 1,208 | 63.16% | 1,168 | 64.21% | -3.3% | High |
| IE | 1,053 | 65.34% | 925 | 65.08% | -12.2% | High |
| NO | 912 | 83.44% | 1,169 | 81.86% | 28.2% | High |
| SE | 867 | 72.32% | 510 | 59.80% | -41.2% | High |
| DK | 786 | 75.32% | 1,143 | 82.59% | 45.4% | High |

---


---

*Report: 2026-06-09*
