n = int(input())

for commands in range(n):
    command = input()

    for char in command:
        if ',' in command or '.' in command or '_' in command:
            print(f'{command} is not pure!')
            break
    else:
        print(f'{command} is pure.')