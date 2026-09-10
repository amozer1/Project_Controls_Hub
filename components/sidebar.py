import streamlit as st

from config.frameworks import FRAMEWORKS


def render_sidebar():

    with st.sidebar:

        # =====================================================
        # HEADER
        # =====================================================

        st.html(
            """
            <div class="pch-header">
                <div class="pch-title">PROJECT CONTROLS HUB</div>
                <div class="pch-subtitle">
                    Design Management Intelligence
                </div>
            </div>
            """
        )

        # =====================================================
        # FRAMEWORKS
        # =====================================================

        st.html(
            """
            <div class="pch-section-label">
                FRAMEWORKS
            </div>
            """
        )

        # Enterprise Framework first
        framework_order = [
            "UU Enterprise Framework",
            "UU DD&B Framework",
        ]

        for index, framework in enumerate(framework_order):

            if framework not in FRAMEWORKS:
                continue

            # Horizontal separator between frameworks
            if index > 0:
                st.html(
                    '<div class="pch-divider"></div>'
                )

            # Framework heading
            st.html(
                f"""
                <div class="pch-framework">
                    {framework}
                </div>
                """
            )

            # Framework assets
            for asset in FRAMEWORKS[framework]:

                selected = (
                    st.session_state.selected_framework == framework
                    and st.session_state.selected_asset == asset
                )

                st.button(
                    asset,
                    key=f"asset_{framework}_{asset}",
                    use_container_width=True,
                    type="primary" if selected else "secondary",
                    on_click=_select_asset,
                    args=(framework, asset),
                )

        # =====================================================
        # NAVIGATION SEPARATOR
        # =====================================================

        st.html(
            '<div class="pch-divider pch-navigation-divider"></div>'
        )

        # =====================================================
        # NAVIGATION
        # =====================================================

        st.html(
            """
            <div class="pch-section-label">
                NAVIGATION
            </div>
            """
        )

        navigation_items = [
            ("▦", "Overview"),
            ("◫", "Programme"),
            ("◇", "Delivery & Programme"),
            ("◌", "Communications"),
            ("▤", "Documents"),
            ("✦", "Intelligence"),
            ("▥", "Reports"),
            ("⚙", "Settings"),
        ]

        for icon, item in navigation_items:

            selected = (
                st.session_state.selected_navigation == item
            )

            st.button(
                f"{icon}  {item}",
                key=f"navigation_{item}",
                use_container_width=True,
                type="primary" if selected else "secondary",
                on_click=_select_navigation,
                args=(item,),
            )

        # =====================================================
        # PROFILE
        # =====================================================

        st.html(
            """
            <div class="pch-profile-divider"></div>

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
            """
        )


# =========================================================
# CALLBACKS
# =========================================================

def _select_asset(framework, asset):

    st.session_state.selected_framework = framework
    st.session_state.selected_asset = asset
    st.session_state.selected_navigation = "Overview"


def _select_navigation(item):

    st.session_state.selected_navigation = item