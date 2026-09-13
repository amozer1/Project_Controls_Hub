```python
import streamlit as st

from config.frameworks import FRAMEWORKS


# ==========================================================
# CONFIGURATION
# ==========================================================

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


# ==========================================================
# SESSION STATE
# ==========================================================

if "selected_framework" not in st.session_state:
    st.session_state.selected_framework = "UU Enterprise Framework"

if "selected_asset" not in st.session_state:
    st.session_state.selected_asset = "Pennington Flash"

if "selected_navigation" not in st.session_state:
    st.session_state.selected_navigation = "Overview"


# ==========================================================
# CALLBACKS
# ==========================================================

def select_asset(framework, asset):
    st.session_state.selected_framework = framework
    st.session_state.selected_asset = asset
    st.session_state.selected_navigation = "Overview"


def select_navigation(item):
    st.session_state.selected_navigation = item


def select_home():
    st.session_state.selected_navigation = "Overview"


# ==========================================================
# SIDEBAR
# ==========================================================

def render_sidebar():

    with st.sidebar:

        # --------------------------------------------------
        # BRAND
        # --------------------------------------------------

        st.image(
            "assets/logo.png",
            width=42,
        )

        st.button(
            "PROJECT CONTROLS HUB",
            key="project_controls_home",
            use_container_width=True,
            type="secondary",
            on_click=select_home,
        )

        st.caption(
            "Design Management Intelligence"
        )

        st.divider()


        # --------------------------------------------------
        # FRAMEWORKS
        # --------------------------------------------------

        st.caption("FRAMEWORKS")


        for framework_index, framework in enumerate(
            FRAMEWORK_ORDER
        ):

            framework_data = FRAMEWORKS.get(
                framework,
                {}
            )

            if isinstance(framework_data, dict):
                assets = framework_data.get(
                    "assets",
                    []
                )
            else:
                assets = framework_data


            if not assets:
                continue


            # Framework heading
            st.markdown(
                f"**{framework}**"
            )


            # Assets
            for asset in assets:

                selected = (
                    st.session_state.selected_framework
                    == framework
                    and
                    st.session_state.selected_asset
                    == asset
                )

                st.button(
                    asset,
                    key=f"asset_{framework}_{asset}",
                    use_container_width=True,
                    type=(
                        "primary"
                        if selected
                        else "secondary"
                    ),
                    on_click=select_asset,
                    args=(framework, asset),
                )


            # Separator
            if framework_index < len(
                FRAMEWORK_ORDER
            ) - 1:

                st.divider()


        # --------------------------------------------------
        # NAVIGATION
        # --------------------------------------------------

        st.divider()

        st.caption("NAVIGATION")


        for item in NAVIGATION_ITEMS:

            selected = (
                st.session_state.selected_navigation
                == item
            )

            st.button(
                item,
                key=f"navigation_{item}",
                use_container_width=True,
                type=(
                    "primary"
                    if selected
                    else "secondary"
                ),
                on_click=select_navigation,
                args=(item,),
            )

