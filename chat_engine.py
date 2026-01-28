import streamlit as st
from openai import OpenAI


def handle_user_message():
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    # Setting up the OpenAI model in session state if it is not already defined
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4o"

    # Initialize system message
    if not st.session_state.messages:
        st.session_state.messages = [{
            "role": "system",
            "content": (f"You are an HR executive that interviews an interviewee called {st.session_state['name']} "
                        f"with experience {st.session_state['experience']} and skills {st.session_state['skills']}. "
                        f"You should interview him for the position {st.session_state['level']} {st.session_state['position']} "
                        f"at the company {st.session_state['company']}")
        }]

    # Display chat history
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Handle user input and OpenAI response
    if st.session_state.user_message_count < 5:
        if prompt := st.chat_input("Your answer.", max_chars=1000):
            st.session_state.messages.append(
                {"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Assistant's response
            if st.session_state.user_message_count < 4:
                with st.chat_message("assistant"):
                    stream = client.chat.completions.create(
                        model=st.session_state["openai_model"],
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ],
                        temperature=1.0,   # High creativity for chatbot
                        top_p=1.0,
                        stream=True,
                    )
                    # Display the assistant's response as it streams
                    response = st.write_stream(stream)
                st.session_state.messages.append(
                    {"role": "assistant", "content": response})

            st.session_state.user_message_count += 1

    if st.session_state.user_message_count >= 5:
        st.session_state.chat_complete = True
