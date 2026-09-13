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
    st.session_state.selected_framework = "UU Enterprise Framework"

if "selected_asset" not in st.session_state:
    st.session_state.selected_asset = "Pennington Flash"

if "selected_navigation" not in st.session_state:
    st.session_state.selected_navigation = "Overview"


# ==========================================================
# CALLBACKS
# ==========================================================

def _select_asset(framework, asset):

    st.session_state.selected_framework = framework
    st.session_state.selected_asset = asset
    st.session_state.selected_navigation = "Overview"


def _select_navigation(item):

    st.session_state.selected_navigation = item


def _select_home():

    st.session_state.selected_navigation = "Overview"


# ==========================================================
# SIDEBAR STYLE
# ==========================================================

def load_sidebar_css():

    st.markdown(
        """
        <style>

        /* Sidebar width */
        section[data-testid="stSidebar"] {
            width: 250px !important;
            min-width: 250px !important;
            max-width: 250px !important;
            background: #061832 !important;
            border-right: 1px solid #17345c !important;
        }

        /* Sidebar padding */
        section[data-testid="stSidebar"] > div {
            padding: 18px 14px 14px 14px !important;
        }

        /* Remove excessive widget gaps */
        section[data-testid="stSidebar"]
        [data-testid="stVerticalBlock"] {
            gap: 0.15rem !important;
        }

        /* All buttons */
        section[data-testid="stSidebar"] .stButton {
            margin: 0 !important;
            padding: 0 !important;
        }

        section[data-testid="stSidebar"] .stButton > button {
            width: 100% !important;
            min-height: 34px !important;
            height: 34px !important;

            margin: 1px 0 !important;
            padding: 0 11px !important;

            border-radius: 5px !important;
            border: 1px solid transparent !important;

            background: transparent !important;

            color: #c8d5e8 !important;

            font-size: 12px !important;
            font-weight: 450 !important;

            text-align: left !important;
            justify-content: flex-start !important;

            box-shadow: none !important;
        }

        /* Button text */
        section[data-testid="stSidebar"]
        .stButton > button p {
            width: 100% !important;
            margin: 0 !important;

            text-align: left !important;
            font-size: 12px !important;
        }

        /* Hover */
        section[data-testid="stSidebar"]
        .stButton > button:hover {
            background: #102b50 !important;
            border: 1px solid #1d416e !important;
            color: #ffffff !important;
        }

        /* Selected */
        section[data-testid="stSidebar"]
        .stButton > button[kind="primary"] {
            background: #1557a6 !important;
            border: 1px solid #2c70c4 !important;
            color: #ffffff !important;
            font-weight: 600 !important;
        }

        /* Section headings */
        section[data-testid="stSidebar"] .stCaption {
            color: #7894b8 !important;
            font-size: 10px !important;
        }

        /* Divider */
        section[data-testid="stSidebar"] hr {
            margin: 10px 0 !important;
            border-color: #17345c !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# RENDER SIDEBAR
# ==========================================================

def render_sidebar():

    load_sidebar_css()

    with st.sidebar:

        # ==================================================
        # BRAND
        # ==================================================

        st.image(
            "assets/logo.png",
            width=42,
        )

        if st.button(
            "PROJECT CONTROLS HUB",
            key="project_controls_home",
            use_container_width=True,
            type="secondary",
            on_click=_select_home,
        ):
            pass

        st.caption(
            "Design Management Intelligence"
        )

        st.divider()


        # ==================================================
        # FRAMEWORKS
        # ==================================================

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


            # ----------------------------------------------
            # Framework name
            # ----------------------------------------------

            st.markdown(
                f"**{framework}**"
            )


            # ----------------------------------------------
            # Assets
            # ----------------------------------------------

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

                    on_click=_select_asset,

                    args=(
                        framework,
                        asset,
                    ),
                )


            # ----------------------------------------------
            # Framework separator
            # ----------------------------------------------

            if framework_index < len(
                FRAMEWORK_ORDER
            ) - 1:

                st.divider()


        # ==================================================
        # NAVIGATION
        # ==================================================

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

                on_click=_select_navigation,

                args=(item,),
            )