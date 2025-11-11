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

#load libraries to store the history of the chat
from langchain_core.prompts import MessagesPlaceholder
from langchain_classic.chains import create_history_aware_retriever
from langchain_community.chat_message_histories import ChatMessageHistory
#from langchain_core.runnables.history import RunnableWithChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
#from langchain_core.chat_history import ChatMessageHistory as BasechatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory



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

        contextualize_q_system_prompt=(
            "Given a chat history and the latest user question"
            "which might reference context in the chat history, "
            "formulate a standalone question which can be understood "
            "without the chat history. Do NOT answer the question, "
            "just reformulate it if needed and otherwise return it as is."
        )
        contextualize_q_prompt = ChatPromptTemplate.from_messages(
                [
                    ("system", contextualize_q_system_prompt),
                    MessagesPlaceholder("chat_history"),
                    ("human", "{input}"),
                ]
            )

        history_aware_retriever=create_history_aware_retriever(llm,retriever,contextualize_q_prompt)


        #Answer question
        system_prompt=ChatPromptTemplate.from_messages(
            [
                ("system","You are a helpful assistant. Use the following context to answer the user's question.\n\n{context}"),
                MessagesPlaceholder(variable_name="chat_history"),
                ("user","{input}")
            ]
        )
        prompt=ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                MessagesPlaceholder(variable_name="chat_history"),
                ("user", "{input}")
            ]
        )
        qa_chain=create_stuff_documents_chain(llm, prompt)
        retrieval_chain = create_retrieval_chain(
            history_aware_retriever,
            qa_chain
        )

        #get session based chat history
        def get_session_history(session_id: str) -> BasechatMessageHistory:
            if session_id not in st.session_state.store:
                st.session_state.store[session_id] = ChatMessageHistory()
            return st.session_state.store[session_id]

        conversation_history_runnable = RunnableWithMessageHistory(
            #retrieval_chain.get_session_history,

            runnable=retrieval_chain,
            get_session_history=lambda _: ChatMessageHistory(),

            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer"
        )
        #get user question input
        user_input=st.text_input("Enter your question about the document here")
        submit=st.button("Generate Response")

        if user_input and submit:
            session_history=get_session_history(st.session_state.session_id)
            response=conversation_history_runnable.invoke(
                {"input":user_input},
                config={"configurable": {"session_id": st.session_state.session_id}}
            )
            st.write(st.session_state.store)
            st.write("Assistant:", response['answer'])
            st.write("Chat History:", session_history.messages)

    else:
        st.info("Please upload a PDF document to get started.")
else:
    st.warning("Please enter your GROQ API key to proceed.")
    



