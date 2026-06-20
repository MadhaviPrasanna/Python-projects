# ==========================================
# ADVANCED BASIC CHATBOT PROJECT
# ==========================================

import datetime


# Function to display chatbot introduction
def show_welcome():

    print("=" * 60)
    print("            WELCOME TO PYTHON CHATBOT")
    print("=" * 60)

    print("\nI can perform the following tasks:")
    print("1. Greet you")
    print("2. Tell my name")
    print("3. Tell the current date and time")
    print("4. Tell a joke")
    print("5. Perform simple calculations")
    print("6. Answer basic questions")
    print("7. Exit the chat")

    print("\nType 'help' to see commands again.")
    print("Type 'bye' to end the conversation.")


# Function for chatbot responses
def chatbot_response(user_input, user_name):

    user_input = user_input.lower()

    if user_input == "hello":
        return f"Hello {user_name}! Nice to meet you."

    elif user_input == "hi":
        return f"Hi {user_name}! How are you today?"

    elif user_input == "how are you":
        return "I am doing great. Thank you for asking!"

    elif user_input == "what is your name":
        return "My name is Python ChatBot."

    elif user_input == "who created you":
        return "I was created as a Python programming project."

    elif user_input == "what can you do":
        return ("I can chat with you, tell jokes, "
                "show date and time, and perform calculations.")

    elif user_input == "thank you":
        return "You're welcome!"

    elif user_input == "help":
        return (
            "\nAvailable Commands:\n"
            "hello\n"
            "hi\n"
            "how are you\n"
            "what is your name\n"
            "who created you\n"
            "what can you do\n"
            "time\n"
            "date\n"
            "joke\n"
            "calculator\n"
            "bye"
        )

    elif user_input == "date":
        today = datetime.date.today()
        return f"Today's date is: {today}"

    elif user_input == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Current time is: {current_time}"

    elif user_input == "joke":
        return ("Why do programmers prefer Python?\n"
                "Because it is easy to read and write!")

    elif user_input == "bye":
        return f"Goodbye {user_name}! Have a wonderful day."

    else:
        return "Sorry, I don't understand that command."


# Function for simple calculator
def calculator():

    print("\n========== CALCULATOR ==========")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":

            if num2 == 0:
                print("Cannot divide by zero.")
                return

            result = num1 / num2

        else:
            print("Invalid operator.")
            return

        print("Result =", result)

    except ValueError:
        print("Please enter valid numbers.")


# Main chatbot function
def main():

    show_welcome()

    user_name = input("\nEnter your name: ")

    print(f"\nChatBot: Welcome, {user_name}!")

    while True:

        user_message = input(f"\n{user_name}: ")

        # Calculator command
        if user_message.lower() == "calculator":
            calculator()
            continue

        response = chatbot_response(user_message, user_name)

        print("ChatBot:", response)

        # Exit condition
        if user_message.lower() == "bye":
            break


# Program starts here
main()
