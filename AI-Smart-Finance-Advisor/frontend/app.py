import streamlit as st
import sys
import os

# ==========================================
# PROJECT ROOT PATH
# ==========================================

ROOT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if ROOT_DIR not in sys.path:

    sys.path.append(ROOT_DIR)
# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Smart Finance Advisor",
    page_icon="💰",
    layout="wide"
)

# ==========================================
# SESSION STATE
# ==========================================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if "user_role" not in st.session_state:

    st.session_state.user_role = ""

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

div[data-testid="stSidebar"] {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# BEFORE LOGIN
# ==========================================

if not st.session_state.logged_in:

    st.title("💰 AI Smart Finance Advisor")

    st.warning(
        "Please login to continue."
    )

    page = st.sidebar.radio(

        "Navigation",

        [
            "Login/Register"
        ]
    )

    if page == "Login/Register":

        exec(open(
            "frontend/modules/8_Login.py"
        , encoding="utf-8").read())

# ==========================================
# AFTER LOGIN
# ==========================================

else:

    st.sidebar.success(
        f"Logged in as {st.session_state.user_role}"
    )

    # ==========================================
    # USER NAVIGATION
    # ==========================================

    if st.session_state.user_role == "user":

        page = st.sidebar.radio(

            "Navigation",

            [
                "Dashboard",
                "Expense Analysis",
                "Investment Planner",
                "AI Suggestions",
                "Reports",
                "Stock Market"
            ]
        )

    # ==========================================
    # ADMIN NAVIGATION
    # ==========================================

    elif st.session_state.user_role == "admin":

        page = st.sidebar.radio(

            "Navigation",

            [
                "Dashboard",
                "Expense Analysis",
                "Investment Planner",
                "AI Suggestions",
                "Reports",
                "Stock Market",
                "Admin"
            ]
        )

    # ==========================================
    # PAGE ROUTING
    # ==========================================

    if page == "Dashboard":

        exec(open(
            "frontend/modules/1_Dashboard.py"
        , encoding="utf-8").read())

    elif page == "Expense Analysis":

        exec(open(
            "frontend/modules/2_Expense_Analysis.py"
        , encoding="utf-8").read())

    elif page == "Investment Planner":

        exec(open(
            "frontend/modules/3_Investment_Planner.py"
        , encoding="utf-8").read())

    elif page == "AI Suggestions":

        exec(open(
            "frontend/modules/4_AI_Suggestions.py"
        , encoding="utf-8").read())

    elif page == "Reports":

        exec(open(
            "frontend/modules/5_Reports.py"
        , encoding="utf-8").read())

    elif page == "Stock Market":

        exec(open(
            "frontend/modules/7_Stock_Market.py"
        , encoding="utf-8").read())

    elif page == "Admin":

        exec(open(
            "frontend/modules/6_Admin.py"
        , encoding="utf-8").read())

    # ==========================================
    # LOGOUT
    # ==========================================

    st.sidebar.markdown("---")

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False

        st.session_state.user_role = ""

        st.rerun()