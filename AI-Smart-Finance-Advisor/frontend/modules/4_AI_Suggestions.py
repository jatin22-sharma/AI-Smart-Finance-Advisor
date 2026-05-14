import streamlit as st
import google.generativeai as gen_ai
from dotenv import load_dotenv
import os

# ==========================================
# LOAD ENV VARIABLES
# ==========================================

load_dotenv()

# ==========================================
# CONFIGURE GEMINI
# ==========================================

API_KEY = os.getenv("GEMINI_API_KEY")

gen_ai.configure(api_key=API_KEY)

model = gen_ai.GenerativeModel(
    "gemini-2.5-flash"
)

# ==========================================
# PAGE TITLE
# ==========================================

st.title("🤖 AI Financial Advisor")

st.markdown("""
Ask financial questions like:

- How can I save more money?
- Best investment for beginners?
- Should I invest in stocks?
- How to reduce expenses?
- SIP vs Fixed Deposit?
""")

# ==========================================
# USER INPUT
# ==========================================

user_question = st.text_area(
    "Ask Your Financial Question"
)

ask_button = st.button(
    "🚀 Get AI Advice"
)

# ==========================================
# AI RESPONSE
# ==========================================

if ask_button:

    if user_question.strip() == "":

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Analyzing your financial query..."
        ):

            prompt = f"""
            You are an expert AI Smart Financial Advisor.

            Provide:
            - professional financial guidance
            - beginner friendly explanations
            - investment suggestions
            - budgeting advice
            - savings strategies

            User Question:
            {user_question}
            """

            response = model.generate_content(
                prompt
            )

            st.subheader("🤖 AI Response")

            st.write(response.text)