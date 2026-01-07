def QLIKE(y_true, y_pred):
    y_pred = np.maximum(y_pred, 1e-8)
    return np.mean(np.log(y_pred) + y_true / y_pred)

def RLOG(y_true, y_pred):
    y_pred = np.maximum(y_pred, 1e-8)
    return np.mean((y_true / y_pred) ** 2)

print(f"QLIKE (Base): {QLIKE(y_test_base, pred_base):.4f}")
print(f"QLIKE (Plus): {QLIKE(y_test_plus, pred_plus):.4f}")

print(f"RLOG (Base): {RLOG(y_test_base, pred_base):.4f}")
print(f"RLOG (Plus): {RLOG(y_test_plus, pred_plus):.4f}")
