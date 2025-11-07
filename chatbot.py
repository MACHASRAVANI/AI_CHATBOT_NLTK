import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Load FAQ data
with open("faqs.json", "r") as f:
    faqs = json.load(f)

# Initialize NLTK tools
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = word_tokenize(text.lower())
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmas

def get_response(user_input):
    tokens = preprocess(user_input)
    
    for key in faqs.keys():
        if key in tokens:
            return faqs[key]
    
    return "Sorry, I didn’t understand that. Can you please rephrase?"

# Chat loop
print("🤖 Chatbot: Hello! Ask me about admissions, fees, or placements.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("🤖 Chatbot: Goodbye! 👋")
        break
    response = get_response(user_input)
    print("🤖 Chatbot:", response)
