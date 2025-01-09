command = input()
new_word = ''
while command != 'End':

    if command == 'SoftUni':
        command = input()
        continue

    for char in command:
        character = char * 2
        new_word += character

    print(new_word)
    new_word = ''
    command = input()