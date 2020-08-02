import backtrader as bt
import pandas as pd

def read_bars(csv_file: str)->pd.DataFrame:
    dtypes = {'exchange': 'category', 'market_type': 'category', 'pair': 'category', 'bar_type': 'category',
              'bar_size':'category', 'open': 'float32', 'timestamp': 'int64', 'timestamp_start': 'int64',
              'high': 'float32', 'low': 'float32', 'close': 'float32', 'mean': 'float32', 'median': 'float32',
              'volume': 'float64', 'volume_sell': 'float64', 'volume_buy': 'float64', 
              'volume_quote': 'float64', 'volume_quote_sell': 'float64', 'volume_quote_buy': 'float64',
              'count': 'int32', 'count_sell': 'int32', 'count_buy': 'int32'}
    bars_df = pd.read_csv(csv_file, engine='c', dtype=dtypes)
    bars_df['vwap'] = bars_df['volume_quote'] / bars_df['volume']
    bars_df['timestamp'] = pd.to_datetime(bars_df['timestamp'], unit='ms', utc=True)
    bars_df['timestamp_start'] = pd.to_datetime(bars_df['timestamp_start'], unit='ms', utc=True)
    if 'TimeBar' in csv_file:
        bars_df.set_index('timestamp', drop=False, inplace=True, verify_integrity=True)
    return bars_df

class CryptoPandasData(bt.feeds.PandasData):
    lines = ('mean', 'median', 'volume_sell', 'volume_buy',
             'volume_quote', 'volume_quote_sell', 'volume_quote_buy',
             'count', 'count_sell', 'count_buy', 'vwap')
    params = (
        ('datetime', 'timestamp'),
        ('openinterest',None),
        ('mean', -1),
        ('median', -1),
        ('volume_sell', -1),
        ('volume_buy', -1),
        ('volume_quote', -1),
        ('volume_quote_sell', -1),
        ('volume_quote_buy', -1),
        ('count', -1),
        ('count_sell', -1),
        ('count_buy', -1),
        ('vwap', -1),
    )
