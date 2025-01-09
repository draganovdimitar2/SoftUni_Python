def add(command, numbers):
    for num in command[:2:-1]:  # reversing the list so when we insert them at the index 0 they will keep their order
        numbers.insert(0, int(num))  # making inplace change to the mutable object, so no need to return anything

numbers = list(map(int,input().split()))
while True:
    command = input()
    if command == 'END':
        break

    command = command.split()
    action = command[0]
    if action == 'add':
        add(command, numbers)
    elif action == 'remove':
        if command[1] == 'greater':
            value = int(command[-1])
            numbers = [num for num in numbers if num <= value]
        else:
            index = int(command[-1])
            if index in range(len(numbers)):  # from 0 to last element inclusive
                numbers.pop(index)
    elif action == 'replace':
        value = int(command[1])
        if value in numbers:
            index = numbers.index(value)
            numbers[index] = int(command[-1])
    elif action == 'find':
        if command[1] == 'even':
            print(' '.join(map(str,[num for num in numbers if num % 2 == 0])))
        else:
            print(' '.join(map(str, [num for num in numbers if num % 2 != 0])))

print(', '.join(map(str, numbers)))


