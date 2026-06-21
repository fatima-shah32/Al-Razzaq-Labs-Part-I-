print("=== Lab 30: Simple Chatbot Logic ===")


def simple_chatbot(user_input):

    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi there! How can I help you today?"

    elif user_input == "what is your name?":
        return "I am a simple chatbot created for this lab."

    elif user_input == "how are you":
        return "I am doing great. Thanks for asking!"

    elif user_input == "what is python":
        return "Python is a popular programming language."

    elif user_input == "what is ai":
        return "AI stands for Artificial Intelligence."

    elif user_input == "help":
        return "You can ask me about Python, AI, my name, or say hello."

    elif user_input == "bye":
        return "Goodbye! Have a great day!"

    else:
        return "I'm sorry, I didn't understand that."


def run_chatbot():

    print("\nWelcome to the Simple Chatbot!")
    print("Type 'bye' to exit.\n")

    chat_log = []

    while True:

        user_input = input("You: ")

        response = simple_chatbot(user_input)

        print("Bot:", response)

        chat_log.append(
            f"You: {user_input}\nBot: {response}\n"
        )

        if user_input.lower() == "bye":
            break

    # Save chat history
    with open("chat_history.txt", "w") as file:

        file.write("Lab 30 Chatbot Conversation Log\n\n")

        for item in chat_log:
            file.write(item + "\n")

    print("\nChat history saved as chat_history.txt")


if __name__ == "__main__":
    run_chatbot()
