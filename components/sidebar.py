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
    ("Delivery & Programme", "◩"),
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

    with st.sidebar:

        # =====================================================
        # PROJECT CONTROLS HUB
        # =====================================================

        st.markdown(
            """
            <div class="sidebar-brand">
                <div class="sidebar-title">
                    PROJECT CONTROLS HUB
                </div>
                <div class="sidebar-subtitle">
                    Design Management Intelligence
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        # =====================================================
        # FRAMEWORKS
        # =====================================================

        st.markdown(
            '<div class="sidebar-section-title">FRAMEWORKS</div>',
            unsafe_allow_html=True,
        )

        for framework_index, framework in enumerate(FRAMEWORK_ORDER):

            if framework not in FRAMEWORKS:
                continue

            # -------------------------------------------------
            # Framework heading
            # -------------------------------------------------

            st.markdown(
                f"""
                <div class="framework-heading">
                    {framework}
                </div>
                """,
                unsafe_allow_html=True,
            )

            # -------------------------------------------------
            # Assets / Projects
            # -------------------------------------------------

            for asset in FRAMEWORKS[framework]:

                selected = (
                    st.session_state.get("selected_framework")
                    == framework
                    and
                    st.session_state.get("selected_asset")
                    == asset
                )

                st.button(
                    asset,
                    key=f"asset_{framework}_{asset}",
                    use_container_width=True,
                    type="primary" if selected else "secondary",
                    on_click=_select_asset,
                    args=(framework, asset),
                )

            # -------------------------------------------------
            # Divider between frameworks
            # -------------------------------------------------

            if framework_index < len(FRAMEWORK_ORDER) - 1:

                st.markdown(
                    '<div class="framework-divider"></div>',
                    unsafe_allow_html=True,
                )

        # =====================================================
        # NAVIGATION
        # =====================================================

        st.divider()

        st.markdown(
            '<div class="sidebar-section-title">NAVIGATION</div>',
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


# ============================================================
# SIDEBAR STYLING
# ============================================================

def load_sidebar_css():

    st.markdown(
        """
        <style>

        /* ====================================================
           SIDEBAR
           ==================================================== */

        section[data-testid="stSidebar"] {
            background:
                linear-gradient(
                    180deg,
                    #06152f 0%,
                    #071a3d 55%,
                    #06152f 100%
                );
            border-right: 1px solid #17396b;
        }


        /* ====================================================
           BRAND
           ==================================================== */

        .sidebar-brand {
            padding: 6px 4px 8px 4px;
        }

        .sidebar-title {
            color: #f4f7ff;
            font-size: 20px;
            font-weight: 700;
            letter-spacing: 0.3px;
            line-height: 1.15;
        }

        .sidebar-subtitle {
            color: #8fa8d2;
            font-size: 13px;
            margin-top: 7px;
        }


        /* ====================================================
           SECTION HEADINGS
           ==================================================== */

        .sidebar-section-title {
            color: #9bb4df;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.8px;
            margin: 6px 0 12px 2px;
        }


        /* ====================================================
           FRAMEWORK HEADINGS
           ==================================================== */

        .framework-heading {
            color: #dce8ff;
            font-size: 13px;
            font-weight: 650;
            margin: 10px 0 6px 2px;
        }


        /* ====================================================
           FRAMEWORK DIVIDER
           ==================================================== */

        .framework-divider {
            height: 1px;
            background: #17396b;
            margin: 13px 0 15px 0;
        }


        /* ====================================================
           BUTTONS
           ==================================================== */

        section[data-testid="stSidebar"]
        button {
            border-radius: 7px !important;
            min-height: 38px !important;
            text-align: left !important;
        }


        /* Normal buttons */

        section[data-testid="stSidebar"]
        button[kind="secondary"] {
            background: transparent !important;
            border: 1px solid transparent !important;
            color: #c5d4ee !important;
        }


        section[data-testid="stSidebar"]
        button[kind="secondary"]:hover {
            background: #102d5e !important;
            border-color: #20477f !important;
            color: #ffffff !important;
        }


        /* Active buttons */

        section[data-testid="stSidebar"]
        button[kind="primary"] {
            background:
                linear-gradient(
                    90deg,
                    #123d91,
                    #174da9
                ) !important;

            border: 1px solid #255cc0 !important;
            color: #ffffff !important;
            box-shadow:
                inset 3px 0 0 #54a6ff;
        }


        /* ====================================================
           DIVIDER
           ==================================================== */

        section[data-testid="stSidebar"] hr {
            border-color: #17396b !important;
            margin: 15px 0 !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )