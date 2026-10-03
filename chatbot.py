"""A simple rule-based chatbot for a beginner Python assignment."""


def get_response(user_input):
    """Return a chatbot response based on the user's message."""
    # Make matching ignore uppercase letters and extra spaces.
    message = user_input.strip().lower()

    if message == "hello" or message == "hi" or message == "hey":
        return "Hello! How can I help you?"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "bye" or message == "goodbye" or message == "exit" or message == "quit":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Please try another message."


def is_goodbye_message(user_input):
    """Return True when the user wants to end the chat."""
    message = user_input.strip().lower()
    return message == "bye" or message == "goodbye" or message == "exit" or message == "quit"


def main():
    """Keep chatting until the user enters a goodbye message."""
    print("Basic Chatbot")
    print("Type 'bye', 'goodbye', 'exit', or 'quit' to end the chat.")

    # The loop keeps accepting messages until a goodbye message is entered.
    while True:
        user_input = input("You: ")
        print("Bot:", get_response(user_input))

        if is_goodbye_message(user_input):
            break


if __name__ == "__main__":
    main()
