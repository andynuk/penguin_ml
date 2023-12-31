import streamlit as st
from openai import OpenAI

st.title("OpenAI Demo")

text = st.text_input("Enter text to analyse")
analyze_button = st.button("Analyse Text")

client = OpenAI(api_key = st.secrets["OPENAI_API_KEY"])

if analyze_button:
    messages = [
        {"role":"system",
         "content": """You are a lepful sentiment analysis assistant. You always respond with the sentiment of the text you are
         given and the confidence of you sentiment analysis with a number between 0 and 1"""},
        {"role":"user",
         "content": f"Sentiment analysis of the the following text: {text}"}
    ]
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    sentiment = response.choices[0].message.content
    st.write(sentiment)
    st.write(response.model_dump_json(indent=2))


