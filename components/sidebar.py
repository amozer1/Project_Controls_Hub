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

    # ========================================================
    # SIDEBAR CSS
    # ========================================================

    st.markdown(
        """
        <style>

        /* ----------------------------------------------------
           SIDEBAR
           ---------------------------------------------------- */

        section[data-testid="stSidebar"] {
            background: #071a3a !important;
            border-right: 1px solid #183968 !important;
        }

        section[data-testid="stSidebar"] > div {
            padding: 18px 12px 12px 16px !important;
        }


        /* ----------------------------------------------------
           SIDEBAR WIDTH
           ---------------------------------------------------- */

        section[data-testid="stSidebar"] {
            width: 250px !important;
        }


        /* ----------------------------------------------------
           ALL BUTTONS
           ---------------------------------------------------- */

        section[data-testid="stSidebar"] .stButton {
            margin: 0 !important;
            padding: 0 !important;
        }

        section[data-testid="stSidebar"] .stButton > button {
            width: 100% !important;
            min-height: 34px !important;
            height: 34px !important;

            padding: 0 10px !important;
            margin: 0 0 2px 0 !important;

            border-radius: 6px !important;

            font-family: inherit !important;
            font-size: 13px !important;
            line-height: 1 !important;

            text-align: left !important;
            justify-content: flex-start !important;

            box-shadow: none !important;
        }


        /* ----------------------------------------------------
           NORMAL BUTTON
           ---------------------------------------------------- */

        section[data-testid="stSidebar"]
        .stButton > button[kind="secondary"] {

            background: transparent !important;

            border: 1px solid transparent !important;

            color: #c5d3e9 !important;
        }


        /* Hover */

        section[data-testid="stSidebar"]
        .stButton > button[kind="secondary"]:hover {

            background: #102e5e !important;

            border-color: #1b477f !important;

            color: #ffffff !important;
        }


        /* ----------------------------------------------------
           SELECTED BUTTON
           ---------------------------------------------------- */

        section[data-testid="stSidebar"]
        .stButton > button[kind="primary"] {

            background: #123e91 !important;

            border: 1px solid #2459b4 !important;

            color: #ffffff !important;

            font-weight: 500 !important;
        }


        /* ----------------------------------------------------
           DIVIDERS
           ---------------------------------------------------- */

        section[data-testid="stSidebar"] hr {

            border: none !important;

            border-top: 1px solid #21436f !important;

            margin: 14px 0 !important;
        }


        /* ----------------------------------------------------
           HUB TITLE
           ---------------------------------------------------- */

        .hub-title {
            color: #f5f7fc;
            font-size: 19px;
            font-weight: 700;
            line-height: 1.15;
            margin: 0;
            padding: 0;
        }

        .hub-subtitle {
            color: #9aafd0;
            font-size: 11px;
            margin-top: 5px;
            margin-bottom: 0;
        }


        /* ----------------------------------------------------
           SECTION TITLE
           ---------------------------------------------------- */

        .sidebar-section {
            color: #9eb5d8;
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 0.5px;
            margin: 0 0 7px 0;
        }


        /* ----------------------------------------------------
           FRAMEWORK TITLE
           ---------------------------------------------------- */

        .framework-title {
            color: #d9e4f6;
            font-size: 13px;
            font-weight: 600;
            margin: 8px 0 4px 0;
        }


        /* ----------------------------------------------------
           USER PROFILE
           ---------------------------------------------------- */

        .user-container {
            border-top: 1px solid #21436f;
            margin-top: 16px;
            padding-top: 12px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


    # ========================================================
    # CONTENT
    # ========================================================

    with st.sidebar:

        # ----------------------------------------------------
        # HEADER
        # ----------------------------------------------------

        st.markdown(
            '<div class="hub-title">PROJECT CONTROLS HUB</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="hub-subtitle">Design Management Intelligence</div>',
            unsafe_allow_html=True,
        )

        st.divider()


        # ----------------------------------------------------
        # FRAMEWORKS
        # ----------------------------------------------------

        st.markdown(
            '<div class="sidebar-section">FRAMEWORKS</div>',
            unsafe_allow_html=True,
        )


        for framework_index, framework in enumerate(FRAMEWORK_ORDER):

            if framework not in FRAMEWORKS:
                continue


            # Framework name

            st.markdown(
                f'<div class="framework-title">{framework}</div>',
                unsafe_allow_html=True,
            )


            # Projects

            for asset in FRAMEWORKS[framework]:

                selected = (
                    st.session_state.get("selected_framework")
                    == framework
                    and
                    st.session_state.get("selected_asset")
                    == asset
                )


                # Circle like screenshot

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


            # Divider between frameworks

            if framework_index < len(FRAMEWORK_ORDER) - 1:
                st.divider()


        # ----------------------------------------------------
        # NAVIGATION
        # ----------------------------------------------------

        st.divider()

        st.markdown(
            '<div class="sidebar-section">NAVIGATION</div>',
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


        # ----------------------------------------------------
        # USER
        # ----------------------------------------------------

        st.markdown(
            '<div class="user-container"></div>',
            unsafe_allow_html=True,
        )

        user_col1, user_col2 = st.columns([0.22, 0.78])

        with user_col1:

            st.markdown(
                """
                <div style="
                    width:36px;
                    height:36px;
                    border-radius:50%;
                    background:#19365f;
                    color:#e4ecfa;
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
                """
                <div style="
                    color:#e6edf8;
                    font-size:13px;
                    font-weight:500;
                    padding-top:2px;
                ">
                    John Smith
                </div>

                <div style="
                    color:#8ea5c7;
                    font-size:11px;
                    margin-top:3px;
                ">
                    Design Manager
                </div>
                """,
                unsafe_allow_html=True,
            )


# ============================================================
# ASSET SELECTION
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