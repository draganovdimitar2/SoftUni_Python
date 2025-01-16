from collections import deque

expression = input().split()
numbers = deque()

operators = {  # mapper (also can be done with if/else construction)
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}

for char in expression:
    if char not in "+-*/":
        numbers.append(int(char))
    else:
        while len(numbers) > 1:  # we can't do operations with only one number
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            numbers.appendleft(operators[char](first_num, second_num))

print(*numbers)  # print(numbers[0])
