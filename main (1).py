'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import random

# Define a list of predefined rules and responses
rules = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm just a computer program, but I'm here to help!", "I don't have feelings, but I'm here to assist you."],
    "bye": ["Goodbye!", "See you later!", "Bye now!"],
    "default": ["I'm not sure what you mean. Can you please rephrase?", "I didn't understand that. Can you try again?"]
}

# Function to get a response based on user input
def get_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if any predefined rule matches the user input
    for key in rules:
        if key in user_input:
            return random.choice(rules[key])

    # If no rule matches, return a default response
    return random.choice(rules["default"])

# Main loop for chatting
print("Chatbot: Hi! I'm your simple chatbot. How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)

