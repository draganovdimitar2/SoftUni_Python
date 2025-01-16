from collections import deque

bees = deque(map(int, input().split()))  # queue
nectar = deque(map(int, input().split()))  # stack
symbols = deque(input().split())  # queue
honey_made = 0

operators = {
    "+": lambda a, b: abs(a + b),
    "-": lambda a, b: abs(a - b),
    "*": lambda a, b: abs(a * b),
    "/": lambda a, b: abs(a / b)
}

while bees and nectar:
    if bees[0] <= nectar[-1]:  # collected
        if symbols[0] == '/' and nectar[-1] <= 0:  # we can't divide a num by zero
            bees.popleft(), nectar.pop(), symbols.popleft()
            continue
        honey_made += operators[symbols[0]](bees[0], nectar[-1])
        bees.popleft(), nectar.pop(), symbols.popleft()

    else:
        nectar.pop()  # remove the nectar

print(f"Total honey made: {honey_made}")
print(f"Bees left: {', '.join(map(str, bees))}") if bees else None
print(f"Nectar left: {', '.join(map(str, nectar))}") if nectar else None
