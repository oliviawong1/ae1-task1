import random
import operator

def ask_question():
    """
    Runs the game where users solve for 'x'.
    Tracks the user's score and ends when they type 'quit'.
    """
    display_welcome_message()

    score = 0
    question_count = 0

    while True:
        equation, missing_value = create_equation()
        question_count += 1
        print(f"\nQuestion {question_count}: Solve this equation, what is x? : {equation}")

        user_input = get_user_input("Enter the missing value or 'quit' to exit: ")
        if user_input == "quit":
            end_game(score, question_count)
            return  # End the game

        if check_answer(user_input, missing_value):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect, the correct answer is {missing_value}")

        print(f"Your current score is {score} out of {question_count}")

if __name__ == "__main__":
    ask_question()