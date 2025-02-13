def selection_sort(nums):
    for idx in range(len(nums)):
        min_idx = idx
        for curr_idx in range(idx + 1, len(nums)):
            if nums[curr_idx] < nums[min_idx]:
                min_idx = curr_idx

        nums[idx], nums[min_idx] = nums[min_idx], nums[idx]  # swap their positions
    return ' '.join(str(num) for num in nums)


numbers = [int(x) for x in input().split()]
print(selection_sort(numbers))
