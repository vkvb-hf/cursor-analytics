# Fraud Investigation: HF-NA 2026-W16

**Metric:** Fraud Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 89.70% → 89.82% (+0.14%)  
**Volume:** 27,399 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

**Overall:** The HF-NA Fraud Approval Rate showed a marginal improvement from 89.70% to 89.82% (+0.14%), which is not statistically significant, with volume remaining stable at 27,399 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Regional Trend | FAR within normal 8-week range (89.11%-91.58%) | +0.14% | ✅ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | US +0.45%, CA -0.66% | ✅ |
| L1: Channel Category | Referral channel exceeds threshold | +5.87% | ⚠️ |
| L2: CA Deep-Dive | Referral channel decline with elevated PF Block | -4.17% FAR, +42.91% PF Block | ⚠️ |
| L2: US Deep-Dive | Referral channel significant improvement | +10.21% FAR, -58.26% PF Block | ⚠️ |

**Key Findings:**
- Duplicate Rate increased across all segments, rising from 26.48% to 28.10% (+1.62pp) at the regional level, with US Paid channel showing +64.19% increase in Dup Block Rate
- US Referral channel showed substantial FAR improvement (+10.21%) driven by a significant decrease in PF Block Rate (-58.26%, from 12.70% to 5.30%)
- CA Referral channel moved in the opposite direction with FAR declining -4.17% and PF Block Rate spiking +42.91% (from 2.97% to 4.24%)
- Paid channels in both countries showed slight FAR declines (US -1.57%, CA +0.42%) while Referral channels exhibited high volatility
- Overall volume decreased slightly (-1.0%) from 27,685 to 27,399 customers

**Action:** Monitor – The overall metric change is not significant and falls within normal operating range. Continue monitoring the divergent Referral channel behavior between US and CA, particularly the elevated PF Block Rate in CA Referral and increased Duplicate Block Rates in US Paid channel.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W16 | 89.82% | 28.10% | 7.72% | 1.60% | 27,399 | +0.14% ← REPORTED CHANGE |
| 2026-W15 | 89.70% | 26.48% | 6.42% | 2.73% | 27,685 | -1.40% |
| 2026-W14 | 90.97% | 25.99% | 6.42% | 1.36% | 23,597 | +2.09% |
| 2026-W13 | 89.11% | 25.96% | 6.23% | 3.32% | 24,577 | -1.35% |
| 2026-W12 | 90.33% | 25.53% | 6.01% | 2.49% | 24,830 | +0.07% |
| 2026-W11 | 90.26% | 24.95% | 5.88% | 2.65% | 26,801 | -1.38% |
| 2026-W10 | 91.52% | 25.46% | 5.83% | 1.39% | 27,713 | -0.06% |
| 2026-W09 | 91.58% | 24.86% | 5.80% | 1.26% | 30,553 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W15 | 89.28% | - | 25.91% | - | 20,224 |  |
| US | 2026-W16 | 89.68% | +0.45% | 27.64% | +6.68% | 20,488 |  |
| CA | 2026-W15 | 90.85% | - | 28.03% | - | 7,461 |  |
| CA | 2026-W16 | 90.25% | -0.66% | 29.47% | +5.17% | 6,911 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 95.50% | - | 25.45% | - | 22,689 |  |
| Paid | 2026-W16 | 94.44% | -1.10% | 27.00% | +6.07% | 22,768 |  |
| Referral | 2026-W15 | 63.37% | - | 31.14% | - | 4,996 |  |
| Referral | 2026-W16 | 67.09% | +5.87% | 33.53% | +7.67% | 4,631 | ⚠️ |

---

## L2: CA Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 96.13% | - | 25.97% | - | 0.61% | - | 1.89% | - | 6,079 |  |
| Paid | 2026-W16 | 96.54% | +0.42% | 27.44% | +5.64% | 0.72% | +18.56% | 1.82% | -3.68% | 5,543 |  |
| Referral | 2026-W15 | 67.58% | - | 37.05% | - | 27.42% | - | 2.97% | - | 1,382 |  |
| Referral | 2026-W16 | 64.77% | -4.17% | 37.72% | +1.81% | 29.46% | +7.42% | 4.24% | +42.91% | 1,368 | ⚠️ |

**Analysis:** The W16 Fraud Approval Rate increase of +0.14% represents normal week-over-week fluctuation within the established 8-week range and requires no immediate action. The most notable patterns are the contrasting Referral channel performance between US (+10.21% FAR improvement) and CA (-4.17% FAR decline), along with rising Duplicate Rates across all segments. These channel-level dynamics should be monitored in subsequent weeks to determine if they represent emerging trends requiring intervention.

---

## L2: US Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 95.26% | - | 25.26% | - | 2.90% | - | 0.85% | - | 16,610 |  |
| Paid | 2026-W16 | 93.77% | -1.57% | 26.86% | +6.31% | 4.75% | +64.19% | 0.62% | -27.34% | 17,225 |  |
| Referral | 2026-W15 | 61.76% | - | 28.89% | - | 24.35% | - | 12.70% | - | 3,614 |  |
| Referral | 2026-W16 | 68.07% | +10.21% | 31.78% | +10.01% | 26.17% | +7.48% | 5.30% | -58.26% | 3,263 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---



*Report: 2026-04-21*
