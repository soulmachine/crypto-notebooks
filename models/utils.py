import pandas as pd

def read_bars(csv_file: str)->pd.DataFrame:
    dtypes = {'exchange': 'category', 'market_type': 'category', 'pair': 'category', 'bar_type': 'category',
              'bar_size':'category', 'open': 'float32', 'timestamp': 'int64', 'timestamp_end': 'int64',
              'high': 'float32', 'low': 'float32', 'close': 'float32', 'mean': 'float32', 'median': 'float32',
              'volume': 'float64', 'volume_sell': 'float64', 'volume_buy': 'float64', 
              'volume_quote': 'float64', 'volume_quote_sell': 'float64', 'volume_quote_buy': 'float64',
              'count': 'int32', 'count_sell': 'int32', 'count_buy': 'int32'}
    bars_df = pd.read_csv(csv_file, engine='c', dtype=dtypes)
    bars_df['vwap'] = bars_df['volume_quote'] / bars_df['volume']
    bars_df['timestamp'] = pd.to_datetime(bars_df['timestamp'], unit='ms', utc=True)
    bars_df['timestamp_end'] = pd.to_datetime(bars_df['timestamp_end'], unit='ms', utc=True)
    bars_df.set_index('timestamp', drop=False, inplace=True, verify_integrity='TimeBar' in csv_file)
    return bars_df
