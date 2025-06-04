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
    data.columns = data.columns.to_flat_index().str.join('_')
    return data

df = getdata("NVDA")
st.dataframe(df)

st.write(os.listdir())
