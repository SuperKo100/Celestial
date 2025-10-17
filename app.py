import streamlit as st

pg = st.navigation(
    {
        "Apps": [
            st.Page("01 screener.py", title="Analyzer", icon=":material/add_circle:"),
            st.Page("02 analyzer.py", title="Market", icon=":material/add_circle:"),
            st.Page("03 market.py", title="Test", icon=":material/add_circle:"),
        ]
    }
)

#st.set_page_config(page_title="Data manager", page_icon=":material/edit:")

pg.run()
