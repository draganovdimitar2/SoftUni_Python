money_as_string = input().split(', ')
number_of_beggars = int(input())
money_as_integer = [int(money) for money in money_as_string]
start_index = 0
list_with_beggars_sum = []

for beggar in range(number_of_beggars):
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_integer), number_of_beggars):
        current_beggar_sum += money_as_integer[current_index]
    list_with_beggars_sum.append(current_beggar_sum)
    start_index += 1

print(list_with_beggars_sum)