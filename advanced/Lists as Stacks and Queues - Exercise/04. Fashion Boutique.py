clothes = list(map(int, input().split()))  # [int(x) for x in input.split()]
capacity = int(input())
current_capacity = capacity
counter = 1

while clothes:
    clothing = clothes.pop()  # LIFO (popping from our stack)
    if clothing <= current_capacity:
        current_capacity -= clothing
    else:
        counter += 1
        current_capacity = capacity
        current_capacity -= clothing

print(counter)
