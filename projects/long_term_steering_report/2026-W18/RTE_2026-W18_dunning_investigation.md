# Dunning Investigation: RTE 2026-W18

**Metric:** Dunning Ship Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 42.88% → 41.70% (-1.18pp)  
**Volume:** 20,964 eligible orders  
**Payday Phase:** Post-Payday → Mid-Cycle

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined from 42.88% to 41.70% (-1.18pp) in W18, driven primarily by FJ's significant performance drop during the Mid-Cycle payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.85% → 92.72% | -0.13pp | ✅ Stable |
| Discount % | 16.13% → 16.59% | +0.46pp | ⚠️ Higher discounts not converting |
| PC2 | 42.77% → 46.46% | +3.69pp | ⚠️ Engagement up but SR down |
| Ship Rate | 42.88% → 41.70% | -1.18pp | ⚠️ Decline |

**Key Findings:**
- **FJ dominates the decline:** FJ (70% of volume) saw Ship Rate drop -4.4% (41.44% → 39.62%), contributing most to cluster-level decline despite stable Pre-Dunning AR
- **Payday phase impact:** Transition from Post-Payday to Mid-Cycle correlates with reduced customer payment capacity across markets
- **PC2 paradox:** Cluster-wide PC2 increased +8.6% yet Ship Rate declined, suggesting engagement isn't translating to conversions during Mid-Cycle
- **Smaller markets improved:** TK (+49.9%), TO (+14.6%), and CF (+4.9%) all showed Ship Rate gains, but insufficient volume to offset FJ's decline
- **Mix shift detected:** TV volume increased +39.8% but remains a low SR tier (22.63%), potentially diluting overall performance

**Action:** **Investigate** - Focus on FJ's Mid-Cycle performance; the disconnect between rising PC2/Discount % and declining Ship Rate suggests potential customer payment capacity issues or offer effectiveness problems specific to this payday phase.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W17 | Post-Payday | 20,231 | 42.88% | - | 92.85% | - | 16.13% | - | 42.77% | - |
| 2026-W18 | Mid-Cycle | 20,964 | 41.70% | ↓-2.8% | 92.72% | →-0.1% | 16.59% | ↑+2.9% | 46.46% | ↑+8.6% |

---

## L1: Country-Level Analysis

### FJ (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W17 | Post-Payday | 14,183 | 41.44% | - | 93.80% | - | 15.94% | - | 44.28% | - |
| 2026-W18 | Mid-Cycle | 14,709 | 39.62% | ↓-4.4% | 93.69% | →-0.1% | 16.39% | ↑+2.8% | 47.85% | ↑+8.1% |

**Analysis:** The -1.18pp Ship Rate decline is concentrated in FJ, where the Mid-Cycle payday phase appears to limit customer conversion despite increased engagement (PC2 +8.1%) and higher discount offers (+2.8%). While smaller markets like TK, TO, and CF showed resilience with improved performance, their combined volume is insufficient to counterbalance FJ's dominant negative contribution. Recommend investigating FJ-specific dunning strategies for Mid-Cycle timing and evaluating whether current discount levels are appropriately calibrated for customer payment capacity during this phase.

### CF (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W17 | Post-Payday | 2,036 | 29.76% | - | 93.93% | - | 18.4% | - | 39.27% | - |
| 2026-W18 | Mid-Cycle | 2,099 | 31.21% | ↑+4.9% | 93.81% | →-0.1% | 19.69% | ↑+7.0% | 39.46% | →+0.5% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### TO (Rank #3 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W17 | Post-Payday | 250 | 29.60% | - | 87.92% | - | 19.52% | - | 24.49% | - |
| 2026-W18 | Mid-Cycle | 280 | 33.93% | ↑+14.6% | 86.87% | →-1.2% | 20.54% | ↑+5.2% | 31.72% | ↑+29.5% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### TK (Rank #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W17 | Post-Payday | 132 | 15.91% | - | 91.98% | - | 17.57% | - | 32.14% | - |
| 2026-W18 | Mid-Cycle | 130 | 23.85% | ↑+49.9% | 90.23% | →-1.9% | 16.9% | ↓-3.8% | 38.64% | ↑+20.2% |

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
| FJ | ↓-4.4% | →-0.1% | ↑+2.8% | ↑+8.1% | Post-Payday → Mid-Cycle | [AI_SUMMARY_PLACEHOLDER] |
| CF | ↑+4.9% | →-0.1% | ↑+7.0% | →+0.5% | Post-Payday → Mid-Cycle | [AI_SUMMARY_PLACEHOLDER] |
| TO | ↑+14.6% | →-1.2% | ↑+5.2% | ↑+29.5% | Post-Payday → Mid-Cycle | [AI_SUMMARY_PLACEHOLDER] |
| TK | ↑+49.9% | →-1.9% | ↓-3.8% | ↑+20.2% | Post-Payday → Mid-Cycle | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| FJ | 14,183 | 41.44% | 14,709 | 39.62% | 3.7% | Medium |
| YE | 3,247 | 60.61% | 3,315 | 60.33% | 2.1% | High |
| CF | 2,036 | 29.76% | 2,099 | 31.21% | 3.1% | Low |
| TO | 250 | 29.60% | 280 | 33.93% | 12.0% | Low |
| TZ | 182 | 32.97% | 191 | 28.80% | 4.9% | Medium |
| TK | 132 | 15.91% | 130 | 23.85% | -1.5% | Low |
| TT | 103 | 44.66% | 103 | 46.60% | 0.0% | Medium |
| TV | 98 | 22.45% | 137 | 22.63% | 39.8% | Low |

---


---

*Report: 2026-05-05*
