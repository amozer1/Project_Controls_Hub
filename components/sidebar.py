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

    # --------------------------------------------------------
    # SIMPLE SIDEBAR CSS
    # --------------------------------------------------------

    st.markdown(
        """
        <style>

        /* Sidebar background */
        [data-testid="stSidebar"] {
            background-color: #061936;
        }

        /* Sidebar text */
        [data-testid="stSidebar"] * {
            box-sizing: border-box;
        }

        /* Buttons */
        [data-testid="stSidebar"] .stButton {
            margin: 0;
            padding: 0;
        }

        [data-testid="stSidebar"] .stButton button {
            width: 100%;
            min-height: 36px;
            margin: 2px 0;
            padding: 7px 10px;

            text-align: left;
            justify-content: flex-start;

            border-radius: 6px;
            font-size: 13px;
            line-height: 18px;
        }

        /* Remove paragraph spacing inside buttons */
        [data-testid="stSidebar"] .stButton button p {
            margin: 0;
            padding: 0;
            text-align: left;
        }

        /* Dividers */
        [data-testid="stSidebar"] hr {
            border-color: #1b3b68;
            margin: 12px 0;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


    # ========================================================
    # SIDEBAR CONTENT
    # ========================================================

    with st.sidebar:

        # ----------------------------------------------------
        # HEADER
        # ----------------------------------------------------

        st.markdown(
            "## PROJECT CONTROLS HUB"
        )

        st.caption(
            "Design Management Intelligence"
        )

        st.divider()


        # ----------------------------------------------------
        # FRAMEWORKS
        # ----------------------------------------------------

        st.markdown("**FRAMEWORKS**")


        for framework_index, framework in enumerate(FRAMEWORK_ORDER):

            if framework not in FRAMEWORKS:
                continue


            # Framework name

            st.markdown(
                f"**{framework}**"
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


                # Selected / unselected circle

                if selected:
                    label = f"●  {asset}"
                else:
                    label = f"○  {asset}"


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

        st.markdown("**NAVIGATION**")


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

        st.divider()

        user_col1, user_col2 = st.columns(
            [1, 3],
            gap="small"
        )


        with user_col1:

            st.markdown(
                "### JS"
            )


        with user_col2:

            st.markdown(
                "**John Smith**"
            )

            st.caption(
                "Design Manager"
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