import streamlit as st
from curriculum import CURRICULUM
from engine import render_lesson
from progress import init_progress, is_completed

st.set_page_config("French Learning App 🇫🇷", layout="wide")

init_progress()

st.title("🇫🇷 French Learning Platform")
st.caption("Structured French from A1 to A2")

# Sidebar navigation
level = st.sidebar.selectbox("Select Level", CURRICULUM.keys())
category = st.sidebar.selectbox("Select Category", CURRICULUM[level].keys())

lessons = CURRICULUM[level][category]
lesson_titles = [l["title"] for l in lessons]
selected_title = st.sidebar.radio("Lessons", lesson_titles)

lesson = next(l for l in lessons if l["title"] == selected_title)

# Completion indicator
lesson_id = f"{level}-{category}-{lesson['title']}"
if is_completed(lesson_id):
    st.sidebar.success("✔ Completed")

render_lesson(level, category, lesson)
