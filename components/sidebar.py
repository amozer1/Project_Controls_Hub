import streamlit as st

from config.frameworks import FRAMEWORKS


def render_sidebar():

    with st.sidebar:

        # HEADER
        st.markdown(
            """
            <div class="sidebar-header">
                <div class="sidebar-title">PROJECT CONTROLS HUB</div>
                <div class="sidebar-subtitle">
                    Design Management Intelligence
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # FRAMEWORKS
        st.markdown(
            '<div class="sidebar-section-title">FRAMEWORKS</div>',
            unsafe_allow_html=True,
        )

        for framework, assets in FRAMEWORKS.items():

            st.markdown(
                f'<div class="framework-name">{framework}</div>',
                unsafe_allow_html=True,
            )

            for asset in assets:

                selected = (
                    st.session_state.selected_framework == framework
                    and st.session_state.selected_asset == asset
                )

                st.button(
                    f"{'●' if selected else '○'}  {asset}",
                    key=f"asset_{framework}_{asset}",
                    use_container_width=True,
                    type="primary" if selected else "secondary",
                    on_click=_select_asset,
                    args=(framework, asset),
                )

        # NAVIGATION
        st.markdown(
            '<div class="sidebar-section-title">NAVIGATION</div>',
            unsafe_allow_html=True,
        )

        navigation_items = [
            ("▣", "Overview"),
            ("◫", "Programme"),
            ("◈", "Delivery & Programme"),
            ("◌", "Communications"),
            ("▤", "Documents"),
            ("⚡", "Intelligence"),
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

        # PROFILE
        st.markdown(
            """
            <div class="sidebar-profile">
                <div class="profile-avatar">JS</div>
                <div class="profile-details">
                    <div class="profile-name">John Smith</div>
                    <div class="profile-role">Design Manager</div>
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