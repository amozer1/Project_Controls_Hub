import streamlit as st

from config.frameworks import FRAMEWORKS


# ============================================================
# ORDER
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

    # --------------------------------------------------------
    # Sidebar CSS
    # --------------------------------------------------------

    st.markdown(
        """
        <style>

        /* ==================================================
           SIDEBAR
           ================================================== */

        section[data-testid="stSidebar"] {
            background: #061936;
            border-right: 1px solid #183763;
        }

        section[data-testid="stSidebar"] > div {
            padding-top: 1rem;
            padding-left: 1rem;
            padding-right: 0.7rem;
        }


        /* ==================================================
           HEADER
           ================================================== */

        .hub-title {
            color: #f5f7fb;
            font-size: 19px;
            font-weight: 700;
            line-height: 1.05;
            margin-bottom: 7px;
            letter-spacing: 0.1px;
        }

        .hub-subtitle {
            color: #a9b9d5;
            font-size: 12px;
            line-height: 1.2;
            margin-bottom: 14px;
        }


        /* ==================================================
           SECTION TITLE
           ================================================== */

        .section-title {
            color: #9eb2d4;
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 0.5px;
            margin-top: 4px;
            margin-bottom: 10px;
        }


        /* ==================================================
           FRAMEWORK NAME
           ================================================== */

        .framework-name {
            color: #d9e4f7;
            font-size: 13px;
            font-weight: 600;
            line-height: 1.2;
            margin-top: 8px;
            margin-bottom: 4px;
        }


        /* ==================================================
           PROJECT BUTTONS
           ================================================== */

        section[data-testid="stSidebar"]
        .project-button button {
            background: transparent !important;
            border: none !important;
            color: #c6d3e8 !important;
            min-height: 32px !important;
            height: 32px !important;
            padding: 0 8px !important;
            margin: 0 !important;
            font-size: 13px !important;
            font-weight: 400 !important;
            text-align: left !important;
            border-radius: 5px !important;
            box-shadow: none !important;
        }

        section[data-testid="stSidebar"]
        .project-button button:hover {
            background: #102d5d !important;
            color: white !important;
        }


        /* ==================================================
           SELECTED PROJECT
           ================================================== */

        section[data-testid="stSidebar"]
        .selected-project button {
            background: #123e8f !important;
            border: 1px solid #1e56b0 !important;
            color: white !important;
            font-weight: 500 !important;
        }


        /* ==================================================
           NAVIGATION BUTTONS
           ================================================== */

        section[data-testid="stSidebar"]
        .nav-button button {
            background: transparent !important;
            border: none !important;
            color: #c6d3e8 !important;
            min-height: 36px !important;
            height: 36px !important;
            padding: 0 8px !important;
            margin: 0 !important;
            font-size: 13px !important;
            text-align: left !important;
            border-radius: 5px !important;
            box-shadow: none !important;
        }

        section[data-testid="stSidebar"]
        .nav-button button:hover {
            background: #102d5d !important;
            color: white !important;
        }


        /* ==================================================
           SELECTED NAVIGATION
           ================================================== */

        section[data-testid="stSidebar"]
        .selected-nav button {
            background: #123e8f !important;
            border: 1px solid #1e56b0 !important;
            color: white !important;
        }


        /* ==================================================
           DIVIDERS
           ================================================== */

        .sidebar-line {
            height: 1px;
            background: #193966;
            margin: 14px 0;
        }


        /* ==================================================
           USER PROFILE
           ================================================== */

        .user-profile {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 12px 5px 5px 3px;
            border-top: 1px solid #193966;
            margin-top: 14px;
        }

        .user-avatar {
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background: #19335c;
            color: #dce8fa;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 13px;
            font-weight: 600;
            flex-shrink: 0;
        }

        .user-name {
            color: #e6edf8;
            font-size: 13px;
            font-weight: 500;
            line-height: 1.2;
        }

        .user-role {
            color: #8fa5c7;
            font-size: 11px;
            margin-top: 3px;
            line-height: 1.2;
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
            """
            <div class="hub-title">
                PROJECT CONTROLS HUB
            </div>

            <div class="hub-subtitle">
                Design Management Intelligence
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('<div class="sidebar-line"></div>', unsafe_allow_html=True)


        # ----------------------------------------------------
        # FRAMEWORKS
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">FRAMEWORKS</div>',
            unsafe_allow_html=True,
        )


        for framework_index, framework in enumerate(FRAMEWORK_ORDER):

            if framework not in FRAMEWORKS:
                continue


            # Framework heading

            st.markdown(
                f"""
                <div class="framework-name">
                    {framework}
                </div>
                """,
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


                # Circle indicator like the screenshot

                icon = "●" if selected else "○"

                label = f"{icon}  {asset}"


                if selected:
                    st.markdown(
                        '<div class="selected-project">',
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        '<div class="project-button">',
                        unsafe_allow_html=True,
                    )


                st.button(
                    label,
                    key=f"asset_{framework}_{asset}",
                    use_container_width=True,
                    on_click=_select_asset,
                    args=(framework, asset),
                )


                st.markdown("</div>", unsafe_allow_html=True)


            # Divider between frameworks

            if framework_index < len(FRAMEWORK_ORDER) - 1:

                st.markdown(
                    '<div class="sidebar-line"></div>',
                    unsafe_allow_html=True,
                )


        # ----------------------------------------------------
        # NAVIGATION
        # ----------------------------------------------------

        st.markdown(
            '<div class="sidebar-line"></div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-title">NAVIGATION</div>',
            unsafe_allow_html=True,
        )


        for item, icon in NAVIGATION_ITEMS:

            selected = (
                st.session_state.get("selected_navigation")
                == item
            )


            if selected:
                st.markdown(
                    '<div class="selected-nav">',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    '<div class="nav-button">',
                    unsafe_allow_html=True,
                )


            st.button(
                f"{icon}  {item}",
                key=f"navigation_{item}",
                use_container_width=True,
                on_click=_select_navigation,
                args=(item,),
            )


            st.markdown("</div>", unsafe_allow_html=True)


        # ----------------------------------------------------
        # USER
        # ----------------------------------------------------

        st.markdown(
            """
            <div class="user-profile">

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