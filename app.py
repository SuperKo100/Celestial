import streamlit as st

pg = st.navigation(
    {
        "Apps": [
            st.Page("01 analyzer.py", title="Analyzer", icon=":material/add_circle:"),
            st.Page("02 market.py", title="Market", icon=":material/add_circle:"),
            st.Page("03 test.py", title="Test", icon=":material/add_circle:"),
            st.Page("04 topics.py", title="Topics", icon=":material/add_circle:"),
        ]
    }
)

#st.set_page_config(page_title="Data manager", page_icon=":material/edit:")

pg.run()
