import streamlit as st


def render_sidebar():
    """Render the Project Controls Hub sidebar."""

    with st.sidebar:

        # ---------------------------------------------------------
        # BRANDING
        # ---------------------------------------------------------

        st.markdown(
            """
            <div class="sidebar-brand">
                <div class="brand-mark">◈</div>
                <div>
                    <div class="brand-title">PROJECT</div>
                    <div class="brand-title">CONTROLS HUB</div>
                    <div class="brand-subtitle">United Utilities</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        # ---------------------------------------------------------
        # FRAMEWORK
        # ---------------------------------------------------------

        st.markdown(
            '<div class="sidebar-section-title">FRAMEWORK</div>',
            unsafe_allow_html=True,
        )

        frameworks = {
            "UU DD&B Framework": "5 Assets",
            "UU Enterprise Framework": "2 Assets",
        }

        selected_framework = st.radio(
            "Framework",
            options=list(frameworks.keys()),
            format_func=lambda x: f"{x}  •  {frameworks[x]}",
            label_visibility="collapsed",
            key="selected_framework",
        )

        st.markdown("---")

        # ---------------------------------------------------------
        # ASSET / PROJECT
        # ---------------------------------------------------------

        st.markdown(
            '<div class="sidebar-section-title">ASSET / PROJECT</div>',
            unsafe_allow_html=True,
        )

        projects = [
            "Ferry PS",
            "Rossall Outfall",
            "Flass Lane",
            "Tally Ho",
            "Eccleston Bridge",
            "Pennington Flash",
            "Davyhulme ASP4",
        ]

        selected_project = st.selectbox(
            "Project",
            projects,
            index=0,
            label_visibility="collapsed",
            key="selected_project",
        )

        st.markdown("---")

        # ---------------------------------------------------------
        # NAVIGATION
        # ---------------------------------------------------------

        st.markdown(
            '<div class="sidebar-section-title">NAVIGATION</div>',
            unsafe_allow_html=True,
        )

        navigation = [
            ("▣", "Overview"),
            ("◫", "Programme"),
            ("◧", "Delivery & Programme"),
            ("◈", "Communications"),
            ("▤", "Documents"),
            ("✦", "Intelligence"),
            ("▥", "Reports"),
            ("⚙", "Settings"),
        ]

        if "current_page" not in st.session_state:
            st.session_state.current_page = "Overview"

        for icon, page in navigation:

            is_active = st.session_state.current_page == page

            active_class = "nav-item-active" if is_active else "nav-item"

            if st.button(
                f"{icon}   {page}",
                key=f"nav_{page}",
                use_container_width=True,
            ):
                st.session_state.current_page = page
                st.rerun()

        # ---------------------------------------------------------
        # SPACER
        # ---------------------------------------------------------

        st.markdown(
            '<div class="sidebar-spacer"></div>',
            unsafe_allow_html=True,
        )

        # ---------------------------------------------------------
        # USER PROFILE
        # ---------------------------------------------------------

        st.markdown("---")

        st.markdown(
            """
            <div class="user-profile">
                <div class="user-avatar">JS</div>
                <div class="user-details">
                    <div class="user-name">John Smith</div>
                    <div class="user-role">Design Manager</div>
                </div>
                <div class="user-menu">⌄</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    return {
        "framework": selected_framework,
        "project": selected_project,
        "page": st.session_state.current_page,
    }