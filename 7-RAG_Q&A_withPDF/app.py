import os
from dotenv import load_dotenv
load_dotenv()

#os.environ["GROQ_API_KEY"]=os.getenv("GROQ_TOKEN")
os.environ["HF_TOKEN"]=os.getenv("HF_TOKEN")

import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from langchain_classic.chains.combine_documents import create_stuff_documents_chain

from langchain_classic.chains.retrieval import create_retrieval_chain




embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

#set-up streamlit app
st.title("🦜🔗 Simple RAG Chatbot with Graoq")
st.write("Upload a PDF document and ask questions about its content.")

#request for groq api key
api_key=st.text_input("Enter your GROQ API key", type="password")

#check of groq api key is provided
if api_key:
    llm=ChatGroq(api_key=api_key,model="llama-3.1-8b-instant")

    #store session id and upload the pdf file
    if "session_id" not in st.session_state:
        st.session_state.session_id=os.urandom(16).hex()
    uploaded_file=st.file_uploader("Upload a PDF file", type="pdf",accept_multiple_files=True)
    if uploaded_file:
        all_docs=[]
        for pdf_file in uploaded_file:
            tempdf=f"./temp_{st.session_state.session_id}.pdf"
            with open(tempdf,"wb") as f:
                f.write(pdf_file.getbuffer())
                
            loader=PyPDFLoader(tempdf)
            docs=loader.load()
            all_docs.extend(docs)
        
        #split the documents into chunks and store it in a vector database
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        documents=text_splitter.split_documents(all_docs)
        vectordb=Chroma.from_documents(documents,embedding=embeddings)
        retriever=vectordb.as_retriever()

        #create the retrieval chain
        prompt=ChatPromptTemplate.from_messages(
            [
                ("system","You are a helpful assistant. Use the following context to answer the user's question.\n\n{context}"),
                MessagePlaceholder("chat_history"),
                ("user","{input}")
            ]
        )

        document_chain=create_stuff_documents_chain(
            llm=llm,
            prompt=prompt
        )

        #retrieval_chain=retriever|document_chain

        retrieval_chain = create_retrieval_chain(
            retriever,
            document_chain
        )

        #get user question input
        user_input=st.text_input("Enter your question about the document here")
        submit=st.button("Generate Response")

        if user_input and submit:
            response=retrieval_chain.invoke(
                {"input":user_input},
                config={"configurable": {"session_id": st.session_state.session_id}}
            )
            

            st.text_area("Response", value=response)
            

    else:
        st.info("Please upload a PDF document to get started.")
else:
    st.warning("Please enter your GROQ API key to proceed.")
    



