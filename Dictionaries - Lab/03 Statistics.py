command = input()
items_in_stock = {}

while command != 'statistics':
    command = command.split(': ')
    for i in range(0, len(command), 2):
        product = command[i]
        quantity = int(command[i+1])
        if product in items_in_stock:
            items_in_stock[product] += quantity
        else:
            items_in_stock[product] = quantity

    command = input()

print("Products in stock:")
for key, value in items_in_stock.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(items_in_stock.keys())}')
print(f"Total Quantity: {sum(items_in_stock.values())}")
