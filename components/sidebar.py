import streamlit as st

from config.frameworks import FRAMEWORKS


# ============================================================
# CONFIGURATION
# ============================================================

FRAMEWORK_ORDER = [
    "UU Enterprise Framework",
    "UU DD&B Framework",
]

NAVIGATION_ITEMS = [
    ("Overview", "⌂"),
    ("Programme", "▤"),
    ("Delivery & Programme", "▱"),
    ("Communications", "◌"),
    ("Documents", "□"),
    ("Intelligence", "✦"),
    ("Reports", "▥"),
    ("Settings", "⚙"),
]


# ============================================================
# SIDEBAR STYLE
# ============================================================

def _sidebar_css():

    st.markdown(
        """
        <style>

        /* =====================================================
           SIDEBAR
           ===================================================== */

        section[data-testid="stSidebar"] {
            background: #071a35 !important;
        }

        section[data-testid="stSidebar"] > div {
            padding: 12px !important;
        }


        /* =====================================================
           CARD
           ===================================================== */

        .pc-card {
            background: #0b2345;
            border: 1px solid #23466f;
            border-radius: 8px;

            padding: 10px;

            margin-bottom: 9px;

            width: 100%;
        }


        /* =====================================================
           CARD TITLE
           ===================================================== */

        .pc-card-title {
            color: #e7eef9;

            font-size: 12px;
            font-weight: 600;

            line-height: 16px;

            padding-bottom: 7px;
            margin-bottom: 5px;

            border-bottom: 1px solid #23466f;

            text-align: left;
        }


        /* =====================================================
           HUB CARD
           ===================================================== */

        .pc-hub-title {
            color: #ffffff;

            font-size: 16px;
            font-weight: 700;

            line-height: 19px;

            text-align: left;
        }

        .pc-hub-subtitle {
            color: #91a9cb;

            font-size: 10px;

            line-height: 14px;

            margin-top: 3px;

            text-align: left;
        }


        /* =====================================================
           BUTTONS
           ===================================================== */

        section[data-testid="stSidebar"] .stButton {
            width: 100%;
            margin: 0 !important;
            padding: 0 !important;
        }

        section[data-testid="stSidebar"] .stButton > button {

            width: 100% !important;

            min-height: 29px !important;
            height: 29px !important;

            margin: 1px 0 !important;

            padding: 3px 7px !important;

            border-radius: 5px !important;

            background: transparent !important;

            border: 1px solid transparent !important;

            color: #c5d3e7 !important;

            font-size: 12px !important;

            line-height: 16px !important;

            text-align: left !important;

            justify-content: flex-start !important;

            box-shadow: none !important;
        }

        section[data-testid="stSidebar"]
        .stButton > button:hover {

            background: #12315b !important;

            color: #ffffff !important;

            border-color: #234e80 !important;
        }

        section[data-testid="stSidebar"]
        .stButton > button > div {

            width: 100% !important;

            justify-content: flex-start !important;

            text-align: left !important;
        }

        section[data-testid="stSidebar"]
        .stButton > button p {

            margin: 0 !important;
            padding: 0 !important;

            text-align: left !important;
        }


        /* =====================================================
           PROJECT INDENT
           ===================================================== */

        .pc-project {
            padding-left: 4px;
        }


        /* =====================================================
           USER
           ===================================================== */

        .pc-user {
            color: #e5edf8;
            font-size: 12px;
            font-weight: 600;
        }

        .pc-role {
            color: #879fc0;
            font-size: 10px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# SIDEBAR
# ============================================================

def render_sidebar():

    _sidebar_css()

    with st.sidebar:

        # ====================================================
        # PROJECT CONTROLS HUB CARD
        # ====================================================

        st.markdown(
            """
            <div class="pc-card">
                <div class="pc-hub-title">
                    PROJECT CONTROLS HUB
                </div>

                <div class="pc-hub-subtitle">
                    Design Management Intelligence
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


        # ====================================================
        # ENTERPRISE CARD
        # ====================================================

        st.markdown(
            """
            <div class="pc-card">
                <div class="pc-card-title">
                    UU Enterprise Framework
                </div>
            """,
            unsafe_allow_html=True,
        )

        for asset in FRAMEWORKS.get(
            "UU Enterprise Framework",
            []
        ):

            st.markdown(
                '<div class="pc-project">',
                unsafe_allow_html=True,
            )

            st.button(
                f"○  {asset}",
                key=f"enterprise_{asset}",
                use_container_width=True,
                type="secondary",
                on_click=_select_asset,
                args=("UU Enterprise Framework", asset),
            )

            st.markdown(
                "</div>",
                unsafe_allow_html=True,
            )

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )


        # ====================================================
        # DD&B CARD
        # ====================================================

        st.markdown(
            """
            <div class="pc-card">
                <div class="pc-card-title">
                    UU DD&B Framework
                </div>
            """,
            unsafe_allow_html=True,
        )

        for asset in FRAMEWORKS.get(
            "UU DD&B Framework",
            []
        ):

            st.markdown(
                '<div class="pc-project">',
                unsafe_allow_html=True,
            )

            st.button(
                f"○  {asset}",
                key=f"ddb_{asset}",
                use_container_width=True,
                type="secondary",
                on_click=_select_asset,
                args=("UU DD&B Framework", asset),
            )

            st.markdown(
                "</div>",
                unsafe_allow_html=True,
            )

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )


        # ====================================================
        # NAVIGATION CARD
        # ====================================================

        st.markdown(
            """
            <div class="pc-card">
                <div class="pc-card-title">
                    NAVIGATION
                </div>
            """,
            unsafe_allow_html=True,
        )

        for item, icon in NAVIGATION_ITEMS:

            st.button(
                f"{icon}  {item}",
                key=f"navigation_{item}",
                use_container_width=True,
                type="secondary",
                on_click=_select_navigation,
                args=(item,),
            )

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )


        # ====================================================
        # USER
        # ====================================================

        st.markdown(
            """
            <div style="
                padding: 5px 4px;
                color: #e5edf8;
                font-size: 12px;
            ">
                <b>JS</b>&nbsp;&nbsp; John Smith
                <br>
                <span style="
                    color:#879fc0;
                    font-size:10px;
                    margin-left:28px;
                ">
                    Design Manager
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# PROJECT SELECTION
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