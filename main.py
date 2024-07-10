import streamlit as st

import function

todos=function.get_todos()

def add_todo():
    todo=st.session_state["new_todo"]+"\n"
#del st.session_state[todo]
    todos.append(todo) 
    function.write_todos(todos)

st.title("my Todo app")
st.subheader("This is my To do app")

st.write("This app is to increase your productivity")
st.checkbox("Buy mac")

for todo in todos:
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.remove(todo)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Add Todo",placeholder="Enter a new todo",
              on_change=add_todo,key="new_todo")
