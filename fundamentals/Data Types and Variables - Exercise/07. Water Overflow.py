capacity = 255
total_liters = 0
lines = int(input())

for _ in range(lines):
    liters = int(input())
    total_liters += liters

    if total_liters > capacity:
        print("Insufficient capacity!")
        total_liters -= liters

print(total_liters)