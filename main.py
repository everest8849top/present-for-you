import os
import utils
import streamlit as st

from openai import OpenAI
client = OpenAI()

st.set_page_config(layout='wide')
import time

class CustomDataChatbot:
    def __init__(self):
        utils.configure_openai_api_key()
        self.openai_model = "gpt-3.5-turbo"

    @utils.enable_chat_history
    def main(self):
        with st.sidebar:
            st.image("sidebar_background.gif", caption="", use_column_width=True)
            openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
            if openai_api_key:
                st.session_state.api_key = openai_api_key
        if st.session_state.api_key:
            client.api_key = st.session_state.api_key
            print(client.api_key)
        st.empty()
        user_query = st.chat_input(placeholder="Ask me anything!")

        if user_query:
            utils.display_msg(user_query, 'user')

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                try:
                    stream = client.chat.completions.create(
                        model=self.openai_model,
                        messages=st.session_state.messages,
                        stream=True,
                    )
                    # stream = "What? What?"
                    st.session_state.messages.append({"role": "assistant", "content": ""})
                    # print(stream)
                    for chunk in stream:
                        chunk_content = chunk.choices[0].delta.content
                        # chunk_content = chunk
                        # print(chunk_content)
                        if chunk_content is not None:
                            st.session_state.messages[-1]['content'] += chunk_content
                            message_placeholder.markdown(st.session_state.messages[-1]['content'])
                except Exception as e:
                    stream = str(e)
                    st.session_state.messages.append({"role": "assistant", "content": "I'm sorry for this error! There are so many visitors to my app and I'm using free gpt api. It has 200 limit per day. Unfortuntely, I used them all. Could you please use your api key?\n:-\n"})
                    for chunk in stream:
                        chunk_content = chunk
                        if chunk_content is not None:
                            st.session_state.messages[-1]['content'] += chunk_content
                            message_placeholder.markdown(st.session_state.messages[-1]['content'])
                        time.sleep(0.01)
        # cols = st.columns(10)
        # with cols[0]:
        #     st.image("left.gif", caption="", use_column_width=True)          


if __name__ == "__main__":
    obj = CustomDataChatbot()
    obj.main()