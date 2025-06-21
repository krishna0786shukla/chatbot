import nltk
from nltk.stem import WordNetLemmatizer
import random

# Initialize
lemmatizer = WordNetLemmatizer()

# Sample intents/responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
    "goodbye": ["Bye!", "Goodbye!", "See you later!"],
    "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
    "age": ["I'm a timeless piece of code!", "Age is just a number when you're digital."],
    "name": ["I'm ChatBot!", "I'm your friendly Python chatbot."],
    "default": ["Sorry, I didn't understand that.", "Can you rephrase?", "I'm still learning!"]
}

keywords = {
    "greeting": ["hello", "hi", "hey", "greetings"],
    "goodbye": ["bye", "goodbye", "see you", "later"],
    "thanks": ["thanks", "thank", "appreciate"],
    "age": ["how old", "your age", "age"],
    "name": ["your name", "who are you", "name"]
}

# Clean and process input
def preprocess(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    return [lemmatizer.lemmatize(token) for token in tokens]

# Match intent
def get_intent(user_input):
    processed = preprocess(user_input)
    for intent, keys in keywords.items():
        for word in keys:
            if any(word in token for token in processed):
                return intent
    return "default"

# Chat loop
def chatbot():
    print("🤖 ChatBot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("🤖 ChatBot:", random.choice(responses["goodbye"]))
            break
        intent = get_intent(user_input)
        print("🤖 ChatBot:", random.choice(responses[intent]))

if __name__ == "__main__":
    chatbot()
