import numpy as np
import datetime as dt
import pandas as pd
import streamlit as st
import yfinance as yf

st.set_page_config(layout="wide")

topics = [
    "growth_technology_stocks",
    "most_actives",
    "most_shorted_stocks",
    "aggressive_small_caps",
    "small_cap_gainers",
    "undervalued_growth_stocks",
    "undervalued_large_caps",
    "day_gainers",
    "day_losers",
]

cols = [
    "symbol", 
    "shortName", 
    "currency", 
    "averageAnalystRating", 
    "forwardPE", 
    "trailingPE", 
    "epsForward", 
    "fiftyTwoWeekHigh", 
    "fiftyTwoWeekLow"
]

@st.cache_data(ttl=3600)
def get_topic(topic: str) -> pd.DataFrame:
    df = pd.DataFrame(yf.screen(topic)["quotes"])
    return df

@st.cache_data(ttl=3600)
def get_candles(symbol: str) -> pd.DataFrame:
    df = yf.Ticker(symbol).history(period="5y")
    return df

topic = st.selectbox(
    "Choose a topic:",
    topics,
    index=0
)

cols = ["symbol", 
        "shortName", 
        "currency", 
        "averageAnalystRating", 
        "forwardPE", 
        "trailingPE", 
        "epsForward", 
        "fiftyTwoWeekHigh", 
        "fiftyTwoWeekLow"]

df_show = get_topic(topic)[cols]
event = st.dataframe(data=df_show,
                    hide_index=True,
                    on_select="rerun",
                    selection_mode=["single-row"]
)

row = event.selection["rows"]

if row:
    symbol = df_show.iloc[row].iat[0,0]
    df_stock = get_candles(symbol)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("close")
        st.line_chart(df_stock["Close"])
    with col2:
        st.write("volume")
        st.line_chart(df_stock["Volume"])
    with col3:
        st.write("log return")
        st.line_chart(np.log(df_stock["Close"]).diff())
