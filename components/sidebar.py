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

            /* ================================================
               SIDEBAR
               ================================================ */

            [data-testid="stSidebar"] {
                background: #061936 !important;
            }

            [data-testid="stSidebar"] > div {
                padding: 14px 12px 14px 12px !important;
            }


            /* ================================================
               CARDS
               ================================================ */

            [data-testid="stSidebar"] div[data-testid="stVerticalBlockBorderWrapper"] {
                background: #081f42;
                border: 1px solid #1c3d6b;
                border-radius: 8px;
                padding: 10px 10px 9px 10px;
                margin-bottom: 10px;
            }


            /* ================================================
               BUTTONS
               ================================================ */

            [data-testid="stSidebar"] .stButton {
                margin: 0 !important;
                padding: 0 !important;
            }

            [data-testid="stSidebar"] .stButton > button {
                width: 100% !important;
                min-height: 32px !important;

                margin: 2px 0 !important;
                padding: 5px 7px !important;

                border-radius: 5px !important;

                display: flex !important;
                align-items: center !important;
                justify-content: flex-start !important;

                text-align: left !important;

                font-size: 12px !important;
                line-height: 17px !important;

                box-shadow: none !important;
            }

            [data-testid="stSidebar"] .stButton > button > div {
                width: 100% !important;
                display: flex !important;
                justify-content: flex-start !important;
                text-align: left !important;
            }

            [data-testid="stSidebar"] .stButton > button p {
                margin: 0 !important;
                padding: 0 !important;
                text-align: left !important;
            }


            /* ================================================
               PROJECT BUTTONS
               ================================================ */

            .project-card button {
                background: transparent !important;
                border: 1px solid transparent !important;
                color: #c4d2e8 !important;
            }

            .project-card button:hover {
                background: #12315d !important;
                color: #ffffff !important;
            }


            /* ================================================
               NAVIGATION BUTTONS
               ================================================ */

            .nav-card button {
                background: transparent !important;
                border: 1px solid transparent !important;
                color: #c4d2e8 !important;
            }

            .nav-card button:hover {
                background: #12315d !important;
                color: #ffffff !important;
            }


            /* ================================================
               CARD HEADINGS
               ================================================ */

            .card-heading {
                color: #dce8f8;
                font-size: 12px;
                font-weight: 600;
                line-height: 17px;

                padding-bottom: 6px;
                margin-bottom: 4px;

                border-bottom: 1px solid #21466f;
            }


            /* ================================================
               HUB CARD
               ================================================ */

            .hub-title {
                color: #ffffff;
                font-size: 16px;
                font-weight: 700;
                line-height: 20px;
            }

            .hub-subtitle {
                color: #9eb3d2;
                font-size: 10px;
                line-height: 14px;
                margin-top: 3px;
            }


            /* ================================================
               USER
               ================================================ */

            .user-name {
                color: #e4ecf8;
                font-size: 12px;
                font-weight: 600;
                line-height: 16px;
            }

            .user-role {
                color: #8da5c7;
                font-size: 10px;
                line-height: 14px;
            }

            </style>
            """,
            unsafe_allow_html=True,
        )


        # ====================================================
        # PROJECT CONTROLS HUB CARD
        # ====================================================

        with st.container(border=True):

            st.markdown(
                '<div class="hub-title">PROJECT CONTROLS HUB</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                '<div class="hub-subtitle">Design Management Intelligence</div>',
                unsafe_allow_html=True,
            )


        # ====================================================
        # UU ENTERPRISE FRAMEWORK CARD
        # ====================================================

        with st.container(border=True):

            st.markdown(
                '<div class="card-heading">UU Enterprise Framework</div>',
                unsafe_allow_html=True,
            )

            projects = FRAMEWORKS.get(
                "UU Enterprise Framework",
                []
            )

            for asset in projects:

                st.markdown(
                    '<div class="project-card">',
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
                    '</div>',
                    unsafe_allow_html=True,
                )


        # ====================================================
        # UU DD&B FRAMEWORK CARD
        # ====================================================

        with st.container(border=True):

            st.markdown(
                '<div class="card-heading">UU DD&B Framework</div>',
                unsafe_allow_html=True,
            )

            projects = FRAMEWORKS.get(
                "UU DD&B Framework",
                []
            )

            for asset in projects:

                st.markdown(
                    '<div class="project-card">',
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
                    '</div>',
                    unsafe_allow_html=True,
                )


        # ====================================================
        # NAVIGATION CARD
        # ====================================================

        with st.container(border=True):

            st.markdown(
                '<div class="card-heading">NAVIGATION</div>',
                unsafe_allow_html=True,
            )

            for item, icon in NAVIGATION_ITEMS:

                st.markdown(
                    '<div class="nav-card">',
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
                    '</div>',
                    unsafe_allow_html=True,
                )


        # ====================================================
        # USER PROFILE
        # ====================================================

        user_col1, user_col2 = st.columns(
            [1, 3],
            gap="small",
        )

        with user_col1:

            st.markdown(
                """
                <div style="
                    width:36px;
                    height:36px;
                    border-radius:50%;
                    background:#19365e;
                    color:#e5edf9;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-size:12px;
                    font-weight:600;
                ">
                    JS
                </div>
                """,
                unsafe_allow_html=True,
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