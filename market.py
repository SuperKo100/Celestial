import yfinance as yf

tikcer = st.selectbox(
    "Select a ticker",
    ["TSM", "NVDA", "IWY", "GLD"]
)

tk = yf.Ticker(ticker)

# CALL THE MULTIPLE FUNCTIONS AVAILABLE AND STORE THEM IN VARIABLES.
actions = tk.get_actions()
analysis = tk.get_analysis()
balance = tk.get_balance_sheet()
calendar = tk.get_calendar()
cashflow = tk.get_cashflow()
info = tk.get_info()
inst_holders = tk.get_institutional_holders()
news = tk.get_news()
recommendations = tk.get_recommendations()
sustainability = tk.get_sustainability()

st.dataframe(actions)
st.dataframe(analysis)
st.dataframe(balance)
st.dataframe(calendar)
st.dataframe(cashflow)
st.dataframe(info)
st.dataframe(news)
st.dataframe(recommendations)
st.dataframe(sustainability)
