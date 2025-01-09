gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    
    parts = command.split()
    action = parts[0]
    
    if action == "OutOfStock":
        gift = parts[1]
        gifts = ["None" if g == gift else g for g in gifts]
    
    elif action == "Required":
        gift = parts[1]
        index = int(parts[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift
    
    elif action == "JustInCase":
        gift = parts[1]
        gifts[-1] = gift

print(" ".join(g for g in gifts if g != "None"))