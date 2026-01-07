# Reset indices and rename date column
pos_var = pos_var.reset_index().rename(columns={'index': 'TradingDate'})
neg_var = neg_var.reset_index().rename(columns={'index': 'TradingDate'})

# Construct weekly and monthly averages
pos_var['pos_var_W'] = pos_var['pos_var'].rolling(window=5, min_periods=1).mean()
pos_var['pos_var_M'] = pos_var['pos_var'].rolling(window=22, min_periods=1).mean()

neg_var['neg_var_W'] = neg_var['neg_var'].rolling(window=5, min_periods=1).mean()
neg_var['neg_var_M'] = neg_var['neg_var'].rolling(window=22, min_periods=1).mean()

pos_var['pos_var'] = pos_var['pos_var'].astype(float)
neg_var['neg_var'] = neg_var['neg_var'].astype(float)

# Merge semivariance measures into main dataset
merged_df = pd.merge(pos_var, neg_var, on='TradingDate', how='left')
merged_df_2 = pd.merge(merged_df_1, merged_df, on='TradingDate', how='left')

# Define forecasting target
y = merged_df_2['RV'].shift(-1).dropna()

# Baseline asymmetric HAR regressors
X_base = add_constant(
    merged_df_2[
        ['pos_var', 'pos_var_W', 'pos_var_M',
         'neg_var', 'neg_var_W', 'neg_var_M']
    ][:-1]
)

# Leverage-augmented asymmetric HAR regressors
X_plus = X_base.copy()
X_plus['leverage factor'] = merged_df_2['LQ'][:-1]

# Fit asymmetric HAR-RSV models
model_base = OLS(y, X_base).fit()
model_plus = OLS(y, X_plus).fit()

print("Base Asymmetric HAR-RSV Model Summary:")
print(model_base.summary())

print("\nLeverage-Augmented Asymmetric HAR-RSV Model Summary:")
print(model_plus.summary())
