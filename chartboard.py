def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what is your name":
        return "my name is kartavya chaubey!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

def run_chatbot():
    print("Welcome to the Chatbot! (Type 'bye' to exit)")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        
        if user_input.lower() == "bye":
            break

run_chatbot()
