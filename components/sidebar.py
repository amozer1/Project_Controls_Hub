import streamlit as st
from config.frameworks import FRAMEWORKS

# ==========================================================
# NAVIGATION
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
    css = """
    <style>

    section[data-testid="stSidebar"]{
        min-width:320px !important;
        max-width:320px !important;

        background:
            radial-gradient(
                circle at top left,
                #12367b 0%,
                #08245a 35%,
                #041332 100%
            ) !important;
    }

    section[data-testid="stSidebar"] > div{
        padding:16px !important;
    }

    [data-testid="stVerticalBlockBorderWrapper"]{
        background:rgba(10,25,65,.75) !important;
        border:1px solid rgba(255,255,255,.08) !important;
        border-radius:14px !important;
        padding:14px !important;
        margin-bottom:14px !important;
    }

    .hub-header{
        display:flex;
        align-items:center;
        gap:12px;
    }

    .hub-logo{
        width:52px;
        height:52px;

        border-radius:12px;

        background:
            linear-gradient(
                135deg,
                #22d68a,
                #2967ff
            );

        display:flex;
        align-items:center;
        justify-content:center;

        color:white;
        font-size:22px;
    }

    .hub-title{
        color:white;
        font-size:18px;
        font-weight:700;
        line-height:20px;
    }

    .hub-subtitle{
        color:#9bb3d9;
        font-size:11px;
        margin-top:4px;
    }

    .section-title{
        color:#c0d2ff;
        font-size:11px;
        font-weight:700;
        letter-spacing:1px;
        text-transform:uppercase;
        margin-bottom:10px;
    }

    .stButton > button{
        width:100% !important;
        min-height:40px !important;

        border-radius:10px !important;

        text-align:left !important;

        display:flex !important;
        justify-content:flex-start !important;

        font-size:13px !important;
    }

    .stButton > button[kind="secondary"]{
        background:transparent !important;
        border:1px solid transparent !important;
        color:#dce5f8 !important;
    }

    .stButton > button[kind="secondary"]:hover{
        background:rgba(255,255,255,.05) !important;
        border:1px solid rgba(255,255,255,.08) !important;
    }

    .stButton > button[kind="primary"]{
        background:
            linear-gradient(
                90deg,
                rgba(38,95,255,.55),
                rgba(38,95,255,.15)
            ) !important;

        border:1px solid rgba(90,145,255,.35) !important;
        color:white !important;
    }

    .avatar{
        width:44px;
        height:44px;

        border-radius:50%;

        background:
            linear-gradient(
                135deg,
                #3366ff,
                #112a70
            );

        display:flex;
        align-items:center;
        justify-content:center;

        color:white;
        font-weight:700;
    }

    .user-name{
        color:white;
        font-size:13px;
        font-weight:600;
        margin-top:4px;
    }

    .user-role{
        color:#90a7cd;
        font-size:11px;
    }

    </style>
    """

    st.markdown(css, unsafe_allow_html=True)


# ==========================================================
# SIDEBAR
# ==========================================================

def render_sidebar():
    load_sidebar_css()

    with st.sidebar:

        # HUB

        with st.container(border=True):

            st.markdown(
                """
                <div class="hub-header">

                    <div class="hub-logo">
                        ⬢
                    </div>

                    <div>
                        <div class="hub-title">
                            PROJECT CONTROLS HUB
                        </div>

                        <div class="hub-subtitle">
                            Design Management Intelligence
                        </div>
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

        # UU ENTERPRISE

        with st.container(border=True):

            st.markdown(
                '<div class="section-title">UU Enterprise Framework</div>',
                unsafe_allow_html=True,
            )

            for asset in FRAMEWORKS.get("UU Enterprise Framework", []):
                selected = (
                        st.session_state.get("selected_framework")
                        == "UU Enterprise Framework"
                        and
                        st.session_state.get("selected_asset") == asset
                )

                st.button(
                    f"{'●' if selected else '○'}  {asset}",
                    key=f"enterprise_{asset}",
                    type="primary" if selected else "secondary",
                    use_container_width=True,
                    on_click=_select_asset,
                    args=("UU Enterprise Framework", asset),
                )

        # DD&B

        with st.container(border=True):

            st.markdown(
                '<div class="section-title">UU DD&B Framework</div>',
                unsafe_allow_html=True,
            )

            for asset in FRAMEWORKS.get("UU DD&B Framework", []):
                selected = (
                        st.session_state.get("selected_framework")
                        == "UU DD&B Framework"
                        and
                        st.session_state.get("selected_asset") == asset
                )

                st.button(
                    f"{'●' if selected else '○'}  {asset}",
