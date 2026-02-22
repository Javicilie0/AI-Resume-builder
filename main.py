import streamlit as st

from backend.match import run_agent
from utils.file_reader import read_file

st.set_page_config(page_title="AI RESUME BUILDER", layout="wide")
st.title("🎯 AI RESUME BUILDER")



tab1, tab2 = st.tabs(["🔍 Job Matcher", "📝 Build Resume"])

with tab1:
    st.header("Build your Resume")

    name = st.text_input("Full Name")

    email = st.text_input("Email")

    phone = st.text_input("Phone Number")

    skills = st.text_input("Skills (comma separated)")

    st.subheader("Experience")

    job_title = st.text_input("Job Title")
    company = st.text_input("Company")
    description = st.text_area("Description", height=100)

    education = st.text_input("Education")

    if st.button("🚀 Generate Resume"):
       
        data = {
            "name": name,
            "email": email,
            "phone": phone,
            "skills": [s.strip() for s in skills.split(",")],
            "experience": [{
                "title": job_title,
                "company": company,
                "description": description
            }],
            "education": education
        }

        




with tab2:
    
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
