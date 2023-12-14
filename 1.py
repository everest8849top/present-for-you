import streamlit as st

def main():
    grids = []
    grids.append(st.columns(4))
    st.title("Welcome! It'my present for you!")
    with grids[0][3]:
        st.image("joypixels.gif", caption="Welcome", use_column_width=True)
    grids.append(st.columns(4))
    user_query = st.chat_input(placeholder="Ask me anything!")
    if user_query:
        utils.display_msg(user_query, 'user')
    grids.append(st.columns(4))
    grids.append(st.columns(4))
    with grids[3][0]:
        st.image("sparkles.gif", caption="Welcome", use_column_width=True)

st.set_page_config(layout='wide')
if __name__ == "__main__":
    main()
