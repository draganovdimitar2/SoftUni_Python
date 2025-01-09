numbers = input()
number_list = [int(num) for num in numbers.split(", ")]
even_indices = [index for index, num in enumerate(number_list) if num % 2 == 0]
print(even_indices)
