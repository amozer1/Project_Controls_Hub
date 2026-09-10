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
        # SIDEBAR CSS
        # ====================================================

        st.markdown(
            """
            <style>

            /* =================================================
               SIDEBAR
               ================================================= */

            [data-testid="stSidebar"] {
                background-color: #071a3a !important;
            }

            [data-testid="stSidebar"] > div {
                padding: 16px 14px 14px 14px !important;
            }


            /* =================================================
               REMOVE DEFAULT BUTTON SPACING
               ================================================= */

            [data-testid="stSidebar"] .stButton {
                margin: 0 !important;
                padding: 0 !important;
            }

            [data-testid="stSidebar"] .stButton > button {
                width: 100% !important;

                min-height: 32px !important;
                height: 32px !important;

                margin: 1px 0 !important;
                padding: 4px 8px !important;

                display: flex !important;
                align-items: center !important;
                justify-content: flex-start !important;

                text-align: left !important;

                border-radius: 5px !important;

                font-size: 12px !important;
                line-height: 16px !important;

                box-shadow: none !important;
            }

            [data-testid="stSidebar"] .stButton > button > div {
                width: 100% !important;

                display: flex !important;
                justify-content: flex-start !important;
                align-items: center !important;

                text-align: left !important;
            }

            [data-testid="stSidebar"] .stButton > button p {
                margin: 0 !important;
                padding: 0 !important;

                width: 100% !important;

                text-align: left !important;
            }


            /* =================================================
               PROJECT BUTTONS
               ================================================= */

            .project-button button {
                background: transparent !important;
                border: 1px solid transparent !important;
                color: #c3d1e7 !important;
            }

            .project-button button:hover {
                background: #102b55 !important;
                color: #ffffff !important;
            }


            /* =================================================
               NAVIGATION BUTTONS
               ================================================= */

            .navigation-button button {
                background: transparent !important;
                border: 1px solid transparent !important;
                color: #c3d1e7 !important;
            }

            .navigation-button button:hover {
                background: #102b55 !important;
                color: #ffffff !important;
            }


            /* =================================================
               DIVIDERS
               ================================================= */

            [data-testid="stSidebar"] hr {
                border: none !important;
                border-top: 1px solid #1d3d68 !important;
                margin: 12px 0 !important;
            }


            /* =================================================
               HUB HEADER
               ================================================= */

            .hub-header {
                background: #123b82;
                border: 1px solid #2455a0;
                border-radius: 6px;

                padding: 9px 10px;

                margin-bottom: 12px;
            }

            .hub-title {
                color: #ffffff;
                font-size: 15px;
                font-weight: 700;

                line-height: 18px;

                text-align: left;
            }

            .hub-subtitle {
                color: #a9bee0;
                font-size: 10px;

                line-height: 14px;

                margin-top: 3px;

                text-align: left;
            }


            /* =================================================
               FRAMEWORK HEADERS
               ================================================= */

            .framework-header {
                background: #0d2b5b;
                border-left: 3px solid #3e83df;

                border-radius: 4px;

                padding: 6px 8px;

                margin: 7px 0 5px 0;

                color: #dce8fa;

                font-size: 12px;
                font-weight: 600;

                line-height: 16px;

                text-align: left;
            }


            /* =================================================
               NAVIGATION HEADER
               ================================================= */

            .navigation-header {
                background: #0d2b5b;
                border-left: 3px solid #3e83df;

                border-radius: 4px;

                padding: 6px 8px;

                margin: 0 0 5px 0;

                color: #dce8fa;

                font-size: 12px;
                font-weight: 600;

                line-height: 16px;

                text-align: left;
            }


            /* =================================================
               PROJECT INDENT
               ================================================= */

            .project-indent {
                margin-left: 8px;
            }


            /* =================================================
               USER PROFILE
               ================================================= */

            .user-name {
                color: #e5edf9;
                font-size: 12px;
                font-weight: 600;
                line-height: 16px;
            }

            .user-role {
                color: #8fa7ca;
                font-size: 10px;
                line-height: 14px;
            }

            </style>
            """,
            unsafe_allow_html=True,
        )


        # ====================================================
        # PROJECT CONTROLS HUB
        # ====================================================

        st.markdown(
            """
            <div class="hub-header">
                <div class="hub-title">
                    PROJECT CONTROLS HUB
                </div>
                <div class="hub-subtitle">
                    Design Management Intelligence
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


        # ====================================================
        # FRAMEWORKS
        # ====================================================

        st.markdown(
            """
            <div class="framework-header">
                UU Enterprise Framework
            </div>
            """,
            unsafe_allow_html=True,
        )


        # ----------------------------------------------------
        # UU ENTERPRISE PROJECTS
        # ----------------------------------------------------

        enterprise_projects = FRAMEWORKS.get(
            "UU Enterprise Framework",
            []
        )

        for asset in enterprise_projects:

            st.markdown(
                '<div class="project-indent">',
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


        # ====================================================
        # DD&B FRAMEWORK
        # ====================================================

        st.markdown(
            """
            <div class="framework-header">
                UU DD&B Framework
            </div>
            """,
            unsafe_allow_html=True,
        )


        # ----------------------------------------------------
        # DD&B PROJECTS
        # ----------------------------------------------------

        ddb_projects = FRAMEWORKS.get(
            "UU DD&B Framework",
            []
        )

        for asset in ddb_projects:

            st.markdown(
                '<div class="project-indent">',
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


        # ====================================================
        # NAVIGATION
        # ====================================================

        st.divider()

        st.markdown(
            """
            <div class="navigation-header">
                NAVIGATION
            </div>
            """,
            unsafe_allow_html=True,
        )


        for item, icon in NAVIGATION_ITEMS:

            st.markdown(
                '<div class="project-indent">',
                unsafe_allow_html=True,
            )

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

        st.divider()

        user_col1, user_col2 = st.columns(
            [1, 3],
            gap="small",
        )

        with user_col1:
            st.markdown(
                "### JS"
            )

        with user_col2:
            st.markdown(
                '<div class="user-name">John Smith</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                '<div class="user-role">Design Manager</div>',
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