import random
import operator

def create_equation():
    operations = {
        '+': operator.add,
        '//': operator.floordiv,
        '*': operator.mul,
        '-': operator.sub,
    }

    first_number = random.randint(1,5)
    second_number = random.randint(1,5)
    operation = random.choice(list(operations.keys()))

    answer = operations[operation](first_number,second_number)
    equation = f"{first_number} {operation} {second_number}"
    return equation, answer

create_equation()