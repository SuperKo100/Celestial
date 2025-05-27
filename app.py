import streamlit as st
import streamlit.components.v1 as components

# Include Google Analytics tracking code
with open("google_analytics.html", "r") as f:
    html_code = f.read()
    components.html(html_code, height=0)

pg = st.navigation(
    {
        "Analyzer": [
            st.Page("01 analyzer.py", title="Analyzer", icon=":material/add_circle:")
        ],
        "Market": [
            st.Page("02 market.py", title="Market", icon=":material/add_circle:")
        ]
    }
)

#st.set_page_config(page_title="Data manager", page_icon=":material/edit:")

pg.run()
