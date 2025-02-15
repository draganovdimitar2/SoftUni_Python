from collections import deque

substances = [int(x) for x in input().split(', ')]  # stack
crystals = deque([int(x) for x in input().split(', ')])  # queue

potions = {
    110: "Brew of Immortality",
    100: "Essence of Resilience",
    90: "Draught of Wisdom",
    80: "Potion of Agility",
    70: "Elixir of Strength"
}

made_potions = []
while potions and substances and crystals:
    substance = substances.pop()
    crystal = crystals.popleft()
    total_sum = substance + crystal

    if total_sum in potions:  # if the sum is equal to one of the potions
        made_potions.append(
            potions.pop(total_sum))  # remove the potion from the dict and append it to the already made potions
    else:
        for key in potions:  # iterate in desc order keys
            if key < total_sum:  # if the key is smaller we make the potion
                made_potions.append(potions.pop(key))
                crystal -= 20
                if crystal > 0:
                    crystals.append(crystal)
                break
        else:  # if there is no such potion
            crystal -= 5
            if crystal > 0:
                crystals.append(crystal)

if potions:
    print("The alchemist failed to complete his quest.")
else:
    print("Success! The alchemist has forged all potions!")

if made_potions:
    print(f"Crafted potions: {', '.join(made_potions)}")

if substances:
    print(f"Substances: {', '.join((str(el) for el in reversed(substances)))}")

if crystals:
    print(f"Crystals: {', '.join((str(el) for el in crystals))}")
