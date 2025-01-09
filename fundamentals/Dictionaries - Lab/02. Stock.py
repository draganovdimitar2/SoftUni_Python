availiable_products = input().split(' ')
searched_products = input().split(' ')
items_in_stock = {}

for i in range(0, len(availiable_products), 2):
    product = availiable_products[i]
    quantity = availiable_products[i+1]
    items_in_stock[product] = int(quantity)

for product in searched_products:
    if product in availiable_products:
        print(f"We have {items_in_stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
