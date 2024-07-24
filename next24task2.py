import random

# Sample responses
responses = {
    "greet": ["Hello!", "Hi there!", "Greetings!", "How can I help you?"],
    "bye": ["Goodbye!", "See you later!", "Take care!", "Bye!"],
    "thanks": ["You're welcome!", "My pleasure!", "Glad to help!", "Anytime!"],
}

# Keywords for matching user input
keywords = {
    "greet": ["hello", "hi", "greetings"],
    "bye": ["bye", "goodbye", "see you"],
    "thanks": ["thank you", "thanks"],
}

def get_response(user_input):
    user_input = user_input.lower()
    
    for key, words in keywords.items():
        if any(word in user_input for word in words):
            return random.choice(responses[key])
    
    return "I'm sorry, I didn't understand that."

def chat():
    print("Chatbot: Hello! I'm here to assist you. (Type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chat()
