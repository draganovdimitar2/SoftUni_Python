def scramble(message: str, character: str, position: int) -> str:
    message = message[:position] + character + message[position + 1:]
    return message


string = input()
command = input().split()

while command != ['Finalize']:
    if command == ['Encrypt']:
        string = string[::-1]
        print(string)
    elif command == ['Decrypt']:
        string = string.swapcase()
        print(string)
    elif command[0] == 'Substitute':
        old_char = command[1]
        if old_char not in string:
            print("Character not found.")
        else:
            new_char = command[2]
            string = string.replace(old_char, new_char)
            print(string)
    elif command[0] == 'Scramble':
        index = int(command[1])
        if index not in range(len(string)):
            print("Index out of bounds.")
        else:
            char = command[2]
            string = scramble(string, char, index)
            print(string)
    elif command[0] == 'Remove':
        substring = command[1]
        string = string.replace(substring, '')
        print(string)
    else:
        print("Invalid command detected!")

    command = input().split()
