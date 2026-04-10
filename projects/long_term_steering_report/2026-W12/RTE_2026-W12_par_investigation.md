# PAR Investigation: RTE 2026-W12

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 94.94% → 94.76% (-0.19%)  
**Volume:** 431,853 orders

## Executive Summary

**Overall:** PAR declined by 0.19 percentage points (94.94% → 94.76%) on a volume of 431,853 orders, continuing a two-week downward trend from the 95.18% peak in W12.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate declining for 2 consecutive weeks | -0.19 pp | ⚠️ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | Max Δ: -1.64 pp (TK) | ✅ |
| L1: Payment Method | All methods within normal range | Max Δ: -0.10 pp (Others) | ✅ |
| L1: Payment Provider | Unknown provider shows -12.50 pp drop | Volume: 24 orders | ⚠️ |

**Key Findings:**
- The PAR rate has declined for two consecutive weeks, dropping 0.42 pp from the W12 peak of 95.18% to current 94.76%
- TK showed the largest country-level decline at -1.64 pp (93.49% → 91.96%), though on low volume (2,338 orders)
- The "Unknown" payment provider experienced a significant -12.50 pp drop (42.86% → 37.5%), but represents negligible volume (24 orders)
- FJ, representing 95% of total volume (408,532 orders), showed a minor decline of -0.17 pp, contributing most to the overall metric movement
- No single dimension shows a clear root cause exceeding alerting thresholds on significant volume

**Action:** Monitor – The decline is modest (-0.19 pp) with no dimension breaching the ±2.5% threshold on meaningful volume. Continue tracking the trend; escalate if decline persists into W15 or any dimension exceeds threshold.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 94.76% | 431,853 | -0.19% |
| 2026-W13 | 94.94% | 442,530 | -0.25% |
| 2026-W12 | 95.18% | 443,994 | +0.08% ← REPORTED CHANGE |
| 2026-W11 | 95.1% | 458,408 | +1.80% |
| 2026-W10 | 93.42% | 467,998 | +0.17% |
| 2026-W09 | 93.26% | 466,696 | +0.20% |
| 2026-W08 | 93.07% | 462,049 | -0.04% |
| 2026-W07 | 93.11% | 474,461 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TK | 91.96% | 93.49% | -1.64% | 2,338 |  |
| TV | 93.47% | 94.31% | -0.89% | 2,205 |  |
| TO | 86.85% | 87.27% | -0.49% | 3,611 |  |
| FJ | 94.3% | 94.46% | -0.17% | 408,532 |  |
| CF | 93.62% | 93.52% | +0.10% | 53,267 |  |
| YE | 88.62% | 88.28% | +0.39% | 48,432 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 97.73% | 97.83% | -0.10% | 7,260 |
| PaymentMethod | Apple Pay | 92.72% | 92.79% | -0.07% | 55,075 |
| PaymentMethod | Paypal | 97.65% | 97.61% | +0.04% | 57,396 |
| PaymentMethod | Credit Card | 95.1% | 94.99% | +0.12% | 324,263 |
| PaymentProvider | Unknown | 37.5% | 42.86% | -12.50% | 24 |
| PaymentProvider | ProcessOut | 93.6% | 93.67% | -0.07% | 48,689 |
| PaymentProvider | Braintree | 95.93% | 95.85% | +0.08% | 314,194 |
| PaymentProvider | Adyen | 93.14% | 92.84% | +0.33% | 78,682 |
| PaymentProvider | No Payment | 95.47% | 94.94% | +0.56% | 2,405 |

---

*Report: 2026-04-10*
