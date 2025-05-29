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
    y.set_index("date", inplace=True)
    return y

indices = {
    "US Treasury 30Y Constant Murity": "DGS30",
    "US Treasury 20Y Constant Murity": "DGS20",
    "US Treasury 10Y Constant Murity": "DGS10",
    "US Treasury 7Y Constant Murity": "DGS7",
    "US Treasury 5Y Constant Murity": "DGS5",
    "US Treasury 3Y Constant Murity": "DGS3",
    "US Treasury 2Y Constant Murity": "DGS2",
    "US Treasury 1Y Constant Murity": "DGS1",
    "US Treasury 6M Constant Murity": "DGS6MO",
    "US Treasury 3M Constant Murity": "DGS3MO",
    "US Treasury 1M Constant Murity": "DGS1MO",
}

index = st.selectbox("Select an index",
                     indices.keys())
data = getdata("indices[index]")
st.write(f"You select {index} and its symbol is {indices[index]}")
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