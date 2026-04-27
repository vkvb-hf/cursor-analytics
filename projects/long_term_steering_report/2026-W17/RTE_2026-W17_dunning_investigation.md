# Dunning Investigation: RTE 2026-W17

**Metric:** Dunning Ship Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 43.82% → 43.02% (-0.80pp)  
**Volume:** 20,311 eligible orders  
**Payday Phase:** Payday → Post-Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined by 0.80pp (43.82% → 43.02%) week-over-week, coinciding with the transition from Payday to Post-Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.76% → 92.86% | +0.1% | ✅ |
| Discount % | 16.79% → 16.12% | -4.0% | ✅ |
| PC2 | 44.21% → 46.59% | +5.4% | ✅ |
| Ship Rate | 43.82% → 43.02% | -1.8% | ⚠️ |

**Key Findings:**
- FJ drove the majority of the decline as the highest-volume country (70% of orders), with Ship Rate dropping 2.6% despite stable Pre-Dunning AR and improved PC2 (+2.8%)
- TK experienced the most severe Ship Rate collapse (-43.7%), with volume increasing 43.5% while conversion plummeted from 28.26% to 15.91%
- TO showed strong counter-trend performance with Ship Rate improving +26.1%, driven by a significant Discount reduction (-30.5%) and PC2 improvement (+19.2%)
- The Payday → Post-Payday transition appears to be the primary systemic factor, as supporting metrics (AR, Discount, PC2) all moved favorably yet Ship Rate still declined
- No Simpson's Paradox detected: volume mix remained stable with FJ and YE maintaining consistent share

**Action:** Monitor - The decline aligns with expected Post-Payday seasonal patterns. Supporting metrics are healthy, suggesting this is cyclical rather than structural. Escalate only if decline persists into W18.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 20,576 | 43.82% | - | 92.76% | - | 16.79% | - | 44.21% | - |
| 2026-W17 | Post-Payday | 20,311 | 43.02% | →-1.8% | 92.86% | →+0.1% | 16.12% | ↓-4.0% | 46.59% | ↑+5.4% |

---

## L1: Country-Level Analysis

### FJ (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 14,415 | 42.68% | - | 93.79% | - | 16.68% | - | 46.82% | - |
| 2026-W17 | Post-Payday | 14,234 | 41.58% | ↓-2.6% | 93.81% | →+0.0% | 15.93% | ↓-4.5% | 48.15% | ↑+2.8% |

**Analysis:** The 0.80pp Ship Rate decline from W16 to W17 is primarily attributable to the Payday → Post-Payday phase transition, with FJ contributing most to the absolute drop due to its volume dominance. While TK showed an alarming 43.7% relative decline, its small volume (132 orders) limits cluster-level impact. Given that upstream metrics (Pre-Dunning AR, Discount %, PC2) all trended favorably, the decline appears to be a temporary cyclical effect rather than a systemic issue requiring immediate intervention.

### YE (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 3,265 | 61.29% | - | 87.83% | - | 15.1% | - | 40.22% | - |
| 2026-W17 | Post-Payday | 3,263 | 60.74% | →-0.9% | 88.43% | →+0.7% | 15.29% | →+1.3% | 49.24% | ↑+22.4% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### TK (Rank #3 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 92 | 28.26% | - | 93.65% | - | 17.84% | - | 33.73% | - |
| 2026-W17 | Post-Payday | 132 | 15.91% | ↓-43.7% | 91.98% | →-1.8% | 17.57% | →-1.5% | 38.61% | ↑+14.5% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### TO (Rank #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 230 | 23.48% | - | 88.79% | - | 28.2% | - | 26.48% | - |
| 2026-W17 | Post-Payday | 250 | 29.60% | ↑+26.1% | 87.92% | →-1.0% | 19.61% | ↓-30.5% | 31.57% | ↑+19.2% |

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
| FJ | ↓-2.6% | →+0.0% | ↓-4.5% | ↑+2.8% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| YE | →-0.9% | →+0.7% | →+1.3% | ↑+22.4% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| TK | ↓-43.7% | →-1.8% | →-1.5% | ↑+14.5% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| TO | ↑+26.1% | →-1.0% | ↓-30.5% | ↑+19.2% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| FJ | 14,415 | 42.68% | 14,234 | 41.58% | -1.3% | Medium |
| YE | 3,265 | 61.29% | 3,263 | 60.74% | -0.1% | High |
| CF | 2,261 | 30.38% | 2,049 | 30.01% | -9.4% | Medium |
| TO | 230 | 23.48% | 250 | 29.60% | 8.7% | Low |
| TZ | 144 | 29.17% | 182 | 32.97% | 26.4% | Low |
| TK | 92 | 28.26% | 132 | 15.91% | 43.5% | Low |
| TT | 85 | 38.82% | 103 | 44.66% | 21.2% | Medium |
| TV | 84 | 26.19% | 98 | 22.45% | 16.7% | Low |

---


---

*Report: 2026-04-27*
