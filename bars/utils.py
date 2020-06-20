from operator import itemgetter
from typing import Dict, List

import numpy as np

def aggregate(nums: np.ndarray)-> Dict:
    assert nums.size > 0
    return {
        'open': nums[0],
        'high': np.max(nums),
        'low': np.min(nums),
        'close': nums[-1],
        'mean': np.mean(nums),
        'median': np.median(nums),
    }

def aggregate_trade(trades)-> Dict:  # trades: pd.DataFrame
    price_ohlcv = aggregate(trades['price'].values);
    
    trades_sell = trades[trades['side'] == True]
    trades_buy = trades[trades['side'] == False]

    volume = trades['quantity'].sum()
    volume_sell = trades_sell['quantity'].sum()
    volume_buy = trades_buy['quantity'].sum()
    volume_quote = (trades['price'] * trades['quantity']).sum()
    volume_quote_sell = (trades_sell['price'] * trades_sell['quantity']).sum()
    volume_quote_buy = (trades_buy['price'] * trades_buy['quantity']).sum()

    price_ohlcv.update({
        'volume': volume,
        'volume_sell': volume_sell,
        'volume_buy': volume_buy,
        'volume_quote': volume_quote,
        'volume_quote_sell': volume_quote_sell,
        'volume_quote_buy': volume_quote_buy,

        'vwap': volume_quote / volume,

        'count': trades.shape[0],
        'count_sell': trades_sell.shape[0],
        'count_buy': trades_buy.shape[0],
    })
    return price_ohlcv

def convert_to_bar(bar_type:str, bar_size: int, trades)->Dict:  # trades: pd.DataFrame
    assert trades.shape[0] > 0

    trades.sort_values('trade_id', inplace=True)

    exchange, marketType, pair = itemgetter('exchange', 'marketType', 'pair')(trades.iloc[0])
    trade_agg = aggregate_trade(trades);

    timestamp_begin = trades.iloc[0].timestamp // bar_size * bar_size if bar_type == 'TimeBar' else trades.iloc[0].timestamp;
    timestamp_end = (timestamp_begin + bar_size) if bar_type == 'TimeBar' else (trades.iloc[-1].timestamp + 1);

    bar = {
      'exchange': exchange,
      'market_type': marketType,
      'pair': pair,
      'bar_type': bar_type,
      'bar_size': bar_size,
      'timestamp': timestamp_begin,
      'timestamp_end': timestamp_end,
    };
    bar.update(trade_agg)

    return bar
