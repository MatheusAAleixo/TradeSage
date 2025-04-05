\=======================================

PROJETO: Trade Sage

\=======================================

Descrição:

\-----------

Este é um protótipo de uma IA que analisa gráficos em tempo real, indicadores técnicos e eventos de mercado para sugerir pontos de entrada (compra/venda) em operações de day trade.

Neste momento, o projeto está focado em criptomoedas,utilizando candles de 5 minutos e uma estratégia conservadora com os seguintes indicadores:

- RSI (Índice de Força Relativa)
- MACD (Média Móvel Convergente e Divergente)
- SMA50 (Média Móvel Simples de 50 períodos)

A ideia é evoluir o projeto para abranger outros ativos como ações,ETFs, commodities e índices da bolsa de valores.

Como executar:

\---------------

1 Instale as dependências:

     pip install -r requirements.txt

2 Execute a análise:

     python main.py

Saída esperada:

\----------------

A aplicação exibirá no console a análise mais recente com base no último candle de 5 minutos, incluindo preço, RSI, MACD, SMA50 e sugestão de ação (comprar, vender ou aguardar).

Exemplo de saída:

[BTCUSDT] 2025-04-05 12:25:00

Preço: 69450.28

Sinal: COMPRAR às 12:25

RSI: 28.91 | MACD: -94.0349 | Signal: -97.3420

SMA50: 69302.87

Próximos passos:

\-----------------

- Suporte a múltiplos ativos (ETH, BNB, ações etc.)
- Conexão com APIs de notícias (eventos políticos, econômicos)
- Notificações por Telegram ou email
- Backtesting de estratégias com dados históricos
- Interface web ou painel interativo com gráficos


