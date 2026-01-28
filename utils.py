import streamlit as st

# ----------- HELPER FUNCTIONS -----------


def complete_setup():
    st.session_state.setup_complete = True


def show_feedback():
    st.session_state.feedback_shown = True


def reset_chat():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()
