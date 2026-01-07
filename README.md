# Jump–Leverage Effect Analysis and Volatility Forecasting  
## High-Frequency Evidence from the CSI 300 Index

This repository studies volatility dynamics and forecasting performance by
explicitly modeling jump–leverage effects using high-frequency financial data.

The empirical framework decomposes realized volatility into continuous,
jump, and asymmetric components, and integrates option-implied information
to capture instantaneous variance and skewness-driven risk asymmetry.

The analysis provides evidence that leverage-related higher-order moments,
closely linked to conditional skewness, significantly enhance volatility
forecasting accuracy.

---

## Research Focus

This project investigates three tightly connected objects:

- **Instantaneous variance**, extracted from high-frequency returns and
  option-implied variance measures
- **Jump variation**, capturing discontinuous price movements
- **Leverage effects**, interpreted as asymmetric responses driven by
  higher-order (third-moment) return dynamics

Together, these components form a unified jump–leverage mechanism that
improves volatility prediction beyond standard HAR-type models.

---

## Methodological Highlights

- Realized volatility decomposition using high-frequency intraday returns
- Jump identification via bipower variation
- Construction of option-implied variance and variance swap measures
- Extraction of a leverage-related factor from term-structure regressions
- Extended HAR models incorporating:
  - Jump variation
  - Quarticity
  - Stochastic volatility
  - Positive and negative realized semivariance
  - Leverage-based asymmetry

---

## Models Implemented

- HAR-RV
- HAR-CJ (continuous + jump)
- HAR-Q (quarticity-augmented)
- HAR-RSV (asymmetric semivariance)
- HAR-RSV-LQ (leverage-augmented)
- HAR-RSV-SV (stochastic volatility filtered)

Both in-sample inference and out-of-sample forecasting performance are evaluated.

---

## Evaluation

Model performance is assessed using:

- Mean squared error (MSE) and R²
- QLIKE and RLOG loss functions
- Rank-based dependence measures
- Residual diagnostics and multicollinearity analysis
- Economic criteria including utility-based evaluation and Value-at-Risk

---

## Technical Stack

- Python
- NumPy, Pandas
- Statsmodels
- ARCH
- Scikit-learn
- Matplotlib / Seaborn

---

## Data Availability

Due to licensing and privacy restrictions, raw data are not included.
All file paths and identifiers have been anonymized.

---
