# ===============================
# Module 7: Realized leverage (RL) construction
# ===============================

spot_vix_inv_date_org = spot_vix_inv_date[:812].copy()
spot_vix_inv_date_org = spot_vix_inv_date_org.reset_index(drop=True)

df_rt = df_rt.reset_index(drop=True)
numm = len(df_rt)

RL = np.zeros(numm - 1)
for i in range(numm - 1):
    RL[i] = (
        252
        * (spot_vix_inv_date_org.spot_vix[i + 1] - spot_vix_inv_date_org.spot_vix[i])
        * df_rt.loc[i, 'RT']
    )

df_rl = pd.concat(
    [date_df, pd.DataFrame(RL, columns=['RL'])], axis=1
)
