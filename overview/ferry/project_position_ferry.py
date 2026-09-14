import streamlit as st
import pandas as pd

from loaders.ferry_loader import load_ferry


def render_project_position_ferry():

    # =====================================================
    # LOAD FERRY DATA
    # =====================================================

    try:
        cl31, cl32 = load_ferry()
    except Exception as e:
        st.error("Unable to load Ferry PS programme data.")
        st.exception(e)
        return

    # =====================================================
    # CHECK DATA
    # =====================================================

    if cl32 is None or cl32.empty:
        st.warning("No CL32 Ferry PS programme data available.")
        return

    # =====================================================
    # GET LATEST CL32 SNAPSHOT
    # =====================================================

    if "SnapshotDate" not in cl32.columns:
        st.error("CL32 data does not contain SnapshotDate.")
        return

    latest_snapshot = cl32["SnapshotDate"].max()

    current = cl32[
        cl32["SnapshotDate"] == latest_snapshot
    ].copy()

    if current.empty:
        st.warning("No current Ferry PS CL32 data available.")
        return

    # =====================================================
    # CLEAN COLUMN NAMES
    # =====================================================

    current.columns = [
        str(column).strip()
        for column in current.columns
    ]

    # =====================================================
    # REMOVE RETIRED ACTIVITIES
    # =====================================================

    if "Activity ID" in current.columns:

        activity_id = (
            current["Activity ID"]
            .astype(str)
            .str.strip()
            .str.upper()
        )

        current = current[
            ~activity_id.str.startswith("FER-DEP-")
        ].copy()

    # =====================================================
    # IDENTIFY FORMAL DELIVERABLES
    # =====================================================

    if "Activity ID" not in current.columns:
        st.error("CL32 data does not contain Activity ID.")
        return

    activity_id = (
        current["Activity ID"]
        .astype(str)
        .str.strip()
    )

    deliverable_mask = activity_id.str.match(
        r"^FER-[A-Z0-9]+-\d{4}$",
        case=False,
        na=False
    )

    deliverables = current[
        deliverable_mask
    ].copy()

    # =====================================================
    # NO DELIVERABLES
    # =====================================================

    if deliverables.empty:
        st.warning("No formal Ferry PS deliverables were found.")
        return

    # =====================================================
    # CONVERT DATA TYPES
    # =====================================================

    if "Activity % Complete" in deliverables.columns:

        deliverables["Activity % Complete"] = pd.to_numeric(
            deliverables["Activity % Complete"],
            errors="coerce"
        ).fillna(0)

    else:

        deliverables["Activity % Complete"] = 0

    if "Total Float" in deliverables.columns:

        deliverables["Total Float"] = pd.to_numeric(
            deliverables["Total Float"],
            errors="coerce"
        )

    else:

        deliverables["Total Float"] = pd.NA

    if "Finish" in deliverables.columns:

        deliverables["Finish"] = pd.to_datetime(
            deliverables["Finish"],
            errors="coerce"
        )

    if "BL1 Finish" in deliverables.columns:

        deliverables["BL1 Finish"] = pd.to_datetime(
            deliverables["BL1 Finish"],
            errors="coerce"
        )

    # =====================================================
    # CALCULATE STATUS
    # =====================================================

    deliverables["Status"] = deliverables.apply(
        calculate_status,
        axis=1
    )

    # =====================================================
    # PROJECT POSITION KPIs
    # =====================================================

    total_deliverables = len(deliverables)

    on_track = int(
        (deliverables["Status"] == "On Track").sum()
    )

    delayed = int(
        (deliverables["Status"] == "Delayed").sum()
    )

    at_risk = int(
        (deliverables["Status"] == "At Risk").sum()
    )

    next_7_days = count_next_7_days(
        deliverables
    )

    overall_status = calculate_overall_status(
        delayed,
        at_risk
    )

    # =====================================================
    # UNIT HEADER
    # =====================================================

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

    # =====================================================
    # KPI CARDS
    # =====================================================

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


# =========================================================
# STATUS LOGIC
# =========================================================

def calculate_status(row):

    finish = row.get("Finish")

    baseline = row.get("BL1 Finish")

    total_float = row.get("Total Float")

    completion = row.get(
        "Activity % Complete",
        0
    )

    today = pd.Timestamp.today().normalize()

    # -----------------------------------------------------
    # COMPLETION
    # -----------------------------------------------------

    try:

        completion = float(completion)

    except (TypeError, ValueError):

        completion = 0

    if completion >= 100:

        return "On Track"

    # -----------------------------------------------------
    # FLOAT
    # -----------------------------------------------------

    try:

        total_float = float(total_float)

    except (TypeError, ValueError):

        total_float = None

    # -----------------------------------------------------
    # PAST FINISH DATE
    # -----------------------------------------------------

    if pd.notna(finish):

        if finish < today:

            return "Delayed"

    # -----------------------------------------------------
    # FINISH DATE MOVEMENT
    # -----------------------------------------------------

    if pd.notna(finish) and pd.notna(baseline):

        movement = (
            finish - baseline
        ).days

        if movement > 0:

            if total_float is None:

                return "At Risk"

            if total_float <= 0:

                return "Delayed"

            if total_float <= 5:

                return "At Risk"

    # -----------------------------------------------------
    # LOW FLOAT
    # -----------------------------------------------------

    if total_float is not None:

        if total_float < 0:

            return "Delayed"

        if total_float <= 5:

            return "At Risk"

    # -----------------------------------------------------
    # NEXT 7 DAYS
    # -----------------------------------------------------

    if pd.notna(finish):

        days_to_finish = (
            finish - today
        ).days

        if 0 <= days_to_finish <= 7:

            if total_float is not None:

                if total_float <= 5:

                    return "At Risk"

    # -----------------------------------------------------
    # DEFAULT
    # -----------------------------------------------------

    return "On Track"


# =====================================================
# NEXT 7 DAYS
# =====================================================

def count_next_7_days(df):

    if "Finish" not in df.columns:

        return 0

    today = pd.Timestamp.today().normalize()

    end_date = (
        today
        + pd.Timedelta(days=7)
    )

    mask = (
        (df["Finish"] >= today)
        & (df["Finish"] <= end_date)
        & (df["Activity % Complete"] < 100)
    )

    return int(mask.sum())


# =====================================================
# OVERALL STATUS
# =====================================================

def calculate_overall_status(
    delayed,
    at_risk
):

    if delayed > 0:

        return "Delayed"

    if at_risk > 0:

        return "At Risk"

    return "On Track"


# =====================================================
# STATUS CLASS
# =====================================================

def get_status_class(status):

    if status == "On Track":

        return "healthy"

    if status == "At Risk":

        return "warning"

    if status == "Delayed":

        return "critical"

    return "neutral"


# =====================================================
# KPI CARD
# =====================================================

def render_kpi(
    label,
    value,
    card_class
):

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