import streamlit as st
from pathlib import Path

from components.sidebar import render_sidebar
from views.overview import render_overview


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
# LOAD CSS
# =========================================================

css_path = Path("assets/styles.css")

st.markdown(
    f"<style>{css_path.read_text()}</style>",
    unsafe_allow_html=True,
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