from functools import reduce

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}

def operate(operator, *args):
    return reduce(operations[operator], args)
