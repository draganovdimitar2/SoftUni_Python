n = int(input())
total = 0

for orders in range(n):

    price = float(input())
    days = int(input())
    capsules_day = int(input())

    if price < 0.01 or price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_day < 1 or capsules_day > 2000:
        continue

    per_coffee = (capsules_day * price) * days
    total += per_coffee
    print(f'The price for the coffee is: ${per_coffee:.2f}')

print(f'Total: ${total:.2f}')