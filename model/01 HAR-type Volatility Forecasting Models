# -------------------------------
# HAR-RV model (baseline vs. leverage-augmented)
# -------------------------------

y = pred_rv['RV_D'].shift(-1).dropna()

X_base = add_constant(pred_rv[['RV_D', 'RV_W', 'RV_M']][:-1])
X_plus = X_base.copy()

# Add leverage factor to the augmented model
X_plus['leverage factor'] = pred_rv['leverage factor'][:-1]

# Fit HAR-RV models
model_base = OLS(y, X_base).fit()
model_plus = OLS(y, X_plus).fit()

print("Base HAR-RV Model Summary:")
print(model_base.summary())

print("\nLeverage-Augmented HAR-RV Model Summary:")
print(model_plus.summary())
