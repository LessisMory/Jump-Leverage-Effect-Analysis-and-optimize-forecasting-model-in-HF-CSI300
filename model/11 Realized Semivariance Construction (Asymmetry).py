# Sort intraday data and group by trading date
grouped_day = spot_300_org.sort_values(by=['date', 'time']).groupby('date')

# Initialize containers for positive and negative semivariances
pos_var = pd.DataFrame(index=trade_date_sgn, columns=['pos_var'])
neg_var = pd.DataFrame(index=trade_date_sgn, columns=['neg_var'])

# Loop over trading days
for day in trade_date_sgn:
    group1 = grouped_day.get_group(day).sort_values(by='time').reset_index(drop=True)

    # Compute intraday returns
    RT_values = group1['close'].diff()[1:]

    # Positive and negative semivariances
    pos_semi_var = np.mean([r**2 for r in RT_values if r > 0])
    neg_semi_var = np.mean([r**2 for r in RT_values if r < 0])

    pos_var.loc[day, 'pos_var'] = pos_semi_var
    neg_var.loc[day, 'neg_var'] = neg_semi_var
