from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv
load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")
model=ChatGroq(api_key=groq_api_key, model_name="llama-3.1-8b-instant")

#Create prompt template

system_template = "Translate the following into {language}."
prompt=ChatPromptTemplate.from_messages(
    [
        ("system",system_template),
        ("user","{text}")
    ]
)
parser=StrOutputParser()
#Create a chain that combines prompt, model and parser
chain=prompt|model|parser

#Create FastAPI app and add langserve routes
app=FastAPI(
    title="LCEL Groq Translation API",
    description="An API that translates text using Groq LLMs and LCEL",
    version="1.0"
)
add_routes(app, chain,path="/chain")

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

