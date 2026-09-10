import streamlit as st


def render():

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Health", "AMBER")

    with c2:
        st.metric("Forecast Finish", "TBC")

    with c3:
        st.metric("Variance", "0 Days")

    with c4:
        st.metric("Float", "0 Days")