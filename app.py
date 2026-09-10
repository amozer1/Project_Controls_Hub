import streamlit as st

from components.sidebar import render_sidebar


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="PROJECT CONTROLS HUB",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# SESSION STATE
# =========================================================

if "selected_framework" not in st.session_state:
    st.session_state.selected_framework = "UU DD&B Framework"

if "selected_asset" not in st.session_state:
    st.session_state.selected_asset = "Ferry PS"

if "selected_navigation" not in st.session_state:
    st.session_state.selected_navigation = "Overview"


# =========================================================
# SIDEBAR
# =========================================================

render_sidebar()


# =========================================================
# TEMPORARY MAIN CONTENT
# =========================================================

st.title(
    st.session_state.selected_navigation
)

st.write(
    f"Framework: **{st.session_state.selected_framework}**"
)

st.write(
    f"Asset: **{st.session_state.selected_asset}**"
)