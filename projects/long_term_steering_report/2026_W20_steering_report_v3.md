# Steering Report - 2026-W20 (v3)

**Week:** 2026-W20  
**Generated:** 2026-05-19 14:46

---

## Payment Checkout Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 94.18% to 94.32% (↑0.15%, not sig., vol: 148.2)
- **HF-NA**: 91.02% to 90.68% (↓0.38%, not sig., vol: 74.0)
- **HF-INTL**: 92.95% to 93.50% (↑0.59%, not sig., vol: 187.3)
- **US-HF**: 89.61% to 89.15% (↓0.51%, not sig., vol: 79.8)
- **RTE**: 96.66% to 96.49% (↓0.18%, not sig., vol: 69.0)
- **WL**: 95.28% to 95.62% (↑0.36%, not sig., vol: 37.7)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - RTE: TT (↑6%)
  - HF-INTL: BE (↑5%), CH (↓4%)
**Dimensions:**
[2.5% - 19%]
  - HF-INTL: PM Others (↑10%)
  - RTE: PM Others (↑5%)
**Low Volume (denom < 50):** 5 segments excluded

### Overall Summary

Payment Checkout Approval Rate showed mixed performance across clusters in 2026-W20, with no statistically significant changes reported. The most concerning finding is the sustained multi-week declining trends in US-HF (-3.42pp since W13) and HF-NA (-3.26pp since W17), both driven by Credit Card payment degradation.

### Cluster Highlights

- **US-HF:** Declined by -0.46pp to 89.15% (not significant), continuing a persistent 8-week downward trend with Credit Card payments contributing most to the decline at -0.86%.
- **HF-INTL:** Improved by +0.59pp to 93.5% (not significant), with CH declining -4.48pp due to CreditCard via ProcessOut issues while BE improved +4.77pp from BcmcMobile recovery.
- **WL:** Improved by +0.36pp to 95.62% (not significant), representing a partial recovery after three consecutive weeks of decline, with ER showing the strongest improvement at +1.48pp.
- **HF-NA:** Declined by -0.37pp to 90.68% (not significant), marking the fourth consecutive week of decline with US Credit Card (-0.63pp) and PayPal (-0.67pp) as primary drivers.
- **RTE:** Declined by -0.18pp to 96.49% (not significant), with TT improving +6.37pp driven by IDeal gains while CF declined -1.57pp on 5,525 orders.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W20

---

## Payment Page Visit to Success

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 32.81% to 32.91% (↑0.31%, not sig., vol: 703.6)
- **HF-NA**: 25.65% to 25.83% (↑0.68%, not sig., vol: 420.5)
- **HF-INTL**: 36.26% to 35.40% (↓2.36%, not sig., vol: 1.6K)
- **US-HF**: 23.74% to 23.79% (↑0.18%, not sig., vol: 90.2)
- **RTE**: 38.47% to 39.22% (↑1.97%, not sig., vol: 1.3K)
- **WL**: 29.28% to 29.34% (↑0.22%, not sig., vol: 81.3)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - HF-INTL: LU (↑26%)
[5.0% - 19%]
  - HF-INTL: FR (↓6%), NZ (↓7%), IE (↑5%)
  - WL: MR (↓8%), AO (↑10%)
  - RTE: YE (↑7%), TT (↑11%), TO (↓9%), TV (↑10%), TK (↓6%)

### Overall Summary

Payment Conversion Rate (Checkout) showed mixed performance across clusters in 2026-W20, with declines in US-HF (-0.07pp) and HF-INTL (-0.85pp) offset by improvements in RTE (+0.70pp) and HF-NA (+0.11pp). The most critical concern is Braintree_ApplePay degradation, which experienced severe success rate declines across multiple clusters (US-HF: -8.74pp, HF-INTL: -12.77pp, HF-NA: -9.19pp), requiring immediate investigation.

### Cluster Highlights

- **US-HF:** PCR declined by -0.07pp to 23.88%, driven primarily by Braintree_ApplePay success rate dropping -8.74pp (74.41% → 65.67%) despite representing ~35% of payment attempts.
- **HF-INTL:** PCR declined by -0.85pp to 35.47%, with Braintree_ApplePay experiencing the largest degradation (-12.77pp to 72.41%) combined with fraud service approval issues in NZ (-2.69pp).
- **WL:** PCR remained stable at 29.38% (+0.05pp), with FE Validation recovery rate declining -2.66pp as APPLEPAY_DISMISSED errors increased, though offset by early-funnel gains.
- **HF-NA:** PCR improved by +0.11pp to 25.93%, driven by CA gains (+1.02pp) that offset US decline (-0.07pp), despite Braintree_ApplePay success rate falling -9.19pp.
- **RTE:** PCR improved by +0.70pp to 39.29%, driven by early-funnel gains in Select Payment Method (+0.83pp) and Click Submit Form (+0.44pp), with TV contributing +3.88pp improvement.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W20

---

## Payment Page Visit to Success (Backend)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 32.78% to 32.55% (↓0.69%, not sig., vol: 2.1K)
- **HF-NA**: 27.28% to 26.94% (↓1.26%, not sig., vol: 825.4)
- **HF-INTL**: 38.51% to 36.81% (↓4.40%, not sig., vol: 3.6K)
- **US-HF**: 25.30% to 24.85% (↓1.81%, not sig., vol: 940.3)
- **RTE**: 33.99% to 34.65% (↑1.95%, not sig., vol: 2.1K)
- **WL**: 27.60% to 27.69% (↑0.36%, not sig., vol: 158.6)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - HF-INTL: LU (↑27%)
[5.0% - 19%]
  - HF-INTL: GB (↓7%), FR (↓6%), NO (↓6%)
  - RTE: YE (↑10%), TT (↑11%), TO (↓10%), TV (↑6%)
  - WL: MR (↓8%), CK (↑5%), AO (↑12%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W20

---

## Reactivation Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 89.96% to 89.63% (↓0.36%, not sig., vol: 296.0)
- **HF-NA**: 90.66% to 90.24% (↓0.46%, not sig., vol: 86.0)
- **HF-INTL**: 90.32% to 89.55% (↓0.85%, not sig., vol: 315.4)
- **US-HF**: 90.74% to 90.20% (↓0.59%, not sig., vol: 88.0)
- **RTE**: 89.01% to 89.27% (↑0.29%, not sig., vol: 54.2)
- **WL**: 88.73% to 89.41% (↑0.77%, not sig., vol: 58.0)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - WL: CK (↑8%), AO (↑3%)
  - RTE: YE (↑5%)
  - HF-INTL: DK (↓3%)
**Dimensions:**
[2.5% - 19%]
  - RTE: PM Apple Pay (↓3%), PM Others (↑10%)
**Low Volume (denom < 50):** 4 segments excluded

### Overall Summary

Reactivation Rate remained broadly stable across all clusters in 2026-W20, with changes ranging from -0.85% (HF-INTL) to +0.77% (WL), none of which were statistically significant. The most notable finding is a consistent volume decline of 10-20% across multiple clusters (US-HF, HF-INTL, HF-NA), though this has not materially impacted reactivation performance.

### Cluster Highlights

- **US-HF:** Declined by -0.54pp (90.74% → 90.2%) within normal variance, with Credit Card showing the largest drop at -0.65% on 69% of volume.
- **HF-INTL:** Declined by -0.85pp (90.32% → 89.55%), with DK exceeding threshold (-2.68%) driven by Paypal decline (-8.64%) on minimal volume (36 orders).
- **WL:** Improved by +0.77pp (88.73% → 89.41%), led by CK (+7.54pp) with broad gains across all payment methods and reduced card expiry declines.
- **HF-NA:** Declined by -0.42pp (90.66% → 90.24%) within normal range, with US driving the decline (-0.59%) while CA remained flat (+0.06%).
- **RTE:** Improved slightly by +0.26pp (89.01% → 89.27%), with YE showing meaningful improvement (+4.91%) on 2,352 orders while flagged declines in TO and TV represent <0.2% of volume.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W20

---

## Fraud Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 92.59% to 92.88% (↑0.31%, not sig., vol: 368.3)
- **HF-NA**: 90.59% to 92.19% (↑1.77%, not sig., vol: 407.2)
- **HF-INTL**: 92.16% to 91.39% (↓0.83%, not sig., vol: 323.6)
- **US-HF**: 90.42% to 92.50% (↑2.31%, not sig., vol: 400.4)
- **RTE**: 94.02% to 94.65% (↑0.67%, not sig., vol: 280.8)
- **WL**: 93.08% to 92.86% (↓0.24%, not sig., vol: 32.5)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - RTE: TV (↑23%)
[5.0% - 19%]
  - RTE: TT (↑13%), TK (↑13%), TO (↑10%), TZ (↑8%)
  - HF-INTL: LU (↑13%)
**Dimensions:**
[+50%]
  - HF-NA: PM Credit Card (↑63%)
[5.0% - 19%]
  - RTE: PM Unknown (↑20%)
**Low Volume (denom < 50):** 3 segments excluded

### Overall Summary

Fraud Approval Rate showed mixed performance across clusters in 2026-W20, with significant improvements in US-HF (+2.31pp) and HF-NA (+1.77pp), while HF-INTL (-0.83pp), WL (-0.24pp), and RTE (+0.67pp) experienced non-significant changes. The most concerning finding is the consistent Referral channel degradation across multiple clusters, with FAR declines of -4.21pp (HF-INTL), -4.06pp (WL), and -2.44pp (RTE), all accompanied by significant duplicate rate increases suggesting potential referral fraud patterns.

### Cluster Highlights

- **US-HF:** FAR improved significantly by +2.31pp to 92.50%, driven primarily by PF Block Rate decreasing from 2.27% to 1.03%, representing a recovery to W18 levels after W19's dip.
- **HF-INTL:** FAR declined by -0.83pp to 91.39% (not significant), with Referral channel the primary driver falling -4.21pp to 74.17% alongside duplicate rates increasing +17.28%.
- **WL:** FAR remained stable with a non-significant -0.24pp decline to 92.86%, though Referral channel dropped -4.06pp with AO Referral showing severe degradation of -14.14pp and duplicate rates surging +70.67%.
- **HF-NA:** FAR improved significantly by +1.77pp to 92.19%, the highest in the 8-week period, driven by US performance (+2.31pp) and PF Block Rate decreasing from 2.04% to 1.31%.
- **RTE:** FAR improved by +0.67pp to 94.65% (not significant), with small markets TV (+23.09pp), TK (+13.49pp), and TT (+12.86pp) showing substantial gains due to reduced Duplicate Block rates in Paid channels.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W20

---

## Total Duplicate Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 21.07% to 23.50% (↑11.50%, not sig., vol: 13.4K)
- **HF-NA**: 22.88% to 25.46% (↑11.29%, not sig., vol: 2.6K)
- **HF-INTL**: 29.33% to 32.95% (↑12.34%, not sig., vol: 4.8K)
- **US-HF**: 21.64% to 24.21% (↑11.89%, not sig., vol: 2.0K)
- **RTE**: 14.39% to 15.50% (↑7.74%, not sig., vol: 3.2K)
- **WL**: 14.17% to 17.78% (↑25.47%, not sig., vol: 3.5K)

**Deep Insights**
**Business Units:**
[+50%]
  - WL: MR (↑50%)
[20% - 49%]
  - WL: CK (↑32%), KN (↑21%), GN (↑37%), AO (↑21%)
  - HF-INTL: IE (↑22%), DK (↑25%), AT (↑33%), NO (↑31%), CH (↑38%)
  - RTE: TV (↓42%)
[10.0% - 19%]
  - HF-NA: US (↑12%)
  - HF-INTL: GB (↑16%), AU (↑14%), BE (↑18%), NZ (↑17%), SE (↑12%)
  - RTE: CF (↑12%), TT (↓12%), TZ (↑13%), TK (↓12%)
  - WL: ER (↑16%)
**Dimensions:**
[20% - 49%]
  - WL: CC Paid (↑27%)
[10.0% - 19%]
  - HF-INTL: CC Paid (↑11%), CC Referral (↑16%)
  - RTE: CC Referral (↑14%)
  - HF-NA: CC Referral (↑19%)
  - WL: CC Referral (↑17%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W20

---

## Total Duplicate Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 4.90% to 5.63% (↑14.91%, not sig., vol: 17.3K)
- **HF-NA**: 5.21% to 5.57% (↑6.92%, not sig., vol: 1.6K)
- **HF-INTL**: 5.61% to 7.08% (↑26.16%, not sig., vol: 10.1K)
- **US-HF**: 5.01% to 5.58% (↑11.26%, not sig., vol: 1.9K)
- **RTE**: 4.14% to 4.40% (↑6.26%, not sig., vol: 2.6K)
- **WL**: 4.61% to 5.42% (↑17.65%, not sig., vol: 2.4K)

**Deep Insights**
**Business Units:**
[+50%]
  - WL: GN (↑65%)
  - HF-INTL: AT (↑68%), CH (↓80%)
[20% - 49%]
  - HF-INTL: GB (↑34%), DE (↑41%), FR (↑22%), BE (↑33%), NZ (↑40%)
  - WL: MR (↑38%), AO (↑33%)
  - RTE: TV (↓46%), TK (↓24%)
[10.0% - 19%]
  - HF-NA: US (↑11%)
  - RTE: CF (↑19%), TT (↓11%), TO (↓11%)
  - WL: KN (↑13%), CG (↓17%), ER (↑10%)
  - HF-INTL: IE (↑15%), NL (↑12%), DK (↑19%), SE (↓17%), NO (↑12%)
**Dimensions:**
[20% - 49%]
  - HF-INTL: CC Referral (↑22%)
[10.0% - 19%]
  - HF-INTL: CC Paid (↑16%)
  - RTE: CC Referral (↑16%)
  - HF-NA: CC Referral (↑19%)
  - WL: CC Referral (↑15%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W20

---

## Payment Fraud Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 0.72% to 0.58% (↓19.86%, not sig., vol: 23.1K)
- **HF-NA**: 2.08% to 1.32% (↓36.58%, not sig., vol: 8.3K)
- **HF-INTL**: 0.27% to 0.34% (↑24.84%, not sig., vol: 9.6K)
- **US-HF**: 2.33% to 1.04% (↓55.51%, not sig., vol: 9.5K)
- **RTE**: 0.25% to 0.29% (↑16.53%, not sig., vol: 6.8K)
- **WL**: 1.03% to 0.88% (↓14.49%, not sig., vol: 2.0K)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-NA: US (↓56%), CA (↑65%)
  - HF-INTL: DE (↓56%), AU (↑94%), NZ (↑350%), NL (↓100%), AT (↓100%)
  - WL: KN (↑111%)
[20% - 49%]
  - HF-INTL: FR (↑32%), IE (↓46%)
  - WL: CG (↓27%)
[10.0% - 19%]
  - RTE: FJ (↑13%)
  - WL: ER (↓11%)
  - HF-INTL: SE (↑11%)
**Dimensions:**
[+50%]
  - RTE: CC Referral (↑235%)
  - HF-INTL: CC Referral (↑82%)
  - WL: CC Referral (↑108%)
  - HF-NA: CC Referral (↓53%)
[10.0% - 19%]
  - HF-INTL: CC Paid (↑13%)
  - WL: CC Paid (↓19%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W20

---

## Payment Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 95.08% to 95.39% (↑0.33%, not sig., vol: 6.0K)
- **HF-NA**: 93.67% to 93.91% (↑0.25%, not sig., vol: 1.2K)
- **HF-INTL**: 97.28% to 97.56% (↑0.28%, not sig., vol: 2.1K)
- **US-HF**: 93.33% to 93.54% (↑0.22%, not sig., vol: 903.5)
- **RTE**: 94.15% to 94.79% (↑0.68%, not sig., vol: 2.8K)
- **WL**: 91.27% to 91.31% (↑0.05%, not sig., vol: 76.5)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - RTE: TK (↑3%)
**Dimensions:**
[20% - 49%]
  - RTE: PP Unknown (↑25%)
[2.5% - 19%]
  - WL: CustomerQuality Bad (↓16%)
  - RTE: LL a. 0 (↑3%), CustomerQuality Bad (↑9%)
  - HF-INTL: CustomerQuality Bad (↓8%), PP Unknown (↑8%)
  - HF-NA: PP Unknown (↑14%)

### Overall Summary

Payment Approval Rate improved across all clusters in 2026-W20, with changes ranging from +0.04pp to +0.68pp, though none reached statistical significance. The most notable finding was RTE's TK market exceeding the ±2.5% threshold (+2.69pp) driven by Apple Pay and Braintree improvements alongside reduced Insufficient Funds declines.

### Cluster Highlights

- **US-HF:** Stable at 93.54% (+0.23pp), with modest gains across all funnel stages led by FirstRunAR (+0.19pp) and no dimensions exceeding thresholds.
- **HF-INTL:** Improved to 97.56% (+0.29pp), driven primarily by FirstRunAR gains (+0.76pp) with all 14 countries showing stable performance within normal bounds.
- **WL:** Stable at 91.31% (+0.04pp), with KN showing the largest country movement (-1.95pp) but remaining below investigation thresholds.
- **HF-NA:** Recovered to 93.91% (+0.26pp) after W19's dip, with both US (+0.16pp) and CA (+0.40pp) contributing to improvement across all funnel stages.
- **RTE:** Strongest improvement to 94.79% (+0.68pp), with TK flagged at +2.69pp due to Apple Pay (+6.12pp) and Braintree (+5.04pp) gains combined with reduced Insufficient Funds declines.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W20

---

## AR Pre Dunning

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 92.89% to 93.28% (↑0.42%, not sig., vol: 7.6K)
- **HF-NA**: 92.00% to 92.15% (↑0.17%, not sig., vol: 811.8)
- **HF-INTL**: 94.61% to 95.08% (↑0.50%, not sig., vol: 3.7K)
- **US-HF**: 91.78% to 91.89% (↑0.13%, not sig., vol: 503.4)
- **RTE**: 92.00% to 92.73% (↑0.79%, not sig., vol: 3.3K)
- **WL**: 89.66% to 89.65% (↓0.01%, not sig., vol: 21.1)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - RTE: YE (↑3%), TK (↑3%)
  - HF-INTL: NO (↓3%)
**Dimensions:**
[2.5% - 19%]
  - WL: CustomerQuality Bad (↓16%)
  - RTE: LL a. 0 (↑3%), CustomerQuality Bad (↑10%), PP Unknown (↑11%)
  - HF-INTL: CustomerQuality Bad (↓9%), PP Unknown (↑6%)
  - HF-NA: CustomerQuality Bad (↓4%)

### Overall Summary

Acceptance Rate (Overall) improved or remained stable across all clusters in 2026-W20, with changes ranging from -0.01pp to +0.79pp, none reaching statistical significance. The most notable finding is a gradual 8-week downward trend in US-HF (92.22% → 91.89%) despite this week's minor uptick, warranting continued monitoring.

### Cluster Highlights

- **US-HF:** Stable at 91.89% (+0.12pp), with all funnel stages showing slight improvements but an 8-week downward drift from 92.22% continues.
- **HF-INTL:** Improved to 95.08% (+0.50pp) with broad-based gains across all countries and payment methods, led by FirstRunAR improvement of +0.76pp.
- **WL:** Essentially flat at 89.65% (-0.01pp) with no material changes across any dimension; KN showed the largest country movement at -2.01pp but remained within tolerance.
- **HF-NA:** Stable at 92.15% (+0.16pp) with modest improvements across all funnel stages; both US (+0.08pp) and CA (+0.39pp) showed aligned positive movement.
- **RTE:** Improved to 92.73% (+0.79pp), driven primarily by TK (+2.93pp) where Apple Pay (+6.43pp) and Braintree (+5.25pp) gains reduced Insufficient Funds declines.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W20

---

## Acceptance LL0 (Initial Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 91.97% to 92.23% (↑0.28%, not sig., vol: 240.4)
- **HF-NA**: 89.72% to 88.94% (↓0.88%, not sig., vol: 131.8)
- **HF-INTL**: 92.66% to 92.60% (↓0.07%, not sig., vol: 20.1)
- **US-HF**: 88.24% to 87.61% (↓0.72%, not sig., vol: 76.7)
- **RTE**: 92.31% to 93.63% (↑1.43%, not sig., vol: 433.0)
- **WL**: 92.19% to 91.91% (↓0.31%, not sig., vol: 37.7)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - RTE: YE (↑3%), TO (↓4%)
  - WL: ER (↓3%)
  - HF-INTL: NZ (↓3%), LU (↑3%)
**Dimensions:**
[2.5% - 19%]
  - HF-INTL: PP Unknown (↑3%)
  - HF-NA: PM Paypal (↓4%)
  - WL: PM Paypal (↓3%)

### Overall Summary

Acceptance Rate (Initial Charges) performance was mixed across clusters in 2026-W20, with RTE showing significant improvement (+1.43pp to 93.63%) while other clusters experienced minor, non-significant declines ranging from -0.06pp to -0.87pp. PayPal emerged as a consistent concern across multiple clusters, with notable declines in US-HF (-4.47pp), HF-NA (-3.81pp), and WL's ER market (-17.59pp).

### Cluster Highlights

- **US-HF:** Declined by -0.63pp to 87.61% (not significant), driven primarily by PayPal payment method dropping -4.47pp to 84.37% on 870 orders.
- **HF-INTL:** Stable at 92.6% with a marginal -0.06pp decline (not significant), though NZ flagged with -3.37pp decline due to increased Insufficient Funds on Braintree.
- **WL:** Declined by -0.28pp to 91.91% (not significant), with ER country exceeding threshold (-2.63pp) driven by PayPal collapsing -17.59pp due to increased Refused declines.
- **HF-NA:** Declined by -0.78pp to 88.94% (not significant), with PayPal flagged as the only dimension exceeding threshold at -3.81pp across both US and CA markets.
- **RTE:** Improved significantly by +1.43pp to 93.63% (8-week high), driven by Credit Card improvement (+1.89pp) and reduced Insufficient Funds in YE (+2.59pp), partially offset by TO's Apple Pay/Braintree degradation (-3.84pp).

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W20

---

## Acceptance LL0 and LL1+ (Recurring Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 92.93% to 93.33% (↑0.43%, not sig., vol: 7.3K)
- **HF-NA**: 92.07% to 92.25% (↑0.20%, not sig., vol: 947.3)
- **HF-INTL**: 94.70% to 95.19% (↑0.52%, not sig., vol: 3.7K)
- **US-HF**: 91.87% to 92.01% (↑0.15%, not sig., vol: 594.9)
- **RTE**: 91.98% to 92.66% (↑0.74%, not sig., vol: 2.8K)
- **WL**: 89.46% to 89.47% (↑0.00%, not sig., vol: 6.6)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - RTE: YE (↑3%), TO (↑3%), TK (↑3%)
  - HF-INTL: NO (↓3%)
**Dimensions:**
[20% - 49%]
  - HF-INTL: PP Unknown (↑33%)
[2.5% - 19%]
  - WL: CustomerQuality Bad (↓16%)
  - RTE: CustomerQuality Bad (↑10%)
  - HF-INTL: CustomerQuality Bad (↓9%)
  - HF-NA: CustomerQuality Bad (↓4%), PP Unknown (↓3%)
**Low Volume (denom < 50):** 2 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W20

---

## Ship Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 53.04% to 52.04% (↓1.90%, not sig., vol: 1.3K)
- **HF-NA**: 47.63% to 48.30% (↑1.40%, not sig., vol: 233.7)
- **HF-INTL**: 68.52% to 67.23% (↓1.89%, not sig., vol: 500.8)
- **US-HF**: 46.38% to 47.14% (↑1.64%, not sig., vol: 214.7)
- **RTE**: 42.95% to 42.92% (↓0.07%, not sig., vol: 14.5)
- **WL**: 32.85% to 31.84% (↓3.07%, not sig., vol: 247.5)

**Deep Insights**
**Business Units:**
[+50%]
  - WL: MR (↓70%)
  - RTE: TV (↑245%)
[10.0% - 19%]
  - WL: ER (↑15%), GN (↓12%)
  - HF-INTL: SE (↑15%), CH (↑11%)
  - RTE: TZ (↑17%), TT (↑16%), TK (↑11%)

### Overall Summary

Dunning Ship Rate performance was mixed globally in 2026-W20, with HF-NA (+0.66pp) and US-HF (+0.76pp) showing improvement while HF-INTL (-1.30pp) and WL (-1.01pp) declined during the Pre-Payday to Payday transition. The most significant concern is HF-INTL's FR market, which experienced a -6.1% Ship Rate decline despite improved Pre-Dunning AR, combined with a -25.7% volume drop that warrants immediate investigation.

### Cluster Highlights

- **US-HF:** Ship Rate improved by +0.76pp (46.38% → 47.14%) driven by Payday phase timing, though elevated Discount % (+9.6%) and PC2 decline (-7.3%) require monitoring.
- **HF-INTL:** Ship Rate declined by -1.30pp (68.53% → 67.23%) primarily driven by FR's -6.1% drop and unfavorable volume mix shift away from higher-performing markets.
- **WL:** Ship Rate declined by -1.01pp (32.85% → 31.84%) due to severe PC2 collapse (-22.9%) at cluster level, with CK and GN showing increased discounting failing to convert to shipments.
- **HF-NA:** Ship Rate improved by +0.66pp (47.63% → 48.29%) with US contributing the largest gain (+1.6%), consistent with expected Payday phase behavior despite PC2 pressure.
- **RTE:** Ship Rate remained essentially flat (-0.02pp) at 42.93% despite positive leading indicators, with Simpson's Paradox detected as high-performing YE lost -16.3% volume share.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W20

---

## Recovery W0

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 47.72% to 43.13% (↓9.63%, not sig., vol: 3.5K)
- **HF-NA**: 39.76% to 38.70% (↓2.65%, not sig., vol: 213.1)
- **HF-INTL**: 50.45% to 44.37% (↓12.06%, not sig., vol: 2.1K)
- **US-HF**: 42.62% to 40.52% (↓4.93%, not sig., vol: 303.9)
- **RTE**: 50.29% to 45.65% (↓9.23%, not sig., vol: 767.3)
- **WL**: 42.28% to 40.26% (↓4.78%, not sig., vol: 122.9)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - HF-INTL: FR (↓43%), BE (↓32%), DK (↓49%), LU (↓31%), CH (↓24%)
  - RTE: TO (↓28%)
[10.0% - 19%]
  - RTE: FJ (↓12%), CF (↓10%)
  - HF-INTL: NO (↓15%), SE (↓19%), NL (↓14%), AT (↓17%)
  - WL: KN (↓16%)
**Low Volume (denom < 50):** 4 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W20

---

## Recovery W12

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 84.49% to 85.38% (↑1.06%, not sig., vol: 478.2)
- **HF-NA**: 79.49% to 80.12% (↑0.80%, not sig., vol: 77.9)
- **HF-INTL**: 87.57% to 88.29% (↑0.82%, not sig., vol: 192.1)
- **US-HF**: 79.50% to 80.33% (↑1.05%, not sig., vol: 72.0)
- **RTE**: 84.67% to 84.61% (↓0.07%, not sig., vol: 6.4)
- **WL**: 80.59% to 82.22% (↑2.03%, not sig., vol: 60.2)

**Deep Insights**
**Business Units:**
[10.0% - 19%]
  - WL: KN (↑14%)
  - RTE: TK (↓15%), TO (↑16%), TV (↑12%)
**Low Volume (denom < 50):** 2 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W20

---

## Dunning Profit

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: €9.28 to €10.37 (↑11.83%, not sig., vol: 9.2K)
- **HF-NA**: €10.79 to €11.39 (↑5.50%, not sig., vol: 999.9)
- **HF-INTL**: €9.96 to €11.01 (↑10.55%, not sig., vol: 3.6K)
- **US-HF**: €10.96 to €11.29 (↑2.97%, not sig., vol: 404.7)
- **RTE**: €8.27 to €9.89 (↑19.56%, not sig., vol: 3.7K)
- **WL**: €4.97 to €5.89 (↑18.38%, not sig., vol: 1.3K)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: ES (↑66%), IT (↑58%)
[20% - 49%]
  - RTE: FJ (↑20%), CF (↑41%)
  - HF-INTL: GB (↑28%), NO (↑31%), SE (↑40%), DK (↑38%), NL (↑26%)
  - WL: AO (↑32%)
[10.0% - 19%]
  - HF-NA: CA (↑14%)
  - HF-INTL: DE (↑14%), NZ (↑20%), CH (↓12%)
  - WL: ER (↑20%), CK (↑12%), CG (↑12%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W20

---
