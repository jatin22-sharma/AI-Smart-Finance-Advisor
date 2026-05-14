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

from backend.database import (
    create_user,
    login_user
)

# ==========================================
# SESSION STATE
# ==========================================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if "user_name" not in st.session_state:

    st.session_state.user_name = ""

# ==========================================
# PAGE TITLE
# ==========================================

st.title("🔐 User Authentication")

menu = st.radio(
    "Select Option",
    [
        "Login",
        "Signup"
    ]
)

# ==========================================
# SIGNUP
# ==========================================

if menu == "Signup":

    st.subheader("📝 Create Account")

    name = st.text_input(
        "Full Name"
    )

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    signup = st.button(
        "Create Account"
    )

    if signup:

        if name and email and password:

            success = create_user(
                name,
                email,
                password
            )

            if success:

                st.success(
                    "Account created successfully!"
                )

            else:

                st.error(
                    "Email already exists."
                )

        else:

            st.warning(
                "Please fill all fields."
            )

# ==========================================
# LOGIN
# ==========================================

elif menu == "Login":

    st.subheader("🔑 Login")

    role = st.selectbox(

        "Login As",

        [
            "user",
            "admin"
        ]
    )

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    login = st.button(
        "Login"
    )

    if login:

        # ADMIN LOGIN

        if role == "admin":

            if (
                email == "admin@gmail.com"
                and
                password == "admin123"
            ):

                st.session_state.logged_in = True

                st.session_state.user_role = "admin"

                st.success(
                    "Admin login successful!"
                )

                st.rerun()

            else:

                st.error(
                    "Invalid admin credentials."
                )

        # USER LOGIN

        else:

            user = login_user(
                email,
                password
            )

            if user:

                st.session_state.logged_in = True

                st.session_state.user_role = "user"

                st.success(
                    f"Welcome {user[1]}!"
                )

                st.rerun()

            else:

                st.error(
                    "Invalid email or password."
                )

# ==========================================
# SHOW LOGIN STATUS
# ==========================================

if st.session_state.logged_in:

    st.markdown("---")

    st.success(
        f"Logged in as: {st.session_state.user_name}"
    )

    if st.button("Logout"):

        st.session_state.logged_in = False

        st.session_state.user_name = ""

        st.rerun()