import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
groq_api_key=os.getenv("GROQ_API_KEY")
from langchain_groq import ChatGroq
model=ChatGroq(api_key=groq_api_key, model="llama-3.1-8b-instant")

prompt= ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer all questions to the best of your ability."),
        ("user", "Question: {question}")
    ]
)


st.title("Langchain Demo with llama model using Groq")
input_text=st.text_input("what question do you have?")

#Ollama Llama2 model


output_parser=StrOutputParser()
chain=prompt|model|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))



   