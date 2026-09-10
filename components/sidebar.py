import streamlit as st

from config.frameworks import FRAMEWORKS
from config.navigation import NAVIGATION


def render_sidebar():

    with st.sidebar:

        # =========================================================
        # HEADER
        # =========================================================

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

        st.markdown(
            '<div class="sidebar-divider"></div>',
            unsafe_allow_html=True,
        )

        # =========================================================
        # FRAMEWORKS
        # =========================================================

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

                label = f"●  {asset}" if selected else f"○  {asset}"

                if st.button(
                    label,
                    key=f"asset_{framework}_{asset}",
                    use_container_width=True,
                    type="primary" if selected else "secondary",
                ):
                    st.session_state.selected_framework = framework
                    st.session_state.selected_asset = asset
                    st.session_state.selected_navigation = "Overview"
                    st.rerun()

        st.markdown(
            '<div class="sidebar-divider"></div>',
            unsafe_allow_html=True,
        )

        # =========================================================
        # NAVIGATION
        # =========================================================

        st.markdown(
            '<div class="sidebar-section-title">NAVIGATION</div>',
            unsafe_allow_html=True,
        )

        icons = {
            "Overview": "▣",
            "Programme": "◫",
            "Delivery & Programme": "◈",
            "Communications": "◌",
            "Documents": "▤",
            "Intelligence": "⚡",
            "Reports": "▥",
            "Settings": "⚙",
        }

        for item in NAVIGATION:

            selected = (
                st.session_state.selected_navigation == item
            )

            icon = icons.get(item, "▣")
            label = f"{icon}  {item}"

            if st.button(
                label,
                key=f"navigation_{item}",
                use_container_width=True,
                type="primary" if selected else "secondary",
            ):
                st.session_state.selected_navigation = item
                st.rerun()

        # =========================================================
        # PROFILE
        # =========================================================

        st.markdown(
            '<div class="sidebar-profile-spacer"></div>',
            unsafe_allow_html=True,
        )

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