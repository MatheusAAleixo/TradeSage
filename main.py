import time
import schedule
from core.exchange_analyst import run_exchange_analysis
from telegram_notifier import send_telegram
from service.config_manager import get_modo

# Lista de ativos a serem analisados
ATIVOS = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT", "ADAUSDT", "DOGEUSDT", "AVAXUSDT", "DOTUSDT", "TRXUSDT"]

def analisar_ativos():
    modo = get_modo()
    print(f"\n🔄 Executando análise dos ativos no modo: {modo.upper()}...\n")
    
    for ativo in ATIVOS:
        try:
            resultado = run_exchange_analysis(symbol=ativo, modo=modo)
            print(f"[{resultado['ativo']}] {resultado['timestamp']}")
            print(f"Preço: {resultado['preco']}")
            print(f"Sinal: {resultado['sinal']}")
            print(f"RSI: {resultado['rsi']} | MACD: {resultado['macd']} | Signal: {resultado['macd_signal']}")
            print(f"SMA50: {resultado['sma50']}\n")
            
            # Enviar para o Telegram apenas se for COMPRA ou VENDA
            if resultado['sinal'].lower() in ['compra', 'venda']:
                send_telegram(resultado)

        except Exception as e:
            print(f"❌ Erro ao analisar {ativo}: {e}")
    
    print("⏳ Aguardando próxima execução em 5 minutos...\n")

# Agendamento para rodar a cada 5 minutos
schedule.every(5).minutes.do(analisar_ativos)

# Executa a primeira vez imediatamente
analisar_ativos()

# Loop de execução contínuo
while True:
    schedule.run_pending()
    time.sleep(1)