import random
import operator

operations = {
    '+': operator.add,
    '/': operator.truediv,
    '*': operator.mul,
    '-': operator.sub,
}

def create_equation():
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 10)
    maths = random.choice(list(operations.keys()))
    result = operations[maths](first_number, second_number)
    return first_number, maths, second_number, result
