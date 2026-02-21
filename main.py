import streamlit as st

from backend.match import run_agent
from utils.file_reader import read_file

st.set_page_config(page_title="AI RESUME BUILDER", layout="wide")

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.title("🎯 AI RESUME BUILDER")
    st.markdown("Build your perfect resume & find matching jobs with AI")


    uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx"])


    job_description = st.text_area("Paste Job Description", height=200)


    resume = read_file(uploaded_file) if uploaded_file else ""

    if st.button("🔍 MATCH Jobs", type="primary"):
        if uploaded_file and job_description:
            st.success("Analyzing...")
            result = run_agent(resume, job_description)
            st.markdown(result.content)
        else:
            st.warning("Please upload resume AND paste job description")
