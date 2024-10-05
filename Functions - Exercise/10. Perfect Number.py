def perfect_num(a):
    sum_numbers = 0

    for num in range(1, a):  # not including 'a'
        if a%num==0:
            sum_numbers += num

    if sum_numbers == a:
        return'We have a perfect number!'
    return "It's not so perfect."

a = int(input())
print(perfect_num(a))