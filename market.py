import streamlit as st
import yfinance as yf

tickers = ["TSM", "NVDA", "IWY", "GLD"]
history = yf.download(tickers, period="10y")

st.dataframe(history)
