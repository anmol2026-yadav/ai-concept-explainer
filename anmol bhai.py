import streamlit as st
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
