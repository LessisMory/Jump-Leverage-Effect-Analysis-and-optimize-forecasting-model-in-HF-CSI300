# ===============================
# Module 8: Dataset construction and baseline regressions
# ===============================

data_sum = pd.merge(inv_date_VS, inv_date_VIX, on='TradingDate')
data_sum = pd.merge(data_sum, inv_date_LQ, on='TradingDate')

data_sum.rename(
    columns={
        'T_1_x': 'spot_vs',
        'T_2_x': 'short_vs',
        'T_3_x': 'long_vs',
        'T_1_y': 'spot_vix',
        'T_2_y': 'short_vix',
        'T_3_y': 'long_vix'
    },
    inplace=True
)

merged_df = pd.merge(data_sum, df_rv, on='TradingDate', how='left')
merged_df = pd.merge(merged_df, df_rt, on='TradingDate', how='left')
merged_df = pd.merge(merged_df, df_rl, on='TradingDate', how='left')

merged_df_1 = merged_df.dropna()
