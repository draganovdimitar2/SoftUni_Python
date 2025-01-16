first_set = set(map(int, input().split()))
second_set = set(map(int, input().split()))
num = int(input())

for _ in range(num):
    command = input().split()
    first_action = command[0]
    second_action = command[1]

    if first_action == 'Add':
        numbers = set(map(int, command[2:]))
        if second_action == 'First':
            first_set.update(numbers)
        else:
            second_set.update(numbers)
    elif first_action == 'Remove':
        numbers = set(map(int, command[2:]))
        if second_action == 'First':
            first_set.difference_update(numbers)
        else:
            second_set.difference_update(numbers)
    else:
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

print(f"{', '.join(map(str, sorted(first_set)))}")
print(f"{', '.join(map(str, sorted(second_set)))}")
