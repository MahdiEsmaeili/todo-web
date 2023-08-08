import streamlit as st

import functions

st.title("My Todo App")
st.subheader("easy to use and user-friendly")
st.write("Use this app to increase your productivity")


todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(placeholder="Enter a todo...", label="")
