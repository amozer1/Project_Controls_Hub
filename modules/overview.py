# modules/overview.py

import streamlit as st
import pandas as pd


def render_overview(framework=None, asset=None):

    st.title("Project Controls Dashboard")

    if framework:
        st.caption(f"Framework: {framework}")

    if asset:
        st.caption(f"Asset: {asset}")

    st.markdown("### Overview")

    st.info("Welcome to the Project Controls Dashboard")

    # KPI Section
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Projects", 12)

    with col2:
        st.metric("Completed", 5)

    with col3:
        st.metric("In Progress", 6)

    with col4:
        st.metric("Delayed", 1)

    st.divider()

    data = {
        "Project": [
            "Project A",
            "Project B",
            "Project C",
            "Project D"
        ],
        "Status": [
            "Complete",
            "In Progress",
            "Delayed",
            "In Progress"
        ],
        "Progress (%)": [
            100,
            75,
            45,
            60
        ]
    }

    df = pd.DataFrame(data)

    st.subheader("Project Status")
    st.dataframe(df, use_container_width=True)

    st.subheader("Progress Overview")
    st.bar_chart(
        df.set_index("Project")["Progress (%)"]
    )