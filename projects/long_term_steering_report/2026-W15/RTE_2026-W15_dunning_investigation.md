# Dunning Investigation: RTE 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 44.24% → 42.61% (-1.63pp)  
**Volume:** 19,543 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined by -1.63pp (from 44.24% to 42.61%) week-over-week during the transition from Mid-Cycle to Pre-Payday phase, with volume decreasing by 9.7% (21,651 → 19,543 orders).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.53% → 92.82% | +0.29pp | ✅ |
| Discount % | 17.77% → 17.50% | -0.27pp | ✅ |
| PC2 | 48.06% → 48.53% | +0.47pp | ✅ |
| Ship Rate | 44.24% → 42.61% | -1.63pp | ⚠️ |

**Key Findings:**
- **FJ drove the majority of the decline:** As the largest market (70% of volume), FJ's -5.4% Ship Rate drop (43.54% → 41.17%) was the primary contributor despite improvements in Pre-Dunning AR (+0.4%) and Discount % (-3.2%)
- **TV experienced severe Ship Rate collapse:** -59.4% relative decline (30.77% → 12.50%) despite stable supporting metrics, indicating potential operational or external factors unrelated to standard funnel metrics
- **TO showed significant deterioration:** -24.6% Ship Rate decline paired with a +9.4% increase in Discount %, suggesting aggressive discounting failed to convert during Pre-Payday phase
- **Mix shift impact detected:** High-performing YE volume decreased (-4.6%) while lower-performing TV volume increased (+5.5%), contributing to overall rate decline
- **Payday phase transition effect:** The Mid-Cycle → Pre-Payday shift appears to have negatively impacted conversion across all major markets despite stable/improving upstream metrics

**Action:** **Investigate** — The disconnect between stable/improving funnel metrics (Pre-Dunning AR, Discount %, PC2) and declining Ship Rate suggests external factors (payday timing, customer liquidity) or operational issues require deeper analysis, particularly for TV and TO markets.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 21,651 | 44.24% | - | 92.53% | - | 17.77% | - | 48.06% | - |
| 2026-W15 | Pre-Payday | 19,543 | 42.61% | ↓-3.7% | 92.82% | →+0.3% | 17.5% | →-1.5% | 48.53% | →+1.0% |

---

## L1: Country-Level Analysis

### FJ (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 15,131 | 43.54% | - | 93.62% | - | 17.72% | - | 49.74% | - |
| 2026-W15 | Pre-Payday | 13,700 | 41.17% | ↓-5.4% | 93.97% | →+0.4% | 17.16% | ↓-3.2% | 50.35% | →+1.2% |

**Analysis:** The -1.63pp decline in Dunning Ship Rate is primarily driven by FJ's volume-weighted underperformance and severe drops in smaller markets TV (-59.4%) and TO (-24.6%), occurring during the Pre-Payday phase transition when customer payment capacity is typically constrained. The paradox of declining Ship Rate despite stable or improving upstream metrics (Pre-Dunning AR +0.3%, PC2 +1.0%) suggests the root cause lies outside standard funnel optimization—likely tied to payday cycle timing effects on customer liquidity rather than operational or targeting issues.

### YE (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 3,484 | 59.62% | - | 88.14% | - | 15.93% | - | 51.18% | - |
| 2026-W15 | Pre-Payday | 3,322 | 58.79% | →-1.4% | 87.77% | →-0.4% | 16.24% | →+1.9% | 50.46% | →-1.4% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### TO (Rank #3 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 341 | 31.67% | - | 84.89% | - | 24.68% | - | 33.11% | - |
| 2026-W15 | Pre-Payday | 268 | 23.88% | ↓-24.6% | 86.67% | →+2.1% | 26.99% | ↑+9.4% | 33.0% | →-0.3% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### TV (Rank #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W14 | Mid-Cycle | 91 | 30.77% | - | 93.41% | - | 17.27% | - | 38.88% | - |
| 2026-W15 | Pre-Payday | 96 | 12.50% | ↓-59.4% | 92.14% | →-1.4% | 17.76% | ↑+2.8% | 38.46% | →-1.1% |

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
| FJ | ↓-5.4% | →+0.4% | ↓-3.2% | →+1.2% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| YE | →-1.4% | →-0.4% | →+1.9% | →-1.4% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| TO | ↓-24.6% | →+2.1% | ↑+9.4% | →-0.3% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |
| TV | ↓-59.4% | →-1.4% | ↑+2.8% | →-1.1% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| FJ | 15,131 | 43.54% | 13,700 | 41.17% | -9.5% | Medium |
| YE | 3,484 | 59.62% | 3,322 | 58.79% | -4.6% | High |
| CF | 2,192 | 30.34% | 1,882 | 30.29% | -14.1% | Medium |
| TO | 341 | 31.67% | 268 | 23.88% | -21.4% | Medium |
| TZ | 194 | 26.80% | 130 | 26.15% | -33.0% | Low |
| TK | 146 | 24.66% | 50 | 32.00% | -65.8% | Low |
| TV | 91 | 30.77% | 96 | 12.50% | 5.5% | Medium |
| TT | 72 | 33.33% | 95 | 40.00% | 31.9% | Medium |

---


---

*Report: 2026-04-22*
