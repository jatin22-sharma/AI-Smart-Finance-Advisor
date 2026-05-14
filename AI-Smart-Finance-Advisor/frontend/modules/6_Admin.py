import streamlit as st
import pandas as pd

import sys
import os

# ==========================================
# BACKEND PATH
# ==========================================

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../"
        )
    )
)

from backend.database import fetch_records

# ==========================================
# AUTH PATH
# ==========================================

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../"
        )
    )
)

from auth import check_login

# ==========================================
# LOGIN PROTECTION
# ==========================================

if not check_login():

    st.error("🔒 Please login first.")

    st.stop()

# ==========================================
# PAGE UI
# ==========================================

st.title("🔐 Admin Dashboard")

st.subheader("📊 Financial Records")

data = fetch_records()

if len(data) > 0:

    columns = [

        "ID",
        "Income",
        "Rent",
        "Food",
        "Travel",
        "Entertainment",
        "Other",
        "Total Expense",
        "Savings",
        "Savings Rate"

    ]

    df = pd.DataFrame(
        data,
        columns=columns
    )

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.info("No records found.")