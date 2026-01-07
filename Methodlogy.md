# Methodology

This project follows a modular volatility decomposition and forecasting framework
built upon high-frequency financial data and option-implied information.

---

## 1. Realized Volatility Decomposition

Intraday log-returns are constructed from high-frequency prices. Daily realized
volatility (RV) is computed as the sum of squared intraday returns.

To isolate jump components, bipower variation (BV) is used as a consistent estimator
of the continuous sample-path variation. Jump variation (J) is defined as:

    J_t = RV_t - BV_t

This decomposition allows separate modeling of continuous and discontinuous
volatility components.

---

## 2. Option-Implied Variance Measures

Using cross-sectional option prices, variance swap (VS) and VIX-type implied
variance measures are constructed for multiple maturities.

Out-of-the-money options are selected to ensure robustness, and numerical
integration over strike prices is applied following standard variance swap
replication methods.

---

## 3. Leverage Factor Construction

For each trading day, term structures of implied variance and variance swap rates
are regressed on time-to-maturity polynomials.

The slope differentials between variance swap and implied variance curves define
a leverage-related factor (LQ), capturing asymmetric volatility response and
downside risk pricing.

---

## 4. Extended HAR Models

The baseline HAR-RV model is specified as:

    RV_{t+1} = β₀ + β₁ RV_t + β₂ RV_t^{(W)} + β₃ RV_t^{(M)} + ε_{t+1}

The framework is extended along several dimensions:

- HAR-CJ: inclusion of jump components
- HAR-Q: inclusion of realized quarticity
- HAR-RSV: decomposition into positive and negative semivariances
- HAR-RSV-LQ: leverage factor augmentation
- HAR-RSV-SV: stochastic volatility extracted from GARCH filtering

All models are estimated using OLS with robust inference.

---

## 5. Evaluation and Diagnostics

Model performance is evaluated using:

- In-sample statistical significance
- Out-of-sample forecasting accuracy (MSE, R²)
- Loss functions (QLIKE, RLOG)
- Correlation and rank-based dependence measures
- Residual diagnostics and multicollinearity checks

Economic relevance is assessed through utility-based measures and risk metrics
such as Value-at-Risk (VaR).

---

## 6. Summary

This methodology provides a unified and extensible framework for volatility
forecasting that jointly accounts for persistence, jumps, asymmetry, leverage,
and option-implied expectations.
