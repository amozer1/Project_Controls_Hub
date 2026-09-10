import streamlit as st

from components.sidebar import render_sidebar


st.set_page_config(
    page_title="Project Controls Hub",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------
# LOAD STYLES
# ---------------------------------------------------------

with open("assets/styles.css", "r", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

sidebar = render_sidebar()


# ---------------------------------------------------------
# TEMPORARY MAIN CONTENT
# ---------------------------------------------------------

st.title("Project Controls Hub")

st.write(
    f"Framework: **{sidebar['framework']}**"
)

st.write(
    f"Project: **{sidebar['project']}**"
)

st.write(
    f"Page: **{sidebar['page']}**"
)