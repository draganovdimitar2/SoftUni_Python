def bubble_sort(nums):
    is_sorted = False
    sorted_elements = 0

    while not is_sorted:
        is_sorted = True
        for j in range(1, len(nums) - sorted_elements):
            i = j - 1
            if nums[i] > nums[j]:
                is_sorted = False
                nums[i], nums[j] = nums[j], nums[i]
        sorted_elements += 1

    return ' '.join(str(num) for num in nums)


numbers = [int(x) for x in input().split()]
print(bubble_sort(numbers))
