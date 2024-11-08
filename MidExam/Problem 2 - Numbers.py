def add(numbers, value):
    numbers.append(value)

def remove(numbers, value):
    if value in numbers:
        numbers.remove(value)

def replace(numbers, value, replacement):
    if value in numbers:
        index = numbers.index(value)
        numbers[index] = replacement

def collapse(numbers, value):
    return [num for num in numbers if num >= value]

numbers = list(map(int,input().split()))
while True:
    command = input()
    if command == 'Finish':
        break
    command = command.split()
    value = int(command[1])

    if command[0] == 'Add':
        add(numbers, value)
    elif command[0] == 'Remove':
        remove(numbers, value)
    elif command[0] == 'Replace':
        replacement = int(command[-1])
        replace(numbers, value, replacement)
    elif command[0] == 'Collapse':
        numbers = collapse(numbers, value)

print(' '.join(map(str, numbers)))

