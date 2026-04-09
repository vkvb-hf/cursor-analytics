# Payment Conversion Rate (Checkout) - Overall Summary

**Week:** 2026-W14  
**Generated:** 2026-04-09 09:53  
**Clusters:** HF-INTL, HF-NA, RTE, US-HF, WL

---

### Overall Summary

Payment Conversion Rate (Checkout) performance was mixed across clusters in 2026-W14, with HF-INTL (+1.16pp) and RTE (+1.55pp) showing strong improvements while US-HF (-0.37pp), WL (-0.15pp), and HF-NA (-0.68pp) experienced declines. The most significant concern is the severe backend degradation at the PVS Attempt step in WL (-9.71pp), combined with persistent FE Validation issues across multiple clusters driven by "terms_not_accepted" and "APPLEPAY_DISMISSED" errors.

### Cluster Highlights

- **US-HF:** PCR declined by -0.37pp to 26.41%, primarily driven by top-of-funnel drop at Select Payment Method (-0.42pp) and FE Validation degradation (-0.41pp), partially offset by improved fraud approval (+2.75pp) and ProcessOut_CreditCard success rates (+3.21pp).
- **HF-INTL:** PCR improved by +1.16pp to 36.04%, driven by France's strong performance (+3.10pp) and gains in Select Payment Method conversion (+0.42pp) combined with improved Braintree_ApplePay success rates (+1.70pp).
- **WL:** PCR declined by -0.15pp to 29.88%, with a critical backend issue at PVS Attempt (-9.71pp) and KN country driving the decline (-3.75pp) due to deteriorating fraud approval rates.
- **HF-NA:** PCR declined by -0.68pp to 27.96%, primarily caused by FE Validation degradation (-0.68pp) concentrated in Canada (-1.77pp overall), with APPLEPAY_DISMISSED errors increasing to 56.9% of error share.
- **RTE:** PCR improved by +1.55pp to 39.36%, driven by strong top-of-funnel gains in Select Payment Method (+1.75pp) and Click Submit Form (+0.90pp), with FJ contributing the majority of improvement (+2.51pp on 64% of volume).

---

*Auto-generated from 5 cluster reports.*
