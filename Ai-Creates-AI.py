import random

# Function that generates a response to a given input
def generate_response(input):
    # Create a list of possible responses
    responses = [
        "I'm sorry, I don't understand.",
        "Could you please rephrase that?",
        "Can you please provide more information?",
        "I'm not sure what you mean.",
        "I'm not sure how to respond to that."
    ]

    # Return a random response from the list
    return random.choice(responses)

# Example conversation
while True:
    # Get input from the user
    user_input = input("You: ")

    # Generate a response
    response = generate_response(user_input)

    # Print the response
    print("Bot: ", response)
