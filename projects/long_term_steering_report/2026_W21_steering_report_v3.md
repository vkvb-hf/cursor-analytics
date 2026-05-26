# Steering Report - 2026-W21 (v3)

**Week:** 2026-W21  
**Generated:** 2026-05-26 14:41

---

## Payment Checkout Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 94.32% to 95.12% (↑0.85%, not sig., vol: 779.1)
- **HF-NA**: 90.68% to 92.33% (↑1.82%, not sig., vol: 343.6)
- **HF-INTL**: 93.50% to 93.72% (↑0.24%, not sig., vol: 68.9)
- **US-HF**: 89.15% to 90.75% (↑1.80%, not sig., vol: 259.0)
- **RTE**: 96.49% to 97.25% (↑0.78%, not sig., vol: 278.9)
- **WL**: 95.62% to 96.86% (↑1.29%, not sig., vol: 121.8)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: DE (↓3%), FR (↑3%), AT (↓3%), CH (↓3%)
  - WL: CK (↑3%)
  - RTE: TO (↓7%)
**Dimensions:**
[2.5% - 19%]
  - HF-INTL: PM Credit Card (↑4%), PM Others (↓5%)
  - HF-NA: PM Credit Card (↑3%), FinalTokenType false (↓6%), PM Others (↓7%)

### Overall Summary

Payment Checkout Approval Rate improved across all clusters in 2026-W21, with significant gains in US-HF (+1.79%), WL (+1.30%), and HF-NA (+1.82%), while HF-INTL (+0.24%) and RTE (+0.79%) showed smaller, non-significant improvements. The most significant concern is HF-INTL, where headline stability masks underlying degradation in DE (Klarna/Adyen at 52.56% approval) and AT (ApplePay/Braintree down 8.13pp), requiring investigation despite the overall positive trend.

### Cluster Highlights

- **US-HF:** Improved by +1.79% to 90.75%, driven by Credit Card approval rate recovery (+2.92%) representing 57% of volume, though rate remains below the 93% baseline from W15-W17.
- **HF-INTL:** Marginal improvement of +0.24% to 93.72% masks concerning declines in DE (-3.04%, Klarna/Adyen issues) and AT (-3.33%, ApplePay/Braintree down 8.13pp), requiring investigation.
- **WL:** Improved significantly by +1.30% to 96.86%, driven by CK (+3.35%) where Credit Card via Adyen improved +4.33% and fraud-related declines dropped from 1.07% to 0.30%.
- **HF-NA:** Improved by +1.82% to 92.33%, led by US Credit Card recovery (+2.46pp) and favorable mix shift toward higher-performing CA (+10.6% volume growth at 97.32% rate).
- **RTE:** Improved by +0.79% to 97.25% (not significant), though TO declined -6.65pp due to Adyen provider issues (-8.90pp) and payment mix shift toward lower-performing BcmcMobile.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W21

---

## Payment Page Visit to Success

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 32.91% to 32.77% (↓0.41%, not sig., vol: 882.6)
- **HF-NA**: 25.83% to 27.26% (↑5.56%, not sig., vol: 3.1K)
- **HF-INTL**: 35.41% to 34.89% (↓1.46%, not sig., vol: 888.7)
- **US-HF**: 23.79% to 25.01% (↑5.14%, not sig., vol: 2.2K)
- **RTE**: 39.22% to 38.47% (↓1.92%, not sig., vol: 1.1K)
- **WL**: 29.34% to 28.64% (↓2.40%, not sig., vol: 909.1)

**Deep Insights**
**Business Units:**
[5.0% - 19%]
  - HF-NA: US (↑5%)
  - WL: MR (↓8%), CK (↑6%)
  - RTE: YE (↑7%), TT (↓18%), TO (↑19%)
  - HF-INTL: IE (↓7%), BE (↑5%), NO (↑7%), CH (↑9%)

### Overall Summary

Payment Conversion Rate (Checkout) performance was mixed globally in 2026-W21, with HF-NA (+1.45pp) and US-HF (+1.27pp) showing strong improvements while HF-INTL (-0.54pp), WL (-0.72pp), and RTE (-0.76pp) experienced declines. The most significant concern is the Braintree_ApplePay success rate collapse in RTE (-8.91pp), driven by a surge in Apple Pay dismissals and new address validation errors requiring immediate investigation.

### Cluster Highlights

- **US-HF:** PCR improved by +1.27pp to 25.15%, driven by ProcessOut_CreditCard success rate gains (+3.46pp) and substantial reduction in Insufficient Funds declines (-202 cases).
- **HF-INTL:** PCR declined by -0.54pp to 34.93%, primarily due to Successful Checkout degradation (-0.99pp) concentrated in DE (-1.49pp PCR) and Adyen_Sepa integration failures (89.8% of attempts not reaching fraud service).
- **WL:** PCR declined by -0.72pp to 28.66%, driven by Select Payment Method drop (-1.68pp), particularly in MR where volume increased +36.7% but payment method selection engagement fell.
- **HF-NA:** PCR improved by +1.45pp to 27.38%, driven by ProcessOut_CreditCard success rate improvement (+3.71pp) and Adyen_CreditCard exceptional gains (+12.55pp to 92.13%).
- **RTE:** PCR declined by -0.76pp to 38.53%, driven by Braintree_ApplePay success rate collapse (-8.91pp) due to Apple Pay dismissal errors increasing to 94.8% of FE validation failures.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W21

---

## Payment Page Visit to Success (Backend)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 32.55% to 32.21% (↓1.06%, not sig., vol: 3.0K)
- **HF-NA**: 26.94% to 28.26% (↑4.93%, not sig., vol: 3.0K)
- **HF-INTL**: 36.81% to 36.56% (↓0.69%, not sig., vol: 519.3)
- **US-HF**: 24.85% to 26.01% (↑4.67%, not sig., vol: 2.2K)
- **RTE**: 34.65% to 33.71% (↓2.71%, not sig., vol: 2.7K)
- **WL**: 27.69% to 26.88% (↓2.94%, not sig., vol: 1.3K)

**Deep Insights**
**Business Units:**
[5.0% - 19%]
  - WL: MR (↓9%), CK (↑6%)
  - RTE: YE (↑6%), TO (↑19%), TT (↓13%)
  - HF-INTL: IE (↓7%), AT (↓8%), NO (↑7%), LU (↑14%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W21

---

## Reactivation Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 89.63% to 89.94% (↑0.34%, not sig., vol: 259.1)
- **HF-NA**: 90.24% to 89.43% (↓0.90%, not sig., vol: 152.7)
- **HF-INTL**: 89.55% to 90.58% (↑1.15%, not sig., vol: 389.0)
- **US-HF**: 90.20% to 88.72% (↓1.64%, not sig., vol: 208.6)
- **RTE**: 89.27% to 89.38% (↑0.13%, not sig., vol: 22.3)
- **WL**: 89.41% to 89.48% (↑0.08%, not sig., vol: 5.5)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: AU (↑3%), NZ (↑6%), DK (↑4%)
  - WL: AO (↓3%)
**Dimensions:**
[2.5% - 19%]
  - HF-NA: PM Apple Pay (↓3%)
  - RTE: PM Apple Pay (↑3%)
  - WL: FinalTokenType true (↓4%)
**Low Volume (denom < 50):** 7 segments excluded

### Overall Summary

Reactivation Rate performance was mixed across clusters in 2026-W21, with US-HF showing a significant decline (-1.64pp) while HF-INTL improved (+1.15pp) and other clusters remained stable. The most significant concern is Apple Pay performance degradation, which was flagged as a driver of declines in both US-HF (-3.84pp) and AO within WL (-22.96%).

### Cluster Highlights

- **US-HF:** Significant decline from 90.2% to 88.72% (-1.64pp), driven primarily by Apple Pay performance dropping 3.84pp to 82.78% on 1,957 orders.
- **HF-INTL:** Improved from 89.55% to 90.58% (+1.15pp), with AU Apple Pay surging +37.15% offsetting a CH Credit Card decline (-19.03%) on minimal volume.
- **WL:** Stable with non-significant change (+0.08pp to 89.48%), though AO showed a -3.24pp decline driven by Apple Pay dropping to 53.33% on low volume.
- **HF-NA:** Non-significant decline from 90.24% to 89.43% (-0.90pp), with Apple Pay flagged at -2.71% but no country exceeding investigation thresholds.
- **RTE:** Stable at 89.38% (+0.12pp), with flagged countries TV, TT, and TO representing less than 0.3% of total volume (48 orders combined).

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W21

---

## Fraud Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 92.79% to 93.02% (↑0.25%, not sig., vol: 271.9)
- **HF-NA**: 92.06% to 91.99% (↓0.07%, not sig., vol: 15.1)
- **HF-INTL**: 91.21% to 92.22% (↑1.10%, not sig., vol: 385.3)
- **US-HF**: 92.33% to 92.04% (↓0.31%, not sig., vol: 48.9)
- **RTE**: 94.65% to 94.30% (↓0.37%, not sig., vol: 139.2)
- **WL**: 92.83% to 93.13% (↑0.33%, not sig., vol: 44.0)

**Deep Insights**
**Business Units:**
[5.0% - 19%]
  - RTE: TT (↓5%)
  - HF-INTL: CH (↓7%)
**Dimensions:**
[+50%]
  - HF-NA: PM Credit Card (↑2783%)
  - RTE: PM Unknown (↓100%)
**Low Volume (denom < 50):** 4 segments excluded

### Overall Summary

Fraud Approval Rate remained broadly stable across all clusters in 2026-W21, with changes ranging from -0.37pp to +1.10pp and most movements not statistically significant. The most notable finding is HF-INTL's CH market showing a -7.22pp FAR decline coupled with a -60.37% drop in Duplicate Rate, suggesting a potential data quality issue or operational change requiring investigation.

### Cluster Highlights

- **US-HF:** Stable at 92.04% (-0.31pp), with slight increases in Duplicate Rate (+0.72pp) and Duplicate Block Rate (+0.57pp) but no segments breaching alert thresholds.
- **HF-INTL:** Improved by +1.10pp to 92.22% (significant), driven by GB (+1.24pp) and DE (+1.49pp), though CH declined -7.22pp with anomalous duplicate rate behavior requiring investigation.
- **WL:** Stable at 93.13% (+0.33pp), with low-volume Referral channel volatility in KN (-20.32pp FAR) driven by duplicate rate surging +70.74%.
- **HF-NA:** Stable at 91.99% (-0.07pp), the smallest weekly change in 8 weeks, with CA Referral improving +3.41pp due to reduced duplicate activity.
- **RTE:** Declined slightly to 94.30% (-0.37pp, not significant), with TT flagged for a +107.54% surge in Duplicate Rate causing FAR to drop -5.19pp.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W21

---

## Total Duplicate Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 23.33% to 23.24% (↓0.35%, not sig., vol: 374.8)
- **HF-NA**: 25.20% to 26.03% (↑3.31%, not sig., vol: 711.3)
- **HF-INTL**: 32.91% to 31.87% (↓3.14%, not sig., vol: 1.1K)
- **US-HF**: 23.97% to 24.62% (↑2.71%, not sig., vol: 424.7)
- **RTE**: 15.30% to 16.00% (↑4.61%, not sig., vol: 1.7K)
- **WL**: 17.62% to 16.98% (↓3.63%, not sig., vol: 480.3)

**Deep Insights**
**Business Units:**
[+50%]
  - RTE: TT (↑107%)
  - HF-INTL: CH (↓58%)
[20% - 49%]
  - HF-INTL: NO (↓26%)
  - RTE: TZ (↑32%), TV (↑30%)
[10.0% - 19%]
  - HF-INTL: BE (↓19%)
  - WL: MR (↓13%), KN (↑12%), GN (↓10%)
  - RTE: YE (↑10%), TO (↑18%), TK (↑18%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W21

---

## Total Duplicate Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 5.42% to 5.40% (↓0.49%, not sig., vol: 521.1)
- **HF-NA**: 5.39% to 5.65% (↑4.81%, not sig., vol: 1.0K)
- **HF-INTL**: 6.89% to 6.14% (↓10.90%, not sig., vol: 3.7K)
- **US-HF**: 5.44% to 6.01% (↑10.47%, not sig., vol: 1.6K)
- **RTE**: 4.17% to 4.64% (↑11.51%, not sig., vol: 4.3K)
- **WL**: 5.17% to 5.21% (↑0.68%, not sig., vol: 90.3)

**Deep Insights**
**Business Units:**
[+50%]
  - RTE: TT (↑112%)
[20% - 49%]
  - HF-INTL: DE (↓20%), AU (↑24%), BE (↓25%), CH (↑25%)
  - WL: MR (↓27%)
  - RTE: TZ (↑35%), TV (↑24%), TK (↑26%)
[10.0% - 19%]
  - RTE: FJ (↑11%)
  - HF-NA: US (↑10%), CA (↓10%)
  - HF-INTL: GB (↓12%), NL (↓19%), DK (↓13%), NO (↓17%)
  - WL: KN (↑18%), CK (↑11%), GN (↓12%)
**Dimensions:**
[20% - 49%]
  - HF-NA: CC Paid (↑25%)
[10.0% - 19%]
  - RTE: CC Paid (↑12%), CC Referral (↑13%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W21

---

## Payment Fraud Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 0.56% to 0.62% (↑10.88%, not sig., vol: 11.6K)
- **HF-NA**: 1.30% to 1.39% (↑6.68%, not sig., vol: 1.4K)
- **HF-INTL**: 0.32% to 0.31% (↓1.78%, not sig., vol: 613.4)
- **US-HF**: 1.03% to 1.06% (↑3.22%, not sig., vol: 504.5)
- **RTE**: 0.28% to 0.32% (↑16.61%, not sig., vol: 6.3K)
- **WL**: 0.84% to 1.00% (↑19.34%, not sig., vol: 2.6K)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: DE (↑153%), BE (↑181%), DK (↑137%), SE (↑111%), NZ (↓70%)
  - WL: KN (↓67%), AO (↑90%)
[20% - 49%]
  - HF-INTL: FR (↓34%), AU (↑22%), IE (↑22%)
  - WL: MR (↑23%), CG (↑35%), ER (↓22%), GN (↑21%)
  - RTE: TZ (↑29%), TK (↓43%)
[10.0% - 19%]
  - RTE: FJ (↑17%)
  - HF-INTL: GB (↓12%)
**Dimensions:**
[20% - 49%]
  - RTE: CC Paid (↑27%), CC Referral (↓32%)
  - HF-NA: CC Paid (↑39%), CC Referral (↓25%)
  - WL: CC Paid (↑26%), CC Referral (↓34%)
  - HF-INTL: CC Referral (↓28%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W21

---

## Payment Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 95.36% to 95.36% (↓0.00%, not sig., vol: 71.5)
- **HF-NA**: 93.87% to 93.64% (↓0.24%, not sig., vol: 1.1K)
- **HF-INTL**: 97.53% to 97.57% (↑0.05%, not sig., vol: 361.2)
- **US-HF**: 93.50% to 93.23% (↓0.28%, not sig., vol: 1.1K)
- **RTE**: 94.78% to 94.85% (↑0.07%, not sig., vol: 275.9)
- **WL**: 91.30% to 91.14% (↓0.17%, not sig., vol: 267.7)

**Deep Insights**
**Dimensions:**
[2.5% - 19%]
  - RTE: CustomerQuality Bad (↓17%), PP Unknown (↑11%)
  - HF-NA: CustomerQuality Bad (↓7%), PP Unknown (↓3%)
  - HF-INTL: CustomerQuality Bad (↓6%)

### Overall Summary

Payment Approval Rate remained broadly stable across all clusters in 2026-W21, with changes ranging from -0.29pp to +0.07pp, none of which were statistically significant. US-HF showed the largest decline at -0.29pp with a concerning 6-week downward trend from 93.82% to 93.23%, though no single dimension exceeded investigation thresholds.

### Cluster Highlights

- **US-HF:** Declined by -0.29pp (93.5% → 93.23%) with modest softening across all funnel stages, particularly PostDunningAR (-0.45pp), though no country or payment dimension exceeded thresholds.
- **HF-INTL:** Stable at 97.57% (+0.04pp), with NO showing the strongest improvement at +1.01pp while upstream funnel metrics declined slightly, offset by recovery mechanisms.
- **WL:** Declined by -0.18pp (91.3% → 91.14%) driven primarily by FirstRunAR softening (-0.57pp), with MR showing the largest country decline at -1.11pp on 20,786 orders.
- **HF-NA:** Declined by -0.25pp (93.87% → 93.64%) with parallel softening across all funnel stages; Unknown PaymentProvider flagged at -3.48pp but represents only 497 orders (0.1% of volume).
- **RTE:** Improved marginally by +0.07pp (94.78% → 94.85%) with all funnel stages stable within ±0.04pp and no countries exceeding thresholds.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W21

---

## AR Pre Dunning

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 93.27% to 93.15% (↓0.13%, not sig., vol: 2.3K)
- **HF-NA**: 92.15% to 91.84% (↓0.33%, not sig., vol: 1.6K)
- **HF-INTL**: 95.08% to 94.94% (↓0.14%, not sig., vol: 1.1K)
- **US-HF**: 91.89% to 91.58% (↓0.34%, not sig., vol: 1.3K)
- **RTE**: 92.72% to 92.76% (↑0.04%, not sig., vol: 168.5)
- **WL**: 89.64% to 89.44% (↓0.22%, not sig., vol: 337.3)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: NO (↑4%)
**Dimensions:**
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↓13%), LL a. 0 (↓3%), PP Unknown (↓5%)
  - RTE: CustomerQuality Bad (↓17%), PP Unknown (↑7%)
  - HF-INTL: CustomerQuality Bad (↓6%), PP Unknown (↓3%)
  - WL: CustomerQuality Bad (↓7%)

### Overall Summary

Acceptance Rate (Overall) declined marginally across all clusters in 2026-W21, with changes ranging from -0.34pp to +0.04pp, none of which were statistically significant. The most notable pattern is a gradual 6-week downward trend in US-HF (cumulative -0.64pp from W15 to W21), while HF-INTL saw a positive outlier with NO improving +3.63pp due to reduced Insufficient Funds declines.

### Cluster Highlights

- **US-HF:** Declined by -0.31pp to 91.58% on 386,911 orders, continuing a 6-week gradual erosion trend with no single dimension exceeding investigation thresholds.
- **HF-INTL:** Declined marginally by -0.14pp to 94.94% on 748,329 orders, with NO showing significant improvement (+3.63pp) driven by a 3.05pp reduction in Insufficient Funds declines.
- **WL:** Declined by -0.20pp to 89.44% on 153,361 orders, with First Run AR showing the largest funnel impact (-0.57pp) but no countries or dimensions exceeding thresholds.
- **HF-NA:** Declined by -0.31pp to 91.84% on 468,983 orders, with broad shallow declines across all funnel stages and both US (-0.23pp) and CA (-0.28pp) contributing proportionally.
- **RTE:** Stable at 92.76% (+0.04pp) on 401,555 orders, with all funnel stages and dimensions showing minimal movement within normal operating range.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W21

---

## Acceptance LL0 (Initial Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 92.09% to 91.93% (↓0.17%, not sig., vol: 135.8)
- **HF-NA**: 89.34% to 88.39% (↓1.06%, not sig., vol: 145.3)
- **HF-INTL**: 92.70% to 92.39% (↓0.34%, not sig., vol: 98.3)
- **US-HF**: 87.77% to 86.81% (↓1.10%, not sig., vol: 105.8)
- **RTE**: 92.97% to 93.04% (↑0.07%, not sig., vol: 18.3)
- **WL**: 91.88% to 92.42% (↑0.59%, not sig., vol: 66.3)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - WL: CK (↑3%)
  - HF-INTL: SE (↓4%), NO (↑3%), CH (↓6%), LU (↓10%)
**Dimensions:**
[2.5% - 19%]
  - WL: PP Adyen (↑3%)
  - HF-NA: PM Paypal (↓3%), PP Unknown (↓3%)
  - RTE: PP Unknown (↓7%)
**Low Volume (denom < 50):** 1 segment excluded

### Overall Summary

Acceptance Rate (Initial Charges) showed mixed performance globally in 2026-W21, with significant declines in US-HF (-0.96pp to 86.81%) and HF-NA (-0.95pp to 88.39%), while RTE, WL, and HF-INTL remained stable. The most critical concern is the persistent 5-week decline trend in US-HF, driven by ProcessOut underperformance (-1.58pp) on Credit Card transactions, which warrants immediate investigation.

### Cluster Highlights

- **US-HF:** Declined significantly by -0.96pp to 86.81%, marking the fifth consecutive week of decline driven by ProcessOut (-1.58pp) and Credit Card (-1.38pp) underperformance.
- **HF-INTL:** Stable with a non-significant decline of -0.31pp to 92.39%, with flagged countries (LU, CH, SE) representing low-volume markets exhibiting normal volatility.
- **WL:** Improved slightly by +0.54pp to 92.42% (not significant), driven by Adyen performance gains (+3.50pp) and credit_card recovery in CK (+5.89pp).
- **HF-NA:** Declined significantly by -0.95pp to 88.39%, with PayPal showing the steepest drop (-2.98pp) across both US and CA markets.
- **RTE:** Stable with marginal improvement of +0.07pp to 93.04%, continuing an 8-week upward trend with no material concerns identified.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W21

---

## Acceptance LL0 and LL1+ (Recurring Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 93.33% to 93.21% (↓0.13%, not sig., vol: 2.2K)
- **HF-NA**: 92.23% to 91.94% (↓0.32%, not sig., vol: 1.4K)
- **HF-INTL**: 95.18% to 95.04% (↓0.14%, not sig., vol: 989.4)
- **US-HF**: 92.00% to 91.70% (↓0.33%, not sig., vol: 1.2K)
- **RTE**: 92.70% to 92.74% (↑0.04%, not sig., vol: 153.5)
- **WL**: 89.46% to 89.21% (↓0.28%, not sig., vol: 392.1)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: NO (↑4%)
**Dimensions:**
[20% - 49%]
  - HF-INTL: PP Unknown (↓31%)
  - HF-NA: PP Unknown (↑24%)
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↓13%)
  - RTE: CustomerQuality Bad (↓17%)
  - HF-INTL: CustomerQuality Bad (↓6%)
  - WL: CustomerQuality Bad (↓7%)
**Low Volume (denom < 50):** 2 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W21

---

## Ship Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 51.71% to 53.05% (↑2.60%, not sig., vol: 1.8K)
- **HF-NA**: 47.65% to 46.53% (↓2.36%, not sig., vol: 389.3)
- **HF-INTL**: 66.96% to 68.76% (↑2.69%, not sig., vol: 743.3)
- **US-HF**: 46.44% to 45.53% (↓1.95%, not sig., vol: 252.9)
- **RTE**: 42.77% to 44.25% (↑3.44%, not sig., vol: 628.2)
- **WL**: 31.72% to 31.71% (↓0.02%, not sig., vol: 1.9)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - RTE: TZ (↑28%), TV (↓48%), TT (↑30%)
[10.0% - 19%]
  - WL: GN (↑13%)

### Overall Summary

Dunning Ship Rate performance was mixed globally in 2026-W21, with HF-INTL (+1.81pp) and RTE (+1.47pp) showing improvement while US-HF (-0.91pp) and HF-NA (-1.13pp) declined during the Post-Payday transition. The most significant finding is the detection of Simpson's Paradox in WL, where aggregate performance remained flat despite individual country improvements due to unfavorable volume mix shifts toward lower-performing segments.

### Cluster Highlights

- **US-HF:** Ship Rate declined by 0.91pp (46.44% → 45.53%) driven by expected Post-Payday cyclical effects, with all controllable funnel metrics remaining stable or favorable.
- **HF-INTL:** Ship Rate improved by 1.81pp (66.95% → 68.76%) led by strong performance in GB (+9.7%) and NL (+8.9%), driven by reduced discount dependency and PC2 gains.
- **WL:** Ship Rate remained flat at 31.71% despite CK (+7.6%) and GN (+13.2%) improvements, offset by ER's -7.9% decline and unfavorable volume shifts to low-performing segments.
- **HF-NA:** Ship Rate declined by 1.13pp (47.65% → 46.52%) with CA experiencing the steepest drop (-3.5%) during the Payday to Post-Payday transition.
- **RTE:** Ship Rate improved by 1.47pp (42.78% → 44.25%) driven primarily by FJ's +6.7% gain, though TV showed an anomalous -47.7% decline requiring investigation.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W21

---

## Recovery W0

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 43.56% to 45.59% (↑4.66%, not sig., vol: 1.7K)
- **HF-NA**: 39.44% to 43.68% (↑10.75%, not sig., vol: 824.2)
- **HF-INTL**: 44.79% to 44.35% (↓0.98%, not sig., vol: 186.7)
- **US-HF**: 41.32% to 44.62% (↑7.99%, not sig., vol: 472.8)
- **RTE**: 45.85% to 50.37% (↑9.85%, not sig., vol: 795.1)
- **WL**: 40.42% to 45.54% (↑12.66%, not sig., vol: 310.8)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - HF-NA: CA (↑21%)
  - HF-INTL: BE (↑24%), NL (↑23%), CH (↑33%)
  - WL: CK (↑37%), CG (↑24%), GN (↑21%)
  - RTE: CF (↑24%), TO (↑40%), TZ (↑31%)
[10.0% - 19%]
  - RTE: FJ (↑11%)
  - HF-INTL: DE (↓18%), IE (↓13%), AT (↑15%), LU (↑16%)
  - WL: ER (↑16%), KN (↓12%)
**Low Volume (denom < 50):** 2 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W21

---

## Recovery W12

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 85.38% to 86.19% (↑0.94%, not sig., vol: 441.3)
- **HF-NA**: 80.12% to 78.95% (↓1.46%, not sig., vol: 132.0)
- **HF-INTL**: 88.29% to 89.32% (↑1.17%, not sig., vol: 305.3)
- **US-HF**: 80.33% to 78.60% (↓2.16%, not sig., vol: 137.7)
- **RTE**: 84.61% to 85.07% (↑0.55%, not sig., vol: 47.0)
- **WL**: 82.22% to 83.89% (↑2.03%, not sig., vol: 58.3)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - RTE: TK (↑34%), TV (↑21%)
[10.0% - 19%]
  - RTE: TO (↓10%)
**Low Volume (denom < 50):** 2 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W21

---

## Dunning Profit

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: €10.37 to €10.63 (↑2.46%, not sig., vol: 1.9K)
- **HF-NA**: €11.39 to €11.44 (↑0.43%, not sig., vol: 72.9)
- **HF-INTL**: €11.01 to €11.48 (↑4.30%, not sig., vol: 1.6K)
- **US-HF**: €11.29 to €11.49 (↑1.79%, not sig., vol: 229.3)
- **RTE**: €9.89 to €9.89 (↓0.04%, not sig., vol: 7.2)
- **WL**: €5.89 to €5.81 (↓1.30%, not sig., vol: 84.6)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: NL (↓51%)
  - WL: GN (↑80%)
[20% - 49%]
  - HF-INTL: GB (↑27%), IE (↑25%), DK (↑21%), IT (↑39%), LU (↑22%)
  - WL: AO (↓34%)
[10.0% - 19%]
  - HF-INTL: FR (↑10%), BE (↑18%), NZ (↓14%), AT (↑10%)
  - WL: ER (↑12%), CG (↑12%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W21

---
