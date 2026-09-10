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
            background: #06172f !important;
        }

        section[data-testid="stSidebar"] > div {
            padding: 14px 12px 18px 12px !important;
        }


        /* ====================================================
           REAL STREAMLIT CARDS
           ==================================================== */

        section[data-testid="stSidebar"]
        [data-testid="stVerticalBlockBorderWrapper"] {

            background: #0b2346 !important;

            border: 1px solid #24496f !important;

            border-radius: 10px !important;

            padding: 14px 13px !important;

            margin: 0 0 12px 0 !important;

            width: 100% !important;

            box-shadow:
                0 3px 10px rgba(0, 0, 0, 0.16) !important;
        }


        /* ====================================================
           CARD INTERNAL SPACING
           ==================================================== */

        section[data-testid="stSidebar"]
        [data-testid="stVerticalBlockBorderWrapper"]
        [data-testid="stVerticalBlock"] {

            gap: 0.25rem !important;
        }


        /* ====================================================
           HUB
           ==================================================== */

        .hub-title {
            color: #ffffff;

            font-size: 15px;

            font-weight: 700;

            line-height: 20px;

            margin: 0;
        }

        .hub-subtitle {
            color: #91a9ca;

            font-size: 10px;

            line-height: 15px;

            margin-top: 3px;
        }


        /* ====================================================
           SECTION TITLE
           ==================================================== */

        .section-title {
            color: #e7eef8;

            font-size: 12px;

            font-weight: 650;

            line-height: 18px;

            margin: 0 0 8px 0;
        }


        /* ====================================================
           BUTTON WRAPPER
           ==================================================== */

        section[data-testid="stSidebar"] .stButton {

            width: 100% !important;

            margin: 0 !important;

            padding: 0 !important;
        }


        /* ====================================================
           BUTTON
           ==================================================== */

        section[data-testid="stSidebar"]
        .stButton > button {

            width: 100% !important;

            height: 32px !important;

            min-height: 32px !important;

            margin: 2px 0 !important;

            padding: 6px 9px !important;

            border-radius: 6px !important;

            display: flex !important;

            align-items: center !important;

            justify-content: flex-start !important;

            text-align: left !important;

            font-size: 11px !important;

            line-height: 16px !important;

            box-shadow: none !important;

            white-space: nowrap !important;
        }


        /* ====================================================
           NORMAL BUTTON
           ==================================================== */

        section[data-testid="stSidebar"]
        .stButton > button[kind="secondary"] {

            background: transparent !important;

            border: 1px solid transparent !important;

            color: #c1d0e4 !important;
        }


        /* ====================================================
           HOVER
           ==================================================== */

        section[data-testid="stSidebar"]
        .stButton > button[kind="secondary"]:hover {

            background: #14365f !important;

            border-color: #2c5681 !important;

            color: #ffffff !important;
        }


        /* ====================================================
           SELECTED
           ==================================================== */

        section[data-testid="stSidebar"]
        .stButton > button[kind="primary"] {

            background: #18518b !important;

            border: 1px solid #3a79b5 !important;

            color: #ffffff !important;

            font-weight: 600 !important;
        }


        /* ====================================================
           BUTTON TEXT
           ==================================================== */

        section[data-testid="stSidebar"]
        .stButton > button p {

            width: 100% !important;

            margin: 0 !important;

            padding: 0 !important;

            text-align: left !important;

            line-height: 16px !important;
        }


        /* ====================================================
           USER CARD
           ==================================================== */

        .user-avatar {
            width: 40px;
            height: 40px;

            border-radius: 50%;

            background: #1b4f87;

            border: 1px solid #3976b2;

            color: #ffffff;

            display: flex;

            align-items: center;

            justify-content: center;

            font-size: 11px;

            font-weight: 700;
        }

        .user-name {
            color: #eef4fc;

            font-size: 12px;

            font-weight: 650;

            line-height: 17px;
        }

        .user-role {
            color: #8fa8c9;

            font-size: 10px;

            line-height: 15px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


    with st.sidebar:

        # ====================================================
        # 1 — PROJECT CONTROLS HUB
        # ====================================================

        with st.container(border=True):

            st.markdown(
                '<div class="hub-title">'
                'PROJECT CONTROLS HUB'
                '</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                '<div class="hub-subtitle">'
                'Design Management Intelligence'
                '</div>',
                unsafe_allow_html=True,
            )


        # ====================================================
        # 2 — UU ENTERPRISE FRAMEWORK
        # ====================================================

        with st.container(border=True):

            st.markdown(
                '<div class="section-title">'
                'UU Enterprise Framework'
                '</div>',
                unsafe_allow_html=True,
            )

            for asset in FRAMEWORKS.get(
                "UU Enterprise Framework",
                [],
            ):

                selected = (
                    st.session_state.get(
                        "selected_framework"
                    )
                    == "UU Enterprise Framework"
                    and
                    st.session_state.get(
                        "selected_asset"
                    )
                    == asset
                )

                st.button(
                    f"{'●' if selected else '○'}  {asset}",
                    key=f"enterprise_{asset}",
                    use_container_width=True,
                    type="primary" if selected else "secondary",
                    on_click=_select_asset,
                    args=(
                        "UU Enterprise Framework",
                        asset,
                    ),
                )


        # ====================================================
        # 3 — UU DD&B FRAMEWORK
        # ====================================================

        with st.container(border=True):

            st.markdown(
                '<div class="section-title">'
                'UU DD&B Framework'
                '</div>',
                unsafe_allow_html=True,
            )

            for asset in FRAMEWORKS.get(
                "UU DD&B Framework",
                [],
            ):

                selected = (
                    st.session_state.get(
                        "selected_framework"
                    )
                    == "UU DD&B Framework"
                    and
                    st.session_state.get(
                        "selected_asset"
                    )
                    == asset
                )

                st.button(
                    f"{'●' if selected else '○'}  {asset}",
                    key=f"ddb_{asset}",
                    use_container_width=True,
                    type="primary" if selected else "secondary",
                    on_click=_select_asset,
                    args=(
                        "UU DD&B Framework",
                        asset,
                    ),
                )


        # ====================================================
        # 4 — NAVIGATION
        # ====================================================

        with st.container(border=True):

            st.markdown(
                '<div class="section-title">'
                'NAVIGATION'
                '</div>',
                unsafe_allow_html=True,
            )

            for item, icon in NAVIGATION_ITEMS:

                selected = (
                    st.session_state.get(
                        "selected_navigation"
                    )
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
        # 5 — USER PROFILE
        # ====================================================

        with st.container(border=True):

            user_col1, user_col2 = st.columns(
                [0.9, 3.1],
                gap="medium",
            )

            with user_col1:

                st.markdown(
                    """
                    <div class="user-avatar">
                        JS
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with user_col2:

                st.markdown(
                    """
                    <div class="user-name">
                        John Smith
                    </div>

                    <div class="user-role">
                        Design Manager
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