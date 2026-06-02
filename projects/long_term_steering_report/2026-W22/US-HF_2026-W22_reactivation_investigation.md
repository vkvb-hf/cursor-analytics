# Reactivation Investigation: US-HF 2026-W22

**Metric:** Reactivation Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 88.72% → 89.95% (+1.39%)  
**Volume:** 13,381 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Reactivation Rate improved from 88.72% to 89.95% (+1.39% / +1.23pp) in US-HF for 2026-W22, representing a significant positive change on 13,381 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (89.71%-90.74%) | +1.39% | ✅ |
| L1: Country Breakdown | No countries exceeding ±2.5% threshold | +1.39% (US only) | ✅ |
| L1: Dimension Scan | PaymentMethod "Others" flagged (-100.00%) | Minimal impact (1 order) | ⚠️ |
| Mix Shift Analysis | US Medium tier stable | +5.5% volume | ✅ |

**Key Findings:**
- The +1.39% improvement represents a recovery from W21's -1.64% decline, bringing the rate back toward the 8-week average (~90%)
- Credit Card payments showed the strongest improvement (+1.66%) with the highest volume (9,211 orders, ~69% of total)
- The "Others" PaymentMethod flag is a false positive—only 1 order affected with no meaningful impact
- Volume increased +5.5% week-over-week (12,683 → 13,381), indicating healthy order flow
- All major payment methods (Credit Card, PayPal, Apple Pay) showed positive movement

**Action:** Monitor — The improvement appears to be natural recovery to baseline levels after W21's dip. No anomalies require investigation.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 89.95% | 13,381 | +1.39% ← REPORTED CHANGE |
| 2026-W21 | 88.72% | 12,683 | -1.64% |
| 2026-W20 | 90.2% | 14,787 | -0.60% |
| 2026-W19 | 90.74% | 17,431 | +0.11% |
| 2026-W18 | 90.64% | 13,634 | +1.04% |
| 2026-W17 | 89.71% | 15,063 | -0.40% |
| 2026-W16 | 90.07% | 18,897 | -0.44% |
| 2026-W15 | 90.47% | 21,155 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 89.95% | 88.72% | +1.39% | 13,381 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 0.0% | 100.0% | -100.00% | 1 | ⚠️ |
| Apple Pay | 83.31% | 82.78% | +0.64% | 2,091 |  |
| Paypal | 92.44% | 91.56% | +0.97% | 2,078 |  |
| Credit Card | 90.9% | 89.42% | +1.66% | 9,211 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 12,683 | 13,381 | +5.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-02*
