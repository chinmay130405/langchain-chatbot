from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# App Title and Description
st.set_page_config(page_title="Llama 2 Translator Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Llama 2 Translator Chatbot")
st.markdown("""
Welcome to the **Llama 2 Translator Chatbot**!\
Enter your question in English and get a professional French translation powered by Meta's Llama 2 model running locally via Ollama.
""")

##Prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that translates English to French."),
        ("user", "Question: {question}"),
    ]
)

##streamlit framework
input_text=st.text_input("Type your question in English:", placeholder="e.g. How are you today?")


#Ollama LLAma2 LLM
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

# Output
if input_text:
    with st.spinner("Translating..."):
        response = chain.invoke({"question": input_text})
        st.success("**French Translation:**")
        st.write(response)

# Footer
st.markdown("<hr style='margin-top:2em;margin-bottom:1em'>", unsafe_allow_html=True)
st.caption("Built with LangChain, Streamlit, and Ollama · © 2025")