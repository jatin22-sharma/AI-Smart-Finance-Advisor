import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../"
        )
    )
)

from auth import check_login

if not check_login():

    st.error("🔒 Please login first.")

    st.stop()
# ==========================================
# PAGE TITLE
# ==========================================

st.title("📈 Real-Time Stock Market Analyzer")

st.markdown("""
Analyze real-time stock market data using AI Smart Finance Advisor.

Popular Indian Stocks:
- RELIANCE.NS
- TCS.NS
- INFY.NS
- HDFCBANK.NS
- ITC.NS
""")

# ==========================================
# STOCK INPUT
# ==========================================

ticker = st.text_input(
    "Enter Stock Symbol",
    value="RELIANCE.NS"
)

search = st.button(
    "🔍 Analyze Stock"
)

# ==========================================
# STOCK ANALYSIS
# ==========================================

if search:

    try:

        # Download stock data

        stock = yf.Ticker(ticker)

        info = stock.info

        history = stock.history(period="6mo")

        # ==========================================
        # BASIC INFO
        # ==========================================

        st.subheader("📊 Company Information")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Current Price",
                f"₹{info.get('currentPrice', 'N/A')}"
            )

        with col2:

            st.metric(
                "Market Cap",
                str(info.get('marketCap', 'N/A'))
            )

        with col3:

            st.metric(
                "52 Week High",
                f"₹{info.get('fiftyTwoWeekHigh', 'N/A')}"
            )

        st.markdown("---")

        # ==========================================
        # COMPANY DETAILS
        # ==========================================

        st.subheader("🏢 Company Details")

        st.write(
            f"**Company Name:** {info.get('longName', 'N/A')}"
        )

        st.write(
            f"**Sector:** {info.get('sector', 'N/A')}"
        )

        st.write(
            f"**Industry:** {info.get('industry', 'N/A')}"
        )

        st.write(
            f"**Country:** {info.get('country', 'N/A')}"
        )

        st.markdown("---")

        # ==========================================
        # STOCK PRICE CHART
        # ==========================================

        st.subheader("📈 Stock Price Trend")

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.plot(
            history.index,
            history["Close"],
            linewidth=2
        )

        ax.set_xlabel("Date")

        ax.set_ylabel("Closing Price")

        ax.set_title(f"{ticker} Stock Trend")

        ax.grid(True)

        st.pyplot(fig)

        st.markdown("---")

        # ==========================================
        # HISTORICAL DATA
        # ==========================================

        st.subheader("📋 Historical Stock Data")

        st.dataframe(
            history.tail(20),
            use_container_width=True
        )

        st.markdown("---")

        # ==========================================
        # SIMPLE AI INSIGHT
        # ==========================================

        st.subheader("🤖 AI Investment Insight")

        latest_price = history["Close"].iloc[-1]

        old_price = history["Close"].iloc[0]

        growth = (
            (latest_price - old_price)
            / old_price
        ) * 100

        if growth > 15:

            st.success(
                "Strong upward trend detected. Positive growth observed."
            )

        elif growth > 0:

            st.info(
                "Moderate growth observed. Stable investment pattern."
            )

        else:

            st.warning(
                "Negative trend observed. Analyze risk before investing."
            )

        st.write(
            f"6-Month Growth: {growth:.2f}%"
        )

    except Exception as e:

        st.error(
            f"Error fetching stock data: {e}"
        )