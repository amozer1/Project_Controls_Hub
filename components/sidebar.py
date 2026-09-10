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

    # ========================================================
    # SIDEBAR CSS
    # ========================================================

    st.markdown(
        """
        <style>

        /* ====================================================
           SIDEBAR
           ==================================================== */

        section[data-testid="stSidebar"] {
            background-color: #071a35 !important;
        }

        section[data-testid="stSidebar"] > div {
            padding: 10px 9px 12px 9px !important;
        }


        /* ====================================================
           ALL CARDS
           ==================================================== */

        section[data-testid="stSidebar"]
        [data-testid="stVerticalBlockBorderWrapper"] {

            background: #0b2345 !important;

            border: 1px solid #23476f !important;

            border-radius: 9px !important;

            padding: 9px 9px 8px 9px !important;

            margin: 0 0 8px 0 !important;

            box-shadow:
                0 2px 5px rgba(0, 0, 0, 0.12) !important;
        }


        /* ====================================================
           HUB CARD
           ==================================================== */

        .hub-title {
            color: #ffffff;

            font-size: 15px;

            font-weight: 700;

            line-height: 18px;

            margin: 0;
        }

        .hub-subtitle {
            color: #91a9ca;

            font-size: 10px;

            font-weight: 400;

            line-height: 14px;

            margin-top: 3px;
        }


        /* ====================================================
           SECTION TITLES
           ==================================================== */

        .section-title {

            color: #e4edf8;

            font-size: 12px;

            font-weight: 650;

            line-height: 16px;

            margin: 0 0 5px 0;

            text-align: left;
        }


        /* ====================================================
           BUTTON CONTAINER
           ==================================================== */

        section[data-testid="stSidebar"] .stButton {

            margin: 0 !important;

            padding: 0 !important;

            width: 100% !important;
        }


        /* ====================================================
           BUTTONS
           ==================================================== */

        section[data-testid="stSidebar"]
        .stButton > button {

            width: 100% !important;

            height: 29px !important;

            min-height: 29px !important;

            padding: 3px 7px !important;

            margin: 1px 0 !important;

            border-radius: 5px !important;

            font-size: 11px !important;

            line-height: 15px !important;

            text-align: left !important;

            justify-content: flex-start !important;

            box-shadow: none !important;
        }


        /* ====================================================
           NORMAL BUTTON
           ==================================================== */

        section[data-testid="stSidebar"]
        .stButton > button[kind="secondary"] {

            background: transparent !important;

            border: 1px solid transparent !important;

            color: #bdcce0 !important;
        }


        /* ====================================================
           HOVER
           ==================================================== */

        section[data-testid="stSidebar"]
        .stButton > button[kind="secondary"]:hover {

            background: #12345d !important;

            border: 1px solid #28527f !important;

            color: #ffffff !important;
        }


        /* ====================================================
           SELECTED BUTTON
           ==================================================== */

        section[data-testid="stSidebar"]
        .stButton > button[kind="primary"] {

            background: #174b82 !important;

            border: 1px solid #3476b5 !important;

            color: #ffffff !important;

            font-weight: 600 !important;
        }


        /* ====================================================
           BUTTON TEXT
           ==================================================== */

        section[data-testid="stSidebar"]
        .stButton > button p {

            margin: 0 !important;

            padding: 0 !important;

            width: 100% !important;

            text-align: left !important;
        }


        /* ====================================================
           USER CARD
           ==================================================== */

        .user-avatar {

            width: 38px;

            height: 38px;

            border-radius: 50%;

            background: #1b4f87;

            border: 1px solid #3974ad;

            color: #ffffff;

            display: flex;

            align-items: center;

            justify-content: center;

            font-size: 11px;

            font-weight: 700;

            letter-spacing: 0.2px;

            margin-top: 1px;
        }


        .user-name {

            color: #edf3fb;

            font-size: 12px;

            font-weight: 650;

            line-height: 16px;

            margin: 0;
        }


        .user-role {

            color: #8fa7c8;

            font-size: 10px;

            font-weight: 400;

            line-height: 14px;

            margin: 0;
        }


        </style>
        """,
        unsafe_allow_html=True,
    )


    # ========================================================
    # SIDEBAR CONTENT
    # ========================================================

    with st.sidebar:


        # ====================================================
        # 1. PROJECT CONTROLS HUB CARD
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
        # 2. UU ENTERPRISE FRAMEWORK CARD
        # ====================================================

        with st.container(border=True):

            st.markdown(
                '<div class="section-title">'
                'UU Enterprise Framework'
                '</div>',
                unsafe_allow_html=True,
            )


            enterprise_projects = FRAMEWORKS.get(
                "UU Enterprise Framework",
                [],
            )


            for asset in enterprise_projects:

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

                    type=(
                        "primary"
                        if selected
                        else "secondary"
                    ),

                    on_click=_select_asset,

                    args=(
                        "UU Enterprise Framework",
                        asset,
                    ),
                )


        # ====================================================
        # 3. UU DD&B FRAMEWORK CARD
        # ====================================================

        with st.container(border=True):

            st.markdown(
                '<div class="section-title">'
                'UU DD&B Framework'
                '</div>',
                unsafe_allow_html=True,
            )


            ddb_projects = FRAMEWORKS.get(
                "UU DD&B Framework",
                [],
            )


            for asset in ddb_projects:

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

                    type=(
                        "primary"
                        if selected
                        else "secondary"
                    ),

                    on_click=_select_asset,

                    args=(
                        "UU DD&B Framework",
                        asset,
                    ),
                )


        # ====================================================
        # 4. NAVIGATION CARD
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

                    type=(
                        "primary"
                        if selected
                        else "secondary"
                    ),

                    on_click=_select_navigation,

                    args=(item,),
                )


        # ====================================================
        # 5. USER PROFILE CARD
        # ====================================================

        with st.container(border=True):

            user_col1, user_col2 = st.columns(
                [0.85, 3.15],
                gap="small",
            )


            # ------------------------------------------------
            # Avatar
            # ------------------------------------------------

            with user_col1:

                st.markdown(
                    """
                    <div class="user-avatar">
                        JS
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


            # ------------------------------------------------
            # User information
            # ------------------------------------------------

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