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

equation, missing_value = create_equation()
print("Equation:", equation)
print("Answer:", missing_value)

