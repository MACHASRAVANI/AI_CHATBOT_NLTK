import json
import nltk
import streamlit as st
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Load FAQ data
with open("faqs.json", "r") as f:
    faqs = json.load(f)

# Initialize NLTK tools
lemmatizer = WordNetLemmatizer()

# Preprocessing function
def preprocess(text):
    tokens = word_tokenize(text.lower())
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmas

# Response generation
def get_response(user_input):
    tokens = preprocess(user_input)
    for key in faqs.keys():
        if key in tokens:
            return faqs[key]
    return "Sorry, I didn’t understand that. Can you please rephrase?"

# Streamlit Web UI
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 AI Chatbot using NLTK")
st.write("Ask me about **admissions**, **fees**, or **placements**!")

# Text input box
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input.strip():
        response = get_response(user_input)
        st.markdown(f"**Chatbot:** {response}")
    else:
        st.warning("Please type something before sending.")
