
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""


def get_user_name():
    while True:
        name = input("Please enter your name: ").strip()
        if name:
            return name
        else:
            print("Name cannot be empty. Please try again.")

def get_user_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age > 0:
                return age
            else:
                print("Age must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number for age.")

def greet_user(user_name, user_age):
    if 0 < user_age <= 18:
        print(f"Wow, {user_name}! You're {user_age}? Your future is vast!. How can I help you?")
    elif 18 < user_age <= 30:
        print(f"Hello, {user_name}! You are doing great! What brings you here today?")
    elif 30 < user_age <= 60:
        print(f"Hello, {user_name}! How is life? How may I help you?")
    elif 60 < user_age <= 99:
        print(f"I can sense you have many stories to tell, {user_name}! How may I help you?")
    elif user_age >= 100:
        print(f"{user_age}? That's outstanding! What can I do to serve you today?")
    else:
        print("Please try again")




def help_user():
    return input(
        "1. Placeholder Option 1\n"
        "2. Placeholder Option 2\n"
        "3. Placeholder Option 3\n"
        "4. Exit\n"
        "Please choose a number: "
        )

def main():
    user_name = get_user_name()
    user_age = int(get_user_age())
    greet_user(user_name, user_age)

    while True:
        user_answer = help_user()
        if user_answer.lower() == "1":
            pass
        elif user_answer.lower() == "2":
            pass
        elif user_answer.lower() == "3":
            pass
        elif user_answer.lower() == "4":
            print("Goodbye!")
            break
        else:
            print("Please try again")

if __name__ == "__main__":
    main()
