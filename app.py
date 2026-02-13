import streamlit as st
from data import lessons
from lessons import show_lesson, quiz_lesson

st.set_page_config(page_title="Learn French 🇫🇷", layout="centered")

st.title("🇫🇷 French Learning App")
st.write("Learn basic French step by step.")

lesson_titles = [lesson["title"] for lesson in lessons]
selected = st.sidebar.selectbox("Choose a lesson", lesson_titles)

lesson = next(l for l in lessons if l["title"] == selected)

tab1, tab2 = st.tabs(["📘 Lesson", "🧠 Quiz"])

with tab1:
    show_lesson(lesson)

with tab2:
    quiz_lesson(lesson)
