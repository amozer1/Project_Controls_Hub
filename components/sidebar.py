import streamlit as st

from config.frameworks import FRAMEWORKS


# ==============================================================
# SIDEBAR ORDER
# ==============================================================

FRAMEWORK_ORDER = [
    "UU Enterprise Framework",
    "UU DD&B Framework",
]


NAVIGATION_ITEMS = [
    ("⌂", "Overview"),
    ("▦", "Programme"),
    ("◈", "Delivery & Programme"),
    ("◇", "Communications"),
    ("▤", "Documents"),
    ("✦", "Intelligence"),
    ("▥", "Reports"),
    ("⚙", "Settings"),
]


# ==============================================================
# SIDEBAR
# ==============================================================

def render_sidebar():

    with st.sidebar:

        # ------------------------------------------------------
        # HEADER
        # ------------------------------------------------------

        st.markdown(
            "### PROJECT CONTROLS HUB"
        )

        st.caption(
            "Design Management Intelligence"
        )

        st.markdown(
            '<div class="sidebar-rule"></div>',
            unsafe_allow_html=True,
        )

        # ------------------------------------------------------
        # FRAMEWORKS
        # ------------------------------------------------------

        st.markdown(
            '<div class="sidebar-section-title">FRAMEWORKS</div>',
            unsafe_allow_html=True,
        )

        for framework_index, framework in enumerate(FRAMEWORK_ORDER):

            if framework not in FRAMEWORKS:
                continue

            # Framework separation
            if framework_index > 0:
                st.markdown(
                    '<div class="sidebar-rule sidebar-rule-small"></div>',
                    unsafe_allow_html=True,
                )

            # Framework heading
            st.markdown(
                f'<div class="framework-title">{framework}</div>',
                unsafe_allow_html=True,
            )

            # Assets
            for asset in FRAMEWORKS[framework]:

                selected = (
                    st.session_state.get("selected_framework")
                    == framework
                    and
                    st.session_state.get("selected_asset")
                    == asset
                )

                st.button(
                    asset,
                    key=f"asset_{framework}_{asset}",
                    use_container_width=True,
                    type="primary" if selected else "secondary",
                    on_click=_select_asset,
                    args=(framework, asset),
                )

        # ------------------------------------------------------
        # NAVIGATION
        # ------------------------------------------------------

        st.markdown(
            '<div class="sidebar-rule"></div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="sidebar-section-title">NAVIGATION</div>',
            unsafe_allow_html=True,
        )

        for icon, item in NAVIGATION_ITEMS:

            selected = (
                st.session_state.get("selected_navigation")
                == item
            )

            st.button(
                f"{icon}  {item}",
                key=f"navigation_{item}",
                use_container_width=True,
                type="primary" if selected else "secondary",
                on_click=_select_navigation,
                args=(item,),
            )

        # ------------------------------------------------------
        # PROFILE
        # ------------------------------------------------------

        st.markdown(
            '<div class="sidebar-rule"></div>',
            unsafe_allow_html=True,
        )

        profile_col1, profile_col2 = st.columns(
            [1, 4],
            vertical_alignment="center",
        )

        with profile_col1:
            st.markdown(
                '<div class="profile-initials">JS</div>',
                unsafe_allow_html=True,
            )

        with profile_col2:
            st.markdown(
                '<div class="profile-name">John Smith</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                '<div class="profile-role">Design Manager</div>',
                unsafe_allow_html=True,
            )


# ==============================================================
# SELECTION HANDLERS
# ==============================================================

def _select_asset(framework, asset):

    st.session_state.selected_framework = framework
    st.session_state.selected_asset = asset
    st.session_state.selected_navigation = "Overview"


def _select_navigation(item):

    st.session_state.selected_navigation = item