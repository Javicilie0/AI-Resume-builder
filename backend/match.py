import os

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


def run_agent(resume, job_description):
    llm = ChatOllama(model="Mistral", temperature = 0)

    prompt_template = ChatPromptTemplate.from_template(
        """You are an experience HR recruiter, analyze how well this candidate's resume matches the job description and provide a detailed answer.:
        Candidate's Resume: {resume}
        job description: {job_description}
        -List skills the candidate has that match the job description
        -List skills the candidate is missing that are in the job description
        -How can the candidate improve their resume to better match the job description?
        Provide  a detailed answer:"""
    )

    chain = prompt_template | llm

    result = chain.invoke({
        "resume": resume,
        "job_description": job_description
    })

    return result