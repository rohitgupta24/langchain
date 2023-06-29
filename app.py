import os

from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st


#streamlit framework

st.title("Langchain Demo")
input_text = st.text_input("Search the topic")

if input_text : 
    pass
