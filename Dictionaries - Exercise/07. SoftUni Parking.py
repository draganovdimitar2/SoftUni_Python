number_of_command = int(input())
database = {}

for _ in range(number_of_command):
    command = input().split(' ')
    action, name = command[0], command[1]

    if action == 'register':
        plate = command[2]
        if name in database:  # if user already exists
            print(f"ERROR: already registered with plate number {database[name]}")
        else:
            database[name] = plate
            print(f"{name} registered {plate} successfully")
    else:  # unregister case
        if name not in database:  # if user doesn't exist
            print(f"ERROR: user {name} not found")
        else:
            database.pop(name)  # remove the user
            print(f"{name} unregistered successfully")

for name, plate in database.items():
    print(f'{name} => {plate}')
