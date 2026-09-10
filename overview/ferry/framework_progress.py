import streamlit as st


def render():

    st.markdown("## 🛣 Framework Progress")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.success("✅ Feasibility")

    with col2:
        st.success("✅ Concept Design")

    with col3:
        st.warning("🟠 Outline Design")

    with col4:
        st.info("⚪ Detailed Design")

    with col5:
        st.info("⚪ Construction Support")