command = input()
coffees = 0

while command != 'END':

    if (command == 'coding' or command == 'CODING' or
        command == 'dog' or command == 'DOG' or
        command == 'cat' or command == 'CAT' or
        command == 'movie' or command == 'MOVIE'):

        if command.islower():
            coffees += 1

        else:
            coffees += 2

    command = input()

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)
