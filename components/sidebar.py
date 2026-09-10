import streamlit as st
from config.frameworks import FRAMEWORKS


# ==========================================================
# NAVIGATION ITEMS
# ==========================================================

NAVIGATION_ITEMS = [
    ("Overview", "⌂"),
    ("Programme", "▤"),
    ("Delivery & Programme", "▱"),
    ("Communications", "◌"),
    ("Documents", "□"),
    ("Intelligence", "✦"),
    ("Reports", "▥"),
    ("Settings", "⚙"),
]


# ==========================================================
# SESSION DEFAULTS
# ==========================================================

if "selected_framework" not in st.session_state:
    st.session_state.selected_framework = "UU DD&B Framework"

if "selected_asset" not in st.session_state:
    st.session_state.selected_asset = "Ferry PS"

if "selected_navigation" not in st.session_state:
    st.session_state.selected_navigation = "Overview"


# ==========================================================
# CALLBACKS
# ==========================================================

def _select_asset(framework, asset):
    st.session_state.selected_framework = framework
    st.session_state.selected_asset = asset
    st.session_state.selected_navigation = "Overview"


def _select_navigation(item):
    st.session_state.selected_navigation = item


# ==========================================================
# CSS
# ==========================================================

def load_sidebar_css():

    st.markdown(
        """
        <style>

        /* --------------------------------------------------
        Sidebar Width
        -------------------------------------------------- */

        section[data-testid="stSidebar"]{
            min-width:320px !important;
            max-width:320px !important;

            background:
                radial-gradient(
                    circle at top left,
                    #10367d 0%,
                    #09255b 35%,
                    #041335 100%
                ) !important;

            border-right:1px solid rgba(255,255,255,.08);
        }

        section[data-testid="stSidebar"] > div{
            padding:18px 14px !important;
        }

        /* --------------------------------------------------
        Cards
        -------------------------------------------------- */

        section[data-testid="stSidebar"]
        [data-testid="stVerticalBlockBorderWrapper"]{

            background:rgba(10,29,73,.76) !important;

            border:1px solid rgba(103,147,255,.12) !important;

            border-radius:14px !important;

            padding:14px !important;

            margin-bottom:14px !important;

            backdrop-filter:blur(12px);

            box-shadow:
                inset 0 1px rgba(255,255,255,.03),
                0 8px 22px rgba(0,0,0,.25);
        }

        /* --------------------------------------------------
        Hub
        -------------------------------------------------- */

        .hub-header{
            display:flex;
            align-items:center;
            gap:14px;
        }

        .hub-logo{
            width:52px;
            height:52px;

            border-radius:14px;

            background:
                linear-gradient(
                    135deg,
                    #27db89,
                    #2869ff
                );

            display:flex;
            align-items:center;
            justify-content:center;

            font-size:24px;
            color:white;
        }

        .hub-title{
            color:white;

            font-size:20px;

            font-weight:700;

            line-height:22px;

            margin:0;
        }

        .hub-subtitle{
            color:#93add9;

            font-size:11px;

            margin-top:4px;
        }

        /* --------------------------------------------------
        Section Labels
        -------------------------------------------------- */

        .section-title{
            color:#bdd0f8;

            font-size:11px;

            font-weight:700;

            text-transform:uppercase;

            letter-spacing:1px;

            margin-bottom:10px;
        }

        /* --------------------------------------------------
        Buttons
        -------------------------------------------------- */

        .stButton{
            width:100%;
        }

        .stButton > button{

            width:100% !important;

            min-height:40px !important;

            border-radius:10px !important;

            display:flex !important;

            justify-content:flex-start !important;

            align-items:center !important;

            padding-left:14px !important;

            text-align:left !important;

            font-size:13px !important;

            transition:.2s;
        }

        .stButton > button p{
            text-align:left !important;
            width:100%;
        }

        .stButton > button[kind="secondary"]{

            background:transparent !important;

            border:1px solid transparent !important;

            color:#d3def4 !important;
        }

        .stButton > button[kind="secondary"]:hover{

            background:rgba(255,255,255,.05) !important;

            border-color:rgba(255,255,255,.08) !important;
