import os
from constants import openai_key

from langchain.llms import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

#streamlit framework

st.title("Langchain GPT")
prompt = st.text_input("Enter the Search Query")

#LLMs
llm =OpenAI(temperature = 0.9)
if prompt :
    response = llm(prompt)
    st.write(response)
