def int_list(user_input):
    new_list = map(int, user_input)
    return sorted(new_list)


user_input = input().split()
print(int_list(user_input))