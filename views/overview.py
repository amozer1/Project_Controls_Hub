import streamlit as st
import pandas as pd


# ==========================================================
# OVERVIEW — PROJECT POSITION
# ==========================================================

def load_overview_styles():
    """
    Overview-only styling.
    This does NOT modify the existing sidebar CSS.
    """

    st.markdown(
        """
        <style>

        /* ==================================================
           PROJECT POSITION CONTAINER
           ================================================== */

        .overview-position {
            background: #ffffff;
            border: 1px solid #dce5ee;
            border-radius: 10px;
            padding: 20px 22px 18px 22px;
            margin-top: 8px;
            margin-bottom: 18px;
            box-shadow: 0 2px 8px rgba(15, 43, 70, 0.04);
        }


        /* ==================================================
           SECTION TITLE
           ================================================== */

        .overview-section-title {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 18px;
        }

        .overview-section-title::before {
            content: "";
            width: 3px;
            height: 20px;
            background: #0878d1;
            border-radius: 3px;
        }

        .overview-section-title span {
            font-size: 14px;
            font-weight: 700;
            letter-spacing: 0.02em;
            color: #123b63;
        }


        /* ==================================================
           KPI GRID
           ================================================== */

        .position-grid {
            display: grid;
            grid-template-columns: 1.35fr repeat(4, 1fr);
            min-height: 96px;
        }


        /* ==================================================
           KPI
           ================================================== */

        .position-kpi {
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 8px 22px;
            border-left: 1px solid #e1e8ef;
        }

        .position-kpi:first-child {
            border-left: none;
            padding-left: 4px;
        }


        /* ==================================================
           OVERALL STATUS
           ================================================== */

        .position-status {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .status-indicator {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            flex-shrink: 0;
        }

        .status-indicator.green {
            background: #16a673;
        }

        .status-indicator.amber {
            background: #f5a623;
        }

        .status-indicator.red {
            background: #e74c3c;
        }

        .status-indicator.neutral {
            background: #b8c4cf;
        }


        /* ==================================================
           STATUS TEXT
           ================================================== */

        .status-value {
            font-size: 25px;
            line-height: 1;
            font-weight: 800;
        }

        .status-value.green {
            color: #128c62;
        }

        .status-value.amber {
            color: #e99a16;
        }

        .status-value.red {
            color: #d83b32;
        }

        .status-value.neutral {
            color: #6f7d8b;
        }

        .status-label {
            margin-top: 6px;
            font-size: 12px;
            color: #607286;
        }


        /* ==================================================
           KPI NUMBERS
           ================================================== */

        .position-number {
            font-size: 27px;
            line-height: 1;
            font-weight: 800;
            color: #123b63;
            letter-spacing: -0.02em;
        }

        .position-label {
            margin-top: 7px;
            font-size: 12px;
            font-weight: 600;
            color: #53677b;
        }

        .position-support {
            margin-top: 6px;
            font-size: 11px;
            color: #7b8b9b;
        }

        .position-support.on-track {
            color: #11966b;
            font-weight: 600;
        }

        .position-support.delayed {
            color: #d83b32;
            font-weight: 600;
        }

        .position-support.risk {
            color: #e49a13;
            font-weight: 600;
        }

        .position-support.next {
            color: #0878d1;
            font-weight: 600;
        }


        /* ==================================================
           RESPONSIVE
           ================================================== */

        @media (max-width: 1100px) {

            .position-grid {
                grid-template-columns: repeat(4, 1fr);
                row-gap: 16px;
            }

            .position-kpi:first-child {
                grid-column: span 4;
                border-bottom: 1px solid #e1e8ef;
                padding-bottom: 16px;
            }

            .position-kpi:nth-child(2) {
                border-left: none;
            }
        }


        @media (max-width: 700px) {

            .position-grid {
                grid-template-columns: 1fr 1fr;
            }

            .position-kpi:first-child {
                grid-column: span 2;
            }

            .position-kpi:nth-child(2),
            .position-kpi:nth-child(4) {
                border-left: none;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# PROJECT POSITION CALCULATION
# ==========================================================

def calculate_project_position(df):
    """
    Calculate the Project Position from CL32 data.

    This function is designed to receive the standardised
    dataframe from the programme loader.

    No project figures are hardcoded here.
    """

    if df is None or df.empty:
        return {
            "status": "Neutral",
            "total": None,
            "on_track": None,
            "delayed": None,
            "at_risk": None,
            "next_7_days": None,
        }

    data = df.copy()

    # ------------------------------------------------------
    # Clean column names
    # ------------------------------------------------------

    data.columns = [
        str(column).strip()
        for column in data.columns
    ]

    # ------------------------------------------------------
    # Activity ID
    # ------------------------------------------------------

    if "Activity ID" in data.columns:

        activity_id = (
            data["Activity ID"]
            .astype(str)
            .str.strip()
        )

        data = data[
            (activity_id != "")
            & (activity_id.str.lower() != "nan")
        ].copy()

    # ------------------------------------------------------
    # Completion
    # ------------------------------------------------------

    if "Activity % Complete" in data.columns:

        data["Activity % Complete"] = pd.to_numeric(
            data["Activity % Complete"],
            errors="coerce"
        ).fillna(0)

    else:

        data["Activity % Complete"] = 0

    # ------------------------------------------------------
    # Total Float
    # ------------------------------------------------------

    if "Total Float" in data.columns:

        data["Total Float"] = pd.to_numeric(
            data["Total Float"],
            errors="coerce"
        )

    else:

        data["Total Float"] = pd.NA

    # ------------------------------------------------------
    # Total deliverables
    # ------------------------------------------------------

    total = len(data)

    if total == 0:

        return {
            "status": "Neutral",
            "total": 0,
            "on_track": 0,
            "delayed": 0,
            "at_risk": 0,
            "next_7_days": 0,
        }

    # ------------------------------------------------------
    # Completed
    # ------------------------------------------------------

    completed = data[
        data["Activity % Complete"] >= 100
    ]

    # ------------------------------------------------------
    # Delayed
    #
    # First control definition:
    # negative float = delayed
    # ------------------------------------------------------

    delayed = data[
        (data["Activity % Complete"] < 100)
        & (data["Total Float"] < 0)
    ]

    # ------------------------------------------------------
    # At Risk
    #
    # Active activities with 0–5 days float.
    # ------------------------------------------------------

    at_risk = data[
        (data["Activity % Complete"] < 100)
        & (data["Total Float"].notna())
        & (data["Total Float"] >= 0)
        & (data["Total Float"] <= 5)
    ]

    # ------------------------------------------------------
    # On Track
    # ------------------------------------------------------

    on_track = (
        total
        - len(completed)
        - len(delayed)
        - len(at_risk)
    )

    on_track = max(on_track, 0)

    # ------------------------------------------------------
    # Overall project status
    # ------------------------------------------------------

    if len(delayed) > 0:
        status = "Red"

    elif len(at_risk) > 0:
        status = "Amber"

    else:
        status = "Green"

    return {
        "status": status,
        "total": total,
        "on_track": on_track,
        "delayed": len(delayed),
        "at_risk": len(at_risk),
        "next_7_days": None,
    }


# ==========================================================
# DISPLAY HELPERS
# ==========================================================

def display_value(value):

    if value is None:
        return "—"

    return f"{value:,}"


def get_status_class(status):

    status = str(status).lower()

    if status == "green":
        return "green"

    if status == "amber":
        return "amber"

    if status == "red":
        return "red"

    return "neutral"


# ==========================================================
# UNIT 1 — PROJECT POSITION
# ==========================================================

def render_project_position(metrics):

    status = metrics.get("status", "Neutral")

    status_class = get_status_class(status)

    total = metrics.get("total")
    on_track = metrics.get("on_track")
    delayed = metrics.get("delayed")
    at_risk = metrics.get("at_risk")
    next_7_days = metrics.get("next_7_days")

    st.markdown(
        f"""
        <section class="overview-position">

            <div class="overview-section-title">
                <span>PROJECT POSITION</span>
            </div>

            <div class="position-grid">


                <!-- ======================================
                     OVERALL STATUS
                     ====================================== -->

                <div class="position-kpi">

                    <div class="position-status">

                        <div class="status-indicator {status_class}">
                        </div>

                        <div>

                            <div class="status-value {status_class}">
                                {status.upper()}
                            </div>

                            <div class="status-label">
                                Overall Status
                            </div>

                        </div>

                    </div>

                </div>


                <!-- ======================================
                     TOTAL DELIVERABLES
                     ====================================== -->

                <div class="position-kpi">

                    <div class="position-number">
                        {display_value(total)}
                    </div>

                    <div class="position-label">
                        Total Deliverables
                    </div>

                    <div class="position-support on-track">
                        {display_value(on_track)} On Track
                    </div>

                </div>


                <!-- ======================================
                     DELAYED
                     ====================================== -->

                <div class="position-kpi">

                    <div class="position-number">
                        {display_value(delayed)}
                    </div>

                    <div class="position-label">
                        Delayed
                    </div>

                    <div class="position-support delayed">
                        {display_value(delayed)} items
                    </div>

                </div>


                <!-- ======================================
                     AT RISK
                     ====================================== -->

                <div class="position-kpi">

                    <div class="position-number">
                        {display_value(at_risk)}
                    </div>

                    <div class="position-label">
                        At Risk
                    </div>

                    <div class="position-support risk">
                        {display_value(at_risk)} items
                    </div>

                </div>


                <!-- ======================================
                     NEXT 7 DAYS
                     ====================================== -->

                <div class="position-kpi">

                    <div class="position-number">
                        {display_value(next_7_days)}
                    </div>

                    <div class="position-label">
                        Next 7 Days
                    </div>

                    <div class="position-support next">
                        Upcoming deliverables
                    </div>

                </div>


            </div>

        </section>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# MAIN OVERVIEW
# ==========================================================

def render_overview(df=None):

    # Load Overview-only styling
    load_overview_styles()

    # ------------------------------------------------------
    # PAGE HEADER
    # ------------------------------------------------------

    st.markdown(
        """
        <div style="
            margin-bottom: 18px;
        ">

            <div style="
                font-size: 28px;
                font-weight: 800;
                color: #123b63;
                line-height: 1.1;
            ">
                Ferry PS
            </div>

            <div style="
                font-size: 15px;
                color: #607286;
                margin-top: 5px;
            ">
                Deliverables Project Controls
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # ------------------------------------------------------
    # CALCULATE PROJECT POSITION
    # ------------------------------------------------------

    metrics = calculate_project_position(df)

    # ------------------------------------------------------
    # UNIT 1
    # ------------------------------------------------------

    render_project_position(metrics)