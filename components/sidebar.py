import streamlit as st
from pathlib import Path

from config.frameworks import FRAMEWORKS


# ==========================================================
# NAVIGATION
# ==========================================================

NAVIGATION_ITEMS = [
    ("⌂", "Overview"),
    ("▣", "Programme"),
    ("⌁", "Delivery & Programme"),
    ("▱", "Communications"),
    ("□", "Documents"),
    ("▥", "Intelligence"),
    ("▦", "Reports"),
    ("⚙", "Settings"),
]


# ==========================================================
# FRAMEWORK ORDER
# ==========================================================

FRAMEWORK_ORDER = [
    "UU Enterprise Framework",
    "UU DD&B Framework",
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
# CSS
# ==========================================================

def load_sidebar_css():

    css = """
    <style>

    /* ======================================================
       SIDEBAR
       ====================================================== */

    section[data-testid="stSidebar"] {

        width: 240px !important;
        min-width: 240px !important;
        max-width: 240px !important;

        background:
            linear-gradient(
                180deg,
                #06183d 0%,
                #041633 55%,
                #03132d 100%
            ) !important;

        border-right: 1px solid rgba(91, 145, 235, 0.22) !important;
    }


    section[data-testid="stSidebar"] > div {

        padding: 18px 14px 14px 14px !important;
    }


    /* Remove Streamlit's excessive vertical gaps */

    section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {

        gap: 0rem !important;
    }


    /* ======================================================
       HEADER
       ====================================================== */

    .pch-header {

        display: flex;
        align-items: center;

        gap: 10px;

        margin: 0 4px 20px 4px;
    }


    .pch-logo {

        width: 46px;
        height: 46px;

        object-fit: contain;

        flex-shrink: 0;
    }


    .pch-title {

        color: #f4f7ff;

        font-size: 17px;
        font-weight: 700;

        line-height: 19px;

        letter-spacing: -0.2px;
    }


    .pch-subtitle {

        color: #9bb4dd;

        font-size: 10px;

        line-height: 14px;

        margin-top: 3px;
    }


    /* ======================================================
       SECTION HEADINGS
       ====================================================== */

    .pch-section {

        display: flex;
        align-items: center;

        color: #9db9e8;

        font-size: 10px;
        font-weight: 700;

        letter-spacing: 0.9px;

        text-transform: uppercase;

        margin: 0 4px 9px 4px;
    }


    .pch-section-line {

        flex: 1;

        height: 1px;

        background: rgba(73, 130, 219, 0.38);

        margin-left: 10px;
    }


    /* ======================================================
       FRAMEWORK HEADINGS
       ====================================================== */

    .pch-framework {

        display: flex;
        align-items: center;

        height: 37px;

        padding: 0 10px;

        margin: 0 0 3px 0;

        border-radius: 7px;

        background:
            linear-gradient(
                90deg,
                rgba(21, 75, 158, 0.48),
                rgba(21, 75, 158, 0.20)
            );

        border: 1px solid rgba(66, 126, 222, 0.18);

        color: #c7dcff;

        font-size: 12px;
        font-weight: 650;
    }


    .pch-framework-arrow {

        color: #78b1ff;

        font-size: 14px;

        margin-right: 9px;
    }


    /* ======================================================
       BUTTON BASE
       ====================================================== */

    section[data-testid="stSidebar"] .stButton {

        margin: 0 !important;

        padding: 0 !important;
    }


    section[data-testid="stSidebar"] .stButton > button {

        width: 100% !important;

        height: 36px !important;

        min-height: 36px !important;

        margin: 0 !important;

        padding: 0 9px !important;

        border-radius: 6px !important;

        border: 1px solid transparent !important;

        background: transparent !important;

        color: #d7e2f6 !important;

        font-size: 12px !important;

        font-weight: 450 !important;

        text-align: left !important;

        box-shadow: none !important;

        transition:
            background 0.15s ease,
            border 0.15s ease;
    }


    /* Asset and navigation button content */

    section[data-testid="stSidebar"] .stButton > button p {

        font-size: 12px !important;

        line-height: 16px !important;
    }


    /* ======================================================
       NORMAL ROW
       ====================================================== */

    section[data-testid="stSidebar"]
    .stButton > button[kind="secondary"] {

        background: transparent !important;

        color: #d7e2f6 !important;
    }


    section[data-testid="stSidebar"]
    .stButton > button[kind="secondary"]:hover {

        background: rgba(53, 106, 194, 0.16) !important;

        border-color: rgba(76, 137, 231, 0.18) !important;

        color: #ffffff !important;
    }


    /* ======================================================
       SELECTED ROW
       ====================================================== */

    section[data-testid="stSidebar"]
    .stButton > button[kind="primary"] {

        background:
            linear-gradient(
                90deg,
                #1558c9 0%,
                #1049aa 100%
            ) !important;

        border: 1px solid rgba(87, 155, 255, 0.42) !important;

        color: #ffffff !important;

        box-shadow:
            inset 3px 0 0 #58a6ff !important;
    }


    section[data-testid="stSidebar"]
    .stButton > button[kind="primary"]:hover {

        background:
            linear-gradient(
                90deg,
                #1961d6 0%,
                #1552b8 100%
            ) !important;
    }


    /* ======================================================
       ASSET INDENTATION
       ====================================================== */

    .pch-asset-spacer {

        height: 2px;
    }


    /* ======================================================
       FRAMEWORK SEPARATOR
       ====================================================== */

    .pch-framework-separator {

        height: 1px;

        margin: 10px 4px 11px 4px;

        background: rgba(77, 127, 205, 0.25);
    }


    /* ======================================================
       NAVIGATION SPACING
       ====================================================== */

    .pch-navigation-start {

        height: 3px;
    }


    /* ======================================================
       FOOTER
       ====================================================== */

    .pch-footer {

        margin-top: 18px;

        padding-top: 12px;

        border-top: 1px solid rgba(77, 127, 205, 0.25);

        color: #8fa8cf;

        font-size: 10px;
    }

    </style>
    """

    st.markdown(css, unsafe_allow_html=True)


# ==========================================================
# SIDEBAR
# ==========================================================

def render_sidebar():

    load_sidebar_css()

    with st.sidebar:

        # ==================================================
        # HEADER
        # ==================================================

        logo_path = Path("assets/logo.png")

        if logo_path.exists():

            logo_html = f"""
                <img
                    src="data:image/png;base64,{_image_to_base64(logo_path)}"
                    class="pch-logo"
                >
            """

        else:

            logo_html = """
                <div class="pch-logo"></div>
            """


        st.markdown(
            f"""
            <div class="pch-header">

                {logo_html}

                <div>

                    <div class="pch-title">
                        PROJECT<br>
                        CONTROLS HUB
                    </div>

                    <div class="pch-subtitle">
                        Design Management Intelligence
                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


        # ==================================================
        # FRAMEWORKS
        # ==================================================

        st.markdown(
            """
            <div class="pch-section">
                FRAMEWORKS
                <div class="pch-section-line"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )


        for framework_index, framework in enumerate(FRAMEWORK_ORDER):

            assets = FRAMEWORKS.get(framework, [])

            if not assets:
                continue


            # ----------------------------------------------
            # Framework heading
            # ----------------------------------------------

            st.markdown(
                f"""
                <div class="pch-framework">
                    <span class="pch-framework-arrow">⌄</span>
                    <span>{framework}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )


            # ----------------------------------------------
            # Assets
            # ----------------------------------------------

            for asset in assets:

                selected = (
                    st.session_state.get("selected_framework")
                    == framework
                    and
                    st.session_state.get("selected_asset")
                    == asset
                )

                st.button(
                    f"▦   {asset}                         ›",
                    key=f"asset_{framework}_{asset}",
                    use_container_width=True,
                    type="primary" if selected else "secondary",
                    on_click=_select_asset,
                    args=(framework, asset),
                )


            # ----------------------------------------------
            # Framework separator
            # ----------------------------------------------

            if framework_index < len(FRAMEWORK_ORDER) - 1:

                st.markdown(
                    '<div class="pch-framework-separator"></div>',
                    unsafe_allow_html=True,
                )


        # ==================================================
        # NAVIGATION
        # ==================================================

        st.markdown(
            """
            <div class="pch-navigation-start"></div>

            <div class="pch-section">
                NAVIGATION
                <div class="pch-section-line"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )


        for item, icon in NAVIGATION_ITEMS:

            selected = (
                st.session_state.get("selected_navigation")
                == item
            )

            st.button(
                f"{icon}   {item}                         ›",
                key=f"navigation_{item}",
                use_container_width=True,
                type="primary" if selected else "secondary",
                on_click=_select_navigation,
                args=(item,),
            )


# ==========================================================
# LOGO HELPER
# ==========================================================

def _image_to_base64(path):

    import base64

    return base64.b64encode(
        path.read_bytes()
    ).decode()