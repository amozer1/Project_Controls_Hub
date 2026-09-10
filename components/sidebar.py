import streamlit as st

from config.frameworks import FRAMEWORKS


FRAMEWORK_ORDER = [
    "UU Enterprise Framework",
    "UU DD&B Framework",
]


NAVIGATION_ITEMS = [
    "Overview",
    "Programme",
    "Delivery & Programme",
    "Communications",
    "Documents",
    "Intelligence",
    "Reports",
    "Settings",
]


def render_sidebar():

    with st.sidebar:

        # =====================================================
        # PROJECT CONTROLS HUB
        # =====================================================

        st.markdown("## PROJECT CONTROLS HUB")
        st.caption("Design Management Intelligence")

        st.divider()

        # =====================================================
        # FRAMEWORKS
        # =====================================================

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

                if selected:
                    button_type = "primary"
                else:
                    button_type = "secondary"

                st.button(
                    asset,
                    key=f"asset_{framework}_{asset}",
                    use_container_width=True,
                    type=button_type,
                    on_click=_select_asset,
                    args=(framework, asset),
                )

            # Space between frameworks only
            if framework_index < len(FRAMEWORK_ORDER) - 1:
                st.markdown("")

        # =====================================================
        # NAVIGATION
        # =====================================================

        st.divider()

        st.markdown("**NAVIGATION**")

        for item in NAVIGATION_ITEMS:

            selected = (
                st.session_state.get("selected_navigation")
                == item
            )

            st.button(
                item,
                key=f"navigation_{item}",
                use_container_width=True,
                type="primary" if selected else "secondary",
                on_click=_select_navigation,
                args=(item,),
            )


# ============================================================
# ASSET SELECTION
# ============================================================

def _select_asset(framework, asset):

    st.session_state.selected_framework = framework
    st.session_state.selected_asset = asset
    st.session_state.selected_navigation = "Overview"


# ============================================================
# NAVIGATION SELECTION
# ============================================================

def _select_navigation(item):

    st.session_state.selected_navigation = item