def binary_search(numbers, t):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid_index = (left + right) // 2

        mid_el = numbers[mid_index]
        if mid_el == target:
            return mid_index
        if mid_el < t:
            left = mid_index + 1
        else:
            right = mid_index - 1

    return -1  # if an error arise


nums = [int(x) for x in input().split()]
target = int(input())
print(binary_search(nums, target))
