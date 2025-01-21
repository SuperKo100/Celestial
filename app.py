import streamlit as st

pg = st.navigation([
    st.Page("market.py", title="Market", icon=":material/add_circle:"),
    # st.Page("delete.py", title="Delete entry", icon=":material/delete:")
])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()

st.write("Hello World")
