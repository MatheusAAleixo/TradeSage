import pandas as pd
from ta.trend import SMAIndicator, MACD
from ta.momentum import RSIIndicator
from binance.client import Client
import datetime

#CONFIGURAÇÕES
SYMBOL = 'BTCUSDT'
INTERVAL = Client.KLINE_INTERVAL_5MINUTE
LIMIT = 100 #ÚLTIMOS 100 CANDLES (~8 HORAS)

client = Client()

def fetch_data()
    klines = client.get_klines(symbol=SYMBOL, interval = INTERVAL, limit = LIMIT)
    DF = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'num_trades', 'taker_buy_base_asset_volume', 'ignore'])
    