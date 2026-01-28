from openai import OpenAI
import streamlit as st

from utils import complete_setup, show_feedback, reset_chat
from chat_engine import handle_user_message
from feedback import generate_feedback


st.set_page_config(page_title="Streamlit Chat", page_icon="💬")
st.title("HR Interview Chatbot")

# ----------- SESSION STATE INITIALIZATION -----------
if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False
if "user_message_count" not in st.session_state:
    st.session_state.user_message_count = 0
if "feedback_shown" not in st.session_state:
    st.session_state.feedback_shown = False
if "chat_complete" not in st.session_state:
    st.session_state.chat_complete = False
if "messages" not in st.session_state:
    st.session_state.messages = []

# User personal info defaults
for key, default in [("name", ""), ("experience", ""), ("skills", ""),
                     ("level", "Junior"), ("position", "Data Scientist"), ("company", "Amazon")]:
    if key not in st.session_state:
        st.session_state[key] = default


# ----------- SETUP STAGE for collecting user details -----------
if not st.session_state.setup_complete:
    # Personal Information Section
    st.subheader('Personal information', divider='rainbow')

    # Fields for personal information
    st.session_state["name"] = st.text_input(
        label="Name", max_chars=40, value=st.session_state["name"], placeholder="Enter your name")

    st.session_state["experience"] = st.text_area(
        label="Expirience", value=st.session_state["experience"], height=None, max_chars=200, placeholder="Describe your experience")

    st.session_state["skills"] = st.text_area(
        label="Skills", value=st.session_state["skills"], height=None, max_chars=200, placeholder="List your skills")

    # Company and Position Section
    st.subheader('Company and Position', divider='rainbow')

    # Field for selecting the job level, position and company
    col1, col2 = st.columns(2)
    with col1:
        st.session_state["level"] = st.radio(
            "Choose level",
            key="visibility",
            options=["Junior", "Mid-level", "Senior"],
            index=["Junior", "Mid-level",
                   "Senior"].index(st.session_state["level"])
        )

    with col2:
        st.session_state["position"] = st.selectbox(
            "Choose a position",
            ("Data Scientist", "Data Engineer", "ML Engineer",
             "BI Analyst", "Financial Analyst"),
            index=("Data Scientist", "Data Engineer", "ML Engineer", "BI Analyst",
                   "Financial Analyst").index(st.session_state["position"])
        )

    st.session_state["company"] = st.selectbox("Choose a Company",
                                               ("Amazon", "Meta", "Amdocs", "Nvidia",
                                                "Microsoft", "CheckPoint", "Spotify")
                                               )

    # A button to complete the setup stage and start the interview
    if st.button("Start Interview", on_click=complete_setup):
        st.success("Setup complete. Starting interview...")

# ----------- INTERVIEW STAGE -----------
if st.session_state.setup_complete and not st.session_state.feedback_shown and not st.session_state.chat_complete:
    # Display a welcome message and prompt the user to introduce themselves
    st.info(
        """
        Start by introducing yourself.
        """,
        icon="👋"
    )
    handle_user_message()


# ----------- GET FEEDBACK BUTTON -----------
if st.session_state.chat_complete and not st.session_state.feedback_shown:
    if st.button("Get Feedback", on_click=show_feedback):
        st.write("Generating feedback...")

# ----------- SHOW FEEDBACK screen -----------
if st.session_state.feedback_shown:
    st.subheader("Feedback")
    feedback_content = generate_feedback(st.session_state.messages)
    st.write(feedback_content)

    # Button to restart the interview
    if st.button("Restart Interview"):
        st.success("Chat reset. You can start a new interview now.")
        reset_chat()
