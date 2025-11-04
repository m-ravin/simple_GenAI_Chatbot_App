import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import openai
import streamlit as st

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot With OPENAI"

#Prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user's query"),
        ("user","Question:{question}")
    ]
)   

def generate_response(question,api_key,engine,temperature,max_tokens):
    os.environ["OPENAI_API_KEY"]=api_key
    llm=ChatOpenAI(model=engine,temperature=temperature,max_tokens=max_tokens)
    output_parsers=StrOutputParser()
    chain=prompt|llm|output_parsers
    response=chain.invoke({"question":question})
    return response

#Title of the app
st.title("🦜🔗 Simple Q&A Chatbot with OPENAI")

#User inputs at the side bar
with st.sidebar:
    st.subheader("Settings")
    api_key=st.text_input("Enter your OPENAI API key", type="password")
    engine=st.selectbox("Select the model", ("gpt-3.5-turbo", "gpt-4"))
    temperature=st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    max_tokens=st.slider("Max Tokens", min_value=10, max_value=1000, value=100, step=10)
#User input for question
user_input=st.text_area("Enter your question here")
submit=st.button("Generate Response")

if user_input and api_key and submit:
    response=generate_response(user_input,api_key,engine,temperature,max_tokens)
    st.text_area("Response", value=response)
elif user_input:
    st.warning("Please enter your OPENAI API key in the sidebar.")
else:
    st.info("Please enter a question to get started.")