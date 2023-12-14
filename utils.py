import os
import random
import streamlit as st

#decorator
def enable_chat_history(func):
    cols = st.columns(9)
    # with cols[0]:
    #     st.image("left.gif", caption="", use_column_width=True)
    with cols[8]:
        st.image("right.gif", caption="", use_column_width=True)
    if st.secrets['OPENAI_API_KEY']:
        st.session_state.api_key = st.secrets['OPENAI_API_KEY']
    if True:
        # to show chat history on ui
        if "messages" not in st.session_state:
            with open("system.txt") as file:
                qa = file.read()
            from datetime import date
            # Get the current date
            current_date = date.today()
            st.session_state["messages"] = [
                {"role" : "system", "content" : qa + str(current_date)},
                {"role": "assistant", "content": "Hello, there! Welcome! My name is Vladyslav Lopuha"},
            ]
        for msg in st.session_state["messages"]:
            if msg['role'] != 'system':
                st.chat_message(msg["role"]).write(msg["content"])

    def execute(*args, **kwargs):
        func(*args, **kwargs)
    return execute

def display_msg(msg, author):
    """Method to display message on the UI

    Args:
        msg (str): message to display
        author (str): author of the message -user/assistant
    """
    st.session_state.messages.append({"role": author, "content": msg})
    st.chat_message(author).write(msg)

def configure_openai_api_key():
    return st.session_state.api_key