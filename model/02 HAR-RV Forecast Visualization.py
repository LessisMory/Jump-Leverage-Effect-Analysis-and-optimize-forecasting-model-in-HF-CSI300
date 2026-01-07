predictions_base = model_base.predict(X_base)
predictions_plus = model_plus.predict(X_plus)

plt.figure(figsize=(12, 6))

# Actual realized volatility
plt.plot(
    pred_rv['RV_D'].reset_index(drop=True),
    label='Actual RV_D',
    color='blue',
    linestyle='-',
    alpha=0.75
)

# HAR-RV forecasts
plt.plot(predictions_base, label='HAR-RV (Base)', color='red', linestyle='--', alpha=0.75)
plt.plot(predictions_plus, label='HAR-RV (Plus)', color='green', linestyle='-.', alpha=0.75)

plt.legend()
plt.title('Actual vs Predicted Daily Realized Volatility')
plt.xlabel('Observation')
plt.ylabel('RV_D')
plt.show()
