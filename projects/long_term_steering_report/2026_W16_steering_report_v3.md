# Steering Report - 2026-W16 (v3)

**Week:** 2026-W16  
**Generated:** 2026-04-22 14:42

---

## Payment Checkout Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 96.25% to 96.54% (↑0.30%, not sig., vol: 350.5)
- **HF-NA**: 94.08% to 93.86% (↓0.23%, not sig., vol: 54.7)
- **HF-INTL**: 96.12% to 97.13% (↑1.05%, not sig., vol: 392.2)
- **US-HF**: 93.02% to 92.75% (↓0.29%, not sig., vol: 52.6)
- **RTE**: 97.22% to 97.20% (↓0.01%, not sig., vol: 5.7)
- **WL**: 97.37% to 97.59% (↑0.22%, not sig., vol: 24.3)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: DE (↑4%), BE (↑4%)
  - RTE: TT (↑8%)
  - WL: MR (↑3%)
**Dimensions:**
[2.5% - 19%]
  - HF-INTL: PM Others (↑7%)
  - RTE: PM Others (↑9%)
**Low Volume (denom < 50):** 1 segment excluded

### Overall Summary

Payment Checkout Approval Rate remained broadly stable across clusters in 2026-W16, with most changes falling within normal variance and only HF-INTL showing a statistically significant improvement (+1.01pp to 97.13%). The most notable finding is the sharp decline in Adyen provider performance with specific payment methods (BcmcMobile in BE and Klarna in DE) in HF-INTL, though reduced volume from these underperforming combinations actually contributed to the overall rate improvement.

### Cluster Highlights

- **US-HF:** Stable at 92.75% with a non-significant -0.29pp decline, volume increased 2.7% with no dimensions exceeding alert thresholds.
- **HF-INTL:** Improved significantly by +1.01pp to 97.13%, driven by DE (+4.35pp) and BE (+3.72pp) as low-performing Adyen/Klarna and Adyen/BcmcMobile combinations saw reduced volume.
- **WL:** Stable at 97.59% (+0.23pp, non-significant), with MR showing ApplePay/Braintree recovery (+7.14pp/+5.88pp) on low volume.
- **HF-NA:** Stable at 93.86% (-0.22pp, non-significant), with US declining -0.29pp while CA improved +0.44pp despite 10.5% volume decrease.
- **RTE:** Stable at 97.20% (-0.02pp, non-significant), with TT improving +7.93pp driven by IDeal/Adyen performance gains on 55% higher volume.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Payment Page Visit to Success

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 36.45% to 36.82% (↑1.03%, not sig., vol: 2.4K)
- **HF-NA**: 27.92% to 27.46% (↓1.64%, not sig., vol: 1.2K)
- **HF-INTL**: 37.70% to 37.03% (↓1.78%, not sig., vol: 1.3K)
- **US-HF**: 26.14% to 25.73% (↓1.59%, not sig., vol: 885.3)
- **RTE**: 45.53% to 48.83% (↑7.26%, not sig., vol: 4.1K)
- **WL**: 34.83% to 35.78% (↑2.72%, not sig., vol: 851.3)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - RTE: TT (↑31%)
  - HF-INTL: LU (↑43%)
[5.0% - 19%]
  - RTE: FJ (↑12%), YE (↓7%), TZ (↑10%)
  - HF-INTL: FR (↓6%), IE (↓13%), NZ (↑10%), DK (↓6%), NO (↓5%)
  - WL: MR (↓7%)

### Overall Summary

Payment Conversion Rate (Checkout) showed mixed performance globally in 2026-W16, with declines in US-HF (-0.41pp), HF-INTL (-0.66pp), and HF-NA (-0.44pp), while WL (+0.97pp) and RTE (+3.33pp) improved significantly. The most significant concern is the fraud service approval rate degradation affecting multiple clusters, particularly US-HF (-1.04pp) and HF-NA (-0.88pp), which warrants immediate investigation into potential fraud rule changes.

### Cluster Highlights

- **US-HF:** PCR declined by -0.41pp (26.24% → 25.83%) driven primarily by a -1.04pp drop in Fraud Service approval rate and Braintree_ApplePay conversion degradation (-2.14pp).
- **HF-INTL:** PCR declined by -0.66pp (37.75% → 37.09%) with Select Payment Method as the primary driver (-1.27pp), showing significant drops in IE, GB, and FR.
- **WL:** PCR improved by +0.97pp (34.86% → 35.83%) driven by Select Payment Method conversion gains (+1.01pp), with CG and GN showing the strongest improvements.
- **HF-NA:** PCR declined by -0.44pp (27.99% → 27.55%) primarily due to Fraud Service approval rate drop (-0.88pp), with US driving the overall decline while CA remained stable.
- **RTE:** PCR improved significantly by +3.33pp (45.59% → 48.92%) driven by Select Payment Method conversion gains (+3.43pp), with FJ and TT contributing the largest positive impacts.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Payment Page Visit to Success (Backend)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 34.58% to 34.74% (↑0.46%, not sig., vol: 1.5K)
- **HF-NA**: 29.59% to 29.18% (↓1.39%, not sig., vol: 1.1K)
- **HF-INTL**: 40.55% to 39.95% (↓1.48%, not sig., vol: 1.4K)
- **US-HF**: 27.68% to 27.36% (↓1.15%, not sig., vol: 680.6)
- **RTE**: 35.56% to 35.97% (↑1.15%, not sig., vol: 1.4K)
- **WL**: 28.80% to 29.52% (↑2.53%, not sig., vol: 1.1K)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - RTE: TT (↑29%)
  - HF-INTL: LU (↑21%)
[5.0% - 19%]
  - HF-INTL: FR (↓5%), IE (↓9%), NZ (↑10%), DK (↓8%), BE (↓5%)
  - WL: MR (↓7%), CK (↑6%), GN (↑6%), AO (↑5%)
  - RTE: YE (↓5%), TV (↓8%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Reactivation Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 90.71% to 90.01% (↓0.77%, not sig., vol: 744.4)
- **HF-NA**: 90.24% to 89.41% (↓0.91%, not sig., vol: 218.6)
- **HF-INTL**: 91.47% to 91.23% (↓0.27%, not sig., vol: 122.3)
- **US-HF**: 90.47% to 90.07% (↓0.44%, not sig., vol: 83.2)
- **RTE**: 90.41% to 89.16% (↓1.39%, not sig., vol: 257.4)
- **WL**: 89.29% to 86.81% (↓2.77%, not sig., vol: 222.3)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-NA: CA (↓3%)
  - WL: CK (↓6%), MR (↓4%), AO (↓4%)
  - RTE: CF (↓4%), YE (↑7%)
  - HF-INTL: CH (↓5%)
**Dimensions:**
[2.5% - 19%]
  - WL: FinalTokenType false (↓3%), PM Credit Card (↓3%), FinalTokenType true (↑3%)
  - RTE: PM Others (↑13%)
**Low Volume (denom < 50):** 5 segments excluded

### Overall Summary

Reactivation Rate declined across most clusters in 2026-W16, with WL experiencing the most significant drop (-2.78pp to 86.81%) and RTE also showing a significant decline (-1.38pp to 89.16%). The most pressing concern is WL's broad-based deterioration, where CK saw all payment methods underperforming and "Expired, Invalid, Closed Card, No Account" decline reasons increased by +3.43pp.

### Cluster Highlights

- **US-HF:** Declined by -0.40pp to 90.07% (not significant), driven by Credit Card rate decline (-1.00%) while PayPal and Apple Pay improved.
- **HF-INTL:** Declined marginally by -0.24pp to 91.23% (not significant), with CH flagged for a -4.69% drop but on insufficient volume (55 orders) to warrant investigation.
- **WL:** Significant decline of -2.78pp to 86.81%, driven by CK (-5.69pp) where all payment methods underperformed and expired/invalid card declines increased substantially.
- **HF-NA:** Declined by -0.92pp to 89.41% (not significant), with CA exceeding threshold at -2.57% due to Credit Card underperformance (-3.05%) and rising fraud-related declines.
- **RTE:** Significant decline of -1.38pp to 89.16%, primarily driven by CF Credit Card dropping -4.67pp and YE volume collapsing -78.2%.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Fraud Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 92.64% to 92.53% (↓0.12%, not sig., vol: 159.0)
- **HF-NA**: 89.71% to 89.82% (↑0.12%, not sig., vol: 33.4)
- **HF-INTL**: 92.13% to 92.06% (↓0.08%, not sig., vol: 37.1)
- **US-HF**: 89.28% to 89.67% (↑0.44%, not sig., vol: 90.2)
- **RTE**: 94.67% to 94.42% (↓0.26%, not sig., vol: 123.9)
- **WL**: 93.28% to 92.95% (↓0.35%, not sig., vol: 49.4)

**Deep Insights**
**Business Units:**
[5.0% - 19%]
  - HF-INTL: LU (↓6%)
**Dimensions:**
[+50%]
  - HF-NA: PM Credit Card (↓100%)
  - WL: PM Credit Card (↑56%)
[5.0% - 19%]
  - HF-NA: CC Referral (↑6%)
**Low Volume (denom < 50):** 3 segments excluded

### Overall Summary

Fraud Approval Rate remained stable globally in 2026-W16, with all five clusters showing non-significant changes ranging from -0.35pp to +0.44pp. The most significant concern across clusters is a systemic Referral channel degradation, with elevated duplicate rates and divergent PF Block behavior driving opposing FAR movements in US (+10.12pp) and CA (-4.31pp) Referral segments.

### Cluster Highlights

- **US-HF:** FAR improved marginally by +0.44pp to 89.67% (not significant), driven by a sharp -58.29% reduction in PF Block rate within the Referral channel that warrants monitoring for potential fraud control degradation.
- **HF-INTL:** FAR stable at 92.06% (-0.08pp), but Referral channel showed consistent FAR declines across all 10 analyzed countries, with LU (-26.96pp) and AT (-11.72pp) most impacted by elevated duplicate blocking.
- **WL:** FAR declined marginally by -0.35pp to 92.95% (not significant), with KN Referral experiencing a sharp -16.91pp FAR drop driven by duplicate rate nearly doubling (+91.81%).
- **HF-NA:** FAR stable at 89.82% (+0.12pp), masking divergent Referral channel trends between US (+10.12pp from reduced PF Block) and CA (-4.31pp from +42.70% PF Block spike).
- **RTE:** FAR stable at 94.42% (-0.26pp), with TT improving +4.60pp while TO declined -3.54pp driven by Referral channel duplicate rate surging +72.88%.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Total Duplicate Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 22.74% to 24.52% (↑7.80%, not sig., vol: 10.4K)
- **HF-NA**: 26.77% to 28.35% (↑5.89%, not sig., vol: 1.6K)
- **HF-INTL**: 31.14% to 33.55% (↑7.75%, not sig., vol: 3.5K)
- **US-HF**: 26.16% to 27.86% (↑6.50%, not sig., vol: 1.3K)
- **RTE**: 14.74% to 15.82% (↑7.33%, not sig., vol: 3.4K)
- **WL**: 15.88% to 17.28% (↑8.80%, not sig., vol: 1.2K)

**Deep Insights**
**Business Units:**
[+50%]
  - RTE: TV (↑75%), TK (↑57%)
[20% - 49%]
  - WL: KN (↑24%)
  - RTE: TT (↓26%), TO (↑47%)
  - HF-INTL: AT (↑28%)
[10.0% - 19%]
  - HF-INTL: DE (↑14%)
  - RTE: CF (↑15%), YE (↑12%), TZ (↑17%)
  - WL: MR (↑20%), GN (↑14%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Total Duplicate Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 5.59% to 6.12% (↑9.34%, not sig., vol: 12.5K)
- **HF-NA**: 6.47% to 7.79% (↑20.31%, not sig., vol: 5.5K)
- **HF-INTL**: 6.76% to 6.93% (↑2.53%, not sig., vol: 1.1K)
- **US-HF**: 6.78% to 8.23% (↑21.34%, not sig., vol: 4.3K)
- **RTE**: 4.16% to 4.61% (↑10.71%, not sig., vol: 5.0K)
- **WL**: 5.01% to 5.31% (↑5.84%, not sig., vol: 828.9)

**Deep Insights**
**Business Units:**
[+50%]
  - RTE: TV (↑87%), TO (↑56%)
  - HF-INTL: CH (↓54%)
[20% - 49%]
  - HF-NA: US (↑21%)
  - HF-INTL: BE (↑28%), IE (↑28%), NZ (↓25%), NO (↓23%), AT (↑29%)
  - WL: KN (↑23%), MR (↑23%)
  - RTE: TT (↓27%), TK (↑34%)
[10.0% - 19%]
  - RTE: FJ (↑10%), YE (↑17%)
  - HF-INTL: FR (↑19%), AU (↓12%)
  - HF-NA: CA (↑15%)
  - WL: ER (↓19%)
**Dimensions:**
[+50%]
  - HF-NA: CC Paid (↑65%)
[20% - 49%]
  - RTE: CC Paid (↑21%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Payment Fraud Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 0.85% to 0.64% (↓24.19%, not sig., vol: 32.3K)
- **HF-NA**: 2.77% to 1.62% (↓41.57%, not sig., vol: 11.3K)
- **HF-INTL**: 0.24% to 0.28% (↑14.99%, not sig., vol: 6.8K)
- **US-HF**: 3.00% to 1.38% (↓54.11%, not sig., vol: 11.0K)
- **RTE**: 0.31% to 0.33% (↑7.55%, not sig., vol: 3.5K)
- **WL**: 0.69% to 0.97% (↑39.06%, not sig., vol: 5.5K)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-NA: US (↓54%)
  - HF-INTL: GB (↑63%), FR (↑51%), NL (↑94%), BE (↑61%), AT (↓100%)
  - WL: GN (↓100%), CG (↑61%), MR (↑53%)
[20% - 49%]
  - HF-INTL: DE (↓30%), IE (↓37%), DK (↓22%), NO (↓21%), LU (↓31%)
  - WL: ER (↑23%), KN (↓23%)
  - RTE: TK (↑21%)
**Dimensions:**
[+50%]
  - HF-INTL: CC Referral (↑85%)
  - RTE: CC Referral (↑97%)
  - HF-NA: CC Referral (↓51%)
[20% - 49%]
  - WL: CC Paid (↑40%)
[10.0% - 19%]
  - HF-NA: CC Paid (↓20%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Payment Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 95.35% to 95.45% (↑0.10%, not sig., vol: 1.9K)
- **HF-NA**: 94.10% to 94.13% (↑0.03%, not sig., vol: 175.7)
- **HF-INTL**: 97.27% to 97.40% (↑0.14%, not sig., vol: 1.1K)
- **US-HF**: 93.76% to 93.82% (↑0.07%, not sig., vol: 303.4)
- **RTE**: 94.87% to 94.81% (↓0.06%, not sig., vol: 255.8)
- **WL**: 91.65% to 91.69% (↑0.04%, not sig., vol: 64.1)

**Deep Insights**
**Dimensions:**
[20% - 49%]
  - WL: CustomerQuality Bad (↓21%)
[2.5% - 19%]
  - HF-INTL: CustomerQuality Bad (↓19%), LL a. 0 (↑3%), PP Unknown (↑3%)
  - RTE: CustomerQuality Bad (↓15%), PP Unknown (↓13%)
  - HF-NA: CustomerQuality Bad (↓8%), LL a. 0 (↑3%)
  - WL: LL a. 0 (↑3%), PP Unknown (↑3%)

### Overall Summary

Payment Approval Rate remained stable globally in 2026-W16, with all five clusters showing non-significant changes ranging from -0.06pp to +0.13pp. No clusters reported material concerns, with all dimensional metrics staying within normal thresholds and "Unknown" PaymentProvider flags affecting only negligible volumes (<1% of orders).

### Cluster Highlights

- **US-HF:** Stable at 93.82% (+0.06pp), continuing an 8-week upward trend with cumulative improvement of +0.66pp since W09, and ProcessOut showed notable gains of +1.87pp on 57,911 orders.
- **HF-INTL:** Improved marginally to 97.4% (+0.13pp), reaching the highest rate in the 8-week trend, with no countries exceeding thresholds and stable mix across all 14 markets.
- **WL:** Stable at 91.69% (+0.04pp), with GN volume growth of +17.8% in the high AR tier contributing positively to rate stability despite minor funnel declines.
- **HF-NA:** Stable at 94.13% (+0.03pp), with effective downstream recovery mechanisms offsetting slight declines in upstream funnel metrics (FirstRunAR -0.26pp).
- **RTE:** Declined marginally to 94.81% (-0.06pp), with the small drop originating at first payment attempt (FirstRunAR -0.28pp) but remaining well within normal 8-week operating range.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## AR Pre Dunning

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 93.26% to 93.24% (↓0.02%, not sig., vol: 311.9)
- **HF-NA**: 92.42% to 92.31% (↓0.12%, not sig., vol: 608.3)
- **HF-INTL**: 94.74% to 94.82% (↑0.08%, not sig., vol: 632.6)
- **US-HF**: 92.22% to 92.10% (↓0.13%, not sig., vol: 568.2)
- **RTE**: 92.83% to 92.65% (↓0.20%, not sig., vol: 862.0)
- **WL**: 90.10% to 90.02% (↓0.09%, not sig., vol: 140.1)

**Deep Insights**
**Dimensions:**
[20% - 49%]
  - WL: CustomerQuality Bad (↓21%)
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↓15%), LL a. 0 (↑3%)
  - HF-INTL: CustomerQuality Bad (↓20%), LL a. 0 (↑3%), PP Unknown (↑4%)
  - RTE: CustomerQuality Bad (↓15%), PP Unknown (↓13%)
  - WL: LL a. 0 (↑3%), PP Unknown (↑3%)

### Overall Summary

Acceptance Rate (Overall) remained stable across all clusters in 2026-W16, with minor non-significant declines ranging from -0.09pp to -0.19pp except for HF-INTL which improved marginally by +0.08pp. No clusters exhibited statistically significant changes or breached alert thresholds, with all flagged anomalies occurring in low-volume dimensions (Unknown PaymentProvider) having minimal impact on overall performance.

### Cluster Highlights

- **US-HF:** Declined by -0.13pp to 92.1% (not significant), with First Run AR showing the largest funnel pressure at -0.31pp while all major payment methods remained within tolerance.
- **HF-INTL:** Improved marginally by +0.08pp to 94.82% across 804,152 orders, with NO showing the largest country decline at -2.03pp but remaining below the ±2.5% threshold.
- **WL:** Declined by -0.09pp to 90.02% (not significant), continuing an overall positive 8-week trend from 88.19% with stable performance across all dimensions.
- **HF-NA:** Declined by -0.12pp to 92.31% (not significant), driven primarily by Credit Card payment method at -0.21pp while US and CA remained stable with offsetting movements.
- **RTE:** Declined by -0.19pp to 92.65% (not significant), with all major payment providers showing minimal movement and no countries exceeding alert thresholds.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Acceptance LL0 (Initial Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 91.27% to 91.35% (↑0.09%, not sig., vol: 89.5)
- **HF-NA**: 89.80% to 89.31% (↓0.55%, not sig., vol: 99.3)
- **HF-INTL**: 91.78% to 91.42% (↓0.39%, not sig., vol: 135.8)
- **US-HF**: 89.37% to 88.70% (↓0.75%, not sig., vol: 93.6)
- **RTE**: 91.68% to 92.47% (↑0.86%, not sig., vol: 273.9)
- **WL**: 91.05% to 91.28% (↑0.26%, not sig., vol: 33.9)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: NZ (↓11%), AU (↑3%), NL (↓3%), SE (↑3%), LU (↓5%)
  - WL: CK (↓4%), GN (↑4%), AO (↑3%)
  - RTE: YE (↑3%), TO (↑5%), TV (↑5%)
**Dimensions:**
[2.5% - 19%]
  - RTE: PP Unknown (↓12%)
  - HF-NA: PP Adyen (↓4%)

### Overall Summary

Acceptance Rate (Initial Charges) remained stable across all clusters in 2026-W16, with changes ranging from -0.55pp to +0.86pp, none of which were statistically significant. The most notable finding was NZ in HF-INTL experiencing a -10.84% decline driven by a +7.48pp increase in Insufficient Funds declines amid a volume surge of +113%.

### Cluster Highlights

- **US-HF:** Declined by -0.67pp to 88.7%, a non-significant change with uniform decreases across all payment methods and no actionable anomalies identified.
- **HF-INTL:** Declined by -0.39pp to 91.42%, with NZ flagged for a -10.84% drop driven by elevated Insufficient Funds (+7.48pp) on doubled volume.
- **WL:** Improved slightly by +0.23pp to 91.28%, with CK declining -4.01% due to Adyen/credit_card "Other reasons" increases (+3.84pp) offsetting gains elsewhere.
- **HF-NA:** Declined by -0.55pp to 89.31%, a non-significant systemic decrease across the full payment funnel with no country or dimension exceeding thresholds.
- **RTE:** Improved by +0.86pp to 92.47%, with all three flagged countries (YE, TV, TO) showing AR improvements driven by reduced Insufficient Funds declines.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Acceptance LL0 and LL1+ (Recurring Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 93.35% to 93.34% (↓0.01%, not sig., vol: 201.8)
- **HF-NA**: 92.50% to 92.42% (↓0.09%, not sig., vol: 466.8)
- **HF-INTL**: 94.86% to 94.97% (↑0.12%, not sig., vol: 937.1)
- **US-HF**: 92.30% to 92.20% (↓0.11%, not sig., vol: 441.4)
- **RTE**: 92.92% to 92.66% (↓0.28%, not sig., vol: 1.1K)
- **WL**: 90.03% to 89.92% (↓0.12%, not sig., vol: 187.5)

**Deep Insights**
**Dimensions:**
[20% - 49%]
  - WL: CustomerQuality Bad (↓21%)
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↓15%), PP Unknown (↑8%)
  - HF-INTL: CustomerQuality Bad (↓20%), PP Unknown (↑16%)
  - RTE: CustomerQuality Bad (↓15%)
**Low Volume (denom < 50):** 2 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Ship Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 51.48% to 52.49% (↑1.96%, not sig., vol: 1.5K)
- **HF-NA**: 48.19% to 48.03% (↓0.32%, not sig., vol: 58.8)
- **HF-INTL**: 65.58% to 66.73% (↑1.75%, not sig., vol: 530.9)
- **US-HF**: 46.72% to 47.61% (↑1.91%, not sig., vol: 269.0)
- **RTE**: 42.61% to 43.82% (↑2.85%, not sig., vol: 587.1)
- **WL**: 31.07% to 31.81% (↑2.37%, not sig., vol: 197.3)

**Deep Insights**
**Business Units:**
[+50%]
  - WL: MR (↓53%)
  - RTE: TV (↑110%)
[20% - 49%]
  - WL: GN (↑27%)
[10.0% - 19%]
  - HF-INTL: NZ (↓13%)
  - RTE: TZ (↑12%), TK (↓12%)

### Overall Summary

Dunning Recovery Rate improved across most clusters in 2026-W16, with gains ranging from +0.74pp to +1.21pp driven by the Pre-Payday to Payday phase transition. The most significant concern is CA in HF-NA, which declined -6.7% despite favorable Payday timing, and NZ in HF-INTL, which dropped -13.3% counter to cluster trends.

### Cluster Highlights

- **US-HF:** Ship Rate improved by +0.89pp (46.72% → 47.61%) driven by Payday phase timing, despite a +6.6% increase in Discount % that was offset by improved customer liquidity.
- **HF-INTL:** Ship Rate improved by +1.15pp (65.58% → 66.73%) led by AU (+7.0%) and NO (+7.3%) benefiting from reduced discounting, though NZ declined -13.3% requiring investigation.
- **WL:** Ship Rate improved by +0.74pp (31.07% → 31.81%) with GN (+27.4%) and AO (+6.4%) driving gains, partially offset by CK declining -6.6% due to a +14.9% spike in Discount %.
- **HF-NA:** Ship Rate declined marginally by -0.16pp (48.19% → 48.03%) as CA's sharp -6.7% drop offset US gains of +1.9%, with CA's increased Discount % (+3.4%) indicating unfavorable order mix.
- **RTE:** Ship Rate improved by +1.21pp (42.61% → 43.82%) driven by Payday effects and reduced discounting (-4.1%), with FJ (+3.7%) and YE (+4.2%) as primary contributors while TK declined -11.7% despite an 84% volume surge.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Recovery W0

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 41.77% to 44.27% (↑5.99%, not sig., vol: 2.4K)
- **HF-NA**: 37.82% to 40.17% (↑6.20%, not sig., vol: 540.3)
- **HF-INTL**: 42.74% to 45.50% (↑6.46%, not sig., vol: 1.3K)
- **US-HF**: 41.49% to 42.25% (↑1.81%, not sig., vol: 121.7)
- **RTE**: 44.06% to 46.12% (↑4.67%, not sig., vol: 421.6)
- **WL**: 39.53% to 42.03% (↑6.31%, not sig., vol: 166.9)

**Deep Insights**
**Business Units:**
[+50%]
  - RTE: TO (↑94%)
  - HF-INTL: CH (↓56%)
[20% - 49%]
  - HF-INTL: FR (↓26%), NO (↑32%), SE (↑33%)
  - HF-NA: CA (↑22%)
[10.0% - 19%]
  - HF-INTL: GB (↑15%), DE (↑14%)
  - WL: CK (↑19%), GN (↑16%), KN (↓18%)
  - RTE: CF (↑17%)
**Low Volume (denom < 50):** 3 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Recovery W12

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 85.11% to 85.77% (↑0.77%, not sig., vol: 334.2)
- **HF-NA**: 81.01% to 80.56% (↓0.56%, not sig., vol: 55.3)
- **HF-INTL**: 87.99% to 88.94% (↑1.08%, not sig., vol: 236.2)
- **US-HF**: 81.07% to 80.97% (↓0.11%, not sig., vol: 8.1)
- **RTE**: 84.01% to 84.61% (↑0.72%, not sig., vol: 61.2)
- **WL**: 81.81% to 82.74% (↑1.15%, not sig., vol: 32.7)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - RTE: TV (↑33%)
[10.0% - 19%]
  - WL: GN (↑11%)
  - HF-INTL: ES (↑11%)
**Low Volume (denom < 50):** 1 segment excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Dunning Profit

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: €9.87 to €10.18 (↑3.10%, not sig., vol: 2.4K)
- **HF-NA**: €11.39 to €11.37 (↓0.17%, not sig., vol: 33.0)
- **HF-INTL**: €9.67 to €10.54 (↑8.96%, not sig., vol: 3.0K)
- **US-HF**: €11.65 to €11.29 (↓3.11%, not sig., vol: 453.2)
- **RTE**: €10.25 to €10.15 (↓0.99%, not sig., vol: 180.7)
- **WL**: €5.51 to €5.22 (↓5.17%, not sig., vol: 362.3)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: GB (↑60%), ES (↑452%)
  - WL: GN (↑55%)
[20% - 49%]
  - HF-INTL: NZ (↑23%), AT (↓32%), LU (↑39%)
[10.0% - 19%]
  - HF-INTL: AU (↓12%), SE (↑15%), IE (↑13%), NL (↑12%)
  - RTE: YE (↓18%)
  - HF-NA: CA (↑10%)
  - WL: ER (↓11%), CK (↓16%), CG (↓15%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---
