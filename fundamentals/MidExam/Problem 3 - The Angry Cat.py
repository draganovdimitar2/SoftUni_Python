def sum_left(price_ratings, entry_point, items_type, entry_point_num):
    if items_type == 'cheap':
        left_part = [num for num in price_ratings[:entry_point] if num < entry_point_num]
    else:  # expensive
        left_part = [num for num in price_ratings[:entry_point] if num >= entry_point_num]
    return sum(left_part)


def sum_right(price_ratings, entry_point, items_type, entry_point_num):
    if items_type == 'cheap':
        right_part = [num for num in price_ratings[entry_point+1:] if num < entry_point_num]
    else:  # expensive
        right_part = [num for num in price_ratings[entry_point+1:] if num >= entry_point_num]
    return sum(right_part)


price_ratings = list(map(int,input().split(', ')))
entry_point = int(input())
items_type = input()  # cheap or expensive
entry_point_num = price_ratings[entry_point]
sum_of_the_left_part = sum_left(price_ratings, entry_point, items_type, entry_point_num)
sum_of_the_right_part = sum_right(price_ratings, entry_point, items_type, entry_point_num)
if sum_of_the_right_part > sum_of_the_left_part:
    print(f"Right - {sum_of_the_right_part}")
else:  # If both sums are equal or left sum is bigger --> print the left one.
    print(f"Left - {sum_of_the_left_part}")




