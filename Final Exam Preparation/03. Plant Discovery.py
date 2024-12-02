def rate(plant: str, rating: float, plants_rating: dict):
    if plant in plants_rating:
        plants_rating[plant].append(rating)
    else:
        plants_rating[plant] = [rating]


n = int(input())
plants_rarity = {}
plants_rating = {}

for _ in range(n):
    info = input().split('<->')
    plant, rarity = info[0], int(info[1])
    plants_rarity[plant] = rarity
    if plant not in plants_rating:
        plants_rating[plant] = []

while True:
    command = input()
    if command == "Exhibition":
        break

    try:
        action, details = command.split(': ')
        if action == "Rate":
            plant, rating = details.split(' - ')
            if plant not in plants_rarity:
                print("error")
                continue
            rate(plant, float(rating), plants_rating)
        elif action == "Update":
            plant, new_rarity = details.split(' - ')
            if plant not in plants_rarity:
                print("error")
                continue
            plants_rarity[plant] = int(new_rarity)
        elif action == "Reset":
            plant = details
            if plant not in plants_rarity:
                print("error")
                continue
            plants_rating[plant] = []  # Reset ratings to empty
        else:
            print("error")
    except (ValueError, IndexError):
        print("error")

print("Plants for the exhibition:")
for plant, rarity in plants_rarity.items():
    ratings = plants_rating.get(plant, [])
    average_rating = sum(ratings) / len(ratings) if ratings else 0
    print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")
