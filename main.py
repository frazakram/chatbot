import os
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
#from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv("C:/Users/fraza/Desktop/raga_ai/vscode/self_project/myenv4/key.env")
api_key = os.environ.get("OPENAI_API_KEY")

# Define the chat prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user."),
    ("user", "Question: {question}")
])

# Initialize the ChatOpenAI model
llm = ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo", api_key=api_key)

# Set up output parser
output_parser = StrOutputParser()

# Combine prompt, model, and output parser into a chain
chain = prompt | llm | output_parser

def my_streamlit_app():
    st.title("My Streamlit App")
    user_input = st.text_input("Enter your queries")

    if user_input:  # Check if there's input from the user
        response = chain.invoke({"question": user_input})
        st.write(response)

if __name__ == '__main__':
    my_streamlit_app()
