def min_max_sum(user_input):
    print(f"The minimum number is {min(int_num)}")
    print(f"The maximum number is {max(int_num)}")
    print(f"The sum number is: {sum(int_num)}")


user_input = input().split()
int_num = list(map(int,user_input))
min_max_sum(user_input)