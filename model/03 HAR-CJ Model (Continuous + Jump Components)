pred_rv.dropna(inplace=True)

y = pred_rv['RV_D'].shift(-1).dropna()

X_base = add_constant(
    pred_rv[['RV_D', 'RV_W', 'RV_M', 'J_D', 'J_W', 'J_M']][:-1]
)

X_plus = X_base.copy()
X_plus['leverage factor'] = pred_rv['leverage factor'][:-1]

model_base = OLS(y, X_base).fit()
model_plus = OLS(y, X_plus).fit()

print("Base HAR-CJ Model Summary:")
print(model_base.summary())

print("\nLeverage-Augmented HAR-CJ Model Summary:")
print(model_plus.summary())
