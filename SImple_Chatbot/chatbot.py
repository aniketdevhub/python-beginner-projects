from responses import get_response

print("=" * 40)
print("Python ChatBot")
print("Type 'bye' to exit")
print("=" * 40)

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    print("Bot:", get_response(user_input))