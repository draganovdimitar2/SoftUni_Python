def move(message: str, letters: int) -> str:
    letters_slice = message[:letters]
    message = message.replace(letters_slice,
                              '') + letters_slice  # first remove the letters, then using concatenation add them to the end of the string
    return message


def insert(message: str, index: int, value_to_insert: str) -> str:
    message = message[:index] + value_to_insert + message[index:]
    return message


def change_all(message: str, substring: str, replacement: str) -> str:
    message = message.replace(substring, replacement)
    return message


encrypted_message = input()

instructions = input()
while instructions != 'Decode':
    instructions = instructions.split('|')
    action = instructions[0]
    if action == 'Move':
        letters_to_move = int(instructions[1])
        encrypted_message = move(encrypted_message, letters_to_move)
    elif action == 'Insert':
        starting_index = int(instructions[1])
        value = instructions[2]
        encrypted_message = insert(encrypted_message, starting_index, value)
    else:  # action == 'ChangeAll'
        old_string = instructions[1]
        new_string = instructions[2]
        encrypted_message = change_all(encrypted_message, old_string, new_string)

    instructions = input()

print(f"The decrypted message is: {encrypted_message}")
