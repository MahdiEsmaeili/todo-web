import streamlit as st

import functions


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("easy to use and user-friendly")
st.write("Use this app to increase your productivity")


todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(placeholder="Enter a todo...", label="",
              on_change=add_todo, key="new_todo")
