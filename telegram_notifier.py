import requests
import os

# Configure sua chave e ID do chat como variáveis de ambiente ou direto aqui
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

def send_telegram(resultado):
    mensagem = (
        f"📈 <b>Análise de {resultado.get('ativo', 'N/A')}</b> ({resultado.get('timestamp', 'N/A')}):\n"
        f"💵 <b>Preço:</b> ${resultado.get('preco', 'N/A')}\n"
        f"📊 <b>Sinal:</b> {resultado.get('sinal', 'N/A')}\n"
        f"📉 <b>RSI:</b> {resultado.get('rsi', 'N/A')}\n"
        f"📈 <b>MACD:</b> {resultado.get('macd', 'N/A')} | <b>Sinal:</b> {resultado.get('macd_signal', 'N/A')}\n"
        f"📏 <b>SMA50:</b> {resultado.get('sma50', 'N/A')}"
    )

    print("🔍 Mensagem formatada:")
    print(mensagem)

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensagem,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, data=payload, timeout=5)
        response.raise_for_status()
        print("✅ Mensagem enviada para o Telegram!")
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ Erro HTTP: {http_err} - Resposta: {response.text}")
    except Exception as err:
        print(f"❌ Erro inesperado: {err}")
