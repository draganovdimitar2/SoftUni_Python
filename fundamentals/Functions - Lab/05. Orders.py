my_dict = {'coffee':1.5, 'water':1, 'coke':1.4, 'snacks':2}

def calculate(quantity, my_input):
    price = f'{my_dict[my_input] * quantity:.2f}'
    print(price)

my_input = input()
quantity = int(input())
calculate(quantity, my_input)