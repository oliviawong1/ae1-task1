import random
import operator

def create_equation():
    operations = {
        "+": operator.add,
        "*": operator.mul,
        "-": operator.sub,
    }

    first_number = random.randint(1, 5)
    second_number = random.randint(1, 5)
    operation = random.choice(list(operations.keys()))

    # Calculate the answer using the selected operation
    answer = operations[operation](first_number, second_number)

    part = ["first_number","second_number","answer"]
    missing_part = random.choice(list(part))

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

def ask_question():
    print("Welcome to the equation game")
    print("Enter 'quit' to end the program")

    score = 0
    question_count = 0

    while True:
        equation, missing_value = create_equation()
        question_count += 1
        print(f"\nQuestion {question_count}: Solve this equation, what is x? : {equation}")

        while True:  # Input validation loop
            user_input = input("Enter the missing value or 'quit' to exit: ").strip().lower()
            
            if user_input == "quit":
                print(f"\nThank you for playing, your final score is {score} out of {question_count}")
                return  # Exit the game
            
            try:
                user_input = int(user_input)
                break  # Exit the input validation loop if input is valid
            except ValueError:
                print("Invalid input. Please enter a number or 'quit' to exit.")

        if user_input == missing_value:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect, the correct answer is {missing_value}")

        print(f"Your current score is {score} out of {question_count}")

ask_question()