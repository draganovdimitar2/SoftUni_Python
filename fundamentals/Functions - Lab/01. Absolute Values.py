def absolute_value(user_input):
    return [abs(x) for x in float_numbers]

user_input = input().split()
float_numbers = map(float, user_input)
print(absolute_value(user_input))