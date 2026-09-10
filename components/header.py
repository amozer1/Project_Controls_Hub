import streamlit as st
from datetime import datetime


def render_header(framework, asset, page):

    today = datetime.today().strftime("%d %b %Y")

    st.markdown("""
    <style>

    .pc-header{
        background: linear-gradient(
            135deg,
            #005A2B 0%,
            #007A3D 100%
        );
        padding: 24px;
        border-radius: 18px;
        color: white;
        margin-bottom: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    }

    .pc-title{
        font-size:32px;
        font-weight:800;
        margin-bottom:4px;
    }

    .pc-subtitle{
        font-size:14px;
        opacity:0.9;
        margin-bottom:20px;
    }

    .pc-grid{
        display:flex;
        gap:18px;
        flex-wrap:wrap;
    }

    .pc-card{
        background:rgba(255,255,255,0.12);
        border:1px solid rgba(255,255,255,0.18);
        border-radius:12px;
        padding:12px 16px;
        min-width:180px;
    }

    .pc-label{
        font-size:12px;
        opacity:0.8;
        margin-bottom:4px;
    }

    .pc-value{
        font-size:16px;
        font-weight:700;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="pc-header">

            <div class="pc-title">
                Project Controls Hub
            </div>

            <div class="pc-subtitle">
                United Utilities · Delivery Performance · Communications · Programme Controls
            </div>

            <div class="pc-grid">

                <div class="pc-card">
                    <div class="pc-label">Framework</div>
                    <div class="pc-value">{framework}</div>
                </div>

                <div class="pc-card">
                    <div class="pc-label">Asset</div>
                    <div class="pc-value">{asset}</div>
                </div>

                <div class="pc-card">
                    <div class="pc-label">Current View</div>
                    <div class="pc-value">{page}</div>
                </div>

                <div class="pc-card">
                    <div class="pc-label">Date</div>
                    <div class="pc-value">{today}</div>
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )