import streamlit as st
import yfinance as yf

tickers = ["TSM", "NVDA", "IWY", "GLD"]
history = yf.download(tickers)

st.dataframe(history)
