import streamlit as st


def render_sidebar():
    """Render the Project Controls Hub sidebar."""

    # =============================================================
    # FRAMEWORK / ASSET STRUCTURE
    # =============================================================

    framework_data = {
        "UU DD&B Framework": {
            "short_name": "UU DD&B",
            "asset_count": 5,
            "assets": [
                "Ferry PS",
                "Rossall Outfall",
                "Flass Lane",
                "Tally Ho",
                "Eccleston Bridge",
            ],
        },
        "UU Enterprise Framework": {
            "short_name": "UU Enterprise",
            "asset_count": 2,
            "assets": [
                "Pennington Flash",
                "Davyhulme ASP4",
            ],
        },
    }

    # =============================================================
    # TEMPORARY CONTROL DATA
    #
    # These values will eventually come from the project data.
    # =============================================================

    control_data = {
        "control_score": 72,
        "programme_status": "Warning",
        "deliverables": 12,
        "exceptions": 4,
        "interfaces": 3,
        "tq_rfi": 3,
        "actions": 7,
        "next_7_days": 9,
    }

    # =============================================================
    # SESSION STATE
    # =============================================================

    if "selected_framework" not in st.session_state:
        st.session_state.selected_framework = (
            "UU DD&B Framework"
        )

    if "selected_project" not in st.session_state:
        st.session_state.selected_project = "Ferry PS"

    if "current_page" not in st.session_state:
        st.session_state.current_page = "Overview"

    # =============================================================
    # SIDEBAR
    # =============================================================

    with st.sidebar:

        # =========================================================
        # BRANDING
        # =========================================================

        st.markdown(
            """
            <div class="sidebar-brand">

                <div class="brand-mark">
                    ◈
                </div>

                <div class="brand-copy">

                    <div class="brand-title">
                        PROJECT
                    </div>

                    <div class="brand-title">
                        CONTROLS HUB
                    </div>

                    <div class="brand-subtitle">
                        DESIGN MANAGEMENT INTELLIGENCE
                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        # =========================================================
        # FRAMEWORKS
        # =========================================================

        st.markdown(
            '<div class="sidebar-section-title">'
            'FRAMEWORKS'
            '</div>',
            unsafe_allow_html=True,
        )

        # ---------------------------------------------------------
        # Framework selector
        #
        # We use radio internally because it gives us a reliable
        # selected state while CSS creates the visual card style.
        # ---------------------------------------------------------

        framework_options = list(framework_data.keys())

        selected_framework = st.radio(
            "Framework",
            framework_options,
            index=framework_options.index(
                st.session_state.selected_framework
            ),
            format_func=lambda x: (
                f"{framework_data[x]['short_name']}  •  "
                f"{framework_data[x]['asset_count']} Assets"
            ),
            label_visibility="collapsed",
            key="framework_selector",
        )

        # ---------------------------------------------------------
        # Update selected framework
        # ---------------------------------------------------------

        if (
            selected_framework
            != st.session_state.selected_framework
        ):
            st.session_state.selected_framework = selected_framework

            # Reset asset if it does not belong to the new framework
            available_assets = framework_data[
                selected_framework
            ]["assets"]

            if (
                st.session_state.selected_project
                not in available_assets
            ):
                st.session_state.selected_project = (
                    available_assets[0]
                )

            st.rerun()

        framework_info = framework_data[selected_framework]

        # ---------------------------------------------------------
        # Framework information
        # ---------------------------------------------------------

        st.markdown(
            f"""
            <div class="framework-meta">

                <span>
                    {selected_framework}
                </span>

                <span>
                    {framework_info["asset_count"]} ASSETS
                </span>

            </div>
            """,
            unsafe_allow_html=True,
        )

        # =========================================================
        # ACTIVE FRAMEWORK
        # =========================================================

        st.markdown(
            f"""
            <div class="framework-active-card">

                <div class="framework-active-top">

                    <span class="framework-active-label">
                        ACTIVE FRAMEWORK
                    </span>

                    <span class="framework-active-status">
                        ACTIVE
                    </span>

                </div>

                <div class="framework-active-name">
                    {framework_info["short_name"]}
                </div>

                <div class="framework-active-assets">
                    {framework_info["asset_count"]} assets in portfolio
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        # =========================================================
        # ASSET / PROJECT
        # =========================================================

        st.markdown(
            '<div class="sidebar-section-title">'
            'ASSET / PROJECT'
            '</div>',
            unsafe_allow_html=True,
        )

        # ---------------------------------------------------------
        # Only assets belonging to selected framework are shown
        # ---------------------------------------------------------

        available_assets = framework_info["assets"]

        # Safety check
        if (
            st.session_state.selected_project
            not in available_assets
        ):
            st.session_state.selected_project = (
                available_assets[0]
            )

        selected_project = st.selectbox(
            "Asset / Project",
            available_assets,
            index=available_assets.index(
                st.session_state.selected_project
            ),
            label_visibility="collapsed",
            key="project_selector",
        )

        st.session_state.selected_project = selected_project

        # ---------------------------------------------------------
        # Active asset indicator
        # ---------------------------------------------------------

        st.markdown(
            f"""
            <div class="active-project-indicator">

                <span class="active-project-dot"></span>

                <div>

                    <div class="active-project-label">
                        ACTIVE ASSET
                    </div>

                    <div class="active-project-name">
                        {selected_project}
                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        # =========================================================
        # CONTROL STATUS
        # =========================================================

        score = control_data["control_score"]

        if score >= 80:

            status_class = "status-good"
            status_label = "CONTROLLED"

        elif score >= 60:

            status_class = "status-warning"
            status_label = "ATTENTION"

        else:

            status_class = "status-critical"
            status_label = "AT RISK"

        st.markdown(
            f"""
            <div class="control-status-card">

                <div class="control-status-header">

                    <span>
                        CONTROL STATUS
                    </span>

                    <span class="{status_class}">
                        ●
                    </span>

                </div>

                <div class="control-score">
                    {score}
                    <span>/100</span>
                </div>

                <div class="control-status-label {status_class}">
                    {status_label}
                </div>

                <div class="control-status-bar">

                    <div
                        class="control-status-fill"
                        style="width:{score}%;">
                    </div>

                </div>

                <div class="control-status-meta">

                    <span>
                        Programme
                    </span>

                    <span>
                        {control_data["programme_status"]}
                    </span>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        # =========================================================
        # NAVIGATION
        # =========================================================

        navigation_groups = [

            {
                "title": "OVERVIEW",
                "items": [
                    ("▣", "Overview", None),
                ],
            },

            {
                "title": "CONTROL CENTRE",
                "items": [
                    ("◫", "Programme", None),
                    (
                        "◧",
                        "Deliverables",
                        control_data["deliverables"],
                    ),
                    (
                        "⚠",
                        "Exceptions",
                        control_data["exceptions"],
                    ),
                    (
                        "◇",
                        "Interfaces",
                        control_data["interfaces"],
                    ),
                ],
            },

            {
                "title": "COMMUNICATIONS",
                "items": [
                    (
                        "◈",
                        "TQs & RFIs",
                        control_data["tq_rfi"],
                    ),
                    (
                        "✓",
                        "Actions",
                        control_data["actions"],
                    ),
                ],
            },

            {
                "title": "INTELLIGENCE",
                "items": [
                    (
                        "✦",
                        "Controls Intelligence",
                        None,
                    ),
                    (
                        "◒",
                        "Trend & Trajectory",
                        None,
                    ),
                    (
                        "⌁",
                        "Dependencies",
                        None,
                    ),
                ],
            },

            {
                "title": "INFORMATION",
                "items": [
                    ("▤", "Documents", None),
                    ("▥", "Reports", None),
                ],
            },
        ]

        for group in navigation_groups:

            st.markdown(
                f"""
                <div class="sidebar-section-title nav-group-title">
                    {group["title"]}
                </div>
                """,
                unsafe_allow_html=True,
            )

            for icon, page, badge in group["items"]:

                is_active = (
                    st.session_state.current_page == page
                )

                # -------------------------------------------------
                # Build button label
                # -------------------------------------------------

                if badge is not None and badge > 0:

                    label = (
                        f"{icon}   {page}   {badge}"
                    )

                else:

                    label = (
                        f"{icon}   {page}"
                    )

                # -------------------------------------------------
                # Active state indicator
                #
                # Streamlit buttons do not accept a CSS class
                # directly, so the active state is represented
                # through the label.
                # -------------------------------------------------

                if is_active:

                    label = f"●  {page}"

                # -------------------------------------------------
                # Navigation button
                # -------------------------------------------------

                if st.button(
                    label,
                    key=f"nav_{page}",
                    use_container_width=True,
                ):

                    st.session_state.current_page = page
                    st.rerun()

        # =========================================================
        # LIVE CONTROL
        # =========================================================

        st.markdown(
            '<div class="sidebar-section-title">'
            'LIVE CONTROL'
            '</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="live-control-panel">

                <div class="live-control-row">

                    <span class="live-dot"></span>

                    <span>
                        <strong>
                            {control_data["exceptions"]}
                        </strong>
                        exceptions
                    </span>

                </div>

                <div class="live-control-row">

                    <span class="live-arrow">
                        →
                    </span>

                    <span>
                        <strong>
                            {control_data["next_7_days"]}
                        </strong>
                        activities next 7 days
                    </span>

                </div>

                <div class="live-control-row">

                    <span class="live-warning">
                        !
                    </span>

                    <span>
                        <strong>
                            {control_data["deliverables"]}
                        </strong>
                        deliverables need attention
                    </span>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        # =========================================================
        # SPACER
        # =========================================================

        st.markdown(
            '<div class="sidebar-spacer"></div>',
            unsafe_allow_html=True,
        )

        # =========================================================
        # SETTINGS
        # =========================================================

        st.markdown(
            '<div class="sidebar-bottom-divider"></div>',
            unsafe_allow_html=True,
        )

        if st.button(
            "⚙   Settings",
            key="nav_settings",
            use_container_width=True,
        ):

            st.session_state.current_page = "Settings"
            st.rerun()

        # =========================================================
        # USER
        # =========================================================

        st.markdown(
            """
            <div class="user-profile">

                <div class="user-avatar">
                    DM
                </div>

                <div class="user-details">

                    <div class="user-name">
                        Design Manager
                    </div>

                    <div class="user-role">
                        Project Controls Hub
                    </div>

                </div>

                <div class="user-menu">
                    ⋮
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    # =============================================================
    # RETURN VALUES
    # =============================================================

    return {
        "framework": selected_framework,
        "project": selected_project,
        "page": st.session_state.current_page,
    }