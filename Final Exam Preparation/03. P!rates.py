command = input()
cities = {}

while command != 'Sail':
    city, population, gold = command.split("||")
    if city in cities:
        cities[city][0] += int(population)
        cities[city][1] += int(gold)
    else:
        cities[city] = [int(population), int(gold)]

    command = input()

event = input()
while event != 'End':
    event = event.split('=>')
    action = event[0]
    town = event[1]

    if action == "Plunder":
        people = int(event[2])
        gold = int(event[3])
        cities[town][0] -= people
        cities[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town][1] <= 0 or cities[town][0] <= 0:
            cities.pop(town)  # remove the town if gold or population is under 0
            print(f"{town} has been wiped off the map!")


    elif action == 'Prosper':
        gold = int(event[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")

    event = input()

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city in cities:
        print(f'{city} -> Population: {cities[city][0]} citizens, Gold: {cities[city][1]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
