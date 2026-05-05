# Steering Report - 2026-W18 (v3)

**Week:** 2026-W18  
**Generated:** 2026-05-05 14:42

---

## Payment Checkout Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 96.34% to 94.90% (↓1.49%, not sig., vol: 1.6K)
- **HF-NA**: 93.94% to 92.45% (↓1.59%, not sig., vol: 336.4)
- **HF-INTL**: 96.67% to 94.18% (↓2.58%, not sig., vol: 881.0)
- **US-HF**: 92.67% to 91.13% (↓1.66%, not sig., vol: 272.0)
- **RTE**: 97.05% to 96.52% (↓0.55%, not sig., vol: 221.9)
- **WL**: 97.02% to 96.02% (↓1.04%, not sig., vol: 111.4)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: DE (↓5%), FR (↓4%), DK (↓5%), BE (↑3%), NO (↓3%)
  - RTE: TO (↓6%), TV (↓4%)
**Dimensions:**
[2.5% - 19%]
  - HF-INTL: FinalTokenType true (↓3%), PM Credit Card (↓4%), PM Others (↓6%)
**Low Volume (denom < 50):** 3 segments excluded

### Overall Summary

Payment Checkout Approval Rate declined across all clusters in 2026-W18, with HF-INTL experiencing the most severe drop of -2.58% (96.67% → 94.18%). Credit Card payment method degradation was the common thread across multiple clusters, with ProcessOut and Adyen provider issues identified as key contributors in affected markets.

### Cluster Highlights

- **US-HF:** Declined by -1.66% to 91.13%, driven primarily by Credit Card approval rate dropping -2.40% across 9,210 orders (56% of volume).
- **HF-INTL:** Declined significantly by -2.58% to 94.18%, with four countries exceeding threshold (LU -8.57%, DK -5.01%, DE -4.65%, FR -4.06%) due to ProcessOut and Adyen provider issues.
- **WL:** Declined by -1.03% to 96.02%, with Credit Card payments dropping -1.76% affecting 5,995 orders, though no individual country exceeded the ±2.5% threshold.
- **HF-NA:** Declined by -1.59% to 92.45%, driven by Credit Card payment method decline of -2.12% impacting both US (-1.66%) and CA (-1.06%).
- **RTE:** Declined by -0.55% to 96.52% (not statistically significant), with isolated issues in low-volume markets TO (-5.64%) and TV (-4.00%) linked to Adyen provider performance.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W18

---

## Payment Page Visit to Success

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 34.04% to 32.59% (↓4.28%, not sig., vol: 10.4K)
- **HF-NA**: 27.35% to 25.11% (↓8.19%, not sig., vol: 5.6K)
- **HF-INTL**: 35.94% to 36.45% (↑1.40%, not sig., vol: 989.9)
- **US-HF**: 25.29% to 23.27% (↓8.00%, not sig., vol: 4.3K)
- **RTE**: 39.39% to 37.83% (↓3.95%, not sig., vol: 2.6K)
- **WL**: 31.83% to 29.70% (↓6.68%, not sig., vol: 2.5K)

**Deep Insights**
**Business Units:**
[5.0% - 19%]
  - HF-NA: US (↓8%), CA (↓7%)
  - RTE: YE (↓16%), TO (↓11%), TZ (↓8%), TV (↓11%)
  - HF-INTL: FR (↑6%), DE (↑6%), NL (↑6%), DK (↑8%), NO (↓9%)
  - WL: ER (↓10%), CK (↓8%), AO (↓19%)
**Low Volume (denom < 50):** 1 segment excluded

### Overall Summary

Payment Conversion Rate (Checkout) declined across most clusters in 2026-W18, with decreases ranging from -1.57pp to -2.20pp in four of five clusters. The most critical concern is a cross-cluster PVS routing issue, evidenced by significant "Call to PVS" conversion drops in US-HF (-2.64pp), HF-NA (-1.84pp), and HF-INTL (-1.00pp at Successful Checkout), alongside a new Adyen_CreditCard integration causing 100% fraud service bypass in US-HF.

### Cluster Highlights

- **US-HF:** PCR declined by -2.02pp (25.39% → 23.37%), primarily driven by a -2.64pp drop in Call to PVS step and a new Adyen_CreditCard integration with 0% success rate on 90 attempts.
- **HF-INTL:** PCR improved by +0.49pp (36.00% → 36.49%), though a new PVS error type "CHARGE_STATE_FAILURE" emerged with 226 occurrences while NO experienced a -4.32pp country-level decline.
- **WL:** PCR declined by -2.11pp (31.86% → 29.74%), driven by a -2.89pp drop in Select Payment Method conversion, with AO experiencing the steepest country-level decline (-10.06pp).
- **HF-NA:** PCR declined by -2.20pp (27.42% → 25.22%), with Adyen_CreditCard success rate dropping -10.43pp and PVS routing issues causing a -1.84pp drop in Call to PVS step.
- **RTE:** PCR declined by -1.57pp (39.46% → 37.88%), primarily due to a -1.44pp drop in Select Payment Method conversion, with YE showing the most severe country-level decline (-6.32pp).

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W18

---

## Payment Page Visit to Success (Backend)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 33.48% to 32.72% (↓2.29%, not sig., vol: 7.4K)
- **HF-NA**: 29.21% to 26.79% (↓8.29%, not sig., vol: 6.1K)
- **HF-INTL**: 39.12% to 39.05% (↓0.19%, not sig., vol: 168.0)
- **US-HF**: 27.06% to 24.89% (↓8.03%, not sig., vol: 4.7K)
- **RTE**: 33.10% to 33.35% (↑0.75%, not sig., vol: 886.4)
- **WL**: 29.36% to 28.29% (↓3.64%, not sig., vol: 1.6K)

**Deep Insights**
**Business Units:**
[5.0% - 19%]
  - HF-NA: US (↓8%), CA (↓7%)
  - RTE: YE (↓10%), TO (↓13%), TT (↑5%), TV (↓8%), TK (↑6%)
  - HF-INTL: DE (↑5%), AU (↓6%), NL (↑6%), IE (↓5%), CH (↓5%)
  - WL: AO (↓12%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W18

---

## Reactivation Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 89.43% to 89.32% (↓0.12%, not sig., vol: 110.3)
- **HF-NA**: 90.35% to 90.48% (↑0.14%, not sig., vol: 27.5)
- **HF-INTL**: 90.74% to 90.32% (↓0.46%, not sig., vol: 201.3)
- **US-HF**: 89.71% to 90.64% (↑1.04%, not sig., vol: 141.5)
- **RTE**: 87.33% to 87.04% (↓0.33%, not sig., vol: 66.2)
- **WL**: 85.35% to 86.51% (↑1.37%, not sig., vol: 101.6)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - WL: AO (↑23%)
[2.5% - 19%]
  - RTE: YE (↓5%)
  - WL: CK (↓3%), KN (↑4%)
  - HF-INTL: IE (↓3%)
**Dimensions:**
[2.5% - 19%]
  - RTE: PM Apple Pay (↑6%)
  - WL: PM Apple Pay (↑4%)
**Low Volume (denom < 50):** 6 segments excluded

### Overall Summary

Reactivation Rate performance was mixed across clusters in 2026-W18, with US-HF and WL showing significant improvements (+1.04pp and +1.36pp respectively) while HF-INTL and RTE experienced minor non-significant declines. The most notable concern is the WL cluster's CK market, which declined -3.27pp with elevated "Blocked, Restricted, Not Permitted" decline reasons, alongside an 84% volume collapse in AO requiring immediate investigation.

### Cluster Highlights

- **US-HF:** Improved significantly by +1.04pp to 90.64%, reversing three consecutive weeks of decline, driven by PayPal (+1.80pp) and Credit Card (+1.22pp) performance gains.
- **HF-INTL:** Declined marginally by -0.46pp to 90.32% (not significant), with IE showing the only material concern at -2.60pp driven by Credit Card expired/invalid card issues.
- **WL:** Improved significantly by +1.36pp to 86.51%, though CK declined -3.27pp across all payment methods and AO experienced an 84% volume collapse requiring investigation.
- **HF-NA:** Stable at 90.48% (+0.14pp, not significant), with CA's -2.11pp decline offset by US's +1.04pp improvement due to higher volume weighting.
- **RTE:** Declined marginally by -0.33pp to 87.04% (not significant), with YE Credit Card underperforming at -7.70pp on increased volume (+66.2%), warranting continued monitoring.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W18

---

## Fraud Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 92.47% to 92.79% (↑0.35%, not sig., vol: 436.9)
- **HF-NA**: 90.70% to 91.71% (↑1.11%, not sig., vol: 276.7)
- **HF-INTL**: 92.13% to 91.87% (↓0.28%, not sig., vol: 118.4)
- **US-HF**: 91.29% to 92.25% (↑1.04%, not sig., vol: 194.7)
- **RTE**: 93.94% to 94.29% (↑0.37%, not sig., vol: 158.0)
- **WL**: 91.76% to 92.87% (↑1.21%, not sig., vol: 170.5)

**Deep Insights**
**Business Units:**
[5.0% - 19%]
  - RTE: TK (↑8%)
  - HF-INTL: LU (↑6%)
**Dimensions:**
[20% - 49%]
  - RTE: PM Unknown (↓22%)
**Low Volume (denom < 50):** 3 segments excluded

### Overall Summary

Fraud Approval Rate improved across most clusters in 2026-W18, with significant gains in US-HF (+1.04pp to 92.25%), WL (+1.21pp to 92.87%), and HF-NA (+1.11pp to 91.71%), while HF-INTL and RTE showed non-significant changes. The most notable finding is the consistent reduction in Duplicate Block rates driving FAR improvements across multiple clusters, particularly in Referral channels.

### Cluster Highlights

- **US-HF:** FAR improved significantly by +1.04pp to 92.25% (8-week high), driven by Duplicate Rate reduction from 26.65% to 24.51% with Paid channel performing strongly at 96.78%.
- **HF-INTL:** FAR declined marginally by -0.28pp to 91.87% (not significant), with AU Paid channel showing elevated PF Block (+228.89% to 3.99%) requiring monitoring.
- **WL:** FAR improved significantly by +1.21pp to 92.87%, driven by Referral channel gains (+4.20pp) from reduced duplicate blocking across all markets, particularly AO (+3.22pp).
- **HF-NA:** FAR improved significantly by +1.11pp to 91.71% (8-week high), driven by US Duplicate Rate decrease of -8.03% while Referral channel remained stable at 66.36%.
- **RTE:** FAR improved marginally by +0.37pp to 94.29% (not significant), with TK showing anomalous +8.34pp increase in Paid channel warranting monitoring for sustained pattern changes.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W18

---

## Total Duplicate Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 25.16% to 24.85% (↓1.23%, not sig., vol: 1.5K)
- **HF-NA**: 28.07% to 26.57% (↓5.34%, not sig., vol: 1.3K)
- **HF-INTL**: 34.94% to 34.51% (↓1.21%, not sig., vol: 501.4)
- **US-HF**: 26.91% to 24.71% (↓8.19%, not sig., vol: 1.5K)
- **RTE**: 16.70% to 17.03% (↑2.01%, not sig., vol: 861.8)
- **WL**: 18.07% to 17.02% (↓5.79%, not sig., vol: 808.9)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - HF-INTL: NO (↓21%), AT (↓22%)
  - RTE: TZ (↑26%), TK (↓29%)
[10.0% - 19%]
  - WL: MR (↓15%), AO (↓11%)
  - HF-INTL: IE (↑10%)
  - RTE: TV (↑12%), TO (↓11%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W18

---

## Total Duplicate Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 5.82% to 5.72% (↓1.72%, not sig., vol: 2.1K)
- **HF-NA**: 6.98% to 6.08% (↓12.95%, not sig., vol: 3.2K)
- **HF-INTL**: 6.31% to 6.61% (↑4.80%, not sig., vol: 2.0K)
- **US-HF**: 6.85% to 5.76% (↓15.99%, not sig., vol: 3.0K)
- **RTE**: 4.74% to 4.77% (↑0.56%, not sig., vol: 238.2)
- **WL**: 5.84% to 5.36% (↓8.17%, not sig., vol: 1.1K)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: IE (↑54%), NO (↓61%), LU (↓100%)
[20% - 49%]
  - RTE: YE (↑25%), TZ (↑28%), TK (↓40%)
  - HF-INTL: BE (↓40%), DK (↓43%), NZ (↓22%), AT (↓28%)
[10.0% - 19%]
  - HF-NA: US (↓16%)
  - HF-INTL: GB (↑16%)
  - WL: MR (↑14%), CG (↓14%), AO (↓14%)
  - RTE: TV (↑17%), TO (↓11%)
**Dimensions:**
[20% - 49%]
  - HF-NA: CC Paid (↓24%)
[10.0% - 19%]
  - RTE: CC Paid (↓15%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W18

---

## Payment Fraud Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 0.60% to 0.73% (↑21.94%, not sig., vol: 27.0K)
- **HF-NA**: 1.22% to 1.44% (↑17.87%, not sig., vol: 4.4K)
- **HF-INTL**: 0.32% to 0.60% (↑83.46%, not sig., vol: 34.7K)
- **US-HF**: 0.96% to 1.25% (↑30.69%, not sig., vol: 5.7K)
- **RTE**: 0.36% to 0.29% (↓18.87%, not sig., vol: 8.1K)
- **WL**: 1.12% to 1.22% (↑8.81%, not sig., vol: 1.2K)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: DE (↑403%), NL (↑558%), AU (↑213%), SE (↓100%), DK (↑84%)
  - WL: CK (↓100%), KN (↑53%)
  - RTE: TK (↓100%)
[20% - 49%]
  - HF-NA: US (↑31%)
  - HF-INTL: FR (↑41%), GB (↓25%), BE (↓26%)
  - WL: MR (↑42%), ER (↓33%)
[10.0% - 19%]
  - RTE: FJ (↓17%)
  - WL: CG (↑11%)
  - HF-INTL: CH (↑15%)
**Dimensions:**
[+50%]
  - HF-INTL: CC Paid (↑113%)
  - HF-NA: CC Referral (↑155%)
  - WL: CC Referral (↓61%)
[20% - 49%]
  - RTE: CC Paid (↓25%), CC Referral (↑38%)
  - HF-NA: CC Paid (↓21%)
[10.0% - 19%]
  - WL: CC Paid (↑16%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W18

---

## Payment Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 95.42% to 95.25% (↓0.18%, not sig., vol: 3.4K)
- **HF-NA**: 94.02% to 93.93% (↓0.10%, not sig., vol: 501.3)
- **HF-INTL**: 97.42% to 97.29% (↓0.13%, not sig., vol: 1.0K)
- **US-HF**: 93.79% to 93.62% (↓0.18%, not sig., vol: 762.3)
- **RTE**: 94.83% to 94.65% (↓0.19%, not sig., vol: 820.3)
- **WL**: 91.67% to 91.24% (↓0.47%, not sig., vol: 786.4)

**Deep Insights**
**Dimensions:**
[2.5% - 19%]
  - WL: CustomerQuality Bad (↓13%)
  - HF-NA: CustomerQuality Bad (↓5%), LL a. 0 (↓3%)
  - HF-INTL: CustomerQuality Bad (↓7%)
  - RTE: CustomerQuality Bad (↓7%)

### Overall Summary

Payment Approval Rate declined marginally across all clusters in 2026-W18, with changes ranging from -0.10pp to -0.47pp, none of which were statistically significant. The most notable pattern was a consistent decline in First Run Approval Rate across clusters (particularly HF-INTL at -1.08pp), though dunning recovery processes largely mitigated the impact on final approval rates.

### Cluster Highlights

- **US-HF:** Declined by -0.17pp to 93.62%, a non-significant change within normal variance with no country or payment method exceeding alert thresholds.
- **HF-INTL:** Declined by -0.13pp to 97.29%, with First Run AR showing the largest upstream drop (-1.08pp) that was substantially recovered through dunning processes.
- **WL:** Declined by -0.47pp to 91.24%, the largest drop across clusters, driven by weakness in Credit Card (-0.57pp) and Apple Pay (-0.65pp) payment methods.
- **HF-NA:** Stable with a minimal decline of -0.10pp to 93.93%, with CA improving +0.29pp while US declined marginally by -0.04pp.
- **RTE:** Declined by -0.19pp to 94.65%, continuing a gradual 6-week erosion trend (-0.53pp since W12) that warrants monitoring if it persists.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W18

---

## AR Pre Dunning

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 93.15% to 92.75% (↓0.43%, not sig., vol: 8.1K)
- **HF-NA**: 92.19% to 92.11% (↓0.08%, not sig., vol: 407.1)
- **HF-INTL**: 94.62% to 93.93% (↓0.73%, not sig., vol: 5.7K)
- **US-HF**: 92.07% to 91.91% (↓0.18%, not sig., vol: 735.4)
- **RTE**: 92.75% to 92.56% (↓0.21%, not sig., vol: 890.0)
- **WL**: 90.09% to 89.61% (↓0.53%, not sig., vol: 885.6)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: LU (↓3%)
**Dimensions:**
[2.5% - 19%]
  - WL: CustomerQuality Bad (↓12%)
  - HF-NA: LL a. 0 (↓3%), CustomerQuality Bad (↓3%)
  - RTE: CustomerQuality Bad (↓7%)
  - HF-INTL: CustomerQuality Bad (↓7%)

### Overall Summary

Acceptance Rate (Overall) declined modestly across all five clusters in 2026-W18, with changes ranging from -0.09% to -0.73%, though none reached statistical significance. HF-INTL showed the largest decline (-0.73%) driven by upstream FirstRunAR deterioration (-1.08%), while all other clusters remained within normal weekly variance with no dimensional flags triggered.

### Cluster Highlights

- **US-HF:** Declined by -0.17% to 91.91% with parallel drops across all funnel stages, indicating systemic fluctuation rather than stage-specific issues, with no country or payment method breaching thresholds.
- **HF-INTL:** Declined by -0.73% to 93.93% driven by FirstRunAR weakness (-1.08%), with Apple Pay showing the steepest payment method decline (-1.29%) and LU/BE experiencing the largest country-level drops (-1.97%/-1.52%).
- **WL:** Declined by -0.53% to 89.61% originating from upstream FirstRunAR (-0.71%), with Credit Card payments showing the largest decline (-0.67%) and uniform softness across all four countries.
- **HF-NA:** Stable with minimal decline of -0.09% to 92.11%, continuing a gradual 8-week downward drift (-0.16pp cumulative), with CA improving +0.38% offsetting US's marginal -0.01% dip.
- **RTE:** Declined by -0.20% to 92.56% within normal 8-week variance (92.45%-93.20%), with FJ maintaining stability (-0.12%) on 92% of total volume and no countries exceeding the ±2.5% threshold.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W18

---

## Acceptance LL0 (Initial Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 91.85% to 91.40% (↓0.49%, not sig., vol: 424.2)
- **HF-NA**: 90.11% to 89.35% (↓0.85%, not sig., vol: 136.2)
- **HF-INTL**: 91.44% to 91.00% (↓0.48%, not sig., vol: 131.8)
- **US-HF**: 88.95% to 88.24% (↓0.80%, not sig., vol: 88.3)
- **RTE**: 93.18% to 92.55% (↓0.68%, not sig., vol: 220.3)
- **WL**: 92.17% to 91.98% (↓0.20%, not sig., vol: 22.3)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: FR (↓3%), NZ (↑5%), LU (↑3%)
  - RTE: TO (↓3%)
**Dimensions:**
[2.5% - 19%]
  - HF-INTL: PM Credit Card (↑4%)

### Overall Summary

Acceptance Rate (Initial Charges) declined across all five clusters in 2026-W18, with changes ranging from -0.19pp to -0.76pp, though none reached statistical significance. The most notable concern is FR in HF-INTL, where Insufficient Funds declines increased by +2.21pp, driving a -2.83% country-level decline.

### Cluster Highlights

- **US-HF:** Declined by -0.71pp to 88.24%, with PayPal showing the largest payment method drop (-1.42pp) but overall change within normal weekly variance.
- **HF-INTL:** Declined by -0.44pp to 91.0%, driven primarily by FR (-2.83%) where Insufficient Funds increased from 2.59% to 4.81% and Apple Pay degraded by -4.69pp.
- **WL:** Stable with a marginal -0.19pp decline to 91.98%, with no countries or dimensions exceeding investigation thresholds.
- **HF-NA:** Declined by -0.76pp to 89.35%, with consistent drops across both US (-0.71pp) and CA (-1.24pp) and all funnel stages showing parallel declines.
- **RTE:** Declined by -0.63pp to 92.55%, with TO exceeding threshold (-3.04%) due to PayPal decline (-5.21%) and increased Insufficient Funds (+2.32pp), though TO represents only 1.3% of volume.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W18

---

## Acceptance LL0 and LL1+ (Recurring Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 93.22% to 92.81% (↓0.43%, not sig., vol: 7.8K)
- **HF-NA**: 92.26% to 92.20% (↓0.07%, not sig., vol: 320.7)
- **HF-INTL**: 94.76% to 94.04% (↓0.76%, not sig., vol: 5.7K)
- **US-HF**: 92.17% to 92.01% (↓0.18%, not sig., vol: 712.7)
- **RTE**: 92.72% to 92.56% (↓0.17%, not sig., vol: 678.8)
- **WL**: 89.94% to 89.44% (↓0.55%, not sig., vol: 859.3)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: LU (↓3%)
  - RTE: TV (↓3%)
**Dimensions:**
[2.5% - 19%]
  - WL: CustomerQuality Bad (↓12%)
  - RTE: CustomerQuality Bad (↓7%)
  - HF-INTL: CustomerQuality Bad (↓7%)
  - HF-NA: CustomerQuality Bad (↓3%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W18

---

## Ship Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 53.30% to 55.12% (↑3.40%, not sig., vol: 2.8K)
- **HF-NA**: 48.71% to 48.35% (↓0.74%, not sig., vol: 133.9)
- **HF-INTL**: 68.23% to 72.25% (↑5.88%, not sig., vol: 2.1K)
- **US-HF**: 47.58% to 48.00% (↑0.89%, not sig., vol: 124.2)
- **RTE**: 42.88% to 41.70% (↓2.75%, not sig., vol: 576.7)
- **WL**: 31.32% to 31.06% (↓0.85%, not sig., vol: 72.5)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - RTE: TK (↑50%)
[10.0% - 19%]
  - HF-INTL: FR (↑12%), DE (↑11%), DK (↑11%)
  - WL: MR (↓11%), CG (↓15%), KN (↓13%)
  - RTE: TO (↑15%), TZ (↓13%)

### Overall Summary

Dunning Ship Rate performance was mixed across clusters in 2026-W18, with HF-INTL showing strong improvement (+4.01pp to 72.25%) while RTE declined notably (-1.18pp to 41.70%). The transition from Post-Payday to Mid-Cycle phase drove divergent outcomes, with reduced discount dependency improving conversion in some markets while limiting customer payment capacity in others.

### Cluster Highlights

- **US-HF:** Ship Rate improved modestly to 48.00% (+0.42pp), driven by stronger PC2 conversion (+4.6%) and reduced discount reliance (-8.3%) despite Mid-Cycle timing.
- **HF-INTL:** Ship Rate surged to 72.25% (+4.01pp) with broad-based gains led by FR (+11.8%), DE (+11.1%), and DK (+11.0%), all benefiting from significant discount reductions.
- **WL:** Ship Rate declined marginally to 31.06% (-0.27pp), with CG experiencing an outsized -15.4% drop requiring monitoring despite stable funnel metrics.
- **HF-NA:** Ship Rate dipped slightly to 48.35% (-0.36pp), driven by CA's -6.1% decline during Mid-Cycle phase while US showed resilience with +0.9% improvement.
- **RTE:** Ship Rate fell to 41.70% (-1.18pp), concentrated in FJ (-4.4%) where increased PC2 engagement and discounting failed to convert during Mid-Cycle phase.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W18

---

## Recovery W0

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 41.65% to 44.40% (↑6.60%, not sig., vol: 3.0K)
- **HF-NA**: 38.94% to 39.62% (↑1.75%, not sig., vol: 153.6)
- **HF-INTL**: 41.57% to 45.82% (↑10.23%, not sig., vol: 2.6K)
- **US-HF**: 41.02% to 42.45% (↑3.49%, not sig., vol: 234.7)
- **RTE**: 45.44% to 45.66% (↑0.49%, not sig., vol: 43.0)
- **WL**: 38.94% to 42.37% (↑8.81%, not sig., vol: 232.7)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: SE (↑63%), CH (↑56%)
  - WL: GN (↑77%)
[20% - 49%]
  - HF-INTL: GB (↑30%), NL (↑40%), LU (↑32%)
  - WL: KN (↑41%), CG (↑24%)
  - RTE: TO (↓28%), TZ (↓22%)
[10.0% - 19%]
  - HF-INTL: DE (↑13%), IE (↑13%), AT (↑16%)
**Low Volume (denom < 50):** 3 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W18

---

## Recovery W12

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 84.17% to 86.22% (↑2.44%, not sig., vol: 1.1K)
- **HF-NA**: 74.65% to 78.97% (↑5.79%, not sig., vol: 563.7)
- **HF-INTL**: 90.06% to 89.62% (↓0.49%, not sig., vol: 119.2)
- **US-HF**: 72.04% to 79.27% (↑10.03%, not sig., vol: 697.4)
- **RTE**: 78.13% to 86.32% (↑10.49%, not sig., vol: 874.5)
- **WL**: 79.50% to 81.80% (↑2.89%, not sig., vol: 87.9)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - RTE: TV (↓30%)
[10.0% - 19%]
  - RTE: FJ (↑18%)
  - HF-NA: US (↑10%)
  - WL: CG (↑10%), KN (↓12%)
**Low Volume (denom < 50):** 2 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W18

---

## Dunning Profit

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: €6.20 to €9.82 (↑58.45%, not sig., vol: 47.5K)
- **HF-NA**: €3.42 to €9.94 (↑190.97%, not sig., vol: 37.2K)
- **HF-INTL**: €11.18 to €10.95 (↓2.06%, not sig., vol: 700.5)
- **US-HF**: €1.46 to €9.20 (↑530.03%, not sig., vol: 77.8K)
- **RTE**: €0.46 to €9.38 (↑1953.16%, not sig., vol: 403.9K)
- **WL**: €3.18 to €5.44 (↑71.09%, not sig., vol: 5.1K)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-NA: US (↑530%)
  - HF-INTL: ES (↑283%)
  - WL: CG (↑109%)
[20% - 49%]
  - HF-INTL: GB (↓26%), NO (↑27%), DK (↑28%), SE (↓23%), AT (↑41%)
  - HF-NA: CA (↑32%)
  - RTE: CF (↑22%)
  - WL: AO (↑27%)
[10.0% - 19%]
  - HF-INTL: AU (↑15%), FR (↓14%), NZ (↑19%), LU (↓19%)
  - WL: CK (↓13%), GN (↓17%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W18

---
