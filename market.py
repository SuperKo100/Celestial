import streamlit as st
import streamlit.components.v1 as components
import yfinance as yf

# Include Google Analytics tracking code
with open("google_analytics.html", "r") as f:
    html_code = f.read()
    components.html(html_code, height=0)

tickers = ["TSM", "NVDA", "IWY", "GLD"]
history = yf.download(tickers, period="10y")

st.dataframe(history[["Close", "Volume"]])
