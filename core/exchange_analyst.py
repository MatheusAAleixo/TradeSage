import pandas as pd
import pytz
import requests
from core.indicators import calculate_rsi, calculate_macd, calculate_sma

def get_binance_klines(symbol:str, interval="1h", limit=100):
    url = f"https://api.binance.com/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data, columns=[
        "timestamp", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "num_trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])

    df["close"] = df["close"].astype(float)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit='ms')
    return df[["timestamp", "close"]]

def run_exchange_analysis(symbol= str, modo="conservador"):
    df = get_binance_klines(symbol=symbol)

    # Calcula os indicadores técnicos
    df["rsi"] = calculate_rsi(df["close"], period=14)
    df["macd"], df["macd_signal"], _ = calculate_macd(df["close"])
    df["sma50"] = calculate_sma(df["close"], window=50)

    # Pega o candle mais recente
    latest = df.iloc[-1]
    sinal = "NEUTRO"

    # 🔍 Estratégia CONSERVADORA (todos os critérios precisam bater)
    if modo == "conservador":
        if latest["rsi"] < 30 and latest["macd"] > latest["macd_signal"] and latest["close"] > latest["sma50"]:
            sinal = "COMPRA"
        elif latest["rsi"] > 70 and latest["macd"] < latest["macd_signal"] and latest["close"] < latest["sma50"]:
            sinal = "VENDA"

    # 🚀 Estratégia AGRESSIVA (basta 2 de 3 critérios se confirmarem)
    elif modo == "agressivo":
        sinais_compra = 0
        sinais_venda = 0

        if latest["rsi"] < 30:
            sinais_compra += 1
        if latest["macd"] > latest["macd_signal"]:
            sinais_compra += 1
        if latest["close"] > latest["sma50"]:
            sinais_compra += 1

        if latest["rsi"] > 70:
            sinais_venda += 1
        if latest["macd"] < latest["macd_signal"]:
            sinais_venda += 1
        if latest["close"] < latest["sma50"]:
            sinais_venda += 1

        if sinais_compra >= 2:
            sinal = "COMPRA"
        elif sinais_venda >= 2:
            sinal = "VENDA"

    fuso_recife = pytz.timezone("America/Recife")
    timestamp_local = latest["timestamp"].tz_localize("UTC").astimezone(fuso_recife)

    resultado = {
        "ativo": symbol,
        "timestamp": timestamp_local.strftime("%Y-%m-%d %H:%M:%S"),
        "preco": round(latest["close"], 2),
        "sinal": sinal,
        "rsi": round(latest["rsi"], 2),
        "macd": round(latest["macd"], 4),
        "macd_signal": round(latest["macd_signal"], 4),
        "sma50": round(latest["sma50"], 2),
    }

    return resultado