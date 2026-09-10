import streamlit as st

from config.frameworks import FRAMEWORKS


# ============================================================
# DISPLAY ORDER
# ============================================================

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


# ============================================================
# SIDEBAR
# ============================================================

def render_sidebar():

    with st.sidebar:

        # ----------------------------------------------------
        # PROJECT CONTROLS HUB
        # ----------------------------------------------------

        st.markdown("## PROJECT CONTROLS HUB")
        st.caption("Design Management Intelligence")

        st.divider()

        # ----------------------------------------------------
        # FRAMEWORKS
        # ----------------------------------------------------

        st.markdown("**FRAMEWORKS**")

        for framework_index, framework in enumerate(FRAMEWORK_ORDER):

            if framework not in FRAMEWORKS:
                continue

            # Framework heading
            st.markdown(f"**{framework}**")

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

            # Separator between frameworks
            if framework_index < len(FRAMEWORK_ORDER) - 1:
                st.divider()

        # ----------------------------------------------------
        # NAVIGATION
        # ----------------------------------------------------

        st.divider()

        st.markdown("**NAVIGATION**")

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

        # ----------------------------------------------------
        # PROFILE
        # ----------------------------------------------------

        st.divider()

        profile_col1, profile_col2 = st.columns(
            [1, 4],
            vertical_alignment="center",
        )

        with profile_col1:
            st.markdown("**JS**")

        with profile_col2:
            st.markdown("**John Smith**")
            st.caption("Design Manager")


# ============================================================
# ASSET SELECTION
# ============================================================

def _select_asset(framework, asset):

    st.session_state.selected_framework = framework
    st.session_state.selected_asset = asset

    # Reset navigation when changing project
    st.session_state.selected_navigation = "Overview"


# ============================================================
# NAVIGATION SELECTION
# ============================================================

def _select_navigation(item):

    st.session_state.selected_navigation = item