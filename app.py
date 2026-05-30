import streamlit as st
from resume_reader import read_resume_pdf
from question_generator import generate_questions
from answer_evaluator import evaluate_answer

st.set_page_config(page_title="AI Interview Preparation Platform", layout="wide")

st.title("AI Interview Preparation Platform")

resume_file = st.file_uploader("Upload Resume PDF", type=["pdf"])
job_description = st.text_area("Paste Job Description", height=200)

if st.button("Generate Interview Questions"):
    if resume_file is None or not job_description.strip():
        st.error("Please upload a resume and paste a job description.")
    else:
        resume_text = read_resume_pdf(resume_file)
        technical_questions, hr_questions = generate_questions(resume_text, job_description)

        st.session_state["technical_questions"] = technical_questions
        st.session_state["hr_questions"] = hr_questions

if "technical_questions" in st.session_state:
    st.subheader("Technical Questions")
    for q in st.session_state["technical_questions"]:
        st.write(f"- {q}")

    st.subheader("HR Questions")
    for q in st.session_state["hr_questions"]:
        st.write(f"- {q}")

    st.subheader("Practice Answer")
    answer = st.text_area("Type your answer here", height=150)

    if st.button("Evaluate Answer"):
        result = evaluate_answer(answer)
        st.metric("Answer Score", result["score"])
        st.write(result["feedback"])
