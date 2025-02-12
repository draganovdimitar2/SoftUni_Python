def calc_sum(some_nums, i=0):
    if i == len(some_nums) - 1:
        return some_nums[i]
    return calc_sum(some_nums, i + 1) + some_nums[i]


num = list(map(int, input().split()))
print(calc_sum(num))
