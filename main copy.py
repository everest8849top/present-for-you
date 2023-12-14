import os
import utils
import streamlit as st

from openai import OpenAI
client = OpenAI()

st.set_page_config(layout='wide')
grids = []

class CustomDataChatbot:
    def __init__(self):
        utils.configure_openai_api_key()
        self.openai_model = "gpt-3.5-turbo"

    @utils.enable_chat_history
    def main(self):
        grids.append(st.columns(4))
        st.title("Welcome! It'my present for you!")
        grids.append(st.columns(4))
        chat_field = st.empty()
        grids.append(st.columns(4))
        # st.sidebar.header(":gift: It's a present for you!")
        user_query = st.chat_input(placeholder="Please have a chat with me!")
        grids.append(st.columns(4))

        if user_query:
            utils.display_msg(user_query, 'user')

            with st.chat_message("assistant"):
                stream = client.chat.completions.create(
                    model=self.openai_model,
                    messages=st.session_state.messages,
                    stream=True,
                )
                # stream = "what? What? What?"
                st.session_state.messages.append({"role": "assistant", "content": ""})
                # print(stream)
                for chunk in stream:
                    chunk_content = chunk.choices[0].delta.content
                    # print(chunk_content)
                    if chunk_content is not None:
                        st.session_state.messages[-1]['content'] += chunk_content
                        message_placeholder.markdown(st.session_state.messages[-1]['content'])
                # for chunk in stream:
                #     chunk_content = chunk
                #     # print(chunk_content)
                #     if chunk_content is not None:
                #         st.session_state.messages[-1]['content'] += chunk_content
                #         message_placeholder.markdown(st.session_state.messages[-1]['content'])
        with grids[0][3]:
            st.image("joypixels.gif", caption="Welcome", use_column_width=True)
        with grids[3][0]:
            st.image("sparkles.gif", caption="Welcome", use_column_width=True)

if __name__ == "__main__":
    obj = CustomDataChatbot()
    obj.main()