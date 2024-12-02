liked_meals = {}  # {guest: [meal_one, meal_two..]}
unliked_meals_count = 0
command = input()

while command != 'Stop':
    command = command.split('-')
    action = command[0]
    guest = command[1]
    meal = command[2]

    if action == 'Like':
        if guest not in liked_meals:
            liked_meals[guest] = []
        if meal in liked_meals[guest]:
            continue
        liked_meals[guest].append(meal)
    else:
        if guest in liked_meals and meal in liked_meals[guest]:
            unliked_meals_count += 1
            liked_meals[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")
        else:
            if guest not in liked_meals:
                print(f"{guest} is not at the party.")
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")

    command = input()

for guest in liked_meals:
    print(f'{guest}: {", ".join(liked_meals[guest])}')
print(f"Unliked meals: {unliked_meals_count}")
