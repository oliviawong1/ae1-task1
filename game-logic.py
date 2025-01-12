import random
import operator

def create_equation():
    """
    Creates a random math equation with one missing value.
    Returns the equation with 'x' as the missing value.
    """
    operations = {
        "+": operator.add,
        "*": operator.mul,
        "-": operator.sub,
    }

    first_number = random.randint(1, 10)
    second_number = random.randint(1, 5)
    operation = random.choice(list(operations.keys()))

    answer = operations[operation](first_number, second_number)

    part = ["first_number", "second_number", "answer"]
    missing_part = random.choice(part)

    if missing_part == "first_number":
        equation = f"x {operation} {second_number} = {answer}"
        missing_value = first_number
    elif missing_part == "second_number":
        equation = f"{first_number} {operation} x = {answer}"
        missing_value = second_number
    else:
        equation = f"{first_number} {operation} {second_number} = x"
        missing_value = answer

    return equation, missing_value

def get_user_input(prompt):
    """
    Prompts the user for input and validates it.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == "quit":
            return user_input 
        try:
            return int(user_input)  # Valid number input
        except ValueError:
            print("Invalid input. Please enter a number or 'quit'.")
            
def display_welcome_message():
    """
    Displays welcome message for equation game.
    """
    print("Welcome to the equation game!")
    print("Enter 'quit' to end the program")

def check_answer(user_input, correct_answer):
    """
    Checks if the user's answer is correct.
    """
    return user_input == correct_answer

def end_game(score, question_count):
    """
    Ends the game and displays the final score.
    """
    print(f"\nThank you for playing! Your final score is {score} out of {question_count - 1}")

