import streamlit as st

from overview.ferry.project_summary import render as render_project_summary
from overview.ferry.intelligence_panel import render as render_intelligence_panel
from overview.ferry.framework_progress import render as render_framework_progress
from overview.ferry.metric_cards import render as render_metric_cards
from overview.ferry.upcoming_milestones import render as render_upcoming_milestones
from overview.ferry.actions_required import render as render_actions_required
from overview.ferry.pie_card_ferry import render_pie_ferry
from overview.ferry.next7days_cl32_ferry import render_next7days_table
from overview.ferry.milestone_cl32_ferry import render_milestone_table
from overview.ferry.deliverables_ferry import render_deliverables_table

def show_overview(asset, programme_df):

    if asset != "Ferry PS":
        st.info(f"{asset} overview not built yet.")
        return

    render_project_summary()

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    render_intelligence_panel(programme_df)

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    render_framework_progress()

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    render_metric_cards()

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    left_col, right_col = st.columns([1, 1])

    with left_col:
        render_upcoming_milestones()

    with right_col:
        render_actions_required()

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    left_col, right_col = st.columns([1, 1])

    with left_col:
        st.markdown("### Delivery Status")
        render_pie_ferry(programme_df)

    with right_col:
        st.markdown("### Next 7 Days")
        render_next7days_table()

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    render_milestone_table()

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    render_deliverables_table()