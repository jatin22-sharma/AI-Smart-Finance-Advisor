import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📋 Expense Analysis")

st.markdown("""
Analyze your spending habits and financial behavior.
""")

# ==========================================
# INPUTS
# ==========================================

st.sidebar.header("Enter Expense Details")

income = st.sidebar.number_input(
    "Monthly Income",
    min_value=0,
    step=1000
)

rent = st.sidebar.number_input(
    "Rent Expense",
    min_value=0
)

food = st.sidebar.number_input(
    "Food Expense",
    min_value=0
)

travel = st.sidebar.number_input(
    "Travel Expense",
    min_value=0
)

entertainment = st.sidebar.number_input(
    "Entertainment Expense",
    min_value=0
)

other = st.sidebar.number_input(
    "Other Expense",
    min_value=0
)

analyze = st.sidebar.button(
    "Analyze Expenses"
)

# ==========================================
# ANALYSIS
# ==========================================

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

        df["Percentage"] = (
            df["Amount"] / income
        ) * 100

    else:

        df["Percentage"] = 0

    # ==========================================
    # METRICS
    # ==========================================

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Income",
        f"₹{income:,.0f}"
    )

    col2.metric(
        "Total Expense",
        f"₹{total_expense:,.0f}"
    )

    col3.metric(
        "Savings",
        f"₹{savings:,.0f}"
    )

    st.markdown("---")

    # ==========================================
    # TABLE
    # ==========================================

    st.subheader("📊 Expense Breakdown")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================================
    # HIGHEST EXPENSE
    # ==========================================

    highest = df.loc[
        df["Amount"].idxmax()
    ]

    st.warning(
        f"Highest spending category: "
        f"{highest['Category']} "
        f"(₹{highest['Amount']:,.0f})"
    )

    # ==========================================
    # PIE CHART
    # ==========================================

    st.subheader("🥧 Expense Distribution")

    fig1, ax1 = plt.subplots()

    ax1.pie(

        df["Amount"],

        labels=df["Category"],

        autopct="%1.1f%%"

    )

    st.pyplot(fig1)

    # ==========================================
    # BAR CHART
    # ==========================================

    st.subheader("📈 Expense Comparison")

    fig2, ax2 = plt.subplots()

    ax2.bar(

        df["Category"],

        df["Amount"]

    )

    ax2.set_ylabel("Amount")

    st.pyplot(fig2)

    st.markdown("---")

    # ==========================================
    # SMART INSIGHTS
    # ==========================================

    st.subheader("🤖 Smart Financial Insights")

    if rent > income * 0.30:

        st.error(
            "Rent exceeds recommended 30% of income."
        )

    if food > income * 0.25:

        st.warning(
            "Food expenses are higher than ideal."
        )

    if entertainment > income * 0.15:

        st.warning(
            "Entertainment spending is high."
        )

    if savings < income * 0.20:

        st.error(
            "Savings rate is below 20%."
        )

    if total_expense > income:

        st.error(
            "Critical overspending detected."
        )

    if savings >= income * 0.30:

        st.success(
            "Excellent savings habit."
        )

else:

    st.info(
        "Enter financial details and click Analyze Expenses."
    )