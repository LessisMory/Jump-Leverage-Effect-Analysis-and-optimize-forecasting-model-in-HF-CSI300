from statsmodels.stats.outliers_influence import variance_inflation_factor

vif_data = pd.DataFrame()
vif_data['feature'] = X_plus.columns
vif_data['VIF'] = [
    variance_inflation_factor(X_plus.values, i)
    for i in range(len(X_plus.columns))
]

print(vif_data)
