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
    ("Programme", "▦"),
    ("Delivery & Programme", "▱"),
    ("Communications", "◌"),
    ("Documents", "□"),
    ("Intelligence", "✦"),
    ("Reports", "▥"),
    ("Settings", "⚙"),
]


# ============================================================
# SIDEBAR
# ============================================================

def render_sidebar():

    # --------------------------------------------------------
    # CSS
    # --------------------------------------------------------

    st.markdown(
        """
        <style>

        /* ====================================================
           SIDEBAR
           ==================================================== */

        section[data-testid="stSidebar"] {
            background: #071a35 !important;
        }

        section[data-testid="stSidebar"] > div {
            padding: 12px 10px !important;
        }


        /* ====================================================
           ALL SIDEBAR BUTTONS
           ==================================================== */

        section[data-testid="stSidebar"] .stButton {
            margin: 0 !important;
            padding: 0 !important;
        }

        section[data-testid="stSidebar"] .stButton button {
            width: 100% !important;
            min-height: 30px !important;
            height: 30px !important;

            padding: 4px 8px !important;
            margin: 1px 0 !important;

            border-radius: 5px !important;

            display: flex !important;
            align-items: center !important;
            justify-content: flex-start !important;

            text-align: left !important;

            font-size: 12px !important;
            line-height: 16px !important;

            box-shadow: none !important;
        }

        section[data-testid="stSidebar"] .stButton button > div {
            width: 100% !important;
            display: flex !important;
            justify-content: flex-start !important;
        }

        section[data-testid="stSidebar"] .stButton button p {
            margin: 0 !important;
            padding: 0 !important;
            text-align: left !important;
        }


        /* ====================================================
           NORMAL ROW
           ==================================================== */

        section[data-testid="stSidebar"]
        .stButton button[kind="secondary"] {
            background: transparent !important;
            border: 1px solid transparent !important;
            color: #bdcce1 !important;
        }

        section[data-testid="stSidebar"]
        .stButton button[kind="secondary"]:hover {
            background: #102d54 !important;
            color: #ffffff !important;
        }


        /* ====================================================
           CARD
           ==================================================== */

        .sidebar-card {
            background: #0b2347;
            border: 1px solid #193d6a;
            border-radius: 8px;

            padding: 9px 8px 8px 8px;

            margin-bottom: 8px;
        }


        /* ====================================================
           CARD HEADER
           ==================================================== */

        .card-title {
            color: #e2ebf8;

            font-size: 11px;
            font-weight: 650;

            line-height: 15px;

            padding: 0 2px 7px 2px;

            margin-bottom: 3px;

            border-bottom: 1px solid #21466f;

            text-align: left;
        }


        /* ====================================================
           HUB CARD
           ==================================================== */

        .hub-title {
            color: #ffffff;

            font-size: 15px;
            font-weight: 700;

            line-height: 18px;

            text-align: left;
        }

        .hub-subtitle {
            color: #91a9cc;

            font-size: 10px;

            line-height: 13px;

            margin-top: 3px;

            text-align: left;
        }


        /* ====================================================
           USER
           ==================================================== */

        .user-block {
            padding: 3px 4px 0 4px;
        }

        .user-name {
            color: #e4ecf8;
            font-size: 12px;
            font-weight: 600;
            line-height: 15px;
        }

        .user-role {
            color: #879fc1;
            font-size: 10px;
            line-height: 13px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


    with st.sidebar:

        # ====================================================
        # PROJECT CONTROLS HUB
        # ====================================================

        st.markdown(
            """
            <div class="sidebar-card">
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
        # UU ENTERPRISE FRAMEWORK
        # ====================================================

        with st.container():

            st.markdown(
                """
                <div class="sidebar-card">
                    <div class="card-title">
                        UU Enterprise Framework
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            for asset in FRAMEWORKS.get(
                "UU Enterprise Framework",
                []
            ):

                st.button(
                    f"○  {asset}",
                    key=f"enterprise_{asset}",
                    use_container_width=True,
                    type="secondary",
                    on_click=_select_asset,
                    args=("UU Enterprise Framework", asset),
                )


        # ====================================================
        # UU DD&B FRAMEWORK
        # ====================================================

        with st.container():

            st.markdown(
                """
                <div class="sidebar-card">
                    <div class="card-title">
                        UU DD&B Framework
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            for asset in FRAMEWORKS.get(
                "UU DD&B Framework",
                []
            ):

                st.button(
                    f"○  {asset}",
                    key=f"ddb_{asset}",
                    use_container_width=True,
                    type="secondary",
                    on_click=_select_asset,
                    args=("UU DD&B Framework", asset),
                )


        # ====================================================
        # NAVIGATION
        # ====================================================

        st.markdown(
            """
            <div class="sidebar-card">
                <div class="card-title">
                    NAVIGATION
                </div>
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


        # ====================================================
        # USER
        # ====================================================

        st.markdown(
            '<div class="user-block">',
            unsafe_allow_html=True,
        )

        user_col1, user_col2 = st.columns(
            [0.8, 3.2],
            gap="small",
        )

        with user_col1:
            st.markdown("**JS**")

        with user_col2:
            st.markdown(
                '<div class="user-name">John Smith</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<div class="user-role">Design Manager</div>',
                unsafe_allow_html=True,
            )

        st.markdown("</div>", unsafe_allow_html=True)


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