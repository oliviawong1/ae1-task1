import random
import operator

# Define operations
operations = {
    '+': operator.add,
    '//': operator.floordiv,
    '*': operator.mul,
    '-': operator.sub,
}
def create_equation():
    """
    Create random equation and calculate answer 

    Returns: 
    tuple: first_number, operation, second_number, result
    """
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    operation = random.choice(list(operations.keys()))
    
    # Calculate the answer
    answer = operations[operation](first_number, second_number)
    #return f"{first_number} {operation} {second_number}", answer

    part = ["first_number", "second_number","answer"]
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

equation, missing_value = create_equation()
print("Equation:", equation)
print("Missing value:", missing_value)