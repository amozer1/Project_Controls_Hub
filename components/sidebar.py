```python
import streamlit as st

from config.frameworks import FRAMEWORKS


# ==========================================================
# FRAMEWORK ORDER
# ==========================================================

FRAMEWORK_ORDER = [
    "UU Enterprise Framework",
    "UU DD&B Framework",
]


# ==========================================================
# NAVIGATION
# ==========================================================

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
    st.session_state.selected_framework = (
        "UU Enterprise Framework"
    )

if "selected_asset" not in st.session_state:
    st.session_state.selected_asset = (
        "Pennington Flash"
    )

if "selected_navigation" not in st.session_state:
    st.session_state.selected_navigation = (
        "Overview"
    )


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

        # ==================================================
        # BRAND
        # ==================================================

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


        # ==================================================
        # FRAMEWORKS
        # ==================================================

        st.caption("FRAMEWORKS")


        for framework_index, framework in enumerate(
            FRAMEWORK_ORDER
        ):

            # ------------------------------------------------
            # Framework data
            # ------------------------------------------------

            framework_data = FRAMEWORKS.get(
                framework,
                {}
            )


            # ------------------------------------------------
            # Support dictionary or list structure
            # ------------------------------------------------

            if isinstance(
                framework_data,
                dict
            ):

                assets = framework_data.get(
                    "assets",
                    []
                )

            else:

                assets = framework_data


            # ------------------------------------------------
            # Skip empty frameworks
            # ------------------------------------------------

            if not assets:
                continue


            # ------------------------------------------------
            # Framework heading
            # ------------------------------------------------

            st.markdown(
                f"**{framework}**"
            )


            # ------------------------------------------------
            # Asset buttons
            # ------------------------------------------------

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

                    key=(
                        f"asset_"
                        f"{framework}_"
                        f"{asset}"
                    ),

                    use_container_width=True,

                    type=(
                        "primary"
                        if selected
                        else "secondary"
                    ),

                    on_click=select_asset,

                    args=(
                        framework,
                        asset,
                    ),
                )


            # ------------------------------------------------
            # Separator between frameworks
            # ------------------------------------------------

            if framework_index == 0:

                st.divider()


        # ==================================================
        # NAVIGATION
        # ==================================================

        st.divider()

        st.caption("NAVIGATION")


        # --------------------------------------------------
        # Navigation buttons
        # --------------------------------------------------

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
```
