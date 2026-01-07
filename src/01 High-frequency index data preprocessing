# ===============================
# Module 1: High-frequency index data preprocessing
# ===============================

from datetime import datetime
import pandas as pd
import numpy as np

# Load high-frequency index price data (path anonymized)
hf_data_path = r'/path/to/data/high_frequency_index.csv'
spot_300 = pd.read_csv(hf_data_path)

# Convert trade time to datetime format
spot_300['trade_time'] = spot_300['trade_time'].apply(
    lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
)

# Sort observations chronologically and construct time variables
spot_300 = spot_300.sort_values(by='trade_time').reset_index()

# Preserve original price level for reference
spot_300['Index'] = spot_300['close']

# Log-price transformation (standard in volatility modeling)
spot_300['close'] = np.log(spot_300['close'])

# Extract trading date and intraday time
spot_300['trade_date'] = pd.to_datetime(spot_300['trade_time'])
spot_300['date'] = spot_300['trade_date'].dt.date
spot_300['time'] = spot_300['trade_date'].dt.time

# Remove duplicated timestamps if any
trade_date_sgn = spot_300['date'].unique()
spot_300 = spot_300.drop_duplicates(subset=['trade_time'])

# Retain core variables for intraday analysis
spot_300_org = spot_300[['date', 'time', 'close']].copy()
