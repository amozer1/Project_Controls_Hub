import streamlit as st

from config.frameworks import FRAMEWORKS


# -------------------------------------------------------------------
# Sidebar configuration
# -------------------------------------------------------------------

FRAMEWORK_ORDER = [
    "UU Enterprise Framework",
    "UU DD&B Framework",
]

NAVIGATION_ITEMS = [
    ("⌂", "Overview"),
    ("▦", "Programme"),
    ("◈", "Delivery & Programme"),
    ("◇", "Communications"),
    ("▤", "Documents"),
    ("✦", "Intelligence"),
    ("▥", "Reports"),
    ("⚙", "Settings"),
]


# -------------------------------------------------------------------
# Sidebar
# -------------------------------------------------------------------

def render_sidebar():

    with st.sidebar:

        # -----------------------------------------------------------
        # Header
        # -----------------------------------------------------------

        st.markdown(
            """
            <div class="pch-header">

                <div class="pch-brand">
                    PROJECT CONTROLS HUB
                </div>

                <div class="pch-tagline">
                    Design Management Intelligence
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        # -----------------------------------------------------------
        # Frameworks heading
        # -----------------------------------------------------------

        st.markdown(
            """
            <div class="pch-section-heading">
                FRAMEWORKS
            </div>
            """,
            unsafe_allow_html=True,
        )

        # -----------------------------------------------------------
        # Frameworks and assets
        # -----------------------------------------------------------

        for framework_index, framework in enumerate(FRAMEWORK_ORDER):

            if framework not in FRAMEWORKS:
                continue

            # Separator between frameworks
            if framework_index > 0:
                st.markdown(
                    '<div class="pch-framework-divider"></div>',
                    unsafe_allow_html=True,
                )

            # Framework title
            st.markdown(
                f"""
                <div class="pch-framework-title">
                    <span class="pch-framework-marker"></span>
                    <span>{framework}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Assets
            for asset in FRAMEWORKS[framework]:

                selected = (
                    st.session_state.get("selected_framework") == framework
                    and st.session_state.get("selected_asset") == asset
                )

                st.button(
                    asset,
                    key=f"pch_asset_{framework}_{asset}",
                    use_container_width=True,
                    type="primary" if selected else "secondary",
                    on_click=_select_asset,
                    args=(framework, asset),
                )

        # -----------------------------------------------------------
        # Navigation separator
        # -----------------------------------------------------------

        st.markdown(
            '<div class="pch-major-divider"></div>',
            unsafe_allow_html=True,
        )

        # -----------------------------------------------------------
        # Navigation heading
        # -----------------------------------------------------------

        st.markdown(
            """
            <div class="pch-section-heading">
                NAVIGATION
            </div>
            """,
            unsafe_allow_html=True,
        )

        # -----------------------------------------------------------
        # Navigation
        # -----------------------------------------------------------

        for icon, item in NAVIGATION_ITEMS:

            selected = (
                st.session_state.get("selected_navigation") == item
            )

            st.button(
                f"{icon}    {item}",
                key=f"pch_navigation_{item}",
                use_container_width=True,
                type="primary" if selected else "secondary",
                on_click=_select_navigation,
                args=(item,),
            )

        # -----------------------------------------------------------
        # Profile
        # -----------------------------------------------------------

        st.markdown(
            """
            <div class="pch-profile-area">

                <div class="pch-profile">

                    <div class="pch-avatar">
                        JS
                    </div>

                    <div class="pch-profile-details">

                        <div class="pch-profile-name">
                            John Smith
                        </div>

                        <div class="pch-profile-role">
                            Design Manager
                        </div>

                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


# -------------------------------------------------------------------
# Selection callbacks
# -------------------------------------------------------------------

def _select_asset(framework, asset):

    st.session_state.selected_framework = framework
    st.session_state.selected_asset = asset
    st.session_state.selected_navigation = "Overview"


def _select_navigation(item):

    st.session_state.selected_navigation = item