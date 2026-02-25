import datetime

def print_header():
    print("\n" + "=" * 55)
    print(" 🤖  SMART RULE-BASED CHATBOT ")
    print("=" * 55)
    print(" Type 'help' to see what I can do")
    print(" Type 'exit' or 'bye' to end the chat")
    print("=" * 55)

def chatbot():
    print_header()

    while True:
        user_input = input("\n👤 You: ").strip().lower()

        if user_input == "hi" or user_input == "hello":
            print("🤖 Bot: Hello! Nice to meet you 😊")

        elif "how are you" in user_input:
            print("🤖 Bot: I'm doing great! Thanks for asking 😄")

        elif "your name" in user_input:
            print("🤖 Bot: I'm a rule-based chatbot built using Python 🐍")

        elif "help" in user_input:
            print("🤖 Bot: I can respond to:")
            print("       - greetings (hi, hello)")
            print("       - time")
            print("       - basic questions")
            print("       - exit command")

        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"🤖 Bot: Current time is {current_time} ⏰")

        elif user_input == "bye" or user_input == "exit":
            print("🤖 Bot: Goodbye! Have a great day 👋✨")
            print("=" * 55)
            break

        elif user_input == "":
            print("🤖 Bot: Please type something 🙂")

        else:
            print("🤖 Bot: Sorry, I didn't understand that 🤔")

# Program starts here
if __name__ == "__main__":
    chatbot()