def check(crops,crop):
    if crop in crops:
        return True
    return False


crops = input().split(' & ')
while True:
    command = input()
    if command == "Collect!":
        break
    command = command.split()
    action = command[0]
    crop = command[1]
    if action == 'Plant':
        if not check(crops, crop):
            crops.insert(0, crop)
    elif action == 'Transplant':
        if check(crops, crop):
            crops.remove(crop)  # first i will remove it
            crops.append(crop)  # then i will append the crop so it will be the last element in our list
    elif action == 'Replace':
        index_one = int(crop)
        index_two = int(command[2])
        if index_one in range(0, len(crops)) and index_two in range(0, len(crops)):
            crops[index_one], crops[index_two] = crops[index_two], crops[index_one]
    elif action == 'Uproot':
        if check(crops, crop):
            crops.remove(crop)

print(" | ".join(crops))



