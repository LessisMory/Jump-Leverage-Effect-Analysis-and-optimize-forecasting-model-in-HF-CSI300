# ===============================
# Module 6: Leverage quantity (LQ) construction
# ===============================

slope_sum = pd.merge(
    slope_vs_inv_date, slope_vix_inv_date, on='TradingDate'
)

LQ = np.zeros(len(slope_sum))
for i in range(len(slope_sum)):
    LQ[i] = -2 * (slope_sum.slope_vs[i] - slope_sum.slope_vix[i])

LQ_df = pd.DataFrame({'LQ': LQ})
inv_date_LQ = pd.concat([date_df, LQ_df], axis=1)

# Drop rows with missing values
inf_rows_index_lq = inv_date_LQ.index[inv_date_LQ.isnull().any(axis=1)]
inv_date_LQ = inv_date_LQ.drop(inf_rows_index_lq)
