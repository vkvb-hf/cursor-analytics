# Reactivation Investigation: US-HF 2026-W17

**Metric:** Reactivation Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 90.07% → 89.71% (-0.40%)  
**Volume:** 15,063 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** US-HF Reactivation Rate declined modestly from 90.07% to 89.71% (-0.36pp) in W17, a statistically non-significant change within normal weekly fluctuation.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (87.76%-91.26%) | -0.36pp | ✅ |
| L1: Country Breakdown | US only; no countries exceeding ±2.5% threshold | -0.40% | ✅ |
| L1: Dimension Scan | PayPal showed largest decline (-1.49%); Others flagged but n=1 | Minor | ✅ |
| Mix Shift Analysis | US Medium tier volume dropped 20.3% (18,897→15,063) | Volume ⚠️ | ⚠️ |

**Key Findings:**
- The -0.36pp decline is **not statistically significant** and falls within the 8-week range of 87.76% to 91.26%
- **PayPal** showed the largest payment method decline (-1.49%, from 93.17% to 91.79%) on 2,532 orders
- **Volume decreased 20.3%** week-over-week (18,897 → 15,063 orders), which is a notable shift in the Medium AR tier
- The "Others" payment method flag (⚠️ +100%) is a false positive based on only 1 order
- Credit Card (n=10,229) remains stable at 89.77% (-0.14%), representing 68% of volume

**Action:** Monitor — No immediate investigation required. Continue tracking PayPal performance and volume trends over the next 1-2 weeks to confirm stability.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 89.71% | 15,063 | -0.40% ← REPORTED CHANGE |
| 2026-W16 | 90.07% | 18,897 | -0.44% |
| 2026-W15 | 90.47% | 21,155 | -0.57% |
| 2026-W14 | 90.99% | 14,736 | +0.40% |
| 2026-W13 | 90.63% | 15,928 | -0.69% |
| 2026-W12 | 91.26% | 15,787 | +2.56% |
| 2026-W11 | 88.98% | 17,703 | +1.39% |
| 2026-W10 | 87.76% | 22,710 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 89.71% | 90.07% | -0.40% | 15,063 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 91.79% | 93.17% | -1.49% | 2,532 |  |
| Apple Pay | 87.14% | 87.56% | -0.48% | 2,301 |  |
| Credit Card | 89.77% | 89.9% | -0.14% | 10,229 |  |
| Others | 100.0% | 50.0% | +100.00% | 1 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 18,897 | 15,063 | -20.3% | ⚠️ Volume drop |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-28*
