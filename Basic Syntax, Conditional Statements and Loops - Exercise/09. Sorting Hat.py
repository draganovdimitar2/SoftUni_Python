name = input()

while name != 'Welcome!':

    if name == 'Voldemort':
        print("You must not speak of that name!")
        break

    else:
        if len(name) > 6:
            print(f"{name} goes to Hufflepuff.")
        elif len(name) == 6:
            print(f"{name} goes to Ravenclaw.")
        elif len(name) == 5:
            print(f"{name} goes to Slytherin.")
        elif len(name) < 5:
            print(f"{name} goes to Gryffindor.")

    name = input()

else:
    print("Welcome to Hogwarts.")
