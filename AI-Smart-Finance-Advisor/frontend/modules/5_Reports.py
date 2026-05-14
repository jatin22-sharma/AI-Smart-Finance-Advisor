import streamlit as st

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

from backend.report_generator import (
    generate_financial_report
)

# ==========================================
# PAGE TITLE
# ==========================================

st.title("📄 Financial Report Generator")

st.markdown("""
Generate professional financial reports including:

- Income Summary
- Expense Analysis
- Savings Overview
- AI Suggestions
""")

# ==========================================
# USER INPUT
# ==========================================

income = st.number_input(
    "Monthly Income",
    min_value=0
)

expense = st.number_input(
    "Total Expense",
    min_value=0
)

savings = income - expense

if income > 0:
    savings_rate = (savings / income) * 100
else:
    savings_rate = 0

# ==========================================
# SAMPLE SUGGESTIONS
# ==========================================

suggestions = []

if savings_rate < 20:

    suggestions.append(
        "Increase your monthly savings."
    )

if expense > income * 0.8:

    suggestions.append(
        "Your expenses are very high."
    )

if len(suggestions) == 0:

    suggestions.append(
        "Excellent financial management."
    )

# ==========================================
# GENERATE BUTTON
# ==========================================

generate = st.button(
    "📥 Generate PDF Report"
)

# ==========================================
# GENERATE PDF
# ==========================================

if generate:

    pdf_path = generate_financial_report(

        income,
        expense,
        savings,
        savings_rate,
        suggestions

    )

    st.success(
        "PDF Report Generated Successfully!"
    )

    # Download Button

    with open(pdf_path, "rb") as file:

        st.download_button(

            label="⬇ Download Report",

            data=file,

            file_name="financial_report.pdf",

            mime="application/pdf"
        )