import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is David's To-To App")
st.write("This app is designed to maximize David's productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(
    label=" ",
    label_visibility="hidden",
    placeholder="Add a new todo",
    on_change=add_todo,
    key="new_todo"
)


