# Dunning Investigation: RTE 2026-W23

**Metric:** Dunning Ship Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 44.19% → 44.16% (-0.03pp)  
**Volume:** 18,238 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate remained essentially flat at 44.16% (-0.03pp) in 2026-W23, with volume increasing 6.9% to 18,238 eligible orders during the transition from Mid-Cycle to Pre-Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.21% → 93.15% | -0.1% | ✅ |
| Discount % | 16.29% → 16.15% | -0.9% | ✅ |
| PC2 | 41.34% → 46.54% | +12.6% | ⚠️ |
| Ship Rate | 44.19% → 44.16% | -0.1% | ✅ |

**Key Findings:**
- TZ experienced a significant Ship Rate decline (-18.0%) despite improved Pre-Dunning AR (+0.9%), driven by a sharp PC2 increase (+57.0%) and higher Discount % (+16.4%), indicating potential payment collection issues during Pre-Payday transition
- TO showed strong Ship Rate improvement (+19.6%) with reduced Discount % (-9.7%) and modest PC2 increase (+7.9%), demonstrating effective dunning performance
- CF maintained slight Ship Rate improvement (+2.3%) despite a 14.6% increase in Discount %, suggesting discount strategy is compensating for Pre-Payday liquidity constraints
- TK volume surged 71.6% but Ship Rate declined to 20.53% (Low tier), contributing negatively to overall performance
- Cluster-wide PC2 increased significantly (+12.6%), which typically correlates with higher Ship Rate, but gains were offset by country-level variations

**Action:** Monitor – Overall performance is stable despite significant country-level volatility. Continue tracking TZ for potential intervention if Ship Rate decline persists through payday cycle.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W22 | Mid-Cycle | 17,067 | 44.19% | - | 93.21% | - | 16.29% | - | 41.34% | - |
| 2026-W23 | Pre-Payday | 18,238 | 44.16% | →-0.1% | 93.15% | →-0.1% | 16.15% | →-0.9% | 46.54% | ↑+12.6% |

---

## L1: Country-Level Analysis

### CF (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W22 | Mid-Cycle | 1,911 | 30.82% | - | 93.73% | - | 18.4% | - | 37.16% | - |
| 2026-W23 | Pre-Payday | 2,144 | 31.53% | →+2.3% | 93.40% | →-0.4% | 21.08% | ↑+14.6% | 37.52% | →+1.0% |

**Analysis:** The Dunning Ship Rate remained stable at 44.16% despite mixed country-level performance, with TO and CF improvements largely offsetting TZ's 18.0% decline. The Pre-Payday phase transition appears to be driving increased PC2 and Discount % across markets, with varying effectiveness. No immediate escalation is required, but TZ warrants close monitoring given its disproportionate decline relative to volume growth.

### TZ (Rank #2 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W22 | Mid-Cycle | 142 | 40.14% | - | 91.04% | - | 12.45% | - | 19.74% | - |
| 2026-W23 | Pre-Payday | 164 | 32.93% | ↓-18.0% | 91.90% | →+0.9% | 14.49% | ↑+16.4% | 31.0% | ↑+57.0% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### TO (Rank #3 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W22 | Mid-Cycle | 175 | 30.86% | - | 90.55% | - | 20.85% | - | 22.62% | - |
| 2026-W23 | Pre-Payday | 187 | 36.90% | ↑+19.6% | 90.72% | →+0.2% | 18.83% | ↓-9.7% | 24.4% | ↑+7.9% |

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
| CF | →+2.3% | →-0.4% | ↑+14.6% | →+1.0% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| TZ | ↓-18.0% | →+0.9% | ↑+16.4% | ↑+57.0% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| TO | ↑+19.6% | →+0.2% | ↓-9.7% | ↑+7.9% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| FJ | 12,042 | 43.32% | 12,775 | 43.34% | 6.1% | Medium |
| YE | 2,540 | 61.14% | 2,668 | 61.39% | 5.0% | High |
| CF | 1,911 | 30.82% | 2,144 | 31.53% | 12.2% | Medium |
| TO | 175 | 30.86% | 187 | 36.90% | 6.9% | Medium |
| TZ | 142 | 40.14% | 164 | 32.93% | 15.5% | Medium |
| TK | 88 | 26.14% | 151 | 20.53% | 71.6% | Low |
| TT | 85 | 37.65% | 92 | 40.22% | 8.2% | Medium |
| TV | 84 | 20.24% | 57 | 21.05% | -32.1% | Low |

---


---

*Report: 2026-06-09*
