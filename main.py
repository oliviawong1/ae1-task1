import random
import operator

operations = {
    '+': operator.add,
    '÷': operator.floordiv,
    'x': operator.mul,
    '-': operator.sub,
}

def create_equation():
    """
    Generates a random equation with two random numbers and an operation.

    Returns:
        tuple: (first_number, second_number, operation, result)
    """
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 10)
    maths = random.choice(list(operations.keys()))  # Select a random operation
    result = operations[maths](first_number, second_number)  # Calculate the result
    return first_number, maths, second_number, result

# Test the function
print(create_equation())