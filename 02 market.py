import streamlit as st
import pandas as pd
import requests
import graphviz

@st.cache_data
def getdata(s: str) -> pd.DataFrame:
    """
    Fetches data from FRED for a given index
    Args:
        s (str): index symbol
    """
    x = requests.get(f"https://api.stlouisfed.org/fred/series/observations?api_key={st.secrets['FRED_API_KEY']}&file_type=json&series_id={s}")
    y = pd.DataFrame(x.json()["observations"])[["date", "value"]]
    return y

data = getdata("SP500").set_index("date")
st.write(data)
st.line_chart(data)

# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge("run", "intr")
graph.edge("intr", "runbl")
graph.edge("runbl", "run")
graph.edge("run", "kernel")
graph.edge("kernel", "zombie")
graph.edge("kernel", "sleep")
graph.edge("kernel", "runmem")
graph.edge("sleep", "swap")
graph.edge("swap", "runswap")
graph.edge("runswap", "new")
graph.edge("runswap", "runmem")
graph.edge("new", "runmem")
graph.edge("sleep", "runmem")

st.graphviz_chart(graph)