import streamlit as st
import random
from progress import mark_complete, is_completed

def render_lesson(level, category, lesson):
    lesson_id = f"{level}-{category}-{lesson['title']}"

    st.header(lesson["title"])
    st.info(lesson["theory"])

    st.subheader("Vocabulary")
    for fr, en in lesson["content"]:
        st.write(f"**{fr}** → {en}")

    st.divider()
    render_quiz(lesson, lesson_id)

def render_quiz(lesson, lesson_id):
    st.subheader("Quiz")

    score = 0
    for fr, en in random.sample(lesson["content"], len(lesson["content"])):
        ans = st.text_input(f"What is '{fr}' in English?", key=f"{lesson_id}-{fr}")

        if ans:
            if ans.lower().strip() == en.lower():
                score += 1
                st.success("Correct")
            else:
                st.error(f"Correct answer: {en}")

    if st.button("Finish Lesson"):
        mark_complete(lesson_id)
        st.success(f"Lesson completed! Score: {score}/{len(lesson['content'])}")
