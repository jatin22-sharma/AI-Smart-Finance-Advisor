import streamlit as st
import matplotlib.pyplot as plt

st.title("💼 Investment Planner")

st.markdown("""
Plan your investments intelligently based on savings and risk appetite.
""")

# ==========================================
# INPUTS
# ==========================================

monthly_savings = st.number_input(

    "Monthly Savings",

    min_value=0,

    step=1000
)

risk_level = st.selectbox(

    "Select Risk Level",

    [
        "Low",
        "Medium",
        "High"
    ]
)

plan = st.button(
    "Generate Investment Plan"
)

# ==========================================
# INVESTMENT LOGIC
# ==========================================

if plan:

    if monthly_savings <= 0:

        st.error(
            "Please enter valid savings."
        )

    else:

        # ==========================================
        # LOW RISK
        # ==========================================

        if risk_level == "Low":

            fd = monthly_savings * 0.50
            mutual = monthly_savings * 0.30
            gold = monthly_savings * 0.20

            labels = [
                "Fixed Deposit",
                "Mutual Funds",
                "Gold"
            ]

            values = [
                fd,
                mutual,
                gold
            ]

        # ==========================================
        # MEDIUM RISK
        # ==========================================

        elif risk_level == "Medium":

            mutual = monthly_savings * 0.40
            stocks = monthly_savings * 0.40
            emergency = monthly_savings * 0.20

            labels = [
                "Mutual Funds",
                "Stocks",
                "Emergency Fund"
            ]

            values = [
                mutual,
                stocks,
                emergency
            ]

        # ==========================================
        # HIGH RISK
        # ==========================================

        else:

            stocks = monthly_savings * 0.60
            crypto = monthly_savings * 0.20
            mutual = monthly_savings * 0.20

            labels = [
                "Stocks",
                "Crypto",
                "Mutual Funds"
            ]

            values = [
                stocks,
                crypto,
                mutual
            ]

        # ==========================================
        # METRICS
        # ==========================================

        st.subheader("📊 Recommended Investment Allocation")

        cols = st.columns(len(labels))

        for i in range(len(labels)):

            cols[i].metric(

                labels[i],

                f"₹{values[i]:,.0f}"

            )

        st.markdown("---")

        # ==========================================
        # PIE CHART
        # ==========================================

        st.subheader("🥧 Investment Distribution")

        fig, ax = plt.subplots()

        ax.pie(

            values,

            labels=labels,

            autopct="%1.1f%%"

        )

        st.pyplot(fig)

        st.markdown("---")

        # ==========================================
        # INVESTMENT ADVICE
        # ==========================================

        st.subheader("🤖 AI Investment Advice")

        if risk_level == "Low":

            st.success(
                "Low-risk portfolio focuses on stable and safe investments."
            )

        elif risk_level == "Medium":

            st.info(
                "Balanced portfolio with moderate growth potential."
            )

        else:

            st.warning(
                "High-risk portfolio may provide higher returns but higher volatility."
            )

        st.markdown("---")

        # ==========================================
        # FUTURE VALUE ESTIMATION
        # ==========================================

        st.subheader("📈 Estimated Future Value (1 Year)")

        if risk_level == "Low":

            future = monthly_savings * 12 * 1.08

        elif risk_level == "Medium":

            future = monthly_savings * 12 * 1.15

        else:

            future = monthly_savings * 12 * 1.25

        st.metric(
            "Estimated Portfolio Value",
            f"₹{future:,.0f}"
        )

else:

    st.info(
        "Enter savings and generate investment plan."
    )