from arch import arch_model

# Estimate conditional volatility using GARCH(1,1)
garch11 = arch_model(pred_rv['RV_D'], vol='Garch', p=1, q=1)
res = garch11.fit(update_freq=5, disp='off')

# Store estimated stochastic volatility
pred_rv['SV'] = res.conditional_volatility
pred_rv.dropna(inplace=True)

# Define forecasting target
y = pred_rv['RV_D'].shift(-1).dropna()

# Baseline HAR-RSV regressors
X_base = add_constant(
    pred_rv[['RV_D', 'RV_W', 'RV_M', 'SV']][:-1]
)

# Leverage-augmented HAR-RSV regressors
X_plus = X_base.copy()
X_plus['leverage factor'] = pred_rv['leverage factor'][:-1]

# Fit HAR-RSV models
model_base = OLS(y, X_base).fit()
model_plus = OLS(y, X_plus).fit()

print("Base HAR-RSV Model Summary:")
print(model_base.summary())

print("\nLeverage-Augmented HAR-RSV Model Summary:")
print(model_plus.summary())
