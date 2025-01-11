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
    second_number = random.randint(1, 20)
    operation = random.choice(list(operations.keys()))
    
    # Calculate the answer
    answer = operations[operation](first_number, second_number)
    
    # Return equation and answer
    return first_number, operation, second_number, answer

print(create_equation)