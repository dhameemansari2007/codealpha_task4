"""
CodeAlpha — Task 4: Basic Chatbot
Rule-based replies for a small set of inputs.
Key concepts: if-elif, functions, loops, input/output.
"""


def reply(message):
    text = message.strip().lower()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    if text in ("how are you", "how are you?"):
        return "I'm fine, thanks!"
    if text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    if text in ("what is your name", "who are you"):
        return "I'm a simple CodeAlpha chatbot."
    if text in ("help",):
        return "Try: hello, how are you, bye."
    return "I don't understand that. Try hello, how are you, or bye."


def main():
    print("=== BASIC CHATBOT ===")
    print("Type a message. Type bye to exit.")
    while True:
        user = input("You: ")
        answer = reply(user)
        print("Bot:", answer)
        if user.strip().lower() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    main()
