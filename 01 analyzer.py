import streamlit as st
import yfinance as yf
from mistralai import Mistral

# Set the page configuration
st.set_page_config(
    page_title="Stock Price App",
    page_icon="📈",
    layout="wide"
)

# LLM
MISTRAL_API_KEY = "YkwXX7KW6nZ5uhUF1zRjEGQmnylSG6jU"
client = Mistral(api_key=MISTRAL_API_KEY)
securities = ["NVDA", "AAPL", "MSFT", "GOOGL", "AMZN"]

@st.cache_data
def getdata(s: str) -> dict:
    """
    Fetches data from Yahoo Finance for a given stock symbol.
    Args:
        s (str): Stock symbol.  
    """
    d = {}
    dat = yf.Ticker(s)
    d["info"] = dat.info
    d["calendar"] = dat.calendar
    d["analyst"] = dat.analyst_price_targets
    d["qstatement"] = dat.quarterly_income_stmt
    d["history"] = dat.history(period="10y")
    return d

def main() -> None:
    """
    Main function to run the Streamlit app.
    """
    data = {s: getdata(s) for s in securities}

    # Define the sidebar
    with st.sidebar:
        sec = st.radio(
            "Which stock do you want to analyze?",
            data.keys()
        )
        st.divider()
        with st.container(border=True):
            result = st.empty()

    # Create the main content
    st.header(f"Stock Price Analysis for {sec}")
    with st.container(border=True):
        st.write(data[sec]["info"]["longBusinessSummary"])

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Info")
        info_fields = ["sector", "industry",
                       "address1", "city", "state", "zip", "country", "website", 
                       "marketCap", "forwardPE", "forwardEps", "dividendYield"]
        info_data = {k: v for k, v in data[sec]["info"].items() if k in info_fields}
        st.dataframe(info_data)

    with col2:
        st.write("Analyst")
        st.dataframe(data[sec]["analyst"])

    with col3:
        st.write("Calendar")
        st.dataframe(data[sec]["calendar"], hide_index=True)

    with st.container(border=True):
        st.write("Quarterly Statement")
        st.dataframe(data[sec]["qstatement"])

    with st.container(border=True):
        st.write("History")
        st.line_chart(data[sec]["history"]["Close"])

    with st.expander("See full info", expanded=False):
        st.write(data)

    # LLM comment
    prompt = f"""Analyze the stock price of {sec} and give me the insight of the data.
                The data is {data[sec]}. Explain what it means for the stock price.
                Reply in markdown format.
    """
    stream_response = client.chat.stream(
        model = "mistral-small-latest",
        messages= [
            {
                "role": "user",
                "content": prompt,
            },
        ]
    )
    response = ""
    for chunk in stream_response:
        response += chunk.data.choices[0].delta.content
        result.write(response)

if __name__ == "__main__":
    main()
