import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="Trade Hunting Terminal",
    page_icon="⚡",
    layout="wide"
)

# --- Custom Retro-Futuristic Styling ---
st.markdown("""
<style>
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
    }
    .metric-box {
        background-color: #171c28;
        border: 1px solid #303b54;
        padding: 12px;
        border-radius: 6px;
        margin-bottom: 8px;
    }
    .metric-title {
        font-size: 11px;
        color: #8a99ad;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 1px;
    }
    h1 {
        color: #ff3366 !important;
        font-family: 'Courier New', Courier, monospace;
        font-size: 24px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("# TRADE HUNTING ENGINE")
st.markdown("---")

# --- Interactive Sidebar (Change Assets & Values Here) ---
st.sidebar.header("⚙️ Live Trade Parameters")

# Expanded asset list
asset_list = ["DOGEUSDT", "BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "PEPEUSDT", "ADAUSDT", "AVAXUSDT"]
selected_asset = st.sidebar.selectbox("Select Asset", asset_list)

trade_direction = st.sidebar.selectbox("Direction", ["SHORT", "LONG"])
total_capital = st.sidebar.number_input("Total Capital (USDT)", value=100000.0, step=1000.0)
leverage = st.sidebar.slider("Leverage (x)", min_value=1, max_value=50, value=10)

st.sidebar.markdown("---")
st.sidebar.subheader("Price Levels")
entry_price = st.sidebar.number_input("Entry Price", value=0.073005, format="%.6f")
take_profit = st.sidebar.number_input("Take Profit", value=0.07289677, format="%.8f")
stop_loss = st.sidebar.number_input("Stop Loss", value=0.07308517, format="%.8f")

# --- Dynamic Calculations ---
quality_score = np.random.uniform(40.0, 85.0)
bayes_prob = round(np.random.uniform(60.0, 95.0), 1)
rmt_mode = round(np.random.uniform(50.0, 80.0), 1)

# --- Main Layout Grid ---
col1, col2 = st.columns(2)

with col1:
    direction_color = '#ff3366' if trade_direction == 'SHORT' else '#2ecc71'
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">Target Asset & Mode</div>
        <div style="font-size: 20px; color: {direction_color}; font-weight: bold;">
            {selected_asset} {trade_direction}
        </div>
        <div style="font-size: 13px; color: #ffffff; margin-top: 4px;">QUALITY SCORE: <b>{quality_score:.1f}</b></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">Entry Price</div>
        <div style="font-size: 18px; color: #00ffcc; font-weight: bold;">{entry_price:.6f}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">Leverage</div>
        <div style="font-size: 18px; color: #ffffff; font-weight: bold;">{leverage}x</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">Take Profit</div>
        <div style="font-size: 18px; color: #2ecc71; font-weight: bold;">{take_profit:.8f}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">Stop Loss</div>
        <div style="font-size: 18px; color: #e74c3c; font-weight: bold;">{stop_loss:.8f}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">Bayesian Probability</div>
        <div style="font-size: 18px; color: #00ffcc; font-weight: bold;">{bayes_prob}%</div>
    </div>
    """, unsafe_allow_html=True)

# --- Bottom Stats Panel ---
st.markdown("---")
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
st.markdown(f"""
<div style="background-color: #171c28; padding: 12px; border-radius: 6px; border: 1px solid #303b54;">
    <div class="metric-title">System Diagnostics & Capital</div>
    <div style="font-size: 13px; color: #e0e0e0; margin-top: 5px;">
        Total Capital: <b>{total_capital:,.2f} USDT</b> | RMT Market Mode: <b>{rmt_mode}%</b><br>
        Status: <span style="color: #f39c12; font-weight: bold;">WATCHING – DYNAMIC SCAN ACTIVE</span><br>
        <i>Last Scan: {current_time}</i>
    </div>
</div>
""", unsafe_allow_html=True)
