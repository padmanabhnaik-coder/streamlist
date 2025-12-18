import streamlit as st


st.title("Task Manager")

if "tasks" not in st.session_state:
    st.session_state.tasks=[]

#add new task
new_task=st.text_input("Enter a new task:")
if st.button("add_task") and new_task:
    st.session_state.tasks.append({"name":new_task,"done":False})

#show tasks with subheaders
st.subheader("Your Tasks:")

for i, task in enumerate(st.session_state.tasks):
    is_done=st.checkbox(task["name"],value=task["done"], key=i)
    st.session_state.tasks[i]["done"]="is_done"


