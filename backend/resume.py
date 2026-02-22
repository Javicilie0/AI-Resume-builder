import os

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


def improve_resume(data: dict) -> dict:
    """Use LLM to improve the resume based on the provided data."""

    llm = ChatOllama(model="Mistral", temperature=0)

    prompt_template = ChatPromptTemplate.from_template(
        """You are an expert resume writer. Based on the following information, improve the candidate's resume:
        You are a professional resume writer.

        Improve this job description:
        - Use strong action verbs (Developed, Implemented, etc.)
        - Make it professional and impactful
        - Keep it short (1-2 sentences)
        - DO NOT invent numbers, metrics or facts
        - DO NOT add information that is not in the original
        - Only rephrase and improve the wording

            Original: {data}

            Improved:
        """
    )

    chain = prompt_template | llm

    improved_experience = []
    for exp in data["experience"]:
        if exp["description"].strip():
            result = chain.invoke({"data": exp["description"] })
            improved_exp = exp.copy()
            improved_exp["description"] = result.content.strip()
            improved_experience.append(improved_exp)
        else:
            improved_experience.append(exp)

    improved_data = data.copy()
    improved_data["experience"] = improved_experience

    return improved_data
