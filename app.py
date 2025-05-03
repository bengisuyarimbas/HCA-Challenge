import streamlit as st
import pandas as pd
from transformers import pipeline
from fuzzywuzzy import fuzz


# Load the datasets
employee_data = pd.read_csv("deidentified_hca_employees.csv", dtype=str)
knowledge_base = pd.read_excel("HurricaneKnowledgebase.xlsx")

# Load Hugging Face model
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Chatbot function
def chatbot_response(user_question):
    if "supervisor" in user_question.lower() or "position" in user_question.lower():
        for index, row in employee_data.iterrows():
            if row["EmpLocationDesc"].lower() in user_question.lower():
                return f"Sure! Here is what I found: Supervisor at {row['EmpLocationDesc']}: {row['EmpFirstName']}, Position: {row['EmpPositionDesc']}"
    if "position" in user_question.lower() or "TX" in user_question.lower():
        for index, row in employee_data.iterrows():
            if row["EmpPositionDesc"].lower() in user_question.lower():
                return f"Supervisor at {row['EmpLocationDesc']}: {row['EmpFirstName']}, Position: {row['EmpPositionDesc']}"
                
    best_match = None
    best_context = None
    for index, row in knowledge_base.iterrows():
        question = str(row["Question"])
        if question.lower() in user_question.lower():
            best_match = row["Question"]
            best_context = row["Answer"]
            break  

    if best_context:
        result = qa_pipeline(question=user_question, context=best_context)
        if result["score"] > 0.4:
            return result["answer"]

    return "Sorry, I don't have information on that. Please check official sources."

# Streamlit UI
st.title("Ask ResQMedAI")

# Text input from user
user_question = st.text_input("Ask a question:")

# Check if the user has entered a question
if user_question:
    response = chatbot_response(user_question)
    st.write(response)
