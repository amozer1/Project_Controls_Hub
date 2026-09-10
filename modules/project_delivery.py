# modules/project_delivery.py

import streamlit as st
import pandas as pd


def render_project_delivery():
    st.title("🚧 Project Delivery")

    st.markdown("### Delivery Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Projects", 12)

    with col2:
        st.metric("On Track", 8)

    with col3:
        st.metric("At Risk", 3)

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
            "On Track",
            "At Risk",
            "Delayed",
            "On Track"
        ],
        "Progress (%)": [
            85,
            60,
            40,
            95
        ],
        "Planned Finish": [
            "2026-08-15",
            "2026-09-10",
            "2026-10-05",
            "2026-08-01"
        ]
    }

    df = pd.DataFrame(data)

    st.subheader("Project Delivery Status")
    st.dataframe(df, use_container_width=True)

    st.subheader("Progress")
    st.bar_chart(
        df.set_index("Project")["Progress (%)"]
    )

    st.subheader("Delivery Notes")

    st.text_area(
        "Project Delivery Comments",
        height=150,
        placeholder="Enter project delivery updates..."
    )