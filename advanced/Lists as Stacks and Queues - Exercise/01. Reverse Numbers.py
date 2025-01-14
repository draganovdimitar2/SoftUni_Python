some_integers = input().split()

stack = []
while some_integers:
    stack.append(some_integers.pop())

print(" ".join(stack))
