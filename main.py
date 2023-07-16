import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import talib

# Título do app
st.title('AppDeAções')
# Barra lateral
st.sidebar.title('Selecione o stock')
ticker_symbol = st.sidebar.text_input('stock', 'AAPL', max_chars=10)
# Baixar dados
data = yf.download(ticker_symbol, start='2020-01-01', end='2023-06-26')
# Cálculo do indicador MACD
macd, signal, hist = talib.MACD(data['Close'])
# Exibir os dados
st.subheader('Histórico')
st.dataframe(data)
# Exibir Gráfico com indicador MACD
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Fechamento'))

fig.add_trace(go.Scatter(x=data.index, y=macd, name='MACD'))
fig.add_trace(go.Scatter(x=data.index, y=signal, name='Sinal'))
fig.add_trace(go.Scatter(x=data.index, y=hist, name='Histograma'))

fig.update_layout(title=f"{ticker_symbol}", xaxis_title="Data", yaxis_title="Preço")
st.plotly_chart(fig)
