# AI_CHATBOT_NLTK
ChatGPT said:This project is an AI Chatbot built using Python, NLTK, and Streamlit. It answers FAQs about admissions, fees, and placements using NLP techniques like tokenization and lemmatization. The chatbot processes user input, matches keywords from a JSON file, and responds interactively through a web interface.

Overview:

This project is a simple FAQ-based chatbot built using Python, NLTK, and Streamlit.
It can answer basic questions about admissions, fees, and placements by matchin

Key Components:

1.faqs.json
Stores a set of predefined questions and answers, for example:

{
  "admission": "Admissions are open till December 2025. Apply through our online portal.",
  "fees": "Course fee is ₹60,000 per year including lab access.",
  "placements": "Top recruiters include TCS, Infosys, and Wipro."
}

2.chatbot.py
A command-line chatbot version.
Uses NLTK for tokenization and lemmatization.
Continuously interacts with the user until they type “bye”, “exit”, or “quit”.
Matches keywords from input to keys in the FAQ data to generate responses.

3.app.py
A web-based chatbot interface built with Streamlit.
Provides a simple UI for chatting with the bot.
Displays chatbot responses interactively when the user clicks “Send”.

4.requirements.txt
Lists dependencies:
nltk
streamlit

-->How It Works:

The chatbot loads FAQ data from faqs.json.

User input is preprocessed — converted to lowercase, tokenized, and lemmatized.

If any keyword (like “admission”, “fees”, or “placements”) is found in the processed tokens, the chatbot retrieves the corresponding answer.

If no match is found, it replies with a default fallback message.

-->Command-line version:
python chatbot.py
-->Streamlit web app:
streamlit run app.py

-->Libraries Used:

  NLTK → for text preprocessing (tokenization, lemmatization).

  Streamlit → for building the web user interface.

-->Learning Outcomes:

Demonstrates basic natural language processing (NLP) using NLTK.

Shows how to build an interactive chatbot using Streamlit.

Provides a foundation for expanding into context-aware or ML-based chatbots later.

