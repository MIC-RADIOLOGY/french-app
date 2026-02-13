import streamlit as st

def init_progress():
    if "completed" not in st.session_state:
        st.session_state.completed = set()

def mark_complete(lesson_id):
    st.session_state.completed.add(lesson_id)

def is_completed(lesson_id):
    return lesson_id in st.session_state.completed
