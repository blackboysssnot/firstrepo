def calculator_chatbot():
    print("Hello! I'm your calculator chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            # Evaluate the user's input as a math expression
            result = eval(user_input, {"__builtins__": None}, {})
            print(f"Bot: The answer is {result}")
        except Exception as e:
            print("Bot: Sorry, I couldn't understand that. Please enter a valid math expression.")

if __name__ == "__main__":
    calculator_chatbot()