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
# CALLBACKS
# ==========================================================

def _select_asset(framework, asset):

    st.session_state.selected_framework = framework
    st.session_state.selected_asset = asset
    st.session_state.selected_navigation = "Overview"


def _select_navigation(item):

    st.session_state.selected_navigation = item


# ==========================================================
# SIDEBAR CSS
# ==========================================================

def load_sidebar_css():

    st.markdown(
        """
        <style>

        /* ==================================================
           SIDEBAR
           ================================================== */

        section[data-testid="stSidebar"] {
            width: 240px !important;
            min-width: 240px !important;
            max-width: 240px !important;

            background:
                linear-gradient(
                    180deg,
                    #061a40 0%,
                    #041633 100%
                ) !important;

            border-right:
                1px solid rgba(76, 135, 220, 0.25) !important;
        }


        /* ==================================================
           SIDEBAR CONTAINER
           ================================================== */

        section[data-testid="stSidebar"] > div {
            padding: 16px 12px 12px 12px !important;
        }


        section[data-testid="stSidebar"]
        [data-testid="stVerticalBlock"] {
            gap: 0 !important;
        }


        /* ==================================================
           HEADER
           ================================================== */

        .pch-header {
            margin: 0 5px 20px 5px;
            padding-bottom: 16px;

            border-bottom:
                1px solid rgba(84, 137, 214, 0.28);
        }


        .pch-title {
            color: #ffffff;

            font-size: 17px;
            font-weight: 700;

            line-height: 19px;

            margin: 0;
        }


        .pch-subtitle {
            color: #9bb5df;

            font-size: 10px;
            line-height: 14px;

            margin-top: 4px;
        }


        /* ==================================================
           SECTION HEADINGS
           ================================================== */

        .pch-section {
            color: #9fb8df;

            font-size: 10px;
            font-weight: 700;

            letter-spacing: 0.9px;

            margin: 0 5px 8px 5px;

            text-transform: uppercase;
        }


        /* ==================================================
           FRAMEWORK HEADER
           ================================================== */

        .pch-framework {
            height: 34px;

            display: flex;
            align-items: center;

            padding: 0 9px;

            margin: 0 0 2px 0;

            border-radius: 6px;

            background:
                rgba(31, 82, 166, 0.25);

            color: #d5e3fb;

            font-size: 12px;
            font-weight: 600;
        }


        .pch-framework-arrow {
            color: #72aaff;

            margin-right: 8px;

            font-size: 13px;
        }


        /* ==================================================
           BUTTON CONTAINER
           ================================================== */

        section[data-testid="stSidebar"]
        .stButton {
            margin: 0 !important;
            padding: 0 !important;
        }


        /* ==================================================
           BUTTON
           ================================================== */

        section[data-testid="stSidebar"]
        .stButton > button {

            height: 34px !important;
            min-height: 34px !important;

            width: 100% !important;

            margin: 0 !important;

            padding:
                0 9px 0 17px !important;

            border-radius: 5px !important;

            border:
                1px solid transparent !important;

            background:
                transparent !important;

            color:
                #d5e0f2 !important;

            font-size:
                12px !important;

            font-weight:
                450 !important;

            text-align:
                left !important;

            justify-content:
                flex-start !important;

            box-shadow:
                none !important;
        }


        /* ==================================================
           BUTTON TEXT
           ================================================== */

        section[data-testid="stSidebar"]
        .stButton > button p {

            font-size:
                12px !important;

            margin:
                0 !important;

            text-align:
                left !important;
        }


        /* ==================================================
           HOVER
           ================================================== */

        section[data-testid="stSidebar"]
        .stButton > button[kind="secondary"]:hover {

            background:
                rgba(45, 103, 204, 0.18) !important;

            border:
                1px solid rgba(79, 139, 226, 0.16) !important;

            color:
                #ffffff !important;
        }


        /* ==================================================
           SELECTED
           ================================================== */

        section[data-testid="stSidebar"]
        .stButton > button[kind="primary"] {

            background:
                linear-gradient(
                    90deg,
                    #1556bd 0%,
                    #10469c 100%
                ) !important;

            border:
                1px solid rgba(91, 157, 255, 0.38) !important;

            color:
                #ffffff !important;

            box-shadow:
                inset 3px 0 0 #5ba5ff !important;
        }


        /* ==================================================
           SEPARATOR
           ================================================== */

        .pch-separator {

            height: 1px;

            margin:
                9px 5px 10px 5px;

            background:
                rgba(79, 133, 211, 0.28);
        }


        /* ==================================================
           NAVIGATION SPACING
           ================================================== */

        .pch-navigation-space {
            height: 4px;
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
        # HEADER
        # ==================================================

        header_col1, header_col2 = st.columns(
            [0.72, 2.8],
            gap="small",
        )

        with header_col1:

            st.image(
                "assets/logo.png",
                width=44,
            )

        with header_col2:

            st.markdown(
                """
                <div class="pch-header">

                    <div class="pch-title">
                        PROJECT<br>
                        CONTROLS HUB
                    </div>

                    <div class="pch-subtitle">
                        Design Management Intelligence
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


        # ==================================================
        # FRAMEWORKS
        # ==================================================

        st.markdown(
            '<div class="pch-section">FRAMEWORKS</div>',
            unsafe_allow_html=True,
        )


        for framework_index, framework in enumerate(
            FRAMEWORK_ORDER
        ):

            # ------------------------------------------------
            # Get framework data
            # ------------------------------------------------

            framework_data = FRAMEWORKS.get(
                framework,
                {}
            )


            # ------------------------------------------------
            # Get assets
            # ------------------------------------------------

            if isinstance(framework_data, dict):

                assets = framework_data.get(
                    "assets",
                    []
                )

            else:

                assets = framework_data


            # ------------------------------------------------
            # Skip empty framework
            # ------------------------------------------------

            if not assets:
                continue


            # ------------------------------------------------
            # Framework heading
            # ------------------------------------------------

            st.markdown(
                f"""
                <div class="pch-framework">

                    <span class="pch-framework-arrow">
                        ⌄
                    </span>

                    <span>
                        {framework}
                    </span>

                </div>
                """,
                unsafe_allow_html=True,
            )


            # ------------------------------------------------
            # Asset buttons
            # ------------------------------------------------

            for asset in assets:

                selected = (
                    st.session_state.get(
                        "selected_framework"
                    ) == framework
                    and
                    st.session_state.get(
                        "selected_asset"
                    ) == asset
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


            # ------------------------------------------------
            # Framework separator
            # ------------------------------------------------

            if framework_index < len(
                FRAMEWORK_ORDER
            ) - 1:

                st.markdown(
                    '<div class="pch-separator"></div>',
                    unsafe_allow_html=True,
                )


        # ==================================================
        # NAVIGATION SPACE
        # ==================================================

        st.markdown(
            '<div class="pch-navigation-space"></div>',
            unsafe_allow_html=True,
        )


        # ==================================================
        # NAVIGATION HEADING
        # ==================================================

        st.markdown(
            '<div class="pch-section">NAVIGATION</div>',
            unsafe_allow_html=True,
        )


        # ==================================================
        # NAVIGATION BUTTONS
        # ==================================================

        for item in NAVIGATION_ITEMS:

            selected = (
                st.session_state.get(
                    "selected_navigation"
                ) == item
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