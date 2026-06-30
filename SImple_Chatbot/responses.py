def get_response(message):
    message = message.lower().strip()

    responses = {
        "hello": "Hello! How can I help you?",
        "hi": "Hi there!",
        "how are you": "I'm just a Python program, but I'm doing great!",
        "your name": "I'm a Rule-Based Python Chatbot.",
        "help": "You can greet me or ask my name.",
        "thanks": "You're welcome!",
        "thank you": "Happy to help!",
        "bye": "Goodbye!",
    }

    for key in responses:
        if key in message:
            return responses[key]

    return "Sorry, I don't understand that."
