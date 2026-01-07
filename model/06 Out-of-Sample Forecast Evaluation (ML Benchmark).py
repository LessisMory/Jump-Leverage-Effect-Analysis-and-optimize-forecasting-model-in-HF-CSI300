from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

predict_sample = pred_rv.copy()
predict_sample['y'] = predict_sample['RV_D'].shift(-1).dropna()
predict_sample = predict_sample[:-1]

features_base = predict_sample[['RV_D', 'RV_W', 'RV_M']]
features_plus = predict_sample[['RV_D', 'RV_W', 'RV_M', 'leverage factor']]
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

print(f"Base model R²: {r2_score(y_test_base, pred_base):.3f}")
print(f"Plus model R²: {r2_score(y_test_plus, pred_plus):.3f}")
