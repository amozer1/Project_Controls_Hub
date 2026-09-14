import streamlit as st
import pandas as pd

from loaders.ferry_loader import load_ferry


# =========================================================
# UNIT 01 — PROJECT POSITION
# =========================================================

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
    # CHECK CL32 DATA
    # =====================================================

    if cl32 is None or cl32.empty:
        st.warning("No CL32 Ferry PS programme data available.")
        return

    # =====================================================
    # CLEAN COLUMN NAMES
    # =====================================================

    cl32.columns = [
        str(column).strip()
        for column in cl32.columns
    ]

    # =====================================================
    # CHECK SNAPSHOT DATE
    # =====================================================

    if "SnapshotDate" not in cl32.columns:
        st.error("CL32 data does not contain SnapshotDate.")
        return

    # =====================================================
    # GET LATEST CL32 SNAPSHOT
    # =====================================================

    latest_snapshot = cl32["SnapshotDate"].max()

    current = cl32[
        cl32["SnapshotDate"] == latest_snapshot
    ].copy()

    if current.empty:
        st.warning("No current Ferry PS CL32 data available.")
        return

    # =====================================================
    # CHECK ACTIVITY ID
    # =====================================================

    if "Activity ID" not in current.columns:
        st.error("CL32 data does not contain Activity ID.")
        return

    # =====================================================
    # REMOVE RETIRED ACTIVITIES
    # =====================================================

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
    # CHECK DELIVERABLES
    # =====================================================

    if deliverables.empty:
        st.warning(
            "No formal Ferry PS deliverables were found."
        )
        return

    # =====================================================
    # CLEAN % COMPLETE
    # =====================================================

    if "Activity % Complete" in deliverables.columns:

        deliverables["Activity % Complete"] = pd.to_numeric(
            deliverables["Activity % Complete"],
            errors="coerce"
        ).fillna(0)

    else:

        deliverables["Activity % Complete"] = 0

    # =====================================================
    # CLEAN TOTAL FLOAT
    # =====================================================

    if "Total Float" in deliverables.columns:

        deliverables["Total Float"] = pd.to_numeric(
            deliverables["Total Float"],
            errors="coerce"
        )

    else:

        deliverables["Total Float"] = pd.NA

    # =====================================================
    # CLEAN FINISH
    # =====================================================

    if "Finish" in deliverables.columns:

        deliverables["Finish"] = pd.to_datetime(
            deliverables["Finish"],
            errors="coerce"
        )

    else:

        deliverables["Finish"] = pd.NaT

    # =====================================================
    # CLEAN BASELINE FINISH
    # =====================================================

    if "BL1 Finish" in deliverables.columns:

        deliverables["BL1 Finish"] = pd.to_datetime(
            deliverables["BL1 Finish"],
            errors="coerce"
        )

    else:

        deliverables["BL1 Finish"] = pd.NaT

    # =====================================================
    # CALCULATE STATUS
    # =====================================================

    deliverables["Status"] = deliverables.apply(
        calculate_status,
        axis=1
    )

    # =====================================================
    # KPI VALUES
    # =====================================================

    total_deliverables = len(deliverables)

    on_track = int(
        (
            deliverables["Status"] == "On Track"
        ).sum()
    )

    delayed = int(
        (
            deliverables["Status"] == "Delayed"
        ).sum()
    )

    at_risk = int(
        (
            deliverables["Status"] == "At Risk"
        ).sum()
    )

    next_7_days = count_next_7_days(
        deliverables
    )

    overall_status = calculate_overall_status(
        delayed,
        at_risk
    )

    # =====================================================
    # SECTION HEADER
    # =====================================================

    st.markdown(
        "### PROJECT POSITION"
    )

    st.caption(
        "Ferry PS  ·  Where are we?"
    )

    # =====================================================
    # KPI ROW
    # =====================================================

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:

        st.metric(
            label="Overall Status",
            value=overall_status
        )

    with col2:

        st.metric(
            label="Total Deliverables",
            value=total_deliverables
        )

    with col3:

        st.metric(
            label="On Track",
            value=on_track
        )

    with col4:

        st.metric(
            label="Delayed",
            value=delayed
        )

    with col5:

        st.metric(
            label="At Risk",
            value=at_risk
        )

    with col6:

        st.metric(
            label="Next 7 Days",
            value=next_7_days
        )


# =========================================================
# STATUS LOGIC
# =========================================================

def calculate_status(row):

    finish = row.get(
        "Finish",
        pd.NaT
    )

    baseline = row.get(
        "BL1 Finish",
        pd.NaT
    )

    total_float = row.get(
        "Total Float",
        pd.NA
    )

    completion = row.get(
        "Activity % Complete",
        0
    )

    today = pd.Timestamp.today().normalize()

    # =====================================================
    # COMPLETION
    # =====================================================

    try:

        completion = float(completion)

    except (
        TypeError,
        ValueError
    ):

        completion = 0

    if completion >= 100:
        return "On Track"

    # =====================================================
    # FLOAT
    # =====================================================

    try:

        if pd.isna(total_float):

            total_float = None

        else:

            total_float = float(total_float)

    except (
        TypeError,
        ValueError
    ):

        total_float = None

    # =====================================================
    # PAST FINISH
    # =====================================================

    if pd.notna(finish):

        if finish < today:
            return "Delayed"

    # =====================================================
    # FINISH MOVEMENT
    # =====================================================

    if (
        pd.notna(finish)
        and pd.notna(baseline)
    ):

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

    # =====================================================
    # FLOAT POSITION
    # =====================================================

    if total_float is not None:

        if total_float < 0:
            return "Delayed"

        if total_float <= 5:
            return "At Risk"

    # =====================================================
    # NEXT 7 DAYS
    # =====================================================

    if pd.notna(finish):

        days_to_finish = (
            finish - today
        ).days

        if (
            0
            <= days_to_finish
            <= 7
        ):

            if total_float is not None:

                if total_float <= 5:
                    return "At Risk"

    # =====================================================
    # DEFAULT
    # =====================================================

    return "On Track"


# =========================================================
# NEXT 7 DAYS
# =========================================================

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
        &
        (df["Finish"] <= end_date)
        &
        (df["Activity % Complete"] < 100)
    )

    return int(
        mask.sum()
    )


# =========================================================
# OVERALL STATUS
# =========================================================

def calculate_overall_status(
    delayed,
    at_risk
):

    if delayed > 0:
        return "Delayed"

    if at_risk > 0:
        return "At Risk"

    return "On Track"