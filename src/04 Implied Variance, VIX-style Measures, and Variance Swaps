sh300 = sh300.groupby(['TradingDate', 'T-t'], group_keys=False).apply(Moneyness)

# Retain only out-of-the-money options
sh300 = sh300[sh300['Moneyness'] == 'OTM']
sh300 = sh300[['Spot', 'TradingDate', 'K', 'ClosePrice', 'T-t']]
sh300 = sh300[~(sh300['T-t'] < 3 / 365)]

date = sh300['TradingDate'].unique()
n = len(date)

# Temporary containers for VIX-like and variance swap measures
VIX_temp = pd.DataFrame(index=range(3 * len(date)), columns=['VIX'])
ttm_temp = pd.DataFrame(index=range(3 * len(date)), columns=['Time to Maturity'])
VS_temp = pd.DataFrame(index=range(n), columns=['VS'])

grouped_time = sh300.groupby('TradingDate')
grouped_ttm = sh300.groupby(['TradingDate', 'T-t'])

# Compute VIX-style variance and variance swap measures
index = 0
for day in date:
    group_date = grouped_time.get_group(day)
    unique_ttm = group_date['T-t'].unique()
    min_three_ttm = unique_ttm[:3]

    for t in min_three_ttm:
        specific_dat = grouped_ttm.get_group((day, t))
        specific_dat = specific_dat.sort_values(by='K')

        vix = np.sum(
            np.diff(specific_dat['K'][:]) *
            specific_dat['ClosePrice'][1:] /
            specific_dat['K'][1:] ** 2
        )

        vs = np.sum(
            (1 - np.log(
                specific_dat['K'][1:] /
                (specific_dat['Spot'][1:] * 1000)
            )) *
            np.diff(specific_dat['K'][:]) *
            specific_dat['ClosePrice'][1:] /
            specific_dat['K'][1:] ** 2
        )

        vix *= 2 / t
        vs *= 2 / t
        vs = vs - t * vix ** 2 / 4

        VIX_temp.loc[index] = vix
        ttm_temp.loc[index] = t
        VS_temp.loc[index] = vs

        index += 1


# Reshape VIX estimates into maturity buckets
n = len(VIX_temp) // 3
vix_data = []

for i in range(n):
    group_data = VIX_temp['VIX'][i * 3:(i + 1) * 3].values
    vix_data.append(group_data)

VIX = pd.DataFrame(vix_data, columns=['T_1', 'T_2', 'T_3'])

# Reshape time-to-maturity data
n = len(ttm_temp) // 3
ttm_data = []

for i in range(n):
    group_data = ttm_temp['Time to Maturity'][i * 3:(i + 1) * 3].values
    ttm_data.append(group_data)

TTM = pd.DataFrame(ttm_data, columns=['T_1', 'T_2', 'T_3'])

# Reshape variance swap estimates
n = len(VS_temp) // 3
vs_data = []

for i in range(n):
    group_data = VS_temp['VS'][i * 3:(i + 1) * 3].values
    vs_data.append(group_data)

VS = pd.DataFrame(vs_data, columns=['T_1', 'T_2', 'T_3'])

date_df = pd.DataFrame({'TradingDate': date})
inv_date_VS = pd.concat([date_df, VS], axis=1)
inv_date_VIX = pd.concat([date_df, VIX], axis=1)
