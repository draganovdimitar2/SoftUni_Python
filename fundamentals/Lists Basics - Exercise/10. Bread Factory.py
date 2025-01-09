events = input().split("|")
current_energy = 100
current_coins = 100
bakery_is_open = True

for event in events:
    event_items = event.split("-")
    type_of_event = event_items[0]
    event_value =  int(event_items[1])

    if type_of_event == "rest":
        initial_energy = current_energy
        current_energy += event_value

        if current_energy > 100:
            current_energy = 100

        gained_energy = current_energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")

    elif type_of_event == "order":
        if current_energy >= 30: # I can complete the order
            current_energy -= 30
            current_coins += event_value
            print(f"You earned {event_value} coins.")

        else:
            current_energy += 50
            print("You had to rest!")

    else:
        if current_coins >= event_value:
            current_coins -= event_value
            print(f"You bought {type_of_event}.")

        else:
            bakery_is_open = False
            print(f"Closed! Cannot afford {type_of_event}.")
            break
        
if bakery_is_open:
    print("Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")