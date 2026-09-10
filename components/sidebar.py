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
    ("Communications", "▱"),
    ("Documents", "□"),
    ("Intelligence", "◈"),
    ("Reports", "▥"),
    ("Settings", "⚙"),
]


# ============================================================
# SIDEBAR
# ============================================================

def render_sidebar():

    with st.sidebar:

        # ====================================================
        # SIDEBAR STYLING
        # ====================================================

        st.markdown(
            """
            <style>

            /* ------------------------------------------------
               SIDEBAR SIZE
               ------------------------------------------------ */

            section[data-testid="stSidebar"] {
                background-color: #071a3a !important;
                border-right: 1px solid #1b3b68 !important;
            }

            section[data-testid="stSidebar"] > div {
                padding: 18px 14px 15px 16px !important;
            }


            /* ------------------------------------------------
               REMOVE STREAMLIT BUTTON GAPS / OVERLAP
               ------------------------------------------------ */

            section[data-testid="stSidebar"] div.stButton {
                width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
            }

            section[data-testid="stSidebar"] div.stButton > button {
                width: 100% !important;

                min-height: 36px !important;
                height: auto !important;

                margin: 1px 0 !important;
                padding: 7px 9px !important;

                border-radius: 6px !important;

                display: flex !important;
                align-items: center !important;
                justify-content: flex-start !important;

                text-align: left !important;

                box-shadow: none !important;

                font-size: 13px !important;
                line-height: 18px !important;
            }


            /* ------------------------------------------------
               BUTTON CONTENT - FORCE LEFT ALIGNMENT
               ------------------------------------------------ */

            section[data-testid="stSidebar"]
            div.stButton > button > div {
                width: 100% !important;

                display: flex !important;
                align-items: center !important;
                justify-content: flex-start !important;

                text-align: left !important;
            }

            section[data-testid="stSidebar"]
            div.stButton > button p {
                width: 100% !important;

                margin: 0 !important;
                padding: 0 !important;

                text-align: left !important;
                line-height: 18px !important;
            }


            /* ------------------------------------------------
               NORMAL BUTTON
               ------------------------------------------------ */

            section[data-testid="stSidebar"]
            div.stButton > button[kind="secondary"] {
                background: transparent !important;
                border: 1px solid transparent !important;
                color: #c5d3e8 !important;
            }

            section[data-testid="stSidebar"]
            div.stButton > button[kind="secondary"]:hover {
                background: #102d5b !important;
                color: #ffffff !important;
            }


            /* ------------------------------------------------
               SELECTED BUTTON
               ------------------------------------------------ */

            section[data-testid="stSidebar"]
            div.stButton > button[kind="primary"] {
                background: #123f91 !important;
                border: 1px solid #2559ad !important;
                color: #ffffff !important;
            }


            /* ------------------------------------------------
               DIVIDER
               ------------------------------------------------ */

            section[data-testid="stSidebar"] hr {
                border: 0 !important;
                border-top: 1px solid #1d416e !important;
                margin: 14px 0 !important;
            }


            /* ------------------------------------------------
               HUB TITLE
               ------------------------------------------------ */

            .hub-title {
                color: #f5f7fc;
                font-size: 19px;
                font-weight: 700;
                line-height: 22px;
                margin: 0;
                padding: 0;
                text-align: left;
            }

            .hub-subtitle {
                color: #91a8cb;
                font-size: 11px;
                line-height: 16px;
                margin-top: 4px;
                text-align: left;
            }


            /* ------------------------------------------------
               SECTION TITLE
               ------------------------------------------------ */

            .section-title {
                color: #9eb4d5;
                font-size: 11px;
                font-weight: 600;
                letter-spacing: 0.5px;
                margin: 0 0 6px 0;
                text-align: left;
            }


            /* ------------------------------------------------
               FRAMEWORK NAME
               ------------------------------------------------ */

            .framework-title {
                color: #dce6f6;
                font-size: 12px;
                font-weight: 600;
                line-height: 18px;

                margin: 7px 0 3px 0;
                padding: 0;

                text-align: left;
            }


            /* ------------------------------------------------
               USER AREA
               ------------------------------------------------ */

            .user-area {
                border-top: 1px solid #1d416e;
                margin-top: 15px;
                padding-top: 12px;

                display: flex;
                align-items: center;
                text-align: left;
            }

            .user-avatar {
                width: 38px;
                height: 38px;

                flex-shrink: 0;

                border-radius: 50%;
                background: #19365e;

                color: #e5edf9;

                display: flex;
                align-items: center;
                justify-content: center;

                font-size: 12px;
                font-weight: 600;

                margin-right: 10px;
            }

            .user-name {
                color: #e6edf8;
                font-size: 13px;
                line-height: 17px;
                text-align: left;
            }

            .user-role {
                color: #8fa6c8;
                font-size: 11px;
                line-height: 15px;
                text-align: left;
            }

            </style>
            """,
            unsafe_allow_html=True,
        )


        # ====================================================
        # HEADER
        # ====================================================

        st.markdown(
            '<div class="hub-title">PROJECT CONTROLS HUB</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="hub-subtitle">Design Management Intelligence</div>',
            unsafe_allow_html=True,
        )

        st.divider()


        # ====================================================
        # FRAMEWORKS
        # ====================================================

        st.markdown(
            '<div class="section-title">FRAMEWORKS</div>',
            unsafe_allow_html=True,
        )


        for framework_index, framework in enumerate(FRAMEWORK_ORDER):

            if framework not in FRAMEWORKS:
                continue


            # -----------------------------------------------
            # FRAMEWORK NAME
            # -----------------------------------------------

            st.markdown(
                f'<div class="framework-title">{framework}</div>',
                unsafe_allow_html=True,
            )


            # -----------------------------------------------
            # PROJECTS
            # -----------------------------------------------

            for asset in FRAMEWORKS[framework]:

                selected = (
                    st.session_state.get("selected_framework")
                    == framework
                    and
                    st.session_state.get("selected_asset")
                    == asset
                )


                # Circle

                circle = "●" if selected else "○"

                label = f"{circle}  {asset}"


                st.button(
                    label,
                    key=f"asset_{framework}_{asset}",
                    use_container_width=True,
                    type="primary" if selected else "secondary",
                    on_click=_select_asset,
                    args=(framework, asset),
                )


            # -----------------------------------------------
            # FRAMEWORK DIVIDER
            # -----------------------------------------------

            if framework_index < len(FRAMEWORK_ORDER) - 1:
                st.divider()


        # ====================================================
        # NAVIGATION
        # ====================================================

        st.divider()

        st.markdown(
            '<div class="section-title">NAVIGATION</div>',
            unsafe_allow_html=True,
        )


        for item, icon in NAVIGATION_ITEMS:

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


        # ====================================================
        # USER
        # ====================================================

        st.markdown(
            """
            <div class="user-area">

                <div class="user-avatar">
                    JS
                </div>

                <div>
                    <div class="user-name">
                        John Smith
                    </div>

                    <div class="user-role">
                        Design Manager
                    </div>
                </div>

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