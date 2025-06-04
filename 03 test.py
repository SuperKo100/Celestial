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
    data = yf.download([s, "^SPX"], period="10y", interval="1wk", multi_level_index=False)
    data.columns = data.columns.to_flat_index().str.join('_')
    data = data[[f"Open_{s}", f"High_{s}", f"Low_{s}", f"Close_{s}", f"Volume_{s}",
                "Open_^SPX", "High_^SPX", "Low_^SPX", "Close_^SPX", "Volume_^SPX"]]
    data = data.fillna(method="ffill").replace(0, method="ffill")
    return data.pct_change()

df = getdata("NVDA")
st.dataframe(df)

st.write(os.listdir())
