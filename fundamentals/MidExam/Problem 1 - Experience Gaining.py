needed_xp = float(input())
battles_count = int(input())
counter = 0

for _ in range(battles_count):
    counter += 1
    xp_per_battle = float(input())
    if counter % 15 == 0:
        xp_per_battle += 0.05 * xp_per_battle
    elif counter % 5 == 0:
        xp_per_battle -= 0.1 * xp_per_battle
    elif counter % 3 == 0:
        xp_per_battle += 0.15 * xp_per_battle
    needed_xp -= xp_per_battle

    if needed_xp <= 0:
        result = f"Player successfully collected his needed experience for {counter} battles."
        break
else: # he was not able to do it:
    result = f"Player was not able to collect the needed experience, {needed_xp:.2f} more needed."

print(result)


#Problem 1 - Experience Gaining

