command = input()
phonebook = {}

while True:
    if '-' in command:
        command = command.split('-')
        name, number = command[0], command[1]
        phonebook[name] = number  # if the name already exists, it's number will be updated

    elif command.isdigit():  # if it is digit the loop starts
        for _ in range(int(command)):  # make the command int
            name = input()

            if name in phonebook.keys():
                print(f'{name} -> {phonebook[name]}')
            else:
                print(f"Contact {name} does not exist.")

        break  # when the for-loop ends, we break out of the while-loop

    command = input()
