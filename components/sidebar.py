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

    st.markdown(
        """
<style>

/* ==========================================================
SIDEBAR
========================================================== */

section[data-testid="stSidebar"]{
    background:
        radial-gradient(
            circle at top left,
            #12357f 0%,
            #08255a 35%,
            #041336 100%
        ) !important;

    border-right:1px solid rgba(255,255,255,.08);
}

section[data-testid="stSidebar"] > div{
    padding:18px 14px !important;
}


/* ==========================================================
CARDS
========================================================== */

section[data-testid="stSidebar"]
[data-testid="stVerticalBlockBorderWrapper"]{

    background:rgba(11,35,70,.72) !important;

    backdrop-filter:blur(12px);

    border:1px solid rgba(123,160,255,.12) !important;

    border-radius:14px !important;

    padding:14px !important;

    margin-bottom:14px !important;

    box-shadow:
        inset 0 1px rgba(255,255,255,.03),
        0 10px 25px rgba(0,0,0,.25);
}


/* ==========================================================
PROJECT HUB
========================================================== */

.hub{
    display:flex;
    align-items:center;
    gap:12px;
}

.hub-logo{
    width:48px;
    height:48px;

    border-radius:12px;

    background:
       linear-gradient(
         135deg,
         #2be68d,
         #286dff
       );

    display:flex;
    align-items:center;
    justify-content:center;

    color:white;
    font-size:22px;
    font-weight:700;
}

.hub-title{
    color:white;
    font-size:20px;
    line-height:20px;
    font-weight:700;
}

.hub-subtitle{
    color:#98b0dc;
    font-size:11px;
    margin-top:4px;
}


/* ==========================================================
SECTION TITLES
========================================================== */

.section-title{
    color:#c8d6ff;

    font-size:11px;

    text-transform:uppercase;

    letter-spacing:1px;

    font-weight:700;

    margin-bottom:10px;
}


/* ==========================================================
BUTTONS
========================================================== */

.stButton{
    width:100%;
}

.stButton > button{

    width:100% !important;

    min-height:38px !important;

    border-radius:10px !important;

    text-align:left !important;

    display:flex !important;

    justify-content:flex-start !important;

    font-size:13px !important;

    transition:.2s;
}

.stButton > button[kind="secondary"]{

    background:transparent !important;

    border:1px solid transparent !important;

    color:#d6e0f2 !important;
}

.stButton > button[kind="secondary"]:hover{

    background:rgba(255,255,255,.05) !important;

    border-color:rgba(255,255,255,.08) !important;

    color:white !important;
}

.stButton > button[kind="primary"]{

    background:
        linear-gradient(
            90deg,
            rgba(47,99,255,.55),
            rgba(47,99,255,.18)
        ) !important;

    border:1px solid rgba(91,148,255,.4) !important;

    color:white !important;

    font-weight:600 !important;
}


/* ==========================================================
USER CARD
========================================================== */

.avatar{

    width:42px;
    height:42px;

    background:
        linear-gradient(
            135deg,
            #275bff,
            #0f266e
        );

    border-radius:50%;

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
}

.user-role{
    color:#8fa8c9;
    font-size:11px;
}


/* ==========================================================
REMOVE BUTTON SHADOWS
========================================================== */

button{
    box-shadow:none !important;
}

</style>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# SIDEBAR
# ==========================================================

def render_sidebar():

    load_sidebar_css()

    with st.sidebar:

        # ======================================================
        # PROJECT HUB
        # ======================================================

        with st.container(border=True):

            st.markdown(
                """
                <div class="hub">
                    <div class="hub-logo">◉</div>

                    <div>
                        <div class="hub-title">
                            PROJECT<br>
                            CONTROLS HUB
                        </div>

                        <div class="hub-subtitle">
                            Design Management Intelligence
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # ======================================================
        # ENTERPRISE FRAMEWORK
        # ======================================================

        with st.container(border=True):

            st.markdown(
                '<div class="section-title">UU Enterprise Framework</div>',
                unsafe_allow_html=True,
            )

            for asset in FRAMEWORKS["UU Enterprise Framework"]:

                selected = (
                    st.session_state.get("selected_framework")
                    == "UU Enterprise Framework"
                    and
                    st.session_state.get("selected_asset")
                    == asset
                )

                st.button(
                    f"{'●' if selected else '○'}  {asset}",
                    key=f"ent_{asset}",
                    use_container_width=True,
                    type="primary" if selected else "secondary",
                    on_click=_select_asset,
                    args=("UU Enterprise Framework", asset),
                )

        # ======================================================
        # DDB FRAMEWORK
        # ======================================================

        with st.container(border=True):

            st.markdown(
                '<div class="section-title">UU DD&B Framework</div>',
                unsafe_allow_html=True,
            )

            for asset in FRAMEWORKS["UU DD&B Framework"]:

                selected = (
                    st.session_state.get("selected_framework")
                    == "UU DD&B Framework"
                    and
                    st.session_state.get("selected_asset")
                    == asset
                )

                st.button(
                    f"{'●' if selected else '○'}  {asset}",
                    key=f"ddb_{asset}",
                    use_container_width=True,
                    type="primary" if selected else "secondary",
                    on_click=_select_asset,
                    args=("UU DD&B Framework", asset),
                )

        # ======================================================
        # NAVIGATION
        # ======================================================

        with st.container(border=True):

            st.markdown(
                '<div class="section-title">Navigation</div>',
                unsafe_allow_html=True,
            )

            for item, icon in NAVIGATION_ITEMS:

                selected = (
                    st.session_state.get(
                        "selected_navigation",
                        "Overview"
                    )
                    == item
                )

                st.button(
                    f"{icon}  {item}",
                    key=f"nav_{item}",
                    use_container_width=True,
                    type="primary" if selected else "secondary",
                    on_click=_select_navigation,
                    args=(item,),
                )

        # ======================================================
        # USER PROFILE
        # ======================================================

        with st.container(border=True):

            c1, c2 = st.columns([1, 4])

            with c1:
                st.markdown(
                    """
                    <div class="avatar">
                        JS
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with c2:
                st.markdown(
                    """
                    <div class="user-name">
                        John Smith
                    </div>

                    <div class="user-role">
                        Design Manager
                    </div>
                    """,
                    unsafe_allow_html=True,
                )