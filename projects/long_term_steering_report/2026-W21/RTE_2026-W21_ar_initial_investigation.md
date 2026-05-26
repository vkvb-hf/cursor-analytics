# AR Initial (LL0) Investigation: RTE 2026-W21

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 92.97% → 93.04% (+0.08%)  
**Volume:** 26,859 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) showed marginal improvement from 92.97% to 93.04% (+0.07 pp) in W21, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stable within normal range (90.9%-93.04%) | +0.08 pp | ✅ |
| L1: Country Breakdown | No countries exceeded ±2.5% threshold | TT -2.28 pp (largest decline) | ✅ |
| L1: PaymentMethod | All methods within normal variance | Others -2.18 pp | ✅ |
| L1: PaymentProvider | Unknown provider flagged | -6.74 pp (88 vol) | ⚠️ |
| L3: Related Metrics | All funnel metrics stable/improving | +0.07 pp to +0.31 pp | ✅ |
| Mix Shift | Volume drops in TT (-28.1%) and TV (-27.3%) | Minor high-tier volume loss | ⚠️ |

**Key Findings:**
- The +0.07 pp improvement continues an upward trend from W14 (90.9%) to W21 (93.04%), representing +2.14 pp gain over 8 weeks
- Unknown PaymentProvider shows a -6.74 pp decline (63.64% vs 68.24%), but with only 88 transactions, impact is negligible
- TT and TV experienced significant volume drops (-28.1% and -27.3% respectively) alongside rate declines (-2.28 pp and -1.72 pp), though combined volume is only 677 orders
- All related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) show stable or improving performance
- Total volume declined -7.0% WoW (26,859 vs 28,894), consistent with declines across most countries

**Action:** Monitor — No intervention required. The metric remains stable within expected range, and flagged items (Unknown provider, TT/TV volume) represent minimal volume impact.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 93.04% | 26,859 | +0.08% ← REPORTED CHANGE |
| 2026-W20 | 92.97% | 28,894 | +0.93% |
| 2026-W19 | 92.11% | 29,534 | -0.28% |
| 2026-W18 | 92.37% | 32,256 | -0.69% |
| 2026-W17 | 93.01% | 30,287 | +0.64% |
| 2026-W16 | 92.42% | 30,983 | +0.88% |
| 2026-W15 | 91.61% | 29,060 | +0.78% |
| 2026-W14 | 90.9% | 31,902 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TT | 95.51% | 97.74% | -2.28% | 445 |  |
| TV | 93.97% | 95.61% | -1.72% | 232 |  |
| TK | 92.80% | 93.92% | -1.19% | 264 |  |
| CF | 94.23% | 94.76% | -0.56% | 5,594 |  |
| FJ | 93.09% | 92.85% | +0.26% | 16,866 |  |
| YE | 89.93% | 89.00% | +1.06% | 2,762 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 95.19% | 97.31% | -2.18% | 957 |  |
| Apple Pay | 91.27% | 91.47% | -0.22% | 5,659 |  |
| Paypal | 95.4% | 95.11% | +0.30% | 3,236 |  |
| Credit Card | 93.06% | 92.75% | +0.33% | 17,007 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 63.64% | 68.24% | -6.74% | 88 | ⚠️ |
| Adyen | 92.58% | 92.87% | -0.31% | 7,887 |  |
| Braintree | 92.69% | 92.82% | -0.14% | 9,000 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 43 |  |
| ProcessOut | 93.95% | 93.37% | +0.62% | 9,841 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.48% | 90.75% | -0.30% | 26,859 | 28,894 |  |
| 2_PreDunningAR | 93.04% | 92.97% | +0.07% | 26,859 | 28,894 |  |
| 3_PostDunningAR | 93.39% | 93.25% | +0.15% | 26,859 | 28,894 |  |
| 6_PaymentApprovalRate | 93.67% | 93.38% | +0.31% | 26,859 | 28,894 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 17,528 | 16,866 | -3.8% | Stable |
| CF | High (>92%) | 6,164 | 5,594 | -9.2% | Stable |
| YE | Medium (>85%) | 3,135 | 2,762 | -11.9% | Stable |
| TT | High (>92%) | 619 | 445 | -28.1% | ⚠️ Volume drop |
| TZ | High (>92%) | 439 | 390 | -11.2% | Stable |
| TO | Medium (>85%) | 361 | 306 | -15.2% | Stable |
| TK | High (>92%) | 329 | 264 | -19.8% | Stable |
| TV | High (>92%) | 319 | 232 | -27.3% | ⚠️ Volume drop |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-26*
