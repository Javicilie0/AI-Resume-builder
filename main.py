import streamlit as st

st.set_page_config(page_title="AI RESUME BUILDER", layout="wide")

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.title("🎯 AI RESUME BUILDER")
    st.markdown("Build your perfect resume & find matching jobs with AI")
    
    
    uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx"])
    
   
    job_description = st.text_area("Paste Job Description", height=200)
    
   
    if st.button("🔍 MATCH Jobs", type="primary"):
        
        if uploaded_file and job_description:
            st.success("Analyzing...")
        else:
            st.warning("Please upload resume AND paste job description")