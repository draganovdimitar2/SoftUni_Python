num = int(input())

for current_num in range(1, num + 1):
    sum_of_digits = sum(int(digit) for digit in str(current_num))
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f'{current_num} -> True')
    else:
        print(f'{current_num} -> False')
