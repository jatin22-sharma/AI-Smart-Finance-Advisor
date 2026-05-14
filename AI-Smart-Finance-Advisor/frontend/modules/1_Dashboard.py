import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../"
        )
    )
)

from backend.database import save_financial_data

st.title("📊 Financial Dashboard")

# Sidebar Inputs
st.sidebar.header("Financial Details")

income = st.sidebar.number_input(
    "Monthly Income",
    min_value=0,
    step=1000
)

rent = st.sidebar.number_input(
    "Rent",
    min_value=0
)

food = st.sidebar.number_input(
    "Food",
    min_value=0
)

travel = st.sidebar.number_input(
    "Travel",
    min_value=0
)

entertainment = st.sidebar.number_input(
    "Entertainment",
    min_value=0
)

other = st.sidebar.number_input(
    "Other",
    min_value=0
)

analyze = st.sidebar.button("Analyze")

if analyze:

    df = pd.DataFrame({
        "Category": [
            "Rent",
            "Food",
            "Travel",
            "Entertainment",
            "Other"
        ],
        "Amount": [
            rent,
            food,
            travel,
            entertainment,
            other
        ]
    })

    total_expense = df["Amount"].sum()
    savings = income - total_expense

    if income > 0:
        savings_rate = (savings / income) * 100
    else:
        savings_rate = 0


    # SAVE TO DATABASE

    save_financial_data(
        income,
        rent,
        food,
        travel,
        entertainment,
        other,
        total_expense,
        savings,
        savings_rate
    )
    
    # KPI Cards

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Income", f"₹{income:,.0f}")
    col2.metric("Expenses", f"₹{total_expense:,.0f}")
    col3.metric("Savings", f"₹{savings:,.0f}")
    col4.metric("Savings %", f"{savings_rate:.1f}%")

    st.markdown("---")

    # Charts

    c1, c2 = st.columns(2)

    with c1:

        st.subheader("Expense Breakdown")

        fig1, ax1 = plt.subplots()

        ax1.bar(
            df["Category"],
            df["Amount"]
        )

        st.pyplot(fig1)

    with c2:

        st.subheader("Expense Distribution")

        fig2, ax2 = plt.subplots()

        ax2.pie(
            df["Amount"],
            labels=df["Category"],
            autopct="%1.1f%%"
        )

        st.pyplot(fig2)

else:
    st.info("Enter financial details and click Analyze.")