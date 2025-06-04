import os
import streamlit as st
import yfinance as yf

@st.cache_data
def getdata(s: str) -> dict:
    """
    Fetches data from Yahoo Finance for a given stock symbol.
    Args:
        s (str): Stock symbol.  
    """
    data = yf.download([s, "^SPX"], period="ytd", interval="1wk", multi_level_index=False)
    data.columns = [f"{b}_{a}" for (a, b) in df.columns.to_flat_index()] # data.columns.to_flat_index().str.join('_')
    data = data.fillna(method="ffill").replace(0, method="ffill")
    return data

df = getdata("NVDA")
st.dataframe(df)

st.write(os.listdir())
