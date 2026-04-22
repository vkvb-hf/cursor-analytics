# Fraud Investigation: US-HF 2026-W16

**Metric:** Fraud Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 89.28% → 89.68% (+0.45%)  
**Volume:** 20,488 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for US-HF improved slightly from 89.28% to 89.68% (+0.45pp) in 2026-W16, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | FAR within normal range (88.55%-91.68%) | +0.45pp | ✅ |
| L1: Country Scan | No countries exceeding ±2.5% threshold | +0.45pp | ✅ |
| L1: Channel Category | Referral channel exceeded threshold | +10.21pp | ⚠️ |
| L2: US Deep-Dive | Referral PF Block rate dropped significantly | -58.26% | ⚠️ |

**Key Findings:**
- Referral channel FAR increased significantly from 61.76% to 68.07% (+10.21pp), flagged as anomalous
- Referral PF Block % dropped sharply from 12.70% to 5.30% (-58.26%), driving the FAR improvement in that channel
- Paid channel FAR decreased slightly from 95.26% to 93.77% (-1.57pp), with Dup Block % increasing from 2.90% to 4.75% (+64.19%)
- Overall Dup Rate increased from 25.91% to 27.64% (+6.68%), indicating higher duplicate submission activity
- Volume increased modestly from 20,224 to 20,488 customers (+1.3%)

**Action:** Monitor – The overall FAR change is not significant, but the substantial drop in Referral PF Block % warrants continued observation to determine if this represents a policy change or anomaly.

---

---

## L0: 8-Week Trend (US-HF)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W16 | 89.68% | 27.64% | 8.17% | 1.37% | 20,488 | +0.45% ← REPORTED CHANGE |
| 2026-W15 | 89.28% | 25.91% | 6.73% | 2.97% | 20,224 | -2.53% |
| 2026-W14 | 91.59% | 25.42% | 6.41% | 0.86% | 16,719 | +3.44% |
| 2026-W13 | 88.55% | 25.05% | 6.67% | 3.59% | 17,570 | -1.49% |
| 2026-W12 | 89.89% | 24.63% | 6.29% | 2.72% | 17,509 | +0.16% |
| 2026-W11 | 89.75% | 23.85% | 6.16% | 2.92% | 19,064 | -2.04% |
| 2026-W10 | 91.62% | 24.68% | 5.92% | 1.22% | 20,597 | -0.08% |
| 2026-W09 | 91.68% | 24.00% | 5.89% | 1.16% | 23,222 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W15 | 89.28% | - | 25.91% | - | 20,224 |  |
| US | 2026-W16 | 89.68% | +0.45% | 27.64% | +6.68% | 20,488 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 95.26% | - | 25.26% | - | 16,610 |  |
| Paid | 2026-W16 | 93.77% | -1.57% | 26.86% | +6.31% | 17,225 |  |
| Referral | 2026-W15 | 61.76% | - | 28.89% | - | 3,614 |  |
| Referral | 2026-W16 | 68.07% | +10.21% | 31.78% | +10.01% | 3,263 | ⚠️ |

---

## L2: US Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 95.26% | - | 25.26% | - | 2.90% | - | 0.85% | - | 16,610 |  |
| Paid | 2026-W16 | 93.77% | -1.57% | 26.86% | +6.31% | 4.75% | +64.19% | 0.62% | -27.34% | 17,225 |  |
| Referral | 2026-W15 | 61.76% | - | 28.89% | - | 24.35% | - | 12.70% | - | 3,614 |  |
| Referral | 2026-W16 | 68.07% | +10.21% | 31.78% | +10.01% | 26.17% | +7.48% | 5.30% | -58.26% | 3,263 | ⚠️ |

**Analysis:** The +0.45pp increase in US-HF Fraud Approval Rate is within normal weekly fluctuation and not statistically significant. The primary driver of interest is the Referral channel, where a 58.26% reduction in PF Block rate contributed to a +10.21pp FAR improvement, though this channel represents only 16% of total volume (3,263 of 20,488 customers). No immediate action is required, but the Referral channel PF Block behavior should be monitored in subsequent weeks to identify whether this is a sustained trend.

---



*Report: 2026-04-22*
