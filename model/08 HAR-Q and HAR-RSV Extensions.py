# ------------------------------------------------------------
# HAR-Q Model: Quarticity-augmented HAR specification
# ------------------------------------------------------------

# Define one-step-ahead forecasting target
y = pred_rv['RV_D'].shift(-1).dropna()

# Baseline HAR-Q regressors
X_base = add_constant(
    pred_rv[['RV_D', 'RV_W', 'RV_M', 'RQ']][:-1]
)

# Leverage-augmented HAR-Q regressors
X_plus = X_base.copy()
X_plus['leverage factor'] = pred_rv['leverage factor'][:-1]

# Fit HAR-Q models
model_base = OLS(y, X_base).fit()
model_plus = OLS(y, X_plus).fit()

print("Base HAR-Q Model Summary:")
print(model_base.summary())

print("\nLeverage-Augmented HAR-Q Model Summary:")
print(model_plus.summary())
