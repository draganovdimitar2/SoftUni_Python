def insertion_sort(nums):
    for j in range(1, len(nums)):
        for i in range(j, 0, -1):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            else:
                break

    return ' '.join(str(num) for num in nums)


numbers = [int(x) for x in input().split()]
print(insertion_sort(numbers))
