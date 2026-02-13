import streamlit as st
import random

def show_lesson(lesson):
    st.subheader(lesson["title"])

    for french, english in lesson["content"]:
        st.write(f"**{french}** — {english}")

def quiz_lesson(lesson):
    st.subheader("Quiz")

    score = 0
    questions = random.sample(lesson["content"], len(lesson["content"]))

    for french, english in questions:
        answer = st.text_input(f"What is the meaning of **{french}**?", key=french)

        if answer:
            if answer.lower().strip() == english.lower():
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Wrong. Correct answer: {english}")

    if st.button("Show Score"):
        st.info(f"Your score: {score} / {len(lesson['content'])}")
