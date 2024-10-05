def even_numbers(user_input):
    user_input = list(map(int, user_input))
    return list(filter(lambda x: x % 2 == 0, user_input))


user_input = input().split()
print(even_numbers(user_input))