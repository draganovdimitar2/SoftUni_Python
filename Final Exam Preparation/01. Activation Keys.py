def contains(raw_string: str, new_str: str) -> bool:  # return True if substring in raw_activation_key
    if new_str in raw_string:
        return True
    return False


def flip(upper_lower: str, activation_key: str, first_index: int, second_index: int) -> str:
    sliced_str = activation_key[first_index:second_index]
    if upper_lower == 'Upper':
        new_str = sliced_str.upper()  # convert each char from lowercase to uppercase
    else:
        new_str = sliced_str.casefold()
    activation_key = activation_key.replace(sliced_str, new_str)
    return activation_key


def delete(activation_key: str, first_index: int, second_index: int) -> str:
    sliced_str = activation_key[first_index:second_index]
    activation_key = activation_key.replace(sliced_str, '')
    return activation_key


raw_activation_key = input()

command = input()
while command != 'Generate':
    instruction = command.split('>>>')
    action = instruction[0]
    if action == 'Contains':
        substring = instruction[-1]
        if contains(raw_activation_key, substring):
            print(f"{raw_activation_key} contains {substring}")
        else:  # if substring not in raw_activation_key
            print("Substring not found!")
    elif action == 'Flip':
        upper_or_lower = instruction[1]
        start_index = int(instruction[-2])
        end_index = int(instruction[-1])
        raw_activation_key = flip(upper_or_lower, raw_activation_key, start_index, end_index)
        print(raw_activation_key)
    else:  # action == 'Slice'
        start_index = int(instruction[1])
        end_index = int(instruction[2])
        raw_activation_key = delete(raw_activation_key, start_index, end_index)
        print(raw_activation_key)

    command = input()

print(f'Your activation key is: {raw_activation_key}')
