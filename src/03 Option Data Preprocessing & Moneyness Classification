# ===============================
# Module 3: Option data preprocessing and moneyness classification
# ===============================

# Load daily ETF spot price data (path anonymized)
etf_data_path = r'/path/to/data/etf_daily_prices.csv'
spot_300etf = pd.read_csv(etf_data_path)

spot_300etf['trade_date'] = spot_300etf['trade_date'].astype(str)
spot_300etf = spot_300etf[['trade_date', 'close']].sort_values(by='trade_date')
spot_300etf['trade_date'] = spot_300etf['trade_date'].apply(
    lambda x: datetime.strptime(x, '%Y%m%d').date()
)
spot_300etf.rename(
    columns={'trade_date': 'TradingDate', 'close': 'Spot'},
    inplace=True
)

# Load option contract metadata (path anonymized)
option_param_path = r'/path/to/data/option_pricing_parameters.csv'
data_par = pd.read_csv(option_param_path)

data_par = data_par[data_par['ShortName'].apply(lambda x: 'CSI 300' in x)]
data_par = data_par[data_par['DataType'] == 1]

def Moneyness(ddata, how='Volume'):
    """
    Classify option moneyness (ATM, OTM, ITM) based on
    trading volume or price-based criteria.
    """

    if how == 'Volume':
        # Define ATM strike as the strike with maximum aggregated volume
        vol_sum = ddata.groupby(['K']).Volume.sum()
        ATM_p = vol_sum.idxmax()

    if how == 'PCP':
        # Alternative ATM definition using call-put price differences
        minus = ddata.groupby(['K']).apply(
            lambda x: abs(x.ClosePrice.diff())
        ).dropna().reset_index()
        ATM_p = minus.loc[minus.ClosePrice.idxmin(), 'StrikePrice']

    ddata.loc[ddata.K == ATM_p, 'Moneyness'] = 'ATM'

    ddata.loc[
        ((ddata.CallOrPut == 'C') & (ddata.K > ATM_p)) |
        ((ddata.CallOrPut == 'P') & (ddata.K < ATM_p)),
        'Moneyness'
    ] = 'OTM'

    ddata.loc[
        ((ddata.CallOrPut == 'C') & (ddata.K < ATM_p)) |
        ((ddata.CallOrPut == 'P') & (ddata.K > ATM_p)),
        'Moneyness'
    ] = 'ITM'

    return ddata
