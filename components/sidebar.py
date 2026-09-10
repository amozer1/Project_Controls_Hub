import streamlit as st

from config.frameworks import FRAMEWORKS


def render_sidebar():

    with st.sidebar:

        # =====================================================
        # HEADER
        # =====================================================

        st.markdown(
            """
            <div class="pch-header">
                <div class="pch-title">PROJECT CONTROLS HUB</div>
                <div class="pch-subtitle">
                    Design Management Intelligence
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # =====================================================
        # FRAMEWORKS
        # =====================================================

        st.markdown(
            '<div class="pch-section-label">FRAMEWORKS</div>',
            unsafe_allow_html=True,
        )

        # Enterprise first
        framework_order = [
            "UU Enterprise Framework",
            "UU DD&B Framework",
        ]

        for framework_index, framework in enumerate(framework_order):

            if framework not in FRAMEWORKS:
                continue

            # Separator between frameworks
            if framework_index > 0:
                st.markdown(
                    '<div class="pch-divider"></div>',
                    unsafe_allow_html=True,
                )

            # Framework name
            st.markdown(
                f"""
                <div class="pch-framework">
                    {framework}
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Assets
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

        st.markdown(
            '<div class="pch-divider pch-navigation-divider"></div>',
            unsafe_allow_html=True,
        )

        # =====================================================
        # NAVIGATION TITLE
        # =====================================================

        st.markdown(
            '<div class="pch-section-label">NAVIGATION</div>',
            unsafe_allow_html=True,
        )

        # =====================================================
        # NAVIGATION
        # =====================================================

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

        st.markdown(
            """
            <div class="pch-profile-divider"></div>

            <div class="pch-profile">
                <div class="pch-avatar">JS</div>

                <div class="pch-profile-details">
                    <div class="pch-profile-name">John Smith</div>
                    <div class="pch-profile-role">Design Manager</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def _select_asset(framework, asset):

    st.session_state.selected_framework = framework
    st.session_state.selected_asset = asset
    st.session_state.selected_navigation = "Overview"


def _select_navigation(item):

    st.session_state.selected_navigation = item