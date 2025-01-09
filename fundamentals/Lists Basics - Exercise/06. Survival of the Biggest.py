numbers_list = input().split()
count_for_remove = int(input())
numbers_int = [int(num) for num in numbers_list]

for num in range(count_for_remove):
    removed_num = min(numbers_int)
    numbers_int.remove(removed_num)

print(', '.join(str(num) for num in numbers_int))