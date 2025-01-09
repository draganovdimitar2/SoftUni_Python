command = input()
counter = 1
resources = {}
current_key = ''

while command != 'stop':
    if counter % 2 != 0:
        current_key = command  # to save out key for later
    else:
        if current_key in resources.keys():  # check if this key already exists
            resources[current_key] += int(command)  # if it exists, we add more quantity to the same key
        else:
            resources[current_key] = int(command)  # if it doesnt, add the key and value to our dict

    command = input()
    counter += 1

for k, v in resources.items():
    print(f'{k} -> {v}')
