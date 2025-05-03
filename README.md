# HCA-Challenge
# Overview

During Hurricane Helene, HCA deployed 42 Response Teams and 572 colleagues across Florida and Georgia. This demonstrated the importance of disaster-ready response teams in patient rescue, resource accessibility, and overall preparedness. Our solution is an AI-chatbot-supported mobile application designed to provide employees with real-time access to resource information across HCA locations. Additionally, a preparedness booklet will offer actionable guidance on disaster response measures.

# Tech Stack

**AI Chatbot** 
**Functionality:** The chatbot processes user input and checks the two datasets imported for relevant information to return an answer with. For employee and location related questions, the model captures keywords like “supervisor” or “position” and checks the “deidentified_hca_employees.csv” for matching information and returns relevant information. 

**Deployment(Front-End):** Hosted in Hugging Face Spaces platform, later it was linked to the mobile application using the URL.

**Libraries and Packages(Back-End):** 
**Streamlit:** Used for building the web interface of the chatbot application.
**Pandas:** Used to load and manage datasets (CSV,Excel) that contain employee data provided by HCA and knowledge base dataset to train the chatbot. 
**Transformers:** Hugging Face’s transformers library was used to leverage the pre-trained question-answering model (roberta-base-squad2), and answers questions based on given context. 
**FuzzyWuzzy:** Fuzzy string matching library was used for improving accuracy of matching user input with imported data.
**Datasets:**

Employee Data (deidentified_hca_employees.csv): Includes employee details, locations, and job roles.
This was used to feed the chatbot for whenever a user asks for specific information about other employees in different locations. 

Hurricane Knowledge Base (HurricaneKnowledgebase.xlsx): A curated dataset of hurricane-related Q&A. Knowledge base is limited to hurricanes and natural disasters as a demo was built, and a sample base enabled quick deployment and testing.

# Features
Real-time response using custom knowledge base
Deployed via Hugging Face Spaces
NLP techniques for intent detection or question answering

Chatbot deployed at: https://huggingface.co/spaces/Bengisuu/HCA_Chatbot?logs=container 
To test it, try asking ask these questions: "Who is the supervisor at HCA Houston Conroe Hospital?" , "What should I include in a hurricane emergency kit?", "Find me someone who's position is Supv Laboratory in GeorgeTown, TX."
![Screenshot 2025-05-02 185822](https://github.com/user-attachments/assets/9c821120-5ca4-4aa5-92b8-3604ee232996)

# Mobile Application Layout
![navigate1](https://github.com/user-attachments/assets/4c5bf75b-36fc-4ab9-86d6-bff0ce44fad1)![Screenshot 2025-02-19 124936](https://github.com/user-attachments/assets/2bf97f7d-b674-43bf-a9f3-4d8542e1ca80)![3Navigate](https://github.com/user-attachments/assets/7a8fc399-e11f-4bcb-85c0-9ccbcf9cae93)






