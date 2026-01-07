# ===============================
# Module 2: Realized volatility and jump construction
# ===============================

import math

grouped_day = spot_300_org.groupby('date')

RV = pd.DataFrame(index=range(len(trade_date_sgn)), columns=['RV'])
BV = pd.DataFrame(index=range(len(trade_date_sgn)), columns=['BV'])
RT = pd.DataFrame(index=range(len(trade_date_sgn)), columns=['RT'])

index = 0

for day in trade_date_sgn:
    group1 = grouped_day.get_group(day)
    num = len(group1)

    RV_diff_values = []   # Squared intraday returns
    BV_diff_values = []   # Bipower variation components
    RT_values = []        # Intraday returns

    for i in range(num - 2):
        group1 = group1.sort_values(by='time').reset_index(drop=True)

        # Realized variance contribution
        RV_diff_values.append((group1.close[i + 1] - group1.close[i]) ** 2)

        # Bipower variation term (jump-robust)
        BV_diff_values.append(
            (group1.close[i + 1] - group1.close[i]) *
            (group1.close[i + 2] - group1.close[i + 1])
        )

        # Realized return
        RT_values.append(group1.close[i + 1] - group1.close[i])

    RV.loc[index] = np.sum(RV_diff_values)
    RT.loc[index] = np.sum(RT_values)
    BV.loc[index] = np.sum(np.abs(BV_diff_values)) * math.pi / 2

    index += 1

# Construct daily realized volatility and jump components
date_df = pd.DataFrame({'TradingDate': trade_date_sgn})

RV['RV'] = RV['RV'].astype(float)
RV['J'] = RV['RV'] - BV['BV']       # Jump component
RV['RV'] = np.sqrt(RV['RV'])         # Realized volatility

df_rv = pd.concat([date_df, RV[['RV', 'J']]], axis=1)
df_rt = pd.concat([date_df, RT[['RT']]], axis=1)
