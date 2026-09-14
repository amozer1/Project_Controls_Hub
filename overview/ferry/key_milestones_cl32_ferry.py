import streamlit as st
import pandas as pd


def render(df):

    # ==================================================
    # VALIDATION
    # ==================================================

    if df is None or df.empty:
        st.warning("No programme data available.")
        return

    df = df.copy()

    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
    )

    required_columns = [
        "Activity Name",
        "Finish",
        "BL1 Finish",
        "Total Float",
        "Activity % Complete"
    ]

    missing = [
        col
        for col in required_columns
        if col not in df.columns
    ]

    if missing:

        st.error(
            f"Missing columns: {', '.join(missing)}"
        )

        return

    # ==================================================
    # DATA CLEANING
    # ==================================================

    df["Finish"] = pd.to_datetime(
        df["Finish"],
        errors="coerce",
        dayfirst=True
    )

    df["BL1 Finish"] = pd.to_datetime(
        df["BL1 Finish"],
        errors="coerce",
        dayfirst=True
    )

    df["Total Float"] = pd.to_numeric(
        df["Total Float"],
        errors="coerce"
    )

    df["Activity % Complete"] = (
        df["Activity % Complete"]
        .astype(str)
        .str.replace("%", "", regex=False)
        .str.strip()
    )

    df["Activity % Complete"] = pd.to_numeric(
        df["Activity % Complete"],
        errors="coerce"
    ).fillna(0)

    # ==================================================
    # PROGRAMME KPI
    # ==================================================

    baseline_finish = df["BL1 Finish"].max()

    forecast_finish = df["Finish"].max()

    variance_days = int(
        (forecast_finish - baseline_finish).days
    )

    terminal_float = int(
        df["Total Float"].min()
    )

    incomplete_df = df[
        df["Activity % Complete"] < 100
    ]

    outstanding_count = len(
        incomplete_df
    )

    # ==================================================
    # HEALTH
    # ==================================================

    if variance_days <= 7 and terminal_float > 0:

        health = "GREEN"
        colour = "#22c55e"

    elif variance_days <= 28:

        health = "AMBER"
        colour = "#f59e0b"

    else:

        health = "RED"
        colour = "#ef4444"

    # ==================================================
    # CURRENT STAGE
    # ==================================================

    current_stage = "Outline Design"

    # ==================================================
    # NEXT GATE
    # ==================================================

    next_gate = "Submission of Outline Design Pack"

    gate_df = df[
        df["Activity Name"]
        .astype(str)
        .str.contains(
            "Submission of Outline Design Pack",
            case=False,
            na=False
        )
    ]

    if not gate_df.empty:

        if gate_df["Activity % Complete"].max() >= 100:

            next_gate = "Client Review of Design Pack"

    # ==================================================
    # PRIMARY DRIVER
    # ==================================================

    primary_driver = "Programme Delivery"

    if (
        "Variance - BL1 Finish Date"
        in df.columns
    ):

        df["Variance - BL1 Finish Date"] = pd.to_numeric(
            df["Variance - BL1 Finish Date"],
            errors="coerce"
        )

        driver_df = df[
            (
                df["Activity % Complete"] < 100
            )
            &
            (
                df["Variance - BL1 Finish Date"] < 0
            )
        ]

        if not driver_df.empty:

            primary_driver = (
                driver_df
                .sort_values(
                    "Total Float",
                    ascending=True
                )
                .iloc[0]["Activity Name"]
            )

    # ==================================================
    # INSIGHT
    # ==================================================

    insight = (
        f"The project is in {current_stage}. "
        f"'{primary_driver}' is currently the "
        f"primary driver of delay. "
        f"{outstanding_count} activities remain "
        f"incomplete and terminal float is "
        f"{terminal_float} days."
    )

    # ==================================================
    # RECOMMENDED ACTION
    # ==================================================

    if terminal_float <= 0:

        action = (
            "Recover critical path activities and "
            "complete outstanding outline design "
            "deliverables."
        )

    elif variance_days > 14:

        action = (
            "Prioritise delayed activities and "
            "implement recovery actions."
        )

    else:

        action = (
            "Maintain delivery momentum and continue "
            "progress monitoring."
        )

    # ==================================================
    # DISPLAY
    # ==================================================

    st.write(
        {
            "health": health,
            "current_stage": current_stage,
            "next_gate": next_gate,
            "baseline_finish": baseline_finish,
            "forecast_finish": forecast_finish,
            "variance_days": variance_days,
            "terminal_float": terminal_float,
            "primary_driver": primary_driver,
            "insight": insight,
            "recommended_action": action
        }
    )