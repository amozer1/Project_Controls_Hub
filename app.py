import streamlit as st
from pathlib import Path

from components.sidebar import render_sidebar


# =========================================================
# OVERVIEW — FERRY
# =========================================================

from overview.ferry.project_position_ferry import (
    render_project_position_ferry,
)


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
# LOAD OVERVIEW CSS
# =========================================================

overview_css_path = Path("assets/overview.css")

st.markdown(
    f"<style>{overview_css_path.read_text()}</style>",
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


# =========================================================
# OVERVIEW
# =========================================================

if st.session_state.selected_navigation == "Overview":

    if st.session_state.selected_asset == "Ferry PS":

        # =================================================
        # UNIT 01 — PROJECT POSITION
        # =================================================

        render_project_position_ferry()