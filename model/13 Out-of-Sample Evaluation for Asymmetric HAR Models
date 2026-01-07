from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

predict_sample = merged_df_2.copy()
predict_sample['y'] = merged_df_2['RV'].shift(-1).dropna()
predict_sample = predict_sample[:-1]

features_base = predict_sample[
    ['pos_var', 'pos_var_W', 'pos_var_M',
     'neg_var', 'neg_var_W', 'neg_var_M']
]

features_plus = predict_sample[
    ['pos_var', 'pos_var_W', 'pos_var_M',
     'neg_var', 'neg_var_W', 'neg_var_M', 'LQ']
]

target = predict_sample['y']

X_train_base, X_test_base, y_train_base, y_test_base = train_test_split(
    features_base, target, test_size=0.2, random_state=42
)

X_train_plus, X_test_plus, y_train_plus, y_test_plus = train_test_split(
    features_plus, target, test_size=0.2, random_state=42
)

model_base = LinearRegression().fit(X_train_base, y_train_base)
model_plus = LinearRegression().fit(X_train_plus, y_train_plus)

pred_base = model_base.predict(X_test_base)
pred_plus = model_plus.predict(X_test_plus)

print(f"Asymmetric HAR Base R²: {r2_score(y_test_base, pred_base):.3f}")
print(f"Asymmetric HAR Plus R²: {r2_score(y_test_plus, pred_plus):.3f}")
