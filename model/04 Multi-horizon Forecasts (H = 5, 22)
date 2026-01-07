# H = 5 days ahead
y_H5 = pred_rv['RV_D'].shift(-5).dropna()

X_base_H5 = add_constant(pred_rv[['RV_D', 'RV_W', 'RV_M', 'J_D']][:-5])
X_plus_H5 = X_base_H5.copy()
X_plus_H5['leverage factor'] = pred_rv['leverage factor'][:-5]

model_base_H5 = OLS(y_H5, X_base_H5).fit()
model_plus_H5 = OLS(y_H5, X_plus_H5).fit()

print("HAR-CJ Model Summary (H=5):")
print(model_base_H5.summary())
print(model_plus_H5.summary())


# H = 22 days ahead
y_H22 = pred_rv['RV_D'].shift(-22).dropna()

X_base_H22 = add_constant(pred_rv[['RV_D', 'RV_W', 'RV_M', 'J_D']][:-22])
X_plus_H22 = X_base_H22.copy()
X_plus_H22['leverage factor'] = pred_rv['leverage factor'][:-22]

model_base_H22 = OLS(y_H22, X_base_H22).fit()
model_plus_H22 = OLS(y_H22, X_plus_H22).fit()

print("HAR-CJ Model Summary (H=22):")
print(model_base_H22.summary())
print(model_plus_H22.summary())
