# ===============================
# Module 9: Predictive regressions and statistical diagnostics
# ===============================

# Simple daily regression of returns on leverage quantity
day_model2 = sm.OLS(
    merged_df_1['RT'].astype(float),
    merged_df_1['LQ']
)
results2 = day_model2.fit()
print(results2.summary())
