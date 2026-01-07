# ===============================
# Module 5: Term structure regression for implied variance measures
# ===============================

import statsmodels.api as sm

# Cross-sectional regressions across maturities
nn = len(TTM)  # Number of trading days (= len(VIX) = len(VS))

spot_vs = np.zeros((nn, 1))
spot_vix = np.zeros((nn, 1))
slope_vs = np.zeros((nn, 1))
slope_vix = np.zeros((nn, 1))

for j in range(nn):
    numpy_vix = VIX.to_numpy()
    numpy_vs = VS.to_numpy()
    numpy_ttm = TTM.to_numpy()

    vix = numpy_vix[j, :].reshape(-1, 1)
    vs = numpy_vs[j, :].reshape(-1, 1)
    T_all = numpy_ttm[j, :].reshape(-1, 1)

    # Quadratic specification of the term structure
    X = np.column_stack((np.ones_like(T_all), T_all ** 2))

    model_vs = sm.OLS(vs, X)
    model_vix = sm.OLS(vix, X)

    results_vs = model_vs.fit()
    results_vix = model_vix.fit()

    # Extract spot (intercept) and slope coefficients
    spot_vs[j, 0] = results_vs.params[0]
    spot_vix[j, 0] = results_vix.params[0]
    slope_vs[j, 0] = results_vs.params[1]
    slope_vix[j, 0] = results_vix.params[1]

# Align regression outputs with trading dates
spot_vs_inv_date = pd.concat(
    [date_df, pd.DataFrame(spot_vs, columns=['spot_vs'])], axis=1
)
spot_vix_inv_date = pd.concat(
    [date_df, pd.DataFrame(spot_vix, columns=['spot_vix'])], axis=1
)
slope_vs_inv_date = pd.concat(
    [date_df, pd.DataFrame(slope_vs, columns=['slope_vs'])], axis=1
)
slope_vix_inv_date = pd.concat(
    [date_df, pd.DataFrame(slope_vix, columns=['slope_vix'])], axis=1
)

# Remove economically implausible negative spot values
negative_indices1 = spot_vs_inv_date[spot_vs_inv_date['spot_vs'] < 0].index
negative_indices2 = spot_vix_inv_date[spot_vix_inv_date['spot_vix'] < 0].index

spot_vs_inv_date.drop(negative_indices1, inplace=True)
spot_vix_inv_date.drop(negative_indices2, inplace=True)
slope_vs_inv_date.drop(negative_indices1, inplace=True)
slope_vix_inv_date.drop(negative_indices2, inplace=True)
