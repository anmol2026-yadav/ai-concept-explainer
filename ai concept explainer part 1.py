import streamlit as st
import os
from openai import OpenAI
client = OpenAI(api_key="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")

st.title("AI Concept Explainer 🧠")
st.write("Understand any topic easily — explained like you're 12!")

topic = st.text_input("Enter a topic or concept you want to understand:")
language = st.selectbox("Choose explanation language:", ["English", "Hindi"])

if st.button("Explain"):
    prompt = f"Explain the concept '{topic}' in very simple {language}. Use real-life examples and short sentences. Avoid jargon."
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    
    st.subheader("Explanation 👇")
    st.write(response.choices[0].message.content)
