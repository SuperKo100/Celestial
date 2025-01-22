import streamlit as st

pg = st.navigation(
    {
        "Market": [
            st.Page("market.py", title="Market", icon=":material/add_circle:")
        ],
        "System": [
            st.Page("market.py", title="Market", icon=":material/add_circle:")
        ]
    }
)

#st.set_page_config(page_title="Data manager", page_icon=":material/edit:")

pg.run()
