import streamlit as st

import function

todos=function.get_todos()

st.title("my Todo app")
st.subheader("This is my To do app")

st.write("This app is to increase your productivity")
st.checkbox("Buy mac")
for todo in todos:
    st.checkbox(todo)


st.text_input(label="",placeholder="Enter a new todo")