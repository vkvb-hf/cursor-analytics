# Payment Conversion Rate (Checkout) - Overall Summary

**Week:** 2026-W20  
**Generated:** 2026-05-19 14:44  
**Clusters:** HF-INTL, HF-NA, RTE, US-HF, WL

---

### Overall Summary

Payment Conversion Rate (Checkout) showed mixed performance across clusters in 2026-W20, with declines in US-HF (-0.07pp) and HF-INTL (-0.85pp) offset by improvements in RTE (+0.70pp) and HF-NA (+0.11pp). The most critical concern is Braintree_ApplePay degradation, which experienced severe success rate declines across multiple clusters (US-HF: -8.74pp, HF-INTL: -12.77pp, HF-NA: -9.19pp), requiring immediate investigation.

### Cluster Highlights

- **US-HF:** PCR declined by -0.07pp to 23.88%, driven primarily by Braintree_ApplePay success rate dropping -8.74pp (74.41% → 65.67%) despite representing ~35% of payment attempts.
- **HF-INTL:** PCR declined by -0.85pp to 35.47%, with Braintree_ApplePay experiencing the largest degradation (-12.77pp to 72.41%) combined with fraud service approval issues in NZ (-2.69pp).
- **WL:** PCR remained stable at 29.38% (+0.05pp), with FE Validation recovery rate declining -2.66pp as APPLEPAY_DISMISSED errors increased, though offset by early-funnel gains.
- **HF-NA:** PCR improved by +0.11pp to 25.93%, driven by CA gains (+1.02pp) that offset US decline (-0.07pp), despite Braintree_ApplePay success rate falling -9.19pp.
- **RTE:** PCR improved by +0.70pp to 39.29%, driven by early-funnel gains in Select Payment Method (+0.83pp) and Click Submit Form (+0.44pp), with TV contributing +3.88pp improvement.

---

*Auto-generated from 5 cluster reports.*
