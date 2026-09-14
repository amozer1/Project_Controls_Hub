import streamlit as st
from pathlib import Path

from components.sidebar import render_sidebar

# =========================================================
# OVERVIEW — FERRY
# =========================================================

from overview.ferry.project_position_ferry import (
    render_project_position_ferry,
)

from overview.ferry.delivery_status_ferry import (
    render_delivery_status_ferry,
)

from overview.ferry.next_7_days_cl32_ferry import (
    render_next_7_days_cl32_ferry,
)

from overview.ferry.programme_changes_ferry import (
    render_programme_changes_ferry,
)

from overview.ferry.key_milestones_cl32_ferry import (
    render_key_milestones_cl32_ferry,
)

from overview.ferry.management_focus_ferry import (
    render_management_focus_ferry,
)

from overview.ferry.delivery_by_discipline_ferry import (
    render_delivery_by_discipline_ferry,
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

        # =================================================
        # UNIT 02 — DELIVERY STATUS
        # =================================================

        render_delivery_status_ferry()

        # =================================================
        # UNIT 03 — NEXT 7 DAYS
        # =================================================

        render_next_7_days_cl32_ferry()

        # =================================================
        # UNIT 04 — PROGRAMME CHANGES
        # =================================================

        render_programme_changes_ferry()

        # =================================================
        # UNIT 05 — KEY MILESTONES
        # =================================================

        render_key_milestones_cl32_ferry()

        # =================================================
        # UNIT 06 — MANAGEMENT FOCUS
        # =================================================

        render_management_focus_ferry()

        # =================================================
        # UNIT 07 — DELIVERY BY DISCIPLINE
        # =================================================

        render_delivery_by_discipline_ferry()