#  build the matrix using nested list comprehension
matrix = [[int(el) for el in input().split(', ')]for row in range(int(input()))]
#  flatten the matrix using list comprehension
flatten_matrix = [num for row in matrix for num in row]
print(flatten_matrix)
