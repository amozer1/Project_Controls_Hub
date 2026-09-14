import streamlit as st
import pandas as pd

from loaders.programme_loader import get_ferry_project_position


def render_project_position_ferry():

    # Load Ferry project position data
    try:
        data = get_ferry_project_position()
    except Exception as e:
        st.error("Unable to load Ferry PS project position.")
        st.exception(e)
        return

    # Check that data exists
    if data is None:
        st.warning("No Ferry PS project position data available.")
        return

    # Convert returned data to DataFrame
    if isinstance(data, pd.DataFrame):
        df = data.copy()

    elif isinstance(data, dict):

        if isinstance(data.get("deliverables"), pd.DataFrame):
            df = data["deliverables"].copy()

        elif isinstance(data.get("active_deliverables"), pd.DataFrame):
            df = data["active_deliverables"].copy()

        else:
            render_summary(data)
            return

    else:
        st.warning("Unsupported Ferry PS project position data.")
        return

    if df.empty:
        st.warning("No active Ferry PS deliverables found.")
        return

    # Clean column names
    df.columns = [str(column).strip() for column in df.columns]

    # Convert completion to numeric
    if "Activity % Complete" in df.columns:
        df["Activity % Complete"] = pd.to_numeric(
            df["Activity % Complete"],
            errors="coerce"
        ).fillna(0)

    # Convert float to numeric
    if "Total Float" in df.columns:
        df["Total Float"] = pd.to_numeric(
            df["Total Float"],
            errors="coerce"
        )

    # Convert dates
    if "Finish" in df.columns:
        df["Finish"] = pd.to_datetime(
            df["Finish"],
            errors="coerce"
        )

    if "BL1 Finish" in df.columns:
        df["BL1 Finish"] = pd.to_datetime(
            df["BL1 Finish"],
            errors="coerce"
        )

    # Calculate status
    df["Status"] = df.apply(calculate_status, axis=1)

    # KPI calculations
    total_deliverables = len(df)

    on_track = int(
        (df["Status"] == "On Track").sum()
    )

    delayed = int(
        (df["Status"] == "Delayed").sum()
    )

    at_risk = int(
        (df["Status"] == "At Risk").sum()
    )

    next_7_days = count_next_7_days(df)

    overall_status = calculate_overall_status(
        total_deliverables,
        delayed,
        at_risk
    )

    # Unit heading
    st.markdown(
        """
        <div class="overview-unit-header">
            <div>
                <div class="overview-unit-kicker">
                    PROJECT POSITION
                </div>
                <div class="overview-unit-title">
                    Ferry PS
                </div>
            </div>

            <div class="overview-unit-question">
                Where are we?
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # KPI columns
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        render_kpi(
            "Overall Status",
            overall_status,
            get_status_class(overall_status)
        )

    with col2:
        render_kpi(
            "Total Deliverables",
            total_deliverables,
            "neutral"
        )

    with col3:
        render_kpi(
            "On Track",
            on_track,
            "healthy"
        )

    with col4:
        render_kpi(
            "Delayed",
            delayed,
            "warning"
        )

    with col5:
        render_kpi(
            "At Risk",
            at_risk,
            "critical"
        )

    with col6:
        render_kpi(
            "Next 7 Days",
            next_7_days,
            "forecast"
        )


def calculate_status(row):

    finish = row.get("Finish")
    baseline = row.get("BL1 Finish")
    total_float = row.get("Total Float")
    completion = row.get("Activity % Complete", 0)

    today = pd.Timestamp.today().normalize()

    try:
        completion = float(completion)
    except (TypeError, ValueError):
        completion = 0

    try:
        total_float = float(total_float)
    except (TypeError, ValueError):
        total_float = None

    # Completed activity
    if completion >= 100:
        return "On Track"

    # Already past finish date
    if pd.notna(finish):

        if finish < today:
            return "Delayed"

        days_to_finish = (finish - today).days

        # Due within seven days
        if 0 <= days_to_finish <= 7:

            if total_float is not None and total_float <= 5:
                return "At Risk"

    # Compare current finish against baseline
    if pd.notna(finish) and pd.notna(baseline):

        movement = (finish - baseline).days

        # Moved later than baseline
        if movement > 0:

            if total_float is None:
                return "At Risk"

            if total_float <= 0:
                return "Delayed"

            if total_float <= 5:
                return "At Risk"

    # Low float
    if total_float is not None:

        if total_float < 0:
            return "Delayed"

        if total_float <= 5:
            return "At Risk"

    return "On Track"


def count_next_7_days(df):

    if "Finish" not in df.columns:
        return 0

    today = pd.Timestamp.today().normalize()

    seven_days = today + pd.Timedelta(days=7)

    mask = (
        (df["Finish"] >= today)
        & (df["Finish"] <= seven_days)
    )

    if "Activity % Complete" in df.columns:
        mask = mask & (
            df["Activity % Complete"] < 100
        )

    return int(mask.sum())


def calculate_overall_status(
    total_deliverables,
    delayed,
    at_risk
):

    if total_deliverables == 0:
        return "No Data"

    if delayed > 0:
        return "Delayed"

    if at_risk > 0:
        return "At Risk"

    return "On Track"


def get_status_class(status):

    if status == "On Track":
        return "healthy"

    if status == "At Risk":
        return "warning"

    if status == "Delayed":
        return "critical"

    return "neutral"


def render_kpi(label, value, card_class):

    st.markdown(
        f"""
        <div class="project-position-kpi {card_class}">
            <div class="project-position-kpi-label">
                {label}
            </div>

            <div class="project-position-kpi-value">
                {value}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_summary(data):

    total_deliverables = int(
        data.get("total_deliverables", 0)
    )

    on_track = int(
        data.get("on_track", 0)
    )

    delayed = int(
        data.get("delayed", 0)
    )

    at_risk = int(
        data.get("at_risk", 0)
    )

    next_7_days = int(
        data.get("next_7_days", 0)
    )

    overall_status = data.get(
        "overall_status",
        calculate_overall_status(
            total_deliverables,
            delayed,
            at_risk
        )
    )

    st.markdown(
        """
        <div class="overview-unit-header">
            <div>
                <div class="overview-unit-kicker">
                    PROJECT POSITION
                </div>

                <div class="overview-unit-title">
                    Ferry PS
                </div>
            </div>

            <div class="overview-unit-question">
                Where are we?
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        render_kpi(
            "Overall Status",
            overall_status,
            get_status_class(overall_status)
        )

    with col2:
        render_kpi(
            "Total Deliverables",
            total_deliverables,
            "neutral"
        )

    with col3:
        render_kpi(
            "On Track",
            on_track,
            "healthy"
        )

    with col4:
        render_kpi(
            "Delayed",
            delayed,
            "warning"
        )

    with col5:
        render_kpi(
            "At Risk",
            at_risk,
            "critical"
        )

    with col6:
        render_kpi(
            "Next 7 Days",
            next_7_days,
            "forecast"
        )