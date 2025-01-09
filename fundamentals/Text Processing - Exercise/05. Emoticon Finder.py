some_string = input()
for index in range(len(some_string)):
    if some_string[index] == ':':
        if index + 1 in range(len(some_string)):
            print(f':{some_string[index + 1]}')
