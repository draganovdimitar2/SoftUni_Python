N = int(input())
stack = []

for _ in range(N):
    inputs = input().split()
    command = int(inputs[0])
    if command == 1:
        number = int(inputs[-1])
        stack.append(number)
    elif stack:
        if command == 2:
            stack.pop()
        elif command == 3:
            print(max(stack))
        elif command == 4:
            print(min(stack))

while stack:
    if len(stack) > 1:
        print(stack.pop(), end = ', ')
    else:
        print(stack.pop(), end = '')
