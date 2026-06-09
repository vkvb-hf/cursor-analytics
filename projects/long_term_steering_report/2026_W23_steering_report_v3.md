# Steering Report - 2026-W23 (v3)

**Week:** 2026-W23  
**Generated:** 2026-06-09 14:42

---

## Payment Checkout Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 95.18% to 95.52% (↑0.35%, not sig., vol: 335.4)
- **HF-NA**: 91.93% to 92.74% (↑0.88%, not sig., vol: 172.4)
- **HF-INTL**: 94.47% to 95.04% (↑0.60%, not sig., vol: 190.3)
- **US-HF**: 90.39% to 91.56% (↑1.29%, not sig., vol: 197.5)
- **RTE**: 97.00% to 97.11% (↑0.10%, not sig., vol: 38.2)
- **WL**: 97.04% to 96.88% (↓0.16%, not sig., vol: 13.4)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - RTE: TT (↓3%)
  - HF-INTL: AT (↑5%)
**Dimensions:**
[2.5% - 19%]
  - HF-NA: FinalTokenType None (↓5%), CheckoutType otp (↓5%), PM Others (↑4%), FinalTokenType false (↑3%)

### Overall Summary

Payment Checkout Approval Rate improved or remained stable across all clusters in 2026-W23, with US-HF showing the only statistically significant change at +1.29pp. The most notable finding was the broad-based recovery in US-HF driven by Apple Pay (+1.88pp) and Credit Card (+1.13pp) improvements, while AT in HF-INTL saw PayPal approval rates jump from 90.74% to 100%.

### Cluster Highlights

- **US-HF:** Significant improvement of +1.29pp (90.39% → 91.56%) driven by Apple Pay (+1.88pp on 5,293 orders) and Credit Card (+1.13pp on 8,750 orders), continuing recovery toward the W16 baseline of 92.75%.
- **HF-INTL:** Modest improvement of +0.60pp (94.47% → 95.04%), not statistically significant, with AT exceeding threshold at +4.79pp due to PayPal and Braintree recovery.
- **WL:** Stable at 96.88% (-0.16pp), with no countries exceeding investigation thresholds despite KN experiencing a 66.1% volume drop.
- **HF-NA:** Improved +0.88pp (91.93% → 92.74%), not statistically significant, with US driving gains at +1.29pp while CA remained stable at 97.10%.
- **RTE:** Stable at 97.11% (+0.11pp), with TT flagged at -3.23pp driven by PayPal (-20pp) and Klarna (-14pp) declines on low volume (624 orders).

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W23

---

## Payment Page Visit to Success

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 33.52% to 33.94% (↑1.25%, not sig., vol: 2.8K)
- **HF-NA**: 27.77% to 27.74% (↓0.09%, not sig., vol: 48.7)
- **HF-INTL**: 36.83% to 36.91% (↑0.22%, not sig., vol: 140.6)
- **US-HF**: 26.02% to 25.90% (↓0.47%, not sig., vol: 206.7)
- **RTE**: 38.67% to 39.76% (↑2.83%, not sig., vol: 1.6K)
- **WL**: 29.36% to 29.99% (↑2.15%, not sig., vol: 962.9)

**Deep Insights**
**Business Units:**
[5.0% - 19%]
  - WL: MR (↑17%), KN (↓7%), CK (↑11%), AO (↑5%)
  - HF-INTL: AU (↓8%), DE (↑5%), IE (↓11%), NZ (↑6%), SE (↑5%)
  - RTE: TV (↓14%), TK (↑10%)

### Overall Summary

Payment Conversion Rate (Checkout) showed mixed performance across clusters in 2026-W23, with RTE (+1.10pp) and WL (+0.61pp) improving while US-HF (-0.13pp) and HF-NA (-0.04pp) declined marginally. The most significant finding is the substantial improvement in payment method success rates across all clusters—particularly ProcessOut_CreditCard and Braintree_ApplePay—which offset top-of-funnel engagement declines in Select Payment Method conversion.

### Cluster Highlights

- **US-HF:** PCR declined marginally by -0.13pp to 26.03%, driven by FE Validation recovery rate dropping -2.29pp while backend payment method success rates improved significantly (ProcessOut_CreditCard +12.40pp).
- **HF-INTL:** PCR improved slightly by +0.07pp to 36.96%, with GB driving gains (+1.77pp) offsetting declines in AU (-2.70pp) and IE (-5.01pp), while Adyen_Sepa remains non-functional at 0% success rate.
- **WL:** PCR improved by +0.61pp to 30.01%, driven by gains across all payment methods (Braintree_ApplePay +14.61pp, ProcessOut_ApplePay +15.24pp) and improved FE Validation recovery rate (+1.86pp).
- **HF-NA:** PCR remained essentially stable at 27.86% (-0.04pp), with Select Payment Method conversion declining -0.77pp offset by significant payment method success rate improvements (Adyen_CreditCard +14.35pp).
- **RTE:** PCR improved by +1.10pp to 39.81%, driven by FE Validation Passed gains (+0.87pp) from apparent Apple Pay address validation fixes and strong payment method performance (Braintree_ApplePay +19.53pp).

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W23

---

## Payment Page Visit to Success (Backend)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 33.15% to 33.85% (↑2.11%, not sig., vol: 6.2K)
- **HF-NA**: 28.77% to 28.85% (↑0.29%, not sig., vol: 177.8)
- **HF-INTL**: 39.16% to 39.63% (↑1.20%, not sig., vol: 941.0)
- **US-HF**: 26.94% to 26.99% (↑0.19%, not sig., vol: 92.1)
- **RTE**: 33.99% to 35.31% (↑3.87%, not sig., vol: 3.9K)
- **WL**: 27.94% to 28.32% (↑1.35%, not sig., vol: 707.9)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - HF-INTL: LU (↑42%)
[5.0% - 19%]
  - RTE: FJ (↑5%), TK (↑13%), TV (↓10%), TO (↑5%)
  - WL: MR (↑17%), KN (↓8%), CK (↑11%), AO (↑9%)
  - HF-INTL: DE (↑5%), AU (↓7%), IE (↓12%), BE (↑8%), NZ (↑6%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W23

---

## Reactivation Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 90.64% to 90.88% (↑0.26%, not sig., vol: 251.0)
- **HF-NA**: 90.67% to 91.83% (↑1.27%, not sig., vol: 294.3)
- **HF-INTL**: 91.07% to 90.70% (↓0.40%, not sig., vol: 170.0)
- **US-HF**: 89.95% to 91.44% (↑1.66%, not sig., vol: 296.4)
- **RTE**: 89.71% to 89.99% (↑0.31%, not sig., vol: 61.8)
- **WL**: 90.86% to 91.33% (↑0.52%, not sig., vol: 48.4)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - WL: KN (↓3%)
**Dimensions:**
[2.5% - 19%]
  - RTE: PM Others (↑6%)
**Low Volume (denom < 50):** 7 segments excluded

### Overall Summary

Reactivation Rate improved or remained stable across all clusters in 2026-W23, with significant gains in US-HF (+1.66%) and HF-NA (+1.28%) while other clusters showed non-significant fluctuations within normal ranges. The most notable finding is the broad-based improvement in North American clusters driven by Credit Card performance gains and substantial volume increases.

### Cluster Highlights

- **US-HF:** Significant improvement from 89.95% to 91.44% (+1.66%) driven by Credit Card gains (+1.71pp) and 33.3% volume increase to 17,834 orders, reaching the 8-week high.
- **HF-INTL:** Stable with non-significant decline from 91.07% to 90.70% (-0.41%), with flagged fluctuations in LU (-9.93pp) and CH (+6.06pp) driven by extremely low volumes (<50 orders each).
- **WL:** Stable improvement from 90.86% to 91.33% (+0.52%), continuing an 8-week upward trend (+4.52pp since W16) despite Apple Pay underperformance in KN (-8.16%).
- **HF-NA:** Significant improvement from 90.67% to 91.83% (+1.28%) led by US Credit Card performance (+1.45%) and 21.8% volume growth to 23,119 orders.
- **RTE:** Stable at 89.99% (+0.31%), with flagged country variations in TK, TO, and TV attributable to volumes under 50 orders where single-order outcomes cause unreliable rate swings.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W23

---

## Fraud Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 93.40% to 93.63% (↑0.25%, not sig., vol: 288.7)
- **HF-NA**: 92.41% to 92.70% (↑0.31%, not sig., vol: 69.1)
- **HF-INTL**: 92.51% to 92.66% (↑0.16%, not sig., vol: 63.0)
- **US-HF**: 92.52% to 93.00% (↑0.52%, not sig., vol: 87.1)
- **RTE**: 94.59% to 94.74% (↑0.15%, not sig., vol: 57.7)
- **WL**: 93.97% to 94.60% (↑0.67%, not sig., vol: 107.9)

**Deep Insights**
**Business Units:**
[5.0% - 19%]
  - RTE: TZ (↓5%)
**Dimensions:**
[+50%]
  - HF-NA: PM Credit Card (↑143%), PM Apple Pay (↑152%)
  - RTE: PM Unknown (↓56%)
**Low Volume (denom < 50):** 1 segment excluded

### Overall Summary

Fraud Approval Rate remained stable globally in 2026-W23, with all five clusters showing modest, non-significant improvements ranging from +0.15pp to +0.67pp. The most significant cross-cluster development is the activation of a new duplicate detection system, which revealed substantial duplicate rates (14-32%) across all clusters, with Referral channels showing notably higher duplicate block rates than Paid channels.

### Cluster Highlights

- **US-HF:** FAR improved slightly to 93.00% (+0.52pp), with a notable spike in Duplicate Rate from 0% to 24.73% following new detection system deployment.
- **HF-INTL:** FAR stable at 92.66% (+0.16pp), with CH exceeding the ±2.5% threshold (+3.63pp) and Referral channel showing elevated duplicate blocking across multiple markets.
- **WL:** FAR improved to 94.60% (+0.67pp), driven primarily by strong MR volume growth (+58.4%) in the Paid channel.
- **HF-NA:** FAR improved to 92.70% (+0.31pp), continuing an 8-week upward trend (+2.95pp cumulative) with US driving gains (+0.48pp) while CA declined slightly (-0.32pp).
- **RTE:** FAR stable at 94.74% (+0.15pp), with TZ flagged for significant FAR decline (-5.17pp) driven by elevated Referral channel duplicate rates (28.77%).

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W23

---

## Total Duplicate Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 0.00% to 23.28% (↑2534926.32%, not sig., vol: 2909.7M)
- **HF-NA**: 0.00% to 26.10% (↑578134.19%, not sig., vol: 128.3M)
- **HF-INTL**: 0.00% to 32.72% (↓0.00%, not sig., vol: 0.0)
- **US-HF**: 0.01% to 24.94% (↑404375.64%, not sig., vol: 67.2M)
- **RTE**: 0.00% to 16.13% (↓0.00%, not sig., vol: 0.0)
- **WL**: 0.00% to 14.15% (↓0.00%, not sig., vol: 0.0)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-NA: US (↑404376%)
**Dimensions:**
[+50%]
  - HF-NA: CC Paid (↑457352%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W23

---

## Total Duplicate Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 0.00% to 4.97% (↓0.00%, not sig., vol: 0.0)
- **HF-NA**: 0.00% to 5.52% (↓0.00%, not sig., vol: 0.0)
- **HF-INTL**: 0.00% to 5.94% (↓0.00%, not sig., vol: 0.0)
- **US-HF**: 0.00% to 5.50% (↓0.00%, not sig., vol: 0.0)
- **RTE**: 0.00% to 4.17% (↓0.00%, not sig., vol: 0.0)
- **WL**: 0.00% to 3.84% (↓0.00%, not sig., vol: 0.0)

**Deep Insights**
- No significant insights

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W23

---

## Payment Fraud Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 0.55% to 0.51% (↓6.88%, not sig., vol: 7.9K)
- **HF-NA**: 1.05% to 0.93% (↓11.31%, not sig., vol: 2.5K)
- **HF-INTL**: 0.37% to 0.22% (↓40.32%, not sig., vol: 15.3K)
- **US-HF**: 0.76% to 0.71% (↓7.16%, not sig., vol: 1.2K)
- **RTE**: 0.34% to 0.36% (↑4.35%, not sig., vol: 1.7K)
- **WL**: 0.74% to 0.98% (↑32.32%, not sig., vol: 5.2K)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: GB (↑107%), DE (↓85%), IE (↑302%), AU (↓65%), DK (↑113%)
  - WL: KN (↑132%), ER (↑77%)
  - RTE: TK (↓100%)
[20% - 49%]
  - HF-INTL: FR (↓44%), BE (↑41%), NZ (↓37%), SE (↑21%)
[10.0% - 19%]
  - HF-NA: CA (↓13%)
**Dimensions:**
[+50%]
  - HF-INTL: CC Referral (↓53%)
  - WL: CC Referral (↑90%)
[20% - 49%]
  - HF-INTL: CC Paid (↓37%)
  - WL: CC Paid (↑28%)
  - RTE: CC Referral (↓38%)
  - HF-NA: CC Referral (↓29%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W23

---

## Payment Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 95.22% to 95.38% (↑0.17%, not sig., vol: 3.0K)
- **HF-NA**: 93.43% to 93.67% (↑0.26%, not sig., vol: 1.2K)
- **HF-INTL**: 97.44% to 97.54% (↑0.10%, not sig., vol: 697.7)
- **US-HF**: 92.92% to 93.19% (↑0.30%, not sig., vol: 1.1K)
- **RTE**: 94.94% to 94.97% (↑0.03%, not sig., vol: 133.7)
- **WL**: 90.96% to 91.44% (↑0.52%, not sig., vol: 803.5)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - RTE: TK (↓3%)
**Dimensions:**
[20% - 49%]
  - HF-NA: CustomerQuality Bad (↑23%)
[2.5% - 19%]
  - WL: CustomerQuality Bad (↑14%), LL a. 0 (↑3%)
  - HF-INTL: CustomerQuality Bad (↑12%)
  - RTE: CustomerQuality Bad (↓5%)
  - HF-NA: PP Unknown (↑15%)

### Overall Summary

Payment Approval Rate improved marginally across all clusters in 2026-W23, with changes ranging from +0.03pp to +0.53pp, though none reached statistical significance. The most notable finding was TK in the RTE cluster experiencing a -3.24pp decline driven by Apple Pay via Braintree, though its low volume (0.5% of RTE) limited overall impact.

### Cluster Highlights

- **US-HF:** Improved by +0.27pp to 93.19%, with gains across all funnel stages and no dimensional anomalies requiring investigation.
- **HF-INTL:** Stable at 97.54% (+0.10pp), with GB volume increasing +10.5% while maintaining rate improvement.
- **WL:** Improved by +0.48pp to 91.44%, with PreDunningAR showing the largest gain (+0.52pp) and Apple Pay improving +0.94pp.
- **HF-NA:** Improved by +0.24pp to 93.67%, driven by FirstRunAR gains (+0.47pp) with both US and CA showing stable slight improvements.
- **RTE:** Stable at 94.97% (+0.03pp), though TK declined -3.24pp due to Apple Pay and Braintree degradation with increased "Insufficient Funds" declines.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W23

---

## AR Pre Dunning

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 92.93% to 93.11% (↑0.19%, not sig., vol: 3.3K)
- **HF-NA**: 91.73% to 92.04% (↑0.34%, not sig., vol: 1.6K)
- **HF-INTL**: 94.49% to 94.63% (↑0.14%, not sig., vol: 1.0K)
- **US-HF**: 91.27% to 91.63% (↑0.39%, not sig., vol: 1.5K)
- **RTE**: 92.90% to 92.85% (↓0.05%, not sig., vol: 204.6)
- **WL**: 89.32% to 89.84% (↑0.58%, not sig., vol: 884.8)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - RTE: TK (↓4%)
**Dimensions:**
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↑16%), PP Unknown (↑14%)
  - HF-INTL: CustomerQuality Bad (↑13%)
  - WL: CustomerQuality Bad (↑15%), LL a. 0 (↑3%)
  - RTE: CustomerQuality Bad (↓3%)

### Overall Summary

Acceptance Rate (Overall) improved modestly across all clusters in 2026-W23, with changes ranging from -0.05pp to +0.58pp, though none were statistically significant. The most notable finding was CH's +2.55pp improvement in HF-INTL driven by reduced "Insufficient Funds" declines and the discontinuation of the twint payment method.

### Cluster Highlights

- **US-HF:** Improved by +0.39pp to 91.63% with gains across all funnel stages, though Apple Pay continues to underperform at 84.68% vs. Credit Card at 92.24%.
- **HF-INTL:** Improved by +0.15pp to 94.63%, with CH exceeding threshold (+2.55pp) due to reduced Insufficient Funds declines and twint discontinuation.
- **WL:** Improved by +0.58pp to 89.84% with stable performance across all countries and payment methods, no dimensions exceeding thresholds.
- **HF-NA:** Improved by +0.34pp to 92.04% with both US (+0.31pp) and CA (+0.22pp) showing stable gains; Unknown PaymentProvider flagged but represents <0.12% of volume.
- **RTE:** Stable at 92.85% (-0.05pp), with TK the only country exceeding threshold (-3.69pp) due to applepay decline and increased Insufficient Funds, though impact is minimal at 0.5% of total volume.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W23

---

## Acceptance LL0 (Initial Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 90.57% to 90.54% (↓0.04%, not sig., vol: 31.0)
- **HF-NA**: 86.92% to 87.06% (↑0.17%, not sig., vol: 25.8)
- **HF-INTL**: 90.03% to 90.41% (↑0.41%, not sig., vol: 113.3)
- **US-HF**: 85.71% to 85.50% (↓0.24%, not sig., vol: 25.9)
- **RTE**: 92.76% to 91.91% (↓0.91%, not sig., vol: 250.4)
- **WL**: 91.04% to 92.08% (↑1.15%, not sig., vol: 143.4)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: FR (↓4%), BE (↓3%), SE (↑5%), NZ (↓4%), AT (↑5%)
  - WL: CK (↑5%), AO (↓3%)
  - RTE: TK (↓6%), TO (↑4%)
**Dimensions:**
[2.5% - 19%]
  - WL: PM Paypal (↑6%)
  - HF-NA: PP Unknown (↑12%), PM Others (↑3%)
  - RTE: PP Unknown (↓5%)
**Low Volume (denom < 50):** 1 segment excluded

### Overall Summary

Acceptance Rate (Initial Charges) showed mixed performance across clusters in 2026-W23, with most changes statistically non-significant except for WL which improved significantly by +1.14% to 92.08%. The most notable concern is US-HF's sustained 8-week downward trend (-3.41pp cumulative from W16), while HF-INTL's overall improvement masks significant country-level volatility with NZ declining -3.84pp and FR declining -3.67pp driven by rising Insufficient Funds declines.

### Cluster Highlights

- **US-HF:** Declined slightly by -0.21pp to 85.50% (not significant), with PayPal showing the most notable deterioration at -2.84pp and an 8-week cumulative erosion of -3.41pp requiring continued monitoring.
- **HF-INTL:** Improved by +0.38pp to 90.41% (not significant), though NZ (-3.84pp) and FR (-3.67pp) exceeded thresholds due to rising Insufficient Funds, offset by gains in SE (+4.89pp) and AT (+4.97pp).
- **WL:** Improved significantly by +1.14% to 92.08%, driven by CK's +4.93pp gain where PayPal acceptance via Braintree surged +35.13pp, partially offset by AO's -2.98pp decline in Apple Pay via ProcessOut.
- **HF-NA:** Stable with marginal improvement of +0.14pp to 87.06% (not significant), though the 8-week trend shows a -3.12pp decline from W17's 90.18% warranting continued observation.
- **RTE:** Declined by -0.85pp to 91.91% (not significant), with TK experiencing a -5.51pp drop driven by Apple Pay via Braintree and a +4.49pp increase in Insufficient Funds declines.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W23

---

## Acceptance LL0 and LL1+ (Recurring Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 93.04% to 93.24% (↑0.21%, not sig., vol: 3.5K)
- **HF-NA**: 91.89% to 92.21% (↑0.35%, not sig., vol: 1.6K)
- **HF-INTL**: 94.64% to 94.79% (↑0.16%, not sig., vol: 1.1K)
- **US-HF**: 91.43% to 91.81% (↑0.42%, not sig., vol: 1.5K)
- **RTE**: 92.91% to 92.92% (↑0.01%, not sig., vol: 44.7)
- **WL**: 89.18% to 89.64% (↑0.51%, not sig., vol: 721.9)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - RTE: TK (↓3%)
  - HF-INTL: CH (↑3%)
**Dimensions:**
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↑16%)
  - HF-INTL: CustomerQuality Bad (↑13%), PP Unknown (↓8%)
  - WL: CustomerQuality Bad (↑15%)
  - RTE: CustomerQuality Bad (↓3%)
**Low Volume (denom < 50):** 2 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W23

---

## Ship Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 53.56% to 54.02% (↑0.87%, not sig., vol: 611.2)
- **HF-NA**: 44.64% to 45.18% (↑1.23%, not sig., vol: 190.7)
- **HF-INTL**: 70.45% to 70.75% (↑0.43%, not sig., vol: 124.6)
- **US-HF**: 44.15% to 45.54% (↑3.13%, not sig., vol: 381.7)
- **RTE**: 44.18% to 44.20% (↑0.05%, not sig., vol: 8.3)
- **WL**: 30.81% to 31.42% (↑1.96%, not sig., vol: 148.0)

**Deep Insights**
**Business Units:**
[+50%]
  - WL: MR (↑118%)
[20% - 49%]
  - WL: GN (↑21%)
[10.0% - 19%]
  - HF-INTL: SE (↓17%), NL (↓12%), CH (↓15%)
  - RTE: TO (↑20%), TK (↓19%), TZ (↓16%), TV (↑17%)

### Overall Summary

Dunning Ship Rate remained stable globally in 2026-W23, with all five clusters showing modest movements between -0.03pp and +1.35pp as the payday phase transitioned from Mid-Cycle to Pre-Payday. The most significant concern is the divergent country-level performance masked by cluster aggregates, particularly SE's -17.3pp decline in HF-INTL and CA's -5.7% decline in HF-NA despite favorable payday timing.

### Cluster Highlights

- **US-HF:** Ship Rate improved +1.35pp (44.15% → 45.50%) driven by Pre-Payday phase timing and strong PC2 gains (+5.7%) with reduced discount reliance (-5.5%).
- **HF-INTL:** Ship Rate stable at +0.16pp (70.45% → 70.61%) as DK's +9.7pp surge offset sharp declines in SE (-17.3pp) and CH (-15.4pp) driven by aggressive discounting.
- **WL:** Ship Rate improved +0.56pp (30.82% → 31.38%) led by GN's +20.7% gain, though cluster improvement masks concerning -9.9% decline in ER despite increased discounting.
- **HF-NA:** Ship Rate improved +0.51pp (44.63% → 45.14%) driven by US (+3.1%) with reduced discounting, partially offset by CA's -5.7% decline amid +12.2% discount increase requiring investigation.
- **RTE:** Ship Rate essentially flat at -0.03pp (44.19% → 44.16%) with volume up 6.9%, as TO's +19.6% improvement offset TZ's -18.0% decline warranting continued monitoring.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W23

---

## Recovery W0

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 42.73% to 49.57% (↑16.00%, not sig., vol: 6.1K)
- **HF-NA**: 35.78% to 42.96% (↑20.06%, not sig., vol: 1.4K)
- **HF-INTL**: 43.82% to 51.03% (↑16.45%, not sig., vol: 3.4K)
- **US-HF**: 36.62% to 44.15% (↑20.56%, not sig., vol: 1.1K)
- **RTE**: 46.71% to 52.08% (↑11.48%, not sig., vol: 926.7)
- **WL**: 42.53% to 47.85% (↑12.50%, not sig., vol: 295.9)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: DE (↑51%), AT (↑53%)
[20% - 49%]
  - HF-INTL: FR (↑45%), GB (↑25%), DK (↑45%), NL (↓27%), CH (↑24%)
  - HF-NA: US (↑21%)
  - WL: CK (↑26%), ER (↑30%)
  - RTE: TZ (↑42%)
[10.0% - 19%]
  - RTE: FJ (↑14%), CF (↑16%)
  - HF-INTL: BE (↑17%), IE (↑11%), LU (↑17%)
  - HF-NA: CA (↑18%)
  - WL: GN (↑19%)
**Low Volume (denom < 50):** 3 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W23

---

## Recovery W12

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 86.96% to 84.51% (↓2.82%, not sig., vol: 1.1K)
- **HF-NA**: 81.47% to 80.72% (↓0.92%, not sig., vol: 76.4)
- **HF-INTL**: 89.67% to 86.82% (↓3.18%, not sig., vol: 629.8)
- **US-HF**: 80.90% to 80.40% (↓0.63%, not sig., vol: 39.2)
- **RTE**: 85.52% to 84.05% (↓1.72%, not sig., vol: 144.1)
- **WL**: 83.27% to 80.79% (↓2.98%, not sig., vol: 82.6)

**Deep Insights**
**Business Units:**
[+50%]
  - WL: MR (↓51%)
[10.0% - 19%]
  - RTE: TO (↑19%)
  - HF-INTL: ES (↓19%)
**Low Volume (denom < 50):** 4 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W23

---

## Dunning Profit

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: €11.19 to €10.07 (↓10.01%, not sig., vol: 7.0K)
- **HF-NA**: €11.43 to €11.09 (↓2.95%, not sig., vol: 468.1)
- **HF-INTL**: €12.45 to €10.62 (↓14.72%, not sig., vol: 4.4K)
- **US-HF**: €11.08 to €10.79 (↓2.65%, not sig., vol: 333.6)
- **RTE**: €10.32 to €9.67 (↓6.36%, not sig., vol: 1.2K)
- **WL**: €5.82 to €5.70 (↓2.13%, not sig., vol: 121.3)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - HF-INTL: GB (↓22%), FR (↓24%), DE (↓22%), SE (↓44%), IE (↓31%)
  - WL: GN (↓35%)
[10.0% - 19%]
  - RTE: YE (↓11%)
  - WL: ER (↑13%), CG (↓19%)
  - HF-INTL: BE (↓11%), NL (↓19%), CH (↓17%), LU (↓16%)
**Low Volume (denom < 50):** 1 segment excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W23

---
