storage = {}
command = input()
while command != 'buy':
    product, price, quantity = command.split(' ')
    price = float(price)
    quantity = int(quantity)

    if product not in storage:
        storage[product] = {"price": price, "quantity": quantity}
    else:
        storage[product]["quantity"] += quantity
        storage[product]["price"] = price  # we replace the price always

    command = input()

for product, details in storage.items():
    total_price = details['quantity'] * details['price']
    print(f'{product} -> {total_price:.2f}')
