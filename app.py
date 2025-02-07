import streamlit as st
import streamlit.components.v1 as components

# Include Google Analytics tracking code
with open("google_analytics.html", "r") as f:
    html_code = f.read()
    st.html(html_code, height=0)

pg = st.navigation(
    {
        "Market": [
            st.Page("market.py", title="Market", icon=":material/add_circle:")
        ],
        "System": [
            st.Page("system.py", title="System", icon=":material/add_circle:")
        ]
    }
)

#st.set_page_config(page_title="Data manager", page_icon=":material/edit:")

pg.run()
